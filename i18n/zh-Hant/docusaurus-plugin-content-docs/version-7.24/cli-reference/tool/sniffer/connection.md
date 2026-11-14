---
sidebar_key: "cli-reference/tool/sniffer/connection"
sidebar_position: 1
title: "connection"
sidebar_label: "connection"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/sniffer/connection
captured_at: '2026-11-01T21:30:20+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/sniffer/connection {#toolsnifferconnection}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="A" typ="active">已啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="composite { address: ipAddr
, port: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { address: ipAddr
, port: enum ()
 }"></ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { in: num
, out: num
 }"></ArgTableRow>
<ArgTableRow arg="resends" typ="composite { in: num
, out: num
 }"></ArgTableRow>
<ArgTableRow arg="mss" typ="composite { in: num
, out: num
 }"></ArgTableRow>
</ArgTable>
