---
sidebar_key: "cli-reference/system/clock/manual"
sidebar_position: 1
title: "manual"
sidebar_label: 'manual'
source: https://manual.mikrotik.com/docs/cli-reference/system/clock/manual
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/clock/manual {#systemclockmanual}
**型別：** 設定目錄

手動 GMT 偏移量和夏令時設定，在 [`/system/clock`](./index.md) 中的 `time-zone-name` 為 `manual` 時生效。參見 [時鐘](../../../system-information-and-utilities/clock.md) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="time-zone" typ="timezone">夏令時未生效時的 GMT 偏移量。僅在 `time-zone-name` 為 `manual` 時生效。預設值：+00:00。</ArgTableRow>
<ArgTableRow arg="dst-delta" typ="timezone">夏令時生效時加到 `time-zone` 上的偏移量。接受負值，用於冬季時間即為夏令時時段所在的時區。預設值：+00:00。</ArgTableRow>
<ArgTableRow arg="dst-start" typ="date">夏令時時段開始的本地日期和時間。夏令時從 `dst-start` 到 `dst-end` 完全按配置生效：該時段是單一的日期區間，不會在後續年份重複。如果 `dst-start` 晚於 `dst-end`，則夏令時永不生效。格式：YYYY-MM-DD HH:MM:SS。省略的日期或時間部分會被重設，日期重設為 1970-01-01，時間重設為 00:00:00（例如 `dst-start=05:00:00` 會得到 `1970-01-01 05:00:00`），因此請始終給出兩部分。預設值：1970-01-01 00:00:00。</ArgTableRow>
<ArgTableRow arg="dst-end" typ="date">夏令時時段結束的本地日期和時間。有關該時段的應用方式，請參見 `dst-start`。格式：YYYY-MM-DD HH:MM:SS。省略的日期或時間部分會被重設，日期重設為 1970-01-01，時間重設為 00:00:00，因此請始終給出兩部分。預設值：1970-01-01 00:00:00。</ArgTableRow>
</ArgTable>
