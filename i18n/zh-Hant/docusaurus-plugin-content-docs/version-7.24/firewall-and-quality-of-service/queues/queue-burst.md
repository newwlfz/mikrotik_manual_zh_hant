---
sidebar_key: "firewall-and-quality-of-service/queues/queue-burst"
sidebar_position: 3
title: "佇列突發"
sidebar_label: "佇列突發"
description: "佇列 Burst 功能允許在平均流量保持在閾值以下時臨時突發超過配置限制的頻寬，使用 burst-limit 和 burst-time 引數來控制突發的持續時間和大小。"
tags:
  - 'queue-burst'
  - 'qos'
  - 'traffic-management'
source: https://manual.mikrotik.com/docs/7.24/firewall-and-quality-of-service/queues/queue-burst
captured_at: '2026-11-04T11:28:22+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

Burst 是一項功能，即使所需速率在有限時間內大於 **MIR**（**max-limit**），也允許滿足佇列對額外頻寬的需求。

只有當佇列在最近 **burst-time** 秒內的 **average-rate** 小於 **burst-threshold** 時，才會發生 Burst。如果佇列在最近 **burst-time** 秒內的 **average-rate** 大於或等於 **burst-threshold**，Burst 將停止。

Burst 機制很簡單——如果允許 Burst，則 **max-limit** 值會被替換為 **burst-limit** 值。當不允許 Burst 時，**max-limit** 值保持不變。

1. **burst-limit** (NUMBER) : 允許 Burst 時可達到的最大上傳/下載資料速率。
2. **burst-time** (TIME) : 用於計算平均資料速率的時間段，以秒為單位。（這不是實際 Burst 的時間）。
3. **burst-threshold** (NUMBER) : 這是 Burst 開啟/關閉開關的值。
4. **average-rate** (read-only) : 在 **burst-time** 的每 1/16 部分，路由器會計算每個類別在最近 **burst-time** 秒內的平均資料速率。
5. **actual-rate** (read-only) : 佇列的實際流量傳輸速率。

## 示例 {#example}

值：**limit-at=1M** , **max-limit=2M** , **burst-threshold=1500k** , **burst-limit=4M**

用戶端將嘗試下載兩個 4MB（32Mb）的資料塊，第一次下載將從第 0 秒開始，第二次下載將從第 17 秒開始。最後一分鐘沒有使用流量。

#### Burst-time=16s {#burst-time16s}

![](/img/c1e23afd6d46874f.webp)![](/img/50d5e4c4dedde6cc.webp)

正如我們所看到的，用戶端一請求頻寬，就能獲得 6 秒的 4Mbps Burst。這是給定值下可能的最長 Burst *（longest-burst-time = burst-threshold \* burst-time / burst-limit）*。一旦 Burst 用完，剩餘資料將以 2Mbps 下載。這樣，一個數據塊在 10 秒內下載完成——如果沒有 Burst，則需要 16 秒。在下一次下載開始之前，Burst 有 7 秒時間重新充電。

請注意，下載開始時仍不允許 Burst，它只會在之後——下載過程中——生效。因此，透過這個示例，我們證明 Burst 可能發生在下載過程中。這次 Burst 持續約 4 秒，第二個資料塊比沒有 Burst 時快 4 秒下載完成。

平均速率每 1/16 個 burst-time 計算一次，因此在這種情況下為 1 秒。

| 時間 | average-rate | burst | actual-rate |
| --: | :-- | :-- | :-- |
| 0 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+0+0)/16=0Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps |
| 1 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+0+4)/16=250Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps |
| 2 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+4+4)/16=500Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps |
| 3 | (0+0+0+0+0+0+0+0+0+0+0+0+0+4+4+4)/16=750Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps |
| 4 | (0+0+0+0+0+0+0+0+0+0+0+0+4+4+4+4)/16=1000Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps |
| 5 | (0+0+0+0+0+0+0+0+0+0+0+4+4+4+4+4)/16=1250Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps |
| 6 | (0+0+0+0+0+0+0+0+0+0+4+4+4+4+4+4)/16=1500Kbps | average-rate = burst-threshold → **不**允許 Burst | **2Mbps** |
| 7 | (0+0+0+0+0+0+0+0+0+4+4+4+4+4+4+2)/16=1625Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps |
| 8 | (0+0+0+0+0+0+0+0+4+4+4+4+4+4+2+2)/16=1750Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps |
| 9 | (0+0+0+0+0+0+0+4+4+4+4+4+4+2+2+2)/16=1875Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps |
| 10 | (0+0+0+0+0+0+4+4+4+4+4+4+2+2+2+2)/16=2Mbps | average-rate > burst-threshold → 不允許 Burst | **0Mbps** |
| 11 | (0+0+0+0+0+4+4+4+4+4+4+2+2+2+2+0)/16=2Mbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps |
| 12 | (0+0+0+0+4+4+4+4+4+4+2+2+2+2+0+0)/16=2Mbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps |
| 13 | (0+0+0+4+4+4+4+4+4+2+2+2+2+0+0+0)/16=2Mbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps |
| 14 | (0+0+4+4+4+4+4+4+2+2+2+2+0+0+0+0)/16=2Mbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps |
| 15 | (0+4+4+4+4+4+4+2+2+2+2+0+0+0+0+0)/16=2Mbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps |
| 16 | (4+4+4+4+4+4+2+2+2+2+0+0+0+0+0+0)/16=2Mbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps |
| 17 | (4+4+4+4+4+2+2+2+2+0+0+0+0+0+0+0)/16=1750Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps |
| 18 | (4+4+4+4+2+2+2+2+0+0+0+0+0+0+0+2)/16=1500Kbps | average-rate = burst-threshold → 不允許 Burst | 2Mbps |
| 19 | (4+4+4+2+2+2+2+0+0+0+0+0+0+0+2+2)/16=1375Kbps | average-rate < burst-threshold → Burst **確實**允許 | 4Mbps |
| 20 | (4+4+2+2+2+2+0+0+0+0+0+0+0+2+2+4)/16=1375Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps |
| 21 | (4+2+2+2+2+0+0+0+0+0+0+0+2+2+4+4)/16=1375Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps |
| 22 | (2+2+2+2+0+0+0+0+0+0+0+2+2+4+4+4)/16=1375Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps |
| 23 | (2+2+2+0+0+0+0+0+0+0+2+2+4+4+4+4)/16=1500Kbps | average-rate = burst-threshold → **不**允許 Burst | 2Mbps |
| 24 | (2+2+0+0+0+0+0+0+0+2+2+4+4+4+4+2)/16=1500Kbps | average-rate = burst-threshold → 不允許 Burst | 2Mbps |
| 25 | (2+0+0+0+0+0+0+0+2+2+4+4+4+4+2+2)/16=1500Kbps | average-rate = burst-threshold → 不允許 Burst | 2Mbps |
| 26 | (0+0+0+0+0+0+0+2+2+4+4+4+4+2+2+2)/16=1500Kbps | average-rate = burst-threshold → 不允許 Burst | 2Mbps |
| 27 | (0+0+0+0+0+0+2+2+4+4+4+4+2+2+2+2)/16=1625Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps |
| 28 | (0+0+0+0+0+2+2+4+4+4+4+2+2+2+2+2)/16=1750Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps |
| 29 | (0+0+0+0+2+2+4+4+4+4+2+2+2+2+2+2)/16=1875Kbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps |
| 30 | (0+0+0+2+2+4+4+4+4+2+2+2+2+2+2+0)/16=1875Kbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps |
| 31 | (0+0+2+2+4+4+4+4+2+2+2+2+2+2+0+0)/16=1875Kbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps |

#### Burst-time=8s {#burst-time8s}

![](/img/1e52f9a67429a1ac.webp)![](/img/6c7a9a312cdcf56d.webp)

如果我們將 burst-time 減小到 8 秒，就能看到在這種情況下，Burst 只發生在下載開始時。平均速率每 1/16 個 burst-time 計算一次，因此在這種情況下每 0.5 秒計算一次。

| 時間 | average-rate | burst | actual-rate |
| --: | :-- | :-- | :-- |
| 0 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+0+0)/8=0Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps（每 0.5 秒 2Mb） |
| 0.5 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+0+2)/8=250Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps（每 0.5 秒 2Mb） |
| 1 | (0+0+0+0+0+0+0+0+0+0+0+0+0+0+2+2)/8=500Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps（每 0.5 秒 2Mb） |
| 1.5 | (0+0+0+0+0+0+0+0+0+0+0+0+0+2+2+2)/8=750Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps（每 0.5 秒 2Mb） |
| 2 | (0+0+0+0+0+0+0+0+0+0+0+0+2+2+2+2)/8=1000Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps（每 0.5 秒 2Mb） |
| 2.5 | (0+0+0+0+0+0+0+0+0+0+0+2+2+2+2+2)/8=1250Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps（每 0.5 秒 2Mb） |
| 3 | (0+0+0+0+0+0+0+0+0+0+2+2+2+2+2+2)/8=1500Kbps | average-rate = burst-threshold → **不**允許 Burst | **2Mbps**（每 0.5 秒 1Mb） |
| 3.5 | (0+0+0+0+0+0+0+0+0+2+2+2+2+2+2+1)/8=1625Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 4 | (0+0+0+0+0+0+0+0+2+2+2+2+2+2+1+1)/8=1750Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 4.5 | (0+0+0+0+0+0+0+2+2+2+2+2+2+1+1+1)/8=1875Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 5 | (0+0+0+0+0+0+2+2+2+2+2+2+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 5.5 | (0+0+0+0+0+2+2+2+2+2+2+1+1+1+1+1)/8=2125Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 6 | (0+0+0+0+2+2+2+2+2+2+1+1+1+1+1+1)/8=2250Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 6.5 | (0+0+0+2+2+2+2+2+2+1+1+1+1+1+1+1)/8=2375Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 7 | (0+0+2+2+2+2+2+2+1+1+1+1+1+1+1+1)/8=2500Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 7.5 | (0+2+2+2+2+2+2+1+1+1+1+1+1+1+1+1)/8=2625Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 8 | (2+2+2+2+2+2+1+1+1+1+1+1+1+1+1+1)/8=2750Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 8.5 | (2+2+2+2+2+1+1+1+1+1+1+1+1+1+1+1)/8=2625Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 9 | (2+2+2+2+1+1+1+1+1+1+1+1+1+1+1+1)/8=2500Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 9.5 | (2+2+2+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2375Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 10 | (2+2+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2250Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 10.5 | (2+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2125Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 11 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 11.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 12 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 12.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 13 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | **0Mbps**（每 0.5 秒 0Mb） |
| 13.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+0)/8=1875Kbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps（每 0.5 秒 0Mb） |
| 14 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+0+0)/8=1750Kbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps（每 0.5 秒 0Mb） |
| 14.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+0+0+0)/8=1625Kbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps（每 0.5 秒 0Mb） |
| 15 | (1+1+1+1+1+1+1+1+1+1+1+1+0+0+0+0)/8=1500Kbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps（每 0.5 秒 0Mb） |
| 15.5 | (1+1+1+1+1+1+1+1+1+1+1+0+0+0+0+0)/8=1375Kbps | average-rate < burst-threshold → Burst **確實**允許 | 0Mbps（每 0.5 秒 0Mb） |
| 16 | (1+1+1+1+1+1+1+1+1+1+0+0+0+0+0+0)/8=1250Kbps | average-rate < burst-threshold → 允許 Burst | 0Mbps（每 0.5 秒 0Mb） |
| 16.5 | (1+1+1+1+1+1+1+1+1+0+0+0+0+0+0+0)/8=1125Kbps | average-rate < burst-threshold → 允許 Burst | 0Mbps（每 0.5 秒 0Mb） |
| 17 | (1+1+1+1+1+1+1+1+0+0+0+0+0+0+0+0)/8=1000Kbps | average-rate < burst-threshold → 允許 Burst | **2Mbps**（每 0.5 秒 1Mb） |
| 17.5 | (1+1+1+1+1+1+1+0+0+0+0+0+0+0+0+1)/8=1000Kbps | average-rate < burst-threshold → 允許 Burst | **4Mbps**（每 0.5 秒 2Mb） |
| 18 | (1+1+1+1+1+1+0+0+0+0+0+0+0+0+1+2)/8=1125Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps（每 0.5 秒 2Mb） |
| 18.5 | (1+1+1+1+1+0+0+0+0+0+0+0+0+1+2+2)/8=1250Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps（每 0.5 秒 2Mb） |
| 19 | (1+1+1+1+0+0+0+0+0+0+0+0+1+2+2+2)/8=1375Kbps | average-rate < burst-threshold → 允許 Burst | 4Mbps（每 0.5 秒 2Mb） |
| 19.5 | (1+1+1+0+0+0+0+0+0+0+0+1+2+2+2+2)/8=1500Kbps | average-rate = burst-threshold → **不**允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 20 | (1+1+0+0+0+0+0+0+0+0+1+2+2+2+2+1)/8=1500Kbps | average-rate = burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 20.5 | (1+0+0+0+0+0+0+0+0+1+2+2+2+2+1+1)/8=1500Kbps | average-rate = burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 21 | (0+0+0+0+0+0+0+0+1+2+2+2+2+1+1+1)/8=1500Kbps | average-rate = burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 21.5 | (0+0+0+0+0+0+0+1+2+2+2+2+1+1+1+1)/8=1625Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 22 | (0+0+0+0+0+0+1+2+2+2+2+1+1+1+1+1)/8=1750Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 22.5 | (0+0+0+0+0+1+2+2+2+2+1+1+1+1+1+1)/8=1875Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 23 | (0+0+0+0+1+2+2+2+2+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 23.5 | (0+0+0+1+2+2+2+2+1+1+1+1+1+1+1+1)/8=2125Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 24 | (0+0+1+2+2+2+2+1+1+1+1+1+1+1+1+1)/8=2250Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 24.5 | (0+1+2+2+2+2+1+1+1+1+1+1+1+1+1+1)/8=2375Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 25 | (1+2+2+2+2+1+1+1+1+1+1+1+1+1+1+1)/8=2500Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 25.5 | (2+2+2+2+1+1+1+1+1+1+1+1+1+1+1+1)/8=2500Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 26 | (2+2+2+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2375Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 26.5 | (2+2+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2250Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 27 | (2+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2125Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 27.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 28 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 28.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 29 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 29.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 30 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | 2Mbps（每 0.5 秒 1Mb） |
| 30.5 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)/8=2000Kbps | average-rate > burst-threshold → 不允許 Burst | **0Mbps**（每 0.5 秒 0Mb） |
| 31 | (1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+0)/8=1875Kbps | average-rate > burst-threshold → 不允許 Burst | 0Mbps（每 0.5 秒 0Mb） |
