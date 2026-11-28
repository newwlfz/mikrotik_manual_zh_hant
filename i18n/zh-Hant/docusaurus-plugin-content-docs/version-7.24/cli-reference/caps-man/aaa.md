---
title: "aaa"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/caps-man/aaa
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## caps-man/aaa 
**套件:** wireless-rep
**類型:** 設定目錄

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-format" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-mode" typ="enum (as-username | as-username-and-password) { as-username:0, as-username-and-password:1 }"></ArgTableRow>
<ArgTableRow arg="mac-caching" typ="alt { mac-caching-disable: enum (disabled) { disabled:0 }
, mac-caching-time: time
 }"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="alt { interim-update-disable: enum (disabled) { disabled:0 }
, interim-update-time: time
 }"></ArgTableRow>
<ArgTableRow arg="called-format" typ="enum (mac:ssid | mac | ssid)"></ArgTableRow>
</ArgTable>
