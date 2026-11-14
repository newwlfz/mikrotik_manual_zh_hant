---
sidebar_key: "cli-reference/ip/dns/forwarders"
sidebar_position: 3
title: "forwarders"
sidebar_label: "forwarders"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/dns/forwarders
captured_at: '2026-11-01T21:28:31+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dns/forwarders {#ipdnsforwarders}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="dns-servers" typ="multi { address (flags=46D)
 }"></ArgTableRow>
<ArgTableRow arg="doh-servers" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="verify-doh-cert" typ="bool"></ArgTableRow>
</ArgTable>
