---
sidebar_key: "cli-reference/routing/ospf/neighbor"
sidebar_position: 6
title: "neighbor"
sidebar_label: 'neighbor'
source: https://manual.mikrotik.com/docs/cli-reference/routing/ospf/neighbor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/ospf/neighbor {#routingospfneighbor}
**型別：** 目錄

當前活動 OSPF 鄰居的列表。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="V" typ="virtual">virtual</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="area" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">發現該鄰居的介面名稱。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)">OSPF 鄰居路由器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="router-id" typ="ipAddr">鄰居路由器的 **RouterID**</ArgTableRow>
<ArgTableRow arg="dr" typ="ipAddr">指定路由器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="bdr" typ="ipAddr">備用指定路由器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="state" typ="string">
- `Down` - 尚未從鄰居收到任何 Hello 封包。
- `Attempt` - 僅適用於 NBMA 雲。該狀態表示未從鄰居收到最近的資訊。
- `Init` - 已從鄰居收到 Hello 封包，但尚未建立雙向通訊（其自身的 RouterID 未列在 Hello 封包中）。
- `2-way` - 該狀態表示已建立雙向通訊。DR 和 BDR 選舉在此狀態期間進行。路由器根據其是 DR 還是 BDR，以及鏈路是 point-to-point 還是虛擬鏈路來建立鄰接關係。
- `ExStart` - 路由器嘗試建立用於封包資訊交換的初始序列號。ID 較高的路由器成為主路由器並開始交換。
- `Exchange` - 路由器交換資料庫描述（DD）封包。
- `Loading` - 在此狀態下，交換實際的鏈路狀態資訊。向鄰居傳送鏈路狀態請求封包，以請求在 Exchange 狀態期間發現的任何新 LSA。
- `Full` - 鄰接關係已完成，鄰居路由器完全鄰接。LSA 資訊在相鄰路由器之間同步。路由器僅與其 DR 和 BDR 達到 Full 狀態。P2P 鏈路是一個例外。
</ArgTableRow>
<ArgTableRow arg="state-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="ls-retransmits" typ="num"></ArgTableRow>
<ArgTableRow arg="ls-requests" typ="num"></ArgTableRow>
<ArgTableRow arg="db-summaries" typ="num"></ArgTableRow>
<ArgTableRow arg="adjacency" typ="time">自鄰接關係形成以來經過的時間。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>
