---
sidebar_key: "cli-reference/ipv6/firewall/address-list"
sidebar_position: 1
title: "address-list"
sidebar_label: 'address-list'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ipv6/firewall/address-list
captured_at: '2026-11-01T21:24:38+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/firewall/address-list {#ipv6firewalladdress-list}
**型別：** 目錄

IPv6 防火牆地址列表是一組命名的 IPv6 地址和字首，IPv6 filter、NAT、mangle 和 raw 規則透過 `src-address-list` 和 `dst-address-list` 與之匹配。條目在此處新增，也可由 `add-src-to-address-list` 和 `add-dst-to-address-list` 規則動作新增，以及從列表中的 DNS 名稱新增。這些動作會把封包傳遞給下一條規則。IPv6 列表與 [`/ip/firewall/address-list`](../../ip/firewall/address-list.md) 中的 IPv4 列表相互獨立，即使兩個列表同名也是如此。參見 [地址列表](../../../firewall-and-quality-of-service/firewall/address-lists.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用：條目保留在列表中，但不匹配。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態：該條目具有超時，或者是以 `dynamic=yes` 新增、由帶有時間或 `none-dynamic` 的防火牆規則新增、來自已解析的 DNS 名稱或由其他功能（DNS、DHCP server）新增。動態條目不會儲存到配置或匯出中，重啟會將其清除。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">地址列表的名稱。使用新名稱會建立該列表。規則透過 `src-address-list` 和 `dst-address-list` 匹配該列表。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { address: ip6Prefix
, dns-name: string
 }">IPv6 地址、字首或 DNS 名稱。帶有主機位的字首會以其網路地址儲存，不帶字首長度的地址會以 /128 儲存。不接受範圍（`is not a valid dns name`）。對於 DNS 名稱，路由器會為應答中的每條 AAAA 記錄新增一個動態條目，並以該名稱作為註釋，並在記錄過期時重新解析該名稱。如果地址已在列表中，則會以 `already have such entry` 拒絕。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">路由器在此時間之後刪除該條目。帶超時的條目是動態的（`D`）：它不會儲存在配置或匯出中，重啟後會被清除。最大值為 `35w3d13h13m56s`。沒有超時時，條目會一直保留，直到你將其刪除。</ArgTableRow>
<ArgTableRow arg="dynamic" typ="bool">設為 `yes` 時，條目是動態的（`D`）且沒有超時：它不會儲存在配置中，重啟後會被清除。預設值：no。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="creation-time" typ="date">條目建立的時間。靜態條目在重啟後保留此時間；匯入的條目會獲得匯入時間。</ArgTableRow>
</ArgTable>
