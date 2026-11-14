---
sidebar_key: "routing-and-networking-protocols/unicast/evpn"
sidebar_position: 3
title: "EVPN"
sidebar_label: "EVPN"
description: "本頁介紹用於二層和三層 VPN 服務的 EVPN 技術，詳細說明 BGP 控制平面、MPLS/VXLAN 封裝以及 EVPN 路由型別（Type-1 至 Type-5）。文中解釋了 NVE、VNI 和 MAC-VRF 等 NVO 術語，描述了透過入口複製處理 BUM 流量的方式，並概述了對稱/非對稱 IR"
tags:
  - 'bgp'
  - 'evpn'
  - 'vxlan'
  - 'ospf'
slug: /user-guides/routing-and-networking-protocols/unicast/evpn
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/unicast/evpn
captured_at: '2026-11-04T11:23:14+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

乙太網虛擬專用網路（EVPN）是一種在不同網段之間擴充套件二層和三層連通性的技術。MPLS 或 VXLAN 封裝透過 MPLS 或基於 IP 的網路傳輸乙太網幀。

BGP EVPN 用作多種資料平面封裝（包括二層和三層 VPN 服務）的控制平面。MP-BGP 承載 MAC 地址、MAC/IP 繫結和 IP 字首。

RFC7432 是最初的 EVPN 標準，它將 BGP 定義為 MPLS 資料平面的控制平面。RFC8365 擴充套件了對其他資料平面（VXLAN、NVGRE 和 MPLS over GRE）的支援，並將 EVPN 定義為網路虛擬化覆蓋（NVO）。

## 術語 {#terminology}

- NVO：網路虛擬化覆蓋（Network Virtualization Overlay），用於提供二層和三層 VPN 服務。
- NVE：網路虛擬化端點（Network Virtualization Endpoint）是 NVO 環境中的提供商邊緣（PE）節點。它負責 VPN 流量的封裝/解封裝。對於 VXLAN，這定義了 VTEP（虛擬隧道端點）。
- VNI：虛擬網路識別符號
- EVI：EVPN 例項
- RD：[路由區分符](../route-distinguisher-and-route-target.md#route-distinguisher) 是附加到 IP 字首的 64 位字首，用於使其唯一；多個租戶可以使用重疊的 IP 地址範圍。
- RT：[路由目標](../route-distinguisher-and-route-target.md#route-targets) 是用於控制路由匯入和匯出的 BGP 擴展團體屬性。通常，RT 基於 AS 號和 MAC-VRF 的 VNI
- MAC-VRF：PE（VTEP）上的 MAC 地址 [VRF](../vrf.md) 表。需要 RD 和 RT。
- BUM：廣播、未知單播和組播流量是 VXLAN 網路中的多目的地二層流量。
- Ingress replication：處理 BUM 流量的單播方法。它使用 IMET 路由自動發現遠端對等體。入口裝置將 BUM 流量複製到與二層 VNI 關聯的所有 VTEP。
- ESI - 乙太網段識別符號（Ethernet Segment Identifier）

為了讓 MP-BGP 承載 EVPN，定義了新的 AFI/SAFI：25（L2 VPN）/70（EVPN）。NLRI 中的下一跳地址是通告該 EVPN 路由的 VTEP 的 IP 地址。

EVPN 路由型別有五種：

- Type-1：（Ethernet A-D）通告多宿主乙太網段的可達性。
- Type-2：（MAC advertisement / MACIP）通告由特定 EVI 學習到的 MAC/IP 繫結中的 MAC 地址。
- Type-3：（Inclusive multicast IMET）通告二層域的成員關係，從而允許自動發現 VTEP。
- Type-4：（Ethernet segment）用於為 EVPN 多宿主模型（active-active 或 active-standby 轉發）發現連線到同一共享乙太網段的 VTEP。
- Type-5：（IP prefix）將 IP 字首通告到 EVPN 域中，允許建立經典三層 VPN（參見 [`/routing/bgp/vpn`](../../../cli-reference/routing/bgp/vpn.md)）。

資料平面封裝由封裝擴展團體屬性值定義：

- 8 - VXLAN（目前 ROS 僅支援這一種）
- 9 - NVGRE
- 10 - MPLS
- 11 - MPLSoGRE

在 EVPN 中支援子網間路由有兩種方法：對稱和非對稱整合路由與橋接（IRB）。兩種方法的主要區別在於，對稱方法在入口和出口 VTEP 上都支援路由和橋接，而非對稱方法在入口上支援路由，但在出口上僅支援橋接。對稱 IRB 需要為 L3VNI 提供 [VRF](../vrf.md) 例項。

## 路由列表 {#route-list}

RouterOS 將在 [`/routing/route`](../../../cli-reference/routing/route.md) 列表中顯示本地和收到的 EVPN 路由

本地生成的路由將帶有 **e-evpn** 標誌。例如：

```routeros
[admin@ros_leaf_3] /routing/route> print where evpn
Flags: e - EVPN
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
  DST-ADDRESS                                     GATEWAY        AFI   DISTANCE  SCOPE  TARGET-SCOPE
e [10.155.101.133:1010]macip:0|0C:50:85:84:00:01  203.0.255.133  evpn       200     40            10
e [10.155.101.133:1010]imet:0|203.0.255.133       203.0.255.133  evpn       200     40            10
e [203.0.255.133:4]imet:0|203.0.255.133           203.0.255.133  evpn       200     40            10

```

EVPN 資料編碼在 `dst-address` 引數中：

```
    Dst [rd]type:x|y
         ^  ^    ^
         |  |    + - where x - tag or ESI; y - type specific data (can show mac addresses, ip addresses, ethernet segments etc.)
         |  +------- name of the EVPN route type (macip, imet, es, ad, prefix)
         +---------- route distinguisher in square brackets

```

## 配置示例 {#configuration-examples}

### 基礎配置示例 {#basic-configuration-example}

基礎的二層 EVPN VXLAN 配置：

```routeros
/interface/bridge
add name=bridge1 vlan-filtering=yes pvid=40
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus3 pvid=40

/ip/address
add address=203.0.113.1 interface=lo

/interface/vxlan
add bridge=bridge1 bridge-pvid=40 local-address=203.0.113.1 name=vxlan1 vni=100040 learning=no

/routing/bgp/instance
add as=65000 name=evpn-inst

/routing/bgp/connection
add afi=evpn instance=evpn-inst local.address=203.0.113.1 .role=ebgp multihop=yes name=to-leaf-lo remote.address=203.0.113.2 .as=65001

/routing/bgp/evpn
add instance=evpn-inst name=bgp-evpn-1o vni=100040
```

對於只有一個 VNI 的簡單設定，無需設定路由區分符或 [`import.route-targets`](../../../cli-reference/routing/bgp/evpn.md#import.route-targets)/[`export.route-targets`](../../../cli-reference/routing/bgp/evpn.md#export.route-targets)。

:::info
當未指定 [RTs](../route-distinguisher-and-route-target.md#route-targets) 或 [RD](../route-distinguisher-and-route-target.md#route-distinguisher) 時，值會自動推導。路由目標設定為 `<PE ASN>:<VNI>`，路由區分符設定為 `<PE address>:<num derived from config id>`）。
:::

EVPN 配置直接對映到具有匹配 VNI 的 VXLAN 配置

### 使用 Arista EOS 和 ROS 的橋接 EVPN VXLAN 覆蓋網路 {#bridged-evpn-vxlan-overlay-with-aristas-eos-and-ros}

#### 拓撲 {#topology}

本示例將使用以下拓撲：

![](/img/63c06c8d554b8099.jpg#gh-light-mode-only)
![](/img/f73b2ee3f50a5d80.png#gh-dark-mode-only)

- 203.0.255.0/24 地址範圍用於環回地址
- 172.16.0.0/16 範圍內的子網用於 leaf 和 spine 路由器的 underlay 連線
- 192.168.0.0/16 範圍內的子網用於 VLAN 上的主機地址分配。

#### Underlay 配置 {#underlay-configuration}

Underlay 連線取決於現有網路；可以使用 eBGP、[OSPF](./ospf/areas-and-virtual-links.md)、ISIS，甚至靜態路由。在本示例中，我們使用 OSPF 作為 underlay 路由協定，以通告環回介面地址的路由。

**Ros\_Spine**

```routeros
/ip/address
add address=203.0.255.138 interface=lo
add address=172.16.1.1/30 interface=ether3
add address=172.16.2.1/30 interface=ether4
add address=172.16.3.1/30 interface=ether5
add address=172.16.4.1/30 interface=ether6
add address=172.16.5.1/30 interface=ether7

/routing/ospf/instance
add name=evpn_underlay
/routing/ospf/area
add disabled=no instance=evpn_underlay name=evpn-underlay-bb
/routing/ospf/interface-template
add area=evpn-underlay-bb disabled=no networks=172.16.0.0/16
add area=evpn-underlay-bb disabled=no interfaces=lo passive
```

**Ros\_Leaf\_3**

```routeros
/ip/address
add address=203.0.255.133 interface=lo
add address=172.16.3.2/30 interface=ether10

/routing/ospf/instance
add name=evpn_underlay
/routing/ospf/area
add disabled=no instance=evpn_underlay name=evpn-underlay-bb
/routing/ospf/interface-template
add area=evpn-underlay-bb disabled=no networks=172.16.0.0/16
add area=evpn-underlay-bb disabled=no interfaces=lo passive
```

**Eos\_Leaf**

```
interface Ethernet1
   no switchport
   ip address 172.16.5.2/30
!
interface Loopback0
   ip address 203.0.255.128/32
!
ip routing
!
router ospf 100
   router-id 203.0.255.135
   redistribute connected
   network 172.16.1.0/30 area 0.0.0.0
!

```

#### BGP EVPN 覆蓋網路 {#bgp-evpn-overlay}

對於 [BGP](./bgp/understanding-bgp.md) overlay，我們使用帶環回地址的 [`multihop`](../../../cli-reference/routing/bgp/connection.md#multihop) eBGP。

為簡化配置，可使用 BGP [`/routing/bgp/template`](../../../cli-reference/routing/bgp/template.md) 設定公共引數，並配置 [`/routing/bgp/connection`](../../../cli-reference/routing/bgp/connection.md) 監聽整個環回地址範圍。這種方法擴充套件性很好：新增更多 leaf 路由器無需在 spine 路由器上做任何更改。

此外，建議將 [`nexthop-choice`](../../../cli-reference/routing/bgp/connection.md#nexthop-choice) 設定為 propagate，尤其是在有多個 spine 時。如果使用 iBGP 作為 overlay，則 spine 應作為路由反射器，並且下一跳傳播預設會發生。

**Ros\_Spine** — [`/routing/bgp/instance`](../../../cli-reference/routing/bgp/instance.md)

```routeros
/routing/bgp/instance
add as=65000 name=bgp-instance-1
/routing/bgp/template
set default afi=evpn multihop=yes nexthop-choice=propagate
/routing/bgp/connection
add instance=bgp-instance-1 local.address=203.0.255.138 .role=ebgp name=evpn_leafs remote.address=\
    203.0.255.0/24 templates=default
```

**Ros\_Leaf\_3** — [`/routing/bgp/instance`](../../../cli-reference/routing/bgp/instance.md), [`/routing/bgp/connection`](../../../cli-reference/routing/bgp/connection.md)

```routeros
/routing/bgp/instance
add as=65003 disabled=no name=bgp-instance-1
/routing/bgp/connection
add afi=evpn instance=bgp-instance-1 local.address=203.0.255.133 .role=ebgp multihop=yes name=to_spine remote.address=\
    203.0.255.138
```

**Eos\_Leaf**

```
service routing protocols model multi-agent
!
router bgp 65005
   neighbor SPINE_EVPN peer group
   neighbor SPINE_EVPN remote-as 65000
   neighbor SPINE_EVPN update-source Loopback0
   neighbor SPINE_EVPN ebgp-multihop 10
   neighbor SPINE_EVPN send-community extended
   neighbor 203.0.255.138 peer group SPINE_EVPN
   !
   address-family evpn
      neighbor SPINE_EVPN activate
!
```

##### 驗證 BGP 連通性 {#verify-bgp-connectivity}

檢查 [`/routing/bgp/session`](../../../cli-reference/routing/bgp/session/index.md) 以驗證 BGP 對等狀態。

**Eos\_Leaf**

```
localhost#show bgp summary
BGP summary information for VRF default
Router identifier 203.0.255.128, local AS number 65005
Neighbor               AS Session State AFI/SAFI                AFI/SAFI State   NLRI Rcd   NLRI Acc
------------- ----------- ------------- ----------------------- -------------- ---------- ----------
203.0.255.138       65000 Established   IPv4 Unicast            Advertised              0          0
203.0.255.138       65000 Established   L2VPN EVPN              Negotiated              6          6
```

**Ros\_Leaf\_3**

```routeros
[admin@ros_leaf_3] /routing/bgp/session> print
Flags: E - established
 0 E name="to_spine-1" instance=bgp-instance-1
     remote.address=203.0.255.138 .as=65000 .id=203.0.255.138 .capabilities=mp,rr,gr,as4 .afi=evpn .messages=7 .bytes=682 .eor=""
     local.address=203.0.255.133 .as=65003 .id=203.0.255.133 .cluster-id=203.0.255.133 .capabilities=mp,rr,gr,as4 .afi=evpn .messages=7
     .bytes=698 .eor=""
     output.procid=20
     input.procid=20 ebgp
     multihop=yes hold-time=3m keepalive-time=1m uptime=1s620ms last-started=2025-05-29 11:01:38 prefix-count=0
```

#### VXLAN 和 EVPN 配置 {#vxlan-and-evpn-configuration}

**Ros\_Leaf\_3**

僅用於演示目的，在 RouterOS leaf 上我們將向主機發送帶 VLAN 標籤的流量。

由於我們使用 [BGP EVPN](../../../cli-reference/routing/bgp/evpn.md) 進行發現，因此應停用 VXLAN 學習。EVPN 配置在 [`/routing/bgp/evpn`](../../../cli-reference/routing/bgp/evpn.md) 選單下完成。

```routeros
/interface/bridge
add name=bridge1 pvid=10 vlan-filtering=yes
/interface/vxlan
add bridge=bridge1 bridge-pvid=10 learning=no local-address=203.0.255.133 mac-address=C2:16:F6:B2:CC:D3 name=vxlan1 vni=1010
/interface/bridge/port
add bridge=bridge1 interface=ether11 pvid=10
/ip/address
add address=192.168.10.133/24 interface=bridge1
/routing/bgp/evpn
add disabled=no export.route-targets=1010:1010 import.route-targets=1010:1010 instance=bgp-instance-1 name=bgp-evpn-1 vni=1010
```

**Eos\_Leaf**

在 Arista 路由器上，我們設定 VLAN trunk，未標記的流量將傳送到主機

```
vlan 10
!
interface Ethernet2
   switchport trunk allowed vlan 10
   switchport mode trunk
!
interface Vlan10
   ip address 192.168.10.128/24
!
interface Vxlan1
   vxlan source-interface Loopback0
   vxlan vlan 10 vni 1010
!
router bgp 65501
   vlan 10
      rd 203.0.255.128:1010
      route-target both 1010:1010
      redistribute learned
```

**Host\_1**

```routeros
/ip/address
add address=192.168.10.132/24 interface=ether2
```

**Host\_3**

```routeros
/interface/vlan
add interface=ether2 name=vlan10 vlan-id=10
/ip/address
add address=192.168.10.129/24 interface=vlan10
```

#### 驗證 L2VPN 服務 {#validate-l2vpn-service}

讓我們驗證 leaf 路由器上是否存在 **IMET** 路由，以及是否發現了 **VTEPs**。

```routeros
[admin@ros_leaf_3] /routing/route> print where dst-address~"imet"
Flags: A - ACTIVE; b - BGP, e - EVPN
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS                               GATEWAY        AFI   DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW
Ab [203.0.255.128:1010]imet:0|203.0.255.128  203.0.255.128  evpn        20     40            30  172.16.3.1%ether10
 e [203.0.255.133:256]imet:0|203.0.255.133   203.0.255.133  evpn       200     40            10

[admin@ros_leaf_3] /interface/vxlan/vteps> print
Flags: D - DYNAMIC
Columns: INTERFACE, REMOTE-IP
#   INTERFACE  REMOTE-IP
0 D vxlan1     203.0.255.128
```

在 Arista 上：

```
localhost#show bgp evpn route-type imet
BGP routing table information for VRF default
Router identifier 203.0.255.135, local AS number 65501
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending BGP convergence
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 203.0.255.128:1010 imet 203.0.255.128
                                 -                     -       -       0       i
 * >      RD: 203.0.255.133:256 imet 203.0.255.133
                                 203.0.255.133         -       100     0       65000 65003 i

localhost#show interfaces vxlan1
Vxlan1 is up, line protocol is up (connected)
  Hardware is Vxlan
  Source interface is Loopback0 and is active with 203.0.255.128
  Listening on UDP port 4789
  Replication/Flood Mode is headend with Flood List Source: EVPN
  Remote MAC learning via EVPN
  VNI mapping to VLANs
  Static VLAN to VNI mapping is
    [10, 1010]
  Note: All Dynamic VLANs used by VCS are internal VLANs.
        Use 'show vxlan vni' for details.
  Static VRF to VNI mapping is not configured
  Headend replication flood vtep list is:
    10 203.0.255.133
  Shared Router MAC is 0000.0000.0000

localhost#show vxlan flood vtep vlan 10
          VXLAN Flood VTEP Table
--------------------------------------------------------------------------------

VLANS                            Ip Address
-----------------------------   ------------------------------------------------
10                              203.0.255.133

```

此時，我們可以嘗試從 **host\_1** ping **host\_3**：

```routeros
[admin@host_1] /interface> print
...
1 R ether2  ether           1500  0C:50:85:84:00:01

[admin@host_1] /ip/address> /ping 192.168.10.129
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 192.168.10.129                             56  64 17ms26us
    1 192.168.10.129                             56  64 13ms119us
    2 192.168.10.129                             56  64 17ms192us
```

**host-3**

```routeros
[admin@host_1] /interface> print
...
1 R ether2  ether           1500  0C:74:39:88:00:01
```

現在，透過檢視 MACIP 路由，我們應該能夠看到 EVPN 用於學習遠端 MAC 地址。

如果檢視 **ros\_leaf** 上的路由，我們可以看到路由器 203.0.255.128 傳送了 0C:74:39:88:00:01 MAC 地址的 macip 路由，該 MAC 地址是位於 **eos\_leaf** 後面的 **host\_1** 的 MAC 地址。

EOS 還會發送 MAC/IP 繫結，用於 ARP/ND 抑制。遺憾的是，在撰寫本文時，RouterOS 尚不具備此功能。

```routeros
[admin@ros_leaf_3] /routing/route> print where dst-address~"macip"
Flags: A - ACTIVE; b - BGP, e - EVPN
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS                                                   GATEWAY        AFI   DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW
Ab [203.0.255.128:1010]macip:0|0C:74:39:88:00:01                 203.0.255.128  evpn        20     40            30  172.16.3.1%ether10
 e [203.0.255.133:256]macip:0|0C:50:85:84:00:01                  203.0.255.133  evpn       200     40            10
Ab [203.0.255.128:1010]macip:0|0C:74:39:88:00:01|192.168.10.129  203.0.255.128  evpn        20     40            30  172.16.3.1%ether10
```

Arista 還允許在 "vxlan mac table" 中檢視遠端學習到的 MAC 地址，"vlan mac-address table" 也包括本地 MAC 地址：

```
localhost#show bgp evpn route-type mac-ip detail
BGP routing table information for VRF default
Router identifier 203.0.255.128, local AS number 65005
BGP routing table entry for mac-ip 0c50.8584.0001, Route Distinguisher: 203.0.255.133:256
 Paths: 1 available
  65000 65003
    203.0.255.133 from 203.0.255.138 (203.0.255.138)
      Origin IGP, metric -, localpref 100, weight 0, tag 0, valid, external, best
      Extended Community: Route-Target-AS:1010:1010 TunnelEncap:tunnelTypeVxlan
      VNI: 0 ESI: 0000:0000:0000:0000:0000
BGP routing table entry for mac-ip 0c74.3988.0001, Route Distinguisher: 203.0.255.128:1010
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, tag 0, valid, local, best
      Extended Community: Route-Target-AS:1010:1010 TunnelEncap:tunnelTypeVxlan
      VNI: 1010 ESI: 0000:0000:0000:0000:0000
BGP routing table entry for mac-ip 0c74.3988.0001 192.168.10.129, Route Distinguisher: 203.0.255.128:1010
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, tag 0, valid, local, best
      Extended Community: Route-Target-AS:1010:1010 TunnelEncap:tunnelTypeVxlan
      VNI: 1010 ESI: 0000:0000:0000:0000:0000

localhost#show vxlan address-table vlan 10
          Vxlan Mac Address Table
----------------------------------------------------------------------

VLAN  Mac Address     Type      Prt  VTEP             Moves   Last Move
----  -----------     ----      ---  ----             -----   ---------
  10  0c50.8584.0001  EVPN      Vx1  203.0.255.133    1       1:30:49 ago
Total Remote Mac Addresses for this criterion: 1

localhost#show mac address-table vlan 10
          Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports      Moves   Last Move
----    -----------       ----        -----      -----   ---------
  10    0c50.8584.0001    DYNAMIC     Vx1        1       1:31:17 ago
  10    0c74.3988.0001    DYNAMIC     Et2        1       1 day, 23:45:18 ago
Total Mac Addresses for this criterion: 2

          Multicast Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       ----        -----
Total Mac Addresses for this criterion: 0
```

### 使用 Arista ESI LAG 的橋接 EVPN 覆蓋網路 {#bridged-evpn-overlay-with-arista-esi-lag}

**ESI-LAG**（Ethernet Segment Identifier - Link Aggregation，乙太網段識別符號 - 鏈路聚合）或 **EVPN-LAG** 是一種網路概念，它使用 **EVPN**（Ethernet Virtual Private Network，乙太網虛擬專用網路）技術實現多宿主，其中用戶端裝置（如接入交換器）可以透過多條鏈路連線到核心裝置（如分佈交換器），形成一個邏輯 **LAG** 介面。

#### 拓撲 {#topology-1}

讓我們擴充套件上一個示例中的拓撲。**Host\_2** 是一臺 RouterOS 裝置，在連線到兩個 Arista leaf 的鏈路上啟用了 **LACP**，形成 active-active 多宿主設定。

![](/img/f668d4d418b4df89.jpg#gh-light-mode-only)
![](/img/cab72d55ae5e371e.png#gh-dark-mode-only)

#### 配置先決條件 {#configuration-prerequisities}

有關設定 underlay 和 EVPN overlay 的詳細資訊，請參閱上面的示例。本節重點介紹 ESI LAG 配置和驗證。

#### Port Channel 配置 {#port-channel-configuration}

假設 underlay 和 overlay 已配置並正在執行，接下來在 Arista 交換器上進行 port-channel 配置：

**leaf\_2** 和 **leaf\_4** 的配置完全相同

```
interface Port-Channel3
   switchport access vlan 10
   switchport trunk allowed vlan 10
   switchport mode trunk
   !
   evpn ethernet-segment
      identifier 0000:0000:0000:0333:3333
      route-target import 00:00:03:33:33:33
   lacp system-id 0000.0333.3333
!
interface Ethernet2
   channel-group 3 mode active
```

**ros\_host\_2**

```routeros
/interface/bonding
add mode=802.3ad name=bond1 slaves=ether2,ether3
/interface/vlan
add interface=bond1 mtu=1496 name=vlan10 vlan-id=10
/ip/address
add address=192.168.10.130/24 interface=vlan10
```

#### 驗證設定 {#validate-setup}

現在，如果檢視 EVPN 路由，我們應該會看到一些新的路由型別。兩臺 Arista 交換器都在通告 Type-1 AD 路由和 Type-4 Ethernet Segment（ES）路由，以發現多宿主 VTEP。

```routeros
[admin@gns3_spine1_ros] /routing/route>  print where afi=evpn dst-address~"(ad|es)"
Flags: A - ACTIVE; b - BGP
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
   DST-ADDRESS                                                      GATEWAY        AFI   DISTANCE  SCOPE  TA
Ab [203.0.255.127:1]ad:4294967295|00:00:00:00:00:00:03:33:33:33     203.0.255.127  evpn        20     40  30
Ab [203.0.255.127:1]es:00:00:00:00:00:00:03:33:33:33|203.0.255.127  203.0.255.127  evpn        20     40  30
Ab [203.0.255.127:1010]ad:0|00:00:00:00:00:00:03:33:33:33           203.0.255.127  evpn        20     40  30

Ab [203.0.255.134:1]ad:4294967295|00:00:00:00:00:00:03:33:33:33     203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1]es:00:00:00:00:00:00:03:33:33:33|203.0.255.134  203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1010]ad:0|00:00:00:00:00:00:03:33:33:33           203.0.255.134  evpn        20     40  30

```

如果檢查兩臺 EOS leaf，我們會看到指定轉發器 203.0.255.127（**eos\_leaf\_4**）被選中：

```
eos_leaf_2#show bgp evpn instance vlan 10
EVPN instance: VLAN 10
  Route distinguisher: 203.0.255.134:1010
  Route target import: Route-Target-AS:1010:1010
  Route target export: Route-Target-AS:1010:1010
  Service interface: VLAN-based
  Local VXLAN IP address: 203.0.255.134
  VXLAN: enabled
  MPLS: disabled
  Local ethernet segment:
    ESI: 0000:0000:0000:0333:3333
      Type: 0 (administratively configured)
      Interface: Port-Channel3
      Mode: all-active
      State: up
      ES-Import RT: 00:00:03:33:33:33
      DF election algorithm: modulus
      Designated forwarder: 203.0.255.127
      Non-Designated forwarder: 203.0.255.134

```

讓我們掛起從 **host2** 到 **eos\_leaf\_4** 的鏈路，並觀察結果：

```
eos_leaf_2#show bgp evpn instance vlan 10
EVPN instance: VLAN 10
  Route distinguisher: 203.0.255.134:1010
  Route target import: Route-Target-AS:1010:1010
  Route target export: Route-Target-AS:1010:1010
  Service interface: VLAN-based
  Local VXLAN IP address: 203.0.255.134
  VXLAN: enabled
  MPLS: disabled
  Local ethernet segment:
    ESI: 0000:0000:0000:0333:3333
      Type: 0 (administratively configured)
      Interface: Port-Channel3
      Mode: all-active
      State: up
      ES-Import RT: 00:00:03:33:33:33
      DF election algorithm: modulus
      Designated forwarder: 203.0.255.134

[admin@spine1_ros] /routing/route>  print interval=1 where dst-address~"ad|es"
Flags: A - ACTIVE; b - BGP
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
   DST-ADDRESS                                                      GATEWAY        AFI   DISTANCE  SCOPE  TA
Ab [203.0.255.134:1]ad:4294967295|00:00:00:00:00:00:03:33:33:33     203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1]es:00:00:00:00:00:00:03:33:33:33|203.0.255.134  203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1010]ad:0|00:00:00:00:00:00:03:33:33:33           203.0.255.134  evpn        20     40  30

[admin@host_2] /interface/bonding> /ping 192.168.10.132 interval=500ms
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 192.168.10.132                             56  64 2ms90us
    1 192.168.10.132                             56  64 2ms172us
    2 192.168.10.132                             56  64 2ms503us
    3 192.168.10.132                                               timeout
    4 192.168.10.132                                               timeout
    5 192.168.10.132                                               timeout
    6 192.168.10.132                             56  64 2ms191us
    7 192.168.10.132                             56  64 2ms31us
```

**eos\_leaf\_2** 成為轉發器，**eos\_leaf\_4** 撤銷 ES 和 AD 路由，流量切換到另一條 LACP 鏈路。
