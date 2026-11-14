---
sidebar_key: "cli-reference/ipv6/nd/settings"
sidebar_position: 3
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/nd/settings
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/nd/settings {#ipv6ndsettings}
**型別：** 設定目錄

IPv6 ND 選單有一個名為 "Settings" 的子選單，可用於更改全域性鄰居發現設定。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="router-advertisement-route-distance" typ="num">指定安裝 SLAAC 預設路由時必須使用的距離。</ArgTableRow>
<ArgTableRow arg="router-advertisement-ignored-options" typ="ubit (dns, mtu)">允許忽略接收到的特定 ND 選項，例如 DNS 和 MTU。如果 RA 包含此類選項，只要在此列表中選擇它們，它們就會被直接忽略。</ArgTableRow>
</ArgTable>
