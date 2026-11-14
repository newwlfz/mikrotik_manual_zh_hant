---
sidebar_key: "cli-reference/interface/ethernet/switch/port-leakage"
sidebar_position: 16
title: "port-leakage"
sidebar_label: 'port-leakage'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/port-leakage
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/port-leakage {#interfaceethernetswitchport-leakage}
**系統能力：** musicswitch
**型別：** 目錄

埠洩漏允許繞過埠上的出站 VLAN 過濾。允許洩漏埠訪問其他埠，用於安全、網路控制和管理等各種應用。注意：當同一埠同時應用隔離和洩漏時，該埠被隔離。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ports" typ="multi { array-id }">隔離/洩漏的埠。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (src | dst) { src:0, dst:1 }">
隔離/洩漏條目的查詢型別：
- src - 條目應用於埠的入方向封包。
- dst - 條目應用於埠的出方向封包。
</ArgTableRow>
<ArgTableRow arg="forwarding-type" typ="ubit (bridged, routed)">匹配 Cloud Router Switch 上的流量轉發型別。</ArgTableRow>
<ArgTableRow arg="traffic-type" typ="ubit (unicast, multicast, broadcast)">匹配流量型別。</ArgTableRow>
<ArgTableRow arg="registration-status" typ="ubit (known, unknown)">匹配封包的註冊狀態。已知封包存在於 UFDB 和 MFDB 中，未知封包則不存在。</ArgTableRow>
<ArgTableRow arg="protocol-type" typ="ubit (arp, nd, dhcpv4, dhcpv6, ripv1)">用於隔離/洩漏的協定。</ArgTableRow>
<ArgTableRow arg="flow-id" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-profile" typ="enum (promiscuous | isolated | community1 | community2) { promiscuous:0, isolated:1, community1:2, community2:3 }">匹配 MAC 隔離/洩漏配置檔案。</ArgTableRow>
<ArgTableRow arg="port-profile" typ="num">匹配埠隔離/洩漏配置檔案。</ArgTableRow>
<ArgTableRow arg="vlan-profile" typ="enum (promiscuous | isolated | community1 | community2) { promiscuous:0, isolated:1, community1:2, community2:3 }">匹配 VLAN 隔離/洩漏配置檔案。</ArgTableRow>
</ArgTable>
