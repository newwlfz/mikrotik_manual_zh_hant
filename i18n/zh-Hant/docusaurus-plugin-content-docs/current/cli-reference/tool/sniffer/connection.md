---
sidebar_key: "cli-reference/tool/sniffer/connection"
sidebar_position: 1
title: "connection"
sidebar_label: 'connection'
source: https://manual.mikrotik.com/docs/cli-reference/tool/sniffer/connection
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/sniffer/connection {#toolsnifferconnection}
**型別：** 目錄

最近一次捕獲中看到的 TCP 連線。請參閱 [封包嗅探器](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="A" typ="active">活動連線。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="composite { address: ipAddr
, port: enum ()
 }">開啟連線的一側的地址和埠，並附帶已知的服務名稱。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { address: ipAddr
, port: enum ()
 }">另一側的地址和埠，並附帶已知的服務名稱，例如 `192.168.88.36:80 (http)`。</ArgTableRow>
<ArgTableRow arg="bytes" typ="composite { in: num
, out: num
 }">捕獲到的由源端和目標端傳送的位元組數，以 源/目標 的形式顯示。</ArgTableRow>
<ArgTableRow arg="resends" typ="composite { in: num
, out: num
 }">從源端和目標端觀察到的重傳次數（源/目標）。</ArgTableRow>
<ArgTableRow arg="mss" typ="composite { in: num
, out: num
 }">源端和目標端通告的 TCP 最大報文段長度（源/目標）。</ArgTableRow>
</ArgTable>
