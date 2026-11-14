---
sidebar_key: "cli-reference/ip/reverse-proxy"
sidebar_position: 18
title: "reverse-proxy"
sidebar_label: 'reverse-proxy'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/reverse-proxy
captured_at: '2026-11-01T21:24:23+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/reverse-proxy {#ipreverse-proxy}
**條件：** !smips
**型別：** 目錄

每條規則會把一個主機名的 HTTPS 請求轉發到 HTTP 伺服器。反向代理在 [`/ip/service`](./service/index.md) 中 `reverse-proxy` 服務的埠上接受 HTTPS 連線，選擇 `sni` 與用戶端傳送的伺服器名稱相匹配的規則，使用該規則的證書終止 TLS，並將請求以 HTTP 轉發到 `ip-address` 和 `port`。僅當至少存在一條已啟用的規則時，該服務埠才會開放。有關概覽和示例，請參見 [反向代理](../../network-management/proxy/reverse-proxy.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該規則已停用。新建規則建立時即為啟用狀態。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">該規則由 RouterOS 為具有 `use-https=yes` 和 Web 介面的容器應用建立（參見 [`/app`](../app/index.md)）。其 `sni` 是應用 URL 的主機名，其證書是在 `/app/settings` 中設定的證書。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="sni" typ="string" mandatory="1">該規則所服務的主機名。它會與用戶端在 TLS 握手期間傳送的伺服器名稱（SNI）進行比較，並且必須完全匹配；諸如 `*.example.com` 之類的萬用字元不會匹配任何內容。路由器會關閉伺服器名稱不匹配任何規則的連線，並且 `rproxy` 日誌會顯示 `no matching rule for <name>`。</ArgTableRow>
<ArgTableRow arg="ip-address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }" mandatory="1">請求所轉發到的伺服器的 IPv4 或 IPv6 地址。路由器會從自身地址發起連線，並將每個請求作為 HTTP/1.1 轉發。它會保留 `Host` 標頭，並新增包含用戶端地址的 `X-Forwarded-For` 和 `X-Real-Ip`，以及 `X-Forwarded-Proto: https`、`X-Forwarded-Host` 和 `Forwarded`。</ArgTableRow>
<ArgTableRow arg="port" typ="num" mandatory="1">伺服器的 TCP 埠。路由器始終使用純 HTTP 進行連線，即使埠為 443 也是如此，因此伺服器必須在此埠上接受 HTTP。</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)">此規則向用戶端出示的證書，例如為 `sni` 主機名簽發的證書。當為 `none` 時，將使用 [`/ip/service`](./service/index.md) 中 `reverse-proxy` 服務的證書。當該證書也為 `none` 時，TLS 握手會失敗，並且 `rproxy` 日誌會顯示 `certificate missing for rule <sni>`。預設值：none.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
</ArgTable>
