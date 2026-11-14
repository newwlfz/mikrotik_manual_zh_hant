---
sidebar_key: "cli-reference/interface/lte/settings"
sidebar_position: 9
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/lte/settings
captured_at: '2026-11-01T21:22:51+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/lte/settings {#interfaceltesettings}
**條件：** !smips
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="mode" typ="enum (auto | serial | mbim | user)"></ArgTableRow>
<ArgTableRow arg="esim-channel" typ="enum (auto | at)"></ArgTableRow>
<ArgTableRow arg="firmware-path" typ="string"></ArgTableRow>
<ArgTableRow arg="log-dir" typ="file" syscap="modemlog"></ArgTableRow>
<ArgTableRow arg="log-file-count" typ="num" syscap="modemlog">儲存在 log-dir 中的輪轉調變解調器日誌檔案數量</ArgTableRow>
<ArgTableRow arg="log-filter-file" typ="file" syscap="modemlog">用於調變解調器日誌捕獲的過濾檔案</ArgTableRow>
<ArgTableRow arg="info-polling-interval" typ="num" syscap="tr069-client">資訊輪詢間隔，單位為秒</ArgTableRow>
<ArgTableRow arg="link-recovery-timer" typ="num">單位為秒</ArgTableRow>
<ArgTableRow arg="sim-slot" typ="enum" syscap="sim-slot"></ArgTableRow>
<ArgTableRow arg="sim-link" typ="enum" syscap="sim-link"></ArgTableRow>
<ArgTableRow arg="external-antenna" typ="enum (auto | main | div | both | none)" syscap="modem-antenna-switch"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="external-antenna-selected" typ="enum (main | div | both | none | none)" syscap="modem-antenna-switch"></ArgTableRow>
</ArgTable>
