---
sidebar_key: "cli-reference/interface/monitor-traffic"
sidebar_position: 22
title: "monitor-traffic"
sidebar_label: 'monitor-traffic'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/monitor-traffic
captured_at: '2026-11-01T21:22:53+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/monitor-traffic {#interfacemonitor-traffic}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="multi { array-id, interface: iface_enum { aggregate:0 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="rx-packets-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bits-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-rx-packets-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-rx-bits-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-drops-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-errors-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packets-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-bits-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-tx-packets-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-tx-bits-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-drops-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-queue-drops-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-errors-per-second" typ="num"></ArgTableRow>
</ArgTable>
