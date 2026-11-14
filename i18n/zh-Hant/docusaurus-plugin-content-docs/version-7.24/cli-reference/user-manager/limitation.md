---
sidebar_key: "cli-reference/user-manager/limitation"
sidebar_position: 5
title: "limitation"
sidebar_label: "limitation"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/user-manager/limitation
captured_at: '2026-11-01T21:30:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user-manager/limitation {#user-managerlimitation}
**軟體包：** userman-5
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="download-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="upload-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="transfer-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime-limit" typ="time"></ArgTableRow>
<ArgTableRow arg="reset-counters-start-time" typ="date"></ArgTableRow>
<ArgTableRow arg="reset-counters-interval" typ="alt { constant: enum (disabled | hourly | daily | weekly | monthly)
, reset-counters-interval: time
 }"></ArgTableRow>
<ArgTableRow arg="rate-limit-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-tx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-tx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-threshold-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-threshold-tx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-time-rx" typ="time"></ArgTableRow>
<ArgTableRow arg="rate-limit-burst-time-tx" typ="time"></ArgTableRow>
<ArgTableRow arg="rate-limit-min-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-min-tx" typ="num"></ArgTableRow>
<ArgTableRow arg="rate-limit-priority" typ="num"></ArgTableRow>
</ArgTable>
