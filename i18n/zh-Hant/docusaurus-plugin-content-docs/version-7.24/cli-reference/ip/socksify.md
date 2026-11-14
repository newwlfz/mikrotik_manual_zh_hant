---
sidebar_key: "cli-reference/ip/socksify"
sidebar_position: 24
title: "socksify"
sidebar_label: "socksify"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/socksify
captured_at: '2026-11-01T21:28:57+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/socksify {#ipsocksify}
**型別：** 目錄

完整文件請參閱 [Socksify](../../network-management/socks/socksify.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">disabled（預設設定）</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">Socksify 服務的名稱</ArgTableRow>
<ArgTableRow arg="connection-timeout" typ="num">連線建立期間等待 SOCKS 代理或目標響應的秒數，超時後將中止並報錯。設為 0 可停用超時（預設值：**60s**）</ArgTableRow>
<ArgTableRow arg="port" typ="num">Socksify 服務使用的 TCP 埠（預設值：**952**）</ArgTableRow>
<ArgTableRow arg="socks5-server" typ="ipAddr">SOCKS5 代理伺服器的 IP 地址，僅支援 IPv4（預設值：**0.0.0.0**）</ArgTableRow>
<ArgTableRow arg="socks5-port" typ="num">SOCKS5 代理伺服器的監聽埠（預設值：**1080**）</ArgTableRow>
<ArgTableRow arg="socks5-user" typ="string">用於訪問 SOCKS5 代理伺服器的使用者名稱</ArgTableRow>
<ArgTableRow arg="socks5-password" typ="string">用於訪問 SOCKS5 代理伺服器的密碼</ArgTableRow>
</ArgTable>
