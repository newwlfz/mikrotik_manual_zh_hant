---
sidebar_key: "firewall-and-quality-of-service/queues/queue-size"
sidebar_position: 4
title: "佇列大小"
sidebar_label: "佇列大小"
description: "本頁面介紹如何在 MikroTik RouterOS 中配置佇列大小限制，詳細說明設定最大封包數量對流量整形和排程的影響。其中包含比較 100% 整形器、排程器和預設佇列型別的示例，以說明丟包率和延遲。"
tags:
  - 'queues'
  - 'packet-scheduling'
  - 'traffic-shaping'
source: https://manual.mikrotik.com/docs/7.25/firewall-and-quality-of-service/queues/queue-size
captured_at: '2026-11-04T11:16:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

最大允許佇列大小可以指定為最大記憶體限制，但許多演算法將其簡化為最大封包數量，因此實際使用的記憶體會隨封包大小而變化。

本頁其餘部分將演示這對於 PFIFO、BFIFO、PCQ 和 RED 等按封包數量處理的佇列型別是如何工作的。

## 示例 {#example}

此示例旨在突出佇列大小對由特定佇列排隊的流量的影響。

為簡化視覺化，假設我們按步驟處理資料，並且確切知道每個步驟將接收/傳輸多少封包，且不會發生丟棄封包的重傳。

![](/img/9846215d6f509cc9.webp)

如上圖所示，在此時間範圍內共有 **25 個步驟**，總共有 **1610 個傳入封包**。

### 100% 整形器 {#100-shaper}

當每個超過允許限制的封包都會被立即丟棄時，佇列就是 100% 整形器。這樣，所有未被丟棄的封包都將無任何延遲地傳送出去。

讓我們對示例應用 **max-limit=100 packets per step** 限制：

![](/img/e7180e5e00f19dc5.webp)

使用這種限制時，1610 個數據包中只有 1250 個能夠透過佇列（**22,4% 丟包率**），但所有封包均無延遲到達。

### 100% 排程器 {#100-scheduler}

當完全沒有丟包時，佇列就是 100% 排程器，所有封包都會排隊，並會在最早可能的時刻傳送出去。

在每個步驟中，佇列必須先發送來自之前步驟的已排隊封包，然後才能傳送本步驟的封包；這樣就能保持正確的封包順序。

我們將再次使用相同的限制（**每步 100 個數據包**）。

![](/img/602cb27b0fe527ac.webp)

沒有封包丟失，但有 630 個 **（39,1%）封包延遲 1 步**，另外 170 個 **（10,6%）封包延遲 2 步**。（延遲 = 時延）

### Default-small 佇列型別 {#default-small-queue-type}

也可以選擇折中方式，即佇列同時使用這兩種排隊機制（整形和排程）。預設情況下，RouterOS 中大多數佇列的佇列大小為 10。

![](/img/c34b3e99ab24c759.webp)

有 320 個 **（19,9%）封包被丟棄**，80 個 **（5,0%）封包延遲 1 步**。

### 預設佇列型別 {#default-queue-type}

RouterOS 中另一個常用的佇列大小是 50。

![](/img/d032181d3683de9a.webp)

有 190 個 **（11.8%）封包被丟棄**，400 個 **（24.8%）封包延遲 1 步**。
