---
sidebar_key: "cli-reference/tool/e-mail"
title: "e-mail"
sidebar_label: 'e-mail'
source: https://manual.mikrotik.com/docs/cli-reference/tool/e-mail
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/e-mail {#toole-mail}
**型別：** 設定目錄

路由器用來發送電子郵件的 SMTP 伺服器設定：伺服器和埠、TLS 模式、證書驗證、發件人和登入資訊。除非命令覆蓋這些設定，否則 `/tool/e-mail/send` 會對每封郵件使用它們。參見 [電子郵件](../../../system-information-and-utilities/e-mail.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="server" typ="alt { ipv6: ip6Addr
, ip: ipAddr
, fqdn: string
 }">SMTP 伺服器 IP 地址、IPv6 地址或 FQDN。使用名稱時，`last-address` 顯示路由器連線到的地址。預設值：0.0.0.0。</ArgTableRow>
<ArgTableRow arg="port" typ="num">SMTP 伺服器埠。預設值：25。</ArgTableRow>
<ArgTableRow arg="tls" typ="enum (no | yes | starttls)">
TLS 加密模式：
- `no`（預設）- 不使用 TLS。即使伺服器提供 STARTTLS，路由器也不會發送 STARTTLS。
- `yes` - 從連線開始就使用 TLS（隱式 TLS，通常為埠 465）。
- `starttls` - 使用 STARTTLS 升級連線（通常為埠 587）。當伺服器不提供 STARTTLS 時，傳送會失敗並顯示 `TLS not supported by server`；不會回退到未加密連線。
</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">服務在其上創建出站連線的 VRF。預設值：main。</ArgTableRow>
<ArgTableRow arg="from" typ="string">將顯示為發件人的名稱或電子郵件地址。當它為空時，路由器會使用空發件人（`<>`）傳送郵件，許多伺服器會拒絕這種郵件。預設值：&lt;&gt;。</ArgTableRow>
<ArgTableRow arg="user" typ="string">用於向 SMTP 伺服器進行身份驗證的使用者名稱。路由器使用 AUTH PLAIN 登入；在沒有 TLS 的情況下，使用者名稱和密碼會以未加密方式透過網路傳輸。預設值：""。</ArgTableRow>
<ArgTableRow arg="password" typ="string">用於向 SMTP 伺服器進行身份驗證的密碼。預設值：""。</ArgTableRow>
<ArgTableRow arg="certificate-verification" typ="enum (no | yes | yes-without-crl)">
TLS 證書驗證：
- `no`（預設）- 路由器會加密連線，但不檢查伺服器的證書。
- `yes` - 根據本地證書儲存驗證證書鏈，包括伺服器名稱。內建信任儲存預設涵蓋電子郵件。
- `yes-without-crl` - 驗證證書但不執行 CRL 檢查。
</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="last-status" typ="enum (none | resolving-dns | in-progress | failed | succeeded)">上次電子郵件傳送嘗試的狀態：結束時為 `succeeded` 或 `failed`。</ArgTableRow>
<ArgTableRow arg="last-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }">上次使用的 SMTP 伺服器的 IP 地址。</ArgTableRow>
</ArgTable>
