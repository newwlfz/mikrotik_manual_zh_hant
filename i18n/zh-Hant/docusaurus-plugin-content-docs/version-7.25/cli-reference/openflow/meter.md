---
sidebar_key: "cli-reference/openflow/meter"
sidebar_position: 3
title: "meter"
sidebar_label: 'meter'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/openflow/meter
captured_at: '2026-11-01T21:24:52+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## openflow/meter {#openflowmeter}
**軟體包：** openflow
**型別：** 目錄

該子選單列出了控制器安裝的流量計量表。計量表支援在輸出和應用動作指令之前進行速率監控。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="switch" typ="enum">安裝該計量表的控制器名稱。</ArgTableRow>
<ArgTableRow arg="id" typ="num">計量表的識別符號。</ArgTableRow>
<ArgTableRow arg="band-count" typ="num">該計量表中的計量帶數量。</ArgTableRow>
<ArgTableRow arg="bands" typ="string">定義速率以及封包處理方式的計量帶列表。</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">該計量表處理的位元組數。</ArgTableRow>
<ArgTableRow arg="packets" typ="num">該計量表處理的封包數。</ArgTableRow>
<ArgTableRow arg="duration" typ="time">自該計量表安裝以來經過的時間。</ArgTableRow>
</ArgTable>
