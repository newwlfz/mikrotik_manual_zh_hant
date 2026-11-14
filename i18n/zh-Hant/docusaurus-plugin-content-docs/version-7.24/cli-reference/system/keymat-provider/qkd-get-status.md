---
sidebar_key: "cli-reference/system/keymat-provider/qkd-get-status"
sidebar_position: 3
title: "qkd-get-status"
sidebar_label: "qkd-get-status"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/keymat-provider/qkd-get-status
captured_at: '2026-11-01T21:29:52+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/keymat-provider/qkd-get-status {#systemkeymat-providerqkd-get-status}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="sae-id" typ="string">如果未指定，將使用 peer-sae-id</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="source-kme-id" typ="string"></ArgTableRow>
<ArgTableRow arg="target-kme-id" typ="string"></ArgTableRow>
<ArgTableRow arg="master-sae-id" typ="string"></ArgTableRow>
<ArgTableRow arg="slave-sae-id" typ="string"></ArgTableRow>
<ArgTableRow arg="key-size" typ="num"></ArgTableRow>
<ArgTableRow arg="stored-key-count" typ="num"></ArgTableRow>
<ArgTableRow arg="max-key-count" typ="num"></ArgTableRow>
<ArgTableRow arg="max-key-per-request" typ="num"></ArgTableRow>
<ArgTableRow arg="max-key-size" typ="num"></ArgTableRow>
<ArgTableRow arg="min-key-size" typ="num"></ArgTableRow>
<ArgTableRow arg="max-sae-id-count" typ="num"></ArgTableRow>
</ArgTable>
