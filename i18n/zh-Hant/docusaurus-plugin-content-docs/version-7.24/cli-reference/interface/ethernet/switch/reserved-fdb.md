---
sidebar_key: "cli-reference/interface/ethernet/switch/reserved-fdb"
sidebar_position: 20
title: "reserved-fdb"
sidebar_label: "reserved-fdb"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/reserved-fdb
captured_at: '2026-11-01T21:27:18+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/reserved-fdb {#interfaceethernetswitchreserved-fdb}
**系統能力：** musicswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (forward | redirect-to-cpu | copy-to-cpu | drop) { forward:0, redirect-to-cpu:1, copy-to-cpu:2, drop:3 }"></ArgTableRow>
<ArgTableRow arg="bypass-ingress-vlan-filter" typ="bool"></ArgTableRow>
<ArgTableRow arg="bypass-ingress-port-policing" typ="bool"></ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }"></ArgTableRow>
</ArgTable>
