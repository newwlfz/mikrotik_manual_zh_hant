---
sidebar_key: "cli-reference/routing/pimsm/interface"
sidebar_position: 5
title: "interface"
sidebar_label: "interface"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/pimsm/interface
captured_at: '2026-11-01T21:29:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/interface {#routingpimsminterface}
**條件：** !smips
**型別：** 目錄

interface 選單顯示當前參與 PIM 的所有介面及其狀態。此選單包含由已定義的介面模板建立的動態和只讀條目。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="P" typ="designated-router">designated-router</ArgTableRow>
<ArgTableRow arg="J" typ="join-tracking">join-tracking</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="dr" typ="switch"></ArgTableRow>
<ArgTableRow arg="join-tracking" typ="switch"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="propagation-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="override-interval" typ="time"></ArgTableRow>
</ArgTable>
