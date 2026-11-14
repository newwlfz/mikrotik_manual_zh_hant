---
sidebar_key: "cli-reference/ip/cloud/back-to-home-file/settings/index"
sidebar_position: 1
title: "settings"
sidebar_label: "settings"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/cloud/back-to-home-file/settings
captured_at: '2026-11-01T21:28:24+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/cloud/back-to-home-file/settings {#ipcloudback-to-home-filesettings}
**系統能力：** cloud-vpn
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="prefer-relay-code" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="dns-name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="relay-rtts" typ="multi { code: string
 }"></ArgTableRow>
<ArgTableRow arg="relay-ipv4-status" typ="string"></ArgTableRow>
<ArgTableRow arg="relay-ipv6-status" typ="string"></ArgTableRow>
<ArgTableRow arg="relay-regions" typ="multi { code: string
 }"></ArgTableRow>
<ArgTableRow arg="relay-addresses" typ="multi { address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="relay-addresses-ipv6" typ="multi { address: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>
