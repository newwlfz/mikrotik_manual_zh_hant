---
sidebar_key: "cli-reference/ip/firewall/service-port"
sidebar_position: 9
title: "service-port"
sidebar_label: "service-port"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/firewall/service-port
captured_at: '2026-11-01T21:28:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/firewall/service-port {#ipfirewallservice-port}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ports" typ="multi { port: num [0 .. 65535]
 }">服務使用的埠號。</ArgTableRow>
<ArgTableRow arg="sip-direct-media" typ="bool">是否啟用 SIP 直連媒體。</ArgTableRow>
<ArgTableRow arg="sip-timeout" typ="time">SIP 超時值。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">服務名稱。</ArgTableRow>
</ArgTable>
