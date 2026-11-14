---
sidebar_key: "wireless/w60g/fail-over-ptp-cli-example"
sidebar_position: 3
title: "故障轉移 PtP CLI 示例"
sidebar_label: "故障轉移 PtP CLI 示例"
description: "本頁提供了一個分步 CLI 示例，用於透過 bonding 在 60Ghz 和 5Ghz 無線鏈路之間配置自動故障轉移，包括為橋接模式和站模式配置網橋以及 W60G 介面。"
tags:
  - 'bonding'
  - 'bridging'
  - 'wireless'
source: https://manual.mikrotik.com/docs/7.25/wireless/w60g/fail-over-ptp-cli-example
captured_at: '2026-11-04T11:24:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 概述 {#summary}

本示例展示如何在 CLI 中配置一條自動故障轉移（bonding）的 5Ghz 鏈路，並與 60Ghz 裝置配合使用。  
當 60Ghz 無線之間的連線丟失時，它將自動使用 bonding 介面。  
本示例在空配置狀態下使用 [[WinBox](https://mikrotik.com/download)] 實用程式完成。

### 逐步連線到裝置 {#connect-to-the-device-step-by-step}

- 配置重設後，只能使用 mac-telnet。
   透過連線到裝置的 MAC 地址來連線裝置，或使用 WinBox New terminal 執行以下命令來查詢 W60G 裝置的 MAC 地址：

```ros
/ip/neighbor/print
```

- 要連線到 W60G 裝置，請執行以下命令。

```ros
/tool/mac-telnet <MAC-ADDRESS>
```

- 輸入使用者名稱和密碼。預設情況下，使用者名稱是 **admin**，密碼為空或印在裝置標籤上：

```ros
[admin@KD_GW] > /tool/mac-telnet C4:AD:34:84:EE:5D
Login: admin
Password:
Trying C4:AD:34:84:EE:5D...
Connected to C4:AD:34:84:EE:5D
```

### 配置 bridge {#configure-bridge}

- 執行以下命令新增新的 bridge 併為其分配 bridge 成員：

```ros
/interface/bridge/add name=bridge
```

要檢查 bridge 是否已建立，請執行命令：

```ros
[admin@MikroTik] > /interface/bridge/print
Flags: X - disabled, R - running
 0 R name="bridge" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=1A:7F:BB:41:B0:94 protocol-mode=rstp  fast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6  vlan-filtering=no dhcp-snooping=no
```

### 設定 60GHz 無線連線 {#set-up-60ghz-wireless-connection}

前面說明的所有步驟與 Bridge 和 Station 裝置相同。配置無線介面時需要使用不同的模式。  

#### 對於網橋裝置 {#for-bridge-device}

- 選擇 SSID、密碼、頻率，並選擇 bridge 模式選項，使其在設定中充當 **網橋**。請參見示例。
- 設定所需引數後，啟用 W60G 介面。

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=yes
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=bridge ssid="MySSID"  frequency=auto default-scan-list=58320,60480,62640,64800 password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=yes
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```

#### 對於站點裝置 {#for-station-device}

- 選擇與網橋裝置相同的 SSID、密碼和頻率，並選擇 station-bridge 模式選項，使其在設定中充當 **站點**，請參見示例。
- 設定所需引數後，啟用 W60G 介面。

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=station-bridge frequency=auto ssid=MySSID password=choosepassword
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=station-bridge ssid="MySSID" frequency=auto default-scan-list=58320,60480,62640,64800password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=yes
[admin@MikroTik] > /interface/w60g/enable wlan60-1 
```

### 設定 5GHz 無線連線 {#set-up-5ghz-wireless-connection}

#### 對於網橋裝置 {#for-bridge-device-1}

- 選擇 SSID、密碼、頻率，並選擇 bridge 模式選項，使其在設定中充當 **網橋**，請參見示例。
- 設定所需引數後，啟用 5GHz 介面。

```ros
[admin@MikroTik] > /interface/wireless/security-profiles/set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword
[admin@MikroTik] > /interface/wireless/set wlan1 frequency=auto scan-list=default installation=outdoor mode=bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac
[admin@MikroTik] > /interface/wireless/enable wlan1 
```

#### 對於站點裝置 {#for-station-device-1}

- 選擇與網橋裝置相同的 SSID、密碼和頻率，並選擇 station-bridge 模式選項，使其在設定中充當 **站點**。請參見示例。
- 設定所需引數後，啟用 W60G 介面。

```ros
[admin@MikroTik] > /interface/wireless/security-profiles/set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword
[admin@MikroTik] > /interface/wireless/set wlan1 frequency=auto scan-list=default installation=outdoor mode=station-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac
[admin@MikroTik] > /interface/wireless/enable wlan1 
```

### 配置網橋和 bonding {#configure-bridge-and-bonding}

- 配置 bonding 並分配從介面。在此設定中，它被選為內建的 wlan1 介面，但在其他型別的設定中也可以是 ether 介面。

   對於 *網橋* 裝置，請將 **bonding** 設定為：

```ros
[admin@MikroTik] > /interface/bonding/add comment=bondingbackup mode=active-backup name=bond1 primary=wlan60-station-1 slaves=wlan60-station-1,wlan1
```

&emsp;&emsp; 對於 *station-bridge* 裝置，請將 **bonding** 設定為：

```ros
[admin@MikroTik] > /interface/bonding/add comment=defconf mode=active-backup name=bond1 primary=wlan60-1 slaves=wlan60-1,wlan1
```

- 將介面成員（ether1 和 bond1）新增到新建的 bridge。

```ros
[admin@MikroTik] > /interface/bridge/port/add interface=ether1 bridge=bridge
[admin@MikroTik] > /interface/bridge/port/add interface=bond1  bridge=bridge
[admin@MikroTik] > /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload
#     INTERFACE                              BRIDGE                              HW   PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
0     ether1                                 bridge                             yes     1     0x80         10                 10       none
1     bond1                                  bridge                             yes     1     0x80         10                 10       none |
```

### 其他配置 {#additional-configuration}

完成前面說明的所有步驟後，鏈路應已建立。建議在兩臺裝置上設定管理員密碼。

### 故障排除 {#troubleshooting}

透過執行以下命令檢查序列號和型號名稱等裝置設定，確保連線到了正確的裝置：

```ros
[admin@MikroTik] > /system/routerboard/print
```

如果網橋設定中的 wlan60-1 介面處於非活動狀態，並且已正確完成配置以在裝置上啟用該介面，請執行以下命令：

```ros
[admin@MikroTik] > /interface/w60g/enable wlan60-1 
```
