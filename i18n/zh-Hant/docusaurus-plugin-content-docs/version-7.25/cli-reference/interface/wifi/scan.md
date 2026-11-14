---
sidebar_key: "cli-reference/interface/wifi/scan"
sidebar_position: 20
title: "scan"
sidebar_label: 'scan'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/wifi/scan
captured_at: '2026-11-01T21:23:15+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wifi/scan {#interfacewifiscan}
**型別：** 命令

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="A" typ="active">已啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="rounds" typ="num"></ArgTableRow>
<ArgTableRow arg="save-file" typ="string"></ArgTableRow>
<ArgTableRow arg="frequency" typ="object" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="security" typ="multi { array-id, auth-type: enum (wpa2-eap | wpa2-psk | ft-eap | ft-wpa2-psk | wpa3-eap | wpa2-psk-sha2 | wpa3-psk | wpa3-psk-gd | ft-wpa3-psk | ft-wpa3-psk-gd | wpa3-eap-192 | ft-wpa3-eap-192 | owe | wpa-eap | wpa-psk | dpp)
 }"></ArgTableRow>
<ArgTableRow arg="signal" typ="num"></ArgTableRow>
<ArgTableRow arg="nf" typ="num"></ArgTableRow>
<ArgTableRow arg="sta-count" typ="num"></ArgTableRow>
</ArgTable>
