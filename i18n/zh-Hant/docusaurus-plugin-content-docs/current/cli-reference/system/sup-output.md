---
sidebar_key: "cli-reference/system/sup-output"
sidebar_position: 33
title: "sup-output"
sidebar_label: 'sup-output'
source: https://manual.mikrotik.com/docs/cli-reference/system/sup-output
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/sup-output {#systemsup-output}
**型別：** 命令

建立支援輸出檔案（`supout.rif`），這是供 MikroTik 支援使用的路由器診斷快照，並在 `created` 中顯示其進度。該檔案經過編碼，需在您的 MikroTik 賬戶中使用 Supout.rif 檢視器開啟。請參閱 [Supout.rif](../../getting-started/supout-rif.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">檔名，或諸如 `usb1/supout` 的路徑，用於將其寫入資料夾。當名稱沒有副檔名時，RouterOS 會新增 `.rif` 副檔名，因此 `supout.rif` 也會寫入 `supout.rif`。預設值：supout。</ArgTableRow>
<ArgTableRow arg="output-width" typ="num" unset="1">檔案中命令輸出的寬度。當檢視器顯示的輸出被截斷或換行時，請使用更大的值，例如 `300`。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="created" typ="num">檔案進度百分比，從開始直到 `100%`。</ArgTableRow>
</ArgTable>
