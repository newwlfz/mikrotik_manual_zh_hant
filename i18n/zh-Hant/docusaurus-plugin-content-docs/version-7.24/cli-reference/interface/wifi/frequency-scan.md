---
title: "frequency-scan"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/wifi/frequency-scan
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/wifi/frequency-scan 
**類型：** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="radar">radar</ArgTableRow>
<ArgTableRow arg="P" typ="primary">primary</ArgTableRow>
<ArgTableRow arg="S" typ="secondary">secondary</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="rounds" typ="num"></ArgTableRow>
<ArgTableRow arg="save-file" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency" typ="object" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="networks" typ="num"></ArgTableRow>
<ArgTableRow arg="load" typ="num"></ArgTableRow>
<ArgTableRow arg="nf" typ="num"></ArgTableRow>
<ArgTableRow arg="max-signal" typ="num"></ArgTableRow>
<ArgTableRow arg="min-signal" typ="num"></ArgTableRow>
<ArgTableRow arg="srp-networks" typ="num"></ArgTableRow>
<ArgTableRow arg="srp-load" typ="num"></ArgTableRow>
</ArgTable>
