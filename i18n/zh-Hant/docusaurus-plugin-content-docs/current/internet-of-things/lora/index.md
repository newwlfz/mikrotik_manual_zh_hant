---
sidebar_key: "internet-of-things/lora"
title: "LoRa"
sidebar_label: "LoRa"
description: "本頁介紹 MikroTik RouterOS LoRa 和 LoRaWAN 配置，涵蓋閘道器設定、通用屬性、伺服器整合以及使用 MQTT/HTTP 的非 LoRaWAN 有效載荷轉發。其中詳細說明了支援的硬體、拓撲元素以及加密有效載荷的指令碼要求。"
tags:
  - 'lora'
  - 'lorawan'
  - 'mqtt'
source: https://manual.mikrotik.com/docs/internet-of-things/lora
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 RouterOS 中的 LoRa 和 LoRaWAN 功能。使用它來配置 LoRa 閘道器、通用屬性以及與受支援的 LoRaWAN 網路的整合。

<DocCardList />

可用設定：

- ## [通用屬性](./general-properties.md)

閘道器初始步驟和不同的 LoRaWAN 設定示例：

- ## [使用者指南](./user-guides/index.md)

術語“LoRa”表示“無線電”本身（“LoRa 負載”是節點使用 LoRa 頻率廣播的封包），而術語“LoRaWAN”表示位於其上的邏輯/鏈路層，用於實現“LoRa”裝置之間的通訊。換句話說，“LoRaWAN”是“LoRa”無線電裝置進行通訊的方式。

**R11e-LR8**（工作在 863-870 MHz 頻率）、**R11e-LR9**（工作在 902-928 MHz 頻率）和 **R11e-LR2**（使用 2.4 GHz 頻率工作）是基於 Semtech 晶片組的 mini PCIe 外形規格的 LoRa® 技術集中器閘道器卡。它們可為任何具有 mPCIe 插槽並已連線 USB 線路的 MikroTik 產品啟用 LoRa® 連線。

典型的 LoRaWAN 拓撲由 3 個主要元素組成 → 伺服器、節點和閘道器。閘道器的工作只是將接收到的、由節點廣播的 LoRa 封包（在相同受支援頻譜範圍內）轉發到伺服器。

MikroTik LoRaWAN 閘道器是帶有 R11e-LR**x** miniPCIe 卡並安裝了“iot”[軟體包](../../getting-started/installation-and-upgrade/packages.md)（用於啟用 LoRa 驅動）的裝置。

MikroTik 閘道器裝置的主要設計是作為 LoRaWAN 裝置執行。要實現這一點，只需在 LoRa 介面設定中配置/選擇正確的伺服器。一些示例可以在[使用者指南部分](./user-guides/index.md)中找到。

#### 非 LoRaWAN 設定 {#non-lorawan-setup}

但是，如果您不希望使用 LoRaWAN 網路/拓撲，並且希望將“原始 LoRa”負載轉發到自己的伺服器，則可以選擇這樣做。您可以使用 [MQTT](../mqtt/index.md) 或 [HTTP POST](../../system-information-and-utilities/fetch.md) 將接收到的負載轉發到您的 MQTT/HTTP 伺服器，但這將需要額外的[指令碼](../../developer-guides/scripting/index.md)。指令碼必須從 `IoT>LoRa>Traffic` 標籤頁收集資訊（負載），將這些負載儲存為變數，用這些變數構造 MQTT/HTTP 訊息併發送。

:::info
請注意，如果節點廣播的負載已加密，並且您希望將它們轉發到自己的 MQTT/HTTP 伺服器（不使用 LoRaWAN），則需要在伺服器端解密這些負載。閘道器沒有內建的解密節點資料的功能。伺服器負責此任務。

此外，無法將下行 MQTT/HTTP 訊息從 MQTT/HTTP 伺服器“中繼”回 LoRa 節點（只能將來自節點的“上行”負載“轉發”到伺服器），主要原因是無法“讓”LR 卡“廣播”自定義負載（無法將 MQTT/HTTP 下行訊息的內容傳入 LoRa 晶片）。
:::
