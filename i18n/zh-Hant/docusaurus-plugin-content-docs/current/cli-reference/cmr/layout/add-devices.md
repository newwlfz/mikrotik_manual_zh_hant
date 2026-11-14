---
sidebar_key: "cli-reference/cmr/layout/add-devices"
sidebar_position: 1
title: "add-devices"
sidebar_label: 'add-devices'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/layout/add-devices
captured_at: '2026-11-09T11:35:47.715Z'
pagination_prev: "cli-reference/cmr/layout"
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/layout/add-devices {#cmrlayoutadd-devices}
**包：** cmr
**型別：** Command

此命令將多個裝置批次新增到拓撲中。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="labels" typ="object" unset="1">選擇應使用標籤新增到拓撲中的裝置。支援 + 和 - 符號分別作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。（預設值：**all**）</ArgTableRow>
<ArgTableRow arg="devices" typ="multi { array-id, device: enum
 }" unset="1">選擇應新增到拓撲中的特定裝置。</ArgTableRow>
</ArgTable>
