---
sidebar_key: "cli-reference/interface/pptp-client/index"
sidebar_position: 1
title: "pptp-client"
sidebar_label: 'pptp-client'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/pptp-client
captured_at: '2026-11-01T21:22:58+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/pptp-client {#interfacepptp-client}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面的描述性名稱。</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大傳輸單元。PPTP 介面在不進行封包分片的情況下能夠傳送的最大封包大小。</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大接收單元。PPTP 介面在不進行封包分片的情況下能夠接收的最大封包大小。</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">鏈路上可接收的最大封包大小。如果封包大於隧道 MTU，則會被拆分為多個數據包，從而允許透過隧道傳送全尺寸的 IP 或乙太網封包。</ArgTableRow>
<ArgTableRow arg="connect-to" typ="alt { address: ipAddr
, name: string
 }" mandatory="1">PPTP 伺服器的遠端地址。</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">用於身份驗證的使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string">用於身份驗證的密碼。</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">指定建立隧道時使用的 PPP 配置檔案。</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">保活超時時間（秒）。</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively) { no:0, yes:1, exclusively:2 }">是否使用對端的 DNS 設定。</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">是否將 PPTP 遠端地址新增為預設路由。</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num">啟用 add-default-route 時應用於自動建立的預設路由的距離值。</ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool">僅在產生出站流量時才連線到 PPTP 伺服器。如果啟用，則在連線尚未建立時會新增一條閘道器地址來自 10.112.112.0/24 網路的路由。</ArgTableRow>
<ArgTableRow arg="allow" typ="ubit (pap, chap, mschap1, mschap2)">允許的身份驗證方法。</ArgTableRow>
</ArgTable>
