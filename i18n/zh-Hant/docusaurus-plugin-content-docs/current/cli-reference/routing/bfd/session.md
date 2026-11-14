---
sidebar_key: "cli-reference/routing/bfd/session"
sidebar_position: 3
title: "session"
sidebar_label: 'session'
source: https://manual.mikrotik.com/docs/cli-reference/routing/bfd/session
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bfd/session {#routingbfdsession}
**型別：**目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="U" typ="up">up</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="multihop" typ="bool"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="local-address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (admin-down | down | init | up)"></ArgTableRow>
<ArgTableRow arg="state-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="desired-tx-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="actual-tx-interval" typ="time">裝置當前傳送 BFD 控制報文的即時頻率。</ArgTableRow>
<ArgTableRow arg="required-min-rx" typ="time"></ArgTableRow>
<ArgTableRow arg="remote-min-rx" typ="time"></ArgTableRow>
<ArgTableRow arg="remote-min-tx" typ="time"></ArgTableRow>
<ArgTableRow arg="multiplier" typ="num"></ArgTableRow>
<ArgTableRow arg="hold-time" typ="time"></ArgTableRow>
<ArgTableRow arg="packets-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-tx" typ="num"></ArgTableRow>
</ArgTable>
