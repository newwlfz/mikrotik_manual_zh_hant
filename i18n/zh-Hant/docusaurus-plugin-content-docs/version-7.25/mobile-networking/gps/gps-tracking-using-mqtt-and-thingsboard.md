---
sidebar_key: "mobile-networking/gps/gps-tracking-using-mqtt-and-thingsboard"
sidebar_position: 2
title: "使用 MQTT 和 ThingsBoard 進行 GPS 跟蹤"
sidebar_label: "使用 MQTT 和 ThingsBoard 進行 GPS 跟蹤"
description: "本頁面介紹如何在 MikroTik RouterOS 上使用 MQTT 和 ThingsBoard 配置 GPS 跟蹤，詳細說明了支援 GPS 的裝置向伺服器傳送位置資料的設定步驟。內容涵蓋代理配置、裝置憑據生成，以及 SSL 和非 SSL 兩種環境下的 MQTT 釋出命令。"
tags:
  - 'mqtt'
  - 'thingsboard'
  - 'gps'
source: https://manual.mikrotik.com/docs/7.25/mobile-networking/gps/gps-tracking-using-mqtt-and-thingsboard
captured_at: '2026-11-04T11:22:30+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

許多 RouterOS 裝置支援 [GPS](./index.md)。它允許 RouterOS 確定其 GPS 接收器的精確位置。GPS 座標將指示當前位置的緯度值和經度值（以及其他引數）。

假設你有一臺 [LTAP](https://mikrotik.com/product/ltap)（或任何其他支援 GPS 的 RouterOS 裝置），並且希望跟蹤它的位置。你希望路由器將這些資料傳送到伺服器，資料將在那裡儲存並整合到地圖中，因為這樣更方便監控。在本指南中，我們將展示如何做到這一點。本場景將使用 MQTT 協定與一個名為 [ThingsBoard](https://thingsboard.io/) 的平臺通訊。

ThingsBoard 提供雲解決方案以及不同的本地安裝選項（可在不同作業系統上安裝）。

由於我們添加了 [container](../../containers/index.md) 功能，現在也可以在 RouterOS 內執行該平臺。這意味著，你可以完全在 RouterOS 裝置上構建此場景 → 即你希望跟蹤的、支援 GPS 的裝置（例如，配備 [LTAP](https://mikrotik.com/product/ltap) 的汽車 → 充當 **MQTT 釋出者** 的 RouterOS 裝置），以及執行在更強大的 RouterOS 裝置內的 ThingsBoard 伺服器（例如，[CHR](../../getting-started/routeros-licensing/chr/index.md) 機器 → 充當 **MQTT 代理** 的 RouterOS 裝置）。

如果你選擇這條路線（container 路線），請務必仔細選擇你計劃用作“伺服器”的裝置，因為此實現可能會佔用大量 RAM（建議使用至少具有 **2 GB** **RAM** 的裝置，或具有 **1 GB RAM** **且負載極低** 的裝置，並且架構為 **ARM64** 或 **AMD64**）。

## 配置 {#configuration}

在本指南中，我們將演示如何配置 GPS 接收器（MQTT 釋出者）以及如何設定 ThingsBoard。

如果你想使用 container 功能來執行 ThingsBoard 例項（MQTT 代理），請檢視[此處](../../containers/user-guides/container-thingsboard-mqtt-http-server.md)的指南。有關 ThingsBoard 和 MQTT 配置的通用指南可在[此處](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md)找到。請務必檢視這兩份指南，因為它們包含額外的有用資訊。

繼續之前，請確保 ThingsBoard 已啟動並執行，並且你可以訪問其 WEB 管理門戶。確認 MQTT 埠已開放和/或已正確進行埠轉發。

### ThingsBoard 準備工作 {#thingsboard-preparation}

:::info
為簡單起見，本示例將展示 [access-token](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md#access-token-scenario-1) 和[透過 access-token 的單向 SSL 通訊](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md#one-way-ssl-communication-scenario)場景，但你也可以使用其他可用選項。
:::

轉到“**裝置**”選單，並透過“**新增新裝置**”按鈕新增新裝置 → 為其命名並建立（例如 LTAP）：

![](/img/062635ec753a108d.webp)

單擊你剛剛新增的裝置，轉到“**詳細資訊**”部分，並在“**管理憑據/裝置憑據**”設定下生成訪問令牌：

![](/img/cb33058054456e88.webp)

### MQTT 代理配置 {#mqtt-broker-configuration}

如果是本地測試，或代理可透過 VPN 訪問，你可以使用非 SSL MQTT：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=1883 username=access_token
```

其中：

- `name` 是你希望給代理指定的名稱，該名稱稍後將在指令碼中使用。
- `address` 是代理的 IP 地址。
- `port` 是代理監聽的 TCP 埠 → 對於非 SSL，通常是 TCP 1883。
- `username` 由 MQTT 代理決定，在我們的情況下，它是在 ThingsBoard 管理門戶中生成的“訪問令牌”。

如果是公共訪問（當你希望透過代理的公網 IP 地址訪問它時），**我們建議使用 SSL MQTT**：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=8883 username=access_token ssl=yes
```

其中：

- `name` 是你希望給代理指定的名稱，該名稱稍後將在指令碼中使用。
- `address` 是代理的 IP 地址。
- `port` 是代理監聽的 TCP 埠 → 對於 SSL，通常是 TCP 8883。
- `username` 由 MQTT 代理決定，在我們的情況下，它是在 ThingsBoard 管理門戶中生成的“訪問令牌”。
- `ssl` 啟用 SSL MQTT 通訊。

### MQTT 釋出 {#mqtt-publish}

你可以使用以下命令透過靜態訊息測試 MQTT 釋出：

```ros
/iot/mqtt/publish broker="tb" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

要釋出 GPS 座標，請匯入下面顯示的指令碼：

```ros
/system/script/add dont-require-permissions=no name=mqttgps owner=admin policy="ftp,re\
    boot,read,write,policy,test,password,sniff,sensitive,romon" \
    source="    ###Configuration###\r\
    \n    #Enter pre-configured broker's name within \"\":\r\
    \n    :local broker \"tb\"\r\
    \n    #Enter the topic name within \"\", per the broker's config\
    uration:\r\
    \n    :local topic \"v1/devices/me/telemetry\"\r\
    \n\r\
    \n    ###Variables####\r\
    \n    :global lat\r\
    \n    :global lon\r\
    \n    :global alt1\r\
    \n    :global alt2\r\
    \n\r\
    \n    ###GPS####\r\
    \n    :put (\"[*] Capturing GPS coordinates...\")\r\
    \n    /system/gps/monitor once do={\r\
    \n    :set \$lat \$(\"latitude\");\r\
    \n    :set \$lon \$(\"longitude\");\r\
    \n    :set \$alt1 \$(\"altitude\")}\r\
    \n    ###remove \"meters\" from the value because JSON format wi\
    ll not understand it###\r\
    \n    :set \$alt2 [:pick \$alt1 0 [find \$alt1 \" m\"]]\r\
    \n\r\
    \n    :local message \\\r\
    \n    \"{\\\"latitude\\\":\$lat,\\\r\
    \n    \\\"longitude\\\":\$lon,\\\r\
    \n    \\\"altitude\\\":\$alt2}\"\r\
    \n\r\
    \n    ###MQTT###\r\
    \n    :if (\$lat != \"none\") do={\\\r\
    \n    :put (\"[*] Sending message to MQTT broker...\");\r\
    \n    /iot/mqtt/publish broker=\$broker topic=\$topic message=\$\
    message} else={:put (\"[*] Latitude=none, not posting anything!\
    \");:log info \"Latitude=none, not posting anything!\"}"
```

簡而言之，該指令碼會捕獲 GPS 資訊，具體來說是緯度、經度和海拔值。然後它會用這些值構造一條 JSON 訊息。如果指令碼啟動時 latitude 值不等於 "none"（即等於任何實際數值）→ 它會透過 MQTT 將 JSON 訊息傳送到名為“**tb**”的代理。如果無法捕獲 GPS 資料 → "latitude" 會被識別為 "none" → 指令碼只會記錄無法捕獲任何內容，不會執行其他操作。

這是一個非常基礎的示例。你可以根據自己的需求修改指令碼，新增自己的 "if"（例如在沒有 GPS 訊號時傳送電子郵件通知）以及其他引數（任何其他 RouterOS 捕獲的值，比如其韌體版本）。

使用以下命令執行指令碼：

```ros
/system/script/run mqttgps 
[*] Capturing GPS coordinates...
        date-and-time: 2023-02-01 10:39:37
             latitude: 56.969862
            longitude: 24.162425
             altitude: 31.799999 m
                speed: 1.000080 km/h
  destination-bearing: none
         true-bearing: 153.089996 deg. True
     magnetic-bearing: 0.000000 deg. Mag
                valid: yes
           satellites: 6
          fix-quality: 1
  horizontal-dilution: 1.42
             data-age: 0s
[*] Sending message to MQTT broker...
```

要自動化該過程，請新增一個 [scheduler](../../system-information-and-utilities/scheduler.md)（例如每 30 秒執行一次指令碼）：

```ros
/system/scheduler/add name=mqttgpsscheduler interval=30s on-event="/system/script/run mqttgps"
```

## 結果驗證 {#result-verification}

轉到你所建立裝置下的“最新遙測”部分，並確認資料已釋出：

![](/img/0a8a6c973a9c90b9.webp)

## 使用地圖進行資料視覺化 {#data-visualization-using-maps}

ThingsBoard 允許你使用 [Widgets](https://thingsboard.io/docs/user-guide/ui/widget-library/) 建立美觀的儀表板。在我們的場景中，我們希望跟蹤 LTAP 的 GPS 座標，因此需要一個地圖小元件。

選擇 latitude 和 longitude 值，然後單擊“**在小元件上顯示**”按鈕：

![](/img/37aa7ead6b186573.webp)

找到“**Maps**”包，然後單擊“**新增到儀表板**”：

![](/img/6baa63ad7eaf37e5.webp)

選擇一個現有儀表板，或建立一個新儀表板並隨意命名：

![](/img/d095d56ffccb51fd.webp)

透過 scheduler 或手動執行指令碼，並檢查結果：

![](/img/ccc0acdea12f403a.webp)

現在，我們可以將其安裝在一個移動目標上並跟蹤其位置：

![](/img/2225362d4a81fbe9.webp)
