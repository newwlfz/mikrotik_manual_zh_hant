---
sidebar_key: "cli-reference/tool/mac-server/index"
sidebar_position: 1
title: "mac-server"
sidebar_label: 'mac-server'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/mac-server
captured_at: '2026-11-01T21:25:55+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/mac-server {#toolmac-server}
**型別：** 設定目錄

MAC Telnet 伺服器設定。MAC 伺服器允許同一 layer-2 網段上的裝置透過其 MAC 地址訪問路由器，而無需 IP 配置：MAC Telnet（此選單）、MAC WinBox（[`/tool/mac-server/mac-winbox`](./mac-winbox.md)）和 MAC ping（[`/tool/mac-server/ping`](./ping.md)）。已開啟的 MAC Telnet 會話列在 [`/tool/mac-server/sessions`](./sessions.md) 中。IP 防火牆不會阻止 MAC 訪問；請使用 `allowed-interface-list` 限制它。示例請參閱 [MAC 伺服器](../../../management-tools/mac-server.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="allowed-interface-list" typ="enum">路由器接受 MAC Telnet 連線的介面列表。列表中的網橋也允許透過其埠到達的連線；僅將網橋埠加入列表則不允許。`none`，或沒有成員的列表，會關閉 MAC Telnet。更改會立即應用於下一個連線；已開啟的會話保持不變。預設配置設定為 `LAN`。預設值：all。</ArgTableRow>
</ArgTable>
