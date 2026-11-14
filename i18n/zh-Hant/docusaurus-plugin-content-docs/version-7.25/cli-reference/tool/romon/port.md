---
sidebar_key: "cli-reference/tool/romon/port"
sidebar_position: 3
title: "port"
sidebar_label: 'port'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/romon/port
captured_at: '2026-11-01T21:25:57+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/romon/port {#toolromonport}
**型別：** 目錄

參與 [RoMON 網路](../../../management-tools/romon.md#configuration) 的埠。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum { all }" mandatory="1">用於 RoMON 的介面名稱或 interface-list。</ArgTableRow>
<ArgTableRow arg="forbid" typ="bool">匹配的介面是被允許還是禁止加入 RoMON 網路。</ArgTableRow>
<ArgTableRow arg="cost" typ="num">埠開銷。所有特定埠條目的優先順序都高於使用 `interface=all` 的通配條目。</ArgTableRow>
<ArgTableRow arg="secrets" typ="multi { array-id, name: string
 }">用於 RoMON 訊息雜湊的各個埠金鑰列表。</ArgTableRow>
</ArgTable>
