---
sidebar_key: "cli-reference/disk/test"
sidebar_position: 16
title: "test"
sidebar_label: 'test'
source: https://manual.mikrotik.com/docs/cli-reference/disk/test
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/test {#disktest}
**條件：** !smips
**型別：** Command

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="N" typ="initializing">測試正在初始化（進行準備、清除快取），尚未開始讀取或寫入。</ArgTableRow>
<ArgTableRow arg="R" typ="running">測試正在執行。</ArgTableRow>
<ArgTableRow arg="F" typ="failed">測試失敗。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="disk" typ="multi { array-id, disk: enum
 }">要測試的磁碟或分割區。</ArgTableRow>
<ArgTableRow arg="block-size" typ="num">單個讀取或寫入塊的大小。預設值：64 KiB。</ArgTableRow>
<ArgTableRow arg="thread-count" typ="num">並行測試執行緒數。預設值：1。</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (read | write)">
測試對資料的處理方式。
- `read`（預設）- 讀取磁碟；不改變其內容。
- `write` - 寫入磁碟；會銷燬磁碟上的所有資料。
</ArgTableRow>
<ArgTableRow arg="type" typ="enum (device | filesystem)">測試目標：`device` 直接讀寫原始塊裝置，`filesystem` 透過已掛載的檔案系統進行。預設值：device。</ArgTableRow>
<ArgTableRow arg="pattern" typ="enum (sequential | random)">
訪問模式。
- `sequential`（預設）- 讀取或寫入連續的塊。
- `random` - 在隨機位置讀取或寫入塊。
</ArgTableRow>
<ArgTableRow arg="entries-to-show" typ="num">保留並顯示多少條最近的結果行。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="seq" typ="enum (TOT) { TOT:0xffffffff }">結果行的序號；`TOT` 行彙總所有執行緒。</ArgTableRow>
<ArgTableRow arg="rate" typ="num">此行的當前吞吐量。</ArgTableRow>
<ArgTableRow arg="iops" typ="num">每秒輸入/輸出運算元。</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">此行到目前為止已傳輸的位元組數。</ArgTableRow>
<ArgTableRow arg="disk" typ="enum (TOT) { TOT:0xffffffff }">被測試的磁碟。</ArgTableRow>
<ArgTableRow arg="thread" typ="enum (TOT) { TOT:0xffffffff }">此行所屬的執行緒；`TOT` 彙總所有執行緒。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (device | filesystem)">啟動測試時指定的測試型別。</ArgTableRow>
<ArgTableRow arg="pattern" typ="enum (sequential | random)">啟動測試時指定的訪問模式。</ArgTableRow>
<ArgTableRow arg="dir" typ="enum (read | write)">啟動測試時指定的方向（`read` 或 `write`）。</ArgTableRow>
<ArgTableRow arg="bsize" typ="num">啟動測試時指定的塊大小。</ArgTableRow>
<ArgTableRow arg="state" typ="string">執行中測試的狀態，例如準備階段為 `clear caches`，工作階段為 `run`。</ArgTableRow>
</ArgTable>
