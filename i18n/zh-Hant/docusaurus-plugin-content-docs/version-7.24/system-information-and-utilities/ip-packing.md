---
sidebar_key: "system-information-and-utilities/ip-packing"
sidebar_position: 8
title: "IP 打包"
sidebar_label: "IP 打包"
description: "IP Packing 可在 RouterOS 的網路鏈路上實現封包聚合與壓縮，需要啟用發現協定並進行對稱配置。它支援多種操作，例如簡單聚合，或對報頭和載荷進行壓縮，並警告可能會增加延遲。"
tags:
  - 'ip-packing'
  - 'packet-aggregation'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/ip-packing
captured_at: '2026-11-04T11:33:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

IP Packing 在網路鏈路上提供封包打包服務。它允許將簡單封包聚合為更大的封包，並對封包內容進行壓縮。

## 要求 {#requirements}

封包打包是系統軟體包的一部分，並且必須在介面上啟用發現協定。

### 配置 {#configuration}

**子選單：** `/ip/packing`

需要在兩個位置進行配置，兩臺路由器應進行對稱設定：

- `/ip/packing`- 用於在介面上啟用封包聚合和/或壓縮。
- `/ip/neighbor/discovery-settings` 用於在介面上啟用發現協定。

### 打包配置 {#packing-configuration}

| 屬性 | 描述 |
| :-- | :-- |
| aggregated-size (*20 .. 16384 預設:**1500***) | 打包在透過網路傳送封包之前將嘗試達到的聚合封包大小 |
| disabled (*yes\|no*) | 打包規則的狀態，如果值為 *yes*，則會被忽略，並且不會成為活動配置的一部分 |
| interface (*介面名稱*) | 打包將嘗試聚合和/或壓縮來自此介面的封包 |
| packing (*simple\|compress-all\|compress-headers\|none*) | 當封包離開配置了此打包規則的介面時應執行的動作：<span className="ros-background-accent-green-bolder"><code>simple</code></span> - 僅聚合封包<span className="ros-background-accent-green-bolder"><code>compress-all</code></span> - 執行聚合並嘗試壓縮封包的頭部和有效載荷<span className="ros-background-accent-green-bolder"><code>compress-headers</code></span> - 執行聚合並嘗試壓縮封包的頭部，而有效載荷保持不變<span className="ros-background-accent-green-bolder"><code>none</code></span> - 按原樣傳送封包 |
| unpacking (*simple\|compress-all\|compress-headers\|none*) | 當在配置了此打包規則的介面上接收到封包時應執行的動作：<span className="ros-background-accent-green-bolder"><code>simple</code></span> - 從介面接收到的聚合封包中解包收到的封包<span className="ros-background-accent-green-bolder"><code>compress-all</code></span> - 解包聚合封包並解壓縮封包的頭部和有效載荷<code>compress-headers </code>- 解包聚合封包並解壓縮封包的頭部<span className="ros-background-accent-green-bolder"><code>none</code></span> - 對收到的封包不做任何處理 |

:::danger
在要啟用打包的介面上，應能在鄰居中看到對端路由器。如果鄰居列表中沒有表明打包的條目，則打包無法正常工作！

**警告：** 打包可能會增加其所在鏈路的延遲。
:::

## 示例 {#example}

Router-A 和 Router-B 透過線纜連線，Router-A 上使用介面 ether1，Router-B 上使用介面 ether3。此示例將聚合來自 Router-A 的封包，但會保持來自 Router-B 的封包不變。在 Router-A 上：

確保已啟用發現協定：

```ros
 /ip/neighbor/discovery/set ether1 discover=yes 
```

為該介面新增打包規則：

```ros
 /ip/packing/add interface=ether1 aggregated-size=1500 packing=simple unpacking=none 
```

在 Router-B 上：

確保已啟用發現協定：

```ros
 /ip/neighbor/discovery/set ether3 discover=yes 
```

為該介面新增打包規則：

```ros
 /ip/packing/add interface=ether3 aggregated-size=1500 packing=none unpacking=simple
```
