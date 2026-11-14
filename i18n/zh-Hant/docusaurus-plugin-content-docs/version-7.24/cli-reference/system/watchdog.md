---
sidebar_key: "cli-reference/system/watchdog"
sidebar_position: 36
title: "watchdog"
sidebar_label: "watchdog"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/watchdog
captured_at: '2026-11-01T21:30:12+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/watchdog {#systemwatchdog}
**型別:** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="watch-address" typ="alt { ip: ipAddr
, ipv6: composite { address: ip6Addr
, interface: [ iface_enum]
 }
 }"></ArgTableRow>
<ArgTableRow arg="watchdog-timer" typ="bool"></ArgTableRow>
<ArgTableRow arg="ping-start-after-boot" typ="time"></ArgTableRow>
<ArgTableRow arg="ping-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="automatic-supout" typ="bool"></ArgTableRow>
<ArgTableRow arg="auto-send-supout" typ="bool"></ArgTableRow>
<ArgTableRow arg="send-email-to" typ="string"></ArgTableRow>
<ArgTableRow arg="send-email-from" typ="string"></ArgTableRow>
<ArgTableRow arg="send-smtp-server" typ="alt { ipv4: ipAddr
, fqdn: string
 }"></ArgTableRow>
</ArgTable>
