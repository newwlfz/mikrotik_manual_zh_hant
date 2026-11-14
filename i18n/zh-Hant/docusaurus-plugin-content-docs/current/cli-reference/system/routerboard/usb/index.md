---
sidebar_key: "cli-reference/system/routerboard/usb"
title: "usb"
sidebar_label: 'usb'
source: https://manual.mikrotik.com/docs/cli-reference/system/routerboard/usb
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/routerboard/usb {#systemrouterboardusb}
**條件：** !i386, !i386, !powerpc
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="type" typ="enum (USB-type-A | mini-PCIe | auto)"></ArgTableRow>
<ArgTableRow arg="usb-mode" typ="enum (automatic | force-host) { automatic:0, force-host:1 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="auto-type" typ="enum (USB-type-A | mini-PCIe)"></ArgTableRow>
<ArgTableRow arg="bootstrap" typ="enum (host-mode | device-mode) { host-mode:0, device-mode:1 }"></ArgTableRow>
</ArgTable>
