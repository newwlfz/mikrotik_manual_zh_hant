---
sidebar_key: "internet-of-things/gpio/using-gpio-as-pulse-input-from-meter"
sidebar_position: 1
title: "使用 GPIO 作為儀表裝置的脈衝輸入"
sidebar_label: "使用 GPIO 作為儀表裝置的脈衝輸入"
description: "將 MikroTik 裝置的 GPIO 用作脈衝輸入，以讀取水錶、電錶或其他儀表，並配合 RouterOS 指令碼對脈衝進行計數。"
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/gpio/using-gpio-as-pulse-input-from-meter
captured_at: '2026-11-04T11:18:24+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

一些水錶、電能表或其他儀表具有脈衝輸出。儀表的規格說明會描述多少個脈衝代表一個整數計量單位。例如，我們用於編寫本手冊的電能表每產生 1000 個脈衝代表 1kWh，因此每個脈衝為 1Wh。您可以使用 KNOT 的數字 GPIO 輸入（pin5）讀取這些脈衝，並統計電能表後方消耗的電能。為此，需要建立一個簡單的 MOSFET 電路原理圖，並按下圖連線所有部件：

![](/img/bede935d660039e3.png)

下一步是編寫一個 RouterOS 指令碼，在每次收到脈衝時執行：

```bash
/iot gpio digital
set pin5 script=":global scriptRunning; :global pulse;\
:if (\$scriptRunning!=true) do={\
:set \$scriptRunning true;\
:set \$pulse (\$pulse+1);\
:log info message=(\"GPIO pulse No. \".\$pulse);\
:delay 1s;\
:set \$scriptRunning false;\
}"
```

當 GPIO 配置完成後，上述指令碼會在每次脈衝時建立一條日誌條目：

```bash
15:32:22 script,info GPIO pulse No. 1 
15:38:01 script,info GPIO pulse No. 2 
15:43:38 script,info GPIO pulse No. 3 
15:49:15 script,info GPIO pulse No. 4 
15:54:51 script,info GPIO pulse No. 5 
16:00:27 script,info GPIO pulse No. 6 
16:06:02 script,info GPIO pulse No. 7 
16:11:37 script,info GPIO pulse No. 8 
16:17:12 script,info GPIO pulse No. 9 
16:22:48 script,info GPIO pulse No. 10 
```
