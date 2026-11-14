---
sidebar_key: "cli-reference/interface/pppoe-client/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/pppoe-client/monitor
captured_at: '2026-11-01T21:22:57+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pppoe-client/monitor {#interfacepppoe-clientmonitor}
**型別：** 命令

該命令將顯示當前 PPPoE 狀態。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">
當前鏈路狀態。可用值有：
- dialing，
- verifying password...，
- connected，
- disconnected。
</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">連線時間，以天、小時、分鐘和秒顯示。</ArgTableRow>
<ArgTableRow arg="active-links" typ="num">繫結的 MLPPP 連線數量（如果未使用 MLPPP，則為 1）。</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">此連線所使用的加密和編碼方式（如果不對稱，則用 '/' 分隔）。</ArgTableRow>
<ArgTableRow arg="service-name" typ="string">所使用的服務名稱。</ArgTableRow>
<ArgTableRow arg="ac-name" typ="string">接入集中器的名稱。</ArgTableRow>
<ArgTableRow arg="ac-mac" typ="macAddr">用戶端所連線的接入集中器（AC）的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">鏈路的有效 MTU。</ArgTableRow>
<ArgTableRow arg="mru" typ="num">鏈路的有效 MRU。</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">分配給用戶端的 IP 地址。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr">分配給伺服器的遠端 IP 地址（即閘道器地址）。</ArgTableRow>
<ArgTableRow arg="local-ipv6-address" typ="ip6Addr">連線的本地 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="remote-ipv6-address" typ="ip6Addr">連線的遠端 IPv6 地址。</ArgTableRow>
</ArgTable>
