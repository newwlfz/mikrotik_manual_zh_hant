---
sidebar_key: "cli-reference/system/keymat-provider/qkd-get-key-with-ids"
sidebar_position: 1
title: "qkd-get-key-with-ids"
sidebar_label: "qkd-get-key-with-ids"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/keymat-provider/qkd-get-key-with-ids
captured_at: '2026-11-01T21:29:53+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/keymat-provider/qkd-get-key-with-ids {#systemkeymat-providerqkd-get-key-with-ids}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="key-ids" typ="multi { array-id, key-id: string
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="keys" typ="object { qkd-key: super { key-id: string
, [key] : string
 }
 }"></ArgTableRow>
</ArgTable>
