---
sidebar_key: "cli-reference/interface/l2tp-server/index"
sidebar_position: 1
title: "l2tp-server"
sidebar_label: 'l2tp-server'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/l2tp-server
captured_at: '2026-11-01T21:22:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/l2tp-server {#interfacel2tp-server}
**型別：** 目錄

對於每個建立到給定伺服器的隧道，都會建立一個介面。L2TP 伺服器配置中有兩種型別的介面：
- 靜態介面由管理員手動新增，用於在需要引用為特定使用者建立的特定介面名稱時（例如在防火牆規則或其他位置）。
- 動態介面會在使用者連線時自動新增到此列表，前提是該使用者的使用者名稱與任何現有靜態條目都不匹配（或者該條目已處於活動狀態，因為同一個名稱不能引用兩個獨立的隧道介面）。

動態介面在使用者連線時出現，並在使用者斷開連線後消失，因此無法在路由器配置中（例如在防火牆中）引用為該使用者建立的隧道，所以如果需要為該使用者設定持久規則，請為其建立靜態條目。否則，使用動態配置是安全的。

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
