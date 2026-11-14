---
sidebar_key: "cli-reference/interface/wifi/sniffer"
sidebar_position: 24
title: "sniffer"
sidebar_label: 'sniffer'
source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/sniffer
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wifi/sniffer {#interfacewifisniffer}
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="stream-address" typ="address (flags=46v)"></ArgTableRow>
<ArgTableRow arg="stream-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="stream-port" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="pcap-file" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="pcap-size-limit" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="filter" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="show-frame" typ="enum (no | yes | radiotap)" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="num" typ="num"></ArgTableRow>
<ArgTableRow arg="wlan.addr1" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="wlan.addr2" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="wlan.addr3" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="raw" typ="string"></ArgTableRow>
</ArgTable>
