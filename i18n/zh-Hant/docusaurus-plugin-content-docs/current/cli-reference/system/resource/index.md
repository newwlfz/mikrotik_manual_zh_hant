---
sidebar_key: "cli-reference/system/resource"
title: "resource"
sidebar_label: 'resource'
source: https://manual.mikrotik.com/docs/cli-reference/system/resource
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/resource {#systemresource}
**型別：** 設定目錄
路由器的整體資源使用情況和身份資訊：uptime、記憶體、磁碟、版本、主機板。請參閱[資源](../../../diagnostics-monitoring-and-troubleshooting/resource.md)指南。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="uptime" typ="time">自啟動以來經過的時間</ArgTableRow>
<ArgTableRow arg="version" typ="string">已安裝的 RouterOS 版本號</ArgTableRow>
<ArgTableRow arg="build-time" typ="string">已安裝的 RouterOS 版本構建時間</ArgTableRow>
<ArgTableRow arg="minimum-version" typ="string">該板卡允許降級到的最低 RouterOS 版本（原為 factory-software）</ArgTableRow>
<ArgTableRow arg="free-memory" typ="num">未使用的 RAM 容量</ArgTableRow>
<ArgTableRow arg="total-memory" typ="num">已安裝的 RAM 容量</ArgTableRow>
<ArgTableRow arg="cpu" typ="string">板卡上的 CPU 型號</ArgTableRow>
<ArgTableRow arg="cpu-count" typ="num">系統上存在的 CPU 數量；每個核心都是一個獨立的 CPU，Intel HT 也計為一個 CPU</ArgTableRow>
<ArgTableRow arg="cpu-frequency" typ="num">當前 CPU 頻率</ArgTableRow>
<ArgTableRow arg="cpu-load" typ="num">已使用 CPU 資源的百分比，為所有 CPU 的合計值；每核心的值位於 [`/system/resource/cpu`](./cpu.md)</ArgTableRow>
<ArgTableRow arg="free-hdd-space" typ="num">硬碟或 NAND 上的可用空間</ArgTableRow>
<ArgTableRow arg="total-hdd-space" typ="num">硬碟或 NAND 的容量</ArgTableRow>
<ArgTableRow arg="write-sect-since-reboot" typ="num">自路由器上次重啟以來對驅動器/NAND 的扇區寫入次數</ArgTableRow>
<ArgTableRow arg="write-sect-total" typ="num">扇區寫入總次數</ArgTableRow>
<ArgTableRow arg="bad-blocks" typ="num">NAND 上壞塊的百分比</ArgTableRow>
<ArgTableRow arg="architecture-name" typ="string">此版本的 CPU 架構（arm、arm64、x86、tile ...）</ArgTableRow>
<ArgTableRow arg="board-name" typ="string">RouterBOARD 型號名稱</ArgTableRow>
<ArgTableRow arg="platform" typ="string">平臺名稱</ArgTableRow>
</ArgTable>
