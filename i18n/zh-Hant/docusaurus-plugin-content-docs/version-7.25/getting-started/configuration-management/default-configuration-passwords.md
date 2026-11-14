---
sidebar_key: "getting-started/configuration-management/default-configuration-passwords"
sidebar_position: 2
title: "預設配置密碼"
sidebar_label: "預設配置密碼"
description: "查詢 MikroTik RouterOS 裝置在出廠全新狀態或完全重設後的預設登入憑據。"
source: https://manual.mikrotik.com/docs/7.25/getting-started/configuration-management/default-configuration-passwords
captured_at: '2026-11-04T11:16:03+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik 裝置出廠時帶有預設配置，其中包含預設密碼。每當執行標準系統重設時，都會重新應用相同的密碼。瞭解如何找到此密碼對於初始裝置訪問至關重要。

:::tip[觀看我們的官方講解]
[預設密碼：為什麼？！](https://www.youtube.com/watch?v=mq7nIIILrVc) — 簡要概述為什麼 MikroTik 裝置現在出廠時帶有唯一的出廠密碼。
:::

早期的 MikroTik 型號通常使用使用者名稱 `admin`，且沒有密碼——輸入 `admin` 作為登入名，並在提示時按 **Enter**。後續型號在出廠時每臺裝置都帶有唯一的預設密碼。

:::note[定製品牌裝置]
定製品牌或 OEM 裝置可能具有不同的預設密碼。如果找不到標準標籤，仍可使用 **[Netinstall 實用程式](../installation-and-upgrade/netinstall/index.md)** 重設裝置。
:::

## 在哪裡查詢密碼 {#where-to-find-the-password}

預設密碼印在多個物理位置：

- 在裝置本身上，位於序列號標籤上
- 在裝置包裝上，同樣位於序列號標籤上
- 在產品盒內隨附的印刷版快速指南頁上

部分 MikroTik [室內無線](https://mikrotik.com/products/indoor-wireless) 裝置（例如 [hAP ac³](https://mikrotik.com/product/hap_ac3) 和 [hAP ax³](https://mikrotik.com/product/hap_ax3)）帶有專用的 **產品資訊隔間**——這是裝置底部的一個小面板，裡面放有帶預設憑據的標籤。請在 Ethernet 埠附近或 RF 聯結器蓋下方尋找該隔間。打開面板，即可看到內部標籤上印有的序列號和預設密碼。

:::warning

在聯絡支援之前，請務必檢查這些標籤。密碼只印在物理材料上——它不會以數字形式儲存在任何線上系統中。

:::

## 如果找不到密碼 {#if-you-cannot-find-the-password}

如果標籤缺失或無法辨認，請聯絡供應此裝置的 MikroTik 分銷商。請提供裝置序列號以及您購買該裝置的賣家或商店名稱。分銷商維護有密碼資料庫，可以從序列號檢索預設密碼。

:::tip

觀看我們的影片指南：[用於無縫配置的秘密 CSV 密碼檔案](https://www.youtube.com/watch?v=q9F871KkGBw) ——瞭解如何使用 CSV 密碼檔案進行自動化裝置設定。

:::

如果無法聯絡分銷商或無法找回密碼，您仍可透過使用 **[網路安裝](../installation-and-upgrade/netinstall/index.md)** **重新安裝 RouterOS**，或執行 **[完整配置重設](./routeros-configuration-reset.md)**，來重新獲得訪問許可權。

:::tip[使用 Flashfig 進行批次配置]

要大規模部署多臺裝置，請使用 Flashfig 工具：

- [使用 flashfig 批次配置 MikroTik](https://www.youtube.com/watch?v=gticPeOdN54)（Windows）
- [在 Linux 上使用 flashfig 批次配置 MikroTik](https://www.youtube.com/watch?v=xasM81Qc11g)（Linux）

:::
