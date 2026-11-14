---
sidebar_key: "cli-reference/routing/ospf/interface-template"
sidebar_position: 3
title: "interface-template"
sidebar_label: 'interface-template'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/ospf/interface-template
captured_at: '2026-11-01T21:25:14+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/ospf/interface-template {#routingospfinterface-template}
**型別：** 目錄

介面模板定義通用的網路和介面匹配項，以及要為匹配的介面分配哪些引數。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="area" typ="enum" mandatory="1">匹配介面將關聯到的 OSPF 區域。</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }" unset="1">匹配器。要匹配的介面。接受特定介面名稱或介面列表的名稱。</ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="networks" typ="object { network: address (flags=46/)
 }" unset="1">匹配器。與該區域關聯的網路字首。OSPF 將在所有至少有一個地址落在該範圍內的介面上啟用。請注意，此檢查使用地址的網路字首（即不是本地地址）。對於點對點介面，這意味著遠端端點的地址。</ArgTableRow>
<ArgTableRow arg="prefix-list" typ="enum" unset="1">包含應通告到 v3 介面的網路的地址列表名稱。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (broadcast | nbma | ptp | ptp-unnumbered | ptmp | ptmp-broadcast)">
此介面上的 OSPF 網路型別。請注意，如果介面配置不存在，則預設網路型別在 PtP 介面上為 'ptp'，在所有其他介面上為 'broadcast'。
- `broadcast` - 適用於乙太網和其他支援多播的鏈路層的網路型別。選舉指定路由器。
- `nbma` - 非廣播多路訪問。協定封包會發送到每個鄰居的單播地址。需要手動配置鄰居。選舉指定路由器。
- `ptp` - 適用於僅由兩個節點組成的網路。不選舉指定路由器。
- `ptmp` - 點對多點。比 NBMA 更易於配置，因為它不需要手動配置鄰居。不選舉指定路由器。這是最穩健的網路型別，因此如果 'broadcast' 模式對無線網路來說效果不夠好，則適合無線網路
- `ptp-unnumbered` - 與 ptp 相同，不同之處在於遠端鄰居沒有與特定 PTP 介面關聯的 IP 地址。例如，在 Cisco 裝置上使用 IP unnumbered 的情況。
</ArgTableRow>
<ArgTableRow arg="retransmit-interval" typ="time">在此時間間隔之後，丟失的鏈路狀態通告將被重新發送。當路由器向其鄰居傳送鏈路狀態通告（LSA）時，該 LSA 會一直保留到收到確認為止。如果未及時收到確認（參見 transmit-delay），路由器將嘗試重新發送該 LSA。</ArgTableRow>
<ArgTableRow arg="transmit-delay" typ="time">鏈路狀態傳輸延遲是在介面上傳輸鏈路狀態更新封包所需的估計時間。</ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time">路由器在此介面上發出的 **HELLO** 封包之間的間隔。此間隔越小，檢測到拓撲變化的速度就越快；代價是更多的 OSPF 協定流量。對於特定網路上的所有路由器，此值必須相同，否則它們之間不會形成鄰接關係。</ArgTableRow>
<ArgTableRow arg="dead-interval" typ="time">指定鄰居被宣告為失效之後的時間間隔。此間隔會在 hello 封包中通告。對於特定網路上的所有路由器，此值必須相同，否則它們之間不會形成鄰接關係。</ArgTableRow>
<ArgTableRow arg="priority" typ="num">
路由器優先順序。用於在廣播網路中確定指定路由器。優先順序值最高的路由器優先。優先順序值為 0 表示該路由器完全沒有資格成為指定路由器或備份指定路由器。

預設值為 128；如果你為 DR/BDR 選舉設定了嚴格的優先順序，請注意這一點。
</ArgTableRow>
<ArgTableRow arg="cost" typ="num">以鏈路狀態度量表示的介面開銷。</ArgTableRow>
<ArgTableRow arg="passive" typ="switch">如果啟用，則路由器不會在匹配的介面上傳送或接收 OSPF 流量。</ArgTableRow>
<ArgTableRow arg="auth" typ="enum (simple | md5 | sha1 | sha256 | sha384 | sha512)" unset="1">
指定 OSPF 協定訊息的認證方法。

- `simple` - 明文認證。
- `md5` - 帶金鑰的訊息摘要 5 認證。
- `sha*` - HMAC-SHA 認證 RFC5709。

如果未設定該引數，則不使用認證。
</ArgTableRow>
<ArgTableRow arg="auth-key" typ="string" unset="1">要使用的認證金鑰，應在此網段的所有鄰居上匹配。</ArgTableRow>
<ArgTableRow arg="auth-id" typ="num" unset="1">金鑰 ID 用於計算訊息摘要（在啟用 MD5 或 SHA 認證時使用）。該值應與同一區域的所有 OSPF 路由器匹配。</ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1"></ArgTableRow>
</ArgTable>
