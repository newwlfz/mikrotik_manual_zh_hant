---
sidebar_key: "cli-reference/mpls/ldp"
title: "ldp"
sidebar_label: 'ldp'
source: https://manual.mikrotik.com/docs/cli-reference/mpls/ldp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/ldp {#mplsldp}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="lsr-id" typ="ipAddr" unset="1">標籤交換路由器的唯一 ID。</ArgTableRow>
<ArgTableRow arg="path-vector-limit" typ="num" unset="1">用於環路檢測的最大路徑向量限制。與 `loop-detect` 屬性配合使用。</ArgTableRow>
<ArgTableRow arg="hop-limit" typ="num" unset="1">用於環路檢測的最大跳數限制。與 `loop-detect` 屬性配合使用。</ArgTableRow>
<ArgTableRow arg="loop-detect" typ="bool" unset="1">定義是否執行 LSP 環路檢測。如果未在所有 LSR 上啟用，則無法正常工作。僅應在非 TTL 網路（例如 ATM）上使用。</ArgTableRow>
<ArgTableRow arg="use-explicit-null" typ="bool" unset="1">是否分發 explicit-null 標籤繫結。</ArgTableRow>
<ArgTableRow arg="distribute-for-default" typ="bool" unset="1">定義是否為預設路由對映標籤。</ArgTableRow>
<ArgTableRow arg="transport-addresses" typ="multi { array-id, transport-address: address (flags=46)
 }" unset="1">指定 LDP 會話連線的源地址，並將這些地址作為傳輸地址通告給 LDP 鄰居。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">此例項將操作的 VRF 表名稱。</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6)" unset="1">確定該例項支援的地址族。</ArgTableRow>
<ArgTableRow arg="preferred-afi" typ="enum (ip | ipv6)" unset="1">確定首選哪種地址族連線。該值也會設定到 dual-stack 元素中（如果使用）。</ArgTableRow>
</ArgTable>
