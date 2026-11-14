---
sidebar_key: "cli-reference/routing/pimsm/uib-g"
sidebar_position: 8
title: "uib-g"
sidebar_label: 'uib-g'
source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/uib-g
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/uib-g {#routingpimsmuib-g}
**條件：** !smips
**型別：** 目錄

上游資訊庫選單顯示任意源組播（\*,G）和源特定組播（S,G）組及其狀態。這些選單僅包含只讀條目。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="R" typ="rp-local">該路由器本身是該組的 Rendezvous Point（RP）。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum">建立該組播組所在的 PIM 例項名稱。</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46i)">組播組地址。</ArgTableRow>
<ArgTableRow arg="rp" typ="address (flags=46i)">該組的 Rendezvous Point 地址。</ArgTableRow>
<ArgTableRow arg="rpf" typ="address (flags=46i)">反向路徑轉發（RPF）指示該組播組的 Join 訊息所指向的路由器地址和出介面。</ArgTableRow>
</ArgTable>
