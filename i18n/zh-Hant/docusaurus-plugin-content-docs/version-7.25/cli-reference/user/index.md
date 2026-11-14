---
sidebar_key: "cli-reference/user/index"
sidebar_position: 5
title: "user"
sidebar_label: 'user'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/user
captured_at: '2026-11-01T21:26:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## 使用者 {#user}

路由器管理使用者賬戶。每個使用者恰好屬於一個 [group](./group.md)，該組授予使用者擁有的許可權（策略）。完整指南請參閱 [使用者](../../authentication-authorization-accounting/user.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="E" typ="expired">密碼已透過 [`/user/expire-password`](./expire-password.md) 過期。下次互動式登入時，系統會要求使用者設定新密碼；設定新密碼會清除該標記。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">使用者賬戶已停用，無法登入。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">登入使用者名稱。允許使用字母、數字以及字元 `_` `.` `#` `-` `@`；名稱必須以字母或數字結尾，且不能以 `.` 或 `-` 開頭。</ArgTableRow>
<ArgTableRow arg="group" typ="enum" mandatory="1">授予使用者所擁有許可權（策略）的使用者組。</ArgTableRow>
<ArgTableRow arg="password" typ="string" mandatory="1">登入密碼。接受任何字元，包括空格、符號和 UTF-8。顯式空值（`password=""`）允許使用空密碼登入。若設定了來自 [`/user/settings`](./settings.md) 的複雜度策略，則應用該策略。</ArgTableRow>
<ArgTableRow arg="inactivity-timeout" typ="time">空閒時間，超過該時間後 `inactivity-policy` 將應用於互動式控制檯會話。範圍 00:01:00 至 1d00:00:00。預設值：10m。</ArgTableRow>
<ArgTableRow arg="inactivity-policy" typ="enum (none | logout | lockscreen)">
當 `inactivity-timeout` 到期時採取的動作：
- `none`（預設）- 空閒會話保持執行。
- `logout` - 關閉空閒會話，並顯示訊息 "`<name>` was logged out due to inactivity"。
- `lockscreen` - 鎖定會話（"Session is locked (Ctrl-D to Quit)"）並要求使用者輸入密碼才能恢復；密碼錯誤時列印 "Sorry, try again."。
</ArgTableRow>
<ArgTableRow arg="address" typ="object { address: alt { address: ipPrefix
, address: ip6Prefix
 }
 }">帶掩碼的 IP 地址或 IPv6 字首。設定後，使用者只能從匹配的源地址登入；來自其他地址的登入將被拒絕。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="last-logged-in" typ="date">使用者上次登入的日期和時間。</ArgTableRow>
</ArgTable>
