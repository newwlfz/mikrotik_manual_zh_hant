---
sidebar_key: "wireless/w60g/fail-over-ptmp-cli-example"
sidebar_position: 2
title: "故障切換 PtMP CLI 示例"
sidebar_label: "故障切換 PtMP CLI 示例"
description: "本頁面提供了一份分步 CLI 指南，用於使用 MikroTik RouterOS 配置 60Ghz 與 5Ghz 無線鏈路之間的自動故障切換，包括網橋設定、介面繫結以及 W60G 裝置連線說明。"
tags:
  - 'bridging'
  - 'bonding'
source: https://manual.mikrotik.com/docs/7.24/wireless/w60g/fail-over-ptmp-cli-example
captured_at: '2026-11-04T11:35:39+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 概述 {#summary}

本示例展示如何在 CLI 中配置自動故障轉移（bonding）5GHz 鏈路，並與 60GHz 裝置配合使用。  
當 60GHz 無線連線中斷時，它會自動使用 bonding 介面。  
本示例在空配置狀態下使用 [[WinBox](https://mikrotik.com/download)] 工具完成

### 逐步連線到裝置 {#connect-to-the-device-step-by-step}

- 配置重設後，只能使用 mac-telnet。
   透過連線到裝置的 MAC 地址來連線裝置，或使用 WinBox New terminal 執行以下命令來查詢 W60G 裝置的 MAC 地址：

```ros
/ip/neighbor/print
```

- 要連線到 W60G 裝置，請執行命令：

```ros
/tool/mac-telnet/mac-address
```

- 輸入使用者名稱和密碼。預設使用者名稱為 **admin**，密碼為空或印在裝置標籤上。

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
admin@MikroTik] > /interface/bridge/print
Flags: X - disabled, R - running
 0 R name="bridge" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=1A:7F:BB:41:B0:94 protocol-mode=rstp  fast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6  vlan-filtering=no dhcp-snooping=no
```

### 設定 60GHz 無線連線 {#set-up-60ghz-wireless-connection}

前面說明的所有步驟與 Bridge 和 Station 裝置相同。配置無線介面時需要使用不同的模式。  
  
#### 對於 ap-bridge 裝置 {#for-ap-bridge-device}

- 選擇 SSID、Password、frequency，並選擇將在此設定中充當 **ap-bridge** 的 bridge 模式選項，請參見示例。
- 設定所需引數後啟用 W60G 介面。

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=ap-bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=no
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=ap-bridge ssid="MySSID"  frequency=auto default-scan-list=58320,60480,62640,64800 password="choosepassword" tx-sector=auto put-stations-in-bridge=none isolate-stations=no
[admin@MikroTik] > /interface/w60g/enable wlan60-1 
```

#### 對於 station 裝置 {#for-station-devices}

- 選擇與 bridge 裝置相同的 SSID、Password 和 frequency，並選擇將在此設定中充當 **station** 的 station-bridge 模式選項，請參見示例。
- 最多可將 8 臺 station 裝置連線到單個 AP 以充當故障轉移。
- 設定所需引數後啟用 W60G 介面。

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=station-bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=no
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=station-bridge ssid="MySSID" frequency=auto default-scan-list=58320,60480,62640,64800password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=no
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```

### 設定 5GHz 無線連線 {#set-up-5ghz-wireless-connection}

#### 對於 ap-bridge 裝置 {#for-ap-bridge-device-1}

- 選擇 SSID、Password、frequency，並選擇將在此設定中充當 **bridge** 的 bridge 模式選項，請參見示例。
- 設定所需引數後啟用 5GHz 介面。

```ros
[admin@MikroTik] > /interface/wireless/security-profiles/set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword
[admin@MikroTik] > /interface/wireless/set wlan1 frequency=auto scan-list=default installation=outdoor mode=ap-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac
[admin@MikroTik] > /interface/wireless/enable wlan1 
```

#### 對於 station 裝置 {#for-station-devices-1}

- 選擇與 bridge 裝置相同的 SSID、Password、frequency，並選擇將在此設定中充當 **station** 的 station-bridge 模式選項。請參見示例。
- 最多可將 8 臺 station 裝置連線到單個 AP 以充當故障轉移。
- 設定所需引數後啟用 W60G 介面。

```ros
[admin@MikroTik] > /interface/wireless/security-profiles/set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword
[admin@MikroTik] > /interface/wireless/set wlan1 frequency=auto scan-list=default installation=outdoor mode=station-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac
[admin@MikroTik] > /interface/wireless/enable wlan1
```

### 為 Access Point 配置 bridge {#configure-bridge-for-access-point}

- 為 AP 配置 bridge，以確保 5GHz 作為故障轉移工作。需要將 **wlan1**、**ether1** 以及所有 60GHz **station 介面** 加入 bridge。
   *示例中僅顯示 2 臺 station 裝置，但最多可新增 8 臺裝置。*  

   對於 ap-bridge 裝置，請按如下方式設定 **configuration**：

```ros
[admin@MikroTik] > /interface/bridge/port/
add bridge=bridge hw=no interface=ether1
add bridge=bridge interface=wlan1
add bridge=bridge interface=wlan60-station-1
add bridge=bridge interface=wlan60-station-2
[admin@MikroTik] > interface/bridge/port/pr
# INTERFACE         BRIDGE  HW  PVID  PRIORITY  PATH-COST  INTERNAL-PATH-COST  HORIZON
0 ether1            bridge      no     1  0x80             10                  10  none
1 wlan1             bridge             1  0x80             10                  10  none
2 wlan60-station-1  bridge             1  0x80             10                  10  none
3 wlan60-station-2  bridge             1  0x80             10                  10  none 
```

### 為 station 裝置配置 bridge 和 bonding {#configure-bridge-and-bonding-for-station-devices}

- 配置 bonding 並分配從介面。在此設定中，選擇內建 wlan1 介面作為從介面，但在其他型別的設定中也可以使用 ether 介面。

   對於 station-bridge 裝置，請按如下方式設定 **bonding**：

```ros
[admin@MikroTik] > /interface/bonding/add mode=active-backup name=bond1 primary=wlan60-1 slaves=wlan60-1,wlan1
```

- 將介面成員（ether1 和 bond1）新增到新建的 bridge。

```ros
[admin@MikroTik] > /interface/bridge/port/add interface=ether1 bridge=bridge
[admin@MikroTik] > /interface/bridge/port/add interface=bond1  bridge=bridge
[admin@MikroTik] > /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload
#     INTERFACE                              BRIDGE                              HW   PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
0     ether1                                 bridge                             yes     1     0x80         10                 10       none
1     bond1                                  bridge                             yes     1     0x80         10                 10       none
```

### 其他配置 {#additional-configuration}

完成前面說明的所有步驟後，鏈路應已建立。建議在兩臺裝置上設定管理員密碼。

### 故障排除 {#troubleshooting}

透過執行以下命令檢查序列號和型號名稱等裝置設定，確保連線到了正確的裝置：

```ros
[admin@MikroTik] > /system/routerboard/print
```

如果 bridge 設定中的 wlan60-1 介面處於 inactive 狀態，並且已正確完成在裝置上啟用該介面的配置，請執行命令：

```ros
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```
