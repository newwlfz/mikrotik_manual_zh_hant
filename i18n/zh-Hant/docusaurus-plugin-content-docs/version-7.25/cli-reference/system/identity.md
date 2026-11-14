---
sidebar_key: "cli-reference/system/identity"
sidebar_position: 11
title: "identity"
sidebar_label: 'identity'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/identity
captured_at: '2026-11-01T21:25:29+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/identity {#systemidentity}
**型別：** 設定目錄

路由器的名稱。有關其出現位置和示例，請參閱 [身份](../../system-information-and-utilities/identity.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">路由器名稱，最多 64 個字元；允許使用空格和其他字元，名稱更長時會失敗並顯示 `could not change identity: too long`。它會顯示在 CLI 提示符和 WinBox 中，出現在鄰居發現中，作為 SNMP 的 `sysName`，作為 DHCP 用戶端傳送的主機名，以及作為舊版無線介面的預設 SSID。SNMP 可以使用具有寫許可權的 community 來設定它。預設值：MikroTik。</ArgTableRow>
</ArgTable>
