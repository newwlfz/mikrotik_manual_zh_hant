---
title: "settings"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/lte/settings
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## interface/lte/settings 
**條件：** !smips
**類型：** 設定目錄

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mode" typ="enum (auto | serial | mbim | user)"></ArgTableRow>
<ArgTableRow arg="esim-channel" typ="enum (auto | at)"></ArgTableRow>
<ArgTableRow arg="firmware-path" typ="string"></ArgTableRow>
<ArgTableRow arg="log-dir" typ="string" syscap="modemlog"></ArgTableRow>
<ArgTableRow arg="info-polling-interval" typ="num" syscap="tr069-client">info polling interval in seconds</ArgTableRow>
<ArgTableRow arg="link-recovery-timer" typ="num">in seconds</ArgTableRow>
<ArgTableRow arg="sim-slot" typ="enum" syscap="sim-slot"></ArgTableRow>
<ArgTableRow arg="sim-link" typ="enum" syscap="sim-link"></ArgTableRow>
<ArgTableRow arg="external-antenna" typ="enum (auto | main | div | both | none)" syscap="modem-antenna-switch"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="external-antenna-selected" typ="enum (main | div | both | none | none)" syscap="modem-antenna-switch"></ArgTableRow>
</ArgTable>
