---
sidebar_key: "cli-reference/cmr/device/pair"
sidebar_position: 3
title: "pair"
sidebar_label: 'pair'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/device/pair
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/device/pair {#cmrdevicepair}
**軟體包：** cmr
**型別：** Command

開始與所選裝置進行配對。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="labels" typ="object" unset="1">選擇要使用 labels 配對的裝置。支援 + 和 - 符號分別作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。</ArgTableRow>
<ArgTableRow arg="username" typ="string" unset="1">當裝置需要時用於配對的使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string" unset="1">當裝置需要時用於配對的密碼。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum">正在配對的裝置。</ArgTableRow>
<ArgTableRow arg="status" typ="string">配對狀態。</ArgTableRow>
</ArgTable>
