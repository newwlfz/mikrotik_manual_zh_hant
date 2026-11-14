---
sidebar_key: "cli-reference/interface/lte/index"
sidebar_position: 6
title: "lte"
sidebar_label: "lte"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/lte
captured_at: '2026-11-01T21:27:23+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/lte {#interfacelte}
**條件：** !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="pin" typ="string"></ArgTableRow>
<ArgTableRow arg="apn-profiles" typ="multi { array-id, apn: enum
 }"></ArgTableRow>
<ArgTableRow arg="modem-init" typ="string">調變解調器初始化時要傳送的字串</ArgTableRow>
<ArgTableRow arg="operator" typ="string">運營商鎖定，使用數字值：mccmnc</ArgTableRow>
<ArgTableRow arg="allow-roaming" typ="bool"></ArgTableRow>
<ArgTableRow arg="sms-read" typ="bool">如果 /tool/sms 中啟用了任何介面，則忽略此設定</ArgTableRow>
<ArgTableRow arg="sms-protocol" typ="enum (mbim | at | auto)"></ArgTableRow>
<ArgTableRow arg="network-mode" typ="multi { array-id, network: enum
 }"></ArgTableRow>
<ArgTableRow arg="band" typ="multi { array-id, band: enum
 }">LTE 頻段</ArgTableRow>
<ArgTableRow arg="nr-band" typ="multi { array-id, nr-band: enum
 }">NR 頻段</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="master" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="advertised-mtu" typ="num"></ArgTableRow>
</ArgTable>
