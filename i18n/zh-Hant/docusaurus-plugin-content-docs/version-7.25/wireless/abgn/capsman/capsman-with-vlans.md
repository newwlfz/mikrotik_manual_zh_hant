---
sidebar_key: "wireless/abgn/capsman/capsman-with-vlans"
sidebar_position: 2
title: "CAPsMAN 與 VLAN"
sidebar_label: "CAPsMAN 與 VLAN"
description: "本頁介紹在 MikroTik RouterOS 中配置 CAPsMAN 與 VLAN，實現對不同用戶端組的集中式無線管理和 VLAN 標記。內容涵蓋本地轉發模式設定、Provisioning 規則、DHCP 配置以及交換器上的 VLAN 過濾。"
tags:
  - 'capsman'
  - 'vlan'
  - 'bridging'
source: https://manual.mikrotik.com/docs/7.25/wireless/abgn/capsman/capsman-with-vlans
captured_at: '2026-11-04T11:23:52+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

可以為家庭或辦公環境建立可擴充套件到許多接入點的集中式接入點管理設定。此類設定配置起來相當簡單，並已在[簡單的 CAPsMAN 設定](./ap-controller-capsman.md#simple-setup-of-a-capsman-system)指南中說明，但對於更復雜的設定，可能需要 VLAN。CAPsMAN 具備在某些條件下分配特定 VLAN ID 的功能。本指南將提供一個示例，說明如何根據無線用戶端連線到的 AP，為無線封包分配 VLAN ID。帶 VLAN 的 CAPsMAN 可以透過使用[本地轉發模式](./ap-controller-capsman.md#local-forwarding-mode)或 [CAPsMAN 轉發模式](./ap-controller-capsman.md#manager-forwarding-mode)來實現；本地轉發模式提供了在 AP 與 CAPsMAN 路由器之間使用交換器來交換封包的可能性（以獲得更大的吞吐量），而當所有流量都應始終轉發到 CAPsMAN 路由器時（大多數情況下是為了過濾封包），則應使用 CAPsMAN 轉發模式。

在此示例中，如果無線用戶端連線到 **WiFi\_WORK**，我們會將所有無線用戶端分配到 **VLAN10**；如果無線用戶端連線到 **WiFi\_GUEST**，我們會將其分配到 **VLAN20**。我們將結合使用虛擬 AP 和 CAPsMAN，在單個物理裝置上為無線用戶端建立多個要連線的 SSID。還將透過使用 CAPsMAN 預配規則展示如何為單個物理裝置使用單個 SSID 的示例。

## 使用本地轉發模式 {#using-local-forwarding-mode}

![](/img/aa0be2c197777367.webp)

在本地轉發模式中，CAPsMAN 路由器會將配置分發到由 CAPsMAN 路由器預配的所有 CAP。在本地轉發模式中，流量不需要傳送到 CAPsMAN 路由器，而是在轉發流量時可以傳送到另一臺路由器而不涉及 CAPsMAN 路由器。此模式允許你在流量從無線用戶端傳送到你的網路之前，用特定 VLAN ID 標記流量，這就增加了使用交換器將特定 VLAN ID 限制到特定埠的可能性。在本地轉發模式中，流量不會使用特殊的 CAPsMAN 報頭進行封裝，而該報頭只能由 CAPsMAN 路由器移除。

### CAPsMAN 路由器 {#capsman-router}

- 為每個 VLAN 建立相應的 CAP 配置：

```
/caps-man/configuration
add country=latvia datapath.local-forwarding=yes datapath.vlan-id=10 datapath.vlan-mode=use-tag name=Config_WORK security.authentication-types=wpa-psk,wpa2-psk \
    security.passphrase=secret_work_password ssid=WiFi_WORK
add country=latvia datapath.local-forwarding=yes datapath.vlan-id=20 datapath.vlan-mode=use-tag name=Config_GUEST security.authentication-types=\
    wpa-psk,wpa2-psk security.passphrase=secret_guest_password ssid=WiFi_GUEST
```

- 我們將建立一條 CAPsMAN 預配規則，以在單個裝置上建立 **WiFi\_WORK** 和 **WiFi\_GUEST** SSID，並且每個已連線的 CAP 都會自動建立這些 SSID。

```
/caps-man/provisioning
add action=create-dynamic-enabled master-configuration=Config_WORK slave-configurations=Config_GUEST
```

:::info
你可以透過新增多個 slave-configurations 來建立更多虛擬 AP。這需要事先建立多個 CAPsMAN 配置。
:::

- 出於安全原因，將 CAPsMAN 限制為單個介面：

```
/caps-man/manager/interface
set [ find default=yes ] forbid=yes
add disabled=no interface=ether1
```

- 啟用 CAPsMAN 管理器：

```
/caps-man/manager
set enabled=yes
```

- 為每個 VLAN 設定 DHCP 伺服器：

```
/interface/vlan
add interface=ether1 name=VLAN10 vlan-id=10
add interface=ether1 name=VLAN20 vlan-id=20
/ip/address
add address=192.168.10.1/24 interface=VLAN10
add address=192.168.20.1/24 interface=VLAN20
/ip/pool
add name=dhcp_pool10 ranges=192.168.10.2-192.168.10.254
add name=dhcp_pool20 ranges=192.168.20.2-192.168.20.254
/ip/dhcp-server
add address-pool=dhcp_pool10 disabled=no interface=VLAN10 name=dhcp10
add address-pool=dhcp_pool20 disabled=no interface=VLAN20 name=dhcp20
/ip/dhcp-server/network
add address=192.168.10.0/24 dns-server=8.8.8.8 gateway=192.168.10.1
add address=192.168.20.0/24 dns-server=8.8.8.8 gateway=192.168.20.1
```

### 交換器 {#switch}

在此示例中，我們將使用[網橋 VLAN 過濾](../../../bridging-and-switching/index.md#vlan-example-trunk-and-access-ports)來過濾未知 VLAN，並將其他裝置分配到相同的網路。某些裝置能夠將此功能解除安裝到內建交換器晶片，請參閱[基本 VLAN 交換](../../../bridging-and-switching/user-guides/basic-vlan-switching.md)指南，瞭解如何在不同型別的裝置上進行配置。

- 設定網橋 VLAN 過濾：

```
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4 pvid=10
add bridge=bridge1 interface=ether5 pvid=20
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1,ether2,ether3 untagged=ether4 vlan-ids=10
add bridge=bridge1 tagged=ether1,ether2,ether3 untagged=ether5 vlan-ids=20
```

:::info
在此示例中，將使用未標記流量在 CAP 與 CAPsMAN 路由器之間通訊。預設情況下，如果未更改 PVID，未標記流量將在設定了相同 PVID 值（包括預設 PVID）的埠之間轉發。
:::

### CAPs {#caps}

- 建立網橋並將連線到 CAPsMAN 路由器的埠分配到該網橋：

```
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1
```

- 在 AP 上啟用 CAP 模式，並確保指定使用新建的網橋：

```
/interface/wireless/cap
set bridge=bridge1 discovery-interfaces=bridge1 enabled=yes interfaces=wlan1
```

- CAP 成功連線到 CAPsMAN 路由器後，wlan1（SSID 為 **WiFi\_WORK**）和新建立的虛擬 wlan5（SSID 為 **WiFi\_GUEST**）介面會作為網橋埠動態新增。VLAN 會分配給無線介面，因此來自無線的所有資料都會被標記，並且只有帶有此標記的資料才會透過無線傳送出去。如果不需要額外的 VLAN 管理和控制，可以停用網橋 vlan-filtering。關聯的 VLAN 可以透過埠 VLAN ID (PVID) 屬性檢視：

```
[admin@CAP_1] /interface/bridge/port/pr
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                     BRIDGE                    HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0   H ether1                        bridge1                   yes    1     0x80         10                 10       none
 1  D  wlan1                         bridge1                         10     0x80         10                 10       none
 2  D  wlan5                         bridge1                         20     0x80         10                 10       none
```

就是這樣！將無線用戶端連線到你的 AP，並檢查連通性。

## 使用 CAPsMAN 轉發模式 {#using-capsman-forwarding-mode}

![](/img/f246b0cbdbda83ed.webp)

在 CAPsMAN 轉發模式中，來自 CAP 的所有流量都會使用特殊的 CAPsMAN 報頭進行封裝，而該報頭只能由 CAPsMAN 路由器移除。這意味著交換器將無法區分由 CAP 設定的 VLAN ID，因為 VLAN 標記也會被封裝。此模式限制了在二層網路中分流流量的可能性，但使你能夠透過三層網路轉發來自每個 CAP 的流量，以便遠端的 CAPsMAN 路由器處理這些流量。當你想要控制遠端位置的多個 CAP，但又想使用集中式閘道器時，此模式很有用。

### CAPsMAN 路由器 {#capsman-router-1}

- 設定網橋 VLAN 過濾，以將介面限制到相應的 VLAN：

```
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1 pvid=10
add bridge=bridge1 interface=ether2 pvid=20
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1 untagged=ether1 vlan-ids=10
add bridge=bridge1 tagged=bridge1 untagged=ether2 vlan-ids=20
```

:::info
 CAPsMAN 會將 CAP 介面附加到網橋，並自動向網橋 VLAN 表中新增相應的條目。
:::

- 為每個 VLAN 建立相應的 CAP 配置：

```
/caps-man/configuration
add country=latvia datapath.bridge=bridge1 datapath.vlan-id=10 datapath.vlan-mode=use-tag name=Config_WORK security.authentication-types=wpa-psk,wpa2-psk \
    security.passphrase=secret_work_password ssid=WiFi_WORK
add country=latvia datapath.bridge=bridge1 datapath.vlan-id=20 datapath.vlan-mode=use-tag name=Config_GUEST security.authentication-types=wpa-psk,wpa2-psk \
    security.passphrase=secret_guest_password ssid=WiFi_GUEST
```

- 我們將建立一條 CAPsMAN 預配規則，以在單個裝置上建立 **WiFi\_WORK** 和 **WiFi\_GUEST** SSID，每個已連線的 CAP 都會自動建立這些 SSID

```
/caps-man/provisioning
add action=create-dynamic-enabled master-configuration=Config_WORK slave-configurations=Config_GUEST
```

:::info
你可以透過新增多個 slave-configurations 來建立更多虛擬 AP。這需要事先建立多個 CAPsMAN 配置。
:::

- 出於安全原因，將 CAPsMAN 限制為 CAP 將要連線的介面：

```
/caps-man/manager/interface
set [ find default=yes ] forbid=yes
add disabled=no interface=ether3
add disabled=no interface=ether4
```

- 啟用 CAPsMAN 管理器：

```
/caps-man/manager
set enabled=yes
```

- 為每個 VLAN 設定 DHCP 伺服器：

```
/interface/vlan
add interface=bridge1 name=VLAN10 vlan-id=10
add interface=bridge1 name=VLAN20 vlan-id=20
/ip/address
add address=192.168.10.1/24 interface=VLAN10
add address=192.168.20.1/24 interface=VLAN20
/ip/pool
add name=dhcp_pool10 ranges=192.168.10.2-192.168.10.254
add name=dhcp_pool20 ranges=192.168.20.2-192.168.20.254
/ip/dhcp-server
add address-pool=dhcp_pool10 disabled=no interface=VLAN10 name=dhcp10
add address-pool=dhcp_pool20 disabled=no interface=VLAN20 name=dhcp20
/ip/dhcp-server/network
add address=192.168.10.0/24 dns-server=8.8.8.8 gateway=192.168.10.1
add address=192.168.20.0/24 dns-server=8.8.8.8 gateway=192.168.20.1
```

### CAPs {#caps-1}

- 在每個 AP 上啟用 CAP 模式，並指定哪個介面連線到 CAPsMAN 路由器：

```
/interface/wireless/cap
set discovery-interfaces=ether1 enabled=yes interfaces=wlan1
```

- CAP 成功連線到 CAPsMAN 路由器後，CAPsMAN 路由器上會動態建立兩個 CAP 介面。由於透過 datapath.bridge=bridge1 顯式選擇了網橋介面，並且使用預設的 CAPsMAN 轉發模式 datapath.local-forwarding=no，這兩個介面都會作為網橋埠動態新增到同一臺 CAPsMAN 路由器上。由於使用了啟用了 vlan-filtering 的網橋，這兩個 CAP 介面也會顯示在網橋 VLAN 表中：

```
[admin@CAPsMAN_Router] /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                       BRIDGE                      HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0     ether1                          bridge1                     yes   10     0x80         10                 10       none
 1     ether2                          bridge1                     yes   20     0x80         10                 10       none
 2  D  cap16                           bridge1                           10     0x80         10                 10       none
 3  D  cap17                           bridge1                           20     0x80         10                 10       none
[admin@CAPsMAN_Router] /interface/bridge/vlan/print
Flags: X - disabled, D - dynamic 
 #   BRIDGE                         VLAN-IDS  CURRENT-TAGGED                         CURRENT-UNTAGGED                        
 0 D bridge1                        1                                                bridge1                                 
 1   bridge1                        10        cap16                                  ether1                                  
 2   bridge1                        20        cap17                                  ether2  
```

就是這樣！將無線用戶端連線到你的 AP，並檢查連通性。

## 案例研究 {#case-studies}

### 不使用虛擬 AP {#without-virtual-aps}

並非每個人都想建立虛擬 AP，因為這會降低總吞吐量。如果你想使用多臺裝置來建立多個 SSID，則可以根據 CAP 的身份為其分配特定配置。為此，應結合使用 CAPsMAN 預配規則和 RegEx 表示式。在此示例中，我們會將 **Config\_WORK** 配置分配給身份設定為 "'**AP\_WORK\_\***" 的 CAP，並將 **Config\_GUEST** 配置分配給身份設定為 "**AP\_GUEST\_\***" 的 CAP。為此，你只需更改 CAPsMAN 預配規則。

- 移除任何現有的預配規則：

```
/caps-man/provisioning/remove [f]
```

- 建立新的預配規則，根據 CAP 的身份為其分配相應的配置：

```
/caps-man/provisioning
add action=create-dynamic-enabled identity-regexp=^AP_GUEST_ master-configuration=Config_GUEST
add action=create-dynamic-enabled identity-regexp=^AP_WORK_ master-configuration=Config_WORK
```

:::note
不要忘記在 CAP 上設定正確的身份，因為 CAPsMAN 將根據其身份在 AP 上分配相應的配置。
:::
