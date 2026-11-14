---
sidebar_key: "cli-reference/ipv6/nd/prefix/index"
sidebar_position: 2
title: "prefix"
sidebar_label: "prefix"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ipv6/nd/prefix
captured_at: '2026-11-01T21:29:08+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/nd/prefix {#ipv6ndprefix}
**型別：** 目錄

路由器通告（RA）訊息中傳送的字首資訊，用於無狀態地址自動配置（[RFC 4862](https://tools.ietf.org/html/rfc4862)）。預設情況下，自動配置僅適用於主機，不適用於路由器。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="prefix" typ="alt { none: enum (none) { none:0 }
, prefix: ip6Prefix
 }">用於無狀態地址自動配置的字首。如果選擇 "none" 選項，RouterOS 僅通告選項，不包含特定字首。</ArgTableRow>
<ArgTableRow arg="6to4-interface" typ="iface_enum { none:0xffffffff }">如果設定，RouterOS 會將此字首與介面的 IPv4 地址組合，以生成有效的 6to4 字首。RouterOS 會將前 16 位替換為 2002，並將接下來的 32 位替換為介面配置的 IPv4 地址。它會按配置通告剩餘的 80 位（包括 SLA ID）。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">執行無狀態自動配置的介面。</ArgTableRow>
<ArgTableRow arg="on-link" typ="bool">設定後，表示 RouterOS 可將此字首視為 on-link。未設定時，RA 訊息不會對此字首的 on-link 或 off-link 狀態作出任何宣告。即使此字首中的某些地址保持 off-link，此字首仍可能用於地址配置。</ArgTableRow>
<ArgTableRow arg="autonomous" typ="bool">設定後，表示 RouterOS 可將此字首用於自主地址配置。否則，RouterOS 會忽略此字首資訊。</ArgTableRow>
<ArgTableRow arg="dhcp6-pd-preferred" typ="bool">表示用戶端應根據 [RFC 9762](https://datatracker.ietf.org/doc/rfc9762/) 使用 DHCPv6 Prefix Delegation。</ArgTableRow>
<ArgTableRow arg="valid-lifetime" typ="alt { special: enum (infinity) { infinity:0xffffffff }
, value: time
, ticking: time
 }">封包傳送後地址保持有效的時間長度。有效生存期必須大於或等於首選生存期。[`Read more >>`](../../../../getting-started/networking-fundamentals/ipv6-neighbor-discovery.md#address-states)</ArgTableRow>
<ArgTableRow arg="preferred-lifetime" typ="alt { special: enum (infinity) { infinity:0xffffffff }
, value: time
, ticking: time
 }">封包傳送後，生成的地址變為棄用狀態的時間。棄用地址僅用於現有連線，並在有效生存期到期之前仍可使用。[`Read more >>`](../../../../getting-started/networking-fundamentals/ipv6-neighbor-discovery.md#address-states)</ArgTableRow>
</ArgTable>
