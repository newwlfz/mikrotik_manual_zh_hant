---
sidebar_key: "cli-reference/system/leds"
title: "leds"
sidebar_label: 'leds'
source: https://manual.mikrotik.com/docs/cli-reference/system/leds
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/leds {#systemleds}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="*" typ="default"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="type" typ="enum (interface-status | interface-receive | interface-transmit | interface-activity | wireless-signal-strength | wireless-status | modem-signal | modem-technology | flash-access | interface-speed | interface-speed-1G | interface-speed-25G | interface-speed-2.5G | interface-speed-100G | poe-out | ap-cap | on | off | fan-fault | poe-fault | gps-valid | align-left | align-right | align-up | align-down)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="leds" typ="object { led: enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="object { iface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="modem-signal-threshold" typ="num">RSSI 閾值</ArgTableRow>
<ArgTableRow arg="color" typ="alt { color-name: enum (none | red | orange | yellow | green-yellow | green | green-cyan | cyan | blue-cyan | blue | blue-magenta | magenta | red-magenta) { none:0, red:0xff0000, orange:0xff7f00, yellow:0xffff00, green-yellow:0x7fff00, green:0x00ff00, green-cyan:0x00ff7f, cyan:0x00ffff, blue-cyan:0x007fff, blue:0x0000ff, blue-magenta:0x7f00ff, magenta:0xff00ff, red-magenta:0xff007f }
, color-number: num [0 .. 0xffffff]
 }"></ArgTableRow>
</ArgTable>
