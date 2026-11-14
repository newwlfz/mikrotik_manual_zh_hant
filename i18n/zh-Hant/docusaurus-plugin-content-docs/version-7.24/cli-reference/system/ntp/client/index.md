---
sidebar_key: "cli-reference/system/ntp/client/index"
sidebar_position: 1
title: "client"
sidebar_label: "client"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/ntp/client
captured_at: '2026-11-01T21:29:54+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ntp/client {#systemntpclient}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (unicast | broadcast | multicast | manycast)"></ArgTableRow>
<ArgTableRow arg="servers" typ="multi { server-list: address (flags=46D)
 }"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="freq-drift" typ="num"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (stopped | waiting | synchronized | using-local-clock)"></ArgTableRow>
<ArgTableRow arg="synced-server" typ="address (flags=46D)"></ArgTableRow>
<ArgTableRow arg="synced-stratum" typ="num"></ArgTableRow>
<ArgTableRow arg="system-offset" typ="num"></ArgTableRow>
</ArgTable>
