---
sidebar_key: "cli-reference/routing/ospf/interface"
sidebar_position: 4
title: "interface"
sidebar_label: 'interface'
source: https://manual.mikrotik.com/docs/cli-reference/routing/ospf/interface
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/ospf/interface {#routingospfinterface}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=4i)" unset="1"></ArgTableRow>
<ArgTableRow arg="area" typ="enum"></ArgTableRow>
<ArgTableRow arg="instance-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (broadcast | nbma | ptp | ptp-unnumbered | ptmp | ptmp-broadcast | virtual-link)">
該介面上的 OSPF 網路型別。請注意，如果介面配置不存在，則預設網路型別在 PtP 介面上為 'ptp'，在所有其他介面上為 'broadcast'。
- `broadcast` - 適用於乙太網和其他支援多播的鏈路層的網路型別。選舉指定路由器。
- `nbma` - 非廣播多路訪問。協定封包傳送到每個鄰居的單播地址。需要手動配置鄰居。選舉指定路由器。
- `ptp` - 適用於僅由兩個節點組成的網路。不選舉指定路由器。
- `ptmp` - 點對多點。比 NBMA 更容易配置，因為它不需要手動配置鄰居。不選舉指定路由器。這是最穩健的網路型別，因此適用於無線網路，如果 'broadcast' 模式對它們來說效果不夠理想。
- `ptp-unnumbered` - 與 ptp 的工作方式相同，不同之處在於遠端鄰居沒有與特定 PTP 介面關聯的 IP 地址。例如，在 Cisco 裝置上使用 IP unnumbered 的情況。
- `virtual-link` - 用於虛擬鏈路的介面。
</ArgTableRow>
<ArgTableRow arg="auth" typ="enum (simple | md5 | sha1 | sha256 | sha384 | sha512)" unset="1"></ArgTableRow>
<ArgTableRow arg="auth-key" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="auth-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="cost" typ="num"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="passive" typ="switch"></ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="retransmit-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="transmit-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="dead-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="vlink-transit-area" typ="enum" unset="1">兩臺路由器共有的非骨幹區域，虛擬鏈路將經由該區域建立。虛擬鏈路不能透過 stub 區域建立。</ArgTableRow>
<ArgTableRow arg="vlink-neighbor-id" typ="ipAddr" unset="1">指定應透過虛擬鏈路連線的鄰居的 **router-id**。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="state" typ="enum (down | loopback | ptp | passive | waiting | standby | dr-other | bdr | dr)"></ArgTableRow>
<ArgTableRow arg="dr" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="bdr" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="vlink-remote-address" typ="address (flags=46)"></ArgTableRow>
</ArgTable>
