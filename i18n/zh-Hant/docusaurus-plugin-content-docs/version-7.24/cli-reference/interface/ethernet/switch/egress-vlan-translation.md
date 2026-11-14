---
sidebar_key: "cli-reference/interface/ethernet/switch/egress-vlan-translation"
sidebar_position: 5
title: "egress-vlan-translation"
sidebar_label: "egress-vlan-translation"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/egress-vlan-translation
captured_at: '2026-11-01T21:27:09+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/egress-vlan-translation {#interfaceethernetswitchegress-vlan-translation}
**系統能力：** musicswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="service-vlan-format" typ="enum (untagged-or-tagged | priority-tagged-or-tagged | tagged | any) { untagged-or-tagged:0, priority-tagged-or-tagged:1, tagged:2, any:3 }"></ArgTableRow>
<ArgTableRow arg="service-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="service-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="service-dei" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-vlan-format" typ="enum (untagged-or-tagged | priority-tagged-or-tagged | tagged | any) { untagged-or-tagged:0, priority-tagged-or-tagged:1, tagged:2, any:3 }"></ArgTableRow>
<ArgTableRow arg="customer-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-dei" typ="num"></ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="alt { special-vid: enum (customer-vid) { customer-vid:4096 }
, vid: num [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="alt { special-vid: enum (service-vid) { service-vid:4096 }
, vid: num [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="pcp-propagation" typ="bool"></ArgTableRow>
<ArgTableRow arg="swap-vids" typ="enum (no | assign-cvid-to-svid) { no:0, assign-cvid-to-svid:0 }"></ArgTableRow>
</ArgTable>
