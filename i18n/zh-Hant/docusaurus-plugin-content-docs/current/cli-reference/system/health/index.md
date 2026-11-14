---
sidebar_key: "cli-reference/system/health"
title: "health"
sidebar_label: 'health'
source: https://manual.mikrotik.com/docs/cli-reference/system/health
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/health {#systemhealth}
**條件：** i386
**型別：** 設定目錄

基於 x86（i386）的裝置上的硬體健康監控。使用 `/system/health/print` 讀取感測器值。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="state-after-reboot" typ="enum (disabled | enabled)">啟用或停用重啟後的硬體健康監控。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="core" typ="num">CPU 核心電壓。</ArgTableRow>
<ArgTableRow arg="3.3v" typ="num">3.3 V 供電線路電壓。</ArgTableRow>
<ArgTableRow arg="5v" typ="num">5 V 供電線路電壓。</ArgTableRow>
<ArgTableRow arg="12v" typ="num">12 V 供電線路電壓。</ArgTableRow>
<ArgTableRow arg="lm87-temp" typ="num">由 LM87 感測器測得的溫度。</ArgTableRow>
<ArgTableRow arg="cpu-temp" typ="num">CPU 溫度。</ArgTableRow>
<ArgTableRow arg="board-temp" typ="num">主機板溫度。</ArgTableRow>
<ArgTableRow arg="voltage1" typ="num">感測器 1 測得的電壓。</ArgTableRow>
<ArgTableRow arg="voltage2" typ="num">感測器 2 測得的電壓。</ArgTableRow>
<ArgTableRow arg="voltage3" typ="num">感測器 3 測得的電壓。</ArgTableRow>
<ArgTableRow arg="voltage4" typ="num">感測器 4 測得的電壓。</ArgTableRow>
<ArgTableRow arg="voltage5" typ="num">感測器 5 測得的電壓。</ArgTableRow>
<ArgTableRow arg="voltage6" typ="num">感測器 6 測得的電壓。</ArgTableRow>
<ArgTableRow arg="voltage7" typ="num">感測器 7 測得的電壓。</ArgTableRow>
<ArgTableRow arg="voltage8" typ="num">感測器 8 測得的電壓。</ArgTableRow>
<ArgTableRow arg="voltage9" typ="num">感測器 9 測量的電壓。</ArgTableRow>
<ArgTableRow arg="voltage10" typ="num">感測器 10 測量的電壓。</ArgTableRow>
<ArgTableRow arg="temp1" typ="num">感測器 1 測量的溫度。</ArgTableRow>
<ArgTableRow arg="temp2" typ="num">感測器 2 測量的溫度。</ArgTableRow>
<ArgTableRow arg="temp3" typ="num">感測器 3 測量的溫度。</ArgTableRow>
<ArgTableRow arg="fan1" typ="num">風扇 1 的轉速，單位為 RPM。</ArgTableRow>
<ArgTableRow arg="fan2" typ="num">風扇 2 的轉速，單位為 RPM。</ArgTableRow>
<ArgTableRow arg="fan3" typ="num">風扇 3 的轉速，單位為 RPM。</ArgTableRow>
<ArgTableRow arg="state" typ="enum (disabled | enabled)">健康監控狀態。</ArgTableRow>
</ArgTable>

## system/health {#systemhealth-1}
**條件：** !i386
**系統能力：** health
**型別：** 目錄

非 x86 裝置上的硬體健康監控。使用 `/system/health/print` 列出每個受監控引數的名稱、當前值和型別。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">被監控引數的名稱，例如 `voltage`、`cpu-temperature` 或 `fan1-speed`。</ArgTableRow>
<ArgTableRow arg="value" typ="alt { valuet: num
, valuer: num
, valuev: num
, valuea: num
, valuew: num
, valueb: enum (ok | fail | not-present | idle | no-input) { ok:0, fail:1, not-present:2, idle:3, no-input:4 }
, values: string
 }">引數的當前值。該值及其單位取決於引數 `type`。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (C | RPM | V | A | W |  | )">測量值的型別：`C` 為攝氏度，`RPM` 為風扇轉速，`V` 為電壓，`A` 為電流，`W` 為功耗。</ArgTableRow>
</ArgTable>
