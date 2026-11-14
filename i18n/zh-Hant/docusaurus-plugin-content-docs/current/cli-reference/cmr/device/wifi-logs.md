---
sidebar_key: "cli-reference/cmr/device/wifi-logs"
sidebar_position: 7
title: "wifi-logs"
sidebar_label: 'wifi-logs'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/device/wifi-logs
captured_at: '2026-11-09T11:35:47.715Z'
pagination_next: "cli-reference/cmr/layout"
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/device/wifi-logs {#cmrdevicewifi-logs}
**軟體包：** cmr
**型別：** 命令

用於所選裝置的 WiFi 日誌監視器。按 `c` 切換到用戶端檢視，按 `l` 返回日誌條目。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="labels" typ="object" unset="1">使用標籤選擇要監控的裝置。支援 + 和 - 符號分別作為 AND 和 AND NOT 運算子；如果未提供符號，則使用 OR 運算子。</ArgTableRow>
<ArgTableRow arg="address" typ="macAddr" unset="1">按用戶端 MAC 地址過濾。</ArgTableRow>
<ArgTableRow arg="bssid" typ="macAddr" unset="1">按 BSSID 過濾。</ArgTableRow>
<ArgTableRow arg="time" typ="time" unset="1">按時間過濾。</ArgTableRow>
<ArgTableRow arg="time-start" typ="date" unset="1">過濾此時間之後的日誌。</ArgTableRow>
<ArgTableRow arg="time-end" typ="date" unset="1">過濾截至此時間的日誌。</ArgTableRow>
<ArgTableRow arg="event" typ="enum (connected | disconnected | failed)" unset="1">按事件過濾：`connected`、`disconnected` 或 `failed`。</ArgTableRow>
</ArgTable>
