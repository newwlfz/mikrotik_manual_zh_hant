---
sidebar_key: "cli-reference/zerotier/interface"
sidebar_position: 2
title: "interface"
sidebar_label: 'interface'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/zerotier/interface
captured_at: '2026-11-01T21:26:15+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## zerotier/interface {#zerotierinterface}
**包：** zerotier
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">介面是否動態建立。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">專案是否已停用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面的短名稱。</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">ARP 超時值。</ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool">強制介面進入執行狀態。</ArgTableRow>
<ArgTableRow arg="network" typ="string" mandatory="1">16 位網路 ID。</ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">ZeroTier 例項名稱。</ArgTableRow>
<ArgTableRow arg="allow-managed" typ="bool">分配由 ZeroTier 管理的 IP 地址和路由。</ArgTableRow>
<ArgTableRow arg="allow-global" typ="bool">ZeroTier IP 地址和路由可以與公網 IP 空間重疊。</ArgTableRow>
<ArgTableRow arg="allow-default" typ="bool">網路可以覆蓋系統預設路由（強制 VPN 模式）。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr">ZeroTier 介面的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">介面的最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="bridge" typ="bool">介面是否充當網橋。</ArgTableRow>
<ArgTableRow arg="dhcp" typ="bool">介面上是否啟用 DHCP。</ArgTableRow>
<ArgTableRow arg="network-name" typ="string">來自控制器的可讀網路名稱。</ArgTableRow>
<ArgTableRow arg="status" typ="string">介面在網路上的當前狀態。</ArgTableRow>
<ArgTableRow arg="type" typ="string">網路介面的型別。</ArgTableRow>
</ArgTable>
