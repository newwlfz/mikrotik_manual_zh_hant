---
sidebar_key: "cli-reference/ip/nat-pmp/interfaces"
sidebar_position: 1
title: "interfaces"
sidebar_label: "interfaces"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/nat-pmp/interfaces
captured_at: '2026-11-01T21:28:49+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/nat-pmp/interfaces {#ipnat-pmpinterfaces}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (external | internal)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="forced-ip" typ="super { forced-ip: ipAddr
 }"></ArgTableRow>
</ArgTable>
