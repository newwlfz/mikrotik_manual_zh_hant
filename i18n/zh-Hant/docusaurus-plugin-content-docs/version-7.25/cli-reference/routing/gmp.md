---
sidebar_key: "cli-reference/routing/gmp"
sidebar_position: 6
title: "gmp"
sidebar_label: 'gmp'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/gmp
captured_at: '2026-11-01T21:25:11+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/gmp {#routinggmp}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }">介面名稱，支援多個介面和介面列表。</ArgTableRow>
<ArgTableRow arg="groups" typ="object { group: address (flags=46)
 }">介面要使用的多播組地址，支援多個組地址。</ArgTableRow>
<ArgTableRow arg="exclude" typ="switch">當設定了 `exclude` 時，介面期望拒絕來自已配置 `sources` 的多播資料。未使用此選項時，介面將為已配置的 `sources` 發出源特定加入。</ArgTableRow>
<ArgTableRow arg="sources" typ="object { source: address (flags=46)
 }" unset="1">介面使用的源地址列表，支援多個源地址。當 IGMPv3 或 MLDv2 協定處於活動狀態時，此設定會生效。</ArgTableRow>
</ArgTable>
