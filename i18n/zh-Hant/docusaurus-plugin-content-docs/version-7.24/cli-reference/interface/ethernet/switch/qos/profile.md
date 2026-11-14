---
sidebar_key: "cli-reference/interface/ethernet/switch/qos/profile"
sidebar_position: 5
title: "profile"
sidebar_label: "profile"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/ethernet/switch/qos/profile
captured_at: '2026-11-01T21:27:16+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/qos/profile {#interfaceethernetswitchqosprofile}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">QoS 配置檔名稱</ArgTableRow>
<ArgTableRow arg="pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num"></ArgTableRow>
<ArgTableRow arg="automap" typ="bool">DSCP 和 PCP 值是否應自動對映到該配置檔案？</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>
