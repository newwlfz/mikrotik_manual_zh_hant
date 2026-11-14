---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/health"
sidebar_position: 13
title: "健康"
sidebar_label: "健康"
description: "本頁面介紹 MikroTik RouterOS 的硬體健康監控功能，詳細說明受支援裝置上的溫度、電壓、風扇轉速和 CPU 狀態等指標。內容包括 CLI 示例、關於裝置限制的警告，以及基於 PoE-out 負載或溫度閾值的風扇控制引數。"
tags:
  - 'system-health'
  - 'fan-control'
  - 'temperature'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/health
captured_at: '2026-11-04T11:15:18+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

支援監控的硬體會顯示不同的硬體狀態資訊，例如溫度、電壓、電流、風扇轉速等。

CCR1072-1G-8S+ 裝置上的示例：

```ros
[admin@MikroTik] > /system/health/print 
Columns: NAME, VALUE, TYPE
 #  NAME                VALUE  TYPE
 0  power-consumption   50.8   W   
 1  cpu-temperature     43     C   
 2  fan1-speed          5654   RPM 
 3  fan2-speed          5825   RPM 
 4  fan3-speed          5800   RPM 
 5  fan4-speed          5750   RPM 
 6  board-temperature1  29     C   
 7  board-temperature2  28     C   
 8  psu1-voltage        0      V   
 9  psu2-voltage        12.1   V   
10  psu1-current        0      A   
11  psu2-current        4.2    A
```

:::info
有關 RouterBOARD 產品的功能可用性，請檢視 [mikrotik.com](https://mikrotik.com/products)
:::

在 [CCR2004-16G-2S+PC](https://mikrotik.com/product/ccr2004_16g_2s_pc) 裝置上進行密集的健康狀態監控（透過控制檯、winbox 或 SNMP）會導致顯著的 CPU 負載。

### 電壓 {#voltage}

支援電壓監控的路由器會顯示供電電壓值。在 CLI/Winbox 中會以伏特為單位顯示。在 scripts/API/SNMP 中，該值為 dV 或 CLI/Winbox 中顯示的值

**注意：** 具有 PEXT 和 PoE 電源輸入的路由器使用 PEXT 進行校準，因此，由於額外的乙太網保護電路，透過 PoE 顯示的值可能低於輸入電壓。

```ros
[admin@MikroTik] > /system/health/print 
Columns: NAME, VALUE, TYPE
#  NAME         VALUE  TYPE
0  voltage      23.8   V   
1  temperature  39     C 
```

:::warning
如果舊版 CRS112、CRS210 和 CRS109 裝置透過 PoE 供電，健康狀態將僅在最高 26.7V 時顯示正確電壓。如果使用更高電壓，健康狀態將顯示恆定的 16V。
:::

### 溫度 {#temperature}

支援溫度監控的路由器會顯示溫度讀數。在 CLI/Winbox 中會以攝氏度為單位顯示。使用 scripts/API/SNMP 時，此值將在 CLI/Winbox 中顯示為乘以 10 後的值。根據裝置不同，有多種溫度感測器。這些感測器可能指：cpu-temperature、pcb-temperature、sfp-temperature。您可以在 [mikrotik.com](https://mikrotik.com/products) 的規格說明中找到裝置經過測試的環境溫度範圍。經過測試的環境溫度範圍是裝置可以實際放置的溫度範圍。它**並不**等同於系統健康監控報告的溫度！

### 風扇控制與行為 {#fan-control-and-behavior}

**子選單：** `/system/health`

使用此選單，使用者可以控制 TILE 架構[裝置](https://mikrotik.com/download)上的風扇行為。

:::info
從 6.45.5 版本開始，風扇穩定性得到改進。
:::

有三個引數可能影響風扇行為：PoE-out 功耗、SFP 溫度和 CPU 溫度。一旦其中一個引數超過最佳值，風扇就會啟動。

#### PoE-out 功耗 {#poe-out-consumption}

如果裝置具有 PoE-out，則風扇 RPM 將如下所述變化：

| PoE-out 負載 | 最大風扇轉速的 RPM 百分比 |
| :-- | :-- |
| 0%..24% | 風扇轉速 0% |
| 25%..46% | 風扇轉速 25% |
| 47%..70% | 風扇轉速 50% |
| 71%..92% | 風扇轉速 75% |
| 93%.. | 風扇轉速 100% |

對於配備 **PWM** 風扇的裝置，轉速將在 9..88% 範圍內線性增加或降低（注意：低於 100W 時風扇 RPM=0）

#### 有限的手動風扇控制選項 {#limited-manual-fan-control-option}

:::info
從 RouterOS 7.9 版本開始，為 CRS3xx、CRS5xx 和 CCR2xxx 裝置添加了有限的手動風扇控制選項。

從 RouterOS 7.14 版本開始，CCR1036-8G-2S+-r2、CCR1036-12G-4S-r2 和 CCR1016-12S-1S+-r2 裝置可用的有限手動風扇控制已提供。
:::

可以使用系統健康狀態的設定部分來調整風扇行為：

```
/system/health/settings/set 
```

可用屬性如下所述：

| 屬性 | 描述 |
| :-- | :-- |
| **fan-full-speed-temp** (*整數* *[-273..65];* 預設值：**65**) | 設定溫度值，達到該值後風扇轉速將提高到最大可能 RPM。  從 CPU、PHY、SWITCH 和 SFP 讀取溫度，並根據溫度最高的元件調整風扇轉速。 |
| **fan-target-temp** (*整數* *[-273..65];* 預設值：**58**) | 設定最熱元件的目標溫度。基於此設定，它會調整風扇行為，以將溫度保持在目標範圍內。 |
| **fan-min-speed-percent** (*整數* *[0..100];* 預設值：**取決於風扇控制器**) | 設定風扇轉速的最低百分比，從而不允許風扇的 RPM 低於此值。**\*注意：** 預設值可能因風扇控制器晶片和/或特定型號要求而異。從 RouterOS 7.14 版本開始，預設值設為 **12**，所有先前版本均為 **0.** |
| **fan-control-interval** (*整數* *[5..30];* 預設值：**30**) | 設定實際溫度資料讀取間隔，以從 CPU、PHY、SWITCH 和 SFP 獲取溫度值。  **\*注意：** 此設定會直接影響 CPU 使用率 |
| **cpu-overtemp-check** *(yes \| no; 預設值：no)* | 啟用/停用 CPU 過溫監控。  *(適用於 ARM/ARM64 裝置)* |
| **cpu-overtemp-threshold** *(整數 [0..105]; 預設值：105)* | 觸發過溫保護前的最高溫度。 |
| **cpu-overtemp-startup-delay** *(時間; 預設值：1m)* | 啟動後啟用過溫監控之前的延遲時間。 |

#### 風扇控制簡要說明 {#brief-description-of-the-fan-control}

如果至少有一個內部測量溫度（CPU、SFP、Switch、Board 等）超過 **fan-target-temp**，風扇就會開始旋轉。溫度越高，風扇旋轉得越快。對於配備 PWM 風扇的裝置，當內部測量溫度超過 **fan-target-temp** 時，風扇會線性提高其 RPM，以儘可能將溫度保持在 **fan-target-temp**；當溫度等於或超過 **fan-full-speed-temp** 時，風扇將達到其最大 RPM。  對於配備 DC 風扇的裝置，當內部測量溫度超過 **fan-target-temp** 時，風扇會開始旋轉，但預設情況下會以更高的最低 RPM 執行。如果 **fan-min-speed-percent** 設為 **0%**，這可能會導致裝置冷卻到風扇完全關閉的程度；而在預設值為 **12%** 的情況下，風扇永遠不會完全停止，從而減少可能出現的噪聲和啟停峰值。隨後溫度可能緩慢升高到 **fan-target-temp**，風扇會再次開啟。目前有一個例外。S+RJ10 模組在觸發風扇之前具有 65C 的溫度閾值。由於這是更高的溫度閾值，風扇會以更高的初始轉速啟動來冷卻裝置。上述所有功能都直接與 **fan-control-interval** 引數值相關，因為它決定了風扇控制器監控所有感測器資料並觸發風扇控制更改的頻率。

:::warning
PWM 和 DC 風扇對風扇控制的反應方式不同。PWM 風扇會以線性方式提高/降低其 RPM，而 DC 風扇只有少數幾個可能的工作轉速等級。
所有讀數均為近似值，可能並非 100% 精確。其目的是~告知使用者可能/即將發生的故障。
:::
