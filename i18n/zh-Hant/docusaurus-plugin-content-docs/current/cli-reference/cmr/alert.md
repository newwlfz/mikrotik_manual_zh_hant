---
sidebar_key: "cli-reference/cmr/alert"
title: "alert"
source: https://manual.mikrotik.com/docs/cli-reference/cmr/alert
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/alert {#cmralert}
**包：** cmr
**型別：** Directory

告警規則定義條件，並在 CMR 控制器上執行其動作。裝置規則透過 `labels` 選擇裝置。狀態告警在所有已配置的狀態條件匹配期間保持活動，並在變為活動時執行一次動作。僅當條件停止匹配、隨後再次匹配後，它們才會再次觸發。事件告警針對每次匹配的發生執行動作，且從不保持活動，也不計入活動告警計數器。一條規則可以包含多個狀態條件，但最多隻能包含一個事件條件。大多數告警按裝置應用；`upgrade-job-done` 是用於整個升級作業的系統事件。有關條件、動作和告警作用範圍，請參閱 [CMR - 告警規則](../../management-tools/cmr.md#alert-rules)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">警報規則已停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" unset="1">警報規則的名稱。</ArgTableRow>
<ArgTableRow arg="labels" typ="object" unset="1">
Select the devices, by labels, that the alert rule applies to. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used.

當未設定 `labels` 時，該規則應用於所有已連線裝置（`labels=all`）。
</ArgTableRow>
<ArgTableRow arg="connected" typ="bool" unset="1">
狀態條件，用於匹配裝置是已連線（`yes`）還是已斷開（`no`）。

預設：no。
</ArgTableRow>
<ArgTableRow arg="cpu-above" typ="num" unset="1">
當 CPU 負載高於給定百分比值（0..100）時告警；等於閾值也會觸發該規則。

預設：unset。
</ArgTableRow>
<ArgTableRow arg="cpu-below" typ="num" unset="1">
當 CPU 負載低於給定百分比值（0..100）時告警；僅當值嚴格低於閾值時才觸發。

預設：unset。
</ArgTableRow>
<ArgTableRow arg="hdd-above" typ="num" unset="1">
當磁碟（HDD）負載高於給定百分比值（0..100）時告警；等於閾值也會觸發該規則。

預設：unset。
</ArgTableRow>
<ArgTableRow arg="hdd-below" typ="num" unset="1">
當磁碟（HDD）負載低於給定百分比值（0..100）時告警；僅當值嚴格低於閾值時才觸發。

預設：unset。
</ArgTableRow>
<ArgTableRow arg="mem-above" typ="num" unset="1">
當 RAM 負載高於給定百分比值（0..100）時告警；等於閾值也會觸發該規則。

預設值：unset。
</ArgTableRow>
<ArgTableRow arg="mem-below" typ="num" unset="1">
當 RAM 負載低於給定的百分比值（0..100）時發出告警；僅當值嚴格低於閾值時觸發。

預設值：unset。
</ArgTableRow>
<ArgTableRow arg="health-above" typ="num" unset="1">
當由 `health-value` 指定的健康感測器高於給定值時發出告警；等於閾值也會觸發該規則。不上報該感測器的裝置會被忽略。

預設值：unset。
</ArgTableRow>
<ArgTableRow arg="health-below" typ="num" unset="1">
當由 `health-value` 指定的健康感測器低於給定值時發出告警；僅當值嚴格低於閾值時觸發。不上報該感測器的裝置會被忽略。

預設值：unset。
</ArgTableRow>
<ArgTableRow arg="health-value" typ="string" unset="1">要比較的健康感測器名稱，需匹配 `/system/health/print` 中的名稱，例如 `cpu-temperature`。在動作文字中使用 `[cpu-temperature]` 樣式的佔位符。</ArgTableRow>
<ArgTableRow arg="interface-change" typ="alt { change: enum (any)
, change: ubit (running, not-running, added, removed)
 }" unset="1">
在介面狀態變化時發出告警：

- `any`（預設）- 任何狀態變化。
- `running` - 介面的鏈路接通。
- `not-running` - 介面的鏈路斷開。
- `added` - 首次發現介面。
- `removed` - 不再發現介面。

`running` 和 `not-running` 遵循介面的鏈路狀態，而不是其管理狀態：啟用或停用沒有連線的介面不會觸發，而實際鏈路丟失或恢復則會觸發。
</ArgTableRow>
<ArgTableRow arg="interface-type" typ="alt { type: enum (any)
, type: ubit (ethernet, wifi, bridge)
 }" unset="1">
將 `interface-change` 告警限制為一種介面型別：

- `any`（預設）- 任意型別的介面。
- `ethernet` - Ethernet 埠。
- `wifi` - 無線介面。
- `bridge` - 橋接介面。
</ArgTableRow>
<ArgTableRow arg="upgrade-available" typ="bool" unset="1">
當裝置有更新的 RouterOS 版本可用時發出告警。

預設值：no。
</ArgTableRow>
<ArgTableRow arg="disconnected-more-than" typ="time" unset="1">
當裝置斷開連線的時間超過給定時間時發出告警。

預設：unset。
</ArgTableRow>
<ArgTableRow arg="upgrade-job-done" typ="alt { cond: enum (yes)
, cond: ubit (success, fail)
 }" unset="1">
當升級任務完成時告警；該規則對整個任務只觸發一次，即在任務中最後一臺裝置完成時觸發：

- `yes`（預設）- 任意結果。
- `success` - 任務成功完成。
- `fail` - 任務失敗。

未安裝升級便結束的任務會被視為失敗任務，因此 `yes` 和 `fail` 兩種取值都會觸發。
</ArgTableRow>
<ArgTableRow arg="upgrade-done" typ="alt { cond: enum (yes)
, cond: ubit (success, fail)
 }" unset="1">
當某臺裝置的升級完成時告警；該規則對每臺完成升級的裝置各觸發一次：

- `yes`（預設）- 任意結果。
- `success` - 升級成功完成。
- `fail` - 升級失敗。

當裝置沒有更新的版本可用時，其升級仍會以失敗結束（`[upgrade-error]` 為 `no upgrade available`），因此 `yes` 和 `fail` 兩種取值都會觸發。
</ArgTableRow>
<ArgTableRow arg="unpaired-device-connected" typ="bool" unset="1">
當一臺未與控制器配對的裝置連線時告警。

預設：no。
</ArgTableRow>
<ArgTableRow arg="rebooted" typ="bool" unset="1">
事件條件，在裝置重啟時觸發；當重啟是升級的一部分或來自 `/cmr/device/reboot` 時也會觸發。

預設：no。
</ArgTableRow>
<ArgTableRow arg="log-topics" typ="multi { array-id, array-id, topic: super { !
, topic: enum
 }
 }" unset="1">要跟蹤的日誌主題；在主題前加上 `!` 可將其排除。與 `log-regex` 一起定義日誌訊息事件條件。CMR 會自動指示裝置轉發匹配的日誌訊息。</ArgTableRow>
<ArgTableRow arg="log-regex" typ="string" unset="1">用給定的正則表示式匹配日誌訊息。每條同時匹配所配置主題和正則表示式的訊息都會觸發動作，但不會建立持久的活動告警。</ArgTableRow>
<ArgTableRow arg="action.log" typ="string" unset="1">告警觸發時向日志寫入一條訊息。訊息中可以包含諸如 `[device]` 或 `[cpu-usage]` 的佔位符，它們會被替換為觸發告警的裝置的值；不適用的佔位符會呈現為 `unknown`。</ArgTableRow>
<ArgTableRow arg="action.log-topics" typ="multi { array-id, topic: enum
 }" unset="1">
要將訊息寫入的日誌主題。

預設：`cmr,info`，對於日誌行條件則為 `cmr,warning`。
</ArgTableRow>
<ArgTableRow arg="action.log-prefix" typ="string" unset="1">日誌訊息的字首。設定後，字首會直接加在訊息之前，中間不加分隔符；未設定時，訊息按原樣寫入。</ArgTableRow>
<ArgTableRow arg="action.script" typ="enum" unset="1">告警觸發時執行指定的系統指令碼。該指令碼必須允許自身以降低的許可權執行；否則該動作會失敗並報 `executing script ... from cmr failed ... (not enough permissions)`。請將該指令碼的 `dont-require-permissions` 設為 yes。</ArgTableRow>
<ArgTableRow arg="action.script-vars" typ="multi { array-id, script-var: string
 }" unset="1">要提供給 `action.script` 的變數名列表：每個變數都會填入觸發告警的裝置對應的值。例如 `device`、`identity`、`address`、`board`、`version` 在指令碼中會變成 `$device`、`$identity` 等。帶連字元的名稱（例如 `cpu-usage`）無法作為普通指令碼變數讀取。</ArgTableRow>
<ArgTableRow arg="action.http-url" typ="string" unset="1">觸發告警時要呼叫的 HTTP webhook URL。呼叫失敗時，告警會將 `alert "<name>" HTTP action failed: <reason>` 寫入 `cmr` 主題，嚴重級別為 `warning`，並在 `action-failures` 中統計該失敗；其他操作仍會執行。</ArgTableRow>
<ArgTableRow arg="action.http-method" typ="enum (get | post | put | delete | head | patch)" unset="1">
用於 webhook 的 HTTP 方法：

- `get`
- `post`
- `put`
- `delete`
- `head`
- `patch`
</ArgTableRow>
<ArgTableRow arg="action.http-body" typ="string" unset="1">傳送到 webhook 的 HTTP 請求正文。支援與日誌訊息相同的佔位符，並按裝置替換（例如 `[device]` 和 `[version]`）。不會自動新增 `Content-Type` 頭；當接收方需要時，可使用 `action.http-headers` 新增，例如為 JSON 正文新增 `Content-Type: application/json`。</ArgTableRow>
<ArgTableRow arg="action.http-headers" typ="multi { header: string
 }" unset="1">隨 webhook 傳送的額外 HTTP 頭，每個格式為 `Header: value`。請求還會攜帶控制器的 `RouterOS <version>` 使用者代理。</ArgTableRow>
<ArgTableRow arg="reset-on-disconnect" typ="enum (yes | no) { yes:0, no:-1 }" unset="1">當裝置斷開連線時清除（重設）狀態警報，以便重新連線的裝置在仍然匹配時再次觸發規則：`yes` 或 `no`。預設值：`no`（斷開連線期間保留狀態）。事件警報沒有可重設的持久狀態。</ArgTableRow>
<ArgTableRow arg="severity" typ="enum (critical | high | medium | low)" unset="1">
警報的嚴重性：

- `critical`
- `high`
- `medium`（預設）
- `low`
</ArgTableRow>
<ArgTableRow arg="category" typ="multi { array-id, category: enum
 }" unset="1">分配給警報的類別。類別是分組標籤：伺服器根據規則的條件分配一個類別（例如 `performance`、`availability`、`version`、`network` 或 `logging`），並且可以將其更改為任意值。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="devices" typ="num">警報規則匹配的裝置數量（由 `labels` 選中的裝置）。當規則覆蓋所有裝置時，此計數包含控制器本身。</ArgTableRow>
<ArgTableRow arg="devices-on" typ="num">存在活動狀態警報的裝置數量。事件發生次數不會增加此計數。</ArgTableRow>
<ArgTableRow arg="fired" typ="num">警報已觸發的總次數。</ArgTableRow>
<ArgTableRow arg="action-failures" typ="num">警報操作失敗的次數，例如無法訪問 webhook。</ArgTableRow>
</ArgTable>
