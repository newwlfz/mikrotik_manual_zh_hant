---
sidebar_key: "cli-reference/user/settings"
sidebar_position: 5
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/user/settings
captured_at: '2026-11-01T21:26:12+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user/settings {#usersettings}
**型別：** 設定目錄

在 [`/user`](./index.md) 中新增使用者或使用 `/password` 更改密碼時，會強制執行密碼複雜度策略。完整指南請參見 [使用者](../../authentication-authorization-accounting/user.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="minimum-password-length" typ="num">可接受的最短密碼長度，以字元為單位。較短的密碼會被拒絕，提示為 "password is too short - must be at least N characters"。範圍 0 到 4294967295。預設值：0。</ArgTableRow>
<ArgTableRow arg="minimum-categories" typ="num">密碼必須使用的字元類別數量，共四類：數字、小寫字母、大寫字母和符號。較弱的密碼會被拒絕，提示為 "password is too weak - it must contain characters from at least N categories (digits, lower and upper case letters, symbols)"。範圍 0 到 4。預設值：0。</ArgTableRow>
</ArgTable>
