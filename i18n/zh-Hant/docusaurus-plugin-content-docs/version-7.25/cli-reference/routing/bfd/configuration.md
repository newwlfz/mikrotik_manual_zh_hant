---
sidebar_key: "cli-reference/routing/bfd/configuration"
sidebar_position: 2
title: "configuration"
sidebar_label: 'configuration'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/bfd/configuration
captured_at: '2026-11-01T21:25:02+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bfd/configuration {#routingbfdconfiguration}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="vrf" typ="enum" unset="1">此配置適用的虛擬路由轉發例項。</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }" unset="1">應啟用 BFD 配置的介面列表。</ArgTableRow>
<ArgTableRow arg="addresses" typ="object { address: alt { ipv6: ip6Prefix
, ip: ipPrefix
 }
 }" unset="1">此配置條目僅適用於與這些特定遠端鄰居建立的 BFD 會話。</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum" unset="1">防火牆地址列表名稱。如果遠端 IP 地址包含在指定列表中，則應用 BFD 配置。</ArgTableRow>
<ArgTableRow arg="min-tx" typ="time" unset="1">本地路由器向鄰居傳送 BFD 封包時希望使用的傳輸間隔。</ArgTableRow>
<ArgTableRow arg="min-rx" typ="time" unset="1">本地路由器在接收的 BFD 封包之間要求的最小接收間隔。</ArgTableRow>
<ArgTableRow arg="multiplier" typ="num" unset="1">此值會與協商後的傳輸間隔相乘，以確定 **Hold Time**；如果在 Hold Time 內未收到任何封包，則鄰居被宣告為 down。 `Hold Time = negotiated interval × multiplier`</ArgTableRow>
<ArgTableRow arg="forbid-bfd" typ="bool" unset="1">如果 = **yes**：匹配條件的 BFD 會話將被禁止。</ArgTableRow>
<ArgTableRow arg="keyring" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>
