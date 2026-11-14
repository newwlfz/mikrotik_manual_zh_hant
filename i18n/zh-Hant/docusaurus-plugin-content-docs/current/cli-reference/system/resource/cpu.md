---
sidebar_key: "cli-reference/system/resource/cpu"
sidebar_position: 1
title: "cpu"
sidebar_label: 'cpu'
source: https://manual.mikrotik.com/docs/cli-reference/system/resource/cpu
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/resource/cpu {#systemresourcecpu}
**型別：** Directory
系統資源計數器的每 CPU 使用率明細。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="cpu" typ="string">顯示其使用率的 CPU 的標識號</ArgTableRow>
<ArgTableRow arg="load" typ="num">CPU 使用率，以百分比表示</ArgTableRow>
<ArgTableRow arg="irq" typ="num">IRQ 使用率，以百分比表示</ArgTableRow>
<ArgTableRow arg="disk" typ="num">磁碟使用率，以百分比表示</ArgTableRow>
</ArgTable>
