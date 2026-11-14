---
sidebar_key: "cli-reference/ip/ssh/known-hosts"
sidebar_position: 3
title: "known-hosts"
sidebar_label: 'known-hosts'
source: https://manual.mikrotik.com/docs/cli-reference/ip/ssh/known-hosts
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ssh/known-hosts {#ipsshknown-hosts}
**型別：** 目錄

路由器 SSH 用戶端所信任的遠端 SSH 伺服器的主機公鑰。當你在互動式用戶端的信任提示中回答 `y`，或使用 `add` 手動固定金鑰時，會儲存金鑰。當在 [`/ip/ssh`](./index.md) 中啟用 `known-hosts-validation` 時使用。完整指南請參見 [SSH](../../../management-tools/ssh.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="host" typ="ip6Addr">金鑰所屬 SSH 伺服器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="key" typ="string">伺服器的主機公鑰，採用一個 OpenSSH 風格條目：`<type> <base64>`，例如 `ssh-rsa AAAAB3...`。貼上其他伺服器的金鑰會按原樣儲存；金鑰不匹配會導致後續連線失敗，並提示 `host key not trusted`。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="key-type" typ="enum (rsa | ed25519)">已固定主機金鑰的金鑰型別：`rsa` 或 `ed25519`。</ArgTableRow>
<ArgTableRow arg="fingerprint" typ="string">固定金鑰的 SHA256 指紋。將其與該伺服器的 `host-key-fingerprint` 進行比較，該值由該伺服器上的 `/ip/ssh/print` 顯示。</ArgTableRow>
</ArgTable>
