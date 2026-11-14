---
sidebar_key: "cli-reference/interface/monitor-traffic"
sidebar_position: 22
title: "monitor-traffic"
sidebar_label: 'monitor-traffic'
source: https://manual.mikrotik.com/docs/cli-reference/interface/monitor-traffic
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/monitor-traffic {#interfacemonitor-traffic}
**型別：** 命令
即時顯示每個介面的吞吐量（每秒速率）。多個介面會並排列印為多列；表格會持續重新整理。使用 `duration` 限制其執行時長。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="multi { array-id, interface: iface_enum { aggregate:0 }
 }">要監視的介面（或使用 `aggregate` 表示合併檢視）</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面名稱</ArgTableRow>
<ArgTableRow arg="rx-packets-per-second" typ="num">每秒接收封包數</ArgTableRow>
<ArgTableRow arg="rx-bits-per-second" typ="num">每秒接收位元數</ArgTableRow>
<ArgTableRow arg="fp-rx-packets-per-second" typ="num">Fast Path 每秒接收封包數</ArgTableRow>
<ArgTableRow arg="fp-rx-bits-per-second" typ="num">Fast Path 每秒接收位元數</ArgTableRow>
<ArgTableRow arg="rx-drops-per-second" typ="num">每秒接收丟棄數</ArgTableRow>
<ArgTableRow arg="rx-errors-per-second" typ="num">每秒接收錯誤數</ArgTableRow>
<ArgTableRow arg="tx-packets-per-second" typ="num">每秒傳送的封包數</ArgTableRow>
<ArgTableRow arg="tx-bits-per-second" typ="num">每秒傳送的位元數</ArgTableRow>
<ArgTableRow arg="fp-tx-packets-per-second" typ="num">Fast Path 每秒傳送的封包數</ArgTableRow>
<ArgTableRow arg="fp-tx-bits-per-second" typ="num">Fast Path 每秒傳送的位元數</ArgTableRow>
<ArgTableRow arg="tx-drops-per-second" typ="num">每秒傳送丟棄數</ArgTableRow>
<ArgTableRow arg="tx-queue-drops-per-second" typ="num">介面佇列每秒丟棄數</ArgTableRow>
<ArgTableRow arg="tx-errors-per-second" typ="num">每秒傳送錯誤數</ArgTableRow>
</ArgTable>
