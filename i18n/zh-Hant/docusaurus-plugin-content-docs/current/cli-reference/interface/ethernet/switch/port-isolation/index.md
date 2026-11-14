---
sidebar_key: "cli-reference/interface/ethernet/switch/port-isolation"
sidebar_position: 15
title: "port-isolation"
sidebar_label: 'port-isolation'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/port-isolation
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/port-isolation {#interfaceethernetswitchport-isolation}
**系統能力：** musicswitch
**型別：** 目錄

CRS 交換器支援靈活的多級隔離功能，可用於使用者訪問控制、流量工程以及高階安全和網路管理。隔離功能提供有組織的結構，使使用者可以輕鬆地按埠、MAC 地址、VLAN、協定、流和幀型別程式設計和控制訪問。支援以下隔離和洩漏功能：

- 埠級隔離
- MAC 級隔離
- VLAN 級隔離
- 協定級隔離
- 流級隔離
- 上述功能的自由組合

埠級隔離在源埠和目標埠上支援不同的控制方案。每個條目可以為源埠或目標埠程式設計訪問控制。

- 當條目配置為源埠訪問控制時，該條目會。

應用於入站封包。

- 當條目配置為目的地埠訪問控制時，該條目

應用於出站封包。

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
<ArgTableRow arg="flow-id" typ="num">隔離/洩漏條目的流 ID。</ArgTableRow>
<ArgTableRow arg="mac-profile" typ="enum (promiscuous | isolated | community1 | community2) { promiscuous:0, isolated:1, community1:2, community2:3 }">匹配 MAC 隔離/洩漏配置檔案。</ArgTableRow>
<ArgTableRow arg="port-profile" typ="num">匹配埠隔離/洩漏配置檔案。</ArgTableRow>
<ArgTableRow arg="vlan-profile" typ="enum (promiscuous | isolated | community1 | community2) { promiscuous:0, isolated:1, community1:2, community2:3 }">匹配 VLAN 隔離/洩漏配置檔案。</ArgTableRow>
</ArgTable>

## interface/ethernet/switch/port-isolation {#interfaceethernetswitchport-isolation-1}
**系統能力：** rbswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="forwarding-override" typ="multi { array-id, port: alt { port: enum
, interface-list: enum
 }
 }">入站流量被轉發到的交換器埠。交換器埠名稱和介面列表可以組合使用，所有指定介面列表中的埠都會新增到顯式列出的埠中。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">交換器埠名稱。</ArgTableRow>
<ArgTableRow arg="switch" typ="enum">埠所屬的交換器組。</ArgTableRow>
<ArgTableRow arg="current-forwarding-override" typ="multi { array-id, port: enum
 }">配置的 `forwarding-override` 所解析到的交換器埠。</ArgTableRow>
</ArgTable>
