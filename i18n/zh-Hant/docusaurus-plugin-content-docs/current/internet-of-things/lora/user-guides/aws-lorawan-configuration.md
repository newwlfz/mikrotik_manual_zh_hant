---
sidebar_key: "internet-of-things/lora/user-guides/aws-lorawan-configuration"
sidebar_position: 1
title: "AWS LoRaWAN 配置"
sidebar_label: "AWS LoRaWAN 配置"
description: "本頁引導使用者在 MikroTik RouterOS 上配置 AWS LoRaWAN 整合，涵蓋在 AWS IoT Core 中註冊閘道器、證書生成和匯入，以及用於 LNS 連線的伺服器設定。"
tags:
  - 'aws'
  - 'iot'
  - 'lora'
source: https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/aws-lorawan-configuration
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
本場景從 RouterOS 版本 **7.14beta8** 開始可用。
:::

在繼續設定之前，您需要在 AWS 系統中建立賬戶。您可以訪問此[連結](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)瞭解有關如何操作的更多資訊。

登入後，前往門戶中的 **Services>IoT Core** 部分。

## AWS - 註冊閘道器 {#aws---registering-the-gateway}

第一步是註冊 LoRaWAN 閘道器。

前往 [Gateways](https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/wireless/gateways) 部分（位於 [LPWAN devices](https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/wireless/landing) 下）。

![](/img/ed4ee05927b02491.webp)

點選 "**Add gateway**" 按鈕。

### 步驟 1 - 新增閘道器 {#step-1---add-gateway}

- 輸入閘道器的 EUI。
- 選擇裝置的頻段。
- 如有需要，配置可選欄位。

![](/img/60a9686c5527b7cc.webp)

再次點選 "**Add gateway**" 完成該步驟。

在 RouterOS 設定中，可以在 **IoT>LoRa>Devices** 標籤頁下檢視閘道器的 EUI 和頻率計劃：

![](/img/680040c219bd18d6.webp)

### 步驟 2 - 配置閘道器 {#step-2---configure-your-gateway}

- 生成閘道器證書（"**Create certificate**" 按鈕），並下載證書檔案和私鑰檔案（"**Download certificate files**" 按鈕）。
- 複製 CUPS 和 LNS 端點，並下載伺服器信任證書（"**Download server trust certificates**" 按鈕）。
- 新增建議的閘道器許可權。

![](/img/821bda4083751dfe.webp)

點選 "**Submit**" 完成該步驟。

你將被重定向到新建立的閘道器應出現的頁面。

## RouterOS - 連線閘道器 {#routeros---connecting-the-gateway}

### 上傳並匯入證書 {#uploading-and-importing-certificates}

:::info
預設情況下，**lora** 服務在[證書 **trust-store**](../../../authentication-authorization-accounting/certificates.md)中是受信任的，並且內建儲存中已經包含所需的 AWS Root 證書。
如果你想手動操作，以下步驟展示瞭如何獲取並安裝 Root AWS 證書。

如果[證書 **trust-store**](../../../authentication-authorization-accounting/certificates.md)中啟用了 **lora** 服務，請跳過匯入 AWS Root CA。
你仍然需要匯入唯一的裝置證書。
:::

在繼續設定之前，你需要下載 [Amazon Root CA](https://www.amazontrust.com/repository/)，並將其與閘道器證書檔案及其金鑰一起上傳到 RouterOS 的檔案列表選單中：

![](/img/679d93cd6d29f923.webp)

檔案上傳後，逐個匯入證書（位於 **System>Certificates** 下）：

![](/img/7dac383ebfcf0a67.webp)

請確保先上傳閘道器證書，再上傳其金鑰（這樣閘道器證書才會同時帶有 K-key 和 T-trusted 標誌）。最終，你應該已匯入全部 3 個檔案，如下所示：

![](/img/2c8c5590f53d016a.webp)

### 伺服器配置 {#server-configuration}

#### LNS 場景 {#lns-scenario}

前往 **IoT>LoRa>Servers** 標籤頁並新增新伺服器：

![](/img/582b6fdeddc052ca.webp)

- 為伺服器命名。
- 輸入 LNS 端點地址（不含 `wss://` 和 `:443`）。
- 選擇 LNS 協定。
- 將埠更改為 "443"。
- 啟用 SSL 複選框。
- 選擇閘道器證書。

確保在 **IoT>LoRa>Devices** 標籤頁下應用新配置的伺服器：

![](/img/5104a0a5720db60f.webp)

然後，**啟用** LoRa 介面。

#### CUPS 場景 {#cups-scenario}

前往 **IoT>LoRa>Servers** 標籤頁並新增新伺服器：

![](/img/771be9bf7ade270f.webp)

- 為伺服器命名。
- 輸入 CUPS 端點地址（不含 `https://` 和 `:443`）。
- 選擇 CUPS 協定。
- 將埠更改為 "443"。
- 啟用 SSL 複選框。
- 選擇閘道器證書。

確保在 **IoT>LoRa>Devices** 標籤頁下應用新配置的伺服器：

![](/img/5104a0a5720db60f.webp)

然後，**啟用** LoRa 介面。

### 連線驗證 {#connection-verification}

如果一切配置正確，你應該會在 AWS 門戶上看到 "connected" 狀態：

![](/img/d8cbfa6776b4b431.webp)
