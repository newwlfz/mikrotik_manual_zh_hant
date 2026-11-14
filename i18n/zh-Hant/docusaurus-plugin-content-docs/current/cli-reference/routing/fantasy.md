---
sidebar_key: "cli-reference/routing/fantasy"
sidebar_position: 4
title: "fantasy"
sidebar_label: 'fantasy'
source: https://manual.mikrotik.com/docs/cli-reference/routing/fantasy
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/fantasy {#routingfantasy}
**型別：** 目錄

Fantasy 選單是一種用於測試目的生成大量路由的巧妙方式。與指令碼相比，這種方法的主要優點是生成速度快且簡單。只需停用 fantasy 規則，就可以輕鬆刪除所有由 fantasy 生成的路由。

Fantasy 使用基於雜湊後的路由序列號、種子和其他引數的隨機生成器。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46it/)">將從中生成路由的字首。</ArgTableRow>
<ArgTableRow arg="prefix-length" typ="range">生成路由的字首長度（可指定為整數範圍）。例如，`dst-address=192.168.0.0/16` 和 `prefix-length=24` 將從 `192.168.0.0/16` 子網生成 /24 路由。</ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=46iv/)"></ArgTableRow>
<ArgTableRow arg="scope" typ="range">要設定的 scope；可設定為範圍。</ArgTableRow>
<ArgTableRow arg="target-scope" typ="range">要設定的 target-scope；可設定為範圍。</ArgTableRow>
<ArgTableRow arg="instance-id" typ="range"></ArgTableRow>
<ArgTableRow arg="dealer-id" typ="range"></ArgTableRow>
<ArgTableRow arg="seed" typ="string">隨機生成器種子。</ArgTableRow>
<ArgTableRow arg="count" typ="num"></ArgTableRow>
<ArgTableRow arg="offset" typ="num">路由序列號偏移。</ArgTableRow>
<ArgTableRow arg="priv-offs" typ="range"></ArgTableRow>
<ArgTableRow arg="priv-size" typ="range"></ArgTableRow>
<ArgTableRow arg="use-hold" typ="bool"></ArgTableRow>
</ArgTable>
