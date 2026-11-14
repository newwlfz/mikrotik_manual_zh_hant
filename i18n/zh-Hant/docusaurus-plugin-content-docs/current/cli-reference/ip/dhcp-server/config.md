---
sidebar_key: "cli-reference/ip/dhcp-server/config"
sidebar_position: 2
title: "config"
sidebar_label: 'config'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/config
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/config {#ipdhcp-serverconfig}
**型別：** 設定目錄

所有 DHCP 伺服器共享的設定：租約儲存的頻率以及 RADIUS 計費。有關詳細資訊，請參閱 [DHCP 伺服器](../../../network-management/dhcp/server.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="store-leases-disk" typ="alt { symbolic-names: enum (immediately | never) { immediately:0, never:0xffffffff }
, time-interval: time
 }">租約儲存到磁碟的頻率：時間間隔、`immediately` 或 `never`。降低儲存頻率可減少對快閃記憶體的寫入。預設值：5m。</ArgTableRow>
<ArgTableRow arg="accounting" typ="bool">是否為使用 RADIUS（`use-radius`）的伺服器的租約傳送 RADIUS 計費。預設值：yes。</ArgTableRow>
<ArgTableRow arg="interim-update" typ="time">RADIUS 臨時計費更新間隔。預設值：0s。</ArgTableRow>
<ArgTableRow arg="radius-password" typ="alt { user: enum (empty | same-as-user)
, password: string
 }">在 RADIUS Access-Request 訊息中傳送的密碼：`empty`、`same-as-user`（使用者名稱，即用戶端的 MAC 地址）或固定密碼。預設值：empty。</ArgTableRow>
</ArgTable>
