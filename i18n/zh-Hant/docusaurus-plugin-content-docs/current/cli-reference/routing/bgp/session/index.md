---
sidebar_key: "cli-reference/routing/bgp/session"
title: "session"
sidebar_label: 'session'
source: https://manual.mikrotik.com/docs/cli-reference/routing/bgp/session
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/bgp/session {#routingbgpsession}
**條件：** !smips
**型別：** 目錄

已建立、尚未連線或已斷開的 BGP 會話列表。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="E" typ="established">established</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="remote.address" typ="address (flags=46iv+:)"></ArgTableRow>
<ArgTableRow arg="remote.port" typ="num"></ArgTableRow>
<ArgTableRow arg="remote.as" typ="super { as: as
, [sub-as] [ /as]
 }"></ArgTableRow>
<ArgTableRow arg="remote.id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="remote.refused-cap-opt" typ="bool"></ArgTableRow>
<ArgTableRow arg="remote.capabilities" typ="ubit (mp, rr, orf, enhe, em, sec, ml, role, gr, as4, dyn, ms, ap, err, llgr, fqdn)">遠端對等體通告/支援的能力。</ArgTableRow>
<ArgTableRow arg="remote.afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)">遠端對等體通告/支援的地址族。</ArgTableRow>
<ArgTableRow arg="remote.hold-time" typ="alt { special: enum (infinity) { infinity:0 }
, number: time [3 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="remote.messages" typ="num">從遠端對等體接收的 BGP 訊息數。</ArgTableRow>
<ArgTableRow arg="remote.bytes" typ="num">從遠端對等體接收的總位元組數。</ArgTableRow>
<ArgTableRow arg="remote.gr-restart" typ="bool"></ArgTableRow>
<ArgTableRow arg="remote.gr-time" typ="num"></ArgTableRow>
<ArgTableRow arg="remote.gr-afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6)"></ArgTableRow>
<ArgTableRow arg="remote.gr-afi-fwp" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6)"></ArgTableRow>
<ArgTableRow arg="remote.eor" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)">從遠端對等體收到 end-of-rib 的地址族列表。</ArgTableRow>
<ArgTableRow arg="remote.role" typ="enum (provider | route-server | route-server-client | customer | peer)">從遠端對等體接收的角色。請參閱[路由洩漏防護](../../../../user-guides/routing-and-networking-protocols/unicast/bgp/route-leak-prevention.md)。</ArgTableRow>
<ArgTableRow arg="local.role" typ="enum (ibgp | ibgp-rr | ebgp | ebgp-provider | ebgp-rs | ebgp-rs-client | ebgp-customer | ebgp-peer)">本地配置的角色。請參閱[路由洩漏防護](../../../../user-guides/routing-and-networking-protocols/unicast/bgp/route-leak-prevention.md)。</ArgTableRow>
<ArgTableRow arg="local.address" typ="address (flags=46iv:)"></ArgTableRow>
<ArgTableRow arg="local.port" typ="num"></ArgTableRow>
<ArgTableRow arg="local.as" typ="super { as: as
, [sub-as] [ /as]
 }"></ArgTableRow>
<ArgTableRow arg="local.id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="local.cluster-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="local.capabilities" typ="ubit (mp, rr, enhe, role, gr, as4, ap)"></ArgTableRow>
<ArgTableRow arg="local.afi" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4, vpnv6, evpn)"></ArgTableRow>
<ArgTableRow arg="local.messages" typ="num"></ArgTableRow>
<ArgTableRow arg="local.bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="local.eor" typ="ubit (ip, ipv6, l2vpn, l2vpn-cisco, vpnv4)"></ArgTableRow>
<ArgTableRow arg="output.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf | input)"></ArgTableRow>
<ArgTableRow arg="output.procid" typ="num"></ArgTableRow>
<ArgTableRow arg="output.filter-select" typ="enum"></ArgTableRow>
<ArgTableRow arg="output.filter-chain" typ="enum"></ArgTableRow>
<ArgTableRow arg="output.network" typ="enum"></ArgTableRow>
<ArgTableRow arg="output.add-path" typ="ubit (ip, ipv6)"></ArgTableRow>
<ArgTableRow arg="output.remove-private-as" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.default-originate" typ="enum (never | if-installed | always)"></ArgTableRow>
<ArgTableRow arg="output.default-prepend" typ="num"></ArgTableRow>
<ArgTableRow arg="output.no-client-to-client-reflection" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.no-early-cut" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.keep-sent-attributes" typ="bool"></ArgTableRow>
<ArgTableRow arg="output.last-notification" typ="string">最後傳送的通知訊息內容。</ArgTableRow>
<ArgTableRow arg="input.affinity" typ="enum (main | alone | remote-as | instance | afi | vrf)"></ArgTableRow>
<ArgTableRow arg="input.procid" typ="num">顯示該會話繫結到哪個路由程式。</ArgTableRow>
<ArgTableRow arg="input.filter" typ="enum"></ArgTableRow>
<ArgTableRow arg="input.allow-as" typ="num"></ArgTableRow>
<ArgTableRow arg="input.as-override" typ="bool"></ArgTableRow>
<ArgTableRow arg="input.ignore-as-path-len" typ="bool"></ArgTableRow>
<ArgTableRow arg="input.limit-process-routes" typ="num"></ArgTableRow>
<ArgTableRow arg="input.add-path" typ="ubit (ip, ipv6)"></ArgTableRow>
<ArgTableRow arg="input.last-notification" typ="string">最後接收的通知訊息內容。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="ibgp" typ="switch">指示該會話是否為 iBGP。</ArgTableRow>
<ArgTableRow arg="ebgp" typ="switch">指示該會話是否為 eBGP。</ArgTableRow>
<ArgTableRow arg="limit-exceeded" typ="switch">指示接收到的字首數是否超過由 `input.limit-process-routes-ipv4` 和/或 `input.limit-process-routes-ipv6` 配置的字首限制。</ArgTableRow>
<ArgTableRow arg="stopped" typ="switch">指示會話是否被管理性停止。</ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum"></ArgTableRow>
<ArgTableRow arg="nexthop-choice" typ="enum (default | force-self | propagate)"></ArgTableRow>
<ArgTableRow arg="cisco-vpls-nlri-len-fmt" typ="enum (auto-bits | auto-bytes | bits | bytes)"></ArgTableRow>
<ArgTableRow arg="multihop" typ="bool"></ArgTableRow>
<ArgTableRow arg="hold-time" typ="alt { special: enum (infinity) { infinity:0 }
, number: time [3 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="keepalive-time" typ="time"></ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time">已建立會話的持續時間。</ArgTableRow>
<ArgTableRow arg="last-started" typ="date"></ArgTableRow>
<ArgTableRow arg="last-stopped" typ="date"></ArgTableRow>
<ArgTableRow arg="save-to" typ="string"></ArgTableRow>
<ArgTableRow arg="prefix-count" typ="num"></ArgTableRow>
<ArgTableRow arg="keepalive-timer" typ="time"></ArgTableRow>
<ArgTableRow arg="restart-timer" typ="time"></ArgTableRow>
</ArgTable>
