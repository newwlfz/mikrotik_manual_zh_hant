---
sidebar_key: "cli-reference/mpls/ldp/interface"
sidebar_position: 3
title: "interface"
sidebar_label: 'interface'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/mpls/ldp/interface
captured_at: '2026-11-01T21:24:47+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/ldp/interface {#mplsldpinterface}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="enum ()" mandatory="1">介面或介面列表的名稱，LDP 將在其中偵聽。</ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time" unset="1">路由器在指定介面上傳送的 hello 報文之間的間隔。預設值為 5s。</ArgTableRow>
<ArgTableRow arg="hold-time" typ="time" unset="1">指定介面上發現的鄰居在多長時間後被宣告為不可達。預設值為 15s。</ArgTableRow>
<ArgTableRow arg="transport-addresses" typ="multi { array-id, transport-address: address (flags=46)
 }" unset="1">如果傳輸地址與 LDP Instance 設定不同，則使用這些傳輸地址。</ArgTableRow>
<ArgTableRow arg="accept-dynamic-neighbors" typ="bool" unset="1">定義是動態發現鄰居，還是僅使用在 LDP neighbors 選單中靜態配置的鄰居。</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6)" unset="1">確定介面地址族。僅考慮例項配置為支援的 AFI。如果未顯式指定該值，則視為等於例項支援的 AFI。</ArgTableRow>
</ArgTable>
