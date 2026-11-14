---
sidebar_key: "cli-reference/tool/dns-update"
sidebar_position: 5
title: "dns-update"
sidebar_label: 'dns-update'
source: https://manual.mikrotik.com/docs/cli-reference/tool/dns-update
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/dns-update {#tooldns-update}
**型別：** 命令

向區域的權威 DNS 伺服器傳送一次動態 DNS 更新（RFC 2136），使用 TSIG hmac-md5 金鑰簽名，並把該區域中的一個名稱指向一個 IPv4 地址。該更新會替換該名稱的 A 記錄。當伺服器接受更新時，該命令不會輸出任何內容。參見 [DNS 更新](../../diagnostics-monitoring-and-troubleshooting/dynamic-dns.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="dns-server" typ="ipAddr">`zone` 的權威 DNS 伺服器的 IPv4 地址。更新會發送到其 TCP 埠 53。</ArgTableRow>
<ArgTableRow arg="zone" typ="string">包含該名稱的 DNS 區域，例如 `example.com`。</ArgTableRow>
<ArgTableRow arg="name" typ="string">要更新的名稱，相對於 `zone`：`name=office` 與 `zone=example.com` 會更新 `office.example.com`。完整名稱會被再次附加到區域後面，而帶末尾點的名稱會失敗並返回 `failure: bad name`。</ArgTableRow>
<ArgTableRow arg="address" typ="multi { addr: ipAddr
 }">該名稱的 A 記錄的 IPv4 地址。必需。只接受一個地址（`failure: only one address allowed`），IPv6 地址會被拒絕。</ArgTableRow>
<ArgTableRow arg="key-name" typ="string">TSIG 金鑰的名稱，與 DNS 伺服器上配置的一致。未提供 `key-name` 和 `key` 時，更新會以未簽名方式傳送。</ArgTableRow>
<ArgTableRow arg="key" typ="string">TSIG 金鑰的機密值（base64 格式），與 DNS 伺服器上配置的一致。演算法為 hmac-md5。請將值放在引號中，因為 base64 值可能以 `=` 結尾。</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">記錄的生存時間，單位為秒。對於會變化的地址，請使用較短的值，例如 `300`。預設值：86400。</ArgTableRow>
</ArgTable>
