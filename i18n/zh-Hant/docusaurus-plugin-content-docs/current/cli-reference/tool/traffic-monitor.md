---
sidebar_key: "cli-reference/tool/traffic-monitor"
sidebar_position: 27
title: "traffic-monitor"
sidebar_label: 'traffic-monitor'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-monitor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-monitor {#tooltraffic-monitor}
**型別：** 目錄

閾值觸發器：當介面的傳送或接收速率越過閾值時，執行一個[指令碼](../../developer-guides/scripting/index.md)（`on-event`）。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">流量監控條目的名稱</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">監控其速率的介面</ArgTableRow>
<ArgTableRow arg="traffic" typ="enum (transmitted | received) { transmitted:1, received:2 }">要監控的方向：`transmitted` 或 `received`</ArgTableRow>
<ArgTableRow arg="trigger" typ="enum (above | below | always) { above:1, below:2, always:3 }">`on-event` 的執行時機：速率超過 `above` 閾值時、低於 `below` 閾值時，或 `always`（每次輪詢時）。</ArgTableRow>
<ArgTableRow arg="threshold" typ="num">觸發器用於比較的流量速率，單位為位元每秒</ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { script: string
 }">觸發條件滿足時執行的指令碼</ArgTableRow>
</ArgTable>
