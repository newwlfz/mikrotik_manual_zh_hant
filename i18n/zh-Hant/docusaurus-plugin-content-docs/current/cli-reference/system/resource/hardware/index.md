---
sidebar_key: "cli-reference/system/resource/hardware"
title: "hardware"
sidebar_label: 'hardware'
source: https://manual.mikrotik.com/docs/cli-reference/system/resource/hardware
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/resource/hardware {#systemresourcehardware}
**條件：** !powerpc、!smips
**型別：** 目錄
檢測到的透過 PCI、USB 或 SCSI 匯流排連線的硬體裝置。在沒有此類匯流排的板卡上為空（例如 hAP ax²）。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="I" typ="inactive">inactive：裝置存在但未啟用</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="device-name" typ="string">裝置韌體報告的名稱（name 列細化）</ArgTableRow>
<ArgTableRow arg="location" typ="string">裝置在系統拓撲中的位置</ArgTableRow>
<ArgTableRow arg="parent" typ="enum">父匯流排或控制器</ArgTableRow>
<ArgTableRow arg="type" typ="enum (usb | pci | scsi | serial)">裝置的匯流排型別：`usb`、`pci`、`scsi` 或 `serial`</ArgTableRow>
<ArgTableRow arg="vendor" typ="string">裝置廠商名稱</ArgTableRow>
<ArgTableRow arg="name" typ="string">裝置名稱或型號</ArgTableRow>
<ArgTableRow arg="category" typ="string">裝置類別</ArgTableRow>
<ArgTableRow arg="serial-number" typ="string">裝置序列號</ArgTableRow>
<ArgTableRow arg="vendor-id" typ="string">供應商識別符號（VID）</ArgTableRow>
<ArgTableRow arg="device-id" typ="string">裝置識別符號（PID / Device ID）</ArgTableRow>
<ArgTableRow arg="speed" typ="string">協商後的裝置速度</ArgTableRow>
<ArgTableRow arg="ports" typ="num">裝置提供的埠數</ArgTableRow>
<ArgTableRow arg="usb-version" typ="string">支援的 USB 版本</ArgTableRow>
<ArgTableRow arg="manufacturer-reported-max-power" typ="string">裝置報告的最大功耗（例如 USB 調變解調器）</ArgTableRow>
<ArgTableRow arg="overcurrent" typ="num" syscap="usb-hub"></ArgTableRow>
<ArgTableRow arg="irq" typ="num">分配的中斷號</ArgTableRow>
<ArgTableRow arg="memory" typ="multi { range: composite { min: num
, max: num
 }
 }">分配給裝置的記憶體視窗</ArgTableRow>
<ArgTableRow arg="io" typ="multi { range: composite { min: num
, max: num
 }
 }">分配給裝置的 I/O 視窗</ArgTableRow>
<ArgTableRow arg="owner" typ="string">擁有該裝置的子系統或驅動程式</ArgTableRow>
<ArgTableRow arg="device-path" typ="multi { path: string
 }">從根匯流排到端點的裝置路徑</ArgTableRow>
</ArgTable>
