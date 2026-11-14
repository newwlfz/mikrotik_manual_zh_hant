---
sidebar_key: "system-information-and-utilities/clock"
sidebar_position: 1
title: "時鐘"
sidebar_label: "時鐘"
description: "RouterOS 系統時鐘：時間源（NTP 用戶端、MikroTik 雲服務、GPS）、時區選擇與自動檢測、手動 GMT 偏移與夏令時規則，以及啟動時的時鐘行為。"
tags:
  - 'time-zone'
  - 'clock'
  - 'ntp'
source: https://manual.mikrotik.com/docs/7.25/system-information-and-utilities/clock
captured_at: '2026-11-04T11:21:56+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 系統時鐘為日誌條目、[排程器](./scheduler.md)、檔案建立時間、證書有效性檢查以及其他依賴時間的功能提供本地日期和時間。RouterOS 以 UTC 儲存時間，並在顯示時間時應用所配置的 GMT 偏移，包括夏令時（DST）。

在具有網際網路訪問的路由器上無需任何配置：時區會被自動檢測，並且 MikroTik 雲服務會在路由器啟動時設定時鐘。為了保持計時準確，請啟用 [NTP 用戶端](./ntp.md)。

:::note
路由器內部的 CPU 時鐘並非用於精確計時操作的可靠時間源，因為其頻率會隨電源管理、溫度條件以及硬體差異而變化，即使是相同型號之間也是如此。這種變化不會影響路由器轉發流量或執行其服務的方式。為了保持計時準確，請使用基於網路的時間同步，例如 [NTP](./ntp.md)。
:::

## 檢查與故障排除 {#check-and-troubleshoot}

當前的時鐘狀態：

```ros
[admin@MikroTik] > /system/clock/print
                  time: 09:43:19
                  date: 2026-09-29
  time-zone-autodetect: yes
        time-zone-name: Europe/Riga
            gmt-offset: +03:00
            dst-active: yes
```

`gmt-offset` 是當前正在使用的偏移，已包含夏令時。`dst-active` 顯示該時區的夏令時時段是否生效。

時鐘錯誤的常見原因：

- 日期為 **1970-01-02**（在 GMT 以西的時區則為 1970-01-01）：路由器啟動時沒有已儲存的時間，且沒有任何時間源設定時鐘。請啟用 NTP 用戶端並檢查它能否訪問其伺服器，檢查路由器能否訪問 MikroTik 雲（在 [`/ip/cloud`](../network-management/cloud/index.md) 中設定 `update-time=yes`；當 NTP 用戶端啟用時，雲不會設定時鐘），或者手動設定時間。
- 時間正確但時區錯誤：自動檢測使用了路由器公網 IP 地址的位置，而網際網路服務提供商有時會將該地址註冊在另一個地區。請改為手動設定時區，並關閉檢測。
- 重啟後時間相差一小時：在 `time-zone-autodetect` 開啟時手動設定的 `time-zone-name` 會在啟動後不久被檢測到的時區替換。自行設定時區時請關閉檢測，如[設定時區](#set-the-time-zone)中所述。
- 設定日期後時間相差一小時：在跨越夏令時變更時於同一條命令中設定 `date` 和 `time` 會使用舊的偏移。請單獨再次設定時間，例如 `/system/clock/set time=10:00:00`。
- 手動時區在下一年停止切換到夏令時：手動 DST 時段不會重複。請更新 `dst-start` 和 `dst-end`，或使用命名時區。

## 設定時間 {#set-the-time}

路由器可以從多個來源獲取時間：

- [NTP 用戶端](./ntp.md)，它會精確地同步時鐘並保持其準確性。當時鍾精度很重要時請使用此項。
- [MikroTik 雲服務](../network-management/cloud/index.md)，當 NTP 用戶端被停用且在 `/ip/cloud` 中啟用了 `update-time` 時，它會在啟動時設定一次時鐘。雲時間是大致的。
- 在具有 GPS 硬體的裝置上，當 `/system/gps` 中啟用了 `set-system-time` 時，可使用 [GPS](../mobile-networking/gps/index.md)。
- 手動設定：

```ros
/system/clock/set date=2026-10-01
/system/clock/set time=10:00:00
```

請先設定日期，並在單獨的命令中設定時間。當你在同一條命令中設定 `date` 和 `time` 時，時間會按照變更之前生效的 GMT 偏移來解釋，因此在跨越夏令時變更時，時鐘最終會偏移一個 DST 差值。

本地時間不屬於匯出的配置內容：`/export` 只包含時區設定，從不包含當前的日期和時間。

## 設定時區 {#set-the-time-zone}

在可能的情況下請選擇命名時區：

```ros
/system/clock/set time-zone-autodetect=no time-zone-name=Europe/Riga
```

在 WinBox 中，開啟 **System > Clock** 並使用 **Time** 標籤頁：

1. 清除 **Time Zone Autodetect**，然後選擇 **Time Zone Name**，例如 `Europe/Riga`。選擇 **OK** 儲存選擇。如果你希望由雲服務來選擇時區，則保留自動檢測選中狀態。
2. 檢視只讀的 **GMT Offset** 和 **DST Active** 欄位，以瞭解生效的偏移和夏令時狀態。

![WinBox Clock Time tab with time zone and clock status settings](/img/778b56ee7b94a12c.webp)

**Time** 和 **Date** 欄位用於手動更改時鐘；請使用 NTP 用戶端進行持續同步。

RouterOS 包含 IANA 時區資料庫中的大多數時區，名稱相同。名稱區分大小寫，例如 `Europe/Riga`：在終端中於 `time-zone-name=` 之後按 <kbd>Tab</kbd> 可列出它們。拼寫錯誤的名稱會失敗並提示 `input does not match any value of time-zone-name`。該時區的夏令時規則會自動應用，而沒有夏令時的時區（例如 `Asia/Dubai`）全年保持一個偏移。由於路由器上的本地時間用於打時間戳和依賴時間的配置，而非歷史日期計算，因此關於過去年份的時區資訊是有限的：只包含從 2005 開始的資料。

### 自動時區檢測 {#automatic-time-zone-detection}

`time-zone-autodetect` 預設啟用。在啟動時，MikroTik 雲服務會查詢路由器公網 IP 地址所在位置的時區並應用它，包括夏令時。當你再次啟用該設定時，檢測也會執行：檢測到的時區隨後會在數秒內替換手動設定的時區。在檢測開啟時設定的 `time-zone-name` 只會保留到下一次檢測，而該檢測會在下一次啟動後不久執行。

如果檢測到的時區不正確，請在設定時區時關閉檢測，如[設定時區](#set-the-time-zone)中的示例所示。

## 設定手動時區和夏令時 {#set-a-manual-time-zone-and-daylight-saving}

當沒有匹配的命名時區，或者你需要自定義 GMT 偏移時，請將 `time-zone-name` 設定為 `manual` 並配置 [`/system/clock/manual`](../cli-reference/system/clock/manual.md) 子選單。這些設定僅在 `time-zone-name` 為 `manual` 時生效，並且只能配置一個 DST 時段。

設定 GMT+02:00 的偏移，並從三月底到十月底使用一小時的夏令時：

```ros
/system/clock/set time-zone-autodetect=no time-zone-name=manual
/system/clock/manual/set time-zone=+02:00 dst-delta=+01:00 \
    dst-start="2026-03-29 03:00:00" dst-end="2026-10-25 04:00:00"
```

```ros
[admin@MikroTik] > /system/clock/manual/print
  time-zone: +02:00
  dst-delta: +01:00
  dst-start: 2026-03-29 03:00:00
    dst-end: 2026-10-25 04:00:00
```

手動設定的工作方式：

- 當 DST 未生效時，GMT 偏移為 `time-zone`。當 DST 生效時，則為 `time-zone` + `dst-delta`。`dst-delta` 可以為負值，用於冬季時間才是夏令時時段的時區。
- DST 從 `dst-start` 到 `dst-end` 生效，完全按照配置執行。該時段是單個日期範圍，不會在後續年份中重複：請每年更新 `dst-start` 和 `dst-end`，或使用命名時區，後者會保持規則最新。
- 請同時給出 `dst-start` 和 `dst-end` 的日期和時間。省略的部分會被重設：日期重設為 1970-01-01，時間重設為 00:00:00。例如，`dst-start=05:00:00` 會得到 `1970-01-01 05:00:00`。
- 如果 `dst-start` 晚於 `dst-end`，DST 永遠不會生效。對於夏季跨越年末的南半球，請將 `dst-start` 設定在較早的年份，將 `dst-end` 設定在較晚的年份，例如 `2026-10-04 02:00:00` 到 `2027-04-04 03:00:00`。

## 技術細節 {#technical-details}

### 啟動時的時鐘 {#clock-at-startup}

RouterOS 在時間被更改時、在正常重啟時以及每天一次儲存當前時間，並在啟動時恢復它。因此，重啟後即使沒有網路時間源，時鐘也會從已儲存的時間開始，而當時間源響應時會更正它。當路由器沒有已儲存的時間時（例如在全新安裝時），日期從 1970-01-02 00:00:00 UTC 開始，並按所配置時區的 gmt-offset 顯示。

### 時鐘限制 {#clock-limits}

日期不能早於所安裝 RouterOS 版本的構建日期：路由器會返回 `cannot set time before package build time`。時鐘可接受的最晚日期是 2038-01-19 03:14:07 UTC；更晚的日期會被忽略且不報錯，時鐘保持其時間。

### 時區檢測 {#time-zone-detection}

檢測使用與其他 [MikroTik 雲服務](../network-management/cloud/communication-mikrotik-cloud-servers.md)相同的到 `cloud2.mikrotik.com` 的連線。檢測到的時區會儲存在配置中，並在 `/system/clock/export` 中顯示為 `time-zone-name`。在首次成功檢測之前，`time-zone-name` 為 `manual`，GMT 偏移為 +00:00。

有關所有屬性，請參閱 CLI 參考中的 [`/system/clock`](../cli-reference/system/clock/index.md) 和 [`/system/clock/manual`](../cli-reference/system/clock/manual.md)。
