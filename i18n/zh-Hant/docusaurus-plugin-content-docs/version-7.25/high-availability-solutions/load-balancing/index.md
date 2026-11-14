---
sidebar_key: "high-availability-solutions/load-balancing/index"
sidebar_position: 3
title: "負載均衡"
sidebar_label: "負載均衡"
description: "MikroTik RouterOS 中的網路負載均衡允許在無需動態路由的情況下將流量分配到多條鏈路上，並提供按連線或按封包的方法選項。該文件包含設定示例，例如故障轉移配置，以及使用 firewall mangle、bonding、OSPF 和 ECMP 對負載均衡技術進行的比較。"
tags:
  - 'load-balancing'
  - 'firewall-mangle'
  - 'bonding'
source: https://manual.mikrotik.com/docs/7.25/high-availability-solutions/load-balancing
captured_at: '2026-11-04T11:17:43+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

- [故障轉移（WAN 備份）](./failover-wan-backup.md)
- [防火牆標記](../../firewall-and-quality-of-service/firewall/mangle.md)
- [Bonding 負載均衡](../bonding.md)
- [OSPF 負載均衡](../../user-guides/routing-and-networking-protocols/unicast/ospf/index.md)
- [按連線分類器](./per-connection-classifier.md)

## 簡介 {#introduction}

網路負載均衡是指將流量分攤到兩條或更多鏈路上的能力。

負載均衡方法有兩種：

- per-packet - 單個流的每個包都可以透過不同鏈路轉發。只有在能夠控制兩個負載均衡端點時，此方法才能可靠工作，尤其是在 TCP 和安全連線上。
- per-connection - 同一連線（流）的所有包始終透過一條鏈路傳送。在只有一端負載均衡受我們控制的設定中，此方法是必需的，例如帶有多條 WAN 連線的家庭路由器。

| 方法 |  | Per-connection | Per-packet |
| :-- | :-- | :-- | :-- |
|  Firewall Mangle | Nth | **是** | **是** |
|  | PCC (Per Connection Classifier) | **是** | no |
|  | 其他匹配器 | **是** | **是** |
| ECMP (Equal Cost Multi-Path) |  | **是** | **否** |
| Bonding |  | no | **是** |
| OSPF |  | **是** | no |
| BGP |  | **是** | no |

## 簡單故障轉移示例 {#simple-failover-example}

最簡單的故障轉移設定是使用多個閘道器：一個閘道器處於 active 狀態，另一個閘道器在第一個閘道器故障時接管。

為此，請為備用閘道器配置更大的 **distance** 值，併為第一個閘道器配置 **check-gateway**：

```ros
/ip/route/add gateway=192.168.1.1 distance=1 check-gateway=ping
/ip/route/add gateway=192.168.2.1 distance=2
```

*check-gateway* 會確保僅當實際流量能夠到達閘道器時，該閘道器才處於 up 狀態。當 ping 失敗時，第一個閘道器將變為 inactive，第二個閘道器將接管；當第一個閘道器恢復時，它將變為 active，並讓第二個閘道器再次作為備份工作。

## 相關主題 {#related-topics}

<DocCardList />
