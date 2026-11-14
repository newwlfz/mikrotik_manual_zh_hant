---
sidebar_key: "cli-reference/tool/traffic-generator/inject-pcap"
sidebar_position: 1
title: "inject-pcap"
sidebar_label: 'inject-pcap'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-generator/inject-pcap
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/inject-pcap {#tooltraffic-generatorinject-pcap}
**型別：** 命令
在介面上從 PCAP 或 PCAPNG 檔案重放封包。PCAPNG 是 [嗅探工具](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) 儲存捕獲資料時使用的格式。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum">重放捕獲封包的介面。</ArgTableRow>
<ArgTableRow arg="pcap-file" typ="file">儲存在路由器上的 PCAP 或 PCAPNG 檔案的名稱。</ArgTableRow>
<ArgTableRow arg="speed-multiplier" typ="num">相對於捕獲速率的重放速度倍數（1 表示按即時速度重放）。</ArgTableRow>
<ArgTableRow arg="loop" typ="bool">是否迴圈重放捕獲內容。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="iteration" typ="num">當前重放迭代編號（在迴圈模式下）。</ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num">目前已重放的封包數量。</ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num">目前已重放的位元組數。</ArgTableRow>
</ArgTable>
