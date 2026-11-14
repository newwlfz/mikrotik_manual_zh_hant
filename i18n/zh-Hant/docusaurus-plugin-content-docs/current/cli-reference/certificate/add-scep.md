---
sidebar_key: "cli-reference/certificate/add-scep"
sidebar_position: 3
title: "add-scep"
sidebar_label: 'add-scep'
source: https://manual.mikrotik.com/docs/cli-reference/certificate/add-scep
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## certificate/add-scep {#certificateadd-scep}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="ca-identity" typ="string"></ArgTableRow>
<ArgTableRow arg="template" typ="enum"></ArgTableRow>
<ArgTableRow arg="scep-url" typ="string"></ArgTableRow>
<ArgTableRow arg="challenge-password" typ="string"></ArgTableRow>
<ArgTableRow arg="on-smart-card" typ="bool">如果硬體支援，將私鑰儲存在智慧卡上</ArgTableRow>
<ArgTableRow arg="refresh" typ="bool">檢查證書到期時間，如果已到期則重新整理</ArgTableRow>
</ArgTable>
