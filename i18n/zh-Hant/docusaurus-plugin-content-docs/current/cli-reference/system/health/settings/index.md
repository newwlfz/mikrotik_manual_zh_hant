---
sidebar_key: "cli-reference/system/health/settings"
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/cli-reference/system/health/settings
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/health/settings {#systemhealthsettings}
**條件：** !i386
**系統能力：** health and health-settings
**型別：** 設定目錄

配置裝置的風扇和溫度監控行為。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="fan-full-speed-temp" typ="num">設定風扇轉速提升至最大可能 RPM 時的溫度值。風扇控制器從 CPU、PHY、switch 和 SFP 讀取溫度，並根據溫度最高的元件調整風扇轉速。範圍：-273..65。預設值：65。</ArgTableRow>
<ArgTableRow arg="fan-target-temp" typ="num">設定最熱元件的目標溫度。風扇控制器會調整風扇行為，使溫度保持在目標範圍內。範圍：-273..65。預設值：58。</ArgTableRow>
<ArgTableRow arg="fan-min-speed-percent" typ="num">設定風扇轉速的最低百分比，使風扇轉速不會低於此值。預設值因風扇控制器晶片而異；當前裝置的預設值為 12。範圍：0..100。</ArgTableRow>
<ArgTableRow arg="fan-control-interval" typ="time">設定從 CPU、PHY、switch 和 SFP 讀取溫度資料的間隔。此設定直接影響 CPU 使用率。範圍：5..30 秒。預設值：30s。</ArgTableRow>
<ArgTableRow arg="fan-mode" typ="enum (manual | auto) { manual:0, auto:1 }">選擇風扇控制模式。使用 `auto` 時，當主風扇發生故障，裝置會自動切換到輔助風扇。使用 `manual` 時，可透過 `use-fan` 和 `use-fan2` 選擇執行哪些風扇。</ArgTableRow>
<ArgTableRow arg="use-fan" typ="enum (auxiliary | main) { auxiliary:0, main:1 }">在手動風扇控制模式下選擇要使用的風扇。</ArgTableRow>
<ArgTableRow arg="use-fan2" typ="enum (auxiliary | main) { auxiliary:0, main:1 }">在手動風扇控制模式下選擇要使用的第二個風扇。</ArgTableRow>
<ArgTableRow arg="fan-switch" typ="enum (auto | on | off) { auto:0, on:1, off:2 }">設定風扇狀態：`auto` 遵循自動溫度控制，`on` 強制風扇執行，`off` 強制風扇停止。</ArgTableRow>
<ArgTableRow arg="fan-on-threshold" typ="num">設定風扇啟動的溫度。</ArgTableRow>
<ArgTableRow arg="cpu-overtemp-check" typ="bool">啟用或停用 CPU 過溫監測。適用於 ARM 和 ARM64 裝置。預設值：no。</ArgTableRow>
<ArgTableRow arg="cpu-overtemp-threshold" typ="num">設定觸發過溫保護前的最高溫度。範圍：0..105。預設值：105。</ArgTableRow>
<ArgTableRow arg="cpu-overtemp-startup-delay" typ="time">設定啟動後啟用過溫監測前的延遲。預設值：1m。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="active-fan" typ="enum (auxiliary | main | none) { auxiliary:0, main:1, none:2 }">當前正在使用的風扇。</ArgTableRow>
<ArgTableRow arg="active-fan2" typ="enum (auxiliary | main | none) { auxiliary:0, main:1, none:2 }">當前正在使用的第二個風扇。</ArgTableRow>
</ArgTable>
