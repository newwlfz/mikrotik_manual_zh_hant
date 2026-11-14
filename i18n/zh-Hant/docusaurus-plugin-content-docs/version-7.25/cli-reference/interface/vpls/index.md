---
sidebar_key: "cli-reference/interface/vpls/index"
sidebar_position: 1
title: "vpls"
sidebar_label: 'vpls'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/vpls
captured_at: '2026-11-01T21:23:02+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/vpls {#interfacevpls}
**條件：** !smips
**型別：** 目錄

所有 VPLS 介面的列表。此選單還會顯示動態建立的基於 BGP 的 VPLS 介面。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="B" typ="bgp-signaled">bgp-signaled</ArgTableRow>
<ArgTableRow arg="C" typ="cisco-bgp-signaled">cisco-bgp-signaled</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面名稱。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">三層最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">介面的靜態 MAC 地址。未設定時自動生成。</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)">地址解析協定。</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">ARP 條目過期前的時間。設定為 `auto` 以使用介面型別的預設值。</ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool">指定是否檢測介面的執行狀態。如果設定為 `no`，介面將始終帶有 `running` 標誌。</ArgTableRow>
<ArgTableRow arg="peer" typ="address (flags=46v)" mandatory="1">遠端對等體的 IP 地址（RFC 4762 第 3.1 節）。</ArgTableRow>
<ArgTableRow arg="vpls-id" typ="address (flags=R)" unset="1">用於標識 VPLS 隧道的唯一編號。編碼為 2byte+4byte 或 4byte+2byte 數字（RFC 4762 第 3.2 節）。</ArgTableRow>
<ArgTableRow arg="cisco-static-id" typ="num" unset="1">Cisco 風格的 VPLS 隧道 ID（RFC 4447 FEC 型別 0x80）。</ArgTableRow>
<ArgTableRow arg="pw-type" typ="enum (tagged-ethernet | raw-ethernet | vpls)" unset="1">偽線型別（RFC 4447 第 5.2 節）。預設使用 `raw-ethernet`。</ArgTableRow>
<ArgTableRow arg="pw-l2mtu" typ="num" unset="1">向遠端對等體通告的 L2MTU 值（RFC 4447 第 5.2 節）。</ArgTableRow>
<ArgTableRow arg="pw-control-word" typ="enum (default | enabled | disabled)" unset="1">啟用或停用 Control Word 的使用（RFC 4623 第 4 節）。常規 VPLS 隧道與 Cisco 風格 VPLS 隧道的預設值不同。Cisco 風格預設停用 Control Word 的使用。請參閱 [控制字](../../../user-guides/routing-and-networking-protocols/mpls/vpls/control-word.md) 一文了解更多資訊。</ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1">VPLS 介面所屬的網橋。</ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1">網橋埠的開銷。</ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1">設定為 `none` 時，不使用網橋 `horizon`。</ArgTableRow>
<ArgTableRow arg="bridge-pvid" typ="num" unset="1">分配給動態橋接介面的埠 VLAN ID（pvid）。僅當網橋 `vlan-filtering` 設定為 `yes` 時適用。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="bgp-vpls" typ="enum">用於建立動態 VPLS 介面的 [BGP VPLS](../../routing/bgp/vpls.md) 例項名稱（RFC 4761 第 3.2 節）。</ArgTableRow>
<ArgTableRow arg="bgp-vpls-prfx" typ="string">用於建立動態 VPLS 介面的 [BGP VPLS](../../routing/bgp/vpls.md) 例項字首（RFC 4761 第 3.2 節）。</ArgTableRow>
</ArgTable>
