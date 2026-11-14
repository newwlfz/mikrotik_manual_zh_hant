---
sidebar_key: "cli-reference/ip/ipsec/active-peers/index"
sidebar_position: 1
title: "active-peers"
sidebar_label: 'active-peers'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/ipsec/active-peers
captured_at: '2026-11-01T21:24:07+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/active-peers {#ipipsecactive-peers}
**型別：** 目錄

此選單提供有關當前已建立 Phase 1 連線的遠端對等體的各種統計資訊。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="R" typ="responder">該對端是否為響應方。</ArgTableRow>
<ArgTableRow arg="N" typ="natt-peer">該對端是否使用 NAT 穿透。</ArgTableRow>
<ArgTableRow arg="P" typ="ppk">是否使用後量子預共享金鑰。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="id" typ="string">對端識別符號。</ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">本地 IP 地址。</ArgTableRow>
<ArgTableRow arg="port" typ="num">遠端埠。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">遠端 IP 地址。</ArgTableRow>
<ArgTableRow arg="state" typ="enum (spawning | starting | message-1-received | message-1-sent | message-2-received | message-2-sent | message-3-received | message-3-sent | message-4-received | established | expired | no-phase1 | eap | crypto | qkd) { spawning:0, starting:1, message-1-received:2, message-1-sent:3, message-2-received:4, message-2-sent:5, message-3-received:6, message-3-sent:7, message-4-received:8, established:9, expired:10, no-phase1:11 }">當前 IKE 第 1 階段狀態。</ArgTableRow>
<ArgTableRow arg="side" typ="enum (initiator | responder)">該對端是否充當響應方。</ArgTableRow>
<ArgTableRow arg="dynamic-address" typ="alt { ip: ipAddr
 }">動態分配的地址。</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">連線執行時間。</ArgTableRow>
<ArgTableRow arg="last-seen" typ="time">自上次收到封包以來的時間。</ArgTableRow>
<ArgTableRow arg="ph2-total" typ="num">第 2 階段交換的總數。</ArgTableRow>
<ArgTableRow arg="spii" typ="string">發起方 SPI 值。</ArgTableRow>
<ArgTableRow arg="spir" typ="string">響應方 SPI 值。</ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num">接收的封包數量。</ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num">接收的位元組數。</ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num">傳送的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num">傳送的位元組數。</ArgTableRow>
</ArgTable>
