---
sidebar_key: "cli-reference/tool/traffic-generator/quick"
sidebar_position: 5
title: "quick"
sidebar_label: 'quick'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-generator/quick
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/quick {#tooltraffic-generatorquick}
**型別：** 命令
啟動流量生成器，將統計資訊列印到終端，並生成延遲/抖動報告。引數會覆蓋流和封包模板中配置的值；如果某個引數只指定一個報頭，則該值會乘用到其他報頭。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="entries-to-show" typ="num">要列印到終端的狀態行數。</ArgTableRow>
<ArgTableRow arg="test-id" typ="num">測試會話 ID（參見 general traffic-generator 選單）。</ArgTableRow>
<ArgTableRow arg="measure-out-of-order" typ="bool">是否為此測試測量並報告亂序接收的封包。</ArgTableRow>
<ArgTableRow arg="cpu-core" typ="multi { array-id, array-id, cpu-core: range [0 .. 255]
 }">流所繫結的 CPU 核心或核心範圍（0-255），用於多核測試。</ArgTableRow>
<ArgTableRow arg="stream" typ="multi { stream: enum
 }">要啟動的流的名稱。</ArgTableRow>
<ArgTableRow arg="port" typ="multi { port: enum
 }">要從中開始傳送的埠。</ArgTableRow>
<ArgTableRow arg="interface" typ="multi { port: iface_enum
 }">要從中開始傳送的介面；每個介面都隱含一個埠。</ArgTableRow>
<ArgTableRow arg="id" typ="multi { id: num [0 .. 255]
 }">要啟動的流 ID。</ArgTableRow>
<ArgTableRow arg="packet-size" typ="multi { array-id, array-id, packet-size: range [1 .. 65535]
 }">覆蓋生成的封包大小（以位元組為單位）；範圍會生成隨機大小。</ArgTableRow>
<ArgTableRow arg="pps" typ="multi { pps: num
 }">覆蓋每秒封包速率。</ArgTableRow>
<ArgTableRow arg="mbps" typ="multi { mbps: num
 }">覆蓋每秒兆位元速率。</ArgTableRow>
<ArgTableRow arg="tx-template" typ="multi { tx-template: enum
 }">覆蓋用作封包內容來源的封包模板（最多 16 個）。</ArgTableRow>
<ArgTableRow arg="packet-count" typ="multi { packet-count: num
 }">覆蓋要傳送的封包數量。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="seq" typ="enum (TOT) { TOT:0xffffffff }">測量序列號，或使用 TOT 表示總計。</ArgTableRow>
<ArgTableRow arg="id" typ="enum (TOT) { TOT:0xffffffff }">流 ID，或使用 TOT 表示所有流的合計。</ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num">傳送的封包總數。</ArgTableRow>
<ArgTableRow arg="tx-rate" typ="num">當前傳送速率，單位為 bps。</ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num">接收的封包總數。</ArgTableRow>
<ArgTableRow arg="rx-rate" typ="num">當前接收速率，單位為 bps。</ArgTableRow>
<ArgTableRow arg="rx-ooo" typ="num">收到的亂序封包。</ArgTableRow>
<ArgTableRow arg="rx-bad-csum" typ="num">收到的校驗和錯誤的封包。</ArgTableRow>
<ArgTableRow arg="lost-packet" typ="num">丟失的封包總數（已傳送減去已接收）。</ArgTableRow>
<ArgTableRow arg="lost-rate" typ="num">當前丟包率，單位為 bps。</ArgTableRow>
<ArgTableRow arg="lost-ratio" typ="string">丟包占已傳送封包的百分比。</ArgTableRow>
<ArgTableRow arg="lat-min" typ="string">測得的最小延遲。</ArgTableRow>
<ArgTableRow arg="lat-avg" typ="string">測得的平均延遲。</ArgTableRow>
<ArgTableRow arg="lat-max" typ="string">測得的最大延遲。</ArgTableRow>
<ArgTableRow arg="jitter" typ="string">測得的延遲變化（抖動）。</ArgTableRow>
</ArgTable>
