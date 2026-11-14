---
sidebar_key: "cli-reference/tool/mac-server/ping"
sidebar_position: 2
title: "ping"
sidebar_label: 'ping'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/mac-server/ping
captured_at: '2026-11-01T21:25:55+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/mac-server/ping {#toolmac-serverping}
**型別：**設定目錄

MAC ping 伺服器設定。啟用伺服器後，路由器會應答傳送到其 MAC 地址的 ping（`/ping <MAC address>`）。有關示例，請參見 [MAC 伺服器](../../../management-tools/mac-server.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">路由器是否應答 MAC ping。路由器自身的 MAC ping 也需要它：伺服器停用時，這些 ping 會失敗並顯示狀態 `unknown interface`。ARP ping 不依賴此設定。預設值：是。</ArgTableRow>
</ArgTable>
