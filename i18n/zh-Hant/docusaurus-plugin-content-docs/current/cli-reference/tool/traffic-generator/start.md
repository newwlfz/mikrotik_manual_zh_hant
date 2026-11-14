---
sidebar_key: "cli-reference/tool/traffic-generator/start"
sidebar_position: 7
title: "start"
sidebar_label: 'start'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-generator/start
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/start {#tooltraffic-generatorstart}
**型別：** 命令
在後臺啟動流量生成器。所有引數都會覆蓋流和報文模板中配置的值（與快速命令中的行為相同）。

<ArgTable c1="引數" c2="型別" c3="描述">
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
