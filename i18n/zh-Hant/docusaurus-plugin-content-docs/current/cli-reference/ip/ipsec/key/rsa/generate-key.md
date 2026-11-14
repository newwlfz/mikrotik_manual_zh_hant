---
sidebar_key: "cli-reference/ip/ipsec/key/rsa/generate-key"
sidebar_position: 2
title: "generate-key"
sidebar_label: 'generate-key'
source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/key/rsa/generate-key
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/key/rsa/generate-key {#ipipseckeyrsagenerate-key}
**型別：** 命令

生成私鑰。接受兩個引數：新生成金鑰的名稱以及金鑰長度 1024、2048 和 4096。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">生成的金鑰的名稱。</ArgTableRow>
<ArgTableRow arg="key-size" typ="alt { key-size: enum (2048 | 4096 | 8192) { 2048:2048, 4096:4096, 8192:8192 }
 }">RSA 金鑰長度（以位為單位）。</ArgTableRow>
</ArgTable>
