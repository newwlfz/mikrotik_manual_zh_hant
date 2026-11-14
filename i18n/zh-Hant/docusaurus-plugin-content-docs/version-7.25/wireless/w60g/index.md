---
sidebar_key: "wireless/w60g/index"
sidebar_position: 6
title: "W60G"
sidebar_label: "W60G"
description: "本頁說明 MikroTik RouterOS W60G 無線介面配置，涵蓋 60GHz 點對點/點對多點鏈路的設定、ARP/MAC 設定、加密以及帶詳細統計監控的站點管理。"
tags:
  - 'w60g'
  - 'wireless'
  - 'arp'
source: https://manual.mikrotik.com/docs/7.25/wireless/w60g
captured_at: '2026-11-04T11:24:07+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 60 GHz 無線示例和指南。使用這些內容來配置 W60G 點對點與點對多點鏈路、故障轉移以及與距離相關的設定。

<DocCardList />

### 概述 {#summary}

**軟體包：** `system`,`wireless`

802.11ad 實現能夠在無線網路上提供千兆乙太網速度。

透過透明的 AES 加密無線 60GHz 鏈路擴充套件千兆網路，避免常見的有線或無線網路問題。

### 常規介面屬性 {#general-interface-properties}

**子選單：** `/interface/w60g`

:::warning
Wireless Wire kit 裝置以預配置、已連線的成對形式提供。手動配置是可選的
:::

| 屬性 | 描述 |
| :-- | :-- |
| **arp**（*disabled \| enabled \| proxy-arp \| reply-only*；預設值：**enabled**） | [`Read more >>`](../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together) |
| **arp-timeout** (*auto \| integer*; Default: **auto**) | ARP 超時是指在沒有從 IP 收到封包後，ARP 記錄在 ARP 表中保留多長時間。值 **auto** 等於 `/ip/settings` 中 **arp-timeout** 的值，預設為 30s |
| **comment** (*string*; Default: ) | 介面的簡短描述 |
| **disabled** (*yes \| no*; Default: **yes**) | 介面是否被停用 |
| **frequency** (*58320 \| 60480 \| 62640 \| 64800 \| 66000 \| auto*; Default: **auto**) | 通訊中使用的頻率（僅在 bridge 裝置上有效） |
| **isolate-stations** (*yes \| no*; Default: **yes**) | 不允許已連線的用戶端之間通訊（自 RouterOS 6.41 起） |
| **l2mtu** (*integer [0..7882]*; Default: **1600**) | 二層最大傳輸單元 |
| **mac-address** (*MAC*; Default: ) | 無線介面的 MAC 地址 |
| **mdmg-fix** (*yes \| no*; Default: **no**) | 僅適用於 wAP60Gx3 裝置的實驗性功能，在某些情況下可提供更好的點對多點穩定性 |
| **mode** (*ap-bridge \| bridge \| sniff \| station-bridge*; Default: **bridge**) | 執行模式 |
| **mtu** (*integer [32..8192]*; Default: **1500**) | 三層最大傳輸單元 |
| **name** (*string*; Default: **wlan60-1**) | 介面名稱 |
| **password** (*string*; Default: **隨機生成**) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於 AES 加密的密碼 |
| **put-stations-in-bridge** (; Default: ) | 將新建的 station 裝置介面放入此 bridge |
| **region** (*asia \| australia \| canada \| china \| eu \| japan \| no-region-set \| usa*; Default: **no-region-set**) | 用於限制頻率使用的引數 |
| **scan-list** (*58320,60480,62640,64800,66000*; Default: **58320,60480,62640,64800**) | 掃描列表，用於限制 station 模式下的頻率連線 |
| **ssid** (*string (0..32 chars)*; Default: **[身份](../../system-information-and-utilities/identity.md) 的值**) | SSID（服務集識別符號）是標識無線網路的名稱 |
| **tx-sector** (*integer [0..63] \| auto*; Default: **auto**) | 停用波束成形並鎖定到選定的輻射方向圖 |

**子選單：** `/interface/w60g/print/stats`

提供有關波束成形發生情況以及一些偵錯資訊的更詳細資訊：

```ros
/interface w60g print stats name: wlan60-1 
beamforming-event: 310 
tx-io-msdu: 0 
tx-sw-msdu: 154 663
tx-fw-msdu: 102 
tx-ppdu: 220 147 
tx-ppdu-from-q: 40 327 
tx-mpdu-new: 154 663 
tx-mpdu-total: 184 759 
tx-mpdu-retry: 30 096 
rx-ppdu: 166 636 
rx-mpdu-crc-err: 4 817 
rx-mpdu-crc-ok: 285 649
```

Station 介面屬性：

:::warning
ap-bridge 裝置需要 License level 4  [(單擊瞭解更多資訊)](../../getting-started/routeros-licensing/x86/index.md#routeros-license-key-levels)  才能支援多個已連線用戶端
:::

已連線的用戶端會被視為獨立介面；成功連線後，會建立一個新的 station 介面。

更新後預設配置仍然有效——新建的 station 介面會被移動到預設網橋。

**子選單：** `/interface/w60g/station`

| 屬性 | 描述 |
| :-- | :-- |
| **parent** (*string*; Default: **wlan60-\***) | 父介面名稱 |
| **put-in-bridge** (*none \| parent \| bridge-name*; Default: **parent**) | 將 station 裝置介面新增到指定網橋 |
| **remote-address** (*MAC*; Default: **與 bridge 介面 MAC 匹配**) | station 要連線的 bridge 介面的 MAC 地址 |

### 掃描 {#scan}

**子選單：** `/interface/w60g/scan`

```ros
/interface w60g scan wlan60-1
```

Scan 命令會搜尋並顯示 W60G 介面所支援頻率範圍內的可用 AP。

使用 scan 命令時，介面執行會被停用（掃描操作期間無線鏈路會斷開）

目前無法進行後臺掃描。

### 監控 {#monitor}

**子選單：** `/interface/w60g/monitor`

```ros
/interface w60g monitor wlan60-1 
connected: yes frequency: 58320 
remote-address: 04:D6:AA:AA:AA:AA 
mcs: 8 
phy-rate: 2.3Gbps 
signal: 80 rssi: -68 
tx-sector: 28 
tx-sector-info: center 
distance: 160.9m
```

Monitor 顯示活動連線的當前狀態。距離測量工具可提供非常精確的距離測量。"tx-sector-info"（測試階段功能）會提供當前所用波束成形方向圖的資訊，並顯示指向中心的方向——理論上的最高功率輸出點。

### 對齊 {#align}

**子選單：** `/interface/w60g/align`

```ros
/interface w60g align wlan60-1 
connected: yes 
frequency: 58320 
remote-address: 04:D6:AA:AA:AA:AB 
tx-mcs: 6 
tx-phy-rate: 1540.0Mbps 
signal: 70 
rssi: -62 
10s-average-rssi: -63.1 
tx-sector: 62 
tx-sector-info: left 19 degrees, up 26.6 degrees 
rx-sector: 96 
distance: 220.88m 
tx-packet-error-rate: 5%
```

在 align 模式下，兩個裝置之間的幀交換更頻繁，訊號質量資訊的顯示也更頻繁。使用 "rssi"、"10s-average-rssi" 和 "tx-sector-info" 值可更精確地對準鏈路。當裝置進入 align 模式時——鏈路會中斷幾秒鐘。

### 嗅探 {#sniff}

Sniff 模式允許捕獲附近的 802.11ad 幀。要使用 sniff 模式，需要使用相同頻率，並將介面執行模式設定為 sniff：

```ros
/interface w60g set wlan60-1 mode=sniff
```

現在可以在 [Tools/Packet Sniffer](../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) 中使用此介面進行封包捕獲。Sniffer 模式不能與常規介面工作模式一起使用。

### 點對多點設定示例 {#point-to-multi-point-setup-example}

所有 MikroTik 裝置都可以互連。目前有四種不同版本的 wAP60G 裝置可用：

- Wireless Wire kit
- wAP 60G
- SXTsq60 Lite60
- wAP 60G AP

以及

- Wireless Wire Dish

在硬體方面，wAP 裝置是相同的，但存在一些軟體限制：

**wAP 60G AP** 設計用於 PtMP（點對多點）設定中的接入點用途，但也可以用作 PtP（點對點）或作為 Station 裝置。它已配備 level4 許可證，可支援多個已連線用戶端。有關更多資訊，請參閱 [RouterOS 許可證金鑰級別](../../getting-started/routeros-licensing/x86/index.md#routeros-license-key-levels)。

**Wireless Wire kit**、**Wireless Wire Dish**、**SXTsq Lite60** 和 **wAP60G** 裝置附帶 level3 許可證。由於其輻射方向圖較窄，Wireless Wire Dish 應僅用作用戶端裝置。

需要升級許可證才能解鎖接入點模式下同時連線多個用戶端，但裝置可以作為常規 Station 裝置連線到接入點。

:::warning
配置前，請確保裝置執行最新的軟體版本：[如何升級](../../getting-started/installation-and-upgrade/upgrade.md)
:::

透明無線鏈路的最小配置是：SSID 匹配、模式正確（bridge || station-bridge），以及將無線和乙太網介面放入同一網橋。

在當前示例中，我們將介紹一個使用場景：**wAP60G AP** 用作接入點，**wAP60G** 和 **Wireless Wire kit** 裝置用作 Station 裝置，組成一個 4 單元網路。

:::warning
建議更改預設 IP 地址，以避免裝置連線問題
:::

**wAP60G AP** 裝置預配置為 WISP Bridge [預設配置](../../getting-started/configuration-management/default-configurations.md)。

無線和乙太網介面之間的 SSID 和網橋已配置。建議設定無線密碼並更改 SSID。如果裝置已被重設，還可以設定正確的模式並啟用介面。

完成上述所有步驟的一行命令：

```ros
/interface w60g set wlan60-1 password="put_your_safe_password_here" ssid="put_your_new_ssid_here" disabled=no mode=ap-bridge
```

**Wireless Wire 和 wAP60G** 裝置預配置為 PTP Bridge 預設配置。

Wireless Wire 裝置已具有隨機生成的匹配 SSID 和無線密碼。

Bridge 裝置（Bridge 或支援一個已連線用戶端的接入點裝置）需要將無線模式更改為 station-bridge。

可用於將裝置設定為用戶端模式的一行命令：

```ros
/interface w60g set wlan60-1 password="put_your_safe_password_here" ssid="put_your_new_ssid_here" disabled=no mode=station-bridge
```

如果從空配置開始配置（重設且不保留預設配置）：

需要建立一個包含無線和乙太網介面的新網橋，並新增一個便於訪問的 IP 地址。

```ros
{ /interface bridge 
add name=bridge1 
/interface bridge port 
add bridge=bridge1 interface=ether1 
add bridge=bridge1 interface=wlan60-1 
/ip address add address=192.168.88.1/24 interface=bridge1 
}
```

對於接入點，新增以下行以確保所有已連線的 station 都將放入同一網橋。

```ros
/interface w60g set wlan60-1 put-stations-in-bridge=bridge1
```

成功連線後，每個用戶端裝置都會在接入點裝置的以下位置出現一個新條目：

```ros
/interface w60g station print
```

```ros
Flags: X - disabled, R - running 

0 name="wlan60-station-1" parent=wlan60-1 remote-address=AA:AA:AA:AA:AA:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AB arp=enabled arp-timeout=auto put-in-bridge=parent 

1 name="wlan60-station-2" parent=wlan60-1 remote-address=AA:AA:AA:AA:AB:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AC arp=enabled arp-timeout=auto put-in-bridge=parent 

2 name="wlan60-station-3" parent=wlan60-1 remote-address=AA:AA:AA:AA:AC:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AD arp=enabled arp-timeout=auto put-in-bridge=parent 

3 name="wlan60-station-4" parent=wlan60-1 remote-address=AA:AA:AA:AA:AD:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AE arp=enabled arp-timeout=auto put-in-bridge=parent 
```

可以為每個用戶端應用單獨設定（佇列、VLAN、防火牆規則等），從而提供更大的配置靈活性。

要限制同一網橋中的用戶端之間的通訊，可以在接入點裝置上使用 isolate-stations 選項：

```ros
/interface w60g set wlan60-1 isolate-stations=yes
```

### 點對點 GUI 配置示例 {#point-to-point-gui-configuration-example}

[點對點 GUI 配置示例](./ptp-gui-example.md)

### 故障排除與建議 {#troubleshooting-and-recommendations}

MikroTik 60GHz 解決方案的功能包括支援 ATPC（自適應發射功率控制）

##### 物理特性 {#physical-properties}

802.11ad 標準所用無線頻率的大氣衰減非常高。部署鏈路前應考慮到這一點。

Wireless Wire kit 已在最遠 200 米的距離下進行測試。

Wireless Wire dish 套件已在最遠 2500 米的距離下測試。為獲得穩定性和全速可用性，建議該套件用於最遠 1500 米的距離。

wAP60G 裝置配備 60° 相控陣波束成形天線，可在短距離內幫助訊號繞過障礙物，但在更遠距離下保持視距仍然至關重要。

LHG60G 裝置的單個輻射方向圖小於 1 度（水平和垂直方向均是）。所有方向圖組合後在水平和垂直平面上可提供接近 3 度的覆蓋。每種情況下的最佳方向圖透過波束成形演算法計算。波束寬度和方向取決於所使用的預定義校準扇區。

##### 裝置射頻特性 {#device-rf-characteristics}

60 GHz 裝置

| **裝置** | **單天線方向圖寬度及完整跨度（度）** | **EIRP** | **發射功率** | **中心扇區\*** |
| :-- | :-- | :-- | :-- | :-- |
| wAP 60G | 單方向圖 15-20 度，水平面總跨度 60 度，垂直面總跨度 30 度 | < 40 dBm |  | 27,28,35,36 |
| wAP 60G AP | 單方向圖 15-20 度，水平面總跨度 60 度，垂直面總跨度 30 度 | < 40 dBm |  | 27,28,35,36 |
| Wireless Wire | 單方向圖 15-20 度，水平面總跨度 60 度，垂直面總跨度 30 度 | < 40 dBm |  | 27,28,35,36 |
| wAP 60Gx3 AP | 單方向圖 15-20 度，水平面總跨度 180 度，垂直面總跨度 30 度 | < 40 dBm |  | 27,28,35,36 |
| SXTsq Lite 60 | 單方向圖 15-20 度，水平面總跨度 60 度，垂直面總跨度 30 度 | < 40 dBm |  | 27,28,35,36 |
| Cube Lite 60 | 單方向圖 4-8 度，水平面總跨度 12 度，垂直面總跨度 12 度 | < 40 dBm | < 10 dBm | 27,28,35,36 |
| Cube 60G ac | 單方向圖 4-8 度，水平面總跨度 12 度，垂直面總跨度 12 度 | < 40 dBm | < 10 dBm | 27,28,35,36 |
| Cube 60Pro ac | 單方向圖 4-8 度，水平面總跨度 11 度，垂直面總跨度 11 度 | < 40 dBm | < 10 dBm | 27,28,35,36 |
| CubeSA 60Pro ac | 單方向圖 15 度，水平面總跨度 60 度，垂直面總跨度 30 度 | < 40 dBm | < 10 dBm | 27,28,35,36 |
| LHG Lite 60 | 單方向圖 < 1 度，水平面總跨度 3 度，垂直面總跨度 3 度 | < 55 dBm | < 10 dBm | 27,28,35,36 |
| LHG 60G | 單方向圖 {`< 1`} 度，水平面總跨度 3 度，垂直面總跨度 3 度 | {`< 55`} dBm | {`< 10`} dBm | 27,28,35,36 |
| Wireless Wire Dish | 單方向圖 {`< 1`} 度，水平面總跨度 3 度，垂直面總跨度 3 度 | {`< 55`} dBm | {`< 10`} dBm | 27,28,35,36 |
| Wireless Wire nRAY | 單方向圖 {`< 1`} 度，水平面總跨度 3 度，垂直面總跨度 3 度 | {`< 55`} dBm 或在使用 EU 區域時為 {`<40`} dBm | {`< 10`} dBm | 31 |

**\*中心扇區是波束成形陣列的校準中心**

##### 區域 {#regions}

MikroTik 802.11ad 裝置支援頻率範圍：57240 MHz - 67080 MHz；如果使用 "region" 引數，則可以限制頻率和通道的使用。

| **區域** | **下限頻率** | **上限頻率** | **可用通道** |
| :-- | :-- | :-- | :-- |
| 美國 | 57.24 GHz | 70.20 GHz | 1, 2, 3, 4, 5, 6 |
| 加拿大 | 57.24 GHz | 63.72 GHz | 1, 2, 3 |
| 亞洲 | 57.24 GHz | 63.72 GHz | 1, 2, 3 |
| 歐盟 | 57.24 GHz | 65.88 GHz | 1, 2, 3, 4 |
| 日本 | 57.24 GHz | 65.88 GHz | 1, 2, 3, 4 |
| 澳大利亞 | 57.24 GHz | 65.88 GHz | 1, 2, 3, 4 |
| 中國 | 59.40 GHz | 63.72 GHz | 2, 3 |

##### 連線問題 {#connection-issues}

為了使裝置連線，它們必須處於直接可見（視距）範圍內，用戶端裝置上的 "scan-list" 需要包含 AP 裝置所使用的 "frequency"。LHG60 裝置需要非常精確的對準，以便在更遠距離下獲得最佳效能。

##### 用於監控的 SNMP OID {#snmp-oids-for-monitoring}

從 RouterOS>=6.42rc6 開始，增加了對 W60G 介面監控的 SNMP 支援。
對於主介面：

```
1.3.6.1.4.1.14988.1.1.1.8.1.2.1  integer  Mode
1.3.6.1.4.1.14988.1.1.1.8.1.3.1  string   SSID
1.3.6.1.4.1.14988.1.1.1.8.1.4.1  integer  Connected status
1.3.6.1.4.1.14988.1.1.1.8.1.5.1  string   Remote MAC
1.3.6.1.4.1.14988.1.1.1.8.1.6.1  integer  Frequency
1.3.6.1.4.1.14988.1.1.1.8.1.7.1  integer  MCS
1.3.6.1.4.1.14988.1.1.1.8.1.8.1  integer  Signal quality
1.3.6.1.4.1.14988.1.1.1.8.1.9.1  integer  tx-sector
1.3.6.1.4.1.14988.1.1.1.8.1.11.1 string   Sector info
1.3.6.1.4.1.14988.1.1.1.8.1.12.1 integer  RSSI
1.3.6.1.4.1.14988.1.1.1.8.1.13.1 gauge32  PHY rate
```

Station 介面將在另一個表下編號：

```
1.3.6.1.4.1.14988.1.1.1.9.1.2.(interfaceID) = integer Connected status
1.3.6.1.4.1.14988.1.1.1.9.1.3.(interfaceID) = Hex-STRING mac-address
1.3.6.1.4.1.14988.1.1.1.9.1.4.(interfaceID) = INTEGER: MCS 
1.3.6.1.4.1.14988.1.1.1.9.1.5.(interfaceID) = INTEGER: Signal Quality Index
1.3.6.1.4.1.14988.1.1.1.9.1.6.(interfaceID) = INTEGER: tx-sector
1.3.6.1.4.1.14988.1.1.1.9.1.8.(interfaceID) = Gauge32: data-rate [Mbps]
1.3.6.1.4.1.14988.1.1.1.9.1.9.(interfaceID) = INTEGER: RSSI
1.3.6.1.4.1.14988.1.1.1.9.1.10.(interfaceID) = INTEGER: distance [cm]
```

InterfaceID 從 3 開始，每連線一個 station 就增加 +1。有關 SNMP 功能和 MIB 檔案的更多資訊，請參閱 [SNMP 手冊](../../diagnostics-monitoring-and-troubleshooting/snmp.md)

##### Wireless Wire 套件的配置重設 {#configuration-reset-for-wireless-wire-kits}

Reset 按鈕的功能與其他裝置相同，詳見 [此處](../../getting-started/configuration-management/routeros-configuration-reset.md)

**啟動時按住按鈕 5 秒（USR LED 燈開始閃爍）** - 重設為受密碼保護的狀態。

**啟動時按住按鈕 10 秒（USR LED 閃爍後變為常亮）** - 完全移除配置。

:::warning
完全移除配置後，只能建立 [mac-telnet](../../management-tools/mac-server.md) 連線
:::
