---
sidebar_key: "cli-reference/caps-man/manager/index"
sidebar_position: 1
title: "manager"
sidebar_label: "manager"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/caps-man/manager
captured_at: '2026-11-01T21:26:21+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
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
