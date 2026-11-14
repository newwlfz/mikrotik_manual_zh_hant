---
sidebar_key: "high-availability-solutions/load-balancing/failover-wan-backup"
sidebar_position: 1
title: "故障轉移（WAN 備份）"
sidebar_label: "故障轉移"
description: "本頁說明如何在 MikroTik RouterOS 中使用遞迴路由為 WAN 連線配置故障轉移，並詳細介紹了使用基礎監控配置和改進監控配置的設定步驟，以實現可靠的鏈路切換。"
tags:
  - 'failover'
source: https://manual.mikrotik.com/docs/7.24/high-availability-solutions/load-balancing/failover-wan-backup
captured_at: '2026-11-04T11:29:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

本文介紹一種使用遞迴路由和路由作用域的高階故障轉移方法。當一條路由（靜態或動態學習的）具有未直接連線到本地路由器的下一跳時，就會發生遞迴路由。有必要限制可用於查詢直接下一跳的路由集合。例如，RIP 或 OSPF 路由的下一跳值應當是可直接到達的，並且只能使用直連路由來查詢。這可以透過使用 scope 和 target-scope 屬性來實現。

## 設定概覽 {#setup-overview}

假設我們的閘道器有兩條公網上行鏈路（"ISP1"、"ISP2"）。第一條上行鏈路應優先使用，第二條應作為備份。

然後我們將流量分成兩部分進行標記：一部分命名為 "ISP1"，另一部分命名為 "ISP2"，並分別透過 ether1 和 ether2。在此設定中，我們希望監控兩臺主機：Host1 和 Host2。我們將使用 IP 為 8.8.8.8（Host1）和 8.8.4.4（Host2）的 Google DNS 伺服器，但並非必須使用這些特定地址。

![failover.png](/img/e885236b5be34b63.webp)

## 配置 {#configuration}

### 基本故障轉移 {#basic-failover}

在配置故障轉移之前，我們必須對經過兩條上行鏈路的 LAN 流量進行偽裝。這允許本地網路中的裝置透過任一連線訪問網際網路：

```ros
/ip/firewall/nat
add chain=srcnat action=masquerade out-interface=ether1
add chain=srcnat action=masquerade out-interface=ether2
```

接下來，我們需要在網際網路上定義兩臺可訪問的主機，以監控每條上行鏈路的狀態。這些主機應當可靠並響應 ICMP 請求。在本示例中，我們使用 Google 的 DNS 伺服器（8.8.8.8 和 8.8.4.4）：

```ros
/ip/route 
add dst-address=8.8.8.8 scope=10 gateway=10.111.0.1
add dst-address=8.8.4.4 scope=10 gateway=10.112.0.1
```

最後，我們新增將透過兩臺測試主機遞迴解析的預設路由。ISP1 連線作為主鏈路（配置為較低的 distance 值）：

```ros
/ip/route/
add distance=1 gateway=8.8.8.8 target-scope=11 check-gateway=ping
add distance=2 gateway=8.8.4.4 target-scope=11 check-gateway=ping
```

此配置確保當主上行鏈路不可用時，流量會自動故障轉移到輔助連線。

### 提高檢測可靠性 {#improve-detection-reliability}

目前，我們依賴單臺主機進行鏈路可達性監控。儘管 Google 服務很少不可用，但我們可以透過在每條鏈路上新增第二臺監控主機來提高可靠性。

```ros
/ip/route
add dst-address=208.67.222.222 gateway=10.111.0.1 scope=10
add dst-address=208.67.220.220 gateway=10.112.0.1 scope=10

add distance=1 gateway=208.67.222.222 target-scope=11 check-gateway=ping
add distance=2 gateway=208.67.220.220 target-scope=11 check-gateway=ping
```

此配置會建立一條 ECMP 預設路由。如果只有一個閘道器變得不可達，第一條鏈路上的預設路由仍保持活動。只有當所有閘道器主機都變得不可達時，才會完全故障轉移到第二條鏈路。
