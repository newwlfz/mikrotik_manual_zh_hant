---
sidebar_key: "cli-reference/cmr/layout/node"
sidebar_position: 3
title: "node"
sidebar_label: 'node'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/layout/node
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/layout/node {#cmrlayoutnode}
**軟體包：** cmr
**型別：** 目錄

特定拓撲節點的配置。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">節點名稱。</ArgTableRow>
<ArgTableRow arg="layout" typ="enum" mandatory="1">節點將顯示在其中的佈局名稱。</ArgTableRow>
<ArgTableRow arg="device" typ="enum" unset="1">節點將在拓撲中表示的裝置名稱。與 `target-layout` 引數互斥。</ArgTableRow>
<ArgTableRow arg="target-layout" typ="enum" unset="1">節點將在拓撲中表示的佈局名稱。與 `device` 引數互斥。</ArgTableRow>
<ArgTableRow arg="x" typ="num" unset="1">節點在拓撲中的 X 座標。預設 X 值在每次新增新節點時遞增 200，以防止在未指定座標時發生重疊。（預設值：**0+200*n**）</ArgTableRow>
<ArgTableRow arg="y" typ="num" unset="1">節點在拓撲中的 Y 座標。（預設值：**0**）</ArgTableRow>
</ArgTable>
