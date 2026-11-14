---
sidebar_key: "cli-reference/user/active"
sidebar_position: 2
title: "active"
sidebar_label: 'active'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/user/active
captured_at: '2026-11-01T21:26:11+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## user/active {#useractive}
**型別：** 目錄

當前已登入的管理會話。所有屬性均為只讀。使用 `/user/active/remove` 終止會話。完整指南請參閱 [使用者](../../authentication-authorization-accounting/user.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="R" typ="radius">透過 RADIUS 認證的使用者（請參閱 [`/user/aaa`](./aaa.md)）。</ArgTableRow>
<ArgTableRow arg="M" typ="by-romon">會話透過 RoMON 建立；`by-romon` 儲存 RoMON 代理的 MAC 地址。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="when" typ="date">會話登入的日期和時間。</ArgTableRow>
<ArgTableRow arg="name" typ="string">登入使用者的名稱，取自 [`/user`](./index.md)。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { ip: ipAddr
, ip6: ip6Addr
, address: macAddr
 }">會話的源地址：IP、IPv6 或 MAC 地址。</ArgTableRow>
<ArgTableRow arg="by-romon" typ="macAddr">會話所經由的 RoMON 代理的 MAC 地址；僅對 RoMON 會話設定（標誌 `M`）。</ArgTableRow>
<ArgTableRow arg="via" typ="enum (unknown | winbox | console | telnet | ftp | web | ssh | mac-telnet | bandwidth-test | api | romon | rest-api) { unknown:0, winbox:1, console:2, telnet:3, ftp:4, web:5, ssh:6, mac-telnet:7, bandwidth-test:8, api:9, romon:10, rest-api:13 }">會話連線所使用的管理服務：`unknown`、`winbox`、`console`、`telnet`、`ftp`、`web`、`ssh`、`mac-telnet`、`bandwidth-test`、`api`、`romon` 或 `rest-api`。</ArgTableRow>
<ArgTableRow arg="group" typ="enum">登入使用者所屬的組，該組授予會話的許可權。</ArgTableRow>
</ArgTable>
