---
sidebar_key: "cli-reference/interface/sstp-server/index"
sidebar_position: 1
title: "sstp-server"
sidebar_label: 'sstp-server'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/sstp-server
captured_at: '2026-11-01T21:23:01+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/sstp-server {#interfacesstp-server}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">條目是否被停用。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">伺服器介面是否為動態建立。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
<ArgTableRow arg="H" typ="hw-crypto">硬體加密是否已啟用。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面名稱。</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">用於身份驗證的使用者名稱。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mtu" typ="num">連線的當前 MTU。</ArgTableRow>
<ArgTableRow arg="client-address" typ="string">已連線用戶端的 IP 地址。</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">連線執行時間。</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">使用的加密編碼。</ArgTableRow>
</ArgTable>
