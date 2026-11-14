---
sidebar_key: "cli-reference/tool/e-mail/send"
sidebar_position: 1
title: "send"
sidebar_label: 'send'
source: https://manual.mikrotik.com/docs/cli-reference/tool/e-mail/send
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/e-mail/send {#toole-mailsend}
**型別：** 命令

透過 [`/tool/e-mail`](./index.md) 中的 SMTP 伺服器傳送一封電子郵件。傳給該命令的引數會覆蓋此郵件的伺服器設定。結果會顯示在 `/tool/e-mail` 的 `last-status` 中。參見[電子郵件](../../../system-information-and-utilities/e-mail.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="server" typ="alt { ipv6: ip6Addr
, ip: ipAddr
, fqdn: string
 }">SMTP 伺服器的 IP 地址、IPv6 地址或 FQDN。如果未指定，則使用伺服器配置中的值。</ArgTableRow>
<ArgTableRow arg="port" typ="num">SMTP 伺服器埠。如果未指定，則使用伺服器配置中的值。</ArgTableRow>
<ArgTableRow arg="to" typ="multi { array-id, to: string
 }">目標電子郵件地址。允許填寫多個地址，以逗號分隔；路由器會向所有這些地址傳送同一封郵件。</ArgTableRow>
<ArgTableRow arg="cc" typ="multi { array-id, cc: string
 }">向列出的收件人傳送副本。允許填寫多個地址，以逗號分隔。</ArgTableRow>
<ArgTableRow arg="from" typ="string">將顯示為發件人的名稱或電子郵件地址。如果未指定，則使用伺服器配置中的值；若該值也為空，則發件人為 `<>`，許多伺服器會拒絕這種發件人。</ArgTableRow>
<ArgTableRow arg="subject" typ="string">郵件的主題。</ArgTableRow>
<ArgTableRow arg="body" typ="string">電子郵件的正文文字。`\n` 表示換行。</ArgTableRow>
<ArgTableRow arg="file" typ="multi { array-id, file: file
 }">要附加到郵件的檔名列表，以逗號分隔。每個檔案都以 `application/octet-stream` 形式附加。不存在的檔案會在傳送前被拒絕（`input does not match any value of file`）。</ArgTableRow>
<ArgTableRow arg="user" typ="string">用於向 SMTP 伺服器進行身份驗證的使用者名稱（AUTH PLAIN；未使用 TLS 時為未加密傳輸）。如果未指定，則使用伺服器配置中的值。</ArgTableRow>
<ArgTableRow arg="password" typ="string">用於向 SMTP 伺服器進行身份驗證的密碼。如果未指定，則使用伺服器配置中的值。</ArgTableRow>
<ArgTableRow arg="tls" typ="enum (no | yes | starttls)">
TLS 加密模式。如果未指定，則使用伺服器配置中的值：
- `no` - 不使用 TLS。即使伺服器提供 STARTTLS，路由器也不會發送 STARTTLS。
- `yes` - 從連線一開始就使用 TLS（隱式 TLS，通常為埠 465）。
- `starttls` - 使用 STARTTLS 升級連線（通常為埠 587）。當伺服器不提供 STARTTLS 時，傳送會失敗並報錯 `TLS not supported by server`；不會回退到未加密的連線。
</ArgTableRow>
<ArgTableRow arg="certificate-verification" typ="enum (no | yes | yes-without-crl)">
TLS 證書驗證。如果未指定，則使用伺服器配置中的值：
- `no` - 路由器會加密連線，但不檢查伺服器的證書。
- `yes` - 對照本地證書儲存驗證證書鏈，包括伺服器名稱。內建信任儲存預設涵蓋電子郵件。
- `yes-without-crl` - 驗證證書，但不執行 CRL 檢查。
</ArgTableRow>
</ArgTable>
