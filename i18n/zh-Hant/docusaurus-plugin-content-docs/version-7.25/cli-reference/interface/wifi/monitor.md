---
sidebar_key: "cli-reference/interface/wifi/monitor"
sidebar_position: 13
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/wifi/monitor
captured_at: '2026-11-01T21:23:13+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wifi/monitor {#interfacewifimonitor}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="ap-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="registered-peers" typ="num"></ArgTableRow>
<ArgTableRow arg="authorized-peers" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-power" typ="num"></ArgTableRow>
<ArgTableRow arg="channel-priorities" typ="multi { array-id, channel: string
 }"></ArgTableRow>
<ArgTableRow arg="afc-status" typ="string"></ArgTableRow>
<ArgTableRow arg="afc-sp-rules" typ="multi { array-id, channel: string
 }"></ArgTableRow>
<ArgTableRow arg="hw-protection-mode" typ="enum (none | rts-cts | cts-to-self)"></ArgTableRow>
<ArgTableRow arg="mld-link-id" typ="num"></ArgTableRow>
</ArgTable>
