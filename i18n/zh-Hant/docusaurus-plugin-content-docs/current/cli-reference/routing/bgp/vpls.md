---
sidebar_key: "cli-reference/routing/bgp/vpls"
sidebar_position: 7
title: "vpls"
sidebar_label: 'vpls'
source: https://manual.mikrotik.com/docs/cli-reference/routing/bgp/vpls
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bgp/vpls {#routingbgpvpls}
**條件：** !smips
**型別：** 目錄

此選單列出所有已配置的基於 BGP 的 VPLS 例項。這些例項允許路由器通告 VPLS BGP NLRI，並表明該路由器屬於特定的客戶 VPLS 網路。

基於 MP-BGP 的自動發現與信令（RFC 4761）。

Cisco VPLS 基於 BGP 的自動發現（draft-ietf-l2vpn-signaling-08）。

支援基於 BGP 的 VPLS 使用多個匯入/匯出的 route target 擴展團體（同時支援 RFC 4761 和 draft-ietf-l2vpn-signaling-08）。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="rd" typ="address (flags=R)" unset="1">指定附加到 VPLS NLRI 上的值，以便接收路由器能夠區分那些原本可能看起來相同的通告。這意味著必須為每個 VPLS 使用唯一的 route-distinguisher。不必為組成同一 VPLS 的所有路由器上的某個 VPLS 使用相同的 route distinguisher，因為 distinguisher 並不用於判斷某個 BGP NLRI 是否與特定 VPLS 相關（此用途由 Route Target 屬性完成），但必須為不同的 VPLS 使用不同的 distinguisher。接受 3 種格式。[閱讀更多>>](../../../user-guides/routing-and-networking-protocols/route-distinguisher-and-route-target.md)</ArgTableRow>
<ArgTableRow arg="site-id" typ="num" unset="1">唯一的站點識別符號。每個站點必須具有唯一的 site-id。若使用&nbsp;RFC 4761 風格的 VPLS 信令，則必須設定該引數。</ArgTableRow>
<ArgTableRow arg="cisco-id" typ="address" unset="1">唯一識別符號。若使用 Cisco 風格的 VPLS 信令，則必須設定該引數。在大多數情況下不應使用它，因為任何現代軟體都支援 RFC 4761 風格的信令（參見 site-id 引數）。該引數是 l2-router-id 與 RD 的合併，例如：10.155.155.1&amp;6550:123</ArgTableRow>
<ArgTableRow arg="import-route-targets" typ="multi { array-id, rt: address (flags=R)
 }" unset="1">該設定用於透過比較從 BGP NLRI 接收到的 route target 來判斷某個 BGP NLRI 是否與特定 VPLS 相關。</ArgTableRow>
<ArgTableRow arg="export-route-targets" typ="multi { array-id, rt: address (flags=R)
 }" unset="1">該設定用於為一個或多個 BGP NLRI 標記一個或多個 route target，在遠端由 `import-route-targets` 使用。</ArgTableRow>
<ArgTableRow arg="local-pref" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="pw-type" typ="enum (tagged-ethernet | raw-ethernet | vpls)" unset="1">偽線型別（RFC 4447 第 5.2 節）。預設使用 `raw-ethernet`。</ArgTableRow>
<ArgTableRow arg="pw-l2mtu" typ="num" unset="1">向遠端對等體通告的 L2MTU 值（RFC 4447 第 5.2 節）。</ArgTableRow>
<ArgTableRow arg="pw-control-word" typ="enum (default | enabled | disabled)" unset="1">啟用或停用 Control Word 的使用（RFC 4623 第 4 節）。常規 VPLS 隧道與 Cisco 風格 VPLS 隧道的預設值不同。Cisco 風格預設停用 Control Word 的使用。請參閱 [控制字](../../../user-guides/routing-and-networking-protocols/mpls/vpls/control-word.md) 一文了解更多資訊。</ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1">該 VPLS 介面所屬的網橋。</ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1">網橋埠的開銷。</ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1">設定為 `none` 時，不使用網橋 `horizon`。</ArgTableRow>
<ArgTableRow arg="bridge-pvid" typ="num" unset="1">分配給動態加入網橋的介面的埠 VLAN ID（pvid）。僅在網橋的 `vlan-filtering` 設定為 `yes` 時生效。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="current-peers" typ="string"></ArgTableRow>
</ArgTable>
