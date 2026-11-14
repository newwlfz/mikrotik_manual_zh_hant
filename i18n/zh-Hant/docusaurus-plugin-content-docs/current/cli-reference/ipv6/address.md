---
sidebar_key: "cli-reference/ipv6/address"
sidebar_position: 1
title: "address"
sidebar_label: 'address'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/address
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/address {#ipv6address}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="G" typ="global">global</ArgTableRow>
<ArgTableRow arg="L" typ="link-local">link-local</ArgTableRow>
<ArgTableRow arg="S" typ="slave">地址是否屬於作為某個其他主介面的從埠的介面。</ArgTableRow>
<ArgTableRow arg="d" typ="deprecated">deprecated</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="composite { address: ip6Addr
, netmask: [ num [ .. 128]]
 }">
IPv6 地址。如果指定了 `from-pool` 引數，地址也可以從地址池構建。
例如，如果 address 設定為 `::1/64`，則地址將按如下方式構建：`<prefix_from_pool>::1/64`
</ArgTableRow>
<ArgTableRow arg="from-pool" typ="enum">用於從中獲取字首以構建 IPv6 地址的地址池名稱，地址的最後一部分取自 address 屬性。</ArgTableRow>
<ArgTableRow arg="from-pool-policy" typ="enum (recommended | strict | without-acquire)">
指定在設定了 `from-pool` 引數時如何從地址池獲取字首。

- 如果提供了 subnet-id，`recommended` 選項將使用 `address` 作為字尾，並使用 **subnet-id**。
- `strict` 將使用 **address** 作為嚴格字尾。
- `without-acquire` 不會從地址池分配字首，並允許其他服務使用完全相同的字首。`without-acquire` 選項主要應用於在路由器上建立 SLAAC 地址，而該路由器同時還是 DHCPv6 伺服器，向同一子網的用戶端提供地址。
</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">指定配置 IPv6 地址的介面。你可以從路由器上可用的介面池中選擇它。</ArgTableRow>
<ArgTableRow arg="eui-64" typ="bool">是否計算 EUI-64 地址並將其用作 IPv6 地址的最後 64 位。</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool">是否啟用無狀態地址配置。該地址的字首會使用 ICMPv6 協定自動向主機通告三次。對於字首長度為 64 的地址，此選項預設啟用。如果地址被刪除或更改，則舊字首將被棄用：會使用 ICMPv6 協定自動向主機通告舊字首三次，並將生存期設定為 `0s`。</ArgTableRow>
<ArgTableRow arg="no-dad" typ="bool">如果啟用（yes）- 會停用介面上 IPv6 地址的重複地址檢測（DAD）。在希望為裝置分配靜態 IPv6 地址並避免 DAD 引起的延遲的場景中，這會很有用。</ArgTableRow>
<ArgTableRow arg="auto-link-local" typ="bool">如果你想手動向介面新增鏈路本地地址，此設定允許你覆蓋自動生成的 IPv6 鏈路本地地址。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-interface" typ="iface_enum">地址實際所在的介面。例如，如果 address 配置在乙太網介面上，並且該乙太網介面被新增到網橋，則實際介面是網橋，而不是乙太網介面。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">指示此 IP 地址關聯到哪個 VRF。</ArgTableRow>
<ArgTableRow arg="valid" typ="alt { valid: enum (forever) { forever:-1 }
, valid: time
 }"></ArgTableRow>
<ArgTableRow arg="preferred" typ="alt { preferred: enum (forever) { forever:-1 }
, preferred: time
 }"></ArgTableRow>
</ArgTable>
