---
sidebar_key: "cli-reference/caps-man/interface/scan"
sidebar_position: 4
title: "scan"
sidebar_label: 'scan'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/caps-man/interface/scan
captured_at: '2026-11-01T21:21:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## caps-man/interface/scan {#caps-maninterfacescan}
**包：** wireless-rep
**型別：** 命令

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="A" typ="active"></ArgTableRow>
<ArgTableRow arg="P" typ="privacy"></ArgTableRow>
<ArgTableRow arg="R" typ="routeros-network"></ArgTableRow>
<ArgTableRow arg="N" typ="nstreme"></ArgTableRow>
<ArgTableRow arg="T" typ="tdma"></ArgTableRow>
<ArgTableRow arg="W" typ="wds"></ArgTableRow>
<ArgTableRow arg="B" typ="bridge"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="save-file" typ="string"></ArgTableRow>
<ArgTableRow arg="rounds" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ssid" typ="string"></ArgTableRow>
<ArgTableRow arg="channel" typ="string"></ArgTableRow>
<ArgTableRow arg="sig" typ="num"></ArgTableRow>
<ArgTableRow arg="nf" typ="num"></ArgTableRow>
<ArgTableRow arg="snr" typ="num"></ArgTableRow>
<ArgTableRow arg="radio-name" typ="string"></ArgTableRow>
<ArgTableRow arg="routeros-version" typ="string"></ArgTableRow>
</ArgTable>
