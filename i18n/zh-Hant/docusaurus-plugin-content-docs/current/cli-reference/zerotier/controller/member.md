---
sidebar_key: "cli-reference/zerotier/controller/member"
sidebar_position: 1
title: "member"
sidebar_label: 'member'
source: https://manual.mikrotik.com/docs/cli-reference/zerotier/controller/member
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## zerotier/controller/member {#zerotiercontrollermember}
**包：** zerotier
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">成員是否處於非活動狀態。</ArgTableRow>
<ArgTableRow arg="A" typ="authorized">成員是否已授權。</ArgTableRow>
<ArgTableRow arg="B" typ="bridge">成員是否充當網橋。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="disabled" typ="bool">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="name" typ="string">成員名稱。</ArgTableRow>
<ArgTableRow arg="network" typ="enum" mandatory="1">成員所屬的網路。</ArgTableRow>
<ArgTableRow arg="zt-address" typ="string" mandatory="1">成員的 ZeroTier 地址。</ArgTableRow>
<ArgTableRow arg="authorized" typ="bool">成員是否已獲授權加入網路。</ArgTableRow>
<ArgTableRow arg="bridge" typ="bool">成員是否充當網橋。</ArgTableRow>
<ArgTableRow arg="ip-address" typ="multi { array-id, addr: address (flags=46)
 }">分配給成員的 IP 地址。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="lost" typ="bool">與成員的連線是否已丟失。</ArgTableRow>
<ArgTableRow arg="last-seen" typ="time">自上次檢測到該成員以來經過的時間。</ArgTableRow>
</ArgTable>
