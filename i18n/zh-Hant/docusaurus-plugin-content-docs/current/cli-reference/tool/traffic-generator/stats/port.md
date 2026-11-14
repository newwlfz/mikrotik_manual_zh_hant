---
sidebar_key: "cli-reference/tool/traffic-generator/stats/port"
sidebar_position: 2
title: "port"
sidebar_label: 'port'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-generator/stats/port
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/stats/port {#tooltraffic-generatorstatsport}
**型別：** Directory
已完成或正在執行的測試的統計資訊，按傳送/接收埠排序。請參閱 [流量生成器](../../../../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) 指南。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="seq" typ="enum (TOT) { TOT:0xffffffff }">測量序列號，或使用 TOT 表示總計。</ArgTableRow>
<ArgTableRow arg="port" typ="composite { p: enum (TOT) { TOT:0xffffffff }
, interface: iface_enum
 }">傳送/接收埠及其介面，或 TOT。</ArgTableRow>
<ArgTableRow arg="rx-unk-packet" typ="num">接收到的、不屬於任何已知流的報文（不匹配任何報文模板）。</ArgTableRow>
<ArgTableRow arg="rx-unk-byte" typ="num">接收到的、不屬於任何已知流的位元組數。</ArgTableRow>
<ArgTableRow arg="rx-unk-rate" typ="num">未知報文的當前接收速率，單位為 bps。</ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num">傳送的封包總數。</ArgTableRow>
<ArgTableRow arg="tx-byte" typ="num">傳送的位元組總數。</ArgTableRow>
<ArgTableRow arg="tx-rate" typ="num">當前傳送速率，單位為 bps。</ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num">接收的封包總數。</ArgTableRow>
<ArgTableRow arg="rx-byte" typ="num">接收的位元組總數。</ArgTableRow>
<ArgTableRow arg="rx-rate" typ="num">當前接收速率，單位為 bps。</ArgTableRow>
<ArgTableRow arg="rx-ooo" typ="num">收到的亂序封包。</ArgTableRow>
<ArgTableRow arg="rx-bad-csum" typ="num">收到的校驗和錯誤的封包。</ArgTableRow>
<ArgTableRow arg="lost-packet" typ="num">丟失的封包總數（已傳送減去已接收）。</ArgTableRow>
<ArgTableRow arg="lost-byte" typ="num">丟失的位元組總數。</ArgTableRow>
<ArgTableRow arg="lost-rate" typ="num">當前丟包率，單位為 bps。</ArgTableRow>
<ArgTableRow arg="lost-ratio" typ="string">丟包占已傳送封包的百分比。</ArgTableRow>
<ArgTableRow arg="lat-min" typ="string">測得的最小延遲。</ArgTableRow>
<ArgTableRow arg="lat-avg" typ="string">測得的平均延遲。</ArgTableRow>
<ArgTableRow arg="lat-max" typ="string">測得的最大延遲。</ArgTableRow>
<ArgTableRow arg="jitter" typ="string">測得的延遲變化（抖動）。</ArgTableRow>
</ArgTable>
