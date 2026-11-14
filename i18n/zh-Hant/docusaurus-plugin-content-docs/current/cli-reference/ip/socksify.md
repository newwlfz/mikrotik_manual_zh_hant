---
sidebar_key: "cli-reference/ip/socksify"
sidebar_position: 24
title: "socksify"
sidebar_label: 'socksify'
source: https://manual.mikrotik.com/docs/cli-reference/ip/socksify
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/socksify {#ipsocksify}
**型別：** 目錄

該服務會將防火牆 NAT 規則（`action=socksify`，通常位於 `dstnat` 鏈中）重定向到它的流量，透過上游 SOCKS5 伺服器轉發。修改記錄屬性後，需要先停用再重新啟用該記錄才會生效。

完整文件請參閱 [Socksify](../../network-management/socks/socksify.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">disabled（預設設定）</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">socksify 服務記錄的名稱。</ArgTableRow>
<ArgTableRow arg="connection-timeout" typ="num">連線建立期間等待 SOCKS 伺服器和目標的時間，單位為秒（0 到 3000），超時後將以錯誤中止。設定為 0 可停用超時。預設值：`60`。</ArgTableRow>
<ArgTableRow arg="port" typ="num">服務監聽的本地 TCP 埠；`socksify` NAT 動作會將截獲的連線重定向到此埠。預設值：`952`。</ArgTableRow>
<ArgTableRow arg="socks5-server" typ="ipAddr">上游 SOCKS5 伺服器的 IPv4 地址。不接受 IPv6 地址。預設值：`0.0.0.0`。</ArgTableRow>
<ArgTableRow arg="socks5-port" typ="num">SOCKS5 伺服器的監聽埠。預設值：`1080`。</ArgTableRow>
<ArgTableRow arg="socks5-user" typ="string">上游 SOCKS5 伺服器的使用者名稱。在 `print detail` 輸出中以明文顯示。預設值：空。</ArgTableRow>
<ArgTableRow arg="socks5-password" typ="string">上游 SOCKS5 伺服器的密碼。在 `print detail` 輸出中以明文顯示。預設值：空。</ArgTableRow>
</ArgTable>
