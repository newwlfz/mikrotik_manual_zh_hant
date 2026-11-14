---
sidebar_key: "cli-reference/cmr/device/dashboard"
sidebar_position: 2
title: "dashboard"
sidebar_label: 'dashboard'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/device/dashboard
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/device/dashboard {#cmrdevicedashboard}
**包：** cmr  
**型別：** 命令

開啟所選裝置的即時檢視：裝置、資源、介面、曲線以及 AP/站點資料。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="labels" typ="object" unset="1">使用 labels 選擇要在儀表板中顯示的裝置。支援 + 和 - 符號分別作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。</ArgTableRow>
</ArgTable>
