---
sidebar_key: "cli-reference/ip/dhcp-server/config"
sidebar_position: 2
title: "config"
sidebar_label: "config"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dhcp-server/config
captured_at: '2026-11-01T21:28:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/config {#ipdhcp-serverconfig}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="store-leases-disk" typ="alt { symbolic-names: enum (immediately | never) { immediately:0, never:0xffffffff }
, time-interval: time
 }"></ArgTableRow>
<ArgTableRow arg="accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="radius-password" typ="alt { user: enum (empty | same-as-user)
, password: string
 }"></ArgTableRow>
</ArgTable>
