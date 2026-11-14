---
sidebar_key: "cli-reference/interface/ethernet/switch/host"
sidebar_position: 6
title: "host"
sidebar_label: "host"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/host
captured_at: '2026-11-01T21:27:09+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/host {#interfaceethernetswitchhost}
**系統能力：** rbswitch and oldswitch
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="switch" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, port: alt { port: enum
, trunk: iface_enum
 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="copy-to-cpu" typ="bool"></ArgTableRow>
<ArgTableRow arg="redirect-to-cpu" typ="bool"></ArgTableRow>
<ArgTableRow arg="drop" typ="bool"></ArgTableRow>
<ArgTableRow arg="mirror" typ="bool"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="share-vlan-learned" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>
