---
sidebar_key: "cli-reference/tool/sniffer/protocol"
sidebar_position: 4
title: "protocol"
sidebar_label: 'protocol'
source: https://manual.mikrotik.com/docs/cli-reference/tool/sniffer/protocol
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/sniffer/protocol {#toolsnifferprotocol}
**型別：** 目錄

按 MAC 協定、IP 協定和埠統計最後一次抓包的包數與位元組數，以及每一行佔全部已抓取位元組的比例。一個包會統計在它所屬的每一行中：對於 TCP 包，會統計在 `ip` 行、`ip`/`tcp` 行以及其每個埠對應的行中。參見[封包嗅探器](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="protocol" typ="enum ()">MAC（L2）協定，例如 `ip`、`arp`、`ipv6` 或 `802.2`。</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (ip) { ip:0 }">IP 協定，例如 `icmp`、`tcp` 或 `udp`。在統計整個 MAC 協定的行上為空。</ArgTableRow>
<ArgTableRow arg="port" typ="enum ()">埠，在已知時附帶其服務名稱，例如 `80 (http)`。在統計整個協定的行上為空。</ArgTableRow>
<ArgTableRow arg="packets" typ="num">此行中已抓取的包數。</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">此行中已抓取的位元組數。</ArgTableRow>
<ArgTableRow arg="share" typ="num">此行位元組數佔全部已抓取位元組的比例，以百分比表示。</ArgTableRow>
</ArgTable>
