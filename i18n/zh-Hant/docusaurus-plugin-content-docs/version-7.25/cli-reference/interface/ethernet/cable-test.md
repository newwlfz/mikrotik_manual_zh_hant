---
sidebar_key: "cli-reference/interface/ethernet/cable-test"
sidebar_position: 2
title: "cable-test"
sidebar_label: 'cable-test'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/cable-test
captured_at: '2026-11-01T21:22:29+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/cable-test {#interfaceethernetcable-test}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (unknown | link-ok | no-link | initializing | auto-init-failed)"></ArgTableRow>
<ArgTableRow arg="cable-pairs" typ="multi { array-id, array-id, mac-mask: composite { status: enum (normal | shorted | open | unknown | line-driver | mismatch)
, cable-length: enum (?) { ?:0xffffffff }
 }
 }"></ArgTableRow>
</ArgTable>
