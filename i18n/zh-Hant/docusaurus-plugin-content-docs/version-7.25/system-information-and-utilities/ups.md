---
sidebar_key: "system-information-and-utilities/ups"
sidebar_position: 16
title: "UPS"
sidebar_label: "UPS"
description: "適用於 APC UPS 裝置的 UPS 監視功能支援 serial/USB 連線，可透過休眠和安全重啟能力妥善處理斷電。它會監視電池狀態、執行測試、記錄電源變化，並需要透過 ups.npk 軟體包手動安裝。"
tags:
  - 'ups'
source: https://manual.mikrotik.com/docs/7.25/system-information-and-utilities/ups
captured_at: '2026-11-04T11:22:15+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 概述 {#summary}

**子選單：** `/system/ups`
**標準：**  `APC Smart Protocol`

UPS 監控功能適用於透過序列 RS232 或 USB 連線支援 "smart" 信令的 APC UPS 裝置。UPS 監控服務不包含在預設軟體包集合中，需要手動下載並安裝 ups.npk 軟體包。該功能使網路管理員能夠監控 UPS，並將路由器設定為在停電時“平穩”處理，而不會損壞路由器。該功能的基本目的是確保路由器在長時間斷電後能夠重新上線。為此，路由器會監控 UPS，並在市電中斷且 UPS 電池剩餘電量低於 10% 時，將自身置於休眠模式。隨後路由器（在休眠模式下）會繼續監控 UPS，並在市電恢復時自行重啟。如果 UPS 電池耗盡且路由器完全斷電，那麼當“市電”恢復時，路由器將重新恢復完整執行。

MikroTik RouterOS 上的 UPS 監控功能支援：

- 在電源和電池故障時休眠並安全重啟
- UPS 電池測試和執行時間校準測試
- 監控 UPS 支援的所有 "smart" 模式狀態資訊
- 記錄電源變化日誌

### 連線 UPS 裝置 {#connecting-the-ups-unit}

序列 APC UPS（BackUPS Pro 或 SmartUPS）需要專用的序列線纜（除非透過 USB 連線）。如果 UPS 未隨附線纜，可以向 APC 訂購，也可以“自制”。請使用以下接線圖：

| 路由器側（DB9f） | 訊號 | 方向 | UPS 側（DB9m） |
| --: | :-- | :-- | --: |
| 2 | 接收 | IN | 2 |
| 3 | 傳送 | OUT | 1 |
| 5 | 接地 |  | 4 |
| 7 | CTS | IN | 6 |

如果使用 RouterBOARD 裝置，請務必將 "RouterBOOT setup key" 設定為 *Delete*，而不是預設的 *Any key*。這樣可以避免在 RouterBOARD 啟動期間，UPS 裝置向序列埠傳送資料時意外開啟設定選單。可以在啟動時透過 RouterBOOT 選項完成此設定，也可以透過 Winbox 中的 RouterBoard Settings 完成：

```
Select key which will enter setup on boot:
 * 1 - any key
   2 - <Delete> key only
your choice:

```

### 常規屬性 {#general-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **alarm-setting** (*delayed \| immediate \| low-battery \| none*；預設：**immediate**) | UPS 聲音報警設定：delayed - 報警延遲到 on-battery 事件時觸發immediate - 在 on-battery 事件後立即報警low-battery - 僅在電池電量低時報警none - 不報警 |
| **check-capabilities** (*yes \| no*；預設：**yes**) | 是否在讀取資訊之前檢查 UPS 能力。停用此項可修復與某些 UPS 型號的相容性問題。（適用於 RouterOS 版本 6，自 v6.17 起實現） |
| **min-runtime** (*time*；預設：**never**) | 最小剩餘執行時間。在“市電”故障後，路由器會監控 runtime-left 值。當該值達到 min-runtime 值時，路由器將進入休眠模式。  never - 當收到表示電池電量低於 10% 的 "battery low" 訊號時，路由器將進入休眠模式0s - 只要電池能提供足夠的電壓，路由器就會繼續工作 |
| **offline-time** (*time*；預設：**0s**) | 使用電池供電的工作時長。路由器等待該時間後進入休眠模式，直到 UPS 報告“市電”恢復  0s - 路由器將根據 min-runtime 設定進入休眠模式。在這種情況下，路由器會一直等待，直到 UPS 報告電池電量低於 10% |
| **port** (*string*；預設：) | 路由器的通訊埠。 |

### 只讀屬性 {#read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **load** (*percent*) | UPS 的輸出負載，以額定滿載（瓦特）的百分比表示。該測量的典型精度為最大 105% 的 ±3% |
| **manufacture-date** (*string*) | UPS 的生產日期，格式為 "mm/dd/yy"（月、日、年）。 |
| **model** (*string*) | 少於 32 個 ASCII 字元的字串，由 UPS 型號名稱組成（即 UPS 正面上的文字） |
| **nominal-battery-voltage** (*integer*) | UPS 的標稱電池電壓額定值（這不是 UPS 的實際電池電壓） |
| **offline-after** (*time*) | 路由器何時離線 |
| **serial** (*string*) | 至少 8 個字元的字串，直接表示出廠時設定的 UPS 序列號。較新的 SmartUPS 型號具有 12 個字元的序列號 |
| **version** (*string*) | UPS 版本由三個欄位組成：SKU 編號、韌體修訂版本、國家程式碼。國家程式碼可能為以下之一：I - 220/230/240 VacD - 115/120 VacA - 100 VacM - 208 VacJ - 200 Vac |

:::info
**注意：** 要啟用 UPS 監控，序列埠必須可用。
:::

#### 示例 {#example}

為 serial1 埠啟用 UPS 監控：

```
[admin@MikroTik] /system/ups> add port=serial1 disabled=no
[admin@MikroTik] /system/ups> print
Flags: X - disabled, I - invalid
 0    name="ups" port=serial1 offline-time=5m min-runtime=5m
      alarm-setting=immediate model="SMART-UPS 1000" version="60.11.I"
      serial="QS0030311640" manufacture-date="07/18/00"
      nominal-battery-voltage=24V
[admin@MikroTik] /system/ups>

```

### 執行時間校準 {#runtime-calibration}

**命令：**  `/system/ups/rtc/<id>`

rtc 命令會讓 UPS 開始執行時間校準，直到電池容量降至低於滿容量的 25%。該命令會校準返回的執行時間值。

:::info
**注意：** 僅當電池容量為 100% 時才會開始測試。
:::

### 監控 {#monitoring}

**命令：**  `/system/ups/monitor <id>`

| 屬性 | 描述 |
| :-- | :-- |
| **battery-charge** () | UPS 的剩餘電池容量，以完全充滿狀態的百分比表示 |
| **battery-voltage** () | UPS 的當前電池電壓。該測量的典型精度為最大值的 ±5%（取決於 UPS 的標稱電池電壓） |
| **frequency** () | 線上執行時，UPS 的內部工作頻率與市電同步，偏差在標稱 50 或 60 Hz 的 3 Hz 範圍內。該測量的典型精度為滿量程值 63 Hz 的 ±1% |
| **line-voltage** () | 線上市電電壓 |
| **load** () | UPS 的輸出負載，以額定滿載（瓦特）的百分比表示。該測量的典型精度為最大 105% 的 ±3% |
| **low-battery** (*yes \| no*) | 僅在 UPS 報告此狀態時顯示 |
| **on-battery** (*yes \| no*) | UPS 電池是否正在供電 |
| **on-line** (*yes \| no*) | 電力是否由外部電網（電力公司）提供 |
| **output-voltage** () | UPS 的輸出電壓 |
| **overloaded-output** (*yes \| no*) | 僅在 UPS 報告此狀態時顯示 |
| **replace-battery** (*yes \| no*) | 僅在 UPS 報告此狀態時顯示 |
| **runtime-calibration-running** (*yes \| no*) | 僅在 UPS 報告此狀態時顯示 |
| **runtime-left** (*time*) | UPS 估計的剩餘執行時間（分鐘）。可以在 UPS 處於線上、旁路或電池供電模式時進行查詢。UPS 的剩餘執行時間回覆基於可用電池容量和輸出負載 |
| **smart-boost-mode** (*yes \| no*) | 僅在 UPS 報告此狀態時顯示 |
| **smart-ssdd-mode** () | 僅在 UPS 報告此狀態時顯示 |
| **transfer-cause** (*string*) | 最近一次切換到電池供電的原因（僅在裝置使用電池供電時顯示） |

#### 示例 {#example-1}

使用市電供電時：

```
[admin@MikroTik] /system/ups> monitor 0
          on-line: yes
       on-battery: no
      RTC-running: no
     runtime-left: 20m
   battery-charge: 100%
  battery-voltage: 27V
     line-voltage: 226V
   output-voltage: 226V
             load: 45%
      temperature: 39C
        frequency: 50Hz
  replace-battery: no
      smart-boost: no
       smart-trim: no
         overload: no
      low-battery: no

[admin@MikroTik] /system/ups>

```

使用電池供電時：

```
[admin@MikroTik] /system/ups> monitor 0
          on-line: no
       on-battery: yes
   transfer-cause: "Line voltage notch or spike"
      RTC-running: no
     runtime-left: 19m
    offline-after: 4m46s
   battery-charge: 94%
  battery-voltage: 24V
     line-voltage: 0V
   output-voltage: 228V
             load: 42%
      temperature: 39C
        frequency: 50Hz
  replace-battery: no
      smart-boost: no
       smart-trim: no
         overload: no
      low-battery: no

      [admin@MikroTik] /system/ups>

```
