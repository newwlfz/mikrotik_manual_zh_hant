---
sidebar_key: "mobile-networking/gps"
title: "GPS"
sidebar_label: "GPS"
description: "本頁介紹 MikroTik RouterOS 中的 GPS 配置與監控，涵蓋通道選擇、座標格式、GPS 初始化字串等屬性，以及帶有 date-and-time、latitude/longitude、altitude、satellites 和 data age 等引數的監控命令。"
tags:
  - 'gps'
source: https://manual.mikrotik.com/docs/mobile-networking/gps
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 GPS 跟蹤示例。你可以使用這些示例將 RouterOS GPS 資料傳送到 HTTP 端點、MQTT 代理和 IoT 平臺。

<DocCardList />

### 概述 {#summary}

**軟體包要求：** `gps`
**子選單：** `/system/gps`
**標準：** `GPS, NMEA 0183, Simple Text Output Protocol`

全球定位系統（GPS）用於確定 GPS 接收器的精確位置。

### 配置屬性 {#configuration-properties}

| 屬性 | 說明 |
| :-- | :-- |
| **channel** (*integer [0..4294967295]*; 預設：**0**) | 裝置使用的埠通道 |
| **coordinate-format** (*dd \| dms \| ddmm*; 預設：**dms**) | 要使用的座標格式：“十進位制度”、“度分秒”或“NMEA 格式 DDDMM.MM[MM]” |
| **enabled** (*yes \| no*; 預設：**no**) | 是否啟用 GPS |
| **gps-antenna-select** (*external \| internal*; 預設：**internal**) | 取決於型號。如果裝置安裝了內建天線，則可以選擇內建天線。 |
| **init-channel** (*integer [0..4294967295]*; 預設：) | 執行 init-string 的通道 |
| **init-string** (*string*; 預設：) | 用於 GPS 初始化的 AT 初始化字串 |
| **port** (*string*; 預設：) | GPS 接收器所連線的 USB/序列埠名稱 |
| **set-system-time** (*yes \| no*; 預設：**no**) | 是否將路由器的日期和時間設定為從 GPS 接收到的日期和時間。 |

### 監控狀態 {#monitoring-status}

**命令：** `/system/gps/monitor`

此命令用於監控從 GPS 接收器接收到的資料。

**引數：**

:::warning
從 7.1rc3 韌體版本開始，新增了一個名為 "data-age" 的引數（以秒為單位）。此引數顯示自裝置收到最後一條 NMEA 訊息以來經過的時間。
:::

| 屬性 | 說明 |
| :-- | :-- |
| **date-and-time** (*date*) | 從 GPS 接收到的日期和時間 |
| **latitude** (*none \| string*) | DM（度分十進位制）格式的緯度 |
| **longitude** (*none \| string*) | DM（度分十進位制）格式的經度 |
| **altitude** (*none \| string*) | 基於 GPS 資料的高度 |
| **speed** (*none \| string*) | GPS 單元當前的移動速度 |
| **destination-bearing** (*none \| string*) | 從當前位置指向已配置目標航點的方位角 |
| **true-bearing** (*none \| string*) | 相對於真北的當前航向 |
| **magnetic-bearing** (*none \| string*) | 相對於磁北的當前航向 |
| **valid** (*yes \| no*) |  |
| **satellites** (*integer*) | 裝置可見的衛星數量。 |
| **fix-quality** (*integer*) | 訊號質量 |
| **horizontal-dilution** (*decimal*) | 水平精度因子（HDOP）； |
| **data-age** (integer) | 自裝置收到最後一條 NMEA 訊息以來經過的時間 |

### 基礎示例 {#basic-examples}

檢查埠使用情況，因為同一時間只能有一個例項使用序列埠：

```ros
[admin@MikroTik] /port/print
Flags: I - inactive 
 #   DEVICE NAME                     CHANNELS USED-BY                   BAUD-RATE
 0          serial0                         1 Serial Console            auto    
```

如果只有一個埠並且它被控制檯使用，請從控制檯選單中釋放它：

```ros
[admin@MikroTik] > /system/console/print 
Flags: X - disabled, U - used, F - free
 #   PORT                                                                       TERM                                                                     
 0 U serial0                                                                    vt102 

[admin@MikroTik] > /system/console/disable 0   
```

根據你的裝置調整埠設定（LtAP mini 保留 "auto"）：

```ros
[admin@MikroTik] /port> set 0 baud-rate=4800 parity=odd
[admin@MikroTik] /port> print detail 
Flags: I - inactive 
 0   name="usb1" used-by="" channels=1 baud-rate=4800 data-bits=8 parity=odd stop-bits=1 flow-control=none
```

啟用 GPS：

```ros
[admin@MikroTik] /system/gps> set enabled=yes port=usb1
[admin@MikroTik] /system/gps> print 
          enabled: yes
             port: usb1
          channel: 0
     init-channel: 0
      init-string:
  set-system-time: no
```

監控狀態：

```ros
[admin@MikroTik] /system/gps> monitor  
        date-and-time: 2021-09-07 08:26:26
             latitude: 56.969689
            longitude: 24.162471
              altitude: 25.799999 m
                speed: 0.759320 km/h
  destination-bearing: none
         true-bearing: 185.500000 deg. True
     magnetic-bearing: 0.000000 deg. Mag
                valid: yes
           satellites: 6
          fix-quality: 1
  horizontal-dilution: 1.3
```

## **LtAP** 的埠和 GPS 設定 {#port-and-gps-settings-for-ltap}

```ros
/port/set serial1 baud-rate=115200
```

```ros
/system/gps/set port=serial1 channel=0 enabled=yes
```

我們還撰寫了一篇深入文章，介紹如何使用指令碼和 Web 伺服器進行即時 GPS 跟蹤：[GPS-tracking](./gps-tracking-using-http-post.md)。

### 故障排除 {#troubleshooting}

請注意，有時為了讓 GPS 模組在 RouterOS 中被識別，你需要更改 `/port` 選單中的波特率設定。

[LtAP mini](https://mikrotik.com/product/ltap_mini) 內建低增益 GPS 天線；為了獲得更好的體驗，我們建議使用額外的[外接天線](https://mikrotik.com/product/acgpsa)。

在 GPS 選單下切換內建天線和外接天線：

```ros
[admin@MikroTik] > /system/gps/set gps-antenna-select=external
```

在某些支援 GPS 的調變解調器上，你需要傳送多個初始化命令以實現持續的 GPS 監控；例如，對於華為卡，你需要傳送 "AT^WPDST=1,AT^WPDGP" 初始化字串才能獲得持續監控。
