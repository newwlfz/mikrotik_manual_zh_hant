---
title: "characteristics"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/iot/bluetooth/connections/characteristics
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## iot/bluetooth/connections/characteristics 
**套件：** iot
**類型：** 目錄

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="handle" typ="num"></ArgTableRow>
<ArgTableRow arg="service-name" typ="string"></ArgTableRow>
<ArgTableRow arg="service-uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="props" typ="multi { array-id, props: enum (bcast | read | write-no-resp | write | notify | indicate | write-signed | ext) { bcast:0x01, read:0x02, write-no-resp:0x04, write:0x08, notify:0x10, indicate:0x20, write-signed:0x40, ext:0x80 }
 }"></ArgTableRow>
<ArgTableRow arg="pdev" typ="enum"></ArgTableRow>
</ArgTable>
