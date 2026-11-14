---
sidebar_key: "cli-reference/caps-man/aaa"
sidebar_position: 1
title: "aaa"
sidebar_label: "aaa"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/caps-man/aaa
captured_at: '2026-11-01T21:26:18+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## caps-man/aaa {#caps-manaaa}
**軟體包：** wireless-rep
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
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
