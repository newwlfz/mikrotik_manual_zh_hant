---
sidebar_key: "routing-and-networking-protocols/multicast/igmp-proxy"
sidebar_position: 2
title: "IGMP 代理"
sidebar_label: "IGMP 代理"
description: "RouterOS 中的 IGMP Proxy 功能透過轉發 IGMP 幀來實現組播路由，為某些拓撲提供比 PIM-SM 更簡單的替代方案。它支援基本的組播轉發且資源佔用極低，但不支援複雜路由設定和環路檢測。"
tags:
  - 'igmp'
  - 'multicast'
  - 'routing'
slug: /user-guides/routing-and-networking-protocols/multicast/igmp-proxy
source: https://manual.mikrotik.com/docs/7.25/user-guides/routing-and-networking-protocols/multicast/igmp-proxy
captured_at: '2026-11-04T11:22:31+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Internet Group Management Protocol（IGMP）代理可以實現組播路由。它轉發 IGMP 幀，通常用於不需要像 PIM 這樣更高階協定的場景。

## IGMP 代理功能 {#igmp-proxy-features}

- 實現組播路由的最簡單方式。
- 可用於因某些原因不適合使用 PIM-SM 的拓撲。
- 相比 PIM-SM 佔用的資源略少。
- 配置簡單。

另一方面，IGMP 代理不太適合複雜的組播路由設定。與基於 PIM 的解決方案相比，IGMP 代理不支援多個上游介面，並且不會檢測或避免路由環路。

預設情況下，IGMP 代理上游介面會發送 IGMPv3 成員報告，並會根據收到的查詢檢測上游裝置（例如組播路由器）正在使用的 IGMP 版本。如果收到 IGMPv1/v2 查詢，上游埠將回退到較低的 IGMP 版本。當 IGMPv1/v2 查詢器存在計時器（400s）到期後，它將轉換回 IGMPv3。IGMP 代理的下游介面只會傳送 IGMPv2 查詢。

:::warning
RouterOS v7 在主 **system** 軟體包中提供了 IGMP 代理配置。較舊的 RouterOS 版本需要安裝額外的 **multicast** 軟體包才能使用 IGMP 代理。有關 [軟體包](../../../getting-started/installation-and-upgrade/packages.md) 的更多詳細資訊，請參閱。
:::

## 示例 {#examples}

---

要將來自 ether2 介面的所有組播資料轉發到連線訂閱者的下游 bridge 介面，請使用以下配置。兩個介面都應具有 IP 地址。

```ros
/routing/igmp-proxy/interface
add interface=ether2 upstream=yes
add interface=bridge1

[admin@MikroTik] /routing/igmp-proxy/interface/print
Columns: INTERFACE, UPSTREAM, THRESHOLD, ROBUSTNESS, QUERY-INTERVAL, 
         QUERY-RESPONSE-INTERVAL, LAST-MEMBER-QUERY-INTERVAL
#   INTERFACE  UPSTREAM  THRESHOLD  ROBUSTNESS  QUERY-INTERVAL  QU  LA
0   ether2     yes               1                                    
1   bridge1     no               1           2  2m5s           10s  1s
```

如果組播發送方地址位於本地路由器無法直接訪問的 IP 子網中，您可能還需要在上游介面上配置 `alternative-subnets`：

```ros
/routing/igmp-proxy/interface
set [find upstream=yes] alternative-subnets=192.168.50.0/24,192.168.60.0/24
```
