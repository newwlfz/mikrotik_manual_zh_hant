---
sidebar_key: "cli-reference/interface/ovpn-client"
title: "ovpn-client"
sidebar_label: 'ovpn-client'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ovpn-client
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ovpn-client {#interfaceovpn-client}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
<ArgTableRow arg="H" typ="hw-crypto">硬體加密是否處於活動狀態。</ArgTableRow>
<ArgTableRow arg="Ta" typ="tls-auth">TLS 身份驗證（tls-auth）是否處於活動狀態。</ArgTableRow>
<ArgTableRow arg="Tc" typ="tls-crypt">tls-crypt 身份驗證是否處於活動狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面的描述性名稱。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">OVPN 介面的 MAC 地址。如果未指定，則自動生成。</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大傳輸單元。OVPN 介面在不進行封包分片的情況下可以傳送的最大封包大小。</ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)" mandatory="1">OVPN 伺服器的遠端地址。</ArgTableRow>
<ArgTableRow arg="port" typ="num">要連線的埠。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (ip | ethernet) { ip:0, ethernet:1 }">Layer3 或 Layer2 隧道模式（也可為 tun、tap）。</ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (tcp | udp)">連線到遠端端點時使用的傳輸協定。</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">用於身份驗證的使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string">用於身份驗證的密碼。長度不得超過 1000 個字元。</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">指定建立隧道時使用哪個 PPP 配置檔案。</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }">證書儲存中的用戶端證書。</ArgTableRow>
<ArgTableRow arg="verify-server-certificate" typ="bool">根據 connect-to 引數檢查伺服器證書的 CN 或 SAN，並啟用針對路由器證書儲存的信任鏈驗證。IP 或主機名必須存在於伺服器證書中。</ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }">指定允許使用哪些 TLS 版本。</ArgTableRow>
<ArgTableRow arg="auth" typ="enum (sha1 | md5 | sha256 | sha384 | sha512 | null) { sha1:1, md5:2, sha256:8, sha384:32, sha512:16, null:4 }">允許的身份驗證方法。</ArgTableRow>
<ArgTableRow arg="cipher" typ="enum (blowfish128 | aes128-cbc | aes192-cbc | aes256-cbc | aes128-gcm | aes192-gcm | aes256-gcm | null) { blowfish128:1, aes128-cbc:2, aes192-cbc:4, aes256-cbc:8, aes128-gcm:16, aes192-gcm:32, aes256-gcm:64, null:128 }">允許的加密演算法。要使用 GCM 加密演算法，請將 auth 設定為 null，因為 GCM 加密演算法也會處理身份驗證。</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively) { no:0, yes:1, exclusively:2 }">是否將 OVPN 伺服器提供的 DNS 伺服器新增到 IP/DNS 配置中。</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">是否將 OVPN 遠端地址新增為預設路由。</ArgTableRow>
<ArgTableRow arg="route-nopull" typ="bool">如果啟用，用戶端不使用伺服器推送的路由（包括 def1）。</ArgTableRow>
<ArgTableRow arg="disconnect-notify" typ="bool">在 UDP 模式下發送顯式斷開連線通知。</ArgTableRow>
</ArgTable>
