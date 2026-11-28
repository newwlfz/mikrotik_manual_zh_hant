---
title: "at-chat"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/lte/at-chat
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/lte/at-chat 
**條件：** !smips
**類型：** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="input" typ="string">sends command to modem and waits for any output before returning</ArgTableRow>
<ArgTableRow arg="wait" typ="alt { wait: enum (no | yes) { no:0, yes:3 }
 }">always wait 3s</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="output" typ="string"></ArgTableRow>
</ArgTable>
