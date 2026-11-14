---
sidebar_key: "cli-reference/interface/pptp-server"
title: "pptp-server"
sidebar_label: 'pptp-server'
source: https://manual.mikrotik.com/docs/cli-reference/interface/pptp-server
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pptp-server {#interfacepptp-server}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該專案是否被停用。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">伺服器介面是否為動態建立。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面名稱。</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">用於身份驗證的使用者名稱。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mtu" typ="num">連線的當前 MTU。</ArgTableRow>
<ArgTableRow arg="mru" typ="num">連線的當前 MRU。</ArgTableRow>
<ArgTableRow arg="client-address" typ="string">已連線用戶端的 IP 地址。</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">連線執行時長。</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">使用的加密編碼。</ArgTableRow>
</ArgTable>
