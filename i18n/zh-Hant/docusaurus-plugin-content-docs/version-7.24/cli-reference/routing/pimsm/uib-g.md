---
sidebar_key: "cli-reference/routing/pimsm/uib-g"
sidebar_position: 8
title: "uib-g"
sidebar_label: "uib-g"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/routing/pimsm/uib-g
captured_at: '2026-11-01T21:29:39+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/uib-g {#routingpimsmuib-g}
**條件：** !smips
**型別：** 目錄

上游資訊庫選單顯示任意源組播（\*,G）和源特定組播（S,G）組及其狀態。這些選單僅包含只讀條目。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="R" typ="rp-local">rp-local</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum">在其上建立多播組的 PIM 例項的名稱。</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46i)">多播組地址。</ArgTableRow>
<ArgTableRow arg="rp" typ="address (flags=46i)">該組的 Rendezvous Point 地址。</ArgTableRow>
<ArgTableRow arg="rpf" typ="address (flags=46i)">反向路徑轉發（RPF）指示該組的 Join 訊息所指向的路由器地址和出介面。</ArgTableRow>
<ArgTableRow arg="rp-local" typ="bool">指示多播路由器本身是否為 RP。</ArgTableRow>
</ArgTable>
