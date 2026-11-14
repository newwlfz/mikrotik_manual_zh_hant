---
sidebar_key: "cli-reference/routing/pimsm/static-rp"
sidebar_position: 7
title: "static-rp"
sidebar_label: 'static-rp'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/pimsm/static-rp
captured_at: '2026-11-01T21:25:19+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/static-rp {#routingpimsmstatic-rp}
**條件：** !smips
**型別：** 目錄

static-rp 選單允許手動定義多播組到 RP 的對映。此類機制對故障並不具備魯棒性，但至少提供了一種基本的互操作機制。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum" mandatory="1">此靜態 RP 所屬的 PIM 例項的名稱。</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46/)">屬於特定 RP 的多播組。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">靜態 RP 的 IP 地址。</ArgTableRow>
</ArgTable>
