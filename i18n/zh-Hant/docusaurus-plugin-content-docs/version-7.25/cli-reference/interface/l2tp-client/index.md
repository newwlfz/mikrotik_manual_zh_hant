---
sidebar_key: "cli-reference/interface/l2tp-client/index"
sidebar_position: 1
title: "l2tp-client"
sidebar_label: 'l2tp-client'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/l2tp-client
captured_at: '2026-11-01T21:22:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/l2tp-client {#interfacel2tp-client}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面的描述性名稱。</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大傳輸單元。L2TP 介面在不進行封包分片的情況下可以傳送的最大封包大小。</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大接收單元。L2TP 介面在不進行封包分片的情況下可以接收的最大封包大小。</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">鏈路上可以接收的最大封包大小。如果封包大於隧道 MTU，則會被拆分為多個數據包，從而允許透過隧道傳送全尺寸 IP 或乙太網封包。</ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)" mandatory="1">L2TP 伺服器的遠端地址。如果該地址位於 VRF 表中，則應指定 VRF，例如 `192.168.88.1@vrf1`。</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">用於認證的使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string">用於認證的密碼。</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">指定在建立隧道時使用哪個 PPP 配置檔案。</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }">保活超時時間，單位為秒。</ArgTableRow>
<ArgTableRow arg="src-address" typ="ipAddr">用於 L2TP 連線的源地址。</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively) { no:0, yes:1, exclusively:2 }">是否使用對端的 DNS 設定。</ArgTableRow>
<ArgTableRow arg="use-ipsec" typ="bool">
啟用此選項後，會新增動態 IPSec 對端配置和策略（傳輸模式），以將 L2TP 連線封裝到 IPSec 隧道中。

同一 NAT 後面的多個 L2tp/ipsec 用戶端在此模式下將無法工作。要實現這種場景，請停用 use-ipsec，併為啟用了 tunnel=yes、level=unique 設定的用戶端設定靜態策略。
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string">IPsec 預共享金鑰。</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">是否允許 FastPath 處理。如果使用 IPsec，則必須停用。</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">是否將 L2TP 遠端地址新增為預設路由。</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num">啟用 add-default-route 時應用於自動建立的預設路由的距離值。</ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool">僅在產生出站流量時才連線到 L2TP 伺服器。如果啟用，則在連線尚未建立時會新增一條閘道器地址來自 10.112.112.0/24 網路的路由。</ArgTableRow>
<ArgTableRow arg="allow" typ="ubit (pap, chap, mschap1, mschap2)">允許的認證方法。</ArgTableRow>
<ArgTableRow arg="random-source-port" typ="bool">是否為 L2TP 連線隨機化源埠。</ArgTableRow>
<ArgTableRow arg="l2tp-proto-version" typ="enum (l2tpv2 | l2tpv3-ip | l2tpv3-udp) { l2tpv2:0, l2tpv3-ip:1, l2tpv3-udp:2 }">要使用的 L2TP 協定版本。</ArgTableRow>
<ArgTableRow arg="l2tpv3-circuit-id" typ="string">L2TPv3 電路識別符號。</ArgTableRow>
<ArgTableRow arg="l2tpv3-cookie-length" typ="enum (0 | 4-bytes | 8-bytes) { 0:0, 4-bytes:4, 8-bytes:8 }">L2TPv3 cookie 長度。</ArgTableRow>
<ArgTableRow arg="l2tpv3-digest-hash" typ="enum (none | md5 | sha1) { none:99, md5:0, sha1:1 }">L2TPv3 摘要雜湊演算法。</ArgTableRow>
</ArgTable>
