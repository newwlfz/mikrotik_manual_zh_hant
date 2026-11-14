---
sidebar_key: "cli-reference/interface/wifi/capsman/index"
sidebar_position: 1
title: "capsman"
sidebar_label: "capsman"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/wifi/capsman
captured_at: '2026-11-01T21:27:46+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wifi/capsman {#interfacewificapsman}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="enum (yes | no)"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface: iface_enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ca-certificate" typ="enum (auto | none) { auto:0 }" unset="1"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (auto) { auto:0 }" unset="1"></ArgTableRow>
<ArgTableRow arg="require-peer-certificate" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="package-path" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="upgrade-policy" typ="enum (none | suggest-same-version | require-same-version)" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="generated-ca-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="generated-certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>
