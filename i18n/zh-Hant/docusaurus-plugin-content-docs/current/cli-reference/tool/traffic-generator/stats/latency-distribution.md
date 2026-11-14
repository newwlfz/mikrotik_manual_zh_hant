---
sidebar_key: "cli-reference/tool/traffic-generator/stats/latency-distribution"
sidebar_position: 1
title: "latency-distribution"
sidebar_label: 'latency-distribution'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-generator/stats/latency-distribution
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/stats/latency-distribution {#tooltraffic-generatorstatslatency-distribution}
**型別：** 目錄
按流或按測量序列顯示落入每個延遲範圍的接收封包數量。請參閱 [流量生成器](../../../../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="stream-id" typ="num">將輸出過濾為單個 stream ID。</ArgTableRow>
<ArgTableRow arg="port" typ="enum">將輸出過濾為單個埠。</ArgTableRow>
<ArgTableRow arg="seq" typ="range">將輸出過濾為單個測量序列號。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="latency" typ="string">此分桶的延遲範圍，例如 0-15.5us。</ArgTableRow>
<ArgTableRow arg="count" typ="num">此延遲範圍內收到的封包數量。</ArgTableRow>
<ArgTableRow arg="share" typ="num">落入此延遲範圍的已接收封包占比，以百分比表示。</ArgTableRow>
<ArgTableRow arg="graph" typ="meter">佔比的圖形化表示。</ArgTableRow>
</ArgTable>
