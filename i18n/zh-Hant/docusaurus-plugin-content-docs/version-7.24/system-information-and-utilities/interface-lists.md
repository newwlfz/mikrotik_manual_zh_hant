---
sidebar_key: "system-information-and-utilities/interface-lists"
sidebar_position: 7
title: "介面列表"
sidebar_label: "介面列表"
description: "RouterOS 中的 Interface Lists 允許定義介面集合，以便在各種配置中簡化管理。主選單列出預定義和自定義的 Interface Lists，而 member 子選單處理靜態配置的成員。動態介面會根據 flags 自動包含或排除，bridge 需要謹慎處理以避免意外行為。"
tags:
  - 'interface-lists'
  - 'firewall'
  - 'bridging'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/interface-lists
captured_at: '2026-11-07T17:11:03.548Z'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

允許定義一組介面，以便在 Neighbor Discovery、Firewall、Bridge 和 Internet Detect 等不同的基於介面的配置部分中更輕鬆地進行介面管理。

## 列表 {#lists}

**子選單：** `/interface/list`

此選單包含有關路由器上所有可用介面列表的資訊。有四個預定義列表 - `all`（包含所有介面）、`none`（不包含任何介面）、`dynamic`（包含動態介面）和 `static`（包含靜態介面）。也可以建立其他介面列表。

:::info
動態介面是指帶有 `dynamic` 標誌的介面。任何不帶 dynamic 標誌的介面都將屬於 `static` 介面列表。
:::

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string*) | 介面列表的名稱 |
| **include** (*string*) | 定義其成員被包含在該列表中的介面列表。可以新增多個列表，以逗號分隔 |
| **exclude** (*string*) | 定義其成員被排除在該列表之外的介面列表。可以新增多個列表，以逗號分隔 |

成員按以下順序新增到介面列表：

1. 將 Include 成員新增到介面列表。
2. 從列表中移除 Exclude 成員。
3. 將靜態配置的成員新增到列表中。

## 成員 {#members}

**子選單：** `/interface/list/member`

此子選單包含有關每個介面列表中靜態配置的介面成員的資訊。請注意，透過 include 和 exclude 語句動態新增的介面不會顯示在此子選單中。

| 屬性 | 描述 |
| :-- | :-- |
| **interface** (*string*) | 介面的名稱 |
| **list** (*string*) | 介面列表的名稱 |

:::info
在使用網橋和列表時需要格外小心。將網橋新增為成員並不等同於新增它的所有埠！而將所有從屬埠新增為成員也不等同於新增網橋本身。這尤其會影響鄰居發現的功能。
:::
