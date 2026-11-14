---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/graphing"
sidebar_position: 11
title: "圖表"
sidebar_label: "圖表"
description: "Graphing 是 RouterOS 的一個工具，用於透過可透過 Web 瀏覽器或選單訪問的視覺化圖表，隨時間監控 CPU、記憶體、磁碟使用率以及介面/佇列流量。配置選項包括資料收集頻率、儲存設定以及針對特定 IP 範圍的訪問許可權。"
tags:
  - 'graphing'
  - 'monitoring'
  - 'resource-usage'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/graphing
captured_at: '2026-11-04T11:28:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

圖形功能是一個用於隨時間監控各種 RouterOS 引數並將收集到的資料放入圖形的工具。  
觀看我們[關於此功能的影片](https://youtu.be/FTQEnDZVHNc)。

:::danger
對於內建記憶體較小的裝置，我們建議不要將圖形儲存在磁碟上。
:::

圖形工具可以顯示以下各項的圖形：

- 資源使用情況（CPU、記憶體和磁碟使用情況）。
- 透過介面的流量。
- 透過簡單佇列的流量。

圖形功能由兩部分組成——第一部分收集資訊，另一部分在 Web 頁面上顯示資料。要訪問圖形，請在 Web 瀏覽器中輸入 http://[Router\_IP\_address]/graphs/ 並選擇要顯示的圖形。

或者，在 WebFig 介面右上角查詢 **≡** 選單（三橫線符號），透過它可以找到“graphs”：

![](/img/502e6bf58d409e15.png)

記憶體圖形示例：

![](/img/42a3d6819ca0c861.webp)

## 配置 {#configuration}

### 常規 {#general}

配置在 `/tool/graphing` 選單下完成。預設情況下，圖形功能處於停用狀態。您可以在各自對應的子選單中為介面、資源和簡單佇列配置圖形功能。

**子選單：** `/tool/graphing`

| 屬性 | 描述 |
| :-- | :-- |
| **store-every** (*24hours \| 5min \| hour*; 預設：**5min**) | 將收集到的資料寫入系統驅動器的頻率。 |
| **page-refresh** (*integer \| never*; 預設：**300**) | 圖形頁面重新整理的頻率 |

### 介面圖形 {#interface-graphing}

該子選單用於配置圖形功能要收集哪個介面的頻寬使用資料。

**子選單：** `/tool/graphing/interface`

| 屬性 | 描述 |
| :-- | :-- |
| **allow-address** (*IP/IPv6 prefix*; 預設：**0.0.0.0/0**) | 允許訪問圖形資訊的 IP 地址範圍 |
| **comment** (*string*; 預設：) | 當前條目的描述 |
| **disabled** (*yes \| no*; 預設：**no**) | 定義是否使用該項 |
| **interface** (*all \| interface name*; 預設：**all**) | 定義將監控哪個介面。**all** 表示將監控路由器上的所有介面。 |
| **store-on-disk** (*yes \| no*; 預設：**yes**) | 定義是否將收集到的資訊儲存在系統驅動器上。 |

### 佇列圖形 {#queue-graphing}

該子選單用於配置圖形功能要收集哪個簡單佇列的頻寬使用資料。

**子選單：** `/tool/graphing/queue`

| 屬性 | 描述 |
| :-- | :-- |
| **allow-address** (*IP/IPv6 prefix*; 預設：**0.0.0.0/0**) | 允許訪問圖形資訊的 IP 地址範圍 |
| **allow-target** (*yes \| no*; 預設：**yes**) | 是否允許從佇列的 target-address 訪問圖形 |
| **comment** (*string*; 預設：) | 當前條目的描述 |
| **disabled** (*yes \| no*; 預設：**no**) | 定義是否使用該項 |
| **simple-queue** (*all \| queue name*; 預設：**all**) | 定義將監控哪些佇列。**all** 表示將監控路由器上的所有佇列。 |
| **store-on-disk** (*yes \| no*; 預設：**yes**) | 定義是否將收集到的資訊儲存在系統驅動器上。 |

:::warning
如果簡單佇列的 target-address 設定為 0.0.0.0/0，那麼即使 allow address 設定為特定地址，所有人也都能訪問佇列圖形。發生這種情況是因為預設情況下，佇列圖形也可從目標地址訪問。
:::

### 資源圖形 {#resource-graphing}

該子選單允許啟用系統資源圖形功能。圖形功能收集以下資料：

- CPU 使用情況
- 記憶體使用情況
- 磁碟使用情況

**子選單：** `/tool/graphing/resource`

| 屬性 | 描述 |
| :-- | :-- |
| **allow-address** (*IP/IPv6 prefix*; 預設：**0.0.0.0/0**) | 允許訪問圖形資訊的 IP 地址範圍 |
| **comment** (*string*; 預設：) | 當前條目的描述 |
| **disabled** (*yes \| no*; 預設：**no**) | 定義是否使用該項 |
| **store-on-disk** (*yes \| no*; 預設：**yes**) | 定義是否將收集到的資訊儲存在系統驅動器上 |

## 在 WinBox 中檢視圖形 {#graphing-in-winbox}

Winbox 允許檢視與網頁上相同的已收集資訊。開啟 **Tools->Graphing** 視窗。雙擊您要檢視圖形的條目。

下圖顯示了 WinBox 的記憶體使用情況圖形：

![](/img/6dd203c558cbdb32.webp)
