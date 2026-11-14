---
sidebar_key: "cli-reference/routing/settings"
sidebar_position: 17
title: "settings"
sidebar_label: "settings"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/settings
captured_at: '2026-11-01T21:29:41+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/settings {#routingsettings}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="single-process" typ="bool">啟用後，所有與路由相關的程式會合併為一個路由程式，以減少 RAM 使用量。停用後，與路由相關的程式會分別執行，在某些設定中可以提高效能和穩定性。預設情況下，僅對 RAM 為 64 MB 或更少的裝置啟用 single-process。需要重啟才能使此更改生效。</ArgTableRow>
<ArgTableRow arg="dynamic-in-chain" typ="enum" unset="1">用於處理所有動態新增路由的鏈的名稱。</ArgTableRow>
<ArgTableRow arg="connected-in-chain" typ="enum" unset="1">用於處理 `connected` 路由的鏈的名稱。</ArgTableRow>
<ArgTableRow arg="check-gateway-ping-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="check-gateway-ping-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="check-gateway-ping-count" typ="num"></ArgTableRow>
<ArgTableRow arg="policy-rules" typ="object { chain: enum
 }">定義路由決策規則的順序。預設情況下，`user` 是新增使用者定義 `/routing/rule` 條目的鏈。你可以在列表中的任意位置新增自定義鏈。</ArgTableRow>
</ArgTable>
