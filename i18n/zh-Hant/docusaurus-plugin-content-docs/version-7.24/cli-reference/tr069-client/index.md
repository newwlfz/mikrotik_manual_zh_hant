---
sidebar_key: "cli-reference/tr069-client/index"
sidebar_position: 1
title: "tr069-client"
sidebar_label: "tr069-client"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tr069-client
captured_at: '2026-11-01T21:30:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tr069-client {#tr069-client}
**軟體包：** tr069-client
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="enum (yes | no)"></ArgTableRow>
<ArgTableRow arg="acs-url" typ="string"></ArgTableRow>
<ArgTableRow arg="username" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="periodic-inform-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="periodic-inform-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="connection-request-username" typ="string"></ArgTableRow>
<ArgTableRow arg="connection-request-password" typ="string"></ArgTableRow>
<ArgTableRow arg="connection-request-port" typ="num"></ArgTableRow>
<ArgTableRow arg="provisioning-code" typ="string"></ArgTableRow>
<ArgTableRow arg="client-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (yes | no)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (disabled | initializing | error | waiting-url | running)"></ArgTableRow>
<ArgTableRow arg="last-session-error" typ="string"></ArgTableRow>
<ArgTableRow arg="retry-count" typ="num"></ArgTableRow>
</ArgTable>
