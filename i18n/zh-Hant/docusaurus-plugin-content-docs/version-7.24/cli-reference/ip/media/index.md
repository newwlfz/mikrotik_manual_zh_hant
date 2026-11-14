---
sidebar_key: "cli-reference/ip/media/index"
sidebar_position: 1
title: "media"
sidebar_label: "media"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ip/media
captured_at: '2026-11-01T21:28:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/media {#ipmedia}
**條件：** !smips
**型別：**目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="path" typ="file"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="friendly-name" typ="string"></ArgTableRow>
<ArgTableRow arg="allowed-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="allowed-hostname" typ="string">僅允許此主機名（如 DHCP 伺服器所知）的 IP 地址訪問內容</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>
