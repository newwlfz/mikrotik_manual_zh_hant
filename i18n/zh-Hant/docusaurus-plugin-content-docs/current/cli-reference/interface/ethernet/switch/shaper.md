---
sidebar_key: "cli-reference/interface/ethernet/switch/shaper"
sidebar_position: 23
title: "shaper"
sidebar_label: 'shaper'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/shaper
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/shaper {#interfaceethernetswitchshaper}
**系統能力：** musicswitch
**型別：** 目錄

流量整形限制從介面傳輸的流的速率和突發大小。整形器透過令牌桶實現。如果封包超過最大速率或突發大小，這意味著沒有足夠的封包令牌，則該封包會儲存在緩衝區中，直到有足夠的令牌傳輸它。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="port" typ="enum" mandatory="1">用於流量整形的物理埠。</ArgTableRow>
<ArgTableRow arg="target" typ="enum (queue0 | queue1 | queue2 | queue3 | queue4 | queue5 | queue6 | queue7 | wrr-group0 | wrr-group1 | port) { queue0:0, queue1:1, queue2:2, queue3:3, queue4:4, queue5:5, queue6:6, queue7:7, wrr-group0:8, wrr-group1:9, port:10 }">
每個埠（包括 CPU 埠）支援三個層級的整形器。
- `port` - 條目應用於交換晶片的埠。
- `wrr-group0` 或 `wrr-group1` - 條目應用於埠上 2 個加權輪詢佇列組之一。
- `queue0`-`queue7` - 條目應用於埠上 8 個佇列之一。
</ArgTableRow>
<ArgTableRow arg="meter-unit" typ="enum (bit | packet) { bit:0, packet:1 }">流量整形速率的計量單位。</ArgTableRow>
<ArgTableRow arg="rate" typ="num">最大資料速率限制。</ArgTableRow>
<ArgTableRow arg="burst" typ="num">在允許突發期間可傳輸的最大資料速率。</ArgTableRow>
</ArgTable>
