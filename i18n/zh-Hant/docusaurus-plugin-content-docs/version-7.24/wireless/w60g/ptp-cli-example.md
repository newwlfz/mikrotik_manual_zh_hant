---
sidebar_key: "wireless/w60g/ptp-cli-example"
sidebar_position: 5
title: "PtP CLI 示例"
sidebar_label: "PtP CLI 示例"
description: "本頁面提供了一個分步 CLI 示例，用於在兩臺 MikroTik W60G 裝置之間配置透明無線網橋，包括透過 MAC-Telnet 連線、設定帶有介面成員的網橋，以及在網橋模式下建立無線連線。"
tags:
  - 'bridging'
  - 'wireless'
  - 'ptp'
source: https://manual.mikrotik.com/docs/7.24/wireless/w60g/ptp-cli-example
captured_at: '2026-11-04T11:35:42+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 概述 {#summary}

本示例展示如何在 CLI 中將一臺 W60G 裝置到另一臺 W60G 裝置配置為透明無線網橋。

本示例從空配置狀態開始，使用 [[WinBox](https://mikrotik.com/download)] 工具完成。

### 逐步連線到裝置 {#connect-to-the-device-step-by-step}

- 配置重設後 —— 只能使用 mac-telnet。
   透過連線到裝置的 MAC 地址來連線裝置，或使用 WinBox 新終端，透過執行以下命令查詢 W60G 裝置的 MAC 地址：

```ros
/ip/neighbor/print
```

- 要連線到 W60G 裝置，請執行以下命令：

```ros
/tool/mac-telnet/mac-address
```

- 輸入使用者名稱和密碼。預設使用者名稱為 **admin**，且未設定密碼：

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

&emsp;&emsp;   要檢查網橋是否已建立，請執行以下命令：

```ros
[admin@MikroTik] > /interface/bridge/print
Flags: X - disabled, R - running
0 R name="bridge" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=1A:7F:BB:41:B0:94 protocol-mode=rstp  fast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6  vlan-filtering=no dhcp-snooping=no
```

- 將介面成員（ether1 和 wlan60-1）新增到新建的網橋：

```ros
[admin@MikroTik] > /interface/bridge/port/add interface=ether1 bridge=bridge
[admin@MikroTik] > /interface/bridge/port/add interface=wlan60-1 bridge=bridge
[admin@MikroTik] > /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload
#     INTERFACE                              BRIDGE                              HW   PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
0     ether1                                 bridge                             yes     1     0x80         10                 10       none
1 I   wlan60-1                               bridge                                     1     0x80         10                 10       none
```

### 設定無線連線 {#set-up-wireless-connection}

前面說明的所有步驟與 Bridge 和 Station 裝置相同。配置無線介面時需要使用不同的模式。  
  
#### 對於網橋裝置 {#for-bridge-device}

- 選擇 SSID、密碼、頻率，並選擇 bridge 模式選項，該選項將在該設定中充當**網橋**，請參見示例；
- 設定所需引數後啟用 W60G 介面：

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=bridge frequency=auto ssid=MySSID password=choosepassword put-stations-in-bridge=bridge isolate-stations=yes
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running 
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=bridge ssid="MySSID"  frequency=auto default-scan-list=58320,60480,62640,64800 password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=yes
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```

#### 對於站點裝置 {#for-station-device}

- 選擇與網橋裝置相同的 SSID、密碼和頻率，並選擇 station-bridge 模式選項，該選項將在該設定中充當**站點**，請參見示例；
- 設定所需引數後啟用 W60G 介面：

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=station-bridge frequency=auto ssid=MySSID password=choosepassword
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running 
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=station-bridge  ssid="MySSID" frequency=auto default-scan-list=58320,60480,62640,64800 password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=yes
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```

### 其他配置 {#additional-configuration}

完成之前說明的所有步驟後，鏈路應已建立。建議在兩臺裝置上都設定管理員密碼。

### 故障排除 {#troubleshooting}

透過執行以下命令檢查序列號和型號名稱等裝置設定，確保連線到了正確的裝置：

```ros
[admin@MikroTik] > /system/routerboard/print
```

如果網橋設定中的 wlan60-1 介面處於非活動狀態，並且配置已正確完成，要在裝置上啟用該介面 —— 請執行以下命令：

```ros
[admin@MikroTik] > /interface/w60g/enable wlan60-1 
```
