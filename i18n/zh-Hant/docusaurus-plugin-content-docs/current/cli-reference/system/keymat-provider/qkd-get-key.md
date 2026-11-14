---
sidebar_key: "cli-reference/system/keymat-provider/qkd-get-key"
sidebar_position: 2
title: "qkd-get-key"
sidebar_label: 'qkd-get-key'
source: https://manual.mikrotik.com/docs/cli-reference/system/keymat-provider/qkd-get-key
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/keymat-provider/qkd-get-key {#systemkeymat-providerqkd-get-key}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="additional-sae-ids" typ="multi { array-id, sae-id: string
 }">還會獲取所生成金鑰的其他 SAE</ArgTableRow>
<ArgTableRow arg="number" typ="num">要生成的金鑰數量</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="keys" typ="object { qkd-key: super { key-id: string
, [key] : string
 }
 }"></ArgTableRow>
</ArgTable>
