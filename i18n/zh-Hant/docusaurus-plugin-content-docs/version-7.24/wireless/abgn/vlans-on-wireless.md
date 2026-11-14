---
sidebar_key: "wireless/abgn/vlans-on-wireless"
sidebar_position: 6
title: "無線網路上的 VLAN"
sidebar_label: "無線網路上的 VLAN"
description: "本頁介紹如何在 MikroTik RouterOS 無線介面上配置 VLAN，從而在不同 Virtual AP 與網路之間實現二層（Layer2）分段。文中包含使用 VLAN 介面隔離 Guest 與 Work AP 的配置示例、帶 VLAN filtering 的網橋配置，以及安全配置檔案（security profile）的設定。"
tags:
  - 'vlan'
  - 'bridge-vlan-filtering'
  - 'wireless'
source: https://manual.mikrotik.com/docs/7.24/wireless/abgn/vlans-on-wireless
captured_at: '2026-11-04T11:35:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

VLAN 可以將裝置隔離到不同的二層網段，同時仍然使用相同的物理層（Layer1）介質。在需要分離不同型別的裝置或使用者的場景中，這非常有用。該功能對於無線網路部署也非常有用，因為你可以隔離不同的虛擬 AP，並透過防火牆限制對特定服務或網路的訪問。下面是一個示例：在同一裝置上配置兩個接入點，並將它們隔離到不同的 VLAN 中。當你擁有 **Guest AP** 和 **Work AP** 時，這種場景非常常見。

## 示例 {#example}

![](/img/24db0ec92d966c8b.webp)

[網橋 VLAN 過濾](../../bridging-and-switching/index.md#bridge-vlan-filtering) 在網橋內提供 VLAN 感知的二層轉發和 VLAN 標籤修改。

### R1 {#r1}

- 在乙太網介面上新增必要的 VLAN 介面，使其成為 VLAN 幹道埠。在 VLAN 介面上新增 IP 地址：

```ros
/interface/vlan
add interface=ether1 name=vlan111 vlan-id=111
add interface=ether1 name=vlan222 vlan-id=222

/ip/address
add address=192.168.1.1/24 interface=vlan111
add address=192.168.2.1/24 interface=vlan222
```

### R2 {#r2}

- 在 wlan1 介面下新增 VirtualAP，併為 wlan1 和 wlan2 建立無線安全配置檔案：

```ros
/interface/wireless/security-profiles
add name=vlan111 authentication-types=wpa-psk,wpa2-psk mode=dynamic-keys wpa-pre-shared-key=secret111 wpa2-pre-shared-key=secret111
add name=vlan222 authentication-types=wpa-psk,wpa2-psk mode=dynamic-keys wpa-pre-shared-key=secret222 wpa2-pre-shared-key=secret222
/interface/wireless
set [ find default-name=wlan1 ] disabled=no mode=ap-bridge security-profile=vlan111 ssid=vlan111 vlan-id=111 vlan-mode=use-tag
add disabled=no master-interface=wlan1 name=wlan2 security-profile=vlan222 ssid=vlan222 vlan-id=222 vlan-mode=use-tag
```

:::info
將 wlan1、wlan2 的 vlan-mode 設定為 "use-tag" 很重要。
:::

- 建立一個網橋，並設定 *vlan-filtering=yes*；
- 新增必要的網橋埠；
- 在 *interface bridge vlan* 部分下新增 *tagged* 介面，並設定正確的 *vlan-ids*：

```ros
/interface/bridge
add fast-forward=no name=bridge1 vlan-filtering=yes

/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wlan1
add bridge=bridge1 interface=wlan2
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2,wlan1 vlan-ids=111
add bridge=bridge1 tagged=ether2,wlan2 vlan-ids=222
```

:::warning
某些裝置具有內建交換晶片，可以以線速效能在乙太網埠之間交換封包。網橋 VLAN 過濾會停用某些裝置的[硬體解除安裝](../../bridging-and-switching/index.md#bridge-hardware-offloading)，這將阻止封包被交換。這不會影響無線介面，因為透過無線介面的流量無論如何都無法解除安裝到交換晶片。
:::

:::tip
此設定中不要求使用 VLAN 過濾，但出於安全原因強烈建議啟用。在沒有 VLAN 過濾的情況下，某些場景中可能會轉發未知的 VLAN ID。停用 VLAN 過濾確實具有效能優勢。
:::

### R3 {#r3}

- 在 wlan1 介面上新增 IP 地址；
- 建立與 R2 wlan1 相容的無線安全配置檔案：

```ros
/ip/address
add address=192.168.1.3/24 interface=wlan1

/interface/wireless
set [ find default-name=wlan1 ] disabled=no mode=station security-profile=vlan111 ssid=vlan111
```

### R4 {#r4}

- 在 wlan1 介面上新增 IP 地址；
- 建立與 R2 wlan2 相容的無線安全配置檔案：

```ros
/ip/address
add address=192.168.2.4/24 interface=wlan1

/interface/wireless
set [ find default-name=wlan1 ] disabled=no mode=station security-profile=vlan222 ssid=vlan222
```
