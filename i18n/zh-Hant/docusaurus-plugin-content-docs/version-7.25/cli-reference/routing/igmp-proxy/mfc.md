---
sidebar_key: "cli-reference/routing/igmp-proxy/mfc"
sidebar_position: 2
title: "mfc"
sidebar_label: 'mfc'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/igmp-proxy/mfc
captured_at: '2026-11-01T21:25:11+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/igmp-proxy/mfc {#routingigmp-proxymfc}
**型別：** 目錄

多播轉發快取 (MFC) 狀態。

RouterOS 支援 IGMP proxy 的靜態多播轉發規則。如果添加了靜態規則，則該組的所有動態規則都將被忽略。僅當配置了 IGMP-proxy 介面（應設定上游和下游介面）時，這些規則才會生效，否則這些規則將不會處於活動狀態。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="A" typ="active">已啟用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="group" typ="ipAddr" mandatory="1">此規則應用的多播組地址。</ArgTableRow>
<ArgTableRow arg="source" typ="ipAddr" mandatory="1">多播資料發起方地址。</ArgTableRow>
<ArgTableRow arg="upstream-interface" typ="iface_enum" mandatory="1">正在接收流資料的介面。</ArgTableRow>
<ArgTableRow arg="downstream-interfaces" typ="multi { interface: iface_enum
 }">接收到的流將僅傳送到列出的介面。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="active-downstream-interfaces" typ="multi { interface: iface_enum
 }">封包流透過此介面離開路由器。</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">接收到的多播流量總量。</ArgTableRow>
<ArgTableRow arg="packets" typ="num">接收到的多播封包總量。</ArgTableRow>
<ArgTableRow arg="wrong-packets" typ="num">接收到的從錯誤介面到達的多播封包總量，例如，多播流是在下游介面而不是上游介面上接收的。</ArgTableRow>
</ArgTable>
