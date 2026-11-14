---
sidebar_key: "cli-reference/interface/wifi/dashboard/show-logs"
sidebar_position: 3
title: "show-logs"
sidebar_label: 'show-logs'
source: https://manual.mikrotik.com/docs/cli-reference/interface/wifi/dashboard/show-logs
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wifi/dashboard/show-logs {#interfacewifidashboardshow-logs}
**型別：** Command

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="multi { array-id, interface: iface_enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="bssid" typ="macAddr" unset="1"></ArgTableRow>
<ArgTableRow arg="time" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="time-start" typ="date" unset="1"></ArgTableRow>
<ArgTableRow arg="time-end" typ="date" unset="1"></ArgTableRow>
<ArgTableRow arg="event" typ="enum (connected | disconnected | failed)" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="event" typ="enum (connected | disconnected | failed)"></ArgTableRow>
<ArgTableRow arg="bssid" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="signal" typ="num"></ArgTableRow>
<ArgTableRow arg="auth-type" typ="enum (wpa2-eap | wpa2-psk | ft-eap | ft-wpa2-psk | wpa3-eap | wpa2-psk-sha2 | wpa3-psk | wpa3-psk-gd | ft-wpa3-psk | ft-wpa3-psk-gd | wpa3-eap-192 | ft-wpa3-eap-192 | owe | wpa-eap | wpa-psk | dpp)"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="reason" typ="string"></ArgTableRow>
</ArgTable>
