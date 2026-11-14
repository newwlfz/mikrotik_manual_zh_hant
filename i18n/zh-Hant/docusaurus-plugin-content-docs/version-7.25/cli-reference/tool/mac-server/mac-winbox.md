---
sidebar_key: "cli-reference/tool/mac-server/mac-winbox"
sidebar_position: 1
title: "mac-winbox"
sidebar_label: 'mac-winbox'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/mac-server/mac-winbox
captured_at: '2026-11-01T21:25:55+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/mac-server/mac-winbox {#toolmac-servermac-winbox}
**型別：** 設定目錄

MAC WinBox 伺服器設定：指定 WinBox 可以透過哪些介面使用 MAC 地址連線到路由器。MAC Telnet 在 [`/tool/mac-server`](./index.md) 中有自己的設定。有關示例，請參閱 [MAC 伺服器](../../../management-tools/mac-server.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="allowed-interface-list" typ="enum">路由器接受 MAC WinBox 連線的介面列表，其設定方式與 [`/tool/mac-server`](./index.md) 中的 MAC Telnet 相同：應把網橋加入列表，而不是它的埠。`none` 會關閉 MAC WinBox。預設配置設定為 `LAN`。預設值：all。</ArgTableRow>
</ArgTable>
