---
sidebar_key: "cli-reference/interface/ipipv6"
sidebar_position: 13
title: "ipipv6"
sidebar_label: 'ipipv6'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ipipv6
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ipipv6 {#interfaceipipv6}
**型別：** 目錄

[IPIP](../../virtual-private-networks/ipip.md)（IP-in-IP）是 RFC 2003 中定義的一種簡單隧道協定，它將 IP 封包封裝在另一個 IP 頭中，以便在兩個端點之間傳輸流量。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面名稱。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer3 最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="local-address" typ="ip6Addr">路由器上供 IPIP 隧道使用的 IP 地址。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=6Dvi)" mandatory="1">IPIP 隧道遠端的 IP 地址。</ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { keepalive-interval: time [1 .. ]
, [keepalive-retries] [ ,num [1 .. ]]
 }">
keepalive 引數設定時間間隔，在該間隔內，即使隧道遠端斷開，隧道的 running 標誌仍會保留。如果配置的時間和重試次數失敗，則移除介面的 running 標誌。  
引數按以下格式寫入：`KeepaliveInterval,KeepaliveRetries`  
 其中 KeepaliveInterval 是時間間隔，KeepaliveRetries 是重試次數。  
預設情況下，keepalive 設定為 10 秒和 10 次重試。
</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">封包的 DSCP 值。Inherited 表示 DSCP 值繼承自隧道傳輸的流量。</ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool">控制是否更改收到的 TCP SYN 封包的 MSS 大小。啟用後，如果當前 MSS 大小超過隧道介面 MTU（考慮 TCP/IP 開銷），路由器會更改收到的 TCP SYN 封包的 MSS 大小。收到的封裝封包仍包含原始 MSS，只有在解封裝後才會更改 MSS。</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool">
是否在相關封包中包含 DF 位。
- `no` - 如需要則進行分片。
- `inherit` - 使用原始封包的 DF 標誌。
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security">指定 secret 後，路由器會向 remote-address 新增動態 IPsec 對等體，並帶有預共享金鑰和策略（預設情況下，phase2 使用 sha1/aes128cbc）。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num">隧道的實際最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ip6Addr">遠端的當前 IP 地址。</ArgTableRow>
</ArgTable>
