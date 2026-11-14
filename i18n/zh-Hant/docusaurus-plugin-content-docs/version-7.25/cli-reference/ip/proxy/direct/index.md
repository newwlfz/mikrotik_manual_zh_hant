---
sidebar_key: "cli-reference/ip/proxy/direct/index"
sidebar_position: 1
title: "direct"
sidebar_label: 'direct'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/proxy/direct
captured_at: '2026-11-01T21:24:23+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/direct {#ipproxydirect}
**型別：** 目錄

當在 [`/ip/proxy`](../index.md) 中透過 `parent-proxy` 和 `parent-proxy-port` 設定父代理時，這些規則決定哪些請求直接發往伺服器。代理會從上到下檢查規則，第一條匹配的規則決定結果。未匹配任何規則的請求會經過父代理。未設定父代理時，每個請求都直接發往伺服器，此列表不會生效。匹配器的用法與 [`/ip/proxy/access`](../access/index.md) 中相同。在匹配器值前加上 `!` 可將其取反，例如 `src-address=!192.168.88.0/24`。有關示例，請參見 [Web 代理](../../../../network-management/proxy/web-proxy.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">disabled。該規則不被使用。新建的規則建立時為啟用狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="super { !
, range: alt { ip4: ipRange
, ip6: ip6Prefix
 }
 }">用戶端地址：IPv4 地址、範圍或字首，或 IPv6 字首。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, range: alt { ip4: ipRange
, ip6: ip6Prefix
 }
 }">代理連線到的伺服器地址，即請求中主機名解析得到的地址。格式與 `src-address` 相同。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, ports: multi { ports: range [ .. 65535]
 }
 }">伺服器埠；對於 HTTPS 請求，為 `CONNECT` 隧道的埠。可以是單個埠、範圍或用逗號分隔的列表，例如 `dst-port=!443`。</ArgTableRow>
<ArgTableRow arg="local-port" typ="super { !
, port: num [0 .. 65535]
 }">請求到達時所使用的代理埠。當 [`/ip/proxy`](../index.md) 中的 `port` 列出多個埠時使用。</ArgTableRow>
<ArgTableRow arg="dst-host" typ="super { !
, host: string
 }">
請求的主機名；對於 HTTPS 請求，為 `CONNECT` 隧道的主機。該值必須匹配完整名稱，並且不區分大小寫，因此 `example.com` 不匹配 `www.example.com`。
- 萬用字元：`*` 匹配任意字元，`?` 匹配單個字元，例如 `*.example.com`。
- 以 `:` 開頭的值是正則表示式，可以匹配名稱的任意部分：`:mail` 匹配 `mail.example.com`。用 `^` 和 `$` 錨定，例如 `:^www`。
</ArgTableRow>
<ArgTableRow arg="path" typ="super { !
, path: string
 }">
所請求 URL 的路徑，包括查詢字串，例如 `/music/a.mp3?x=1`。萬用字元和正則表示式的用法與 `dst-host` 相同。
- 萬用字元必須匹配包括查詢字串在內的完整路徑，因此 `*.mp3` 匹配 `/music/a.mp3`，但不匹配 `/music/a.mp3?x=1`。
- 路徑始終以 `/` 開頭，因此路由器會拒絕諸如 `music/*` 這樣的值，因為它永遠無法匹配。
- HTTPS 請求沒有路徑，因此帶 `path` 的規則永遠不會匹配這類請求。
</ArgTableRow>
<ArgTableRow arg="method" typ="super { !
, method: enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE)
 }">請求的 HTTP 方法：`GET`、`HEAD`、`POST`、`PUT`、`CONNECT`、`OPTIONS`、`DELETE` 或 `TRACE`。代理用戶端使用 `CONNECT` 請求 HTTPS 頁面。這些方法定義於 [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110#name-methods)。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (allow | deny)">
代理如何傳送匹配的請求。
- `allow`（預設）- 直接連線到伺服器。
- `deny` - 透過父代理傳送請求。
</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hits" typ="num">該規則匹配的請求數。可使用 [`reset-counters`](./reset-counters.md) 或 [`reset-counters-all`](./reset-counters-all.md) 重設。</ArgTableRow>
</ArgTable>
