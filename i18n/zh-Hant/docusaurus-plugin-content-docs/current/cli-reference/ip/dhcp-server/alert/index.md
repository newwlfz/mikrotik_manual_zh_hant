---
sidebar_key: "cli-reference/ip/dhcp-server/alert"
title: "alert"
sidebar_label: 'alert'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/alert
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/alert {#ipdhcp-serveralert}
**型別：** 目錄

檢測介面上的未知（非法）DHCP 伺服器。該警報大約每分鐘自行傳送一次 DHCPDISCOVER，並將它看到的每個 DHCP 回覆的來源與 `valid-server` 進行核對。未知伺服器會使用 `dhcp,critical` 主題記錄日誌，列在 `unknown-server` 中，並觸發 `on-alert`。由於該警報自身會發送 DHCP 請求，請勿在路由器執行 DHCP 用戶端的介面上使用它。詳情請參見 [DHCP 伺服器](../../../../network-management/dhcp/server.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該警報已停用。新建的警報在建立時處於停用狀態。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">警報配置無效。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">用於監視 DHCP 伺服器的介面。</ArgTableRow>
<ArgTableRow arg="valid-server" typ="multi { mac-address: macAddr
 }">該介面上允許的 DHCP 伺服器的 MAC 地址。來自其他伺服器的回覆會觸發警報。</ArgTableRow>
<ArgTableRow arg="on-alert" typ="alt { script: string
 }">檢測到未知 DHCP 伺服器時要執行的指令碼。</ArgTableRow>
<ArgTableRow arg="alert-timeout" typ="alt { symbolic-names: enum (none) { none:0 }
, time-interval: time
 }">檢測到的伺服器被遺忘之前經過的時間。如果之後該伺服器仍然存在，則會觸發新警報。使用 `none` 時，檢測到的伺服器永遠不會被遺忘。預設值：1h。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="unknown-server" typ="multi { mac-address: macAddr
 }">檢測到的未知 DHCP 伺服器的 MAC 地址。</ArgTableRow>
</ArgTable>
