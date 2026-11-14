---
sidebar_key: "cli-reference/cmr/layout/link"
sidebar_position: 2
title: "link"
sidebar_label: 'link'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/layout/link
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/layout/link {#cmrlayoutlink}
**軟體包：** cmr
**型別：** 目錄

用於拓撲中特定鏈路的配置。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="layout" typ="enum" mandatory="1">連結將顯示所在佈局的名稱。</ArgTableRow>
<ArgTableRow arg="node1" typ="enum" mandatory="1">鏈路中第一個節點的名稱。</ArgTableRow>
<ArgTableRow arg="node2" typ="enum" mandatory="1">鏈路中第二個節點的名稱。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="links" typ="multi { array-id, array-id, link: super { port1: object
, [port2] --object
 }
 }">有關鏈路狀態的詳細資訊，例如 PoE 狀態、介面名稱和流量資訊。埠名稱前的 `*` 表示直連的物理鏈路。示例：`ether1(,tx=85.9KiB,rx=10.8KiB)--ether23(poe=powered-on,tx=10.9KiB,rx=86.8KiB)`</ArgTableRow>
</ArgTable>
