---
sidebar_key: "cli-reference/user/aaa"
sidebar_position: 1
title: "aaa"
sidebar_label: 'aaa'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/user/aaa
captured_at: '2026-11-01T21:26:11+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user/aaa {#useraaa}
**型別：** 設定目錄

用於管理登入的 AAA 設定：針對 RADIUS 伺服器進行身份驗證，以及對管理會話進行 RADIUS 計費。完整指南請參見 [使用者](../../authentication-authorization-accounting/user.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="use-radius" typ="bool">使用 RADIUS 伺服器對管理登入進行身份驗證；必須存在一個帶有 `service=login` 的 [`/radius`](../radius/index.md) 條目。首先查詢本地使用者資料庫——RADIUS 僅用於本地未找到的使用者名稱。Access-Accept 中的 `Mikrotik-Group` 屬性選擇本地組。透過 RADIUS 進行 SSH 登入的密碼身份驗證使用 MS-CHAPv2。預設值：no.</ArgTableRow>
<ArgTableRow arg="accounting" typ="bool">當管理會話登入和登出時，傳送 RADIUS 計費 Start 和 Stop 訊息。管理會話計費不包含頻寬計數器。預設值：yes。</ArgTableRow>
<ArgTableRow arg="interim-update" typ="time">活動會話的 Interim-Update 計費訊息之間的間隔。預設值：0s。</ArgTableRow>
<ArgTableRow arg="default-group" typ="enum">當伺服器未傳送組，或傳送的組列在 `exclude-groups` 中時，分配給透過 RADIUS 身份驗證的使用者的組。預設值：read。</ArgTableRow>
<ArgTableRow arg="exclude-groups" typ="multi { group: enum
 }">從不接受來自 RADIUS 伺服器的組。如果伺服器傳送其中任意一個，使用者將改為獲得 `default-group`；這可防止惡意 RADIUS 伺服器授予完全許可權。預設值：none。</ArgTableRow>
</ArgTable>
