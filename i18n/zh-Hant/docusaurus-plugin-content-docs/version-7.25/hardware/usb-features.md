---
sidebar_key: "hardware/usb-features"
sidebar_position: 13
title: "USB 功能"
sidebar_label: "USB 功能"
description: "本頁面介紹 MikroTik RouterOS 中的 USB 功能，包括可配置持續時間和匯流排選擇的 USB 電源重設功能、USB 埠型別路由選項（auto/USB-type-A/mini-PCIe），以及特定型號對 micro USB 主機模式的支援，並附有關於裝置相容性的警告。"
tags:
  - 'usb'
  - 'power-management'
source: https://manual.mikrotik.com/docs/7.25/hardware/usb-features
captured_at: '2026-11-04T11:17:35+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

**子選單：** `/system/routerboard/usb`  
**軟體包：** `system (v6, v7)`

本文介紹 RouterBoard 裝置支援的 USB 功能。

## USB 電源重設 {#usb-power-reset}

USB 電源重設會關閉 USB 埠電源一段指定的時間。當 3G/LTE 調變解調器需要重啟，但無法對其進行物理接觸時，這一功能非常有用。

## 可用屬性 {#available-properties}

- duration (*time*；預設值："3s") - 關閉電源的時間間隔。

例如，關閉 USB 埠電源 10 秒：

```ros
/system/routerboard/usb/power-reset duration=10s 
```

具有多條 USB 匯流排的 RouterBoard 還需要指定匯流排，才能執行 USB 電源重設。  

## 可用屬性 {#available-properties-1}

- duration (*time*；預設值："3s") - 關閉電源持續的時間間隔。
- bus (*integer*；預設值：1) - 應用電源重設的 USB 匯流排。

:::warning
**RB953GS**：在 RB953GS 板上，靠近乙太網埠的 miniPCIe 插槽是與 USB 埠共享的那個插槽，並且具有可配置的 [USB 埠型別](#usb-port-type)，其 USB 匯流排編號為 1。根據 [USB 埠型別](#usb-port-type) 的不同，電源重設在 USB 埠或 miniPCIe 插槽上執行。另一個靠近 SFP 插槽的 miniPCIe 插槽具有獨立的匯流排 - 2。

:::

:::warning
**RB922UAG**：USB 埠具有獨立的匯流排 - 1。miniPCIe 插槽具有獨立的匯流排 - 2。

:::

:::warning
**CCR1072-1G-8S+**：micro USB 埠具有獨立的匯流排 - 0。USB Type-A 埠具有獨立的匯流排 - 1。

:::

## USB 埠型別 {#usb-port-type}

具有可切換 USB 埠路由的板卡具有共享的 USB 線路，這些線路可路由到外部 USB-Type 埠或 mini-PCIe 插槽。更多參考請參見板卡規格頁面文件部分中的板卡框圖。

```ros
[admin@MikroTik] > /system/routerboard/usb/set type=
USB-type-A     auto     mini-PCIe 
```

|  |  |
| :-- | :-- |
| **auto**（預設） | 在 RouterOS 啟動期間檢查 mini-PCIe 插槽中是否存在 USB 裝置：如果存在 - 使用 mini-PCIe 插槽中的裝置如果不存在 - 預設為外部 USB Type A 埠 |
| **USB-type-A** | 使用連線到 USB Type A 聯結器的 USB 裝置 |
| **mini-PCIe** | 將 USB 線路路由到相應的 mini-PCIe 插槽 |

:::warning
**RB953GS：** 在 RB953GS 板上，靠近乙太網埠的 miniPCIe 插槽是與 USB 埠共享的那個插槽，並且具有可配置的 [USB 埠型別](#usb-port-type)，其 USB 匯流排編號為 1。根據 [USB 埠型別](#usb-port-type) 的不同，電源重設在 USB 埠或 miniPCIe 插槽上執行。另一個靠近 SFP 插槽的 miniPCIe 插槽具有獨立的匯流排 - 2。

:::

## USB 埠模式 {#usb-port-mode}

RB2011 系列、CRS1xx 系列和 mAP 具有一個 micro USB 埠，當透過 USB OTG 線纜連線 USB 裝置時，該埠以主機模式執行。某些廠商的線纜需要強制主機模式才能識別所連線的裝置。

## 可用屬性 {#available-properties-2}

- usb-mode (*automatic | force-host*；預設值："automatic") - 定義 USB 埠模式。

:::warning
警告

在 RB2011 和 CRS1xx 系列板卡上，USB 裝置首次插入時可能無法工作。在這種情況下，需要斷電重啟（不是軟重啟）。

:::

## RouterBoard USB 埠限制 {#routerboard-usb-port-limitations}

某些 RouterBoard 裝置存在值得注意的 USB 埠限制。

\* RB mAP 2n - 不支援 USB 電源重設  
\* RB750UP - 不支援 USB 電源重設  
\* RB751U-2HnD - 不支援 USB 電源重設  
\* RB751G-2HnD - 不支援 USB 電源重設  
\* RB411U - 不支援 USB 電源重設  
\* RB411UAHR - 不支援 USB 電源重設和 USB 供電（需要 [USB 電源注入器](https://mikrotik.com/product/5VUSB)）  
\* RB433UAH - 不支援 USB 電源重設  
\* RB435G - 不支援 USB 電源重設  
\* RB493G - 不支援 USB 電源重設和 USB 供電（需要 [USB 電源注入器](https://mikrotik.com/product/5VUSB)）

:::warning
RouterOS 不支援 USB 調變解調器上的儲存插槽。

:::
