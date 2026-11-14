---
sidebar_key: "system-information-and-utilities/clock"
sidebar_position: 1
title: "時鐘"
sidebar_label: "時鐘"
description: "本頁介紹 MikroTik RouterOS 時鐘配置，詳細說明時區設定，包括自動檢測和手動調整、GMT 偏移、夏令時規則，以及有關內部時鐘可靠性的警告。"
tags:
  - 'time-zone'
  - 'clock'
  - 'ntp'
source: https://manual.mikrotik.com/docs/7.24/system-information-and-utilities/clock
captured_at: '2026-11-04T11:33:21+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 使用 TZ 資料庫中的資料。該資料庫中的大多數時區均已包含，並保持相同名稱。由於路由器上的本地時間主要用於時間戳記錄和依賴時間的配置，而不是用於歷史日期計算，因此不包含過去年份的時區資訊。目前僅包含從 2005 年開始的資訊。

以下設定可在 `/system/clock` 控制檯路徑以及 WinBox 的“System > Clock”視窗中的“Time”標籤頁中使用。

啟動日期和時間為 **1970-01-02 00:00:00** [+|-]gmt-offset。

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **time** (*HH:MM:SS);* | 其中 *HH* - 小時 00..23，*MM* - 分鐘 00..59，*SS* - 秒 00..59。 |
| **date** (*YYYY-MM-DD);* | 其中 *YYYY* - 年份，1970..2037，*MM* - 月份，01..12，*DD* - 日期，01..31：**date** 和 **time** 顯示路由器上的當前本地時間。這些值可以使用 **set** 命令調整。但是，本地時間無法匯出，並且不會與配置的其餘部分一起儲存。 |
| **time-zone-name** (*manual*，或時區名稱；預設值：*manual*)； | 時區名稱。與 RouterOS 中的大多數文字值一樣，此值區分大小寫。特殊值 *manual* 應用手動配置的 GMT 偏移，預設情況下為 *00:00*，且不啟用夏令時。 |
| **time-zone-autodetect** (*yes* 或 *no*；預設值：yes)； | 從 v6.27 起可用的功能。如果啟用，將自動設定時區。 |

:::warning
time-zone-autodetect 預設在新安裝 RouterOS 時以及配置重設後啟用。時區根據路由器的公共 IP 地址和我們的 Cloud 伺服器資料庫進行檢測。從 RouterOS v6.43 起，裝置將使用 cloud2.mikrotik.com 與 MikroTik 的 Cloud 伺服器通訊。較舊版本將使用 cloud.mikrotik.com 與 MikroTik 的 Cloud 伺服器通訊。

**重要：** 請注意，路由器的內部 CPU 時鐘不是用於精確計時操作的可靠時間源，因為其頻率可能會因電源管理、溫度條件以及硬體差異而變化，即使是相同型號之間也是如此。這種變化是預期內的，不會影響路由器的正常效能。為了準確計時，建議使用基於網路的時間同步，例如 NTP（Network Time Protocol）。
:::

配置

### 活動時區資訊 {#active-time-zone-information}

- **dst-active** (*yes* 或 *no*；只讀屬性)：當前時區的夏令時處於活動狀態時，此屬性的值為 *yes*。
- **gmt-offset** ([*+*|*-*]*HH:MM* - 以小時和分鐘表示的偏移量；只讀屬性)：這是系統在應用基礎時區偏移和當前生效的夏令時偏移後使用的當前 GMT 偏移值。

### 手動時區配置 {#manual-time-zone-configuration}

這些設定可在 `/system/clock/manual` 控制檯路徑以及 WinBox 的“System > Clock”視窗中的“Manual Time Zone”標籤頁中使用。僅當 **time-zone-name**=*manual* 時，這些設定才會生效。只能手動配置一個夏令時時段。

- **time-zone**、**dst-delta** ([*+*|*-*]*HH:MM* - 以小時和分鐘表示的時間偏移量，前導加號可選；預設值：*+00:00*)：當 DST 未生效時，使用 GMT 偏移 **time-zone**。當 DST 生效時，使用 GMT 偏移 **time-zone** + **dst-delta**。
- **dst-start**、**dst-end** (*YYYY-MM-DD HH:MM:SS* - 日期和時間，在 **set** 命令中可以省略日期或時間；預設值：*1970-01-01 00:00:00*)：DST 開始和結束時的本地時間。
