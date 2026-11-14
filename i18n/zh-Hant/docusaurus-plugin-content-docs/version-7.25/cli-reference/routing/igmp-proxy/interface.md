---
sidebar_key: "cli-reference/routing/igmp-proxy/interface"
sidebar_position: 1
title: "interface"
sidebar_label: 'interface'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/igmp-proxy/interface
captured_at: '2026-11-01T21:25:12+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/igmp-proxy/interface {#routingigmp-proxyinterface}
**型別：** 目錄

配置哪些介面將作為路由器上的 IGMP 代理介面參與工作。如果某個介面未配置為 IGMP 代理介面，則從該介面收到的所有 IGMP 流量都會被忽略。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum { all:0 }">介面名稱。</ArgTableRow>
<ArgTableRow arg="upstream" typ="bool">如果介面位於組播樹根的方向，則該介面稱為 "upstream"。IGMP 轉發路由器必須恰好配置一個 upstream 介面。upstream 介面用於傳送 IGMP 成員關係請求。</ArgTableRow>
<ArgTableRow arg="threshold" typ="num">最小 TTL。接收到 TTL 值更低的封包將被忽略</ArgTableRow>
<ArgTableRow arg="alternative-subnets" typ="multi { numbers: super { as: ipAddr
, [netmask] /num
 }
 }">預設情況下，僅接受來自直連子網的封包。此引數可用於指定備用有效封包源子網列表，適用於資料和 IGMP 封包。僅對 upstream 介面生效。當組播資料的源經常位於不同的 IP 網路時應使用此引數。</ArgTableRow>
<ArgTableRow arg="robustness" typ="num">此介面的 robustness 值。覆蓋 `/routing/igmp-proxy` 選單中的全域性 robustness 設定。</ArgTableRow>
<ArgTableRow arg="query-interval" typ="time">透過此介面傳送 IGMP Query 訊息的頻率。覆蓋 `/routing/igmp-proxy` 選單中的全域性 query-interval 設定。</ArgTableRow>
<ArgTableRow arg="query-response-interval" typ="time">在此介面上等待 IGMP Query 訊息響應的時間。覆蓋 `/routing/igmp-proxy` 選單中的全域性 query-response-interval 設定。</ArgTableRow>
<ArgTableRow arg="last-member-query-interval" typ="time">此介面上組特定查詢的超時時間。覆蓋 `/routing/igmp-proxy` 選單中的全域性 last-member-query-interval 設定。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="state.querier" typ="bool">此介面當前是否為當選的 IGMP querier。</ArgTableRow>
<ArgTableRow arg="state.source-ip-address" typ="ipAddr">此介面用於 IGMP 訊息的源 IP 地址。</ArgTableRow>
<ArgTableRow arg="state.rx-bytes" typ="num">介面上接收到的組播流量總量，以位元組為單位。</ArgTableRow>
<ArgTableRow arg="state.rx-packets" typ="num">介面上接收到的組播流量總量，以封包為單位。</ArgTableRow>
<ArgTableRow arg="state.tx-bytes" typ="num">介面上傳送的組播流量總量，以位元組為單位。</ArgTableRow>
<ArgTableRow arg="state.tx-packets" typ="num">介面上傳送的組播流量總量，以封包為單位。</ArgTableRow>
<ArgTableRow arg="state.robustness" typ="num">介面上正在使用的有效 robustness 值。當此介面不是當選的 querier 時，它會採用當選 querier 在其 IGMP 查詢中通告的 robustness 值。</ArgTableRow>
<ArgTableRow arg="state.query-interval" typ="time">介面上正在使用的有效查詢間隔。當此介面不是當選的 querier 時，它會採用當選 querier 在其 IGMP 查詢中通告的查詢間隔。</ArgTableRow>
</ArgTable>
