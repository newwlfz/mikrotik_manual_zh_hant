---
sidebar_key: "cli-reference/interface/l2tp-ether/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/l2tp-ether/monitor
captured_at: '2026-11-01T21:22:49+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/l2tp-ether/monitor {#interfacel2tp-ethermonitor}
**型別：** 命令

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">當前連線狀態。</ArgTableRow>
<ArgTableRow arg="circuit-id" typ="string">L2TPv3 電路識別符號。</ArgTableRow>
<ArgTableRow arg="cookie-length" typ="num">L2TPv3 cookie 長度。</ArgTableRow>
<ArgTableRow arg="header-format" typ="string">L2TPv3 報頭格式。</ArgTableRow>
<ArgTableRow arg="l2-sublayer" typ="bool">是否啟用 L2 子層。</ArgTableRow>
<ArgTableRow arg="remote-sess-id" typ="num">遠端會話 ID。</ArgTableRow>
<ArgTableRow arg="local-sess-id" typ="num">本地會話 ID。</ArgTableRow>
<ArgTableRow arg="control-conn-id" typ="num">控制連線 ID。</ArgTableRow>
<ArgTableRow arg="peer-address" typ="string">已連線對端的 IP 地址。</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">使用的加密編碼。</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">連線執行時間。</ArgTableRow>
</ArgTable>
