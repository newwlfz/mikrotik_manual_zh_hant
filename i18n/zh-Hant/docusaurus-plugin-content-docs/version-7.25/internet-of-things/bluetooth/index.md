---
sidebar_key: "internet-of-things/bluetooth/index"
sidebar_position: 1
title: "藍牙"
sidebar_label: "藍牙"
description: "本頁面介紹 MikroTik RouterOS 的 Bluetooth IoT 功能，涵蓋 Bluetooth 通道結構、廣播封包格式，以及透過 `/iot/bluetooth` 子選單進行的配置。文中說明了 PDU 型別、天線選擇，以及用於 Bluetooth 晶片管理的裝置命名，並列出對 iot 軟體包或 USB-Bluetooth 介面卡支援的要求。"
tags:
  - 'bluetooth'
  - 'iot'
  - 'packet-structure'
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/bluetooth
captured_at: '2026-11-04T11:17:50+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹基於藍牙的 IoT 示例。可使用本節內容配置藍牙標籤跟蹤，並將收集到的資料與 MQTT 和 ThingsBoard 整合。

<DocCardList />

藍牙是一種短距離無線技術，允許透過特定的藍牙通道廣播資料。

共有 40 個獨特的頻段（通道），每個頻段間隔 2 MHz。通道 37、38 和 39 用於主廣播，0-36 用於資料傳輸。

在廣播過程中，會廣播 BLE 廣播封包。該封包包含 Preamble、Access Address、PDU 和 CRC 欄位。

Preamble 和 Access Address 欄位可幫助接收方檢測幀。CRC 欄位用於檢查錯誤。PDU 由 PDU Header 和 PDU Payload 組成。PDU 定義封包本身。

PDU Header 包含有關 PDU 型別的資訊。根據型別不同，負載欄位可能有所不同。

例如，當 PDU 型別為 ADV\_NOCONN\_IND 時 → PDU Payload 由 "AdvA"（包含廣播者地址資訊的欄位）和 "AdvData"（包含資料資訊的欄位）欄位組成：

1 個八位組 = 1 個位元組 = 8 位

| 名稱 | 長度 |
| :-- | :-- |
| Preamble | 1 個八位組 |
| Access-Address | 4 個八位組 |
| PDU | <ul><li>PDU 頭 = 2 個八位組</li><li>PDU 載荷 = AdvA（6 個八位組）+AdvData（0...31 個八位組）</li></ul> |
| CRC | 3 個八位組 |

PDU 型別有多種：

- ADV\_IND（其中負載由 AdvA [6octets] + AdvData [0-31 octets] 組成，用於可連線、可掃描的非定向廣播）。
- ADV\_NOCONN\_IND（其中負載由 AdvA [6octets] + AdvData [0-31 octets] 組成，用於不可連線、不可掃描的非定向廣播）。
- ADV\_SCAN\_IND（其中負載由 AdvA [6octets] + AdvData [0-31 octets] 組成，用於可掃描、非定向廣播）。
- SCAN\_REQ（其中負載由 ScanA [6octets] + AdvA [6octets] 組成，ScanA 欄位包含掃描器地址，AdvA 包含廣播者地址，用於請求 SCAN\_RSP 響應）。
- SCAN\_RSP（其中負載由 AdvA [6octets] + ScanRspData [0-31 octets] 組成，ScanRspData 可包含來自廣播者主機的任意資料，用於響應 SCAN\_REQ 請求）。
- ADV\_DIRECT\_IND（其中負載由 AdvA [6octets] + TargetA [6octets] 組成，TargetA 是 PDU 定址到的裝置地址欄位，用於可連線的定向廣播）。
- 等等。

可在[此處](https://www.bluetooth.com/specifications/specs/core-specification/)（藍牙規範）找到有關封包結構的更多資訊。

RouterOS 中藍牙介面的主要應用是監控由其他裝置（例如 [藍牙標籤](https://help.mikrotik.com/docs/display/UM/TG-BT5-IN)）廣播的藍牙廣播封包（掃描器功能），或傳送廣播封包（廣播器功能）。

## 配置 {#configuration}

**子選單：** `/iot/bluetooth`

:::info
**iot** 軟體包是帶有內建藍牙晶片的裝置所必需的，例如 [KNOT](https://mikrotik.com/product/knot) 或 [KNOT Embedded LTE](https://mikrotik.com/product/knot_embedded_lte4)。

如果你的裝置是 ARM、ARM64 架構並且帶有 USB 插槽，則 **iot-bt-extra** 軟體包可透過 USB 藍牙介面卡啟用藍牙功能。並非所有藍牙介面卡都經過測試。介面卡必須支援 **LE 4.0+**。目前還沒有 "peripheral" 列表。

**Iot** 軟體包在 RouterOS 版本 6.48.3 中可用。**Iot-bt-extra 軟體包**在 RouterOS 7.18 中可用。你可以從我們的[下載頁面](https://mikrotik.com/download)獲取它們 - 位於 "Extra packages" 下。
:::

### 裝置 {#devices}

在此選單中，你可以檢視並設定常規藍牙晶片引數：

```ros
/iot/bluetooth/print
Columns: NAME, PUBLIC-ADDRESS, RANDOM-STATIC-ADDRESS, ANTENNA
  #  NAM  PUBLIC-ADDRESS     RANDOM-STATIC-ADD  ANTENNA 
  0  bt1  00:00:00:00:00:00  F4:4E:E8:04:77:3A  internal
/iot/bluetooth/set
```

***注意**：* 公共地址是 IEEE 註冊的永久地址。此地址無法更改。在上面的 "print" 示例中，裝置未分配公共地址（所有 octets 均設定為 0）。

可配置設定如下所示：

| 屬性 | 描述 |
| :-- | :-- |
| **antenna** (*string*; 預設：internal) | 選擇使用內部還是外部藍牙天線 |
| **name** (*string*; 預設：) | 藍牙晶片/介面的描述性名稱 |
| **random-static-address** (*MAC address*; 預設：) | 藍牙晶片的使用者可配置地址 |

可以使用以下命令監控晶片統計資訊：

```ros
/iot/bluetooth/print stats
Columns: NAME, RX-BYTES, TX-BYTES, RX-ERRORS, TX-ERRORS, RX-EVT, TX-CMD, RX-ACL, TX-ACL
  #  NAM  RX-BYTE  TX-  R  T  RX-EV  TX  R  T
  0  bt1  1857835  235  0  0  46677  45  0  0
```

### 廣播器 {#advertisers}

在此選單中，可以將藍牙晶片設定為傳送廣播封包。可以使用以下命令檢視和設定廣播器設定：

```ros
/iot/bluetooth/advertisers/print
Flags: X - DISABLED
Columns: DEVICE, MIN-INTERVAL, MAX-INTERVAL, OWN-ADDRESS-TYPE, CHANNEL-MAP, AD-SIZE
#   DEVICE  MIN-INTERVAL  MAX-INTERVAL  OWN-ADDRESS-TYPE  CHANNEL-MAP  AD-SIZE
0 X bt1     1280ms        2560ms        random-static              37        0
                                                                   38         
                                                                   39         
/iot/bluetooth/advertisers/set
```

可配置設定如下所示：

| 屬性 | 描述 |
| :-- | :-- |
| **ad-structures** (*string*; 預設：) | 為廣播封包選擇預配置結構。更多資訊請參閱 "AD 結構" 小節。 |
| **channel-map** (*37 \| 38 \| 39*; 預設：37, 38, 39) | 用於廣播的通道。 |
| **disabled** (*yes \| no*; 預設：**yes**) | 用於停用或啟用藍牙晶片廣播封包的選項。 |
| **max-interval** (*integer:*20..10240;** 預設：**2560** **ms**) | 傳送廣播封包的最大間隔。 |
| **min-interval** (*integer:*20..10240;** 預設：**1280 ms**) | 傳送廣播封包的最小間隔。 |
| **own-address-type** (*public \| random-static \| rpa-fallback-to-public \| rpa-fallback-to-random*; 預設：**random-static**) | 將用於廣播封包負載的 MAC 地址：public → 使用 IEEE 註冊的永久地址。random-static → 使用使用者可配置地址（將在下次重新上電時更改）。rpa-fallback-to-public → 使用可解析隨機私有地址（RPA），僅當接收方擁有我們的身份解析金鑰（IRK）時才能解析。如果無法生成 RPA，則改用公共地址。rpa-fallback-to-random → 與 "rpa-fallback-to-public" 相同，但如果無法生成 RPA，則改用 random-static 地址。 |
| **phy** (*1M \| 2M \| CODED*; 預設：**1M**) | 設定裝置在廣播期間使用的 "物理層"：CODED → 最低速率 125 kbps = 更遠距離；1M → 標準速率 1 Mbps = 中等距離；2M → 最高速率 2 Mbps = 短距離；**重要：** CODED 僅受 [KNOT Embedded LTE](https://mikrotik.com/product/knot_embedded_lte4) 支援。  |
| **legacy** (*yes \| no*) | 設定廣播型別 → 擴充套件或傳統。使用 `legacy=no` 時，AD 結構長度可擴充套件到最多 191 bytes。使用 `legacy=yes` 時，AD 結構長度限制為 31 bytes。傳統廣播僅使用 "primary" 藍牙通道來廣播負載。擴充套件廣播同時使用 "primary" 和 "secondary" 通道。  |

***注意**：* 廣播封包將每隔 *min-interval* \<= **X** \<= *max-interval* milliseconds 廣播一次。

### AD 結構 {#ad-structures}

本節允許你為藍牙晶片將要廣播的廣播封包定義負載。

目前僅支援 4 種類型：0x08 "Shortened Local Name"；0x09 "Complete Local Name"；0xFF "Manufacturer Specific Data"；"Service Data"

可以使用以下命令檢視和設定 "AD 結構" 設定：

```ros
/iot/bluetooth/advertisers/ad-structures/print
Columns: NAME, TYPE, DATA
#  NAME  TYPE              DATA
0  test  short-local-name  TEST
/iot/bluetooth/advertisers/ad-structures/set 
```

可配置屬性如下所示：

| 屬性 | 描述 |
| :-- | :-- |
| **data** (*string*; 預設：) | 定義廣播封包負載的 AdvData 部分 |
| **name**(*string*; 預設：) | AD 結構的描述性名稱 |
| **type** (complete-local-name \| manufacturer-data \| short-local-name \| service-data; 預設：) | 用於設定 AD 結構型別的選項：0x08 "Shortened Local Name"（"text" 格式）0x09 "Complete Local Name"（"text" 格式）0xFF "Manufacturer Specific Data"（"hex" 格式）0x20 "Service Data 32-bit"（"hex" 格式） |

例如，如果選擇 "Shortened Local Name" 型別，並將 "data" 欄位配置為 "TEST" → 則負載的 AdvData 部分將如下所示：

05 08 54 45 53 54（十六進位制格式）

，其中第一個 octet（05）表示後續 bytes 數量（5 bytes），第二個 octet（08）表示型別（Shortened Local Name）。第 3、4、5 和 6（等等）個 octets 是 "data" [54 (hex)=**T** (ASCII), 45 (hex)=**E** (ASCII), 53 (hex)=**S** (ASCII), 54 (hex)=**T** (ASCII)]。

"Complete Local Name" 型別也是如此。只有 AdvData 負載中的第二個 octet 會有所不同，並將設定為 09。

對於 "Manufacturer Specific Data" 型別，你需要以十六進位制格式配置 "data" 欄位。此型別的第二個 octet 將設定為 FF。

### 連線 {#connections}

:::info
從 v**7.12beta9** 開始可用。
:::

目前僅支援 `central` 角色。不支援 `Peripheral device` 角色以及 `pairing` 和 `encryption` 選項。

可用小節如下：

| 小節 | 描述 |
| :-- | :-- |
| async-data | 用於檢視已訂閱的資料。 |
| characteristics | 用於檢視裝置支援的所有特徵。 |
| connect | 用於連線到處於 `connactable` 狀態的裝置。 |
| disconnect | 用於斷開與裝置的連線。 |
| read | 用於讀取特徵值。 |
| write | 用於寫入特徵值。 |
| subscribe | 用於訂閱特徵值。 |
| unsubscribe | 用於取消訂閱特徵值。 |

要連線到處於 `connectable` 狀態的藍牙裝置，請使用以下命令（其中 `pdev` 是裝置地址）：

```ros
/iot/bluetooth/connections/connect pdev=DC:2C:6E:0F:C0:3D
```

:::info
要連線 TG-BT5-IN/OUT 標籤，請確保將磁鐵靠近磁性開關，使其進入 `connectable` 狀態。
:::

要檢視已建立的連線：

```ros
/iot/bluetooth/connections/print
```

要檢視裝置特徵：

```ros
/iot/bluetooth/connections/characteristics/print
Columns: PDEV, NAME, UUID
 #  PDEV               NAME                              UUID                            
 0  DC:2C:6E:0F:C0:3D  Service Changed                   2a05                            
 1  DC:2C:6E:0F:C0:3D  Database Hash                     2b2a                            
 2  DC:2C:6E:0F:C0:3D  Client Supported Features         2b29                            
 3  DC:2C:6E:0F:C0:3D  Device Name                       2a00                            
 4  DC:2C:6E:0F:C0:3D  Appearance                        2a01                            
...
...
...
```

要讀取特定特徵，請指定 `pdev` 地址和 `uuid`：

```ros
/iot/bluetooth/connections/read pdev=DC:2C:6E:0F:C0:3D uuid=2a00
```

### 掃描器 {#scanners}

在此選單中，可以為藍牙晶片設定掃描器設定。停用時，裝置將無法再接收廣播報告。啟用時，你可以在 "廣播報告" 標籤頁中監控廣播報告（本指南稍後將對此進行說明）。可以使用以下命令檢視和設定掃描器設定：

```ros
/iot/bluetooth/scanners/print
Flags: X - DISABLED
Columns: DEVICE, TYPE, INTERVAL, WINDOW, OWN-ADDRESS-TYPE, FILTER-POLICY, FILTER-DUPL
ICATES
#   DEVICE  TYPE     INTERVAL  WINDOW  OWN-ADDRESS-TYPE  FILTER-POLICY  FIL
0 X bt1     passive  10ms      10ms    random-static     default        off
/iot/bluetooth/scanners/set
```

可配置屬性如下所示：

| 屬性 | 描述 |
| :-- | :-- |
| **disabled** (*yes \| no*; 預設：**no**) | 用於停用或啟用藍牙晶片接收廣播報告的選項。 |
| **filter-duplicates** (keep-newest \| keep-oldest \| keep-unique \| off; 預設：**off**) | 用於丟棄來自同一廣播者的重複廣播的選項：keep-newest → 保留最新報告（丟棄最舊報告）。僅保留來自單個 AdvA 的最新 PDU。keep-oldest → 保留最舊報告（丟棄最新報告）。僅保留來自單個 AdvA 的最舊 PDU。此類 PDU 過濾發生在控制器層面，因此是最高效（就能量/頻寬而言）的重複過濾方法。keep-unique → 僅顯示具有唯一負載的廣播。也就是說，如果發現 1 個以上相同負載（AdvData），則僅顯示第一個負載，而 "克隆" 會被丟棄/忽略。off → 不丟棄重複項。所有具有相同 AdvA 的 PDU 都將保留。**重要：** 重複廣播報告是指從同一裝置地址傳送的廣播報告。實際資料（負載的 "AdvData" 部分）可能變化/不同，在確定重複廣播報告時並不將其視為重要因素。也就是說，例如，如果藍牙介面從同一標籤接收到 10 個負載（一個接一個的負載，間隔 1 秒）：如果使用 "keep-oldest" 設定 → 藍牙介面將僅顯示從該標籤接收到的第一個負載（後續 9 個負載將被過濾掉）。如果使用 "keep-newest" 設定 → 藍牙介面將僅顯示從該標籤接收到的最後一個負載（每個後續負載都會重寫前一個負載）。 |
| **filter-policy** (default \| whitelist *\| no*; 預設：**default**) | 用於設定過濾策略（控制器層面的廣播過濾）的選項：default → 啟用此策略時，掃描器將僅接受 ADV_IND、ADV_NOCONN_IND、ADV_SCAN_IND、SCAN_RSP 和 ADV_DIRECT_IND（其中 TargetA 是掃描器自身的藍牙地址）PDU 型別。whitelist → 啟用此策略時，掃描器將僅接受由地址配置在 "Whitelist" 小節中的廣播者廣播的 ADV_IND、ADV_NOCONN_IND、ADV_SCAN_IND、SCAN_RSP PDU 型別，以及 ADV_DIRECT_IND 型別 PDU（其中 TargetA 是掃描器自身的藍牙地址）。 |
| **interval** (*integer:3..10240*;** 預設：**10 ms**) | 掃描器開始掃描下一個廣播通道之前的時間。 |
| **own-address-type** (*public \| random-static \| rpa-fallback-to-public \| rpa-fallback-to-random*; 預設：**random-static**) | 掃描請求中使用的地址型別（如果使用主動掃描型別）：public → 使用 IEEE 註冊的永久地址。random-static → 使用使用者可配置地址（將在下次重新上電時更改）。rpa-fallback-to-public → 使用可解析隨機私有地址（RPA），僅當擁有我們的身份解析金鑰（IRK）時才能解析。如果無法生成 RPA，則改用公共地址。rpa-fallback-to-random → 與 "rpa-fallback-to-public" 相同，但如果無法生成 RPA，則改用 random-static 地址。 |
| **type** (*active \| passive;* 預設：**passive**) | 定義掃描器型別：active → 如果收到可掃描廣播，掃描器可以傳送掃描請求。掃描器可以傳送 SCAN_REQ 以獲取 SCAN_RSP 響應。passive → 掃描器僅監聽廣播，不會發送任何資料（例如掃描請求）。 |
| **window** (*integer:3..10240;* 預設：**10 ms**) | 掃描器掃描單個廣播通道所花費的時間。 |
| **phy** (*1M \| 2M \| CODED*; 預設：**1M**) | 設定裝置在掃描期間使用的 "物理層"：CODED → 最低速率 125 kbps = 更遠距離；1M → 標準速率 1 Mbps = 中等距離；2M → 最高速率 2 Mbps = 短距離；**重要：** CODED 僅受 [KNOT Embedded LTE](https://mikrotik.com/product/knot_embedded_lte4) 支援。     |

例如，如果將掃描器 interval 設定為 20ms，這意味著只有在 20ms 之後，裝置才會開始掃描下一個排隊的通道。如果將掃描器 window 設定為 10ms，這意味著裝置僅在該 10ms 視窗內掃描每個通道。這意味著它將掃描通道 37 達 10ms（window 時間），並在再過 10ms 後開始掃描下一個通道（20ms[interval]-10ms[window]）。掃描通道 38 將花費 10ms，再過 10ms 後，裝置將開始掃描通道 39。

掃描器將能夠同時捕獲 "extended" 和 "legacy" 廣播型別。

### 廣播報告 {#advertising-reports}

在本節中，可以監控（來自附近廣播者的）藍牙廣播報告。列表限制為 1024 個條目（如果列表已滿 1024 個條目，則收到的每個新負載都會覆蓋 "最舊" 的條目）。可以使用以下命令監控廣播報告：

```ros
/iot/bluetooth/scanners/advertisements/print      
Columns: DEVICE, PDU-TYPE, TIME, ADDRESS-TYPE, ADDRESS, RSSI
 #  DEV  PDU-TYPE        TIME                  ADDRES  ADDRESS            RSSI  
 0  bt1  adv-noconn-ind  2021-07-28 09:30:56  public  2C:C8:1B:93:16:49  -24dBm
 1  bt1  adv-noconn-ind  2021-07-28 09:30:56  random  0B:16:17:9E:7B:EF  -60dBm
```

可以使用以下命令為報告設定過濾器：

```ros
/iot/bluetooth/scanners/advertisements/print where  
```

例如，要列印由特定藍牙地址廣播的報告，請使用以下命令：

```ros
/iot/bluetooth/scanners/advertisements/print where address=XX:XX:XX:XX:XX:XX
 # DEVICE    PDU-TYPE       TIME                 ADD... ADDRESS                    RSSI     LENGTH DATA    
79 bt1       adv-noconn-ind 2021-07-28 09:46:38 public XX:XX:XX:XX:XX:XX        -70dBm         30 02010...
80 bt1       adv-noconn-ind 2021-07-28 09:46:43 public XX:XX:XX:XX:XX:XX        -67dBm         30 02010...
81 bt1       adv-noconn-ind 2021-07-28 09:46:44 public XX:XX:XX:XX:XX:XX        -70dBm         28 1bff0...
82 bt1       adv-noconn-ind 2021-07-28 09:46:48 public XX:XX:XX:XX:XX:XX        -75dBm         30 02010...
```

要僅顯示 RSSI 強於 -30 dBm 的廣播報告，請使用以下命令：

```ros
/iot/bluetooth/scanners/advertisements/print where rssi > -30
 # DEVICE         PDU-TYPE       TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA       
307 bt1            adv-noconn-ind 2021-07-29 10:11:31 public       2C:C8:1B:93:16:49        -24dBm         22 15ff4f09.>
308 bt1            adv-noconn-ind 2021-07-29 10:11:31 public       2C:C8:1B:93:16:49        -26dBm         22 15ff4f09.>
```

可用過濾器（可以使用以下引數過濾廣播報告列表）：

| 過濾器 | 描述 |
| :-- | :-- |
| **address** | 藍牙廣播者的地址 |
| **address-type** | 廣播者的地址型別（例如 public 或 random） |
| **data** | 十六進位制格式的廣播資料（AdvData 負載） |
| **device** | 藍牙晶片/介面名稱 |
| **epoch** | 自 Unix 紀元以來的毫秒數 |
| **filter-comment** | 匹配的 whitelist 過濾器的註釋 |
| **length** | 廣播資料長度 |
| **pdu-type** | 廣播 PDU 型別 |
| **rssi** | 訊號強度 |
| **time** | 廣播封包接收時間 |

### 白名單 {#whitelist}

在此標籤頁中，可以配置將在 "掃描器" 小節的過濾策略中使用的白名單。換句話說，它用於指定將要掃描（並顯示在 "廣播報告" 中）的藍牙地址。

可以使用以下命令檢視白名單條目：

```ros
/iot/bluetooth/whitelist/print
Columns: DEVICE, ADDRESS-TYPE, ADDRESS
# DEVICE  ADDRESS-TYPE  ADDRESS    
0 bt1     any           *:*:*:*:*:*
```

可以使用以下命令新增新的白名單條目：

```ros
/iot/bluetooth/whitelist/add
```

### 可配置屬性 {#configurable-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*MAC address*; 預設：) | 廣播者的地址 |
| **address-type** (*any \| public \| random*; 預設：) | 廣播者的地址型別 |
| **comment**(*string*; 預設：) | 白名單條目的簡短描述 |
| **copy-from** | 用於複製條目的選項 - 更多資訊請檢視[控制檯命令](../../developer-guides/scripting/index.md#common-commands) |
| **device** (*bt1*; 預設：) | 選擇藍牙介面/晶片名稱 |
| **disabled** (*yes \| no*; 預設：) | 用於停用或啟用條目的選項 |

:::info
在 **7.14beta8** 版本之前，最多隻能新增 8 個白名單條目。  
從 **7.14beta8** 版本開始，白名單不再限制為 8 個條目，並且 address 欄位支援星號萬用字元。
:::

例如，如果要將所有以 "DC:2C:..." octets 開頭的 MAC 地址加入白名單，請使用星號萬用字元新增條目：

```ros
/iot/bluetooth/whitelist/add address=DC:2C:*:*:*:*
```

星號萬用字元不能用在特定 octets 之間，例如 `AA:*:*:BB:*:*`（這是無效條目）。

有效條目如下：

- `AA:BB:CC:DD:*:*`
- `AA:BB:CC:DD:EE:*`
- `AA:*:*:*:*:*`

### 外設裝置 {#peripheral-devices}

本節顯示解碼後的 Eddystone TLM、Eddystone UID、iBeacon 和 MikroTik 藍牙負載。如果 "外設裝置" 捕獲到其他信標型別，則不會對其進行解碼。

可以使用 `print detail` 命令檢視解碼後的列表：

```ros
/iot/bluetooth/peripheral-devices/print detail 
 0 address-type=public address=60:C0:BF:87:E2:1C name="60:C0:BF:87:E2:1C" persist=no 
   mtik-key="" rssi=-64 
   last-data="0201041BFFCD0960C0BF87E21C025B1F198B21AC62CDAE0045FAFEFE057D7B" 
   last-seen=2023-08-22 11:20:09 beacon-types="" 

 1 address-type=public address=DC:2C:6E:0F:C0:3D name="DC:2C:6E:0F:C0:3D" persist=no 
   mtik-key="" rssi=-47 
   last-data="0303AAFE1716AAFE00E5B2B98DE4C81C47C2B14E7500000000000000" 
   last-seen=2023-08-22 11:20:05 beacon-types=mikrotik,ibeacon,eddystone-uid 
   mtik-version=1 mtik-encrypted=no mtik-acc-x=-0.007G mtik-acc-y=-0.015G 
   mtik-acc-z=-0.007G mtik-temperature=23.808C mtik-battery=100% 
   mtik-uptime=14342160s mtik-flags="" 
   ibeacon-uuid="55555555-5555-5555-5555-222222222222" ibeacon-major=1280 
   ibeacon-minor=512 ibeacon-rssi-at-1m=-68dBm eddy-rssi-at-1m=-27dBm 
   eddy-namespace="b2b98de4c81c47c2b14e" eddy-instance="750000000000" 

 2 address-type=public address=DC:2C:6E:F6:54:7D name="DC:2C:6E:F6:54:7D" persist=no 
   mtik-key="" rssi=-74 
   last-data="0201060303AAFE1116AAFE20000B701549023532D802384F46" 
   last-seen=2023-08-22 11:20:13 beacon-types=eddystone-tlm eddy-version=0 
   eddy-battery-voltage=2.928V eddy-temperature=21.285C eddy-packet-count=37040856 
   eddy-uptime=3724474.2s 

 3 address-type=public address=DC:2C:6E:0F:C0:3E name="DC:2C:6E:0F:C0:3E" persist=no 
   mtik-key="" rssi=-72 last-data="15FF4F0901000214FFFF0200FDFF4F1774E00F000064" 
   last-seen=2023-08-22 11:20:06 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=-0.003G mtik-acc-y=0.007G mtik-acc-z=-0.011G 
   mtik-temperature=23.308C mtik-battery=100% mtik-uptime=1040500s mtik-flags="" 

 4 address-type=public address=60:C0:BF:20:9A:50 name="60:C0:BF:20:9A:50" persist=no 
   mtik-key="" rssi=-66 
   last-data="0201041BFF4160C0BF209A50FFA4CA8906E48C0377DCFDD2DF7AF02FFC6AC5" 
   last-seen=2023-08-22 11:20:11 beacon-types="" 
```

例如，可以根據裝置的 "address"（已知標籤的 MAC 地址）過濾列表：

```ros
/iot/bluetooth/peripheral-devices/print detail where address="DC:2C:6E:0F:C0:3E"
 0 address-type=public address=DC:2C:6E:0F:C0:3E name="my_tag" persist=yes 
   mtik-key="" rssi=-60 last-data="15FF4F090100669DFCFF0600FCFF6117F1E50F000064" 
   last-seen=2023-08-22 11:43:31 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=-0.015G mtik-acc-y=0.023G mtik-acc-z=-0.015G 
   mtik-temperature=23.378C mtik-battery=100% mtik-uptime=1041905s mtik-flags=""

/iot/bluetooth/peripheral-devices/print value-list where address="DC:2C:6E:0F:C0:3E"
      address-type: public
           address: DC:2C:6E:0F:C0:3E
              name: my_tag
           persist: yes
          mtik-key: 
              rssi: -71
         last-data: 15FF4F0901002AC60400000004004F17D4E90F000064
         last-seen: 2023-08-22 12:00:06
      beacon-types: mikrotik
      mtik-version: 1
    mtik-encrypted: no
        mtik-acc-x: 0.015G
        mtik-acc-y: 0G
        mtik-acc-z: 0.015G
  mtik-temperature: 23.308C
      mtik-battery: 100%
       mtik-uptime: 1042900s
        mtik-flags: 
```

或者，例如根據信標型別過濾列表：

```ros
/iot/bluetooth/peripheral-devices/print detail where beacon-types=mikrotik 
 0 address-type=public address=DC:2C:6E:0F:C0:3E name="my_tag" persist=yes 
   mtik-key="" rssi=-69 last-data="15FF4F0901000747020002000100611778E60F000064" 
   last-seen=2023-08-22 11:45:46 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=0.007G mtik-acc-y=0.007G mtik-acc-z=0.003G 
   mtik-temperature=23.378C mtik-battery=100% mtik-uptime=1042040s mtik-flags="" 

 7 address-type=public address=2C:C8:1B:4B:BB:0A name="2C:C8:1B:4B:BB:0A" persist=no 
   mtik-key="" rssi=-44 last-data="15FF4F09010077090000FCFFFDFFD519BF9EFF00005B" 
   last-seen=2023-08-22 11:45:53 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=0G mtik-acc-y=-0.015G mtik-acc-z=-0.011G 
   mtik-temperature=25.832C mtik-battery=91% mtik-uptime=16752319s mtik-flags="" 
```

此外，你可以選擇設定 `persist=yes`，這將確保裝置/標籤永久保留在列表中（因為停止廣播負載的裝置將在一分鐘後超時並從列表中移除，直到新的負載開始出現在空中）：

```ros
/iot/bluetooth/peripheral-devices/set persist=yes address="DC:2C:6E:0F:C0:3E"
```

還可以使用以下命令為裝置設定名稱，以便在列表中更容易找到它：

```ros
/iot/bluetooth/peripheral-devices/set name="my_tag" address="DC:2C:6E:0F:C0:3E"
```

### Decode-ad {#decode-ad}

在此選單中，可以解碼靜態 MikroTik、Eddystone TLM、Eddystone UID 和 iBeacon 負載。

要解碼負載，只需將其輸入到 "data" 欄位中：

```ros
/iot/bluetooth/decode-ad data=0201060303AAFE1116AAFE20000B6E158402353AF20238576B 
             type: eddystone-tlm
          version: 0
  battery-voltage: 2.926V
      temperature: 21.515C
     packet-count: 37042930
           uptime: 3724682.7s

/iot/bluetooth/decode-ad data=15FF4F090100032E0100FFFF00004F17C1E80F000064      
         type: mikrotik
      version: 1
    encrypted: no
        acc-x: 0.003G
        acc-y: -0.003G
        acc-z: 0G
  temperature: 23.308C
       uptime: 1042625s
        flags: 
      battery: 100%
```
