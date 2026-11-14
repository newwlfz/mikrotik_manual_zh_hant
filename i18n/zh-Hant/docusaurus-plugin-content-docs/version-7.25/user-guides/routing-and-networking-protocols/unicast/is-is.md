---
sidebar_key: "routing-and-networking-protocols/unicast/is-is"
sidebar_position: 4
title: "IS-IS"
sidebar_label: "IS-IS"
description: "IS-IS 是一種內部閘道器協定，用於在單個自治系統內分發 IP 路由資訊，作為鏈路狀態協定執行，並在鄰居之間交換拓撲資料。它支援 IPv4 和 IPv6，使用基於 TLV 的擴充套件，並且需要配置 area ID、system ID 和 NSAP 地址才能實現正確路由。"
tags:
  - 'is-is'
  - 'routing'
  - 'ospf'
slug: /user-guides/routing-and-networking-protocols/unicast/is-is
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/unicast/is-is
captured_at: '2026-11-04T11:22:48+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

IS-IS（Intermediate System - Intermediate System）協定是一種內部閘道器協定（IGP），用於在單個自治系統內分發 IP 路由資訊。

它最初是作為 CLNP 的路由協定開發的，但後來在 IP 流行時擴充套件為包含 IP 路由。擴充套件版本有時稱為 Integrated IS-IS。

IS-IS 屬於鏈路狀態協定族，該協定族在最近的鄰居之間交換拓撲資訊，並將其泛洪到整個 AS。主要優點是，對網路拓撲的完整了解允許路由器選擇到達目的地的最佳路徑。它還可以用於流量工程目的。

鄰居定期交換 **Hello** 報文，形成鄰接關係，並根據協商結果選擇指定 IS（DIS）。Hello 報文分別針對 **Level-1** 和 **Level-2** 傳送。

## 標準與技術 {#standards-and-technologies}

- [RFC 1195](https://datatracker.ietf.org/doc/html/rfc1195) 在 TCP/IP 和雙環境中使用 OSI IS-IS 進行路由
- [RFC 5302](https://datatracker.ietf.org/doc/html/rfc5302) 兩級 IS-IS 的域範圍字首分發
- [RFC 5303](https://datatracker.ietf.org/doc/html/rfc5303) IS-IS 點對點鄰接的三次握手
- [RFC 5305](https://datatracker.ietf.org/doc/html/rfc5305) IS-IS 流量工程擴充套件（僅支援 wide metric）
- [RFC 5308](https://datatracker.ietf.org/doc/html/rfc5308) 使用 IS-IS 路由 IPv6

## IS-IS 術語 {#is-is-terminology}

- **IS** - 中間系統是一種能夠在相距較遠的主機之間轉發流量的路由器。
- **LSP** - 鏈路狀態 PDU 包含路由器本地狀態的資訊（可用介面、可達鄰居以及介面開銷）。參見 [`/routing/isis/lsp`](../../../cli-reference/routing/isis/lsp.md)。
- **SPF** - 最短路徑優先演算法。
- **DIS** - 指定中間系統。DIS 確保網路中的所有路由器維護同步的資料庫。L1 和 L2 路由分別選舉不同的 DIS。DIS 的選舉基於最高的介面優先順序。
- **Level-1 (L1) routing** - 控制 IS-IS 區域內路由資訊的分佈。L1 路由基於 system ID。
- **Level-2 (L2) routing** - 控制 IS-IS 區域之間路由資訊的分佈。L2 路由基於 area ID。
- **IS-IS 鄰接關係** - IS-IS 鄰居之間的鏈路（參見 [`/routing/isis/neighbor`](../../../cli-reference/routing/isis/neighbor.md)）。形成的鄰接型別取決於 IS-IS Hello 報文中交換的引數。每個相鄰路由器都會執行 DIS 選舉過程，以確定它是否有資格在廣播網路上成為 L1 或 L2 DIS。
- **NSAP** - 用於標識路由器的網路服務訪問點地址。
- **NET** - 網路實體標題。最後一個位元組始終設定為零的 NSAP 地址。

## 協定基礎 {#protocol-basics}

IS-IS 協定基於 TLV（Type/Length/Value），因此易於擴充套件。它使用 OSI 定址原則，並且 NSAP 地址是按節點分配的，而不是按介面分配。

NSAP 地址分為三部分：

```
+-----+------+-----------+----+
| AFI | Area | System-ID | NS |
+-----+------+-----------+----+
```

- **AFI** - 最左側的第一個位元組定義 NSAP 地址的含義。IS-IS 的 [`afi`](../../../cli-reference/routing/isis/instance.md#afi) 引數控制例項處理的地址族。
- **Area ID** - 2 個八位組。
- 大多數 IS-IS 實現使用 6 個八位組的 **System-ID**。
- **NS**（N-selector）- 一個位元組，並且 IS-IS 始終將其設定為零。

地址以十六進位制字串形式書寫，每兩個位元組的部分用點分隔，但有一些例外。
例如，NET 地址 `49222211112222aded00` 寫作 `49.2222.1111.2222.aded.00`：

- 最左側的點分隔 AFI（2 個字元）。
- 隨後是 Area ID（4 個字元）。
- 隨後是 System ID，它被分成 3 組、每組 4 個字元。
- 最右側的點必須位於 System ID 和 N-selector 之間。

RouterOS 將 NET 地址拆分到兩個配置選項中。前 3 個位元組（AFI 和 Area）透過 [`areas`](../../../cli-reference/routing/isis/instance.md#areas) 引數配置，接下來的 6 個位元組是 System ID，透過 [`system-id`](../../../cli-reference/routing/isis/instance.md#system-id) 引數配置，而最後一個 NS 位元組不會在任何地方顯式配置。它始終被假定為零。

某些其他廠商的實現可能要求將 AFI 位元組設定為特定值，例如，`0x47` 表示經典的 ISO NSAP 地址。
此外，`0x49` 可以用作私有地址空間，類似於 IPv4 私有地址範圍（10.0.0.0/8 等）。

## 基本配置示例 {#basic-configuration-example}

基本配置需要建立一個例項（位於 [`/routing/isis/instance`](../../../cli-reference/routing/isis/instance.md) 下）並設定區域 ID 和系統 ID，同時透過 [`/routing/isis/interface-template`](../../../cli-reference/routing/isis/interface-template.md) 在介面上啟用 IS-IS。

例如，在三臺路由器之間建立一個 IS-IS 設定，其中一臺是 Cisco，兩臺是 RouterOS。

**R1:**

```ros
/routing/isis/instance
add afi=ip areas=49.2222 disabled=no name=isis-instance-1 system-id=90ab.cdef.0001
/routing/isis/interface-template
add instance=isis-instance-1 interfaces=ether1 levels=l1,l2

[] /routing/isis/neighbor> print 
 0 instance=isis-instance-1 interface=ether1 level-type=l2 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 1 instance=isis-instance-1 interface=ether1 level-type=l2 snpa=D4:CA:6D:78:2F:2E srcid="1111.2222.cded" state=up 

 2 instance=isis-instance-1 interface=ether1 level-type=l1 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 3 instance=isis-instance-1 interface=ether1 level-type=l1 snpa=D4:CA:6D:78:2F:2E srcid="1111.2222.cded" state=up 

[] /routing/route> print where is-is
Flags: A - ACTIVE; i - IS-IS
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS        GATEWAY                AFI  DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW         
 i 0.0.0.0/0          10.155.101.214%ether1  ip4       115     20            10  10.155.101.214%ether1
 i 10.155.101.0/24    10.155.101.216%ether1  ip4       115     20            10  10.155.101.216%ether1
Ai 10.255.255.162/32  10.155.101.216%ether1  ip4       115     20            10  10.155.101.216%ether1

```

**R2:**

```ros
/routing/isis/instance
add afi=ip areas=49.2222 disabled=no l1.originate-default=always l2.originate-default=always name=isis-instance-1 \
    system-id=1111.2222.cded
/routing/isis/interface-template
add instance=isis-instance-1 interfaces=sfp12 levels=l1,l2
add instance=isis-instance-1 interfaces=lo levels=l2

[] /routing/isis/neighbor> print 
 0 instance=isis-instance-1 interface=sfp12 level-type=l1 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 1 instance=isis-instance-1 interface=sfp12 level-type=l1 snpa=C4:AD:34:43:EA:5C srcid="90ab.cdef.0001" state=up 

 2 instance=isis-instance-1 interface=sfp12 level-type=l2 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 3 instance=isis-instance-1 interface=sfp12 level-type=l2 snpa=C4:AD:34:43:EA:5C srcid="90ab.cdef.0001" state=up 

```

**R3 Cisco:**

```ros
interface Loopback0
 ip address 10.255.255.162 255.255.255.255
 ip router isis 
!
interface GigabitEthernet1
 ip address dhcp
 ip router isis 
 negotiation auto
!
router isis
 net 49.2222.1111.2222.aded.00
!

# show isis neighbors 

Tag null:
System Id      Type Interface   IP Address      State Holdtime Circuit Id
90AB.CDEF.0001 L1   Gi1         10.155.101.183  UP    27       1111.2222.CDED.01  
90AB.CDEF.0001 L2   Gi1         10.155.101.183  UP    27       1111.2222.CDED.01  
1111.2222.CDED L1   Gi1         10.155.101.214  UP    9        1111.2222.CDED.01  
1111.2222.CDED L2   Gi1         10.155.101.214  UP    9        1111.2222.CDED.01 

# show ip route

i*L1  0.0.0.0/0 [115/11] via 10.155.101.214, 4w5d, GigabitEthernet1
      10.0.0.0/8 is variably subnetted, 5 subnets, 2 masks
C        10.155.101.0/24 is directly connected, GigabitEthernet1
L        10.155.101.216/32 is directly connected, GigabitEthernet1
i L2     10.155.255.214/32 [115/10] via 10.155.101.183, 2w3d, GigabitEthernet1

```

## 故障排除 {#troubleshooting}

### IS-IS 無法工作並列印警告訊息 "invalid 3way tlv" {#is-is-does-not-work-and-prints-the-warning-message-invalid-3way-tlv}

此警告表明，遠端鄰居很可能不符合 RFC 5303 中針對點對點網路的 3-way handshake。例如，在 Cisco 上，必須在介面上啟用 "isis three-way-handshake ietf" 才能具有 15 位元組的 TLV。
