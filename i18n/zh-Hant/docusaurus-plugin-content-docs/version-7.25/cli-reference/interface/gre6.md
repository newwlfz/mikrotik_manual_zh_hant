---
sidebar_key: "cli-reference/interface/gre6"
sidebar_position: 11
title: "gre6"
sidebar_label: 'gre6'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/gre6
captured_at: '2026-11-01T21:22:44+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/gre6 {#interfacegre6}
**型別：** 目錄

[Generic Routing Encapsulation (GRE)](../../virtual-private-networks/gre.md) 是一種隧道協定，最初由 Cisco 開發，用於透過 IP 網路封裝各種網路層協定。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">隧道名稱。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer3 最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="local-address" typ="ip6Addr">用於本地隧道端的 IPV6 地址。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=6Dvi)" mandatory="1">遠端隧道端的 IPV6 地址。</ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { keepalive-interval: time [1 .. ]
, [keepalive-retries] [ ,num [1 .. ]]
 }">
keepalive 引數設定一個時間間隔，在該間隔內即使隧道遠端宕機，隧道 running 標誌仍會保持。如果配置的時間和重試次數失敗，則移除介面 running 標誌。  
引數按以下格式書寫：`KeepaliveInterval,KeepaliveRetries`  
 其中 KeepaliveInterval 是時間間隔，KeepaliveRetries 是重試次數。  
預設情況下，keepalive 設定為 10 秒和 10 次重試。
</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">封包的 DSCP 值。Inherited 表示 DSCP 值繼承自隧道流量。</ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool">控制是否更改接收到的 TCP SYN 封包的 MSS 大小。啟用後，如果當前 MSS 大小超過隧道介面 MTU（考慮 TCP/IP 開銷），路由器會更改接收到的 TCP SYN 封包的 MSS 大小。接收到的封裝封包仍包含原始 MSS，只有在解封裝後才會更改 MSS。</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool">
是否在相關封包中包含 DF 位。
- `no` - 如有需要則分片。
- `inherit` - 使用原始封包的 DF 標誌。
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security">指定金鑰後，路由器會使用預共享金鑰和策略向 remote-address 新增動態 IPsec 對等體（預設情況下 phase2 使用 sha1/aes128cbc）。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ip6Addr"></ArgTableRow>
</ArgTable>
