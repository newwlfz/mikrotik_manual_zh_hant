---
sidebar_key: "cli-reference/system/scheduler"
sidebar_position: 26
title: "scheduler"
sidebar_label: 'scheduler'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/scheduler
captured_at: '2026-11-01T21:25:44+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/scheduler {#systemscheduler}
**型別：** 目錄

排程器條目在設定的日期和時間執行 RouterOS 命令或 `/system/script` 條目，也可以按間隔重複執行、在啟動期間執行，或在選定的工作日執行。有關示例以及下次執行時間的計算方式，請參閱 [排程器](../../system-information-and-utilities/scheduler.md) 指南。`reset` 命令會清除 `on-event` 並將 `interval` 設定為 `0s`；它不會重設 `run-count`。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用的條目；在啟用前不會執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">條目名稱。其執行產生的日誌訊息會以 `scheduler:<name>` 指代它。</ArgTableRow>
<ArgTableRow arg="start-date" typ="date">首次執行的日期，格式為 `YYYY-MM-DD`（年份 1970..2106）。預設值：新增條目時的日期。</ArgTableRow>
<ArgTableRow arg="start-time" typ="alt { startup: enum (startup) { startup:0xffffffff }
, time: date
 }">
首次執行的時間：

- `HH:MM:SS` - 首次執行會在 `start-date` 的此時間發生。
- `startup` - 在系統啟動期間執行。當 `interval=0s` 時，條目在每次啟動時執行一次。當 `interval` 非零時，首次執行發生在啟動後一個間隔（或在路由器執行期間新增條目後一個間隔），而不是在啟動本身時。

啟動執行發生在介面啟用之前，也發生在 DHCP 用戶端獲得地址之前。預設值：新增條目時的時間。
</ArgTableRow>
<ArgTableRow arg="days" typ="alt { day: enum (never | always) { never:0, always:127 }
, day: ubit (sun, mon, tue, wed, thu, fri, sat)
 }" unset="1">
條目執行的星期幾：

- 未設定（預設）- 不考慮星期幾。執行按 `start-time` 加 `interval` 連續跨越午夜。
- `always` - 每天，按日排程：每天重新從 `start-time` 開始。
- `never` - 該條目從不執行。
- `sun`、`mon`、`tue`、`wed`、`thu`、`fri`、`sat` - 僅在列出的日期執行（以逗號分隔）。每個匹配的日期從 `start-time` 開始，並按 `interval` 重複，直到當天結束。當 `interval=0s` 時，條目在每個匹配的日期執行一次。

當設定了 `days` 時，不支援 `1d` 或更長的 `interval`；此時條目會顯示提示 `multi-day intervals are not supported with active day scheduling`。
</ArgTableRow>
<ArgTableRow arg="interval" typ="time">執行之間的時間間隔。執行發生在 `start-date` 和 `start-time` 加上間隔的整數倍時，因此過去的開始時間會對齊排程：`start-time=00:00:00 interval=1h` 會在每個整點執行。`0s` 會讓條目在 `start-date` 和 `start-time` 執行一次（設定了 `days` 時，在每個匹配的日期執行一次）。預設值：0s。</ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { script: string
 }">要執行的 RouterOS 命令，或 `/system/script` 條目的名稱。按名稱呼叫的指令碼會使用此條目的 `policy` 執行；當指令碼自身的策略具有此條目的策略所缺少的許可權時，會以 `not enough permissions` 拒絕執行。預設值：空。</ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, policy: enum
 }">命令執行所使用的策略。需要某個缺失策略的命令會在日誌中失敗，並顯示 `not enough permissions (9)`。請參閱 [指令碼許可權](../../developer-guides/scripting/index.md#script-permissions)。預設值：新增條目的使用者的策略，限於 `ftp`、`reboot`、`read`、`write`、`policy`、`test`、`password`、`sniff`、`sensitive` 和 `romon`。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="owner" typ="string">新增該條目的使用者。</ArgTableRow>
<ArgTableRow arg="run-count" typ="num">自上次啟動以來的執行次數。重啟會將其重設為 0。</ArgTableRow>
<ArgTableRow arg="next-run" typ="date">下次執行的日期和時間。當沒有待執行的執行時為空：執行結束後的 `interval=0s` 條目、`interval=0s` 的 `startup` 條目，或 `days=never` 的條目。</ArgTableRow>
</ArgTable>
