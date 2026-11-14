---
sidebar_key: "cli-reference/ip/address"
sidebar_position: 1
title: "address"
sidebar_label: 'address'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/address
captured_at: '2026-11-01T21:23:47+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/address {#ipaddress}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="S" typ="slave">該地址是否屬於一個作為某個其他主介面的從埠的介面。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="composite { address: ipAddr
, netmask: [ num [ .. 32]]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="network" typ="ipAddr">網路地址，即使用 address 本身和 netmask 從 address 引數計算出的地址。</ArgTableRow>
<ArgTableRow arg="netmask" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="broadcast" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">指定配置該 IPv4 地址的介面。可以從路由器上可用的介面池中選擇它。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-interface" typ="iface_enum">地址所設定到的實際介面。例如，如果地址配置在 ethernet 介面上，並且該 ethernet 介面被新增到 bridge，那麼實際介面是 bridge，而不是 ethernet。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">指示此 IP 地址關聯到哪個 VRF。</ArgTableRow>
</ArgTable>
