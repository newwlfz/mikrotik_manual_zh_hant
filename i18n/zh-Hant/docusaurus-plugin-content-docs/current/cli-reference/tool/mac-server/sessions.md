---
sidebar_key: "cli-reference/tool/mac-server/sessions"
sidebar_position: 3
title: "sessions"
sidebar_label: 'sessions'
source: https://manual.mikrotik.com/docs/cli-reference/tool/mac-server/sessions
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/mac-server/sessions {#toolmac-serversessions}
**型別：** 目錄

開啟到該路由器的 MAC Telnet 會話。MAC WinBox 連線不會列出。有關示例，請參閱 [MAC 伺服器](../../../management-tools/mac-server.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum">會話到達的介面。</ArgTableRow>
<ArgTableRow arg="src-address" typ="macAddr">用戶端的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">會話已開啟的時長。</ArgTableRow>
</ArgTable>
