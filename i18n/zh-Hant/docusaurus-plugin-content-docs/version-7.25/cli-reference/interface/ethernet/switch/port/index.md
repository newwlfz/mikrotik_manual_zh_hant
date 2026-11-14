---
sidebar_key: "cli-reference/interface/ethernet/switch/port/index"
sidebar_position: 1
title: "port"
sidebar_label: 'port'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/port
captured_at: '2026-11-01T21:22:37+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/port {#interfaceethernetswitchport}
**系統能力：** musicswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ingress-customer-tpid-override" typ="num">入站客戶 TPID 覆蓋允許接收帶有自定義客戶標籤 TPID 的特定幀。預設值用於 802.1Q 幀的標籤。</ArgTableRow>
<ArgTableRow arg="egress-customer-tpid-override" typ="num">出站客戶 TPID 覆蓋允許對帶有客戶標籤的出站幀進行自定義標識。預設值用於 802.1Q 幀的標籤。</ArgTableRow>
<ArgTableRow arg="ingress-service-tpid-override" typ="num">入站服務 TPID 覆蓋允許接收帶有自定義服務標籤 TPID 的特定幀。預設值用於 802.1AD 幀的服務標籤。</ArgTableRow>
<ArgTableRow arg="egress-service-tpid-override" typ="num">出站服務 TPID 覆蓋允許對帶有服務標籤的出站幀進行自定義標識。預設值用於 802.1AD 幀的服務標籤。</ArgTableRow>
<ArgTableRow arg="drop-secure-static-mac-move" typ="bool">如果 MAC 已在另一個埠上學習到，則在 UFDB 超時之前阻止靜態條目的 MAC 重新學習。</ArgTableRow>
<ArgTableRow arg="drop-dynamic-mac-move" typ="bool">如果 MAC 已在另一個埠上學習到，則在 UFDB 超時之前阻止 MAC 重新學習。</ArgTableRow>
<ArgTableRow arg="learn-limit" typ="num">啟用或停用 MAC 地址學習，並設定埠上的 MAC 限制。預設情況下停用 MAC 學習限制。</ArgTableRow>
<ArgTableRow arg="allow-unicast-loopback" typ="bool">埠上的單播環回。啟用後，對於已知單播封包，當源埠和目標埠相同時，允許將其發回。</ArgTableRow>
<ArgTableRow arg="allow-multicast-loopback" typ="bool">埠上的組播環回。啟用後，對於已註冊的組播或廣播封包，當源埠和目標埠相同時，允許將其發回。</ArgTableRow>
<ArgTableRow arg="action-on-static-station-move" typ="enum (forward | redirect-to-cpu | copy-to-cpu | drop) { forward:0, redirect-to-cpu:1, copy-to-cpu:2, drop:3 }">當 UFDB 已包含具有此類 MAC 但埠不同的靜態條目時，對封包執行的動作。</ArgTableRow>
<ArgTableRow arg="drop-when-ufdb-entry-src-drop" typ="bool">啟用或停用當 UFDB 條目的動作為 src-drop 時丟棄封包。</ArgTableRow>
<ArgTableRow arg="isolation-leakage-profile-override" typ="num">
用於埠隔離/洩漏配置的自定義埠配置檔案。
- 埠級隔離配置檔案 0。上行埠 - 允許該埠與裝置中的所有埠通訊。
- 埠級隔離配置檔案 1。隔離埠 - 允許該埠僅與上行埠通訊。
- 埠級隔離配置檔案 2 - 31。團體埠 - 允許同一團體埠和上行埠之間通訊。
</ArgTableRow>
<ArgTableRow arg="vlan-type" typ="enum (edge-port | network-port) { edge-port:0, network-port:1 }">埠 VLAN 型別指定在 UFDB 學習中是否使用 VLAN ID。網路埠在 UFDB 中學習 VLAN ID，邊緣埠不學習 - VLAN 0。只能在 IVL 學習模式中觀察到。</ArgTableRow>
<ArgTableRow arg="allow-fdb-based-vlan-translate" typ="bool">啟用或停用埠上基於 MAC 的 VLAN 轉換。</ArgTableRow>
<ArgTableRow arg="allow-mac-based-service-vlan-assignment-for" typ="enum (none | untagged-and-priority-tagged-frame-only | tagged-frame-only | all) { none:0, untagged-and-priority-tagged-frame-only:1, tagged-frame-only:2, all:3 }">應用基於 MAC 的服務 VLAN 轉換的幀型別。</ArgTableRow>
<ArgTableRow arg="allow-mac-based-customer-vlan-assignment-for" typ="enum (none | untagged-and-priority-tagged-frame-only | tagged-frame-only | all) { none:0, untagged-and-priority-tagged-frame-only:1, tagged-frame-only:2, all:3 }">應用基於 MAC 的客戶 VLAN 轉換的幀型別。</ArgTableRow>
<ArgTableRow arg="filter-untagged-frame" typ="bool">是否在埠上過濾未標記幀。</ArgTableRow>
<ArgTableRow arg="filter-priority-tagged-frame" typ="bool">是否在埠上過濾帶優先順序的標記幀。</ArgTableRow>
<ArgTableRow arg="filter-tagged-frame" typ="bool">是否在埠上過濾標記幀。</ArgTableRow>
<ArgTableRow arg="egress-vlan-tag-table-lookup-key" typ="enum (egress-vid | according-to-bridge-type) { egress-vid:0, according-to-bridge-type:1 }">
出站 VLAN 表（VLAN 標記）查詢：
- `egress-vid` - 當配置為邊緣埠時，查詢 VLAN ID 為 `CVID`；當配置為網路埠時，為 `SVID`。
- `according-to-bridge-type` - 當配置為客戶 VLAN 網橋時，查詢 VLAN ID 為 `CVID`；當配置為服務 VLAN 網橋時，為 `SVID`。
</ArgTableRow>
<ArgTableRow arg="egress-vlan-mode" typ="enum (untagged | tagged | unmodified) { untagged:0, tagged:1, unmodified:2 }">埠上的出站 VLAN 標記動作。</ArgTableRow>
<ArgTableRow arg="ingress-mirror-to" typ="enum (none | mirror0 | mirror1) { none:0xffffffff, mirror0:0, mirror1:1 }">用於基於埠的入站映象的分析儀埠。</ArgTableRow>
<ArgTableRow arg="ingress-mirroring-according-to-vlan" typ="bool"></ArgTableRow>
<ArgTableRow arg="egress-mirror-to" typ="enum (none | mirror0 | mirror1) { none:0xffffffff, mirror0:0, mirror1:1 }">用於基於埠的出站映象的分析儀埠。</ArgTableRow>
<ArgTableRow arg="qos-scheme-precedence" typ="multi { array-id, qos-type: enum (pcp-based | vlan-based | protocol-based | da-based | sa-based | dscp-based | ingress-acl-based) { pcp-based:0, vlan-based:1, protocol-based:2, da-based:3, sa-based:4, dscp-based:5, ingress-acl-based:6 }
 }">指定在埠入站方向應用的 QoS 分配方案。</ArgTableRow>
<ArgTableRow arg="default-customer-pcp" typ="num">埠的預設客戶 PCP。</ArgTableRow>
<ArgTableRow arg="default-service-pcp" typ="num">埠的預設服務 PCP。</ArgTableRow>
<ArgTableRow arg="pcp-propagation-for-initial-pcp" typ="bool">
啟用或停用入站方向上初始 PCP 分配時的 PCP 傳播。
- 如果埠 `vlan-type` 為邊緣埠，則服務 PCP 從客戶 PCP 複製。
- 如果埠 `vlan-type` 為網路埠，則客戶 PCP 從服務 PCP 複製。
</ArgTableRow>
<ArgTableRow arg="egress-pcp-propagation" typ="bool">啟用或禁用出站 PCP 傳播。如果埠 `vlan-type` 為邊緣埠，則服務 PCP 從客戶 PCP 複製。如果埠 `vlan-type` 為網路埠，則客戶 PCP 從服務 PCP 複製。</ArgTableRow>
<ArgTableRow arg="dscp-based-qos-dscp-to-dscp-mapping" typ="bool">啟用或停用埠上的 DSCP 到內部 DSCP 對映。</ArgTableRow>
<ArgTableRow arg="pcp-or-dscp-based-qos-change-dei" typ="bool">啟用或停用埠上基於 PCP 或 DSCP 的 DEI 更改。</ArgTableRow>
<ArgTableRow arg="pcp-or-dscp-based-qos-change-pcp" typ="bool">啟用或停用埠上基於 PCP 或 DSCP 的 PCP 更改。</ArgTableRow>
<ArgTableRow arg="pcp-or-dscp-based-qos-change-dscp" typ="bool">啟用或停用埠上基於 PCP 或 DSCP 的 DSCP 更改。</ArgTableRow>
<ArgTableRow arg="pcp-based-qos-drop-precedence-mapping" typ="object { range-and-drop-precedence: composite { pcp-dei-range: range [ .. 15]
, drop-precedence: enum (green | yellow | red | drop)
 }
 }">PCP/DEI 到丟棄優先順序（drop | green | red | yellow）對映的新丟棄優先順序值。允許多個對映，以逗號分隔，例如 "0-7:yellow,8-15:red"。</ArgTableRow>
<ArgTableRow arg="pcp-based-qos-dscp-mapping" typ="object { range-and-dscp: composite { pcp-dei-range: range [ .. 15]
, dscp: num [ .. 63]
 }
 }">PCP/DEI 到 DSCP 對映的新 DSCP 值。允許多個對映，以逗號分隔，例如 "0-7:25,8-15:50"。</ArgTableRow>
<ArgTableRow arg="pcp-based-qos-dei-mapping" typ="object { range-and-dei: composite { pcp-dei-range: range [ .. 15]
, dei: num [ .. 1]
 }
 }">PCP/DEI 到 DEI 對映的新 DEI 值。允許多個對映，以逗號分隔，例如 "0-7:0,8-15:1"。</ArgTableRow>
<ArgTableRow arg="pcp-based-qos-pcp-mapping" typ="object { range-and-pcp: composite { pcp-dei-range: range [ .. 15]
, pcp: num [ .. 7]
 }
 }">PCP/DEI 到 PCP 對映的新 PCP 值。允許多個對映，以逗號分隔，例如 "0-7:3,8-15:4"。</ArgTableRow>
<ArgTableRow arg="pcp-based-qos-priority-mapping" typ="object { range-and-priority: composite { pcp-dei-range: range [ .. 15]
, priority: num [ .. 15]
 }
 }">PCP/DEI 到優先順序對映的新內部優先順序值。允許多個對映，以逗號分隔，例如 "0-7:5,8-15:15"。</ArgTableRow>
<ArgTableRow arg="priority-to-queue" typ="object { priority-range-and-queue: composite { priority-range: range [ .. 15]
, queue: num [ .. 7]
 }
 }">每個埠的內部優先順序（0..15）到佇列（0..7）的對映。</ArgTableRow>
<ArgTableRow arg="per-queue-scheduling" typ="object { scheduling-type-and-weight: composite { scheduling-type: enum (strict-priority | wrr-group0 | wrr-group1) { strict-priority:0, wrr-group0:1, wrr-group1:2 }
, weight: [ num [ .. 255]]
 }
 }">設定埠對每個佇列組使用嚴格優先順序或加權輪詢策略進行流量整形。</ArgTableRow>
<ArgTableRow arg="custom-drop-counter-includes" typ="ubit (device-loopback, fdb-hash-violation, exceeded-port-learn-limitation, dynamic-station-move, static-station-move, ufdb-source-drop, host-source-drop, unknown-host, ingress-vlan-filtered)">用於為交換器埠 custom-drop-packet 計數器統計丟棄封包的自定義包含項。</ArgTableRow>
<ArgTableRow arg="queue-custom-drop-counter0-includes" typ="ubit (red, yellow, green, queue0, queue1, queue2, queue3, queue4, queue5, queue6, queue7)">用於為交換器埠 tx-queue-custom0-drop-packet 和 tx-queue-custom0-drop-byte 計數器統計丟棄封包及位元組數的自定義包含項。</ArgTableRow>
<ArgTableRow arg="queue-custom-drop-counter1-includes" typ="ubit (red, yellow, green, queue0, queue1, queue2, queue3, queue4, queue5, queue6, queue7)">用於為交換器埠 tx-queue-custom1-drop-packet 和 tx-queue-custom1-drop-byte 計數器統計丟棄封包及位元組數的自定義包含項。</ArgTableRow>
<ArgTableRow arg="policy-drop-counter-includes" typ="ubit (ingress-policing, ingress-acl, egress-policing, egress-acl)">用於為交換器埠 policy-drop-packet 計數器統計丟棄封包的自定義包含項。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ingress-customer-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="egress-customer-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="ingress-service-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="egress-service-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="learn" typ="bool"></ArgTableRow>
<ArgTableRow arg="isolation-leakage-profile" typ="num"></ArgTableRow>
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

## interface/ethernet/switch/port {#interfaceethernetswitchport-1}
**系統能力：** rbswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="R" typ="running"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="vlan-mode" typ="enum (disabled | fallback | check | secure) { disabled:0, fallback:1, check:2, secure:3 }" syscap="oldswitch">更改入站流量針對 VLAN 表的 VLAN 查詢機制。`disabled` - 完全停用針對 VLAN 表的檢查，不丟棄任何流量。`fallback` - 針對 VLAN 表檢查標記流量，轉發所有未標記流量。`check` - 檢查標記流量，丟棄所有未標記流量。`secure` - 檢查標記流量，丟棄所有未標記流量，入站和出站埠都必須在 VLAN 表中找到，否則流量會被丟棄。</ArgTableRow>
<ArgTableRow arg="vlan-header" typ="enum (leave-as-is | always-strip | add-if-missing) { leave-as-is:0, always-strip:1, add-if-missing:2 }" syscap="oldswitch">設定埠對出站流量執行的動作。`add-if-missing` - 使用入站埠的 `default-vlan-id` 新增 VLAN 標籤，用於 trunk 埠。`always-strip` - 移除 VLAN 標籤，用於 access 埠。`leave-as-is` - 不新增也不移除 VLAN 標籤，用於 hybrid 埠。</ArgTableRow>
<ArgTableRow arg="default-vlan-id" typ="num" syscap="oldswitch">在埠上的所有未標記入站流量上新增具有指定 VLAN ID 的 VLAN 標籤。應與 `vlan-header=always-strip` 一起使用，以將埠配置為 access 埠。對於 hybrid 埠，`default-vlan-id` 用於為未標記流量新增標籤。如果兩個埠具有相同的 `default-vlan-id`，則不會新增 VLAN 標籤，因為交換器晶片假定流量正在 access 埠之間轉發。</ArgTableRow>
<ArgTableRow arg="mirror-ingress" typ="bool" syscap="switch-mirror-prestera">是否將入站封包副本傳送到 `mirror-target` 埠。</ArgTableRow>
<ArgTableRow arg="mirror-egress" typ="bool" syscap="switch-mirror-prestera">是否將出站封包副本傳送到 `mirror-target` 埠。</ArgTableRow>
<ArgTableRow arg="mirror-ingress-target" typ="enum (none) { none:0 }" syscap="switch-mv88e6xxx">選擇單個映象入站目標埠。來自 `mirror-ingress` 的映象封包將傳送到所選埠。</ArgTableRow>
<ArgTableRow arg="ingress-rate" typ="num" syscap="switch-rate">透過丟包限制接收（入站）流量。超過所定義限制的一切流量都會被丟棄。</ArgTableRow>
<ArgTableRow arg="egress-rate" typ="num" syscap="switch-rate">限制傳送（出站）流量。整形器會嘗試將超過限制的封包排隊，而不是將其丟棄。</ArgTableRow>
<ArgTableRow arg="storm-rate" typ="num" syscap="crs_prestera">將廣播、未知組播和/或未知單播流量限制為鏈路速度的百分比。</ArgTableRow>
<ArgTableRow arg="limit-unknown-unicasts" typ="bool" syscap="crs_prestera">限制交換器埠上的未知單播流量。</ArgTableRow>
<ArgTableRow arg="limit-unknown-multicasts" typ="bool" syscap="crs_prestera">限制交換器埠上的未知組播流量。</ArgTableRow>
<ArgTableRow arg="limit-broadcasts" typ="bool" syscap="crs_prestera">限制交換器埠上的廣播流量。</ArgTableRow>
<ArgTableRow arg="l3-hw-offloading" typ="bool" syscap="crs_prestera">三層硬體解除安裝。透過此埠進行硬體路由。設定為 `no` 時，僅停用進出此特定埠的硬體路由。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum"></ArgTableRow>
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
