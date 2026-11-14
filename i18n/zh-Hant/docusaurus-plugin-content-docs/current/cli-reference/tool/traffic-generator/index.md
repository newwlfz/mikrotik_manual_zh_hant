---
sidebar_key: "cli-reference/tool/traffic-generator"
title: "traffic-generator"
sidebar_label: 'traffic-generator'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-generator
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator {#tooltraffic-generator}
**型別：** 設定目錄
流量生成器總體設定和命令。請參閱[流量生成器](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator.md)指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="test-id" typ="num">測試會話的 ID。`start` 和 `quick` 命令接受 `test-id` 以覆蓋該值。預設值：0。</ArgTableRow>
<ArgTableRow arg="measure-out-of-order" typ="bool">是否測量並報告亂序到達的接收封包。在多核裝置上啟用時，單個流使用單個 CPU 核心。預設值：多核裝置為 no，單核裝置為 yes。</ArgTableRow>
<ArgTableRow arg="latency-distribution-max" typ="time">延遲分佈測量的最大延遲範圍。RouterOS 根據此值推匯出 `latency-distribution-measure-interval` 範圍。預設值：100us。</ArgTableRow>
<ArgTableRow arg="stats-samples-to-keep" typ="num">保留多少個統計樣本。預設值：100。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="running" typ="bool">流量生成器當前是否正在執行。</ArgTableRow>
<ArgTableRow arg="latency-distribution-samples" typ="num">latency-distribution-measure-interval 被劃分成的各個延遲範圍的數量。</ArgTableRow>
<ArgTableRow arg="latency-distribution-measure-interval" typ="string">當前使用的總延遲測量範圍，例如 0-2.67us。</ArgTableRow>
</ArgTable>
