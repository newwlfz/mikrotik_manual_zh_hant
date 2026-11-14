---
sidebar_key: "cli-reference/tool/bandwidth-server/index"
sidebar_position: 1
title: "bandwidth-server"
sidebar_label: "bandwidth-server"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/bandwidth-server
captured_at: '2026-11-01T21:30:14+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/bandwidth-server {#toolbandwidth-server}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="authenticate" typ="bool"></ArgTableRow>
<ArgTableRow arg="allocate-udp-ports-from" typ="num">UDP 埠範圍的起始值</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">最大併發測試數</ArgTableRow>
<ArgTableRow arg="allowed-addresses4" typ="object { address: ipPrefix
 }"></ArgTableRow>
<ArgTableRow arg="allowed-addresses6" typ="object { address: ip6Prefix
 }"></ArgTableRow>
</ArgTable>
