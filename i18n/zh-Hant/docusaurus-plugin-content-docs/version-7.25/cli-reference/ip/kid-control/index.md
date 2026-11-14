---
sidebar_key: "cli-reference/ip/kid-control/index"
sidebar_position: 2
title: "kid-control"
sidebar_label: 'kid-control'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/kid-control
captured_at: '2026-11-01T21:24:16+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/kid-control {#ipkid-control}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="P" typ="paused">paused</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">blocked</ArgTableRow>
<ArgTableRow arg="L" typ="rate-limited">rate-limited</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="sun" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="mon" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tue" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="wed" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="thu" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="fri" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="sat" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="tur-sun" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }">週日不限速率的時間</ArgTableRow>
<ArgTableRow arg="tur-mon" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tur-tue" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tur-wed" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tur-thu" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tur-fri" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
<ArgTableRow arg="tur-sat" typ="multi { time: composite { start: time [0 .. 86400]
, end: time [0 .. 86400]
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="pause-left" typ="time"></ArgTableRow>
<ArgTableRow arg="pause-till" typ="date"></ArgTableRow>
</ArgTable>
