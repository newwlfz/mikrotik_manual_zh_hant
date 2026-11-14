---
sidebar_key: "cli-reference/interface/ovpn-server/index"
sidebar_position: 1
title: "ovpn-server"
sidebar_label: 'ovpn-server'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/ovpn-server
captured_at: '2026-11-01T21:22:54+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ovpn-server {#interfaceovpn-server}
**型別：** 目錄

為連線到指定伺服器的每個隧道建立一個介面。OVPN 伺服器配置中有兩種型別的介面：

- 靜態介面由管理員手動新增，用於在需要引用為特定使用者建立的某個具體介面名稱時使用（例如在防火牆規則或其他位置）。
- 動態介面會在使用者連線時自動加入此列表，前提是該使用者的使用者名稱與任何現有靜態條目都不匹配，或者匹配的靜態條目已處於活動狀態，因為兩個獨立的隧道介面不能使用相同的名稱。

動態介面在使用者連線時出現，在使用者斷開連線時消失。因此，無法在路由器配置中（例如在防火牆規則中）引用為該使用者建立的隧道。如果需要為使用者保留持久規則，請建立靜態條目。否則，動態配置已經足夠。

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
