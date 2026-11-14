---
sidebar_key: "cli-reference/interface/l2tp-ether/index"
sidebar_position: 1
title: "l2tp-ether"
sidebar_label: "l2tp-ether"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/l2tp-ether
captured_at: '2026-11-01T21:27:21+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/l2tp-ether {#interfacel2tp-ether}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="u" typ="unmanaged">unmanaged</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)">遠端伺服器地址，或為空（零）地址以接受入站連線</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="use-ipsec" typ="bool">對被動（入站）連線被忽略（入站連線請使用 l2tp-server 設定）</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string">對被動（入站）連線被忽略（入站連線請使用 l2tp-server 設定）</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool"></ArgTableRow>
<ArgTableRow arg="l2tp-proto-version" typ="enum (l2tpv3-ip | l2tpv3-udp) { l2tpv3-ip:1, l2tpv3-udp:2 }">L2TPv3 封裝模式（IP 或 UDP）</ArgTableRow>
<ArgTableRow arg="circuit-id" typ="string">L2TPv3 遠端識別符號（虛擬電路 ID）</ArgTableRow>
<ArgTableRow arg="cookie-length" typ="enum (0 | 4-bytes | 8-bytes) { 0:0, 4-bytes:4, 8-bytes:8 }">對被動（入站）連線被忽略（入站連線請使用 l2tp-server 設定）</ArgTableRow>
<ArgTableRow arg="digest-hash" typ="enum (none | md5 | sha1) { none:99, md5:0, sha1:1 }">對被動（入站）連線被忽略（入站連線請使用 l2tp-server 設定）</ArgTableRow>
<ArgTableRow arg="use-l2-specific-sublayer" typ="bool">啟用 L2TPv3 乙太網偽線的二層預設子層</ArgTableRow>
<ArgTableRow arg="local-address" typ="alt { local-ipv4-address: ipAddr
, local-ipv6-address: ip6Addr
 }">本地 IPv4 或 IPv6 地址（非託管 L2TP 連線）</ArgTableRow>
<ArgTableRow arg="local-tunnel-id" typ="num">本地隧道 ID（非託管 L2TP 連線）</ArgTableRow>
<ArgTableRow arg="local-session-id" typ="num">本地會話 ID（非託管 L2TP 連線）</ArgTableRow>
<ArgTableRow arg="remote-tunnel-id" typ="num">遠端隧道 ID（非託管 L2TP 連線）</ArgTableRow>
<ArgTableRow arg="remote-session-id" typ="num">遠端會話 ID（非託管 L2TP 連線）</ArgTableRow>
<ArgTableRow arg="peer-cookie" typ="string">接收報文的 cookie 十六進位制值（8 或 16 個字元，或為空）（非託管 L2TP 連線）</ArgTableRow>
<ArgTableRow arg="send-cookie" typ="string">傳送報文的 cookie 十六進位制值（8 或 16 個字元，或為空）（非託管 L2TP 連線）</ArgTableRow>
<ArgTableRow arg="unmanaged-mode" typ="bool">啟用/停用非託管（靜態）隧道模式</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num"></ArgTableRow>
</ArgTable>
