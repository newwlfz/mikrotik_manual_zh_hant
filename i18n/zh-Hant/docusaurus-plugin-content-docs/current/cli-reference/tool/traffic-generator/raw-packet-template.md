---
sidebar_key: "cli-reference/tool/traffic-generator/raw-packet-template"
sidebar_position: 6
title: "raw-packet-template"
sidebar_label: 'raw-packet-template'
source: https://manual.mikrotik.com/docs/cli-reference/tool/traffic-generator/raw-packet-template
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/traffic-generator/raw-packet-template {#tooltraffic-generatorraw-packet-template}
**型別：** 目錄
從原始報頭字串構建封包內容。當您需要 packet-template 構建器無法表達的低層封包時，請使用此項。請參閱[流量生成器](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator.md)指南。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">RAW 封包模板的描述性名稱。</ArgTableRow>
<ArgTableRow arg="port" typ="enum">埠名稱（來自 port 選單），封包透過該埠傳送出去。</ArgTableRow>
<ArgTableRow arg="header" typ="string">以十六進位制字串表示的 RAW 封包頭部；它完整定義了頭部棧。</ArgTableRow>
<ArgTableRow arg="data" typ="enum (uninitialized | random | specific-byte | incrementing) { uninitialized:0, random:1, specific-byte:2, incrementing:3 }">封包載荷（頭部之後的部分）的填充方式：uninitialized（不置零；最快）、specific-byte（使用 data-byte 填充）、incrementing（位元組 00 01 02 ...）、random（隨機位元組；最慢）。</ArgTableRow>
<ArgTableRow arg="data-byte" typ="num">當 data=specific-byte 時用於填充載荷的位元組。</ArgTableRow>
<ArgTableRow arg="random-byte-offsets-and-masks" typ="multi { array-id, array-id, offset-and-mask: composite { offset: num [ .. 256]
, mask: num [ .. 255]
 }
 }">封包中的位元組偏移量，每個都帶有一個位掩碼，這些位置將被填入隨機值。</ArgTableRow>
<ArgTableRow arg="random-ranges" typ="object { random-range: super { offset: num [ .. 256]
, [width] :enum (8 | 16 | 32) { 8:8, 16:16, 32:32 }
, [range] :range
 }
 }">位於給定位元組偏移處的欄位將被填入隨機值：`width` 設定欄位大小（8、16 或 32 位），`range` 設定取值範圍。</ArgTableRow>
<ArgTableRow arg="ip-header-offset" typ="multi { ip-header-offset: num [ .. 65535]
 }">IPv4 頭部在封包中的位元組偏移量，以便生成器能夠定位並解析它。</ArgTableRow>
<ArgTableRow arg="ipv6-header-offset" typ="multi { ipv6-header-offset: num [ .. 65535]
 }">IPv6 頭在封包中的位元組偏移量。</ArgTableRow>
<ArgTableRow arg="udp-header-offset" typ="multi { udp-header-offset: num [ .. 65535]
 }">UDP 頭在封包中的位元組偏移量。</ArgTableRow>
<ArgTableRow arg="udp-compute-checksum" typ="multi { udp-compute-checksum: bool
 }">UDP 校驗和是否由生成器計算。</ArgTableRow>
<ArgTableRow arg="tcp-header-offset" typ="multi { tcp-header-offset: num [ .. 65535]
 }">TCP 頭在封包中的位元組偏移量。</ArgTableRow>
<ArgTableRow arg="special-footer" typ="bool">是否在生成的封包後附加特殊尾部。</ArgTableRow>
<ArgTableRow arg="compute-checksum-from-offset" typ="num">計算 2 位元組校驗和的起始位元組偏移量；例如 14 表示跳過乙太網頭。no-checksum 表示停用校驗和。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="header-length" typ="num">封包頭部的總長度（以位元組為單位）。</ArgTableRow>
</ArgTable>
