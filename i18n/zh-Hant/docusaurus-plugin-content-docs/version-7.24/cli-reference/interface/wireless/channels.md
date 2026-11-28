---
title: "channels"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/wireless/channels
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/wireless/channels 
**套件:** wireless-rep
**類型:** 目錄

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="width" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="band" typ="enum (2ghz-b | 2ghz-onlyg | 2ghz-b/g | 5ghz-a | 5ghz-onlyn | 5ghz-a/n | 2ghz-onlyn | 2ghz-b/g/n | 2ghz-g/n | 5ghz-a/n/ac | 5ghz-n/ac | 5ghz-onlyac)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="extension-channel" typ="enum (disabled | Ce | eC | Ceee | eCee | eeCe | eeeC)"></ArgTableRow>
</ArgTable>
