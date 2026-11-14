---
sidebar_key: "cli-reference/cmr/layout/rebuild-links"
sidebar_position: 4
title: "rebuild-links"
sidebar_label: 'rebuild-links'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/layout/rebuild-links
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/layout/rebuild-links {#cmrlayoutrebuild-links}
**包：** cmr
**型別：** Command

如果拓撲中節點之間的鏈路已被刪除或最初未生成，此命令會根據埠資料自動生成這些鏈路。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="labels" typ="object" unset="1">使用標籤選擇應重建鏈路的裝置。支援 + 和 - 符號分別作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。（預設值：**all**）</ArgTableRow>
<ArgTableRow arg="devices" typ="multi { array-id, device: enum
 }" unset="1">選擇應重建鏈路的具體裝置。</ArgTableRow>
</ArgTable>
