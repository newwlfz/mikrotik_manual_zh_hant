---
sidebar_key: "cli-reference/system/clock"
title: "clock"
sidebar_label: 'clock'
source: https://manual.mikrotik.com/docs/cli-reference/system/clock
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/clock {#systemclock}
**型別：** 設定目錄

系統時鐘設定：本地日期和時間、時區選擇以及自動時區檢測。有關時間源、夏令時配置和故障排除的資訊，請參閱 [時鐘](../../../system-information-and-utilities/clock.md) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="time" typ="date">HH:MM:SS，其中 HH 表示小時 00..23，MM 表示分鐘 00..59，SS 表示秒 00..59。設定或顯示路由器上的當前本地時間。當在一條命令中同時設定 `date` 和 `time` 時，時間會按照更改前生效的 GMT 偏移量來解釋。</ArgTableRow>
<ArgTableRow arg="date" typ="date">YYYY-MM-DD，其中 YYYY 表示年份，MM 表示月份 01..12，DD 表示日期 01..31。設定或顯示路由器上的當前本地日期。日期不能設定為早於已安裝 RouterOS 版本的構建日期，而晚於 2038-01-19 03:14:07 UTC 的日期會被忽略且不會報錯。本地時間無法匯出，也不會與配置的其餘部分一起儲存。</ArgTableRow>
<ArgTableRow arg="time-zone-autodetect" typ="bool">如果啟用，MikroTik 雲服務會在啟動時根據路由器公共 IP 地址的位置查詢時區，並將其應用到 `time-zone-name`，包括夏令時。再次啟用該設定時也會執行檢測，檢測到的時區隨後會在幾秒內替換手動設定的時區。在檢測開啟時手動設定的 `time-zone-name` 會保留到下一次檢測。預設值：yes。</ArgTableRow>
<ArgTableRow arg="time-zone-name" typ="enum">來自 IANA 時區資料庫的時區名稱，例如 `Europe/Riga`。區分大小寫。該時區的夏令時規則會自動應用。特殊值 `manual` 會應用在 [`/system/clock/manual`](./manual.md) 中配置的 GMT 偏移量和夏令時時段。預設值：manual。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="gmt-offset" typ="timezone">系統當前使用的 GMT 偏移量值，已應用基礎時區偏移量和當前生效的夏令時偏移量。`print` 將其顯示為 `+03:00`；在指令碼中，`get gmt-offset` 會返回以秒為單位的偏移量，例如 `10800`。</ArgTableRow>
<ArgTableRow arg="dst-active" typ="bool">當前時區的夏令時時段生效時為 `yes`。</ArgTableRow>
</ArgTable>
