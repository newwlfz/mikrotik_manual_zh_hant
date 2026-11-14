---
sidebar_key: "cli-reference/interface/ethernet/poe/settings"
sidebar_position: 3
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ethernet/poe/settings
captured_at: '2026-11-01T21:22:30+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/poe/settings {#interfaceethernetpoesettings}
**系統能力：** (poe or poe-in) and poesettings
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ether1-poe-in-long-cable" typ="bool" syscap="poeattiny"></ArgTableRow>
<ArgTableRow arg="psu-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="psu1-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="psu2-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack1-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack2-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin1-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin2-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="poe-in-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="version" typ="string" syscap="poeattiny"></ArgTableRow>
<ArgTableRow arg="routerboard-max-self-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="routerboard-max-total-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="poe-out-limit-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="psu-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="psu1-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="psu2-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack1-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack2-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin1-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin2-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="poe-in-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
</ArgTable>
