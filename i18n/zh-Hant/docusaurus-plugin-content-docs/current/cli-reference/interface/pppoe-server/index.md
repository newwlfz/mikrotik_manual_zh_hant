---
sidebar_key: "cli-reference/interface/pppoe-server"
title: "pppoe-server"
sidebar_label: 'pppoe-server'
source: https://manual.mikrotik.com/docs/cli-reference/interface/pppoe-server
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pppoe-server {#interfacepppoe-server}
**型別：** 目錄

PPPoE 伺服器配置中有兩類介面（隧道）項——靜態使用者和動態連線。為每個建立到給定伺服器的隧道建立一個介面。如果需要引用為特定使用者建立的特定介面名稱（在防火牆規則或其他位置），則會以管理方式新增靜態介面。每當使用者連線且其使用者名稱不匹配任何現有靜態條目時，動態介面會自動新增到此列表（或者如果該條目已處於活動狀態，因為不能有兩個單獨的隧道介面使用同一名稱引用——如果這是個問題，請設定 *one-session-per-host* 值）。動態介面在使用者連線時出現，並在使用者斷開後消失，因此無法在路由器配置中（例如在防火牆中）引用為該使用者建立的隧道，所以如果你需要為該使用者設定持久規則，請為其建立靜態條目。否則，使用動態配置是安全的。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">該專案是否被停用。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">伺服器介面是否為動態建立。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面名稱。</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">用於認證的使用者名稱。</ArgTableRow>
<ArgTableRow arg="service" typ="string" mandatory="1">PPPoE 服務名稱。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mtu" typ="num">連線的當前 MTU。</ArgTableRow>
<ArgTableRow arg="mru" typ="num">連線的當前 MRU。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="string">連線的遠端 IP 地址。</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">所使用的加密編碼。</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">連線執行時長。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">用戶端接入的介面。</ArgTableRow>
<ArgTableRow arg="vid" typ="num">連線的 VLAN ID。</ArgTableRow>
</ArgTable>
