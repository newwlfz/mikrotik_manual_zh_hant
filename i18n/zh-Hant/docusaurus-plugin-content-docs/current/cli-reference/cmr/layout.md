---
sidebar_key: "cli-reference/cmr/layout"
title: "layout"
source: https://manual.mikrotik.com/docs/cli-reference/cmr/layout
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/layout {#cmrlayout}
**包：** cmr
**型別：** 目錄

拓撲配置；拓撲本身只能在 GUI 中顯示，無法在 CLI 中顯示。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">佈局/拓撲的名稱。</ArgTableRow>
<ArgTableRow arg="scale" typ="num" unset="1">背景圖片縮放百分比。預設值：100。</ArgTableRow>
<ArgTableRow arg="file" typ="string" unset="1">背景圖片選擇。</ArgTableRow>
</ArgTable>
