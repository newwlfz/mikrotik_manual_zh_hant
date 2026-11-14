---
sidebar_key: "internet-of-things/wiliot"
sidebar_position: 6
title: "威利奧特"
sidebar_label: "威利奧特"
description: "Wiliot 是一家物聯網公司，提供無電池藍牙標籤，用於廣播遙測資料，需要具備藍牙支援的 MikroTik RouterOS 裝置來實現閘道器和橋接模式。該文件指導使用者將 MikroTik 板卡註冊為 Wiliot 閘道器，包括 API token 設定和 MQTT 連線的建立。"
tags:
  - 'wiliot'
  - 'mqtt'
  - 'bluetooth'
source: https://manual.mikrotik.com/docs/7.24/internet-of-things/wiliot
captured_at: '2026-11-04T11:31:46+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**[Wiliot](https://www.wiliot.com/company)** 是一家 **物聯網** 公司，以其 [IoT Pixels](https://www.wiliot.com/product/iot-pixels)（標籤）等解決方案而聞名。Pixel 的一大優勢在於它是一種無需電池、標籤大小（緊湊）的藍牙“標籤”（會廣播帶有遙測資料的藍牙信標）。

- 要為 IoT Pixel 供電，你需要一個 bridge（“energizer”）裝置。它透過無線電波提供“能量”，並從遠處為 IoT Pixel 供電。
- 要將 IoT Pixel 的資料轉發到伺服器（“dashboard”），你需要一個 gateway 裝置。它使用 TCP/IP 連線與伺服器建立連線，並轉發包含感測器資料（例如溫度）的標籤負載。

這兩種執行模式可以由單個裝置執行，也可以由不同裝置執行。

RouterOS 允許在支援藍牙的裝置上使用 Wiliot 的 `gateway` 和 `bridge` 模式。

Wiliot `gateway` 模式負責與 MQTT 伺服器建立連線（透過 API 註冊閘道器、獲取所需的令牌和憑據，並對裝置進行授權）。它還負責透過已建立的 MQTT 連線轉發其無線捕獲的 Pixel 藍牙負載，並負責透過藍牙廣播中繼它可能從已訂閱的 MQTT 主題收到的附加命令。

Wiliot `bridge` 模式負責透過該頻率提供能量，並保持 IoT Pixel 供電。

:::warning
`bridge` 模式尚未實現。
:::

## 分步操作 {#step-by-step}

分步操作需要兩個快速步驟：

1. 註冊裝置並激活 MikroTik 板；
2. 設定 IoT Pixel。

### 步驟 #1，網關注冊 {#step-1-gateway-registration}

#### 在 Wiliot 門戶上 {#on-the-wiliot-portal}

- 登入 Wiliot 註冊頁面 →  [https://deployment-tool.wiliot.com](https://deployment-tool.wiliot.com)

![](/img/b2a9c9652ca2bb5d.webp)

- 選擇“Gateway Registration”。
- 選擇“Manual input”（螢幕右上角）。
- 輸入“Gateway ID”。

你可以從 RouterOS 設定（`gateway-id` 欄位）中複製“Gateway ID”：

```routeros
[admin@MikroTik] > /iot wiliot configuration print
                  status: inactive                
              gateway-id: XXXXXXXXX          
                    type: mikrotik-knot-embedded
                   owner: xxxx              
               spoof-gps: xx                   
                     lat: xx                    
                    long: xx                    
  token-refresh-handicap: 3600                  
                  server: Wiliot US East        
                 scanner: bt1                   
              advertiser: bt1                   
                   wi-fi: none                  
                features: gateway  
```

- 新閘道器應在平臺上以“pre-registered”狀態出現 → [https://platform.wiliot.com/edge/gateways](https://platform.wiliot.com/edge/gateways)

#### 在 RouterOS 中 {#in-the-routeros}

:::info
你可以使用不同的工具來瀏覽設定。建議的管理方式是使用 [Winbox](../management-tools/winbox.md) 軟體。[使用此連結下載該工具](https://mikrotik.com/download/winbox)並執行它。用乙太網線將你的 PC 連線到任何以 ether2+ 開頭的埠（避免使用 ether1，因為在大多數情況下它被配置為 WAN 埠並受防火牆限制，而其餘埠是開放訪問且啟用了 DHCP-server 的 LAN 埠），或者使用 Wi-Fi 連線（如果板上有 Wi-Fi 晶片）。

在 Winbox 中，導航到“Neighbors”標籤頁（Select from: Neighbors），找到你的 MikroTik 板的 MAC 地址（它印在裝置標籤上），點選該 MAC 地址，輸入登入憑據（也印在標籤上）並“connect”到它。

從這裡，你可以使用“GUI”或“CLI”命令。**本指南展示“CLI”命令示例**，你可以透過從 Winbox 選項中開啟“New Terminal”來執行這些示例。但是，GUI 中也提供完全相同的部分和標籤頁。例如，如果命令顯示為“**`/iot/wiliot/enable`**”，請轉到 **IoT→ Wiliot** 標籤頁，並點選“**enable**”按鈕。
:::

- 啟用“wiliot”功能。

```routeros
[admin@MikroTik] > /iot/wiliot/enable
```

- 確認裝置已成功獲取令牌、獲得授權，並以“**active**”狀態（`status: active`）連線到 MQTT 伺服器。

```routeros
[admin@MikroTik] > /iot/wiliot/configuration/print
                  status: active                  
              gateway-id: XXXXXXXXX           
                    type: mikrotik-knot-embedded
                   owner: xxxx              
  token-refresh-handicap: 3600                  
                  server: Wiliot US East        
                 scanner: bt1                   
              advertiser: bt1                   
                   wi-fi: none                  
                features: gateway               
```

 Gateway 狀態應在 Wiliot 平臺上從“pre-registered”變為“approved”（和/或變為“online”）→ [https://platform.wiliot.com/edge/gateways](https://platform.wiliot.com/edge/gateways)

### 步驟 #2，新增 IoT Pixel（標籤） {#step-2-adding-iot-pixel-label}

#### 在 Wiliot 門戶上 {#on-the-wiliot-portal-1}

- 登入 Wiliot 平臺並導航到“Category”標籤頁 → [https://platform.wiliot.com/categories](https://platform.wiliot.com/categories)。新增新的“Category”（“Add new”）。為其命名並選擇所需的類別型別。
- 導航到“Pixels”標籤頁 → [https://platform.wiliot.com/edge/pixels](https://platform.wiliot.com/edge/pixels)。檢查標籤的“ID”。標籤應已分配給你的賬戶。
- 轉到“Assets”標籤頁 → [https://platform.wiliot.com/assets](https://platform.wiliot.com/assets)。建立新資產（“Add New”）。將該資產選擇/連結到之前建立的“Category”，輸入“Asset ID”（或生成一個隨機 ID），並從列表中選擇 Pixel 的 ID。
- 透過點選已建立的“asset”條目（一旦標籤被供能且閘道器就緒），你將能夠看到標籤的讀數（溫度等）。

## RouterOS 設定 {#routeros-settings}

**子選單：** `/iot/wiliot`

***注意**：* 需要 **iot** 軟體包。

| 屬性 | 描述 |
| :-- | :-- |
| **configuration** | 常規 Wiliot gateway/bridge 設定。 |
| **servers** | MQTT 伺服器配置。 |
| **bluetooth traffic** | 藍牙流量選單。 |
| **mqtt traffic** | MQTT 流量選單。 |

### 配置（常規選項） {#configuration-general-options}

要啟用配置，請使用命令：

```routeros
/iot/wiliot/enable
```

要停用配置：

```routeros
/iot/wiliot/disable
```

要清除（purge）MQTT 連線/認證資料（僅在“disabled”狀態下可用）：

```routeros
/iot/wiliot/disable
/iot/wiliot/clear
```

:::info
“清除”配置後，你將必須刪除閘道器（[https://platform.wiliot.com/edge/gateways](https://platform.wiliot.com/edge/gateways)），並重新註冊閘道器（[https://deployment-tool.wiliot.com/](https://deployment-tool.wiliot.com/)）。
:::

配置屬性可以使用“set”命令應用（僅在“disabled”狀態下可用）：

```routeros
/iot/wiliot/set
```

示例：

```routeros
/iot/wiliot/set features=gateway
```

| 屬性 | 描述 |
| :-- | :-- |
| **advertiser** (預設：bt1) | 選擇將用於廣播（中繼從 MQTT 伺服器獲取的命令）的藍牙介面。 |
| **scanner** (預設：bt1) | 選擇將用於掃描（捕獲 Pixel 的負載）的藍牙介面。 |
| **spoof-gps** (*yes \| no*; 預設：no) | 選擇是否使用將傳送到伺服器的手動 GPS 座標。 |
| **lat** (預設：) | 設定在使用“spoof-gps”時與伺服器連線期間要包含的 GPS 緯度值。 |
| **long** (預設：) | 設定在使用“spoof-gps”時與伺服器連線期間要包含的 GPS 經度值。 |
| **features** (*gateway \| bridge* ; 預設：) | 選擇裝置的角色：gateway。在此模式下，裝置與伺服器建立 MQTT 連線，並將其捕獲的 IoT Pixel 信標轉發給伺服器。它還會向附近的 bridge 廣播從已訂閱主題收到的命令。bridge。在此模式下，裝置為周圍的 IoT Pixel 供能（為其供電）。**注意：** `bridge` 模式尚未實現。  |
| **server**(預設：) | 設定用於 MQTT 連線的伺服器。 |

### 伺服器 {#servers}

要更改 MQTT 伺服器的設定：

| 屬性 | 描述 |
| :-- | :-- |
| **address** (預設：) | MQTT 伺服器的 IP/域名地址。 |
| **certificate** (預設：) | 指定在伺服器要求時用於 SSL MQTT 連線的證書。 |
| **name** (預設：) | 伺服器名稱。 |
| **port** (預設：) | MQTT 伺服器使用的 TCP 埠。 |
| **ssl** (yes \| no; 預設：) | 啟用與伺服器的 SSL 通訊。 |

### 藍牙流量 {#bluetooth-traffic}

顯示附近 IoT Pixel 的原始資料：

```routeros
/iot/wiliot/bluetooth-traffic/print 
Columns: TIME, ADDRESS, RSSI, PAYLOAD
 #  TIME        ADDRESS            RSSI    PAYLOAD                                                                                     
 0  2026-01-07  E9:B7:32:XX:XX:XX  -34dBm  1E 16 C6 FC 03 00 7C 7B 3C 22 0E D8 54 38 B0 03 E0 DA 8C 06 36 B4 CF AC 8A D6 76 54 BD FC B9
    14:23:26                                                                                                                           
 1  2026-01-07  E9:B7:32:XX:XX:XX  -41dBm  1E 16 C6 FC 03 00 3C DB 7D 72 BF A0 C1 62 9C 5F B6 D5 90 00 C1 62 BF 68 EC E5 64 02 63 F9 C3
    14:23:26                                                                                                                           
 2  2026-01-07  E9:B7:32:XX:XX:XX  -42dBm  1E 16 C6 FC 03 00 3C A8 3B 27 17 25 BC 6D 01 F5 49 E1 98 03 CA 3C 64 04 30 B2 E1 86 FC 80 CB
    14:23:28                                                                                                                           
 3  2026-01-07  E9:B7:32:XX:XX:XX  -33dBm  1E 16 C6 FC 03 00 3C F5 AF 22 CC E2 60 FA BC 4E 57 F7 8C 01 80 6A 21 EF 82 CB 62 2A 16 5A 3F
    14:23:29                                                                                                                           
 4  2026-01-07  E9:B7:32:XX:XX:XX  -33dBm  1E 16 C6 FC 03 00 3C FC AC 9A 1B 9A BD 2C DE B7 02 FF 7C 03 C7 28 BD AB 20 1B 91 89 B9 ED 88
```

### MQTT 流量 {#mqtt-traffic}

顯示 MQTT 流量：

```routeros
/iot/wiliot/mqtt-traffic/print
   time: 2026-03-02                                                                                                                      >
         07:37:43                                                                                                                        >
  topic: update/mikrotik/XXXXXXXXXXX                                                                                                     >
   data: {"txPacket":"1E16C6FC0000ED070C3443B7D39DE2CE08993D7F40B2F56B822096AA19CD00","txMaxRetries":8,"txMaxDurationMs":700,"action":0} >
```

### 偵錯 {#debugging}

你可以使用以下命令啟用“wiliot”偵錯日誌：

```routeros
/system/logging
add topics=wiliot
```

結果，你應該會在日誌中看到更詳細的條目（`/log/print` 命令）：

```routeros
 2026-02-12 12:04:54 wiliot,debug [CFG] authorizing...
 2026-02-12 12:04:54 wiliot,debug [CFG] authorization complete
 2026-02-12 12:04:54 wiliot,debug [CFG] registering...
 2026-02-12 12:04:55 wiliot,debug [CFG] registration complete
 2026-02-12 12:04:55 wiliot,debug [CFG] polling for token...
 2026-02-12 12:04:55 wiliot,debug [CFG] token obtained
 2026-02-12 12:04:55 wiliot,debug [CFG] ownerId
 2026-02-12 12:04:55 wiliot,debug [CFG] authorization complete
 2026-02-12 12:04:55 wiliot,debug [CFG] updating MQTT credentials
 2026-02-12 12:04:56 wiliot,debug [CFG] MQTT credentials updated
 2026-02-12 12:04:56 wiliot,debug [CFG] connecting to MQTT server
  2026-02-12 12:04:56 wiliot,debug [CFG] subscribing to BLE advertisements
 2026-02-12 12:04:56 wiliot,debug [CFG] active
```

### 證書 {#certificates}

Wiliot 功能使用 [/tool/fetch](../system-information-and-utilities/fetch.md) 發起 HTTP POST，並使用 [/mqtt](./mqtt/index.md) 建立 MQTT 連線。HTTP 和 MQTT 都需要 SSL 證書。RouterOS 有一個“builtin trust store”，其中從一開始就包含所有必需的證書。

**[預設情況下](../authentication-authorization-accounting/certificates.md#settings)，** “**all**” **服務應被允許使用內建證書儲存**，因此你無需執行任何操作。但是，如果你決定限制此行為（如果你決定不允許“all”服務訪問“store”），為了讓“wiliot”正常工作，你需要啟用“wiliot”、“mqtt”和“fetch”服務（或停用 builtin-trust-store 並手動上傳證書）：

```routeros
[admin@MikroTik] > /certificate/settings/print
  builtin-trust-store: fetch                    
                       mqtt                      
                       wiliot                     
         crl-download: no    
              crl-use: no    
            crl-store: ram 
```
