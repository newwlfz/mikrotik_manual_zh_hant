---
sidebar_key: "hardware/lcd-touchscreen"
sidebar_position: 3
title: "LCD 觸控式螢幕"
sidebar_label: "LCD 觸控式螢幕"
description: "本頁面介紹了 MikroTik RouterOS 上的 LCD 觸控式螢幕功能，涵蓋背光超時、配色方案和螢幕預設值等配置選項。它還說明了校準流程、螢幕截圖捕獲、介面監控設定，以及用於網路統計的基於頁面的圖表顯示。"
tags:
  - 'lcd'
  - 'touchscreen'
  - 'configuration'
source: https://manual.mikrotik.com/docs/7.25/hardware/lcd-touchscreen
captured_at: '2026-11-04T11:17:25+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

RouterBOARD 2011U 和 CCR 系列裝置配備電阻式觸控式螢幕，可快速訪問裝置統計資訊和簡單配置選項。觸控式螢幕需要按壓表面才能識別觸控；因此，輕掃和快速或短暫的點選可能不會被識別（這與手機上常見的電容式觸控式螢幕不同）。如果您用手指操作螢幕有困難，也可以嘗試使用觸控筆或筆的另一端。

## 配置 {#configuration}

**子選單：** `/lcd`

此子選單提供 LCD 觸控式螢幕的配置選項。

| 屬性 | 描述 |
| :-- | :-- |
| **backlight-timeout** (*時間間隔：5m..2h \| never*；預設：**30m**) | 指定 LCD 觸控式螢幕背光關閉前的無操作時長。設定為 "never" 可使背光始終開啟。 |
| **color-scheme** (*dark \| light*；預設：取決於 RouterBoard 型號) | 設定 LCD 顯示屏的配色方案，在深色或淺色背景之間選擇。 |
| **default-screen** (*informative-slideshow\|interface\|log\|main-menu\|stat-slideshow\|stats\|stats-all*；預設：**main-menu**) | 定義路由器啟動後 LCD 上顯示的預設螢幕。 |
| **enabled** (*yes \| no*；預設：**yes**) | 啟用或停用 LCD 觸控式螢幕。停用後，觸控式螢幕停止工作，統計資訊收集會重設，LCD 程式關閉。 |
| **read-only-mode** (*yes \| no*；預設：**yes**) | 啟用或停用只讀模式。啟用後，允許更改配置的選單會從 LCD 介面中隱藏。 |
| **time-interval** (*min \| hour \| daily \| weekly*；預設：**min**) | 設定 Stats 螢幕中顯示的介面統計資訊所使用的時間間隔。 |
| **touch-screen** (*enabled \| disabled*，預設：**enabled**) | 啟用或停用觸控式螢幕輸入功能。 |

### 可用功能 {#available-functions}

LCD 觸控式螢幕支援以下功能：

- **backlight** - 開啟或關閉 LCD 背光。LCD 程式會繼續執行。
- **recalibrate** - 啟動 LCD 觸控式螢幕校準過程。
- **show** - 指定 LCD 上顯示的螢幕。
- **take-screenshot** - 擷取當前顯示的 LCD 螢幕截圖。

### LCD 觸控式螢幕校準 {#lcd-touchscreen-calibration}

LCD 觸控式螢幕在首次使用前需要校準。校準成功後，校準資料會儲存在路由器上。如果不存在校準資料，校準過程會自動啟動。

在校準或重新校準期間，您必須觸控式螢幕幕上顯示的四個點。其中三個點用於計算校準變數，第四個點用於驗證校準是否成功。如果校準失敗，校準變數不會被儲存。觸控第四個點後，會顯示一條訊息說明校準結果。

### 擷取 LCD 截圖 {#take-lcd-screenshot}

take-screenshot 功能會將當前 LCD 螢幕捕獲為 BMP 影像，並使用指定的檔名儲存到 File List 中。沒有檔名的截圖不會被儲存。如果已存在指定名稱的檔案，它將被覆蓋。

示例：

```ros
[admin@MikroTik] /lcd/take-screenshot file-name=screen-1
Screenshot taken
[admin@MikroTik] >
```

## LCD 介面 {#lcd-interface}

**子選單：** `/lcd/interface`

Interfaces 子選單用於配置各個介面統計資訊在 Stat Slideshow 中的顯示方式。最多可以向 LCD 新增 10 個額外的（非物理）介面用於監控。

| 屬性 | 描述 |
| :-- | :-- |
| **disabled** (*yes | no*；預設：**no**) | 定義該項在 Informative Slideshow 中是被忽略還是被使用 |
| **max-speed** (*integer | auto*；預設：) | 設定用於在 All Interface 圖表和 Interface 螢幕中計算頻寬使用率的最大介面速率。"auto" 值只能分配給物理介面。 |
| **timeout** (*時間間隔：1s..1m*；預設：**10s**) | 指定幻燈片播放期間每個介面頁面的顯示時長 |

- **display** - 在 Stats 螢幕中顯示該介面。

### All Interface 圖表螢幕 {#all-interface-graph-screen}

**子選單：** `/lcd/interface/pages`

頁面是一個最多可包含 12 個介面條形圖的螢幕。該子選單允許配置頁面中顯示哪些介面。All Interface Graph 螢幕最多可新增 5 個頁面，每頁最多 12 個介面。要將介面新增到頁面，必須先在 `/lcd/interface` 子選單下新增該介面。

| 屬性 | 描述 |
| :-- | :-- |
| **interfaces** (介面名稱；預設：) | 螢幕上顯示的介面。必須至少有 1 個介面。 |

## LCD 資訊螢幕 {#lcd-informative-screens}

**子選單：** `/lcd/screen`

Screens 選單允許您為 Informative Slideshow 中的每張幻燈片配置顯示時長。

| 屬性 | 描述 |
| :-- | :-- |
| **disabled** (*yes | no*；預設：**no**) | 定義該項在 Informative Slideshow 中是被忽略還是被使用 |
| **timeout** (*時間間隔：1s..1m*；預設：**10s**) | 每張資訊幻燈片的顯示時長 |

## LCD PIN 碼 {#lcd-pin-code}

**子選單：** `/lcd/pin`

![](/img/35909f17b70e255b.webp)

PIN 碼用於保護 LCD 螢幕上的敏感選單。當只讀模式被停用，而您嘗試新增 IP 地址、重設或重啟路由器時，會要求輸入 PIN 碼。預設 PIN 碼為 **1234**。

| 屬性 | 描述 |
| :-- | :-- |
| **pin-number** (*number*；預設：**1234**) | PIN 保護碼 |
| **hide-pin-number** (*yes | no*；預設：**no**) | 是在 LCD 螢幕上顯示輸入的數字，還是用星號將其隱藏 |

## LCD 螢幕/模式 {#lcd-screensmodes}

自 v6.0 起，LCD 具有選單結構。選單螢幕由用於導航選單的按鈕組成。如果內容無法完全顯示在實際螢幕上，螢幕右側會顯示捲軸。如果還有更多可用選項，可以向上或向下拖動螢幕來訪問它們。每個選單螢幕頂部都有一個 "Back" 按鈕，可跳轉到上一個螢幕。

### 啟動 {#startup}

![](/img/b7e3dabc4313f282.webp)

如果路由器使用預設配置——使用者名稱為 "admin" 且沒有密碼，則 LCD 上會出現警告。此螢幕顯示分配給各介面的 IP 地址，可用於連線路由器。否則，啟動後會顯示主選單螢幕。

### 介面 {#interfaces}

Interfaces 選單顯示所有乙太網和無線介面。頻寬使用情況的顯示方式與 All interface 圖表螢幕類似。在 Interfaces 螢幕上，您可以選擇要檢視的特定介面。可用選項如下：

- Info（僅限物理介面）- 顯示介面相關資訊的選單。
- Registration Table（僅限無線介面）- 顯示該無線介面所有已註冊用戶端及其各自訊號強度的選單。
- Addresses - 列出分配給該介面的所有地址的選單。
- Stats - 允許您跳轉到 "Stats" 螢幕中所選介面的選單。您可以直接選擇顯示 Bandwidth 或 Packets。

|  |  |  |  |
| :-- | :-- | :-- | :-- |
| ![](/img/54a0dafdc25ce2fc.jpg)  Info  | ![](/img/24fbfa7cdb655cfe.jpg)  Registration Table  | ![](/img/56c1afa87b0aae11.jpg)  Addresses  | ![](/img/222dfe20247759b5.jpg)  Stats 選擇  |

### 統計 {#stats}

Stats 螢幕顯示 RX 和 TX 的單介面圖表。數值從右向左更新（從最新到最舊）。顯示的資訊包括：RX/TX 速率和封包。

![](/img/baabdd8d0c21d2da.webp)

介面名稱顯示在右上角；如果名稱過長，它會被截斷（末尾的字元被截掉）。右上角顯示這些數值對應的時間間隔。可用的時間值如下：

- **Min（分鐘）** - 顯示最近一分鐘的數值。單位 = 秒。垂直線分隔前 30 秒。總數值：30 + 24。
- **Hour** - 顯示最近數小時的數值。單位 = 5 分鐘。垂直線分隔 1 小時。總數值：12 + 12 + 3。
- **Daily** - 顯示最近數天的數值。單位 = 小時。垂直線分隔 1 天。總數值：12 + 12 + 3。
- **Weekly** - 顯示最近數週的數值。單位 = 天。垂直線分隔 1 周。總數值：7 + 7 + 4。

## 手勢 {#motions}

- 點選 - 手指觸碰觸控式螢幕且移動幅度不大。
  - 如果點選落在螢幕右上角（高度為螢幕 1/4 的方形區域），資訊時間間隔會切換：Min -> Hour -> Daily -> Weekly -> Min...
  - 否則，點選會在圖表資訊之間迴圈切換：rate -> packets -> rate...
- 滑動/拖動 - 按住手指的同時向任意方向移動。拖動過程中更改項應會高亮顯示。
  - 上 - 進入主選單。
  - 下 - 選擇 All Interface 圖表螢幕。
  - 左 - 下一個介面。
  - 右 - 上一個介面。

### All Interface 圖表螢幕 {#all-interface-graph-screen-1}

![](/img/73afe769af809f81.webp)

All interface 圖表螢幕顯示所有介面的 RX/TX 頻寬使用情況。最大值的計算方式如下——對於乙太網介面，為協商速率或設定速率。對於無線介面，則根據所用頻段、通道寬度和鏈數，使用理論值計算。此螢幕的目的是檢視單個介面上各數值之間的相互關係。

## 手勢 {#motions-1}

- 滑動/拖動：
  - 上 - 返回（到 Stats 螢幕）。
  - 左 - 下一頁。
  - 右 - 上一頁。

### 統計幻燈片 {#stat-slideshow}

Stat Slideshow 螢幕與 "Stats" 螢幕類似，但介面會在超時後切換。幻燈片播放的設定儲存在 RouterOS 子選單 `/lcd/interface` 中

### 資訊幻燈片 {#informative-slideshow}

子選單 `/lcd/screen` 中的 Informative Slideshow 螢幕會迴圈顯示各種系統資訊：

- 總流量。
- 總封包。
- 資源。
- 系統。
- 健康。
- 日期和時間。

|  |  |  |
| :-- | :-- | :-- |
| ![](/img/556666c2b85fc33a.jpg)  系統  | ![](/img/a011c555fbd9b951.jpg)  資源  | ![](/img/6fc018ab15574df5.jpg)  健康  |

### 日誌 {#log}

![](/img/e11d01a3e7b29812.webp)
Log 螢幕顯示 log action=echo 的最近 5 條日誌記錄。

### 重啟和重設配置 {#reboot-and-reset-configuration}

這些螢幕僅在只讀模式被停用時可用。要訪問其中任何一個螢幕，都必須輸入 PIN 碼。如果 PIN 認證成功，使用者必須按 "Yes" 按鈕確認所需操作，或按 "No" 取消。
