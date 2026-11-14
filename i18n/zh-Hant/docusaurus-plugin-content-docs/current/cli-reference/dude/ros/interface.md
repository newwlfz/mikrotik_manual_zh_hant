---
sidebar_key: "cli-reference/dude/ros/interface"
sidebar_position: 4
title: "interface"
sidebar_label: 'interface'
source: https://manual.mikrotik.com/docs/cli-reference/dude/ros/interface
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## dude/ros/interface {#duderosinterface}
**軟體包：** dude
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
<ArgTableRow arg="S" typ="slave"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="actual-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="max-l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="fast-path" typ="bool"></ArgTableRow>
<ArgTableRow arg="last-link-down-time" typ="date"></ArgTableRow>
<ArgTableRow arg="last-link-up-time" typ="date"></ArgTableRow>
<ArgTableRow arg="link-downs" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-drop" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-drop" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-error" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-error" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-rx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-tx-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="fp-tx-packet" typ="num"></ArgTableRow>
</ArgTable>
