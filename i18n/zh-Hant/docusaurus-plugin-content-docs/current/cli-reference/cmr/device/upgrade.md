---
sidebar_key: "cli-reference/cmr/device/upgrade"
sidebar_position: 6
title: "upgrade"
sidebar_label: 'upgrade'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/device/upgrade
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/device/upgrade {#cmrdeviceupgrade}
**軟體包：** cmr
**型別：** Command

為所選裝置啟動升級（任務）。升級在 [`/cmr/upgrade/job`](../upgrade/job.md) 中作為任務執行，具有相同的任務狀態和結果計數器。在控制檯上，該命令會顯示任務的裝置及其狀態，直到您按下 <kbd>Control</kbd>+<kbd>C</kbd> 或 `duration` 中給定的時間結束；任務將在伺服器上繼續執行。使用 `order` 時，標籤組會依次升級；請將其他裝置所連線的裝置（例如交換器和閘道器）列在最後。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="L" typ="controller">包含 CMR 伺服器本身（自用戶端）。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="labels" typ="object" unset="1">使用 labels 選擇要升級的裝置。支援 + 和 - 符號分別作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。</ArgTableRow>
<ArgTableRow arg="order" typ="object" unset="1">執行順序（按 labels）。</ArgTableRow>
<ArgTableRow arg="channel" typ="alt" unset="1">升級通道（`long-term`、`stable`、`testing` 或 `development`）或固定版本，例如 `channel=7.24.4`。當未設定時，每臺裝置按其自身的升級通道升級，即 `/cmr/device` 中顯示的 `channel` 值。</ArgTableRow>
<ArgTableRow arg="schedule-time" typ="super { time: date
, [day] [ @enum (sun | mon | tue | wed | thu | fri | sat) { sun:1, mon:2, tue:3, wed:4, thu:5, fri:6, sat:7 }]
 }" unset="1">升級開始的時間：一個時間，可在 `@` 之後附加可選的工作日，例如 `14:00:00` 或 `00:00:00@sat`。任務會以 `scheduled` 狀態等待，直到該時間的下一次到來。</ArgTableRow>
<ArgTableRow arg="strategy" typ="enum (parallel | sequential)" unset="1">裝置的升級方式：`parallel` 同時升級所有涉及的裝置；`sequential` 依次逐臺升級並等待每臺完成。使用 `continue-order` 時，裝置按 `order` 給定的順序逐標籤組處理：在 `parallel` 下每組裝置一起升級，在 `sequential` 下逐臺升級。預設值：`parallel`。</ArgTableRow>
<ArgTableRow arg="fail-policy" typ="enum (continue | stop | continue-order)" unset="1">裝置失敗時的行為：`continue` 跳過失敗的裝置並繼續處理其餘裝置；`stop` 在首次失敗時停止整個升級，不再繼續處理剩餘裝置或下一個標籤組；`continue-order` 跳過失敗的裝置並繼續處理下一個標籤組，按 `order` 給定的順序逐組處理各標籤。在 `sequential` 下，失敗裝置所在標籤組的其餘裝置會被跳過；在 `parallel` 下，只放棄失敗的裝置，組內已在進行中的裝置會繼續完成。預設值：`stop`。</ArgTableRow>
<ArgTableRow arg="packages" typ="multi { package: string
 }" unset="1">要升級的軟體包。</ArgTableRow>
</ArgTable>
