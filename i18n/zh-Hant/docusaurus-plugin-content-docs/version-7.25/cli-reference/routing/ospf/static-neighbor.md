---
sidebar_key: "cli-reference/routing/ospf/static-neighbor"
sidebar_position: 7
title: "static-neighbor"
sidebar_label: 'static-neighbor'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/ospf/static-neighbor
captured_at: '2026-11-01T21:25:14+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/ospf/static-neighbor {#routingospfstatic-neighbor}
**型別：** 目錄

OSPF 鄰居的靜態配置。非廣播多路訪問網路需要此配置。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="area" typ="enum" mandatory="1">鄰居所屬區域的名稱。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)" mandatory="1">單播 IP 地址以及可用於到達鄰居 IP 的介面。例如，`address=1.2.3.4%ether1` 表示 IP 為 `1.2.3.4` 的鄰居可透過 `ether1` 介面到達。</ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="poll-interval" typ="time">向處於 `down` 狀態的鄰居（即沒有來自它們的流量）傳送 hello 訊息的頻率。</ArgTableRow>
</ArgTable>
