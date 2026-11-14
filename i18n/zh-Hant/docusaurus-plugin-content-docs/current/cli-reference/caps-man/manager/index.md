---
sidebar_key: "cli-reference/caps-man/manager"
title: "manager"
sidebar_label: 'manager'
source: https://manual.mikrotik.com/docs/cli-reference/caps-man/manager
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## caps-man/manager {#caps-manmanager}
**軟體包：** wireless-rep
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none | auto) { auto:0 }"></ArgTableRow>
<ArgTableRow arg="ca-certificate" typ="enum (none | auto) { auto:0 }"></ArgTableRow>
<ArgTableRow arg="package-path" typ="string"></ArgTableRow>
<ArgTableRow arg="upgrade-policy" typ="enum (none | suggest-same-version | require-same-version)"></ArgTableRow>
<ArgTableRow arg="require-peer-certificate" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="generated-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="generated-ca-certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>
