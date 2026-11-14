---
sidebar_key: "cli-reference/cmr/device/run-script"
sidebar_position: 5
title: "run-script"
sidebar_label: 'run-script'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/device/run-script
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/device/run-script {#cmrdevicerun-script}
**包：** cmr
**型別：** 命令

在選定的裝置上執行指令碼。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="script" typ="alt { script: string
 }">要在選定裝置上執行的指令碼。</ArgTableRow>
<ArgTableRow arg="labels" typ="object" unset="1">使用標籤選擇要執行指令碼的裝置。支援 + 和 - 符號分別作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。</ArgTableRow>
<ArgTableRow arg="order" typ="object">執行順序（按標籤）。</ArgTableRow>
<ArgTableRow arg="strategy" typ="enum ()" unset="1">裝置的處理方式：`parallel` 或 `sequential`。</ArgTableRow>
<ArgTableRow arg="fail-policy" typ="enum ()" unset="1">裝置失敗時的行為：`continue`、`stop` 或 `continue-order`。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time" unset="1">指令碼執行超時時間。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum">正在執行指令碼的裝置。</ArgTableRow>
<ArgTableRow arg="status" typ="string">執行狀態。</ArgTableRow>
<ArgTableRow arg="output" typ="string">指令碼輸出。</ArgTableRow>
</ArgTable>
