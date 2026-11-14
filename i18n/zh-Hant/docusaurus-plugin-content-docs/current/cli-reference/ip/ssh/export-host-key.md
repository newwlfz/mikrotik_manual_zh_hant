---
sidebar_key: "cli-reference/ip/ssh/export-host-key"
sidebar_position: 1
title: "export-host-key"
sidebar_label: 'export-host-key'
source: https://manual.mikrotik.com/docs/cli-reference/ip/ssh/export-host-key
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ssh/export-host-key {#ipsshexport-host-key}
**型別：** 命令

將 RSA/Ed25519 公鑰和私鑰匯出到檔案。

:::info
主機金鑰以 PKCS#8 格式匯出。

匯出 SSH 主機金鑰需要 "sensitive" 使用者策略。
:::

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="key-file-prefix" typ="string">生成檔案的字首：例如，對於 RSA 主機金鑰，`my` 會生成 `my_rsa.pem`（私鑰）和 `my_rsa_pub.pem`（公鑰）；對於 Ed25519 主機金鑰，則會生成 `my_ed25519.pem` 和 `my_ed25519_pub.pem`。兩個檔案均為 PKCS#8 PEM 格式。</ArgTableRow>
<ArgTableRow arg="passphrase" typ="string">私鑰密碼短語。</ArgTableRow>
</ArgTable>
