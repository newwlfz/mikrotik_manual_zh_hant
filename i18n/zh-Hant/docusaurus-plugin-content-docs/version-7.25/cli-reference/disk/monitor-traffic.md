---
sidebar_key: "cli-reference/disk/monitor-traffic"
sidebar_position: 7
title: "monitor-traffic"
sidebar_label: 'monitor-traffic'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/disk/monitor-traffic
captured_at: '2026-11-01T21:22:11+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/monitor-traffic {#diskmonitor-traffic}
**條件：** !smips
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="io-ops" typ="num">自上次 `reset-counters` 以來的 I/O 操作總數。</ArgTableRow>
<ArgTableRow arg="io-errors" typ="num">I/O 錯誤總數。</ArgTableRow>
<ArgTableRow arg="slot" typ="string">正在監控的磁碟。</ArgTableRow>
<ArgTableRow arg="read-ops" typ="num">讀取操作總數。</ArgTableRow>
<ArgTableRow arg="read-ops-per-second" typ="num">每秒讀取運算元。</ArgTableRow>
<ArgTableRow arg="read-bytes" typ="num">讀取總位元組數。</ArgTableRow>
<ArgTableRow arg="read-rate" typ="num">當前讀取速度。</ArgTableRow>
<ArgTableRow arg="read-merges" typ="num">合併讀取操作總數（驅動程式合併的相鄰請求）。</ArgTableRow>
<ArgTableRow arg="read-time" typ="time">讀取所花費的總時間。</ArgTableRow>
<ArgTableRow arg="write-ops" typ="num">寫入操作總數。</ArgTableRow>
<ArgTableRow arg="write-ops-per-second" typ="num">每秒寫入運算元。</ArgTableRow>
<ArgTableRow arg="write-bytes" typ="num">寫入總位元組數。</ArgTableRow>
<ArgTableRow arg="write-rate" typ="num">當前寫入速度。</ArgTableRow>
<ArgTableRow arg="write-merges" typ="num">合併寫入操作總數。</ArgTableRow>
<ArgTableRow arg="write-time" typ="time">寫入所花費的總時間。</ArgTableRow>
<ArgTableRow arg="in-flight-ops" typ="num">當前在磁碟上排隊的運算元。</ArgTableRow>
<ArgTableRow arg="active-time" typ="time">磁碟忙於處理請求的總時間。</ArgTableRow>
<ArgTableRow arg="wait-time" typ="time">請求在被處理前在佇列中等待的總時間。</ArgTableRow>
<ArgTableRow arg="discard-ops" typ="num">discard（TRIM）操作總數。</ArgTableRow>
<ArgTableRow arg="discard-bytes" typ="num">已丟棄的總位元組數。</ArgTableRow>
<ArgTableRow arg="discard-merges" typ="num">合併 discard 操作總數。</ArgTableRow>
<ArgTableRow arg="discard-time" typ="time">執行丟棄所花費的總時間。</ArgTableRow>
<ArgTableRow arg="flush-ops" typ="num">flush 操作總數。</ArgTableRow>
<ArgTableRow arg="flush-time" typ="time">執行 flush 所花費的總時間。</ArgTableRow>
</ArgTable>
