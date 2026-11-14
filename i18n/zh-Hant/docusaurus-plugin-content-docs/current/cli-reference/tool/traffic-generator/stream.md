---
sidebar_key: "cli-reference/tool/traffic-generator/stream"
sidebar_position: 10
title: "stream"
sidebar_label: 'stream'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-generator/stream
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/stream {#tooltraffic-generatorstream}
**型別：** 目錄
定義生成的流量流：速率、封包大小、封包模板和 CPU 核心繫結。請參閱[流量生成器](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator.md)指南。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">流的描述性名稱。</ArgTableRow>
<ArgTableRow arg="port" typ="enum">流所經過的埠名稱（來自 port 選單）。通常取自封包模板；可在此處覆蓋。</ArgTableRow>
<ArgTableRow arg="id" typ="num">用於在統計資訊以及 start/quick 命令中標識該流的流 ID。值 TOT 保留用於總計。</ArgTableRow>
<ArgTableRow arg="packet-size" typ="range">所生成封包的 L2 大小（以位元組為單位）；使用範圍（例如 64-1518）可生成隨機封包大小。</ArgTableRow>
<ArgTableRow arg="pps" typ="num">該流嘗試生成的每秒封包數。</ArgTableRow>
<ArgTableRow arg="mbps" typ="num">該流嘗試生成的每秒兆位元數。</ArgTableRow>
<ArgTableRow arg="packet-count" typ="num">要傳送的封包數量；`unlimited` 表示持續傳送，直到該流被停止。</ArgTableRow>
<ArgTableRow arg="cpu-core" typ="range">該流所繫結的 CPU 核心（0-255），或用於多核流的核心範圍。</ArgTableRow>
<ArgTableRow arg="tx-template" typ="enum" mandatory="1">用作封包內容來源的封包模板（來自 packet-template 或 raw-packet-template）的名稱。必填。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="default-port" typ="enum">此資料流傳送所使用的埠，取自封包模板。</ArgTableRow>
</ArgTable>
