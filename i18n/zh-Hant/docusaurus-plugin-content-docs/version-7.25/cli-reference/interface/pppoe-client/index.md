---
sidebar_key: "cli-reference/interface/pppoe-client/index"
sidebar_position: 1
title: "pppoe-client"
sidebar_label: 'pppoe-client'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/pppoe-client
captured_at: '2026-11-01T21:22:56+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pppoe-client {#interfacepppoe-client}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否已停用。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">介面是否無效。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">PPPoE 介面的名稱，若未指定則由 RouterOS 生成。</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大接收單元。</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">鏈路上可接收的最大封包大小。如果封包大於隧道 MTU，則會被拆分為多個數據包，從而允許透過隧道傳送完整大小的 IP 或乙太網封包。</ArgTableRow>
<ArgTableRow arg="interface" typ="multi { array-id, interface: iface_enum
 }">執行用戶端的介面名稱。</ArgTableRow>
<ArgTableRow arg="user" typ="string">用於身份驗證的使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string">用於身份驗證的密碼。</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">指定建立隧道時使用的 PPP 配置檔案。</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">保活超時時間，單位為秒。</ArgTableRow>
<ArgTableRow arg="service-name" typ="string">指定接入集中器上設定的服務名稱。可以留空以連線到任何 PPPoE 伺服器。</ArgTableRow>
<ArgTableRow arg="ac-name" typ="string">接入集中器名稱。可以留空，用戶端將連線到廣播域中的任何接入集中器。</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">是否自動新增預設路由。</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num">如果同時啟用了 add-default-route，則應用於自動建立的預設路由的距離值。</ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool">僅在生成出站流量時才連線到 AC。如果選中，則在連線尚未建立時新增一條閘道器地址來自 10.112.112.0/24 網路的路由。</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool">是否從對端獲取 DNS 設定。</ArgTableRow>
<ArgTableRow arg="allow" typ="ubit (pap, chap, mschap1, mschap2)">允許的身份驗證方法。預設情況下，允許所有方法。</ArgTableRow>
<ArgTableRow arg="host-uniq" typ="string">十六進位制格式的 host-uniq 值。</ArgTableRow>
</ArgTable>
