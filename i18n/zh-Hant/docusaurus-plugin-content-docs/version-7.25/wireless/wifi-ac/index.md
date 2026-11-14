---
sidebar_key: "wireless/wifi-ac/index"
sidebar_position: 2
title: "Wi-Fi 5（802.11ac）"
sidebar_label: "Wi-Fi 5"
description: "MikroTik 802.11ac（Wi-Fi 5）ARM 裝置有兩種驅動方式：透過新的 `/interface/wifi` 選單並使用 `wifi-qcom-ac` 軟體包（WPA3、快速漫遊、新的 CAPsMAN），或者透過傳統的 `/interface/wireless` 選單並使用 `wireless` 軟體包（Nstreme、Nv2、舊版 CAPsMAN）。本頁幫助您在兩者之間做出選擇，並連結到相應的配置參考文件。"
tags:
  - 'wifi'
  - 'wireless'
  - '802-11ac'
source: https://manual.mikrotik.com/docs/7.25/wireless/wifi-ac
captured_at: '2026-11-04T11:24:12+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 MikroTik **802.11ac (Wi-Fi 5)** 的 ARM 架構裝置。這些產品比較特殊：**同一硬體可以透過兩個 RouterOS 選單之一進行配置**，具體取決於安裝了哪個驅動包。請選擇與您所需功能相匹配的那一個。
:::warning
`wifi-qcom-ac` 驅動非常佔用資源。我們建議 WiFi 5 (802.11ac) 裝置使用其原有的 `wireless` 驅動，因為後者較為輕量。
:::

## 執行 802.11ac 裝置的兩種方式 {#two-ways-to-run-an-80211ac-device}

| 如果您需要… | 安裝包 | 配置位置 | 文件 |
| :-- | :-- | :-- | :-- |
| WPA3、快速漫遊 (802.11r)、新的 CAPsMAN | `routeros` + `wifi-qcom-ac` | `/interface/wifi` | [Wi-Fi 6 / 7 (802.11ax/be)](../wifi/index.md) — `/interface/wifi` 選單是共用的 |
| Nstreme、Nv2、WDS、HWMP+ 網狀組網、舊的 CAPsMAN | `routeros` + `wireless` | `/interface/wireless` | [802.11 a/b/g/n](../abgn/index.md) — `/interface/wireless` 選單是共用的 |

內建射頻上不能同時使用這兩個包 — 有關如何切換，請參閱[替換 'wireless' 包](../wifi/index.md)。

:::info
新的 `/interface/wifi` 選單管理 **Wi-Fi 5 wave2 及更新**的介面，因此執行 `wifi-qcom-ac` 的 802.11ac 裝置使用的配置，與 [Wi-Fi 6 / 7 (802.11ax/be)](../wifi/index.md) 下記錄的 802.11ax/be 裝置完全相同。因此本節連結到該參考文件，而不重複其內容。
:::

## 可選擇驅動的裝置 {#devices-with-a-choice-of-driver}

以下 802.11ac ARM 型號可以執行 `wifi-qcom-ac`（新的 `/interface/wifi` 選單）或 `wireless`（舊版 `/interface/wireless` 選單）：

> Audience、Audience LTE kit、Chateau（D53 的所有變體）、hAP ac²、hAP ac³、cAP ac、cAP XL ac、LDF 5 ac、LHG XL 5 ac、LHG XL 52 ac、NetMetal ac²、mANTBox 52 15s、wAP ac (RBwAPG-5HacD2HnD)、SXTsq 5 ac

:::warning
`wifi-qcom-ac` 驅動升級主要面向室內裝置。儘管它也可以安裝在我們的室外型號（LDF 5 ac、LHG XL 5 ac、LHG XL 52 ac、NetMetal ac²、mANTBox 52 15s、SXTsq 5 ac）上，但 `wifi-qcom-ac` 並非為室外使用而定製。這主要是因為該驅動不支援 **distance** 設定，而超過 2 km 的鏈路需要此設定。因此，我們建議在所有室外板卡上使用 `wireless` 驅動。
:::

要按裝置型別和 CAPsMAN 場景選擇軟體包，請參閱[無線概覽](../index.md)中的決策表。
