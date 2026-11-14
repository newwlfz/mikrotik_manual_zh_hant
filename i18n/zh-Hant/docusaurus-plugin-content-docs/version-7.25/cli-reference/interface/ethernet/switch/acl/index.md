---
sidebar_key: "cli-reference/interface/ethernet/switch/acl/index"
sidebar_position: 1
title: "acl"
sidebar_label: 'acl'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/switch/acl
captured_at: '2026-11-01T21:22:33+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/acl {#interfaceethernetswitchacl}
**系統能力：** musicswitch
**型別：** 目錄

訪問控制列表由入站策略和出站策略引擎組成，最多允許配置 128 條策略規則（受 RouterOS 限制）。它是一種高階工具，可基於二層、三層和四層協定頭欄位條件進行線速封包過濾、轉發、整形和修改。

:::note
由於硬體限制，無法在特定埠上匹配廣播/組播流量。應使用埠隔離、在入方向埠上丟棄流量，或使用 VLAN 過濾來阻止某些廣播/組播流量被轉發。
:::

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="table" typ="enum (ingress | egress) { ingress:0, egress:1 }">選擇用於入站或出站封包的策略表。</ArgTableRow>
<ArgTableRow arg="invert-match" typ="bool">反轉整個 ACL 規則的匹配結果。</ArgTableRow>
<ArgTableRow arg="src-ports" typ="multi { array-id }">匹配物理源埠或 trunk。</ArgTableRow>
<ArgTableRow arg="dst-ports" typ="multi { array-id }">匹配物理目標埠或 trunk。由於硬體限制，無法在出站埠上匹配廣播/組播流量。</ArgTableRow>
<ArgTableRow arg="service-vid" typ="super { !
, service-vid: range [ .. 4095]
 }">匹配服務 VLAN ID。</ArgTableRow>
<ArgTableRow arg="service-pcp" typ="num">匹配服務 PCP。</ArgTableRow>
<ArgTableRow arg="service-dei" typ="num">匹配服務 DEI。</ArgTableRow>
<ArgTableRow arg="customer-vid" typ="super { !
, customer-vid: range [ .. 4095]
 }">匹配客戶 VLAN ID。</ArgTableRow>
<ArgTableRow arg="customer-pcp" typ="num">匹配客戶 PCP。</ArgTableRow>
<ArgTableRow arg="customer-dei" typ="num">匹配客戶 DEI。</ArgTableRow>
<ArgTableRow arg="src-l3-port" typ="super { !
, src-l3-port: range [ .. 65535]
 }">匹配 Layer3 源埠。</ArgTableRow>
<ArgTableRow arg="dst-l3-port" typ="super { !
, dst-l3-port: range [ .. 65535]
 }">匹配 Layer3 目標埠。</ArgTableRow>
<ArgTableRow arg="custom-fields" typ="object { custom-field: super { !
, custom-field: super { base: enum (start-of-frame | end-of-l2-header | end-of-l3-header) { start-of-frame:0, end-of-l2-header:1, end-of-l3-header:2 }
, [offset] :num [ .. 127]
, [range] :range [ .. 65535]
, [mask] [ /num [ .. 65535]]
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="priority" typ="num">匹配內部優先順序。僅在 egress 表中有效。</ArgTableRow>
<ArgTableRow arg="drop-precedence" typ="enum (green | yellow | red | drop)">匹配內部丟棄優先順序。僅在 egress 表中有效。</ArgTableRow>
<ArgTableRow arg="dst-addr-registered" typ="bool">定義是否匹配具有已註冊狀態的封包——即目標 MAC 地址位於 UFDB/MFDB/RFDB 中的封包。僅在 egress 表中有效。</ArgTableRow>
<ArgTableRow arg="service-tag" typ="enum (untagged | priority-tagged | tagged | tagged-or-priority-tagged) { untagged:0, priority-tagged:1, tagged:2, tagged-or-priority-tagged:3 }">服務標籤的格式。</ArgTableRow>
<ArgTableRow arg="customer-tag" typ="enum (untagged | priority-tagged | tagged | tagged-or-priority-tagged) { untagged:0, priority-tagged:1, tagged:2, tagged-or-priority-tagged:3 }">客戶標籤的格式。</ArgTableRow>
<ArgTableRow arg="mac-src-address" typ="super { address: macAddr
, [mask] [ /macAddr]
 }">源 MAC 地址和掩碼。</ArgTableRow>
<ArgTableRow arg="mac-dst-address" typ="super { address: macAddr
, [mask] [ /macAddr]
 }">目標 MAC 地址和掩碼。</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="alt { protocol-name: enum (ip-or-ipv6 | non-ip) { ip-or-ipv6:0x10000, non-ip:0x10001 }
, protocol-number: num [ .. 65535]
 }">
乙太網載荷型別（MAC 層協定）。
- `802.2` - 802.2 幀（0x0004）
- `arp` - Address Resolution Protocol（0x0806）
- `capsman` - CAPsMAN 到 CAP 的 MAC 層連線（0x88BB）
- `dot1x` - EAPoL IEEE 802.1X（0x888E）
- `homeplug-av` - HomePlug AV MME（0x88E1）
- `ip` - Internet Protocol version 4（0x0800）
- `ip-or-ipv6` - IPv4 或 IPv6（0x0800 或 0x86DD）
- `ipv6` - Internet Protocol Version 6（0x86DD）
- `ipx` - Internetwork Packet Exchange（0x8137）
- `lacp` - Link Aggregation Control Protocol（0x8809）
- `lldp` - Link Layer Discovery Protocol（0x88CC）
- `loop-protect` - Loop Protect Protocol（0x9003）
- `macsec` - MAC security IEEE 802.1AE（0x88E5）
- `mpls-multicast` - MPLS 組播（0x8848）
- `mpls-unicast` - MPLS 單播（0x8847）
- `mvrp` - Multiple VLAN Registration protocol（0x88F5）
- `non-ip` - 非 Internet Protocol version 4（不是 0x0800）
- `packing-compr` - 使用壓縮 [IP packing](../../../../ip/packing.md) 的封裝封包（0x9001）
- `packing-simple` - 使用簡單 [IP packing](../../../../ip/packing.md) 的封裝封包（0x9000）
- `pppoe` - PPPoE 會話階段（0x8864）
- `pppoe-discovery` - PPPoE 發現階段（0x8863）
- `rarp` - Reverse Address Resolution Protocol（0x8035）
- `romon` - Router Management Overlay Network [RoMON](../../../../../management-tools/romon.md)（0x88BF）
- `service-vlan` - Provider Bridging IEEE 802.1ad 和 Shortest Path Bridging IEEE 802.1aq（0x88A8）
- `vlan` - 帶 VLAN 標記的幀 IEEE 802.1Q 和具有 NNI 相容性的 Shortest Path Bridging IEEE 802.1aq（0x8100）
</ArgTableRow>
<ArgTableRow arg="lookup-vid" typ="num">用於查詢的 VLAN ID。它可以在到達 egress 表之前被更改。</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (tcp | udp | udp-lite | other) { tcp:0, udp:1, udp-lite:2, other:3 }">IP 協定型別。</ArgTableRow>
<ArgTableRow arg="fragmented" typ="bool">是否匹配分片封包。</ArgTableRow>
<ArgTableRow arg="first-fragment" typ="bool">YES 匹配未分片的封包和首片，NO 匹配其他分片。</ArgTableRow>
<ArgTableRow arg="ttl" typ="enum (0 | 1 | max | other) { 0:0, 1:1, max:2, other:3 }">匹配封包的 TTL 欄位。</ArgTableRow>
<ArgTableRow arg="ip-dst" typ="composite { address: ipAddr
, netmask: [ num [ .. 32]]
 }">匹配目標 IPv4 地址。</ArgTableRow>
<ArgTableRow arg="ip-src" typ="composite { address: ipAddr
, netmask: [ num [ .. 32]]
 }">匹配源 IPv4 地址。</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">匹配封包的 DSCP 欄位。</ArgTableRow>
<ArgTableRow arg="ecn" typ="num">匹配封包的 ECN 欄位。</ArgTableRow>
<ArgTableRow arg="ipv6-dst" typ="ip6Prefix">匹配目標 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="ipv6-src" typ="ip6Prefix">匹配源 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="mac-isolation-profile" typ="enum (promiscuous | isolated | community1 | community2) { promiscuous:0, isolated:1, community1:2, community2:3 }">根據 UFDB 匹配隔離配置檔案。僅在 egress 策略表中有效。</ArgTableRow>
<ArgTableRow arg="src-mac-addr-state" typ="enum (sa-found | sa-not-found | dynamic-station-move | static-station-move) { sa-found:0, sa-not-found:1, dynamic-station-move:2, static-station-move:3 }">定義是否匹配具有已註冊狀態的封包——即目標 MAC 地址位於 UFDB/MFDB/RFDB 中的封包。僅在 egress 策略表中有效。</ArgTableRow>
<ArgTableRow arg="flow-id" typ="num"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (forward | redirect-to-cpu | copy-to-cpu | send-to-new-dst-ports | drop) { forward:0, redirect-to-cpu:1, copy-to-cpu:2, send-to-new-dst-ports:3, drop:7 }">
對匹配 ACL 的封包執行的動作。
- `copy-to-cpu` - 封包被複制到 CPU。
- `drop` - 封包被丟棄。
- `forward` - 封包被轉發。
- `redirect-to-cpu` - 封包被重定向到 CPU。
- `send-to-new-dst-ports` - 封包被髮送到新的目標埠。
</ArgTableRow>
<ArgTableRow arg="new-dst-ports" typ="multi { array-id }">如果動作為 `send-to-new-dst-ports`，則此屬性設定哪些埠/trunk 作為新的目標。</ArgTableRow>
<ArgTableRow arg="new-flow-id" typ="num"></ArgTableRow>
<ArgTableRow arg="attack-filter-bypass" typ="bool"></ArgTableRow>
<ArgTableRow arg="ingress-vlan-filter-bypass" typ="bool">允許匹配的封包繞過 VLAN 表中的入站 VLAN 過濾。這僅適用於 ingress 策略表。</ArgTableRow>
<ArgTableRow arg="egress-vlan-filter-bypass" typ="bool">允許匹配的封包繞過 VLAN 表中的出站 VLAN 過濾。這僅適用於 ingress 策略表。</ArgTableRow>
<ArgTableRow arg="isolation-filter-bypass" typ="bool">允許匹配的封包繞過 Isolation 表。這僅適用於 ingress 策略表。</ArgTableRow>
<ArgTableRow arg="new-registered-state" typ="bool">是否修改封包狀態。YES 將封包狀態設定為 registered，NO 設定為 unregistered。僅在 ingress 策略表中有效。</ArgTableRow>
<ArgTableRow arg="src-mac-learn" typ="bool">是否學習匹配 ACL 的封包的源 MAC。僅在 ingress 策略表中有效。</ArgTableRow>
<ArgTableRow arg="mirror-to" typ="enum (mirror0 | mirror1) { mirror0:0, mirror1:1 }">ACL 封包的映象目標。</ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="num">ACL 封包的新的服務 VLAN ID。</ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="num">ACL 封包的新的客戶 VLAN ID。如果設定為 4095，則流量會被丟棄。</ArgTableRow>
<ArgTableRow arg="egress-vlan-translate-bypass" typ="bool">允許匹配的封包繞過出站 VLAN 轉換表。</ArgTableRow>
<ArgTableRow arg="new-service-pcp" typ="num">ACL 封包的新的服務 PCP。</ArgTableRow>
<ArgTableRow arg="new-service-dei" typ="num">ACL 封包的新的服務 DEI。</ArgTableRow>
<ArgTableRow arg="new-customer-pcp" typ="num">ACL 封包的新的客戶 PCP。</ArgTableRow>
<ArgTableRow arg="new-customer-dei" typ="num">ACL 封包的新的客戶 DEI。</ArgTableRow>
<ArgTableRow arg="new-dscp" typ="num">ACL 封包的新的 DSCP。</ArgTableRow>
<ArgTableRow arg="new-priority" typ="num">ACL 封包的新的內部優先順序。</ArgTableRow>
<ArgTableRow arg="new-drop-precedence" typ="enum (green | yellow | red | drop)">ACL 封包的新的內部丟棄優先順序。</ArgTableRow>
<ArgTableRow arg="policer" typ="enum">應用於 ACL 封包的 ACL Policer。</ArgTableRow>
</ArgTable>
