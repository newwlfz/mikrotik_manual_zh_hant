---
sidebar_key: "cli-reference/ip/firewall/address-list"
sidebar_position: 1
title: "address-list"
sidebar_label: 'address-list'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/firewall/address-list
captured_at: '2026-11-01T21:23:56+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/firewall/address-list {#ipfirewalladdress-list}
**型別：** 目錄

防火牆地址列表是由 IPv4 地址、字首和範圍組成的命名集合，filter、NAT、mangle 和 raw 規則透過 `src-address-list` 和 `dst-address-list` 與其匹配。條目可在此處新增，也可由 `add-src-to-address-list` 和 `add-dst-to-address-list` 規則動作新增，或從列表中的 DNS 名稱新增。這些動作會將封包傳遞給下一條規則。IPv6 地址放入 [`/ipv6/firewall/address-list`](../../ipv6/firewall/address-list.md)。參見 [地址列表](../../../firewall-and-quality-of-service/firewall/address-lists.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用：條目保留在列表中，但不匹配。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態：該條目具有超時，或者是以 `dynamic=yes` 新增、由帶有時間或 `none-dynamic` 的防火牆規則新增、來自已解析的 DNS 名稱或由其他功能（DNS、DHCP server）新增。動態條目不會儲存到配置或匯出中，重啟會將其清除。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">地址列表的名稱。新名稱會建立列表。規則使用 `src-address-list` 和 `dst-address-list` 匹配該列表。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { address: ipRange
, dns-name: string
 }">一個 IP 地址、一個字首、一個範圍或一個 DNS 名稱。帶有主機位的字首會儲存為其網路地址（`203.0.113.77/24` 變為 `203.0.113.0/24`）。恰好為一個字首的範圍會儲存為該字首（`198.51.100.0-198.51.100.255` 變為 `198.51.100.0/24`）；其他範圍仍保持為範圍。不是有效地址的文字會作為 DNS 名稱儲存，且不會報錯，因此諸如 `203.0.113.1-254` 這樣的簡短範圍不會匹配任何內容；請完整寫出範圍。對於 DNS 名稱，路由器會為應答中的每條 A 記錄新增一個動態條目，並以該名稱作為註釋，並在記錄過期時再次解析該名稱。已在列表中的地址會被拒絕，並提示 `already have such entry`；重疊條目會被接受。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">經過此時間後，路由器會移除該條目。帶有超時時間的條目是動態的（`D`）：它不會儲存在配置或匯出中，重啟會清除它。最大值為 `35w3d13h13m56s`。沒有超時時間時，條目會一直保留，直到您將其移除。</ArgTableRow>
<ArgTableRow arg="dynamic" typ="bool">使用 `yes` 時，條目是動態的（`D`）且沒有超時時間：它不會儲存在配置中，重啟會清除它。預設值：no。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="creation-time" typ="date">條目建立的時間。靜態條目在重啟後保留此時間；匯入的條目會獲得匯入時間。</ArgTableRow>
</ArgTable>
