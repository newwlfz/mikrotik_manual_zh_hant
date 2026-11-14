---
sidebar_key: "cli-reference/system/resource/irq"
title: "irq"
sidebar_label: 'irq'
source: https://manual.mikrotik.com/docs/cli-reference/system/resource/irq
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/resource/irq {#systemresourceirq}
**型別：** Directory
每個中斷源的 IRQ 計數器。使用 `cpu=auto` 時，IRQ 處理按中斷計數進行均衡（NAPI 輔助）；僅在需要時將 IRQ 固定到特定核心。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="o" typ="read-only">只讀（CPU 分配由硬體固定）</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="cpu" typ="num">IRQ 所繫結到的 CPU；`auto` 表示由排程器根據中斷計數進行均衡</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="irq" typ="num">IRQ 標識號</ArgTableRow>
<ArgTableRow arg="users" typ="object { user: alt { interface: iface_enum
, other: string
 }
 }">繫結到該 IRQ 的程式/驅動</ArgTableRow>
<ArgTableRow arg="active-cpu" typ="num">在多核系統上當前正在處理該 IRQ 的 CPU</ArgTableRow>
<ArgTableRow arg="count" typ="num">已處理的中斷數量（在乙太網介面上，中斷 = 封包）</ArgTableRow>
<ArgTableRow arg="per-cpu-count" typ="multi { count: num
 }">以列表形式給出的每 CPU 中斷計數</ArgTableRow>
</ArgTable>
