---
sidebar_key: "routing-and-networking-protocols/multicast/pim-sm"
sidebar_position: 3
title: "PIM-SM"
sidebar_label: "PIM-SM"
description: "本頁介紹 MikroTik RouterOS 中的 IP 組播和協定無關組播 - 稀疏模式（PIM-SM），說明它如何實現跨網路的高效資料共享。內容包括用於在獨立介面之間進行組播路由的 PIM-SM 基本配置，涵蓋介面設定、PIM 例項建立以及 IGMP 整合。"
tags:
  - 'pim-sm'
  - 'igmp'
  - 'ospf'
slug: /user-guides/routing-and-networking-protocols/multicast/pim-sm
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/multicast/pim-sm
captured_at: '2026-11-04T11:22:41+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

IP 組播是一種允許透過 Internet 與許多接收者高效共享資料的技術。傳送端將其資料傳輸到特定的組播 IP 地址，接收端表示有興趣接收發送到該地址的資料。然後網路負責將資料從傳送端傳遞到接收端。

如果某個組播組的傳送端和接收端位於同一本地網段，則該過程不需要路由器。通訊可以直接進行，並且可以透過使用 [IGMP 偵聽](../../../bridging-and-switching/user-guides/bridge-igmp-mld-snooping.md) 交換器來增強。但是，如果傳送端和接收端位於不同網段，則必須使用組播路由協定來建立它們之間的資料傳輸路徑。

協定無關組播 - 稀疏模式（PIM-SM 或 PIM）使 RouterOS 能夠支援網路區域內的組播流傳輸。PIM 代表協定無關組播，這意味著它不繫結到任何特定的單播路由。SM 代表稀疏模式，這意味著特定控制訊息確保資料僅傳遞到有接收者需要它的網段。除了管理網段之間資料傳輸的路由協定之外，路由器還需要一種方法來發現其直連網段上的本地接收者。對於 IPv4，這透過 Internet 組管理協定（IGMP）實現；對於 IPv6，則透過組播偵聽者發現（MLD）實現。

![](/img/6708aabff35dbf61.webp)

:::info
RouterOS v7 在主 **system** 軟體包中提供 PIM-SM 配置。較舊的 RouterOS 版本需要安裝額外的 **multicast** 軟體包才能使用 PIM-SM。有關 [軟體包](../../../getting-started/installation-and-upgrade/packages.md) 的更多詳細資訊。

該功能在 SMIPS 裝置（hAP lite、hAP lite TC 和 hAP mini）上不受支援。
:::

## 單裝置上的基本組播路由 {#basic-multicast-routing-on-single-device}

設想這樣一個場景：你有一臺具有兩個介面（即 ether1 和 ether2）的路由器，並且每個介面都設定在獨立的網路中。通常情況下，路由器會建立直連路由，並且兩個網路上的主機將能夠使用單播流量進行通訊。但是，如果要在這些網路之間啟用組播通訊，則需要單獨配置組播路由，否則無法工作。在此場景中，我們將建立一個簡單配置。這包括建立 PIM 例項並配置所需介面。

![](/img/8c9bb4fc76a4a35b.webp)

首先確保已在路由器介面上設定 IP 地址。

```ros
/ip/address
add address=192.168.10.1/24 interface=ether1 network=192.168.10.0
add address=192.168.20.1/24 interface=ether2 network=192.168.20.0
```

配置 PIM 例項。對於此示例，預設設定應該可以正常工作。

```ros
/routing/pimsm/instance
add name=pimsm-instance-1
```

為將接收組播流量的介面新增 PIM 介面模板。

```ros
/routing/pimsm/interface-template
add interfaces=ether1 instance=pimsm-instance-1
```

在 ether2 上配置 IGMP 查詢器，以便 PIM 例項可以瞭解本地組成員關係。

```ros
/routing/pimsm/igmp-interface-template
add instance=pimsm-instance-1 interfaces=ether2
```

現在，路由器開始監聽 IGMP 成員報告（用戶端加入訊息），並將組播流量路由到有興趣接收它的用戶端。

要測試該配置，你可以使用 RouterOS [traffic-generator](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) 配置組播發送端，並使用 [GMP](./group-management-protocol.md) 配置 IGMP 用戶端。

```ros
# 组播发送者
/ip/address
add address=192.168.10.10/24 interface=ether1 network=192.168.10.0
/tool/traffic-generator/packet-template
add interface=ether1 ip-dst=229.1.1.2 mac-dst=01:00:5E:01:01:02/FF:FF:FF:FF:FF:FF name=multicast
/tool/traffic-generator/quick tx-template=multicast mbps=10

# 组播客户端
/ip/address
add address=192.168.20.10/24 interface=ether1 network=192.168.20.0
/routing/gmp
add disabled=no groups=229.1.1.2 interfaces=ether1
```

要驗證組播流量是否被正確路由，請監控用戶端介面上接收的封包計數器，或使用 [Torch](../../../diagnostics-monitoring-and-troubleshooting/torch.md) 或 [封包嗅探器](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) 等工具。

還可以監控路由器上的活動組播組：

```ros
/routing/pimsm/uib-g/print
Columns: INSTANCE, GROUP
# INSTANCE          GROUP    
0 pimsm-instance-1  229.1.1.2

/routing/pimsm/uib-sg/print
Flags: K - KEEPALIVE; S - SPT-BIT
Columns: INSTANCE, GROUP, SOURCE
#    INSTANCE          GROUP      SOURCE       
0 KS pimsm-instance-1  229.1.1.2  192.168.10.10

```

## 使用靜態 RP 的組播路由 {#multicast-routing-with-static-rp}

在接下來的示例中，我們將使用多臺 PIM 路由器，如下圖所示。PIM-SM 使用共享樹，為使此機制正常工作，我們需要指定一個特定節點作為組播根分發點。在 PIM 中，該路由器稱為匯聚點（Rendezvous Point），或 RP。在 PIM 中有多種選擇 RP 的方法，例如引導路由器（BSR）方法。但是，對於此示例，我們將使用一種稱為靜態 RP 配置的簡單方法。這意味著管理員可以為特定組播組手動指定一個或多個 RP。

![](/img/456509a833c70101.webp)

首先，我們需要配置 IP 地址並設定單播路由。在此示例中，我們將使用 OSPF 在路由器之間交換路由資訊。有關 [OSPF](../unicast/ospf/index.md) 的更多詳細資訊。

```ros
# R1 汇聚点：
/ip/address
add address=10.0.0.1 interface=lo network=10.0.0.1
add address=10.0.1.1/24 interface=ether2 network=10.0.1.0
add address=10.0.2.1/24 interface=ether3 network=10.0.2.0
/routing/ospf/instance
add disabled=no name=ospf-instance-1 router-id=10.0.0.1
/routing/ospf/area
add disabled=no instance=ospf-instance-1 name=ospf-area-1
/routing/ospf/interface-template
add area=ospf-area-1 disabled=no interfaces=lo,ether2,ether3

# R2:
/ip/address
add address=10.0.0.2 interface=lo network=10.0.0.2
add address=10.0.1.2/24 interface=ether1 network=10.0.1.0
add address=192.168.20.1/24 interface=ether12 network=192.168.20.0
/routing/ospf/instance
add disabled=no name=ospf-instance-1 router-id=10.0.0.2
/routing/ospf/area
add disabled=no instance=ospf-instance-1 name=ospf-area-1
/routing/ospf/interface-template
add area=ospf-area-1 disabled=no interfaces=lo,ether1,ether12

# R3:
/ip/address
add address=10.0.0.3 interface=lo network=10.0.0.3
add address=10.0.2.3/24 interface=ether1 network=10.0.2.0
add address=192.168.30.1/24 interface=ether12 network=192.168.30.0
/routing/ospf/instance
add disabled=no name=ospf-instance-1 router-id=10.0.0.3
/routing/ospf/area
add disabled=no instance=ospf-instance-1 name=ospf-area-1
/routing/ospf/interface-template
add area=ospf-area-1 disabled=no interfaces=lo,ether1,ether12
```

與之前單路由器示例一樣，我們需要配置 PIM 例項並在所有路由器上新增必要的介面。

```ros
# R1 汇聚点：
/routing/pimsm/instance
add disabled=no name=pimsm-instance-1
/routing/pimsm/interface-template
add instance=pimsm-instance-1 interfaces=lo,ether2,ether3

# R2:
/routing/pimsm/instance
add disabled=no name=pimsm-instance-1
/routing/pimsm/interface-template
add instance=pimsm-instance-1 interfaces=lo,ether1,ether12
/routing/pimsm/igmp-interface-template
add instance=pimsm-instance-1 interfaces=ether12

# R3:
/routing/pimsm/instance
add disabled=no name=pimsm-instance-1
/routing/pimsm/interface-template
add instance=pimsm-instance-1 interfaces=lo,ether1,ether12
/routing/pimsm/igmp-interface-template
add instance=pimsm-instance-1 interfaces=ether12

```

現在，讓我們檢視 PIM 鄰居及其當前狀態。在 R1 上有兩個鄰居，而在 R2 和 R3 上各只有一個鄰居。

```ros
# R1 汇聚点：
/routing/pimsm/neighbor/print
Flags: R - DESIGNATED-ROUTER; J - JOIN-TRACKING
Columns: INSTANCE, ADDRESS, PRIORITY
#    INSTANCE          ADDRESS          PRIORITY
0 RJ pimsm-instance-1  10.0.1.2%ether2  1       
1 RJ pimsm-instance-1  10.0.2.3%ether3  1       

# R2:
/routing/pimsm/neighbor/print 
Flags: R - DESIGNATED-ROUTER; J - JOIN-TRACKING
Columns: INSTANCE, ADDRESS, PRIORITY
#    INSTANCE          ADDRESS          PRIORITY
0  J pimsm-instance-1  10.0.1.1%ether1  1       

# R3:
/routing/pimsm/neighbor/print 
Flags: J - JOIN-TRACKING
Columns: INSTANCE, ADDRESS, PRIORITY
#   INSTANCE          ADDRESS          PRIORITY
0 J pimsm-instance-1  10.0.2.1%ether1  1       

```

最後，我們將選擇一臺路由器作為我們的匯聚點（RP）。我們將在所有 PIM 路由器上配置 R1 環回 IP 地址。確保每臺路由器都具有到達 R1 環回地址的正確路由資訊非常重要。

```ros
# R1 汇聚点：
/routing/pimsm/static-rp
add address=10.0.0.1 instance=pimsm-instance-1

# R2:
/routing/pimsm/static-rp
add address=10.0.0.1 instance=pimsm-instance-1

# R3:
/routing/pimsm/static-rp
add address=10.0.0.1 instance=pimsm-instance-1
```
