---
sidebar_key: "cli-reference/interface/ethernet/switch/protocol-based-vlan"
sidebar_position: 17
title: "protocol-based-vlan"
sidebar_label: "protocol-based-vlan"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/protocol-based-vlan
captured_at: '2026-11-01T21:27:14+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/protocol-based-vlan {#interfaceethernetswitchprotocol-based-vlan}
**系統能力：** musicswitch
**型別：**目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="frame-type" typ="enum (ethernet | rfc-1042 | llc) { ethernet:0, rfc-1042:1, llc:2 }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="alt { protocol: enum ()
, protocol-number: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="set-service-vid-for" typ="enum (none | untagged-or-priority-tagged | tagged | all) { none:0, untagged-or-priority-tagged:1, tagged:2, all:3 }"></ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="set-customer-vid-for" typ="enum (none | untagged-or-priority-tagged | tagged | all) { none:0, untagged-or-priority-tagged:1, tagged:2, all:3 }"></ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="set-qos-for" typ="enum (none | untagged-or-priority-tagged | tagged | all) { none:0, untagged-or-priority-tagged:1, tagged:2, all:3 }"></ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }"></ArgTableRow>
</ArgTable>
