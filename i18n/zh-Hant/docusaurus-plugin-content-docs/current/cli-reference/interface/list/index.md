---
sidebar_key: "cli-reference/interface/list"
title: "list"
sidebar_label: 'list'
source: https://manual.mikrotik.com/docs/cli-reference/interface/list
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/list {#interfacelist}
**型別：**目錄

介面列表允許定義一組介面，以便在基於介面的不同配置部分（如 Neighbour Discovery、Firewall、Bridge 和 Internet Detect）中更輕鬆地管理介面。

共有四個預定義列表：`all`（包含所有介面）、`none`（不包含任何介面）、`dynamic`（包含動態介面）和 `static`（包含靜態介面）。你還可以建立其他介面列表。

:::info
動態介面是帶有 "dynamic" 標誌的介面。任何沒有 dynamic 標誌的介面都將屬於 `static` 介面列表。
:::

成員按以下順序新增到介面列表中：

1. 將 Include 成員新增到介面列表。
2. 從列表中移除 Exclude 成員。
3. 將靜態配置的成員新增到列表中。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="builtin">內建系統列表。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態建立的列表。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">介面列表的名稱。預定義列表包括 "all"、"none"、"dynamic" 和 "static"。</ArgTableRow>
<ArgTableRow arg="include" typ="multi { include-list: enum
 }">其成員會包含在此列表中的介面列表。可以指定多個列表，用逗號分隔。</ArgTableRow>
<ArgTableRow arg="exclude" typ="multi { exclude-list: enum
 }">其成員會從此列表中排除的介面列表。可以指定多個列表，用逗號分隔。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="dynamic" typ="bool">介面列表是否為動態建立。</ArgTableRow>
</ArgTable>
