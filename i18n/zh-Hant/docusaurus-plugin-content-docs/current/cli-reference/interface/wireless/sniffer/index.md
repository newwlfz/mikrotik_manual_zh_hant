---
sidebar_key: "cli-reference/interface/wireless/sniffer"
title: "sniffer"
sidebar_label: 'sniffer'
source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/sniffer
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireless/sniffer {#interfacewirelesssniffer}
**軟體包：** wireless-rep
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="multiple-channels" typ="bool"></ArgTableRow>
<ArgTableRow arg="channel-time" typ="time"></ArgTableRow>
<ArgTableRow arg="only-headers" typ="bool"></ArgTableRow>
<ArgTableRow arg="receive-errors" typ="bool"></ArgTableRow>
<ArgTableRow arg="memory-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="file-name" typ="string"></ArgTableRow>
<ArgTableRow arg="file-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="streaming-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="streaming-server" typ="super { ip: ipAddr
, [port] [ :num [1 .. 65535]]
 }"></ArgTableRow>
<ArgTableRow arg="streaming-max-rate" typ="num"></ArgTableRow>
</ArgTable>
