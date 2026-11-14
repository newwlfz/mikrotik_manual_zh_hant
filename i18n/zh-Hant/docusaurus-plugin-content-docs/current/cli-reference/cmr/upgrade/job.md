---
sidebar_key: "cli-reference/cmr/upgrade/job"
title: "job"
source: https://manual.mikrotik.com/docs/cli-reference/cmr/upgrade/job
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/upgrade/job {#cmrupgradejob}
**軟體包：** cmr
**型別：** 目錄

一個升級作業就是一次升級執行。作業由升級規則建立，其引數在建立時從規則複製，並且是隻讀的。計劃作業僅在啟動時才解析其裝置列表，因此對於計劃作業，`show-devices` 可能為空。移除排隊中或處理中的作業即可取消它。作業狀態會變為 `cancelled`。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">任務已停用。</ArgTableRow>
<ArgTableRow arg="R" typ="rule">由升級規則建立的任務。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="labels" typ="object" unset="1">任務涵蓋的裝置，按標籤選擇。對於由 `/cmr/device/upgrade` 為按編號選擇的裝置啟動的任務，此欄位為空。</ArgTableRow>
<ArgTableRow arg="order" typ="object">標籤組的執行順序，與 `continue-order` 配合使用。</ArgTableRow>
<ArgTableRow arg="channel" typ="alt">任務安裝的升級通道或固定版本。當每臺裝置按各自的升級通道升級時為空。</ArgTableRow>
<ArgTableRow arg="strategy" typ="enum ()" unset="1">任務升級裝置的方式：`parallel` 同時全部升級，`sequential` 依次逐個升級。使用 `continue-order` 時，裝置按 `order` 給定的順序逐標籤組處理。</ArgTableRow>
<ArgTableRow arg="fail-policy" typ="enum ()" unset="1">裝置失敗時任務的行為：`continue`、`stop` 或 `continue-order`。`stop` 在首次失敗時停止整個任務；`continue-order` 繼續處理 `order` 中的下一個標籤組。</ArgTableRow>
<ArgTableRow arg="schedule-time" typ="date" unset="1">任務計劃執行的時間，格式與規則的 `schedule-time` 相同。</ArgTableRow>
<ArgTableRow arg="starts-in" typ="time" unset="1">作業開始前的剩餘時間。僅對已排程的作業顯示。</ArgTableRow>
<ArgTableRow arg="start-time" typ="date" unset="1">作業開始執行的時間。</ArgTableRow>
<ArgTableRow arg="end-time" typ="date" unset="1">作業完成的時間。</ArgTableRow>
<ArgTableRow arg="state" typ="enum (scheduled | queued | waiting devices | queued (busy) | version check | processing | done | cancelled)">當前作業狀態：`scheduled`（等待執行）、`queued`（在另一個作業執行時建立，待其完成後開始）、`waiting devices`、`version check`（查詢可用版本）、`processing`（正在升級）、`done`（已完成）或 `cancelled`（已移除）。</ArgTableRow>
<ArgTableRow arg="success" typ="composite { success: num
, total: num
 }" unset="1">已升級/總數，例如 `3/10`。當裝置已處於目標版本，或作業開始時某臺被覆蓋的裝置不可達，會出現 `0/total`。</ArgTableRow>
<ArgTableRow arg="run-time" typ="time" unset="1">作業執行所花費的時間。</ArgTableRow>
<ArgTableRow arg="packages" typ="multi { package: string
 }" unset="1">作業升級的軟體包。</ArgTableRow>
</ArgTable>
