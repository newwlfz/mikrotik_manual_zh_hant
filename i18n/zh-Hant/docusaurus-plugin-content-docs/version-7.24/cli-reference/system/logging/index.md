---
sidebar_key: "cli-reference/system/logging/index"
sidebar_position: 2
title: "logging"
sidebar_label: "logging"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/logging
captured_at: '2026-11-01T21:29:54+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/logging {#systemlogging}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="Y" typ="managed"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="topics" typ="multi { array-id, array-id, topic: super { !
, topic: enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="prefix" typ="string"></ArgTableRow>
<ArgTableRow arg="regex" typ="string"></ArgTableRow>
<ArgTableRow arg="action" typ="enum"></ArgTableRow>
</ArgTable>
