---
sidebar_key: "internet-of-things/lora/user-guides/chirpstack"
sidebar_position: 2
title: "ChirpStack"
sidebar_label: "ChirpStack"
description: "本頁面指導 MikroTik RouterOS 使用者將 LoRaWAN 網關注冊到 ChiprStack 開源伺服器。"
tags:
  - 'lora'
  - 'iot'
source: https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/chirpstack
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[ChirpStack](https://www.chirpstack.io/) 是一個開源 LoRaWAN 伺服器，你可以在本地安裝它。

伺服器啟動並執行後，登入 ChirpStack 管理門戶。

## 網關注冊 {#gateway-registration}

### 註冊閘道器 {#registering-gateway}

導航到“Tenant>Gateways”部分，然後點選“Add gateway”：

![](/img/7518e720ffd3b40e.png)

為裝置命名，並輸入“Gateway ID”：

![](/img/c4a01c848dbbdd57.png)

在 RouterOS 中，**Gateway EUI** 值可在“**IoT>LoRa>Devices>Gateway ID**”下找到：

![](/img/95e95d931677b14b.webp)

### 連線閘道器 {#connecting-gateway}

閘道器可透過 **UDP** 或 **LNS** 連線。有關如何配置兩者的更多詳細資訊，請參閱 ChirpStack 文件。

在 RouterOS 中，新增一個新伺服器，指向 ChripStack 的 IP/域名。如果使用 UDP：

```ros
/iot lora servers
add address=10.x.x.x name=Chirpstack protocol=UDP
```

如果使用 LNS：

```ros
/iot lora servers
add address=10.x.x.x name=Chirpstack port=3001 protocol=LNS ssl=no
```

:::info
埠、地址和 SSL 選項可能因你設定 ChirpStack 本身的方式而異。
:::

確保介面已停用（否則你將無法應用任何更改）：

```ros
/iot lora disable [find]
```

將伺服器附加到介面：

```ros
/iot lora set servers=Chirpstack [find]
```

啟用介面：

```ros
/iot lora enable [find]
```

### 網關注冊驗證 {#gateway-registration-verification}

在 RouterOS 中，你可以透過日誌確認閘道器已連線：

```ros
/log print where topics ~"lora"
```

你應該會看到“forwarder is ready”訊息：

```
 2026-06-15 14:31:09 lora,info [FWD] gateway-0 forwarder started
 2026-06-15 14:31:22 lora,info [FWD] gateway-0 forwarder is ready
 2026-06-15 14:31:41 lora,debug [FWD] gateway-0, Rx, Freq 868.100, CRC Error
 2026-06-15 14:32:10 lora,debug [FWD] gateway-0, Rx, Freq 867.100, CRC Error
```

在 ChirpStack 門戶上，在“Gateway”儀表板（“Tenant>Gateway”部分）下檢查狀態：

![](/img/c59399315b1543e5.png)

## 節點註冊 {#node-registration}

### 建立裝置配置檔案 {#create-device-profile}

新增新的[“Device Profile”](https://www.chirpstack.io/docs/chirpstack/use/device-profiles.html)：

![](/img/3ed00b288a70ab80.png)

根據你的節點/感測器支援的功能，配置“*Region*”、“*MAC version*”、“*Regional parameters revision*”、“*ADR algorithm*”和其他設定。
你也可以選擇啟用不同的類（例如 Class B）。

MikroTik **TG-LR** 標籤的資訊可在[此處](./tg-lr-setup-guide.md)找到。

新增“Payload codec”：

![](/img/eaa77004ac43d16e.png)

- 選擇“JavaScript functions”；
- 將[提供的指令碼 **tg-lrx2-2.0-ul-dec.js**](./tg-lr-setup-guide.md#quickstart-guide) 的內容複製/貼上到“Codec functions”欄位中，然後點選“Submit”。

### 建立應用 {#create-application}

新增新的[“Application”](https://www.chirpstack.io/docs/chirpstack/use/applications.html)：

![](/img/5763a995e012a6aa.png)

### 建立裝置 {#create-device}

如果你使用的是 **TG-LR** MikroTik 標籤，請在包裝內的標籤上找到印有的“**JoinEUI**”、“**DevEUI**”和“**AppKey**”。如果你使用的是其他廠商的感測器，請向製造商瞭解它們是什麼。

在先前建立的“Application”下新增新的[“Device”](https://www.chirpstack.io/docs/chirpstack/use/devices.html)：

![](/img/f31d2be1260d1519.png)

輸入“**Device EUI**”、“**Join EUI**”，選擇先前建立的“Device profile”並點選“Submit”。

最後：

![](/img/bbb6f789355f7d47.png)

輸入“**Application key**”並點選“Submit”。

### 給標籤上電 {#power-on-the-tag}

請檢視我們關於 [TG-LR 選項](./tg-lr-setup-guide.md) 的完整指南。

一開始，標籤將處於“Shutdown”模式（休眠）。

要啟用它，請檢視我們的[快速入門指南](./tg-lr-setup-guide.md#quickstart-guide)，然後只需將磁鐵靠在磁簧開關上約 1.5 秒，直到看到 LED 閃爍 2 次（之後移開磁鐵）。

:::info
使用其他廠商的感測器時，請了解如何啟用它。
:::

### 節點註冊驗證 {#node-registration-verification}

節點一旦上電，就應開始嘗試加入網路。

終端裝置將傳送“Join-request”封包，並期望收到“Join-accept”作為回應。

在 RouterOS 中，你可以在“**IoT>LoRa>Traffic**”標籤頁中看到該互動：

![](/img/ed9fe119970c72dd.png)

在門戶上，你應該能夠根據“LoRaWAN frames”標籤頁確認註冊：

![](/img/c2c239739507bf4d.png)
