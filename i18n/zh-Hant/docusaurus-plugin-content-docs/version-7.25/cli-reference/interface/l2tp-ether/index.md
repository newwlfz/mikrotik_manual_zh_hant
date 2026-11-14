---
sidebar_key: "cli-reference/interface/l2tp-ether/index"
sidebar_position: 1
title: "l2tp-ether"
sidebar_label: 'l2tp-ether'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/l2tp-ether
captured_at: '2026-11-01T21:22:45+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/l2tp-ether {#interfacel2tp-ether}
**型別：** 目錄

二層隧道協定版本 3（L2TPv3）。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否處於 disabled 狀態。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">介面是否為動態建立。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否處於 running 狀態。</ArgTableRow>
<ArgTableRow arg="u" typ="unmanaged">介面是否處於 unmanaged 狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面名稱。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)">遠端伺服器地址。對於入站連線，設定為 0.0.0.0。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">L2TP 介面的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="use-ipsec" typ="bool">對於被動（入站）連線會被忽略。對於入站連線，請使用 l2tp-server 設定。</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string">對於被動（入站）連線會被忽略。對於入站連線，請使用 l2tp-server 設定。</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">是否允許 FastPath 處理。</ArgTableRow>
<ArgTableRow arg="l2tp-proto-version" typ="enum (l2tpv3-ip | l2tpv3-udp) { l2tpv3-ip:1, l2tpv3-udp:2 }">L2TPv3 封裝模式（IP 或 UDP）。</ArgTableRow>
<ArgTableRow arg="circuit-id" typ="string">L2TPv3 遠端識別符號（虛擬電路 ID）。</ArgTableRow>
<ArgTableRow arg="cookie-length" typ="enum (0 | 4-bytes | 8-bytes) { 0:0, 4-bytes:4, 8-bytes:8 }">對於被動（入站）連線會被忽略。對於入站連線，請使用 l2tp-server 設定。</ArgTableRow>
<ArgTableRow arg="digest-hash" typ="enum (none | md5 | sha1) { none:99, md5:0, sha1:1 }">對於被動（入站）連線會被忽略。對於入站連線，請使用 l2tp-server 設定。</ArgTableRow>
<ArgTableRow arg="use-l2-specific-sublayer" typ="bool">啟用 L2TPv3 乙太網偽線二層預設子層。</ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { local-ipv4-address: ipAddr
, local-ipv6-address: ip6Addr
 }">用於 unmanaged L2TP 連線的本地 IPv4 或 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="local-tunnel-id" typ="num">用於 unmanaged L2TP 連線的本地隧道 ID。</ArgTableRow>
<ArgTableRow arg="local-session-id" typ="num">用於 unmanaged L2TP 連線的本地會話 ID。</ArgTableRow>
<ArgTableRow arg="remote-tunnel-id" typ="num">用於 unmanaged L2TP 連線的遠端隧道 ID。</ArgTableRow>
<ArgTableRow arg="remote-session-id" typ="num">用於 unmanaged L2TP 連線的遠端會話 ID。</ArgTableRow>
<ArgTableRow arg="peer-cookie" typ="string">用於 unmanaged L2TP 連線的接收封包 Cookie 十六進位制值（8 或 16 個字元，或為空）。</ArgTableRow>
<ArgTableRow arg="send-cookie" typ="string">用於 unmanaged L2TP 連線的傳送封包 Cookie 十六進位制值（8 或 16 個字元，或為空）。</ArgTableRow>
<ArgTableRow arg="unmanaged-mode" typ="bool">啟用或停用 unmanaged（靜態）隧道模式。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num">隧道的實際最大傳輸單元。</ArgTableRow>
</ArgTable>
