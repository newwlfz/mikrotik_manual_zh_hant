---
sidebar_key: "internet-of-things/lora/general-properties"
sidebar_position: 1
title: "通用屬性"
sidebar_label: "通用屬性"
description: "本頁記錄了在 MikroTik RouterOS 上設定 LoRaWAN 閘道器的配置設定，包括天線增益、通道計劃、伺服器連線和流量轉發規則。它說明了如何啟用閘道器、選擇頻段、配置 LBT 協定，以及透過 `/iot/lora` 和 `/iot/lora/channels` 等子選單管理通道。"
tags:
  - 'lora'
  - 'iot-package'
  - 'sub-menu'
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/lora/general-properties
captured_at: '2026-11-04T11:18:58+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

每個帶有支援 LTE 調變解調器的 miniPCI-e 插槽的 RouterBOARD，都可以透過安裝 **R11e-LR8** 或 **R11e-LR9** 卡用作 LoRaWAN 閘道器。支援 UDP 和 LNS（從 **v7.12rc1** 測試版本開始）協定。

:::info
要使用 LoRa，應安裝 IoT 軟體包。你可以在[下載](https://mikrotik.com/download)頁面的額外軟體包歸檔中找到適用於你裝置架構的軟體包。

**重要：** 從 v**7.11**（穩定版）開始，LoRa 功能已移入 **IoT 軟體包**，該軟體包可在[下載](https://mikrotik.com/download)頁面的額外軟體包下獲取。仍可下載單獨的 LoRa 軟體包。

使用 IoT 軟體包時，LoRa 功能將移到 `/iot/lora` 子選單。使用 LoRa 軟體包時，LoRa 功能可透過 `/lora` 子選單使用。

LoRa 軟體包不再是必需的，僅出於相容性原因保留。

**警告：** ***注意**：* RouterOS 不支援第三方 LoRaWAN 閘道器卡。
:::

## 屬性 {#properties}

此選單用於將設定應用到 LoRa 介面。

**子選單：** `/iot/lora`

| 屬性 | 描述 |
| :-- | :-- |
| **antenna-gain** (*integer [-128..127]*; 預設：**0**) | 以 dBi 為單位的天線增益。此值應等於 `setup-antenna-gain` 減去 `cable-loss`。使用 6.5 dBi 天線時，應配置為 6.5（不考慮線纜損耗）。閘道器的輸出功率由伺服器決定。閘道器將透過從 `server_value`（下行訊息中接收到的值）中減去 `antenna-gain` 設定來計算其實際輸出功率。 |
| **channel-plan** (*2.4-ghz \| as-923 \| as-923-2 \| as-923-3 \| as-923-4 \| au-915 \| au-915-1 \| au-915-2 \| custom \| eu-868 \| in-865 \| kr-920 \| ru-864 \| ru-864-mid \| us-915 \| us-915-1 \| us-915-2 \| us-915-3 \| us-915-4 \| us-915-5 \| us-915-6 \| us-915-7 \| us-915-8*; 預設：**eu-868**) | 各地區的頻率計劃。 |
| **disabled** (*yes \| no*; 預設：**yes**) | 是否停用 LoRaWAN 閘道器。 |
| **forward** (*crc-validation \| dev-addr-validation \| proprietary-traffic*; 預設：**crc-validation**) | 定義應將哪些型別的封包轉發到網路伺服器：crc-validation - 轉發具有正確 CRC 的有效封包。dev-addr-validation - 檢查封包的 DevAddr 是否與 NetID 對應，如果不對應，則丟棄該封包。具體過程如下：1) 從接收到的 LoRa 封包中“獲取” Dev. Addr 值；2) 將 Dev. Addr 與“有效” Net ID 列表進行“比較”；3) 如果該 Dev. Addr 沒有對應的 Net ID，則不轉發該封包；4) 如果 Net ID 有效且 Dev. Addr 範圍有效，則轉發該封包。proprietary-traffic - 檢查 LoRa 封包的內容，如果幀的“type”為“proprietary”，則不轉發該封包。 |
| **gateway-id**(string) | 向伺服器註冊閘道器時使用閘道器 ID 或閘道器 EUI。 |
| **lbt-enabled** (*yes \| no*; 預設：**no**) | 閘道器是否應使用 LBT（Listen Before Talk）協定。 |
| **listen-time** (*integer [0us..4294967295us]*; 預設：**5000us**) | 傳送（TX）前跟蹤 RSSI 的時間，以微秒為單位（當 **lbt-enabled=yes** 時使用）。 |
| **name** (*string*; 預設： ) | LoRaWAN 閘道器的名稱。 |
| **network** (*private \| public*; 預設：**public**) | 通訊時是否應使用同步字（network=private）或不使用（network=public）。 |
| **rssi-threshold** (*integer [-32,768 .. 32,767]*; 預設：**-65dBm**) | 用於確定轉發器是否可以使用特定通道進行通訊的 RSSI 值。如果 RSSI 值低於 **rssi-threshold**，則可以使用該通道（當 **lbt-enabled=yes** 時使用）。 |
| **servers** (*list of string*; 預設： ) | `/iot/lora/servers` 部分中的伺服器名稱。 |
| **src-address** (*IP*; 預設： ) | 如有必要，指定上行封包的源地址（該地址應與 RB 上配置的地址匹配）。 |
| **spoof-gps** (*bool \| lat \| long \| alt*; 預設： ) | 設定自定義 GPS 位置。使用 `lat`、`long`、`alt` 指定緯度、經度和高度值。 |

:::info
一旦選擇了伺服器並使用 `/iot/lora/enable [find]` 命令啟用了 LoRa 介面，裝置就會開始作為 LoRaWAN 閘道器執行。它將開始把 [`/iot/lora/traffic`](./general-properties.md#traffic) 標籤頁中的 LoRa 負載轉發到已配置的伺服器。
:::

## 通道 {#channels}

本節用於更改通道/頻率相關設定。

**子選單：** `/iot/lora/channels`

| 屬性 | 描述 |
| :-- | :-- |
| **bandwidth** (*200\_kHz \| 400\_kHz \| 62.5\_kHz \| 125\_kHz \| 250\_kHz \| 500\_kHz*; 預設：**125\_kHz**) | 特定通道的頻寬，在使用任何 channel-plan 預設時預定義，但當 channel-plan 設定為 custom 時可手動更改。 |
| **disabled** (*yes \| no*; 預設：**no**) | 停用或啟用該通道。 |
| **freq-off** (*integer* [-400000..400000]; 預設：  ) | 通道頻率相對於無線電中心頻率的偏移，可調整通道頻率，使通道不會重疊。 |
| **radio** (*radio0 \| radio1*; 預設： ) | 定義哪個無線電使用所選通道。 |
| **spread-factor** (*SF5 \| SF6 \| SF7 \| SF8 \| SF9 \| SF10 \| SF11 \| SF12*; 預設： ) | 定義 type=LoRa 通道的擴頻因子（Spread Factor）。擴頻因子越低，資料速率越高。 |

要檢視當前通道，請執行命令 `/iot/lora/channels/print`：

```ros
/iot/lora/channels/print
Columns: NAME, TYPE, RADIO, FREQ-OFF, BANDWIDTH, FREQ, SPREAD-FACTOR, DATARATE
# NAME       TYPE  RADIO   FREQ-OFF  BANDWIDTH  FREQ   SPREAD-FACTOR  DATARATE
0 gateway-0  MSF   radio1  -400000   125_kHz    868.1                         
1 gateway-0  MSF   radio1  -200000   125_kHz    868.3                         
2 gateway-0  MSF   radio1  0         125_kHz    868.5                         
3 gateway-0  MSF   radio0  -400000   125_kHz    867.1                         
4 gateway-0  MSF   radio0  -200000   125_kHz    867.3                         
5 gateway-0  MSF   radio0  0         125_kHz    867.5                         
6 gateway-0  MSF   radio0  200000    125_kHz    867.7                         
7 gateway-0  MSF   radio0  400000    125_kHz    867.9                         
8 gateway-0  LoRa  radio1  -200000   250_kHz    868.3  SF7                    
9 gateway-0  FSK   radio1  300000    125_kHz    868.8                    50000
```

通道是使用 `freq-off` 和無線電的 `center-freq` 頻率建立的。要檢視**無線電**的中心頻率，請使用命令 `/iot/lora/radios/print`。

要了解每個通道的頻率是如何計算的，請檢視下面的示例：

```ros
# NAME       TYPE  RADIO   FREQ-OFF  BANDWIDTH  FREQ   SPREAD-FACTOR  DATARATE
0 gateway-0  MSF   radio1  -400000   125_kHz    868.1                         
```

`radio1` 被選擇用於通道 #0，並且它被配置為 `center-freq=868500000`（868500000 Hz 或 868.5 MHz）。

透過使用頻率偏移 `freq-off=-400000`（-400000 Hz 或 -0.4 MHz），我們將通道 #0 定義為 `868500000-400000=868100000` Hz 或 868.1 MHz。

:::info
要配置自定義通道，請使用以下命令選擇 "custom" 通道配置檔案：

```ros
/iot/lora/set [find] channel-plan=custom
```
:::

## Join EUI {#join-eui}

閘道器會將它接收到的每一個 LoRaWAN 負載都轉發到伺服器。這也包括鄰近 LoRaWAN 節點的負載。轉發所有內容可能並不理想，例如，這會增加所使用的資料量（並直接影響 ISP 套餐費用）。

Join EUI 選單允許你指定一個 JOIN EUI 黑名單或白名單範圍，閘道器應轉發（如果為 "whitelisted"）或阻止（如果為 "blacklisted"）該範圍內的 JOIN EUI。新增範圍後，請確保將其應用到[伺服器](./general-properties.md#servers)設定。

過濾器按以下原則工作：

1) 預設情況下，允許所有內容（除非添加了 whitelist/blacklist 過濾器）；

2) **如果添加了 "blacklist" 過濾範圍**，並且附近出現一個與黑名單範圍匹配的 JOIN EUI 封包 → **它會被丟棄**；

3) **如果添加了 "whitelist" 過濾範圍，則其優先順序高於 "blacklist" 過濾器**。這意味著如果 "blacklist" 和 "whitelist" 都匹配同一個 JOIN EUI，則 "whitelist" 優先，封包會被轉發。

你可以藉助 RouterOS GUI 找到節點使用的 Join EUI。轉到 "LoRa" 部分，然後轉到 "Traffic" 子選單（僅在使用圖形介面時可用）。為 LoRaWAN 節點通電後，節點應傳送 "Join-request" 封包。雙擊該封包以檢查它：

![](/img/66e2220bdef5fcad.webp)

**子選單：** `/iot/lora/joineui`

| 屬性 | 描述 |
| :-- | :-- |
| **joineuis** (*string*; 預設： ) | 定義 Join EUI 範圍。 |
| **logging**(*yes \| no*; 預設：no) | 為過濾功能啟用額外日誌記錄。 |
| **name** (*string*; 預設： ) | 定義該範圍的名稱。 |
| **type** (blacklist \| whitelist; 預設：whitelist) | 定義過濾器型別：blacklist（如果範圍匹配，則阻止/丟棄封包）whitelist（如果範圍匹配，則轉發封包） |

Join EUI 的示例類似於 **E0 E1 E2 01 02 03 04 05**。它由 8 個十六進位制格式的八位組組成。

要新增一個**阻止所有內容**的範圍，請新增如下過濾器：

```ros
/iot/lora/joineui/add name=block_all joineuis=0000000000000000-ffffffffffffffff type=blacklist logging=yes
```

要允許某個特定的單個 Join EUI，請新增如下過濾器：

```ros
/iot/lora/joineui/add name=allow_my_node joineuis=E0E1E20102030405-E0E1E20102030405 type=whitelist logging=yes
```

停用 LoRa 介面：

```ros
/iot/lora/disable [find where ]
```

將兩個範圍都應用到正在使用的 LoRa 伺服器，並再次啟用介面：

```ros
/iot/lora/servers/set joineui=block_all,allow_my_node [find where address ~ "eu1.cloud.thethings.network"]
/iot/lora/enable [find where ]
```

結果，我們將只允許 "JOIN EUI=**E0 E1 E2 01 02 03 04 05**" 的節點負載被轉發，而其他所有可能的 JOIN EUI 都會被 blacklist 規則丟棄。

## 網路 ID {#network-id}

閘道器會將它接收到的每一個 LoRaWAN 負載都轉發到伺服器。這也包括鄰近 LoRaWAN 節點的負載。轉發所有內容可能並不理想，例如，這會增加所使用的資料量（並直接影響 ISP 套餐費用）。

NetID 選單允許你指定一個 NetID 黑名單或白名單範圍，閘道器應轉發（如果為 "whitelisted"）或阻止（如果為 "blacklisted"）該範圍內的 NetID。新增列表後，請確保將其應用到[伺服器](./general-properties.md#servers)設定。

過濾器按以下原則工作：

1) 預設情況下，允許所有內容（除非添加了 whitelist/blacklist 過濾器）；

2) **如果添加了 "blacklist" 過濾範圍**，並且封包的 NetID 與黑名單範圍匹配 → **它會被丟棄**；

3) **如果添加了 "whitelist" 過濾範圍，則其優先順序高於 "blacklist" 過濾器**。這意味著如果 "blacklist" 和 "whitelist" 都匹配同一個 NetID，則 "whitelist" 優先，封包會被轉發。

NetID 定義了 LoRaWAN 聯盟分配給不同運營商/伺服器的裝置地址（DevAddr）範圍。大多數範圍列表可在 [TTN 指南](https://www.thethingsnetwork.org/docs/lorawan/prefix-assignments/) 中找到。

在與伺服器進行通訊後，LoRaWAN 伺服器會為 LoRaWAN 節點分配 DevAddr。例如，[TTN](https://www.thethingsnetwork.org/) 會從 26000000 - 27FFFFFF 範圍內為你的節點分配一個地址。你可以在 LoRaWAN 伺服器儀表板下找到它，或使用 RouterOS GUI，在 "Traffic" 子選單下（在 "join-request" 和 "join-accept" 通訊發生後）的 Dev Addr 列/欄位中找到它。

假設 TTN 為你的節點分配了 **26 1B D8 D1** 這個 Dev Addr。根據 [TTN 指南](https://www.thethingsnetwork.org/docs/lorawan/prefix-assignments/)，它屬於 26000000 - 27FFFFFF DevAddr 範圍，並且屬於 **000013 NetID**。

**子選單：** `/iot/lora/netid`

| 屬性 | 描述 |
| :-- | :-- |
| **netids** (*string*; 預設： ) | 定義 NetID |
| **logging**(*yes \| no*; 預設：no) | 為過濾功能啟用額外日誌記錄。 |
| **name** (*string*; 預設： ) | 定義該 ID 的名稱。 |
| **type** (blacklist \| whitelist; 預設：whitelist) | 定義過濾器型別：blacklist（如果範圍匹配，則阻止/丟棄封包）whitelist（如果範圍匹配，則轉發封包） |

要新增允許特定 NetID 的過濾器（在本例中為屬於 TTN 的 **000013** NetID），請使用以下命令：

```ros
/iot/lora/netid/add name=allow_TTN netids=000013-000013 type=whitelist
```

要阻止所有其他 NetID，請使用 `type=blacklist`：

```ros
/iot/lora/netid/add name=block_all netids=000000-ffffff type=blacklist
```

停用 LoRa 介面：

```ros
/iot/lora/disable [find where ]
```

將兩個範圍都應用到正在使用的 LoRa 伺服器，並再次啟用介面：

```ros
/iot/lora/servers/set netid=block_all,allow_TTN [find where address ~ "eu1.cloud.thethings.network"]
/iot/lora/enable [find where ]
```

## 伺服器 {#servers}

本節用於新增新的伺服器設定或更改當前伺服器設定。

**子選單：** `/iot/lora/servers`

有幾個預定義伺服器可以使用（使用它們需要建立一個 [The Things Network](https://thethingsnetwork.org) 賬戶）：

```ros
[admin@MikroTik] /iot/lora/servers/print
Columns: NAME, UP-PORT, DOWN-PORT, ADDRESS
#  NAME              UP-PORT  DOWN-PORT  ADDRESS                                     
0  TTS Cloud (eu1)      1700       1700  eu1.cloud.thethings.industries         
1  TTS Cloud (nam1)     1700       1700  nam1.cloud.thethings.industries        
2  TTS Cloud (au1)      1700       1700  au1.cloud.thethings.industries         
3  TTN V3 (eu1)         1700       1700  eu1.cloud.thethings.network            
4  TTN V3 (nam1)        1700       1700  nam1.cloud.thethings.network           
5  TTN V3 (au1)         1700       1700  au1.cloud.thethings.network          
```

也可以新增自定義伺服器。如果第一個伺服器不更改封包的 "DevAddress" 部分，並且在所有伺服器都能解碼該封包的條件下，向多個伺服器轉發資料可以同時工作。

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*domain name or IP address*; 預設： ) | 定義 LoRaWAN 網路伺服器地址。 |
| **name** (*string*; 預設： ) | 定義伺服器名稱。 |
| **protocol** (*UDP \| LNS \| CUPS*; 預設：**UDP**) | 指定與 LoRaWAN 伺服器通訊時使用 UDP、LNS 還是 CUPS 協定。 |
| **down-port** (*integer [0..65535]*; 預設：**1700**) | 當選擇 UDP 協定時使用的引數。定義與 LoRaWAN 網路伺服器進行下行鏈路通訊（從伺服器到節點）的埠。大多數已知的開源伺服器預設使用埠 1700，但如果在同一臺機器上配置了多個伺服器，則該埠可能會更改。 |
| **up-port** (*integer [0..65535]*; 預設：**1700**) | 當選擇 UDP 協定時使用的引數。定義與 LoRaWAN 網路伺服器進行上行鏈路通訊（從節點到伺服器）的埠。大多數已知的開源伺服器預設使用埠 1700，但如果在同一臺機器上配置了多個伺服器，則該埠可能會更改。 |
| **netid**(*list of string*; 預設： ) | 當選擇 UDP 協定時使用的引數。應用過濾器，僅傳送與已配置的 Network ID (Net ID) 過濾器匹配的 LoRaWAN 負載。 |
| **joineui** (*list of string*; 預設： ) | 當選擇 UDP 協定時使用的引數。應用過濾器，僅傳送與已配置的 Join EUI 過濾器匹配的 LoRaWAN 負載。 |
| **port** (*integer [0..65535]*; 預設：**8887**) | 當選擇 LNS 或 CUPS 協定時使用的引數。對於 LNS，定義 WSS（WebSocket）埠；對於 CUPS，定義 HTTPS 埠。 |
| **key** (*string*; 預設： ) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 當選擇 LNS 或 CUPS 協定時使用的引數。指定 LoRa Basics Station LNS 認證金鑰或 CUPS API 金鑰（兩者均在伺服器上生成）。 |
| **ssl** (*yes or no*; 預設：no) | 當選擇 LNS 或 CUPS 協定時使用的引數。指定是否使用 SSL（如果伺服器支援 TLS 伺服器認證）。選擇此選項時，必須在 [certificates](../../authentication-authorization-accounting/certificates.md) 選單下上傳根 SSL 證書。 |
| **certificate** (*list of string*; 預設：**none**) | 當選擇 LNS 或 CUPS 協定時使用的引數。選擇用戶端[證書儲存中的證書](../../authentication-authorization-accounting/certificates.md)（如果伺服器等待 TLS 用戶端認證）。如果伺服器不要求 TLS 用戶端認證，請使用預設的 "**none**" 設定。 |
| **interval**(*integer [0..65535]*; 預設： ) | 當選擇 CUPS 協定時使用的引數。指定 LoRa Basics Station 向 CUPS 伺服器查詢配置更新/更改的時間間隔。 |

有幾個預配置的 The Things 預設伺服器。如果你刪除了其中一個並想恢復預設伺服器，可以使用以下命令：

```ros
/iot/lora/servers/reset-servers
```

:::warning
請注意，重設伺服器也會刪除所有先前配置的伺服器，因此請務必提前“儲存”它們。
:::

## 流量 {#traffic}

本節顯示周圍節點廣播的 LoRa 負載。

**子選單：** `/iot/lora/traffic`

| 屬性 | 描述 |
| :-- | :-- |
| **options** | 允許為 Traffic 標籤頁配置附加選項：crc-errors (yes \| no) → 設定為 "no" 可丟棄狀態為 "crc error" 的封包，使其不出現在 Traffic 標籤頁中；pckt-limit (10...1024) → 用於限制 Traffic 標籤頁的日誌列表。 |
| **clear** | 清除列表（刪除所有條目）。 |

要檢視列表，請使用 `print` 命令：

```ros
[admin@MikroTik] /iot/lora/traffic/print
Columns: TIME, GWID, MSGTYPE, DEVADDR, MVER, FCNT, CRC, TYPE, JOINEUI, DEVEUI
 #  TIME                             GWID  MSGTYPE                DEVADDR      MVER         FCNT  CRC    TY  JOINEUI                  DEVEUI                 
 0  2024-11-08 13:33:28  xxxxxxxxxxxxxxxx  Unconfirmed Data Up    6C B9 XX XX  LoRaWAN R1  59434  Error  Rx                                                  
 1  2024-11-08 13:33:50  xxxxxxxxxxxxxxxx  Rejoin-request                      LoRaWAN R1         Error  Rx                           50 62 9F FE XX XX XX XX
 2  2024-11-08 13:34:09  xxxxxxxxxxxxxxxx  Unconfirmed Data Down  5E 00 XX XX  RFU         41736  Error  Rx                                                  
 3  2024-11-08 13:34:15  xxxxxxxxxxxxxxxx  Rejoin-request                      RFU                Error  Rx                           D9 C2 BD 4B XX XX XX XX
 4  2024-11-08 13:34:55  xxxxxxxxxxxxxxxx  Join-request                        LoRaWAN R1         Error  Rx  A1 AE B1 8A XX XX XX XX  F4 62 81 BE XX XX XX XX
```

要清除列表（刪除所有條目），請執行 `clear` 命令：

```ros
[admin@MikroTik] /iot/lora/traffic/clear
```

Traffic 標籤頁顯示 "LoRa" 負載。一旦使用 `/iot/lora/enable [find]` 命令啟用 LoRa 介面，列表中的所有負載都會被轉換為 TCP/UDP 封包（取決於你使用的是 UDP 1700 還是 LNS/CUPS 協定），並轉發到已配置的伺服器。

如果你不想使用 LoRaWAN 拓撲，並且希望將“原始”LoRa 負載轉發到你自己的伺服器，可以選擇使用 [MQTT](../mqtt/index.md) 或 [獲取](../../system-information-and-utilities/fetch.md)，按你選擇的時間間隔執行指令碼以持續傳送資料。

關於如何將流量負載轉換為名為 "traffic" 的變數的基本示例（指令碼中的第一步）：

```ros
[admin@MikroTik] > :global traffic;:set traffic [/iot/lora/traffic/print as-value ];put $traffic 
.id=*4f;band=125 kHz;coderate=?/?;counter=890652548;crc=Error;datarate=SF 7;freqhz=868300;gwid=50313xxxxxx;ifcha
in=1;mod=LoRa;msgtype=Proprietary;mver=RFU;rfchain=1;rssi=-116.00;rxcrc=3809;size=213;snr=-12.00;snrmax=-8.25;snrmin=
-14.25;time=2024-11-08 14:39:45;type=Rx
```

## 偵錯 {#debugging}

如果連接出現問題，請確保啟用日誌：

```ros
/system/logging/add topics=debug,lora
```

這將啟用偵錯日誌記錄，並幫助你確定潛在問題所在。可以使用以下命令檢視日誌：

```ros
/log/print
```

成功連線的外觀如下：

```ros
 13:50:33 lora,info gateway-0 forwarder started
 13:50:38 lora,info [LNS] connecting to wss://eu1.cloud.thethings.network:8887/router-info
 13:50:39 lora,info [LNS] eu1.cloud.thethings.network discovered
 13:50:39 lora,info [LNS] eu1.cloud.thethings.network disconnected
 13:50:39 lora,info [LNS] connecting to wss://eu1.cloud.thethings.network:8887/traffic/eui-xxxx
 13:50:39 lora,info [LNS] eu1.cloud.thethings.network configured
 13:50:52 lora,info gateway-0 forwarder is ready
```

更多日誌資訊可在我們的[日誌](../../diagnostics-monitoring-and-troubleshooting/log/index.md)指南中找到。
