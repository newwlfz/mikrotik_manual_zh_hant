---
sidebar_key: "cli-reference/ip/socks/index"
sidebar_position: 3
title: "socks"
sidebar_label: 'socks'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/socks
captured_at: '2026-11-01T21:24:25+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/socks {#ipsocks}
**型別：** 設定目錄

SOCKS 代理伺服器在其 TCP 埠上接受 SOCKS 用戶端連線，並將其轉發到請求的目標，同時應用 [`access`](./access.md) 規則，並可選擇使用 [`users`](./users.md) 身份驗證。更多資訊，請參見 [SOCKS](../../../network-management/socks/index.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">SOCKS 代理伺服器是否執行。預設值：`no`。</ArgTableRow>
<ArgTableRow arg="port" typ="num">代理監聽的 TCP 埠。預設值：`1080`。</ArgTableRow>
<ArgTableRow arg="connection-idle-timeout" typ="time">空閒代理連線在被終止前等待的時間。預設值：`2m`。</ArgTableRow>
<ArgTableRow arg="max-connections" typ="num">同時代理連線的最大數量，`1` 到 `500`。預設值：`200`。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">代理監聽的 VRF。如果使用 `main` 以外的 VRF，則該埠只能在該 VRF 內部訪問。預設值：`main`。</ArgTableRow>
<ArgTableRow arg="version" typ="enum (4 | 5)">
伺服器接受的 SOCKS 協定版本。
- `4`（預設）- 僅接受 SOCKS4 用戶端。
- `5` - 僅接受 SOCKS5 用戶端。密碼身份驗證以及 [`socksify`](../socksify.md) 服務需要此版本，該服務始終使用 SOCKS5。
</ArgTableRow>
<ArgTableRow arg="auth-method" typ="enum (none | password)">
伺服器要求用戶端使用的身份驗證方式。
- `none`（預設）- 無身份驗證。
- `password` - 用戶端必須使用 [`users`](./users.md) 中的使用者名稱和密碼進行身份驗證。如果不存在任何使用者，則拒絕所有連線。
</ArgTableRow>
</ArgTable>
