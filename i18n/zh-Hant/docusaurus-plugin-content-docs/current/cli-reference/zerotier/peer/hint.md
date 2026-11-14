---
sidebar_key: "cli-reference/zerotier/peer/hint"
sidebar_position: 1
title: "hint"
sidebar_label: 'hint'
source: https://manual.mikrotik.com/docs/cli-reference/zerotier/peer/hint
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## zerotier/peer/hint {#zerotierpeerhint}
**包：** zerotier
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該項是否已停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum" mandatory="1">ZeroTier 例項名稱。</ArgTableRow>
<ArgTableRow arg="identity" typ="string" mandatory="1">對等端的 ZeroTier 身份。</ArgTableRow>
<ArgTableRow arg="addresses" typ="multi { array-id, array-id, address: composite { addr: address (flags=46)
, port: num [1 .. 65535]
 }
 }" mandatory="1">對等端的 IP 地址和埠列表。</ArgTableRow>
</ArgTable>
