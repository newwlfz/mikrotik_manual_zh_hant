---
sidebar_key: "cli-reference/cmr/client"
title: "client"
source: https://manual.mikrotik.com/docs/cli-reference/cmr/client
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/client {#cmrclient}
**條件：** !smips
**型別：** 設定目錄

有關 CMR-client 及其用法的概述，請參閱 [CMR-用戶端](../../management-tools/cmr/client.md) 文件。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="enum (yes | no)">CMR 用戶端是否啟用。預設值：no。</ArgTableRow>
<ArgTableRow arg="peer-id" typ="string" unset="1">CMR 伺服器的唯一 CMR 專用裝置識別符號。</ArgTableRow>
<ArgTableRow arg="local-id" typ="string" unset="1">唯一的 CMR 專用裝置識別符號。</ArgTableRow>
<ArgTableRow arg="pairing-requirement" typ="enum (none | password | confirm)" unset="1">
定義遠端裝置必須執行哪些操作，本裝置才會接受配對：
- **none** - 本裝置自動接受配對，無需額外檢查
- **password**（預設）- 遠端裝置可透過提供此裝置上 RouterOS 使用者的使用者名稱和密碼來批准配對；CMR 沒有單獨的配對密碼
- **confirm** - 必須在此裝置上使用 [`/cmr/client/pair`](/docs/cli-reference/cmr/pair) 在本地批准配對；無法從遠端側批准
</ArgTableRow>
<ArgTableRow arg="controller-addresses" typ="multi { array-id, address: address (flags=46D)
 }" unset="1">指定要使用的控制器 IP 地址。當用戶端可以透過鄰居發現或 DNS（`_cmr._tcp.lan`，或 `_cmr._tcp.` 後跟來自 DHCP 的域名）自動發現控制器時，此設定為可選；但當無法自動確定控制器地址時，必須配置此設定。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">當前 CMR 用戶端狀態。</ArgTableRow>
<ArgTableRow arg="controller-identity" typ="string">CMR 伺服器身份。</ArgTableRow>
<ArgTableRow arg="controller-address" typ="address">CMR 伺服器 IP 地址。</ArgTableRow>
<ArgTableRow arg="pairing-status" typ="multi { array-id, status: string
 }">當前配對狀態。</ArgTableRow>
<ArgTableRow arg="saved-addresses" typ="multi { array-id, address: address (flags=46)
 }">CMR 伺服器已發現的 IP 地址列表。</ArgTableRow>
</ArgTable>
