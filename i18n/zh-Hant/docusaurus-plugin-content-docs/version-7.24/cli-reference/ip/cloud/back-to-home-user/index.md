---
sidebar_key: "cli-reference/ip/cloud/back-to-home-user/index"
sidebar_position: 1
title: "back-to-home-user"
sidebar_label: "back-to-home-user"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/cloud/back-to-home-user
captured_at: '2026-11-01T21:28:24+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/cloud/back-to-home-user {#ipcloudback-to-home-user}
**系統能力：** cloud-vpn
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="A" typ="active">已啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="expires" typ="alt { expires: enum (never) { never:0xFFFFFFFF }
, interval: time
, date-time: date
 }"></ArgTableRow>
<ArgTableRow arg="allow-lan" typ="bool"></ArgTableRow>
<ArgTableRow arg="private-key" typ="string"></ArgTableRow>
<ArgTableRow arg="public-key" typ="string"></ArgTableRow>
<ArgTableRow arg="file-access" typ="enum (disabled | read-only | full)"></ArgTableRow>
<ArgTableRow arg="file-access-path" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="client-address" typ="multi { address: address (flags=46/)
 }"></ArgTableRow>
<ArgTableRow arg="file-access-token" typ="string"></ArgTableRow>
</ArgTable>
