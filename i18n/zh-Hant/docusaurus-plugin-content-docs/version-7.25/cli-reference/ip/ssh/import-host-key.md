---
sidebar_key: "cli-reference/ip/ssh/import-host-key"
sidebar_position: 2
title: "import-host-key"
sidebar_label: 'import-host-key'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/ssh/import-host-key
captured_at: '2026-11-01T21:24:27+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ssh/import-host-key {#ipsshimport-host-key}
**型別：** 命令

從指定檔案匯入並替換 RSA/Ed25519 私鑰

:::info
私鑰支援 PEM 或 PKCS#8 格式。
:::

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="private-key-file" typ="file">PEM 或 PKCS#8 格式的 RSA/Ed25519 私鑰檔案的名稱。</ArgTableRow>
<ArgTableRow arg="passphrase" typ="string">私鑰密碼短語。</ArgTableRow>
</ArgTable>
