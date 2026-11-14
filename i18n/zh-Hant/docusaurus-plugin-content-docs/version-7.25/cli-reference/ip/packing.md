---
sidebar_key: "cli-reference/ip/packing"
sidebar_position: 15
title: "packing"
sidebar_label: 'packing'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/packing
captured_at: '2026-11-01T21:24:17+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/packing {#ippacking}
**型別：** 目錄

打包規則會把介面的出站封包聚合成更大的封包（可選壓縮），並在接收端將其解包。兩臺路由器都需要在該介面上執行鄰居發現。路由器透過打包鏈路發起的 TCP 連線會失敗，請參閱 [IP 打包](../../system-information-and-utilities/ip-packing.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">打包規則已停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">用於聚合或壓縮出站封包並解包入站封包的介面。路由器只會向透過鄰居發現通告其解包能力的鄰居進行打包，因此兩臺路由器都必須在該介面上執行發現。兩臺路由器必須對稱配置。</ArgTableRow>
<ArgTableRow arg="packing" typ="enum (none | simple | compress-headers | compress-all) { none:0x00, simple:0x01, compress-headers:0x03, compress-all:0x07 }">
對出站封包執行的操作：
- `none`（預設）- 按原樣傳送封包。
- `simple` - 僅聚合封包。
- `compress-headers` - 聚合封包並壓縮其頭部；保持載荷不變。
- `compress-all` - 聚合封包並壓縮頭部和載荷。
</ArgTableRow>
<ArgTableRow arg="unpacking" typ="enum (none | simple | compress-headers | compress-all) { none:0x00, simple:0x01, compress-headers:0x03, compress-all:0x07 }">
對傳入封包執行的操作。路由器會向鄰居通告此設定（`/ip/neighbor` 中的 `unpack` 欄位）：
- `none`（預設值）- 對接收到的封包不做任何處理。
- `simple` - 解包聚合封包。
- `compress-headers` - 解包聚合封包並解壓縮報頭。
- `compress-all` - 解包聚合封包並解壓縮報頭和負載。
</ArgTableRow>
<ArgTableRow arg="aggregated-size" typ="num">打包在傳送聚合封包前嘗試達到的大小（以位元組為單位）。打包會等待填滿封包，因此會增加鏈路延遲。範圍：20..16384。預設值：1500。</ArgTableRow>
</ArgTable>
