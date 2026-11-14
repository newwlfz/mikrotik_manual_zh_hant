---
sidebar_key: "cli-reference/interface/bridge/msrp/domain"
sidebar_position: 2
title: "domain"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/bridge/msrp/domain
captured_at: '2026-11-02T09:09:02+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bridge/msrp/domain {#interfacebridgemsrpdomain}
**條件：** MSRP_ENABLE
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
</ArgTable>
