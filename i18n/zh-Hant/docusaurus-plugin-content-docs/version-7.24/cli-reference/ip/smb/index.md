---
sidebar_key: "cli-reference/ip/smb/index"
sidebar_position: 1
title: "smb"
sidebar_label: "smb"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/smb
captured_at: '2026-11-01T21:28:57+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/smb {#ipsmb}
**條件：** !smips
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="enum (no | auto | yes)"></ArgTableRow>
<ArgTableRow arg="domain" typ="string"></ArgTableRow>
<ArgTableRow arg="comment" typ="string"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface: iface_enum { all:0 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
