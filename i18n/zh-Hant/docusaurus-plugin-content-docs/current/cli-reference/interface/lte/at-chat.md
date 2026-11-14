---
sidebar_key: "cli-reference/interface/lte/at-chat"
sidebar_position: 2
title: "at-chat"
sidebar_label: 'at-chat'
source: https://manual.mikrotik.com/docs/cli-reference/interface/lte/at-chat
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/lte/at-chat {#interfacelteat-chat}
**條件：** !smips
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="input" typ="string">向調變解調器傳送命令，並在返回前等待任意輸出</ArgTableRow>
<ArgTableRow arg="wait" typ="alt { wait: enum (no | yes) { no:0, yes:3 }
 }">始終等待 3 秒</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="output" typ="string"></ArgTableRow>
</ArgTable>
