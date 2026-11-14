---
sidebar_key: "cli-reference/ip/proxy/access/index"
sidebar_position: 1
title: "access"
sidebar_label: 'access'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/proxy/access
captured_at: '2026-11-01T21:24:19+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/access {#ipproxyaccess}
**型別：** 目錄

用於允許、拒絕、重定向或修改代理用戶端請求的規則，HTTP 和 HTTPS（`CONNECT`）請求均適用。代理會從上到下依次檢查規則，由第一條匹配的規則做出決定。不匹配任何規則的請求將被允許。沒有匹配條件的規則會匹配所有請求。在匹配條件的值前加上 `!` 可對其取反，例如 `src-address=!192.168.88.0/24`。有關示例，請參見 [Web 代理](../../../../network-management/proxy/web-proxy.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">disabled。該規則不被使用。新建的規則建立時為啟用狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="super { !
, range: alt { ip4: ipRange
, ip6: ip6Prefix
 }
 }">用戶端的地址：IPv4 地址、範圍或字首，或 IPv6 字首。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, range: alt { ip4: ipRange
, ip6: ip6Prefix
 }
 }">代理連線到的伺服器地址，即請求中主機名解析後的地址。格式與 `src-address` 相同。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, ports: multi { ports: range [ .. 65535]
 }
 }">伺服器的埠；對於 HTTPS 請求，是 `CONNECT` 隧道的埠。可以是單個埠、範圍或用逗號分隔的列表，例如 `dst-port=!443`。</ArgTableRow>
<ArgTableRow arg="local-port" typ="super { !
, port: num [0 .. 65535]
 }">請求到達時所使用的代理埠。當 [`/ip/proxy`](../index.md) 中的 `port` 列出多個埠時使用。</ArgTableRow>
<ArgTableRow arg="dst-host" typ="super { !
, host: string
 }">
請求的主機名；對於 HTTPS 請求，是 `CONNECT` 隧道的主機。該值必須匹配完整名稱，且不區分大小寫，因此 `example.com` 不匹配 `www.example.com`。
- 萬用字元：`*` 匹配任意字元，`?` 匹配一個字元，例如 `*.example.com`。
- 以 `:` 開頭的值是正則表示式，可以匹配名稱的任意部分：`:mail` 匹配 `mail.example.com`。使用 `^` 和 `$` 將其錨定，例如 `:^www`。
</ArgTableRow>
<ArgTableRow arg="path" typ="super { !
, path: string
 }">
所請求 URL 的路徑，包括查詢字串，例如 `/music/a.mp3?x=1`。萬用字元和正則表示式的用法與 `dst-host` 中相同。
- 萬用字元必須匹配包括查詢字串在內的整個路徑，因此 `*.mp3` 匹配 `/music/a.mp3`，但不匹配 `/music/a.mp3?x=1`。
- 路徑始終以 `/` 開頭，因此路由器會拒絕 `music/*` 這樣的值，因為它永遠無法匹配。
- HTTPS 請求沒有路徑，因此帶有 `path` 的規則永遠不會匹配它們。
</ArgTableRow>
<ArgTableRow arg="method" typ="super { !
, method: enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE)
 }">請求的 HTTP 方法：`GET`、`HEAD`、`POST`、`PUT`、`CONNECT`、`OPTIONS`、`DELETE` 或 `TRACE`。代理用戶端使用 `CONNECT` 請求 HTTPS 頁面。這些方法定義於 [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110#name-methods)。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (allow | deny | redirect | url-append)">
代理對匹配請求執行的操作。
- `allow`（預設） - 將請求繼續傳遞。
- `deny` - 返回 HTTP 403 錯誤頁面。
- `redirect` - 返回 HTTP 307，並將 `action-data` 中的 URL 作為新位置。
- `url-append` - 將 `action-data` 中的文字新增到所請求 URL 的末尾（位於路徑和查詢字串之後），並繼續傳遞請求。
</ArgTableRow>
<ArgTableRow arg="action-data" typ="string">重定向 URL/追加 URL。當 `action=redirect` 時，是用戶端被髮送到的 URL，例如 `http://intranet.example.com/blocked.html`。當 `action=url-append` 時，是新增到所請求 URL 末尾的文字，按原樣新增，不帶分隔符。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hits" typ="num">該規則匹配的請求數。可使用 [`reset-counters`](../direct/reset-counters.md) 或 [`reset-counters-all`](../direct/reset-counters-all.md) 重設。</ArgTableRow>
</ArgTable>
