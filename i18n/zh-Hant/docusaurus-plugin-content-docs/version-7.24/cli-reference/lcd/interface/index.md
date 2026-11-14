---
sidebar_key: "cli-reference/lcd/interface/index"
sidebar_position: 3
title: "interface"
sidebar_label: "interface"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/lcd/interface
captured_at: '2026-11-01T21:29:13+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## lcd/interface {#lcdinterface}
**條件：** !smips
**系統能力：** lcd
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="displayed">displayed</ArgTableRow>
<ArgTableRow arg="W" typ="default-wireless">default-wireless</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="max-speed" typ="num" mandatory="1"></ArgTableRow>
</ArgTable>
