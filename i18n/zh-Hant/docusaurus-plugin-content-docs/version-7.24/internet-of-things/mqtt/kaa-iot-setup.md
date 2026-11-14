---
sidebar_key: "internet-of-things/mqtt/kaa-iot-setup"
sidebar_position: 1
title: "Kaa IoT 設定"
sidebar_label: "Kaa IoT 設定"
description: "本頁面介紹面向 MikroTik RouterOS 的 Kaa IoT 設定，涵蓋 MQTT 和 HTTP 協定支援、透過指令碼進行系統資源監控，以及 Kaa IoT 門戶配置步驟，包括建立應用/裝置和管理端點令牌。頁面還概述了 RouterOS 的前提條件，例如網際網路訪問，以及為使用 MQTT 而可選安裝 iot 軟體包。"
tags:
  - 'mqtt'
  - 'http'
  - 'scripting'
source: https://manual.mikrotik.com/docs/7.24/internet-of-things/mqtt/kaa-iot-setup
captured_at: '2026-11-04T11:31:51+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[MQTT](./index.md) 和 [HTTP](../../system-information-and-utilities/fetch.md) 是用於傳輸各類資料的最流行協定之一。這兩種協定在不同 IoT 部署中都被大量使用，並且它們都受 [RouterOS](../../getting-started/software-specifications/index.md) 支援。

您可能會問，是什麼型別的資料？幾乎任何資料……RouterOS [指令碼](../../developer-guides/scripting/index.md) 是一個非常強大的工具，可以藉助[排程](../../system-information-and-utilities/scheduler.md)幫助您自動化裝置。

例如，您可以藉助命令 `/system/resource/print` 檢查系統的資源資訊：

```ros
/system/resource/print
                   uptime: 4d1h37m55s
                  version: 7.14.3 (stable)
               build-time: 2024-04-17 12:47:58
         factory-software: 6.45.9
              free-memory: 926.0MiB
             total-memory: 1024.0MiB
                      cpu: ARM
                cpu-count: 4
            cpu-frequency: 533MHz
                 cpu-load: 0%
           free-hdd-space: 88.5MiB
          total-hdd-space: 128.0MiB
  write-sect-since-reboot: 1107
         write-sect-total: 1447413
               bad-blocks: 0%
        architecture-name: arm
               board-name: RB1100AHx4
                 platform: MikroTik
```

該命令會顯示有用的資訊，例如 CPU 使用率、RAM 記憶體使用率、裝置執行時間及其韌體版本。另一個命令會輸出 [GPS](../../mobile-networking/gps/index.md) 座標（如果裝置內建 GPS 晶片）等等……

本質上，這意味著任何能夠“列印輸出”到 RouterOS [終端](../../management-tools/console.md)的內容，都可以透過指令碼組織成 JSON 格式訊息，並按配置的間隔傳送出去。我們將在本指南後面展示一個更詳細的示例。

換句話說，您可以將 MikroTik 中的資料傳送到您選擇的任何 MQTT 或 HTTP 伺服器。[Kaa IoT](https://www.kaaiot.com/) 就是這樣一個伺服器。

[為什麼選擇 Kaa IoT？](https://www.kaaiot.com/advantages/platform)

## Kaa IoT 配置 {#kaa-iot-configuration}

請務必檢視 [KAA：連線您的第一臺裝置](https://www.kaaiot.com/docs/tutorials/getting-started/connecting-your-first-device)。

登入門戶後，首先請按照[操作手冊](https://www.kaaiot.com/docs/tutorials/getting-started/connecting-your-first-device)中的步驟操作：

a) 在 "**Home>Device management>Applications**" 下，點選 "**Add application**" 按鈕建立應用，為其命名，然後點選 "**Create**"：

![](/img/bac400b8d4d8d195.webp)

b) 在 "**Home>Device management>Devices**" 下，點選 "**Add device**" 按鈕建立裝置，為其命名，然後點選 "**Create**"：

![](/img/9497b03be79a6946.webp)

輸入您自己的 "Endpoint token"，或讓系統自動生成一個。請務必“儲存”它（因為之後您將無法再次訪問它）。

剩下要做的就是使用 MQTT 或 HTTP 將我們的路由器連線到伺服器，釋出一些資料，並自定義我們的第一個儀表板，以便更輕鬆地將其視覺化。

## RouterOS 配置 {#routeros-configuration}

首先，裝置應具備網際網路訪問能力。請檢視我們的[首次配置](../../getting-started/first-time-configuration.md)指南。

網際網路正常執行後，如果您計劃使用 [MQTT](./index.md) 協定，請確保已安裝 **iot** 軟體包。您可以從我們的[下載頁面](https://mikrotik.com/download)下載它，位於 "Extra packages" 檔案中（對應您裝置的架構）。解壓 "Extra packages" 檔案，並將 **iot** 軟體包上傳到 "[檔案](../../system-information-and-utilities/files.md)"（之後重啟裝置）。如果您只計劃使用 [HTTP 傳送](../../system-information-and-utilities/fetch.md)，則無需安裝 iot 軟體包。

在繼續之前，請參閱 Kaa IoT 的 [MQTT](https://www.kaaiot.com/docs/device-connectivity/mqtt-device-api) 和 [HTTP](https://www.kaaiot.com/docs/device-connectivity/http-device-api) 裝置 API 指南。

### 使用 HTTP 傳送資料 {#using-http-to-post-the-data}

要釋出一條基本 JSON 訊息：

```bash
{"test":"data"}
```

只需執行以下命令：

```ros
/tool/fetch url="https://next.kaaiot.com/kpc/kp1/<app-version>/epmx/<token>/update/keys" http-method=post  http-header-field="Content-Type: application/json" http-data="{\"test\":\"data\"}" output=user mode=https
```

其中應將 `<app-version>`（可在 "**Home>Device management>Devices>Specific device**" 標籤頁下檢視）和 `<token>`（您在平臺上建立裝置後生成的）替換為各自的值。

您應該能看到在 "**Home>Device management>Devices>Specific device>Overview**" 標籤頁下出現了新的 "Metadata" 值，或在 "**Home>Device management>Devices>Specific device>Data logs"** 標籤頁下檢視日誌。

要收集 `/system/resource/print` 資訊併發布它，我們可以使用指令碼。將下面所示指令碼的內容複製並貼上到命令列中：

```ros
/system/script
add dont-require-permissions=no name=systeminfo owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#####################\
    ############### System ###################################\r\
    \n:put (\"[*] Gathering system info...\")\r\
    \n:local cpuLoad [/system/resource/get cpu-load];\r\
    \n:local freeMemory [/system/resource/get free-memory];\r\
    \n:local usedMemory ([/system/resource/get total-memory] - \$freeMemory);\r\
    \n:local rosVersion [/system/package/get value-name=version \\\r\
    \n[/system/package/find where name ~ \"^routeros\"]];\r\
    \n:local model [/system/routerboard/get value-name=model];\r\
    \n:local serialNumber [/system/routerboard/get value-name=serial-number];\r\
    \n:local upTime [/system/resource/get uptime];\r\
    \n\r\
    \n#################################### message #####################################\r\
    \n:local message \\\r\
    \n\"{\\\"model\\\":\\\"\$model\\\",\\\r\
    \n\\\"sn\\\":\\\"\$serialNumber\\\",\\\r\
    \n\\\"ros\\\":\\\"\$rosVersion\\\",\\\r\
    \n\\\"cpu\\\":\\\"\$cpuLoad\\\",\\\r\
    \n\\\"umem\\\":\\\"\$usedMemory\\\",\\\r\
    \n\\\"fmem\\\":\\\"\$freeMemory\\\",\\\r\
    \n\\\"uptime\\\":\\\"\$upTime\\\"}\"\r\
    \n\r\
    \n:log info \"\$message\";\r\
    \n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
    \n:put (\"[*] Sending message...\")\r\
    \n/tool/fetch url=\"https://next.kaaiot.com/kpc/kp1/<app-version>/epmx/<token>/up\
    date/keys\" http-method=post  http-header-field=\"Content-Type: application/json\" http-data=\
    \"\$message\" output=user mode=https\r\
    \n:put (\"[*] Done\")"
```

更改 URL 中的 `<app-version>` 和 `<token>` 值。然後使用以下命令執行指令碼：

```ros
/system/script/run systeminfo
```

JSON 訊息將如下所示：

```bash
{
  "model": "RB924iR-2nD-BT5&BG77",
  "sn": "XXXXXXX",
  "ros": "7.99",
  "cpu": "7",
  "umem": "45113344",
  "fmem": "21995520",
  "uptime": "4d22:16:08"
}
```

### 使用 MQTT 傳送資料 {#using-mqtt-to-post-the-data}

為了使用單向 SSL MQTT 場景，請透過點選 "**Get root certificate**" 按鈕，從 "**Home>Device management>Credentials**" 獲取根證書。更多資訊可在[此處](https://www.kaaiot.com/docs/tutorials/getting-started/authenticating-client-with-tls-certificate)找到。

將 ca.pem 證書檔案上傳到 RouterOS，並使用以下命令匯入：

```ros
/certificate/import file-name=ca.pem passphrase=""
```

新增新的 MQTT 代理：

```ros
/iot/mqtt/brokers
add address=mqtt.next.kaaiot.com name=kaaiot port=8883 ssl=yes
```

連線到該代理，並藉助 "print" 命令檢查連線是否持續（應存在 "**connected=yes**"）：

```ros
/iot/mqtt/connect broker=kaaiot

/iot/mqtt/brokers/print
0 name="kaaiot" address="mqtt.next.kaaiot.com" port=8883 ssl=yes auto-connect=no keep-alive=60 parallel-scripts-limit=off connected=yes

```

要釋出一條基本 JSON 訊息：

```bash
{"test":"data"}
```

只需執行以下命令：

```ros
/iot/mqtt/publish broker=kaaiot message="{\"test\":\"data\"}" topic="kp1/<app-version>/epmx/<token>/update/keys/88"
```

其中應將 `<app-version>`（可在 "**Home>Device management>Devices>Specific device**" 標籤頁下檢視）和 `<token>`（您在平臺上建立裝置後生成的）替換為各自的值。

您應該能看到在 "**Home>Device management>Devices>Specific device>Overview**" 標籤頁下出現了新的 "Metadata" 值，或在 "**Home>Device management>Devices>Specific device>Data logs**" 標籤頁下檢視日誌。

要收集 `/system/resource/print` 資訊併發布它，我們可以使用指令碼。將下面所示指令碼的內容複製並貼上到命令列中：

```ros
/system/script
add dont-require-permissions=no name=systeminfo owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#####\
    ############################### System ###################################\r\
    \n:put (\"[*] Gathering system info...\")\r\
    \n:local cpuLoad [/system/resource/get cpu-load];\r\
    \n:local freeMemory [/system/resource/get free-memory];\r\
    \n:local usedMemory ([/system/resource/get total-memory] - \$freeMemory);\r\
    \n:local rosVersion [/system/package/get value-name=version \\\r\
    \n[/system/package/find where name ~ \"^routeros\"]];\r\
    \n:local model [/system/routerboard/get value-name=model];\r\
    \n:local serialNumber [/system/routerboard/get value-name=serial-number];\r\
    \n:local upTime [/system/resource/get uptime];\r\
    \n\r\
    \n#################################### message #####################################\r\
    \n:local message \\\r\
    \n\"{\\\"model\\\":\\\"\$model\\\",\\\r\
    \n\\\"sn\\\":\\\"\$serialNumber\\\",\\\r\
    \n\\\"ros\\\":\\\"\$rosVersion\\\",\\\r\
    \n\\\"cpu\\\":\\\"\$cpuLoad\\\",\\\r\
    \n\\\"umem\\\":\\\"\$usedMemory\\\",\\\r\
    \n\\\"fmem\\\":\\\"\$freeMemory\\\",\\\r\
    \n\\\"uptime\\\":\\\"\$upTime\\\"}\"\r\
    \n\r\
    \n:log info \"\$message\";\r\
    \n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
    \n:put (\"[*] Sending message...\")\r\
    \n/iot/mqtt/publish broker=kaaiot message=\$message topic=\"kp1/<app-version>/epmx/<token>/update/keys/88\"\r\
    \n:put (\"[*] Done\")"
```

更改主題中的 `<app-version>` 和 `<token>` 值。然後使用以下命令執行指令碼：

```ros
/system/script/run systeminfo
```

JSON 訊息將如下所示：

```bash
{
  "model": "RB924iR-2nD-BT5&BG77",
  "sn": "XXXXXXX",
  "ros": "7.99",
  "cpu": "7",
  "umem": "45113344",
  "fmem": "21995520",
  "uptime": "4d22:16:08"
}
```

## 使用儀表板視覺化資料 {#data-visualization-using-dashboards}

要視覺化先前釋出的資料，請轉到 "**Home>Solutions>Your\_Solution>Dashboards>Your\_Dashboard**"，然後點選 "**Add widget**"：

![](/img/b7fb7d39b26494dc.webp)

選擇小元件型別（我們將使用 "**Device management**"），以及預置小元件（我們將使用 "**Endpoint metadata**"）。

"**Edit**" 該小元件，並在 "**Data source>Endpoint ID**" 下選擇您的 "Endpoint ID"。從這裡，您可以進一步自定義儀表板：

![](/img/cdb90037e971b282.webp)

因此，您可以建立自己的指令碼，改為收集對您重要的資訊，然後只需應用[排程器](../../system-information-and-utilities/scheduler.md)以您選擇的間隔執行該指令碼。也許您想從 [LTAP](https://mikrotik.com/product/ltap#fndtn-specifications) 收集 GPS 座標，並使用 "map" 小元件將其視覺化？這一切完全由您決定！
