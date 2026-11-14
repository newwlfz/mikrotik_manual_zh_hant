---
sidebar_key: "cli-reference/routing/pimsm/uib-sg"
sidebar_position: 9
title: "uib-sg"
sidebar_label: 'uib-sg'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/pimsm/uib-sg
captured_at: '2026-11-01T21:25:17+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/uib-sg {#routingpimsmuib-sg}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="K" typ="keepalive">keepalive</ArgTableRow>
<ArgTableRow arg="S" typ="spt-bit">最短路徑樹 (SPT) 位指示轉發是在 (S,G) 最短路徑樹上進行，還是在 (\*,G) 樹上進行。在源特定樹構建期間，路由器可以擁有 (S,G) 狀態，並且仍然在 (\*,G) 狀態上進行轉發。當 SPT 位為 false 時，僅使用 (\*,G) 轉發狀態來轉發從 S 到 G 的封包。當 SPT 位為 true 時，會同時使用 (\*,G) 和 (S,G) 轉發狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum">在其上建立組播組的 PIM 例項的名稱。</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46i)">組播組地址。</ArgTableRow>
<ArgTableRow arg="source" typ="address (flags=46i)">該組播組的源 IP 地址。</ArgTableRow>
<ArgTableRow arg="rpf" typ="address (flags=46i)">反向路徑轉發 (RPF) 指示該組的 Join 訊息發往的路由器地址和出介面。</ArgTableRow>
<ArgTableRow arg="register" typ="enum (join | join-pending | prune)"></ArgTableRow>
</ArgTable>
