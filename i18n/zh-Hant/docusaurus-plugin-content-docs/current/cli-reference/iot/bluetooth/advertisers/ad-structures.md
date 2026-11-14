---
sidebar_key: "cli-reference/iot/bluetooth/advertisers/ad-structures"
sidebar_position: 1
title: "ad-structures"
sidebar_label: 'ad-structures'
source: https://manual.mikrotik.com/docs/cli-reference/iot/bluetooth/advertisers/ad-structures
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## iot/bluetooth/advertisers/ad-structures {#iotbluetoothadvertisersad-structures}
**包：** iot
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (short-local-name | complete-local-name | service-data | manufacturer-data) { short-local-name:8, complete-local-name:9, service-data:22, manufacturer-data:255 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="data" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>
