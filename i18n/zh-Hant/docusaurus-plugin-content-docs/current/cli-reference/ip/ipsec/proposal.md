---
sidebar_key: "cli-reference/ip/ipsec/proposal"
sidebar_position: 9
title: "proposal"
sidebar_label: 'proposal'
source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/proposal
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/proposal {#ipipsecproposal}
**型別：** 目錄

IKE 守護程式為某些策略建立 SA 而傳送的提議資訊。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否已停用。</ArgTableRow>
<ArgTableRow arg="*" typ="default">專案是否為預設項。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">提議名稱。</ArgTableRow>
<ArgTableRow arg="auth-algorithms" typ="ubit (sha512, sha256, sha1, md5, null)">允許的身份驗證演算法。MD5 使用 128 位金鑰，SHA1 使用 160 位金鑰。</ArgTableRow>
<ArgTableRow arg="enc-algorithms" typ="ubit (chacha20poly1305, aes-256-cbc, aes-256-ctr, aes-256-gcm, camellia-256, aes-192-cbc, aes-192-ctr, aes-192-gcm, camellia-192, aes-128-cbc, aes-128-ctr, aes-128-gcm, camellia-128, 3des, blowfish, twofish, des, null)">允許的加密演算法。</ArgTableRow>
<ArgTableRow arg="lifetime" typ="time">階段 2 生命週期。</ArgTableRow>
<ArgTableRow arg="pfs-group" typ="enum (none | ecp256 | ecp384 | ecp521 | modp6144 | modp4096 | modp3072 | modp2048 | modp1536 | modp1024 | modp768) { none:0 }">完美前向保密組。</ArgTableRow>
</ArgTable>
