---
sidebar_key: "cli-reference/interface/ethernet/switch"
title: "switch"
sidebar_label: 'switch'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch {#interfaceethernetswitch}
**條件：** !smips
**系統能力：** musicswitch
**型別：** 設定目錄

CRS1xx 和 2xx 系列交換器的全域性引數。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">交換器的名稱。</ArgTableRow>
<ArgTableRow arg="bridge-type" typ="enum (customer-vid-used-as-lookup-vid | service-vid-used-as-lookup-vid) { customer-vid-used-as-lookup-vid:0, service-vid-used-as-lookup-vid:1 }">定義哪個 VLAN 標籤用作 Lookup-VID。Lookup-VID 用作所有基於 VLAN 的查詢的 VLAN 鍵。</ArgTableRow>
<ArgTableRow arg="drop-if-no-vlan-assignment-on-ports" typ="multi { array-id }">如果未應用基於 MAC、基於協定的 VLAN 分配或入向 VLAN 轉換，則丟棄幀的埠。</ArgTableRow>
<ArgTableRow arg="drop-if-invalid-or-src-port-not-member-of-vlan-on-ports" typ="multi { array-id, port: enum
 }">丟棄無效幀以及其他埠 VLAN ID 幀的埠。</ArgTableRow>
<ArgTableRow arg="unknown-vlan-lookup-mode" typ="enum (ivl | svl)">
具有無效 VLAN 的封包的查詢和學習模式。
 - `ivl` - 使用獨立 VLAN 學習，
 - `svl` - 使用共享 VLAN 學習。
</ArgTableRow>
<ArgTableRow arg="forward-unknown-vlan" typ="bool">是否允許轉發不屬於 VLAN 表的 VLAN。</ArgTableRow>
<ArgTableRow arg="use-svid-in-one2one-vlan-lookup" typ="bool">是否使用服務 VLAN ID 進行 1:1 VLAN 交換查詢。</ArgTableRow>
<ArgTableRow arg="use-cvid-in-one2one-vlan-lookup" typ="bool">是否使用客戶 VLAN ID 進行 1:1 VLAN 交換查詢。</ArgTableRow>
<ArgTableRow arg="mac-level-isolation" typ="bool">全域性啟用或停用 MAC 級別隔離。一旦啟用，交換器將從單播轉發表中檢查源和目標 MAC 地址條目及其 `isolation-profile`。預設情況下，交換器會學習 MAC 地址並將其放入 `promiscuous` 隔離配置檔案。建立靜態單播條目時可以使用其他隔離配置檔案。如果源或目標 MAC 地址位於 `promiscuous` 隔離配置檔案中，則轉發封包。如果源和目標 MAC 地址都位於相同的 `community1` 或 `community2` 隔離配置檔案中，則轉發封包。當源和目標 MAC 地址隔離配置檔案為 `isolated` 時，或者當源和目標 MAC 地址隔離配置檔案來自不同社群（例如源 MAC 地址為 `community1`，目標 MAC 地址為 `community2`）時，封包將被丟棄。當 MAC 級別隔離全域性停用時，隔離會被繞過。</ArgTableRow>
<ArgTableRow arg="multicast-lookup-mode" typ="enum (dst-mac-and-vid-always | dst-ip-and-vid-for-ipv4) { dst-mac-and-vid-always:0, dst-ip-and-vid-for-ipv4:1 }">
IPv4 組播橋接的查詢模式。
- `dst-mac-and-vid-always` - 對於所有封包型別，查詢鍵是目標 MAC 和 VLAN ID。
- `dst-ip-and-vid-for-ipv4` - 對於 IPv4 封包，查詢鍵是目標 IP 和 VLAN ID。
</ArgTableRow>
<ArgTableRow arg="override-existing-when-ufdb-full" typ="bool">當 UFDB 已滿時，啟用或停用覆蓋具有最低老化值的現有條目。</ArgTableRow>
<ArgTableRow arg="unicast-fdb-timeout" typ="time">單播 FDB 條目的超時時間。</ArgTableRow>
<ArgTableRow arg="ingress-mirror0" typ="composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff }
, trunk: enum
 }
, packet-format: [ enum (unmodified | analyzer-configured) { unmodified:0, analyzer-configured:1 }]
 }">
第一個入向映象分析器埠或 trunk 及映象格式。
 - `analyzer-configured` - 封包與發往目標的封包相同，VLAN 格式根據分析器埠的 VLAN 配置進行修改。
 - `unmodified` - 流量按原始傳入封包格式進行映象，不對其做任何更改，但邊緣埠中的服務 VLAN 標籤會被剝離。
</ArgTableRow>
<ArgTableRow arg="ingress-mirror1" typ="composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff }
, trunk: enum
 }
, packet-format: [ enum (unmodified | analyzer-configured) { unmodified:0, analyzer-configured:1 }]
 }">
第二個入向映象分析器埠或 trunk 及映象格式。
 - `analyzer-configured` - 封包與發往目標的封包相同，VLAN 格式根據分析器埠的 VLAN 配置進行修改。
 - `unmodified` - 流量按原始傳入封包格式進行映象，不對其做任何更改，但邊緣埠中的服務 VLAN 標籤會被剝離。
</ArgTableRow>
<ArgTableRow arg="ingress-mirror-ratio" typ="enum (1/1 | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 | 1/128 | 1/256 | 1/512 | 1/1024 | 1/2048 | 1/4096 | 1/8192 | 1/16384 | 1/32768)">入向映象封包占所有封包的比例。</ArgTableRow>
<ArgTableRow arg="egress-mirror0" typ="composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff }
, trunk: enum
 }
, packet-format: [ enum (modified | analyzer-configured | original) { modified:0, analyzer-configured:1, original:2 }]
 }">
第一個出向映象分析器埠或 trunk 及映象格式。
 - `analyzer-configured` - 封包與發往目標的封包相同，VLAN 格式根據分析器埠的 VLAN 配置進行修改。
 - `modified` - 封包與發往目標的封包相同，VLAN 格式根據出向埠的 VLAN 配置進行修改。
 - `original` - 流量按原始傳入封包格式進行映象，不對其做任何更改，但邊緣埠中的服務 VLAN 標籤會被剝離。
</ArgTableRow>
<ArgTableRow arg="egress-mirror1" typ="composite { port-or-trunk: alt { port: enum (none) { none:0xffffffff }
, trunk: enum
 }
, packet-format: [ enum (modified | analyzer-configured | original) { modified:0, analyzer-configured:1, original:2 }]
 }">
第二個出向映象分析器埠或 trunk 及映象格式。
 - `analyzer-configured` - 封包與發往目標的封包相同，VLAN 格式根據分析器埠的 VLAN 配置進行修改。
 - `modified` - 封包與發往目標的封包相同，VLAN 格式根據出向埠的 VLAN 配置進行修改。
 - `original` - 流量按原始傳入封包格式進行映象，不對其做任何更改，但邊緣埠中的服務 VLAN 標籤會被剝離。
</ArgTableRow>
<ArgTableRow arg="egress-mirror-ratio" typ="enum (1/1 | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 | 1/128 | 1/256 | 1/512 | 1/1024 | 1/2048 | 1/4096 | 1/8192 | 1/16384 | 1/32768)">出向映象封包占所有封包的比例。</ArgTableRow>
<ArgTableRow arg="fdb-uses" typ="enum (mirror0 | mirror1) { mirror0:0, mirror1:1 }">用於基於 FDB 的映象的分析器埠。</ArgTableRow>
<ArgTableRow arg="vlan-uses" typ="enum (mirror0 | mirror1) { mirror0:0, mirror1:1 }">用於基於 VLAN 的映象的分析器埠。</ArgTableRow>
<ArgTableRow arg="mirror-egress-if-ingress-mirrored" typ="bool">當封包同時應用入向和出向映象時，如果此設定被停用，則僅對該封包執行入向映象。如果啟用，則應用兩種映象型別。</ArgTableRow>
<ArgTableRow arg="mirror-tx-on-mirror-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="mirrored-packet-qos-priority" typ="num">映象封包中重標記的優先順序。</ArgTableRow>
<ArgTableRow arg="mirrored-packet-drop-precedence" typ="enum (green | yellow | red | drop)">映象封包中重標記的丟棄優先順序。此 QoS 屬性用於映象封包的入隊或丟棄。</ArgTableRow>
<ArgTableRow arg="bypass-vlan-ingress-filter-for" typ="ubit (eapol, ripv1, dhcpv4, dhcpv6, igmp, mld, arp, nd, pppoe-discovery)">從入向 VLAN 過濾中排除的協定。如果這些協定具有無效 VLAN，則不會被丟棄。（arp、dhcpv4、dhcpv6、eapol、igmp、mld、nd、pppoe-discovery、ripv1）。</ArgTableRow>
<ArgTableRow arg="bypass-ingress-port-policing-for" typ="ubit (eapol, ripv1, dhcpv4, dhcpv6, igmp, mld, arp, nd, pppoe-discovery)">從入向埠監管中排除的協定。（arp、dhcpv4、dhcpv6、eapol、igmp、mld、nd、pppoe-discovery、ripv1）。</ArgTableRow>
<ArgTableRow arg="bypass-l2-security-check-filter-for" typ="ubit (eapol, ripv1, dhcpv4, dhcpv6, igmp, mld, arp, nd, pppoe-discovery)">從策略規則安全檢查中排除的協定。（arp、dhcpv4、dhcpv6、eapol、igmp、mld、nd、pppoe-discovery、ripv1）。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="type" typ="enum (QCA-8513L | QCA-8519 | QCA-8511) { QCA-8513L:9, QCA-8519:11, QCA-8511:12 }"></ArgTableRow>
</ArgTable>

## interface/ethernet/switch {#interfaceethernetswitch-1}
**系統能力：** rbswitch
**型別：** 目錄

具有 Marwell Prestera 晶片的交換器的全域性引數。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mirror-source" typ="iface_enum { none:0 }" syscap="switch-mirror1">選擇單個映象源埠。入向和出向流量將被髮送到 `mirror-target` 埠。請注意，`mirror-target` 埠必須屬於同一交換器。</ArgTableRow>
<ArgTableRow arg="mirror-target" typ="iface_enum { none:0, cpu:0xffffffff }" syscap="switch-mirror-prestera">選擇單個映象目標埠。來自 [`mirror-egress`](./port/index.md#mirror-egress)、[`mirror-ingress`](./port/index.md#mirror-ingress) 和 [`mirror`](./rule/index.md#mirror) 的映象封包將被髮送到所選埠。</ArgTableRow>
<ArgTableRow arg="mirror-egress-target" typ="enum (none) { none:0 }" syscap="switch-mv88e6xxx">選擇單個映象出向目標埠。來自 `mirror-egress`（參見埠選單中的屬性）的映象封包將被髮送到所選埠。</ArgTableRow>
<ArgTableRow arg="rspan" typ="bool" syscap="switch-mirror-prestera">在 `mirror-target` 上啟用遠端交換器埠分析器（RSPAN）功能。標記為入向或出向映象的流量透過指定的遠端分析器 VLAN 傳輸 - `rspan-egress-vlan-id` 和 `rspan-ingress-vlan-id`。</ArgTableRow>
<ArgTableRow arg="rspan-ingress-vlan-id" typ="num" syscap="switch-mirror-prestera">選擇標記的入向流量的 VLAN ID。僅在啟用 `rspan` 時適用。</ArgTableRow>
<ArgTableRow arg="rspan-egress-vlan-id" typ="num" syscap="switch-mirror-prestera">選擇標記的出向流量的 VLAN ID。僅在啟用 `rspan` 時適用。</ArgTableRow>
<ArgTableRow arg="switch-all-ports" typ="bool">僅在 RB450G/RB435G/RB850Gx2 裝置上更改 ether1 交換器組。`yes` - ether1 屬於交換器，並支援所有高階功能，包括擴充套件統計資訊。`no` - ether1 不屬於交換器，實際上使其成為獨立乙太網埠，提高吞吐量但移除交換能力。</ArgTableRow>
<ArgTableRow arg="cpu-flow-control" typ="bool" syscap="switch-mv88e6xxx">停用或啟用 CPU 流控功能。交換器晶片透過在鏈路容量超出時傳送 Pause 幀來確保 CPU 埠不會擁塞。如果沒有此功能，對路由或管理至關重要的封包可能會被丟棄。</ArgTableRow>
<ArgTableRow arg="l3-hw-offloading" typ="bool" syscap="crs_prestera">三層硬體解除安裝。允許將路由功能解除安裝到交換器晶片以實現線速。</ArgTableRow>
<ArgTableRow arg="qos-hw-offloading" typ="bool" syscap="crs_prestera">服務質量（QoS）硬體解除安裝。允許為給定交換器晶片啟用 QoS（如果支援 QoS）。關閉此設定不會完全恢復到之前的功能。建議在停用後重啟裝置。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="type" typ="enum (ADMtek | IC-Plus-175C | IC-Plus-178C | IC-Plus-175D | Atheros-8316 | Atheros-7240 | Atheros-8227 | Atheros-8327 | Atheros-8236 | QCA-8513L | Atheros-8327N | QCA-8519 | QCA-8511 | QCA-8337 | MediaTek-MT7621 | Realtek-RTL8367 | Marvell-98DX3236 | Marvell-98DX8216 | Marvell-98DX8208 | Marvell-98DX8332 | Marvell-98DX8212 | Marvell-98DX3257 | IPQ-PPE | Marvell-98DX8525 | Marvell-98PX1012 | Marvell-98DX4310 | Marvell-98DX224S | Marvell-98DX226S | Marvell-88E6393X | Marvell-98DX3255 | Marvell-88E6191X | Marvell-98DX2528 | Marvell-98CX8410 | Marvell-88E6341 | MediaTek-MT7531 | Marvell-88E6190 | Marvell-98DX7335 | Marvell-98DX3510 | Marvell-98DX3550 | MediaTek-MT7531AE | Marvell-98DX1508M | IPQ-9570 | Marvell-98DX3530 | Marvell-98DX4550M | QCA-8386 | EN7523 | Marvell-98DX2521 | Marvell-98DX2556 | Marvell-98DX2588 | Marvell-98DX7335M) { ADMtek:0, IC-Plus-175C:1, IC-Plus-178C:2, IC-Plus-175D:3, Atheros-8316:4, Atheros-7240:5, Atheros-8227:6, Atheros-8327:7, Atheros-8236:8, QCA-8513L:9, Atheros-8327N:10, QCA-8519:11, QCA-8511:12, QCA-8337:13, MediaTek-MT7621:14, Realtek-RTL8367:15, Marvell-98DX3236:16, Marvell-98DX8216:17, Marvell-98DX8208:18, Marvell-98DX8332:19, Marvell-98DX8212:20, Marvell-98DX3257:21, IPQ-PPE:22, Marvell-98DX8525:23, Marvell-98PX1012:24, Marvell-98DX4310:25, Marvell-98DX224S:26, Marvell-98DX226S:27, Marvell-88E6393X:28, Marvell-98DX3255:29, Marvell-88E6191X:30, Marvell-98DX2528:31, Marvell-98CX8410:32, Marvell-88E6341:33, MediaTek-MT7531:34, Marvell-88E6190:35, Marvell-98DX7335:36, Marvell-98DX3510:37, Marvell-98DX3550:38, MediaTek-MT7531AE:39, Marvell-98DX1508M:40, IPQ-9570:41, Marvell-98DX3530:42, Marvell-98DX4550M:43, QCA-8386:44, EN7523:45, Marvell-98DX2521:46, Marvell-98DX2556:47, Marvell-98DX2588:48, Marvell-98DX7335M:49 }"></ArgTableRow>
<ArgTableRow arg="driver-rx-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-rx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-tx-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="driver-tx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-too-short" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-too-long" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-broadcast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-pause" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-multicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-fcs-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-align-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-fragment" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-overflow" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-control" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-unknown-op" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-length-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-code-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-carrier-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-jabber" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-drop" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-ip-header-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-tcp-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-udp-checksum-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-too-short" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-too-long" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-broadcast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-pause" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-multicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-underrun" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-excessive-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-multiple-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-single-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-excessive-deferred" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-deferred" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-late-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-total-collision" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-pause-honored" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-jabber" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-fcs-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-control" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-fragment" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-carrier-sense-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-64" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-65-127" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-128-255" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-256-511" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-512-1023" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1024-1518" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1519-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom0-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom0-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom1-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom1-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="policy-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="custom-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="current-learned" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="not-learned" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-unicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-unicast" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-error-events" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1024-max" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-codewords" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-corrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-uncorrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-symbol-error" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-rx-block" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-block-corrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-block-uncorrected" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue0-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue0-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-byte" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-packet" typ="multi { counter: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-byte" typ="multi { counter: num
 }"></ArgTableRow>
</ArgTable>
