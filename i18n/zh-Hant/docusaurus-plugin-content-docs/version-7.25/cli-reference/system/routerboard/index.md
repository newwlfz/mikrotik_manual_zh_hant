---
sidebar_key: "cli-reference/system/routerboard/index"
sidebar_position: 1
title: "routerboard"
sidebar_label: 'routerboard'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/routerboard
captured_at: '2026-11-01T21:25:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/routerboard {#systemrouterboard}
**條件：** !i386
**型別：** 設定目錄

此選單允許您檢視 RouterBOARD 裝置的基本硬體和韌體資訊。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="routerboard" typ="bool">指示裝置是否為 RouterBOARD 單元。</ArgTableRow>
<ArgTableRow arg="board-name" typ="string"></ArgTableRow>
<ArgTableRow arg="model" typ="string">RouterBOARD 型號編號。</ArgTableRow>
<ArgTableRow arg="revision" typ="string"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string">裝置的唯一序列號。</ArgTableRow>
<ArgTableRow arg="firmware-type" typ="string">裝置使用的引導載入程式韌體型別。</ArgTableRow>
<ArgTableRow arg="minimum-firmware" typ="string">出廠時安裝的韌體版本。</ArgTableRow>
<ArgTableRow arg="current-firmware" typ="string">當前使用的 RouterBOOT 載入程式版本。不要將其與 RouterOS 作業系統版本混淆。</ArgTableRow>
<ArgTableRow arg="upgrade-firmware" typ="string">RouterOS 升級可能包含新的 RouterBOOT 版本檔案，但必須手動應用。此行指示裝置上是否已找到新的 RouterBOOT 檔案。該檔案可能包含在最近的 RouterOS 升級中，或作為 FWF 檔案手動上傳。無論哪種情況，此處都會顯示可用的最新版本。</ArgTableRow>
</ArgTable>
