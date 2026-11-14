---
sidebar_key: "cli-reference/interface/mesh"
title: "mesh"
sidebar_label: 'mesh'
source: https://manual.mikrotik.com/docs/cli-reference/interface/mesh
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/mesh {#interfacemesh}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="auto-mac" typ="bool"></ArgTableRow>
<ArgTableRow arg="admin-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="mesh-portal" typ="bool"></ArgTableRow>
<ArgTableRow arg="hwmp-default-hoplimit" typ="num"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-waiting-time" typ="time"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-retries" typ="num"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-destination-only" typ="bool"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-reply-and-forward" typ="bool"></ArgTableRow>
<ArgTableRow arg="hwmp-prep-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="hwmp-rann-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="hwmp-rann-propagation-delay" typ="num"></ArgTableRow>
<ArgTableRow arg="hwmp-rann-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="reoptimize-paths" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>
