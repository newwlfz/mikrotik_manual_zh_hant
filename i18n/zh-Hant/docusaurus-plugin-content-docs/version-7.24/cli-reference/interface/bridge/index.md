---
sidebar_key: "cli-reference/interface/bridge/index"
sidebar_position: 4
title: "bridge"
sidebar_label: "bridge"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/bridge
captured_at: '2026-11-01T21:26:58+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bridge {#interfacebridge}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="Y" typ="managed">managed</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="protocol-mode" typ="enum (none | stp | rstp | mstp) { none:0, stp:1, rstp:2, mstp:3 }"></ArgTableRow>
<ArgTableRow arg="fast-forward" typ="bool"></ArgTableRow>
<ArgTableRow arg="igmp-snooping" typ="bool"></ArgTableRow>
<ArgTableRow arg="multicast-router" typ="enum (disabled | temporary-query | permanent) { disabled:0, temporary-query:1, permanent:2 }"></ArgTableRow>
<ArgTableRow arg="multicast-querier" typ="bool"></ArgTableRow>
<ArgTableRow arg="querier-uses-bridge-address" typ="bool"></ArgTableRow>
<ArgTableRow arg="startup-query-count" typ="num"></ArgTableRow>
<ArgTableRow arg="last-member-query-count" typ="num"></ArgTableRow>
<ArgTableRow arg="last-member-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="membership-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="querier-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="query-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="query-response-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="startup-query-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="igmp-version" typ="enum (2 | 3) { 2:2, 3:3 }"></ArgTableRow>
<ArgTableRow arg="mld-version" typ="enum (1 | 2) { 1:1, 2:2 }"></ArgTableRow>
<ArgTableRow arg="auto-mac" typ="bool"></ArgTableRow>
<ArgTableRow arg="admin-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ageing-time" typ="time"></ArgTableRow>
<ArgTableRow arg="priority" typ="alt { priority: enum (0x0000 | 0x1000 | 0x2000 | 0x3000 | 0x4000 | 0x5000 | 0x6000 | 0x7000 | 0x8000 | 0x9000 | 0xa000 | 0xb000 | 0xc000 | 0xd000 | 0xe000 | 0xf000) { 0x0000:0x0000, 0x1000:0x1000, 0x2000:0x2000, 0x3000:0x3000, 0x4000:0x4000, 0x5000:0x5000, 0x6000:0x6000, 0x7000:0x7000, 0x8000:0x8000, 0x9000:0x9000, 0xa000:0xa000, 0xb000:0xb000, 0xc000:0xc000, 0xd000:0xd000, 0xe000:0xe000, 0xf000:0xf000 }
, priority: num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="max-message-age" typ="time"></ArgTableRow>
<ArgTableRow arg="forward-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="transmit-hold-count" typ="num"></ArgTableRow>
<ArgTableRow arg="region-name" typ="string"></ArgTableRow>
<ArgTableRow arg="region-revision" typ="num"></ArgTableRow>
<ArgTableRow arg="max-hops" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-filtering" typ="bool"></ArgTableRow>
<ArgTableRow arg="ether-type" typ="enum (0x8100 | 0x88a8 | 0x9100) { 0x8100:0x8100, 0x88a8:0x88a8, 0x9100:0x9100 }"></ArgTableRow>
<ArgTableRow arg="pvid" typ="num"></ArgTableRow>
<ArgTableRow arg="frame-types" typ="enum (admit-all | admit-only-vlan-tagged | admit-only-untagged-and-priority-tagged) { admit-all:0, admit-only-vlan-tagged:1, admit-only-untagged-and-priority-tagged:2 }"></ArgTableRow>
<ArgTableRow arg="ingress-filtering" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-snooping" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-agent-circuit-id" typ="string">
指定要新增到經過橋的 DHCP 報文中的 option 82 的 relay agent circuit-id 子選項值。
字串長度限制為 255 個字元，預設值為：$(INTERFACE):$(VID)。
字串值可以包含變數，變數名必須放在括號內，並在前面加上美元符號。
示例：'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'。
支援以下變數：HOSTNAME、INTERFACE、VID 和 BRIDGEMAC。
為了與早期版本相容（當時 remote-id 值是固定的），當未啟用 VLAN 過濾時，預設值表示式中出現的分號不會
包含在 remote-id 值中。
</ArgTableRow>
<ArgTableRow arg="dhcp-agent-remote-id" typ="string">
指定要新增到經過橋接的 DHCP 報文中的 option 82 的 relay agent remote-id 子選項值。
字串長度限制為 255 個字元，預設值為：$(BRIDGEMAC)。
字串值可以包含變數，變數名必須放在括號中，並在前面加上美元符號。
示例：'some_arbitrary_text $(HOSTNAME) another_piece_of_text $(BRIDGEMAC)'。
支援以下變數：HOSTNAME、INTERFACE、VID 和 BRIDGEMAC。
</ArgTableRow>
<ArgTableRow arg="dhcpv6-snooping" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcpv6-agent-circuit-id" typ="string">
指定要新增到經過橋接的 DHCPv6 報文中的 DHCPv6 option 18 值。
字串長度限制為 255 個字元，預設值為：$(INTERFACE):$(VID)。
字串值可以包含變數，變數名必須放在括號中，並在前面加上美元符號。
示例：'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'。
支援以下變數：HOSTNAME、INTERFACE、VID 和 BRIDGEMAC。
</ArgTableRow>
<ArgTableRow arg="dhcpv6-agent-remote-id" typ="string">
指定要新增到經過橋接的 DHCPv6 報文中的 DHCPv6 option 37 值。
字串長度限制為 255 個字元，預設值為：$(BRIDGEMAC)。
字串值可以包含變數，變數名必須放在括號中，並在前面加上美元符號。
示例：'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'。
支援以下變數：HOSTNAME、INTERFACE、VID 和 BRIDGEMAC。
</ArgTableRow>
<ArgTableRow arg="ra-guard" typ="bool"></ArgTableRow>
<ArgTableRow arg="port-cost-mode" typ="enum (short | long)"></ArgTableRow>
<ArgTableRow arg="mvrp" typ="bool"></ArgTableRow>
<ArgTableRow arg="msrp" typ="bool"></ArgTableRow>
<ArgTableRow arg="forward-reserved-addresses" typ="bool"></ArgTableRow>
<ArgTableRow arg="max-learned-entries" typ="alt { max-learned-entries: enum (unlimited | auto)
, max-learned-entries: num
 }"></ArgTableRow>
<ArgTableRow arg="mlag-peer-port" typ="alt { interface: iface_enum { none }
, interface-bond: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="mlag-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="mlag-heartbeat" typ="alt { mlag-heartbeat: enum (none) { none:0 }
, mlag-heartbeat: time [1s .. 10s]
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>
