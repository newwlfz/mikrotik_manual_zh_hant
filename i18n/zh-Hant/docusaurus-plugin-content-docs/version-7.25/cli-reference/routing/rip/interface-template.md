---
sidebar_key: "cli-reference/routing/rip/interface-template"
sidebar_position: 2
title: "interface-template"
sidebar_label: 'interface-template'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/rip/interface-template
captured_at: '2026-11-01T21:25:19+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/rip/interface-template {#routingripinterface-template}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="source-addresses" typ="object { address: address (flags=46)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="cost" typ="num"></ArgTableRow>
<ArgTableRow arg="split-horizon" typ="bool"></ArgTableRow>
<ArgTableRow arg="poison-reverse" typ="bool"></ArgTableRow>
<ArgTableRow arg="key-chain" typ="enum" unset="1">包含 MD5 金鑰的 key-chain 名稱。僅在需要 MD5 認證時設定。</ArgTableRow>
<ArgTableRow arg="password" typ="string" unset="1">用於明文認證的密碼。僅在需要明文認證時設定。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (passive | strict)" unset="1"></ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1"></ArgTableRow>
</ArgTable>
