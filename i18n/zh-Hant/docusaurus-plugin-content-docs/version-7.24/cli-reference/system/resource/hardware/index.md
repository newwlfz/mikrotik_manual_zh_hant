---
sidebar_key: "cli-reference/system/resource/hardware/index"
sidebar_position: 2
title: "hardware"
sidebar_label: "hardware"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/resource/hardware
captured_at: '2026-11-01T21:30:02+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/resource/hardware {#systemresourcehardware}
**條件：** !powerpc, !smips
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="location" typ="string"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (usb | pci | scsi | serial)"></ArgTableRow>
<ArgTableRow arg="vendor" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="category" typ="string"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="vendor-id" typ="string"></ArgTableRow>
<ArgTableRow arg="device-id" typ="string"></ArgTableRow>
<ArgTableRow arg="speed" typ="string"></ArgTableRow>
<ArgTableRow arg="ports" typ="num"></ArgTableRow>
<ArgTableRow arg="usb-version" typ="string"></ArgTableRow>
<ArgTableRow arg="manufacturer-reported-max-power" typ="string"></ArgTableRow>
<ArgTableRow arg="irq" typ="num"></ArgTableRow>
<ArgTableRow arg="memory" typ="multi { range: composite { min: num
, max: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="io" typ="multi { range: composite { min: num
, max: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
<ArgTableRow arg="device-path" typ="multi { path: string
 }"></ArgTableRow>
</ArgTable>
