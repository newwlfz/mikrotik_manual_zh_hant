---
sidebar_key: "cli-reference/ip/hotspot/ip-binding"
sidebar_position: 4
title: "ip-binding"
sidebar_label: 'ip-binding'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/hotspot/ip-binding
captured_at: '2026-11-01T21:24:03+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/hotspot/ip-binding {#iphotspotip-binding}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="P" typ="bypassed">bypassed</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">blocked</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="address" typ="ipRange"></ArgTableRow>
<ArgTableRow arg="to-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all) { all:0 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (regular | bypassed | blocked) { regular:0, bypassed:1, blocked:2 }"></ArgTableRow>
</ArgTable>
