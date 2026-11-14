---
sidebar_key: "cli-reference/ip/dns/forwarders"
sidebar_position: 3
title: "forwarders"
sidebar_label: 'forwarders'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/dns/forwarders
captured_at: '2026-11-01T21:23:55+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dns/forwarders {#ipdnsforwarders}
**型別：** 目錄

為靜態 `FWD` 條目命名上游伺服器組：將 [`/ip/dns/static`](./static.md) 中某個條目的 `forward-to` 設定為該轉發器名稱。每個查詢會依次輪換使用 `dns-servers` 和 `doh-servers` 中的下一個伺服器（輪詢）。無響應的伺服器不會被跳過：在 `query-total-timeout` 之後，傳送給它的查詢會以 SERVFAIL 失敗，因此請只列出可正常工作的伺服器。有關示例，請參閱 [DNS](../../../network-management/dns.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">轉發器已停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">轉發器的名稱，在靜態 `FWD` 條目中用作 `forward-to`。</ArgTableRow>
<ArgTableRow arg="dns-servers" typ="multi { address (flags=46D)
 }">轉發器的 DNS 伺服器，形式為 IP 地址或 DNS 名稱，例如 `dns-servers=1.1.1.1,8.8.8.8`。</ArgTableRow>
<ArgTableRow arg="doh-servers" typ="multi { string
 }">轉發器的 DoH 伺服器 URL，例如 `doh-servers=https://dns.google/dns-query`。路由器透過 `/ip/dns` 中的 `servers` 查詢它們的主機名。</ArgTableRow>
<ArgTableRow arg="verify-doh-cert" typ="bool">路由器是否根據 `/certificate` 和內建信任儲存驗證 DoH 伺服器的證書。證書不受信任的伺服器會在日誌中失敗，並顯示 `SSL: ssl: no trusted CA certificate found (6)`。此預設值與 `/ip/dns` 中的 `verify-doh-cert` 不同。預設值：yes.</ArgTableRow>
</ArgTable>
