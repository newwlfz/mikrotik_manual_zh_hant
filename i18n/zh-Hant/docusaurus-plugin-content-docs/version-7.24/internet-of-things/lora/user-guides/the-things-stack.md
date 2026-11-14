---
sidebar_key: "internet-of-things/lora/user-guides/the-things-stack"
sidebar_position: 5
title: "The Things Stack"
sidebar_label: "The Things Stack"
description: "本頁面指導 MikroTik RouterOS 使用者將 LoRaWAN 網關注冊到 The Things Stack，涵蓋 UDP 和 LNS/CUPS 協定。它說明了如何查詢 Gateway EUI 值、配置伺服器設定、生成身份驗證金鑰，以及匯入根證書以便與 TTN 伺服器進行安全通訊。"
tags:
  - 'lora'
  - 'iot'
source: https://manual.mikrotik.com/docs/7.24/internet-of-things/lora/user-guides/the-things-stack
captured_at: '2026-11-04T11:32:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[The Things Stack](https://console.cloud.thethings.network/) 是 The Things Network 的新版本。

![](/img/85a06075ddcb3e2a.webp)

選擇您所在的區域，並使用 The Things Network 賬戶或其他憑據登入。

## 註冊閘道器 {#registering-gateway}

登入後，導航到 “Go to gateways”：

![](/img/ce4dbbbc1730e36b.webp)

單擊 “**+ Register gateway**” 按鈕註冊閘道器：

![](/img/aeaf84f3b36a7b46.webp)

從這裡開始，閘道器可以透過兩種方式連線到伺服器：

- 使用 UDP 協定；

- 使用 LNS/CUPS 協定。

### UDP 場景 {#udp-scenario}

:::warning
[LNS/CUPS](./the-things-stack.md#lns-and-cups-scenario) 更加安全，我們建議改用 LNS/CUPS！
:::
UDP 是伺服器與閘道器之間的一種傳統通訊方式。

#### UDP 協定網關注冊 {#udp-protocol-gateway-registration}

填寫空白項。輸入 **Gateway EUI**。確保選擇正確的頻率計劃。不要啟用 “**Require authenticated connection**” 選項（該選項用於 LNS 和 CUPS）！

![](/img/4fdda867b0f2455a.webp)

在 RouterOS 中，**Gateway EUI** 值可在 “**IoT>LoRa>Devices>Gateway ID**” 下找到：

![](/img/95e95d931677b14b.webp)

更多資訊請檢視他們的 [文件頁面](https://www.thethingsindustries.com/docs/getting-started/)。

#### UDP 協定 RouterOS 配置 {#udp-protocol-routeros-configuration}

請再次確認 LoRa 裝置（在 RouterOS 中）選擇了正確的 TTN 伺服器，並且伺服器設定使用 “UDP” 協定：

![](/img/e387d9dababfe19a.webp)

### LNS 和 CUPS 場景 {#lns-and-cups-scenario}

[**LNS/CUPS**](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) 是現代協定。它們透過使用 TCP（TLS）為每個封包加密來提供更高的安全性，並引入了使用證書進行閘道器認證的機制（以及其他新功能）。

#### LNS 和 CUPS 協定網關注冊 {#lns-and-cups-protocol-gateway-registration}

填寫空白項。輸入 **Gateway EUI**。確保選擇正確的頻率計劃。啟用 “**Require authenticated connection**” 以及後續選項（用於 LNS） “**Generate API key for LNS**” 和（用於 CUPS） “**Generate API key for CUPS**”：

![](/img/f4e048050dad02c9.webp)

在 RouterOS 中，**Gateway EUI** 值可在 “**IoT>LoRa>Devices>Gateway ID**” 下找到：

![](/img/95e95d931677b14b.webp)

單擊 “**Register gateway**” 按鈕後，系統應提示您下載金鑰。請下載這些金鑰。

要檢視 LNS 和 CUPS 金鑰，請檢查下載的檔案。LNS 金鑰還應顯示在 “**LoRa Basics Station LNS authentication Key**” 欄位下：

![](/img/6b481c2675756635.webp)

更多資訊請檢視他們的 [文件頁面](https://www.thethingsindustries.com/docs/getting-started/)。

#### LNS 協定 RouterOS 設定 {#lns-protocol-routeros-settings}

確保選擇了正確的 TTN 伺服器，配置了正確的埠（TTN 期望 LNS 使用 8887），選擇了 LNS 協定，輸入了 LNS 金鑰（來自 “**LoRa Basics Station LNS authentication Key**” 欄位），並且啟用了 “**SSL**” 複選框：

![](/img/06acb23a58d3d095.webp)

如果您使用的是預設設定，則應為 **lora** 服務啟用閘道器內部的 [**builtin-trust-store**](../../../authentication-authorization-accounting/certificates.md#settings)，並且應已預裝所需的 Root CA。**您可以跳到下一步**。

**可選地**，如果您已停用 [**builtin-trust-store**](../../../authentication-authorization-accounting/certificates.md#settings)，並且想要手動上傳證書，請下載並匯入 [Root Certificates](https://www.thethingsindustries.com/docs/reference/root-certificates/)。

證書檔案下載後，將其拖放到 RouterOS 檔案選單中，並匯入證書列表：

![](/img/bbb71910231fbee8.webp)

這應使證書列表變為受信任：

![](/img/6d8106139a7b15ce.webp)

#### CUPS 協定 RouterOS 設定 {#cups-protocol-routeros-settings}

確保選擇了正確的 TTN 伺服器，配置了正確的埠（TTN 期望 CUPS 使用 443），選擇了 CUPS 協定，輸入了 CUPS 金鑰（在網關注冊步驟中從下載的 cups.key 檔案中獲取），並且啟用了 “**SSL**” 複選框：

![](/img/c3d21b3f77dbf8e1.webp)

如果您使用的是預設設定，則應為 **lora** 服務啟用閘道器內部的 [**builtin-trust-store**](../../../authentication-authorization-accounting/certificates.md#settings)，並且應已預裝所需的 Root CA。**您可以跳到下一步**。

**可選地**，如果您已停用 [**builtin-trust-store**](../../../authentication-authorization-accounting/certificates.md#settings)，並且想要手動上傳證書，請下載並匯入 [Root Certificates](https://www.thethingsindustries.com/docs/reference/root-certificates/)。

證書檔案下載後，將其拖放到 RouterOS 檔案選單中，並匯入證書列表：

![](/img/bbb71910231fbee8.webp)

這應使證書列表變為受信任：

![](/img/6d8106139a7b15ce.webp)

### 網關注冊驗證 {#gateway-registration-verification}

如果一切配置正確，在 RouterOS 中啟用 LoRa 介面（“**IoT>LoRa>Devices>Enable**”）後：

![](/img/c78b6928ce331176.webp)

您應會看到閘道器連線 “Live data” 更新：

![](/img/414378ecf0a2f937.webp)

## 註冊節點 {#registering-the-node}

本節將演示如何將 MikroTik 的 **TG-LR** 標籤（[**TG-LR82**](https://mikrotik.com/product/tg_lr82) 或 [**TG-LR92**](https://mikrotik.com/product/tg_lr92)）新增到門戶中。

同樣的原則適用於其他廠商的節點/感測器/標籤。

### 建立應用 {#create-application}

在 TTS 門戶中，導航到 “**Applications**” 標籤頁，然後單擊 “**add application**”：

![](/img/205f51eca2e54255.png)

輸入您希望其使用的 ID，為其命名，新增描述，然後建立它（“**Create application**”）：

![](/img/29afd2dd097c71e0.png)

### 註冊終端裝置 {#register-end-device}

在您剛建立的應用下，導航到 “**End devices**” 標籤頁並單擊 “**+ Register end device**”：

![](/img/9359918e5bff4301.png)

您可以選擇 “Select the end device in the LoRaWAN Device Repository”（並自動完成該過程），也可以手動新增（“Enter end device specifics manually”）：

![](/img/cbb773c9ffc92ddb.png)

- 輸入 “**Frequency plan**”（例如，*Europe 863-870 MHz (SF9 for RX2 - recommended)*，具體取決於您的標籤支援哪個頻率）；
- “**LoRaWAN version**”（“*LoRaWAN Specification 1.0.4*”）；
- “**Regional Parameters version**”（“*RP002 Regional Parameters 1.0.4*”）。

找到包裝內標籤上印有的 “**JoinEUI**”、“**DevEUI**” 和 “**AppKey**”，然後繼續填寫預配資訊：

![](/img/1440133c00145fad.png)

- 從標籤輸入 “**JoinEUI**”，並確認；
- 從標籤輸入 “**DevEUI**”；
- 從標籤輸入 “**AppKey**”；
- 為您的標籤設定 ID/名稱；
- 單擊 “**Register end device**”。

### 啟用解碼器 {#enable-decoder}

:::info
如果跳過此步驟，TTS 門戶將僅顯示 “raw hex” 負載。
:::

為了讓伺服器以可讀/可理解的格式顯示標籤的資料，它首先需要能夠“解碼”其接收到的負載。
您可以在新建立的標籤選項下的 “[Payload formatters](https://www.thethingsindustries.com/docs/integrations/payload-formatters/)” 部分中輸入解碼器指令碼：

![](/img/6e8e3cfbb626c1fd.png)

- 選擇 “Custom Javascript formatter”；
- 將 [提供的指令碼 **tg-lrx2-2.0-ul-dec.js**](./tg-lr-setup-guide.md#quickstart-guide) 的內容複製/貼上到 “Formatter code” 欄位中，並單擊 “Save changes”。

### 給標籤上電 {#power-on-the-tag}

請檢視我們關於 [TG-LR 選項](./tg-lr-setup-guide.md) 的完整指南。

一開始，標籤將處於“Shutdown”模式（休眠）。

要啟用它，請檢視我們的[快速入門指南](./tg-lr-setup-guide.md#quickstart-guide)，然後只需將磁鐵靠在磁簧開關上約 1.5 秒，直到看到 LED 閃爍 2 次（之後移開磁鐵）。

### 節點註冊驗證 {#node-registration-verification}

節點上電後，應立即開始嘗試 [加入網路](https://www.thethingsnetwork.org/docs/lorawan/end-device-activation/)。

終端裝置將傳送“Join-request”封包，並期望收到“Join-accept”作為回應。

在 RouterOS 中，你可以在“**IoT>LoRa>Traffic**”標籤頁中看到該互動：

![](/img/ed9fe119970c72dd.png)

最後，您應能夠根據 TTS 日誌確認註冊：

![](/img/765de8dd9d41e26a.png)
