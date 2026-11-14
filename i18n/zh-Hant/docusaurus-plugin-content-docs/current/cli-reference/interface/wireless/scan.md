---
sidebar_key: "cli-reference/interface/wireless/scan"
sidebar_position: 16
title: "scan"
sidebar_label: 'scan'
source: https://manual.mikrotik.com/docs/cli-reference/interface/wireless/scan
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireless/scan {#interfacewirelessscan}
**軟體包:** wireless-rep
**型別:** 命令

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
<ArgTableRow arg="background" typ="bool"></ArgTableRow>
<ArgTableRow arg="save-file" typ="string"></ArgTableRow>
<ArgTableRow arg="rounds" typ="num"></ArgTableRow>
<ArgTableRow arg="passive" typ="bool"></ArgTableRow>
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
