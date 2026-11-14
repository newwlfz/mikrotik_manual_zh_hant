---
sidebar_key: "cli-reference/system/resource/hardware/usb-power-reset"
sidebar_position: 5
title: "usb-power-reset"
sidebar_label: 'usb-power-reset'
source: https://manual.mikrotik.com/docs/cli-reference/system/resource/hardware/usb-power-reset
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/resource/hardware/usb-power-reset {#systemresourcehardwareusb-power-reset}
**條件：** !powerpc、!smips、i386
**型別：** 命令
對 USB 埠進行電源重啟：先斷電 `duration` 時間，再重新上電（無需重啟路由器即可重設出現異常的調變解調器和驅動器）。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="duration" typ="time">重新啟用 USB 前的斷電持續時間</ArgTableRow>
<ArgTableRow arg="bus" typ="num">USB 匯流排編號（由 `/system/resource/hardware` 顯示）</ArgTableRow>
<ArgTableRow arg="slot" typ="num">總線上的 USB 插槽編號</ArgTableRow>
</ArgTable>
