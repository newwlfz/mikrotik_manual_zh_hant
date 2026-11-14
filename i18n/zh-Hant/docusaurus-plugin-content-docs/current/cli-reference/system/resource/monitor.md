---
sidebar_key: "cli-reference/system/resource/monitor"
sidebar_position: 4
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/cli-reference/system/resource/monitor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/resource/monitor {#systemresourcemonitor}
**型別：** 命令
即時系統資源監控輸出（表格持續重新整理；在 `duration` 後停止）。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="cpu-used" typ="num">所有核心的總 CPU 使用率</ArgTableRow>
<ArgTableRow arg="cpu-used-per-core" typ="multi { cpu-used: num
 }" syscap="smp">每個核心一行，顯示其百分比使用率</ArgTableRow>
<ArgTableRow arg="free-memory" typ="num">空閒記憶體，單位 KiB</ArgTableRow>
</ArgTable>
