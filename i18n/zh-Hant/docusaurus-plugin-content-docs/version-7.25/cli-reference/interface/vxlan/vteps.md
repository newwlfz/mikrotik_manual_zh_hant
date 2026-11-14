---
sidebar_key: "cli-reference/interface/vxlan/vteps"
sidebar_position: 2
title: "vteps"
sidebar_label: 'vteps'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/vxlan/vteps
captured_at: '2026-11-01T21:23:03+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/vxlan/vteps {#interfacevxlanvteps}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬體解除安裝</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="remote-ip" typ="alt { address: ipAddr
, ipv6-address: ip6Addr
 }" mandatory="1"></ArgTableRow>
</ArgTable>
