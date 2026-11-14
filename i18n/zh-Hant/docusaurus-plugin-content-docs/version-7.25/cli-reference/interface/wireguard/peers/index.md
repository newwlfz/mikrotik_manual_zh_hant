---
sidebar_key: "cli-reference/interface/wireguard/peers/index"
sidebar_position: 1
title: "peers"
sidebar_label: 'peers'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/wireguard/peers
captured_at: '2026-11-01T21:23:20+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireguard/peers {#interfacewireguardpeers}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">該對端是否為動態建立。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">該對端所屬的 WireGuard 介面的名稱。</ArgTableRow>
<ArgTableRow arg="name" typ="string">為對端新增名稱，用作 WireGuard 日誌中的引用。自 RouterOS 7.15 版本起可用。</ArgTableRow>
<ArgTableRow arg="public-key" typ="string">從私鑰計算得出的 base64 公鑰。對端使用公鑰相互認證。</ArgTableRow>
<ArgTableRow arg="private-key" typ="alt { private-key: num
, private-key: string
 }">base64 私鑰。`auto` 會自動生成金鑰，`none` 會停用它。</ArgTableRow>
<ArgTableRow arg="endpoint-address" typ="address (flags=46D)">WireGuard 用於在兩個對端之間建立安全連線的 IP 地址或主機名。</ArgTableRow>
<ArgTableRow arg="endpoint-port" typ="num">WireGuard 對端用於監聽傳入流量的 UDP 埠。</ArgTableRow>
<ArgTableRow arg="allowed-address" typ="multi { allowed-address: address (flags=46/)
 }" mandatory="1">帶有 CIDR 掩碼的 IP（v4 或 v6）地址列表，允許來自這些地址的傳入流量發往該對端，並且該對端的傳出流量會發往這些地址。Allowed-address 範圍不能在同一介面上重疊。</ArgTableRow>
<ArgTableRow arg="preshared-key" typ="alt { preshared-key: num
, preshared-key: string
 }">base64 預共享金鑰。增加一層對稱金鑰加密，以提供抗後量子能力。`auto` 會自動生成金鑰。</ArgTableRow>
<ArgTableRow arg="persistent-keepalive" typ="time">以秒為單位的間隔，表示向對端傳送經過身份驗證的空封包的頻率，以保持有狀態防火牆或 NAT 對映有效。值為 0 會停用 keepalive。</ArgTableRow>
<ArgTableRow arg="client-address" typ="multi { client-address: address (flags=46/)
 }">當用戶端透過二維條碼匯入時，會在該裝置上設定此 WireGuard 介面的地址。</ArgTableRow>
<ArgTableRow arg="client-dns" typ="multi { client-dns: address (flags=46D)
 }">生成的用戶端配置中包含的 DNS 伺服器。這不會更改此路由器上的 DNS 配置。</ArgTableRow>
<ArgTableRow arg="client-endpoint" typ="address (flags=46D)">生成的用戶端配置中作為 endpoint 包含的 IP 地址或主機名。WireGuard 介面的監聽埠會附加到其後。</ArgTableRow>
<ArgTableRow arg="client-keepalive" typ="time">與 persistent-keepalive 相同，但從對端一側使用。</ArgTableRow>
<ArgTableRow arg="client-listen-port" typ="num">WireGuard 隧道用於監聽來自對端的傳入流量並從中發出傳出封包的本地埠。</ArgTableRow>
<ArgTableRow arg="client-allowed-address" typ="multi { client-allowed-address: address (flags=46/)
 }">為用戶端配置的允許 IP。自 RouterOS 7.21 版本起可用。</ArgTableRow>
<ArgTableRow arg="client-mtu" typ="num">匯入配置時在用戶端上設定的 MTU 值。</ArgTableRow>
<ArgTableRow arg="responder" typ="bool">指定該對端是連線發起方還是僅作為響應方。在充當用戶端裝置伺服器的 WireGuard 裝置上使用。否則，路由器會反覆嘗試連線到 endpoint-address 或 current-endpoint-address。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="current-endpoint-address" typ="address (flags=46)">來自該對端的、經過正確身份驗證的封包的最新源 IP 地址。</ArgTableRow>
<ArgTableRow arg="current-endpoint-port" typ="num">來自該對端的、經過正確身份驗證的封包的最新源 IP 埠。</ArgTableRow>
<ArgTableRow arg="rx" typ="num">從該對端接收的總位元組數。</ArgTableRow>
<ArgTableRow arg="tx" typ="num">傳輸到該對端的總位元組數。</ArgTableRow>
<ArgTableRow arg="last-handshake" typ="time">自上次成功握手後經過的時間（秒）。</ArgTableRow>
</ArgTable>
