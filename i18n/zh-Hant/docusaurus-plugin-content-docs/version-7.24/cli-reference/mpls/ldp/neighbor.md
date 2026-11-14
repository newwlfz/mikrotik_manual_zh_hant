---
sidebar_key: "cli-reference/mpls/ldp/neighbor"
sidebar_position: 5
title: "neighbor"
sidebar_label: "neighbor"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/mpls/ldp/neighbor
captured_at: '2026-11-01T21:29:15+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## mpls/ldp/neighbor {#mplsldpneighbor}
**條件：** !smips
**型別：** 目錄

已發現和靜態配置的 LDP 鄰居列表。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="O" typ="operational">指示對端是否處於執行狀態。</ArgTableRow>
<ArgTableRow arg="C" typ="active-connect">指示已選擇主動角色，並且路由器正在嘗試建立會話。</ArgTableRow>
<ArgTableRow arg="W" typ="passive-wait">指示對端是否處於被動角色，並且當前正在等待會話初始化。</ArgTableRow>
<ArgTableRow arg="T" typ="throttled">指示會話是否處於節流狀態。初始化失敗後會話會被節流，最大節流時間為 120s。</ArgTableRow>
<ArgTableRow arg="t" typ="sending-targeted-hello">是否正在向鄰居傳送定向 hello。</ArgTableRow>
<ArgTableRow arg="v" typ="vpls">鄰居是否用於 LDP 信令的 VPLS 隧道。</ArgTableRow>
<ArgTableRow arg="p" typ="passive">指示對端是否處於被動角色。</ArgTableRow>
<ArgTableRow arg="d" typ="on-demand">Downstream On Demand 標籤分發。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="transport" typ="address (flags=46vi)" mandatory="1">遠端傳輸地址。</ArgTableRow>
<ArgTableRow arg="send-targeted" typ="bool" unset="1">指定是否嘗試傳送定向 hello，用於定向（非直連）LDP 會話。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="peer" typ="object { peer-id: composite { id: ipAddr
, namespace: num
 }
 }">鄰居的 LSR-ID 和標籤空間。</ArgTableRow>
<ArgTableRow arg="local-transport" typ="address (flags=46)">選定的本地傳輸地址。</ArgTableRow>
<ArgTableRow arg="addresses" typ="multi { array-id, address: address (flags=46)
 }">鄰居上發現的地址列表。</ArgTableRow>
<ArgTableRow arg="path-vector-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="on-demand" typ="bool">Downstream On Demand 標籤分發。</ArgTableRow>
<ArgTableRow arg="used-afi" typ="ubit (ip, ipv6)">使用的傳輸 AFI。</ArgTableRow>
</ArgTable>
