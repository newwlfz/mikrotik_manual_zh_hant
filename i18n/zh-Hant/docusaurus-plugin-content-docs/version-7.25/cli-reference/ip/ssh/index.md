---
sidebar_key: "cli-reference/ip/ssh/index"
sidebar_position: 3
title: "ssh"
sidebar_label: 'ssh'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/ssh
captured_at: '2026-11-01T21:24:27+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ssh {#ipssh}
**型別：** 設定目錄

SSH 伺服器設定（ciphers、轉發、身份驗證），以及路由器作為 SSH 用戶端連線時用於驗證遠端伺服器的設定。完整指南請參閱 [SSH](../../../management-tools/ssh.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ciphers" typ="multi { array-id, cipher: enum (aes-gcm | aes-ctr | aes-cbc | 3des-cbc | null | auto)
 }">允許的加密演算法列表。</ArgTableRow>
<ArgTableRow arg="forwarding-enabled" typ="enum (no | local | remote | both)">控制允許哪種 SSH 轉發方式：`no` - 停用 SSH 轉發，`local` - 允許 SSH 用戶端從伺服器（路由器）發起連線，這也會控制動態轉發，`remote` - 允許 SSH 用戶端在伺服器（路由器）上監聽並轉發傳入連線，`both` - 同時允許本地和遠端轉發方式。</ArgTableRow>
<ArgTableRow arg="password-authentication" typ="enum (yes | no | yes-if-no-key)">當為使用者配置了公鑰授權時，是否允許密碼登入。</ArgTableRow>
<ArgTableRow arg="publickey-authentication-options" typ="enum (none | touch-required | verify-required)">公鑰身份驗證選項。`touch-required` 選項會使採用 FIDO 身份驗證器演算法的公鑰身份驗證始終要求籤名證明物理在場的使用者已明確確認身份驗證（通常透過觸控身份驗證器）。`verify-required` 選項要求 FIDO 金鑰簽名證明使用者已透過驗證，例如透過使用 PIN。</ArgTableRow>
<ArgTableRow arg="strong-crypto" typ="bool">使用更強的加密、HMAC 演算法，使用更大的 DH 素數並禁止較弱的：使用 256 和 192 bit 加密而不是 128 bits，停用 null 加密，使用 sha256 進行雜湊而不是 sha1，停用 md5，使用 2048bit 素數進行 Diffie-Hellman 交換而不是 1024bit。</ArgTableRow>
<ArgTableRow arg="known-hosts-validation" typ="bool">根據儲存在 [`known-hosts`](./known-hosts.md) 中的金鑰，每當路由器作為 SSH 用戶端連線時（fetch SFTP、[`/system/ssh`](../../system/ssh.md)、[`/system/ssh-exec`](../../system/ssh-exec.md)）驗證伺服器的主機金鑰。在啟用驗證且沒有儲存匹配金鑰的情況下，互動式用戶端會顯示伺服器的指紋並詢問 `do you want to trust this host key?`，而非互動式命令會失敗並顯示 `host key not trusted`。在新安裝中，驗證處於啟用狀態；升級後的路由器會保留之前的值。預設值：yes.</ArgTableRow>
<ArgTableRow arg="known-hosts-trusted-subnets" typ="object { subnets: ip6Prefix
 }">對於地址屬於這些子網的伺服器，即使啟用了 `known-hosts-validation`，也跳過主機金鑰驗證。所列子網之外的主機仍會進行驗證。</ArgTableRow>
<ArgTableRow arg="host-key-size" typ="enum (1024 | 1536 | 2048 | 4096 | 8192) { 1024:1024, 1536:1536, 2048:2048, 4096:4096, 8192:8192 }">重新生成主機金鑰時的 RSA 金鑰大小。</ArgTableRow>
<ArgTableRow arg="host-key-type" typ="enum (rsa | ed25519) { rsa:0, ed25519:3 }">主機金鑰型別。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="host-key-fingerprint" typ="string">當前主機金鑰的指紋。可用於驗證你連線的是正確的路由器。</ArgTableRow>
</ArgTable>
