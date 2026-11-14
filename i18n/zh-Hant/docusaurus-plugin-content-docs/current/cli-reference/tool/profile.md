---
sidebar_key: "cli-reference/tool/profile"
sidebar_position: 17
title: "profile"
sidebar_label: 'profile'
source: https://manual.mikrotik.com/docs/cli-reference/tool/profile
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/profile {#toolprofile}
**型別：**命令

按 RouterOS 程式型別顯示 CPU 使用率，可對所有核心彙總統計，也可按核心分別統計。請參閱 [分析器](../../diagnostics-monitoring-and-troubleshooting/profiler.md) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="cpu" typ="enum (all | total) { all:0xfffffffe, total:0xfffffffd }" syscap="smp">在多核系統上選擇 CPU 檢視：`total`（預設值）彙總所有核心的使用率，`all` 為每個核心顯示單獨的行，而整數（`0` .. 核心數減一）則只顯示該核心。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">程式分類名稱（例如 `wireless`、`console`）。每個核心的彙總行命名為 `cpu0`、`cpu1`、...，彙總檢視會額外新增一行 `total`。</ArgTableRow>
<ArgTableRow arg="cpu" typ="num" syscap="smp">該行使用率所屬的 CPU 核心（僅限按核心檢視）。</ArgTableRow>
<ArgTableRow arg="usage" typ="num">CPU 的使用份額，以百分比表示，自上一輸出幀以來測量。</ArgTableRow>
</ArgTable>
