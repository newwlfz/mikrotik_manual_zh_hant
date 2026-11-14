---
sidebar_key: "cli-reference/ip/firewall/address-list"
sidebar_position: 1
title: "address-list"
sidebar_label: "address-list"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/firewall/address-list
captured_at: '2026-11-01T21:28:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/firewall/address-list {#ipfirewalladdress-list}
**型別：** 目錄

防火牆地址列表允許使用者建立按共同名稱分組的 IP 地址列表。隨後，防火牆的 filter、mangle 和 NAT 功能可以使用這些地址列表來匹配封包。

地址列表記錄還可以透過 NAT、Mangle 和 Filter 功能中的 `action=add-src-to-address-list` 或 `action=add-dst-to-address-list` 項動態更新。

帶有 `add-src-to-address-list` 或 `add-dst-to-address-list` 動作的防火牆規則以 passthrough 模式工作，這意味著匹配的封包將被傳遞給後續防火牆規則。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">IP 地址將被新增到的地址列表名稱。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { address: ipRange
, dns-name: string
 }">要新增到地址列表的單個 IP 地址或 IP 範圍，或 DNS 名稱。例如，你可以輸入 `192.168.0.0-192.168.1.255`，儲存時它會自動將輸入的條目修改為 192.168.0.0/23。IP-IP 範圍僅支援 IPv4 地址。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">地址從地址列表中被移除之前的時間。如果未指定 timeout，則地址將永久儲存在地址列表中；否則地址將儲存在 RAM 中，並在系統重啟後被移除。</ArgTableRow>
<ArgTableRow arg="dynamic" typ="bool">該條目是否為動態建立。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="creation-time" typ="date">建立該條目的時間。</ArgTableRow>
</ArgTable>
