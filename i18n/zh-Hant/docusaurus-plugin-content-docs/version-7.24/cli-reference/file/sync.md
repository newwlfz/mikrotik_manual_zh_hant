---
title: "sync"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/file/sync
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## file/sync 
**套件:** rose-storage
**類型:** 目錄

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="remote-address" typ="multi { array-id, address: string
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (upload | download)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="local-path" typ="file"></ArgTableRow>
<ArgTableRow arg="remote-path" typ="string"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
