---
sidebar_key: "cli-reference/routing/pimsm/interface"
sidebar_position: 5
title: "interface"
sidebar_label: 'interface'
source: https://manual.mikrotik.com/docs/cli-reference/routing/pimsm/interface
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/pimsm/interface {#routingpimsminterface}
**條件：** !smips
**型別：** 目錄

interface 選單顯示當前參與 PIM 的所有介面及其狀態。此選單包含由已定義的介面模板建立的動態和只讀條目。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="P" typ="pim-enabled">該介面已啟用 PIM。</ArgTableRow>
<ArgTableRow arg="G" typ="gmp-enabled">該介面已配置為進行 GMP（IGMP/MLD）操作。</ArgTableRow>
<ArgTableRow arg="R" typ="designated-router">該路由器是該介面網路上的指定路由器（DR）。</ArgTableRow>
<ArgTableRow arg="J" typ="join-tracking">該介面已啟用加入跟蹤。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum">該介面所屬的 PIM 例項。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">介面的名稱。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">該介面上 PIM 使用的 IP 地址。</ArgTableRow>
<ArgTableRow arg="pim.priority" typ="num">該路由器在介面網路上的 DR 優先順序。DR 優先順序最高的路由器會被選舉為指定路由器。</ArgTableRow>
<ArgTableRow arg="pim.propagation-delay" typ="time">該介面網路上 DR 使用的傳播延遲，會在 PIM hello 訊息中通告。</ArgTableRow>
<ArgTableRow arg="pim.override-interval" typ="time">該介面網路上 DR 使用的覆蓋間隔，會在 PIM hello 訊息中通告。</ArgTableRow>
<ArgTableRow arg="gmp.robustness" typ="num">該介面上 IGMP/MLD 查詢器配置的健壯性值。</ArgTableRow>
<ArgTableRow arg="gmp.query-interval" typ="time">該介面上傳送 IGMP/MLD 通用查詢的配置間隔。</ArgTableRow>
<ArgTableRow arg="gmp.query-response-interval" typ="time">該介面上 IGMP/MLD 通用查詢中通告的已配置最大響應時間。</ArgTableRow>
<ArgTableRow arg="gmp.last-member-query-interval" typ="time">該介面上 IGMP/MLD 組特定查詢中通告的已配置響應時間。</ArgTableRow>
<ArgTableRow arg="gmp.querier" typ="bool">該路由器當前是否是該介面上選舉出的 IGMP/MLD 查詢器。</ArgTableRow>
<ArgTableRow arg="gmp.state.robustness" typ="num">該介面上實際使用的有效健壯性值。當路由器不是選舉出的查詢器時，它會採用選舉出的查詢器在其查詢中通告的健壯性值。</ArgTableRow>
<ArgTableRow arg="gmp.state.query-interval" typ="time">該介面上實際使用的有效查詢間隔。當路由器不是選舉出的查詢器時，它會採用選舉出的查詢器在其查詢中通告的查詢間隔。</ArgTableRow>
</ArgTable>
