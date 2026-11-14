---
sidebar_key: "cli-reference/cmr/upgrade"
title: "upgrade"
source: https://manual.mikrotik.com/docs/cli-reference/cmr/upgrade
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/upgrade {#cmrupgrade}
**包：** cmr
**型別：** 目錄

升級規則用於描述何時將選定裝置（按標籤）升級至哪個通道。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">規則已停用。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">規則為動態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" unset="1">升級規則的名稱。</ArgTableRow>
<ArgTableRow arg="labels" typ="object" unset="1">使用標籤選擇該規則涵蓋的裝置。支援使用 + 和 - 符號分別作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。如果省略，則該規則涵蓋所有已連線裝置。預設值：`all`。</ArgTableRow>
<ArgTableRow arg="order" typ="object">執行順序（按標籤）。當 `fail-policy=continue-order` 時必填。</ArgTableRow>
<ArgTableRow arg="channel" typ="alt" mandatory="1">升級通道：`long-term`、`stable`、`testing` 或 `development`。或者，透過直接將版本作為值來固定特定版本，例如 `channel=7.24.4`。</ArgTableRow>
<ArgTableRow arg="schedule-time" typ="multi { array-id, array-id, time: super { time: date
, [day] [ @enum (sun | mon | tue | wed | thu | fri | sat) { sun:1, mon:2, tue:3, wed:4, thu:5, fri:6, sat:7 }]
 }
 }" unset="1">升級開始時間：時間，可選星期幾在 `@` 後給出。例如 `14:00:00` 表示每天 14:00 開始，`00:00:00@sat` 表示每週六午夜開始。多個條目用逗號分隔，例如 `00:00:00@sat,00:00:00@sun`。</ArgTableRow>
<ArgTableRow arg="strategy" typ="enum ()" unset="1">裝置如何升級：`parallel` 會同時升級所有涵蓋的裝置；`sequential` 會逐個升級它們，並等待每個完成。使用 `continue-order` 時，裝置按 `order` 給定的順序按標籤組處理：在 `parallel` 中，每個組的裝置一起升級，在 `sequential` 中一次一個。預設值：`parallel`。</ArgTableRow>
<ArgTableRow arg="fail-policy" typ="enum ()" unset="1">裝置失敗時的行為：`continue` 跳過失敗的裝置並繼續處理其餘裝置；`stop` 在首次失敗時停止整個升級，並且不繼續處理剩餘裝置，也不繼續處理下一個標籤組；`continue-order` 跳過失敗的裝置並繼續處理下一個標籤組，按照 `order` 給定的順序逐個處理標籤組。使用 `sequential` 時，會跳過失敗裝置所在組的其餘部分；使用 `parallel` 時，只會放棄失敗的裝置，組中已在進行的裝置會完成。預設值：`stop`。</ArgTableRow>
</ArgTable>
