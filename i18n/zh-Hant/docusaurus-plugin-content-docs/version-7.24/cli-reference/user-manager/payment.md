---
sidebar_key: "cli-reference/user-manager/payment"
sidebar_position: 7
title: "payment"
sidebar_label: "payment"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/user-manager/payment
captured_at: '2026-11-01T21:30:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user-manager/payment {#user-managerpayment}
**包：** userman-5
**型別：** 目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="price" typ="num"></ArgTableRow>
<ArgTableRow arg="currency" typ="string"></ArgTableRow>
<ArgTableRow arg="trans-start" typ="date"></ArgTableRow>
<ArgTableRow arg="trans-end" typ="alt { constant: enum (not-finished) { not-finished:0 }
, date: date
 }"></ArgTableRow>
<ArgTableRow arg="trans-status" typ="enum (started | pending | approved | declined | error | timeout | aborted | user-approved)"></ArgTableRow>
<ArgTableRow arg="method" typ="enum (paypal | authorize-net)"></ArgTableRow>
<ArgTableRow arg="user-message" typ="string"></ArgTableRow>
</ArgTable>
