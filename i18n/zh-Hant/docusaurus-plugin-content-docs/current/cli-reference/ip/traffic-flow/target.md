---
sidebar_key: "cli-reference/ip/traffic-flow/target"
sidebar_position: 3
title: "target"
sidebar_label: 'target'
source: https://manual.mikrotik.com/docs/cli-reference/ip/traffic-flow/target
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/traffic-flow/target {#iptraffic-flowtarget}
**型別：** 目錄
匯出目標：透過 UDP 接收 traffic-flow 資料的收集器主機（例如 NetFlow 分析器主機）。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }">匯出封包的源地址。0.0.0.0 表示自動檢測：路由器使用出介面的源地址</ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }" mandatory="1">接收流資料的主機的 IP 地址</ArgTableRow>
<ArgTableRow arg="port" typ="num">傳送流資料的目標 UDP 埠。預設值：2055</ArgTableRow>
<ArgTableRow arg="version" typ="enum (1 | 5 | 9 | ipfix) { 1:1, 5:5, 9:9, ipfix:10 }">匯出封包的 NetFlow 格式：`1`、`5`、`9` 或 `ipfix`</ArgTableRow>
<ArgTableRow arg="v9-template-refresh" typ="num">重新發送 FlowSet 模板之前所經過的匯出封包數量（僅適用於 version 9 和 IPFIX）。預設值：20</ArgTableRow>
<ArgTableRow arg="v9-template-timeout" typ="time">如果到此時仍未傳送 FlowSet 模板，則在該間隔後傳送（僅適用於 version 9 和 IPFIX）</ArgTableRow>
</ArgTable>
