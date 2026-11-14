---
sidebar_key: "cli-reference/routing/rule"
sidebar_position: 16
title: "rule"
sidebar_label: 'rule'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/rule
captured_at: '2026-11-01T21:25:20+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/rule {#routingrule}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="address (flags=64iv/)" unset="1">要匹配的源地址。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=64iv/)" unset="1">要匹配的目標地址。</ArgTableRow>
<ArgTableRow arg="routing-mark" typ="enum" unset="1">匹配特定的路由標記。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" unset="1">要匹配的入介面。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (lookup | lookup-only-in-table | unreachable | drop | mangle)">
對匹配封包執行的操作：
- drop - 靜默丟棄封包。
- lookup - 在路由表中執行查詢。
- lookup-only-in-table - 僅在指定的路由表中執行查詢（參見 `table` 引數）。
- unreachable - 生成 ICMP 不可達訊息併發送給源。
- mangle - 按防火牆 mangle 規則執行操作。
</ArgTableRow>
<ArgTableRow arg="table" typ="enum (local) { local:4095 }">用於查詢的路由表名稱。</ArgTableRow>
<ArgTableRow arg="min-prefix" typ="num" unset="1">隱藏路由表中具有指定字首長度的路由，使其不用於此路由規則處理的封包。這等同於 Linux IP 規則 `suppress_prefixlength`。例如，將值設定為 0 以在路由決策中抑制預設路由。</ArgTableRow>
<ArgTableRow arg="vrf" typ="switch"></ArgTableRow>
<ArgTableRow arg="realm" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="chain" typ="enum" unset="1">路由決策規則使用的鏈名稱。預設情況下，未指定鏈時使用 `user`。如果鏈名稱與內建路由決策名稱匹配，則使用者建立的規則會新增到該決策之後。例如，如果 `chain=mangle`，則此鏈中使用者建立的規則位於 `mangle` 決策之後。</ArgTableRow>
</ArgTable>
