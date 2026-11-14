---
sidebar_key: "cli-reference/system/license/renew"
sidebar_position: 3
title: "renew"
sidebar_label: 'renew'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/license/renew
captured_at: '2026-11-01T21:25:31+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/license/renew {#systemlicenserenew}
**系統能力：** chr
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="account" typ="string">MikroTik.com 賬戶使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string">MikroTik.com 賬戶密碼。</ArgTableRow>
<ArgTableRow arg="level" typ="enum (p1 | p10 | p-unlimited) { p1:1, p10:2, p-unlimited:3 }">所需的 CHR 許可證級別。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">續訂操作的狀態。</ArgTableRow>
</ArgTable>
