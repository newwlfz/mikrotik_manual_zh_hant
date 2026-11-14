---
sidebar_key: "cli-reference/system/routerboard/wps-button"
sidebar_position: 6
title: "wps-button"
sidebar_label: 'wps-button'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/routerboard/wps-button
captured_at: '2026-11-01T21:25:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/routerboard/wps-button {#systemrouterboardwps-button}
**條件：** !i386
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">啟用或停用該按鈕。</ArgTableRow>
<ArgTableRow arg="hold-time" typ="composite { min: time [0 .. 60]
, max: time [0 .. 60]
 }">僅當按鈕被按住的時長處於指定範圍內時，才觸發按鈕動作。</ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { script: string
 }">按下按鈕時要執行的指令碼名稱。您必須在 [Script](../../../developer-guides/scripting/index.md) 選單中建立並命名該指令碼。WPS 按鈕以 `read,write,reboot,ftp,romon,test` 許可權執行。</ArgTableRow>
</ArgTable>
