---
sidebar_key: "cli-reference/tool/sms/send"
sidebar_position: 2
title: "send"
sidebar_label: 'send'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/sms/send
captured_at: '2026-11-01T21:25:58+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/sms/send {#toolsmssend}
**條件：** !smips
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="port" typ="alt { serial: enum
, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="channel" typ="num"></ArgTableRow>
<ArgTableRow arg="phone-number" typ="string"></ArgTableRow>
<ArgTableRow arg="smsc" typ="string"></ArgTableRow>
<ArgTableRow arg="message" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (class-1 | class-0 | ussd)"></ArgTableRow>
<ArgTableRow arg="status-report-request" typ="bool"></ArgTableRow>
</ArgTable>
