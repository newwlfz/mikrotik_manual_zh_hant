---
sidebar_key: "cli-reference/interface/bonding/monitor-slaves"
sidebar_position: 1
title: "monitor-slaves"
sidebar_label: 'monitor-slaves'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/bonding/monitor-slaves
captured_at: '2026-11-01T21:22:20+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/bonding/monitor-slaves {#interfacebondingmonitor-slaves}
**型別：** 命令

該命令用於監控單個 bonding 埠。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="A" typ="active">已啟用</ArgTableRow>
<ArgTableRow arg="P" typ="partner">partner</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="bond" typ="iface_enum">要監控的 bonding 介面。</ArgTableRow>
<ArgTableRow arg="once" typ="bool">僅顯示一次監控輸出，而不是持續顯示。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="port" typ="iface_enum">使用的 bonding 埠。</ArgTableRow>
<ArgTableRow arg="key" typ="num">顯示本地 LACP 聚合鍵。低 6 位會根據各個埠的鏈路速率和雙工模式自動分配。高 10 位可以使用 lacp-user-key 設定手動指定。</ArgTableRow>
<ArgTableRow arg="flags" typ="string">
顯示本地 LACP 標誌。
- A - activity（鏈路處於活動狀態）。
- T - timeout（鏈路正在使用短超時）。
- G - aggregation（鏈路可聚合）。
- S - synchronization（鏈路已同步）。
- C - collecting（鏈路能夠收集傳入幀）。
- D - distributing（鏈路能夠分發傳出幀）。
- F - defaulted（鏈路正在使用預設的對端資訊）。
- E - expired（鏈路處於過期狀態）。
</ArgTableRow>
<ArgTableRow arg="partner-sys-id" typ="macAddr">顯示對端 LACP 系統 ID。</ArgTableRow>
<ArgTableRow arg="partner-sys-priority" typ="num">顯示對端 LACP 優先順序。</ArgTableRow>
<ArgTableRow arg="partner-key" typ="num">顯示對端 LACP 聚合鍵。</ArgTableRow>
<ArgTableRow arg="partner-flags" typ="string">顯示對端 LACP 標誌。</ArgTableRow>
</ArgTable>
