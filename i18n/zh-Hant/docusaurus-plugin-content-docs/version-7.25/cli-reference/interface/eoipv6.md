---
sidebar_key: "cli-reference/interface/eoipv6"
sidebar_position: 8
title: "eoipv6"
sidebar_label: 'eoipv6'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/eoipv6
captured_at: '2026-11-01T21:22:29+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/eoipv6 {#interfaceeoipv6}
**型別：** 目錄

[IP 上的乙太網（EoIP）](../../virtual-private-networks/eoip.md) 隧道是一種 MikroTik RouterOS 協定，用於透過 IP 網路在兩臺路由器之間建立乙太網隧道。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">隧道名稱。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer3 最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">介面的媒體訪問控制編號。地址分配機構 IANA 允許自由使用 00:00:5E:80:00:00 - 00:00:5E:FF:FF:FF 範圍內的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="local-address" typ="ip6Addr">隧道封包的源地址，屬於路由器本地。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=6Dvi)" mandatory="1">EoIP 隧道遠端的 IPV6 地址。</ArgTableRow>
<ArgTableRow arg="tunnel-id" typ="num" mandatory="1">唯一的隧道識別符號，必須與隧道另一端匹配。</ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { keepalive-interval: time [1 .. ]
, [keepalive-retries] [ ,num [1 .. ]]
 }">
keepalive 引數設定時間間隔；即使隧道遠端斷開，隧道的 running 標誌也會在該時間間隔內保留。如果配置的時間和重試次數失敗，則移除介面的 running 標誌。  
引數按以下格式寫入：`KeepaliveInterval,KeepaliveRetries`  
 其中 KeepaliveInterval 是時間間隔，KeepaliveRetries 是重試嘗試次數。  
預設情況下，keepalive 設定為 10 秒和 10 次重試。
</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">封包的 DSCP 值。Inherited 表示 DSCP 值繼承自待封裝的封包。</ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool">控制是否更改收到的 TCP SYN 封包的 MSS 大小。啟用後，如果當前 MSS 大小超過隧道介面 MTU（考慮 TCP/IP 開銷），路由器會更改收到的 TCP SYN 封包的 MSS 大小。收到的封裝封包仍包含原始 MSS，只有在解封裝之後才會更改 MSS。</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool">
是否在相關封包中包含 DF 位。
- `no` - 如有需要則進行分片。
- `inherit` - 使用原始封包的 DF 標誌。
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security">指定金鑰時，路由器會使用預共享金鑰和策略向 remote-address 新增動態 IPsec 對等體（預設情況下 phase2 使用 sha1/aes128cbc）。</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }">[地址解析協定](../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together) 模式。</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">ARP 條目超時的時間間隔。</ArgTableRow>
<ArgTableRow arg="arp-accept" typ="bool">是否接受免費 ARP 回覆。</ArgTableRow>
<ArgTableRow arg="loop-protect" typ="enum (default | off | on) { default:0, off:1, on:2 }">在所選介面上啟用或停用環路保護。`default` 的作用等同於關閉。</ArgTableRow>
<ArgTableRow arg="loop-protect-send-interval" typ="time">設定所選介面上傳送環路保護封包的頻率。</ArgTableRow>
<ArgTableRow arg="loop-protect-disable-time" typ="time">設定檢測到環路時停用所選介面的時長。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num">隧道的實際最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num">[Layer2 最大傳輸單元](../../hardware/mtu-in-routeros.md)。對於 EoIP 不可配置。</ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ip6Addr">遠端的當前 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled) { off:1, on:2, disabled:3 }">
環路保護狀態：
- `on` - 已啟用環路保護，並且介面正在傳送和監聽環路保護封包
- `off` - 已停用環路保護
- `disabled` - 已啟用環路保護，介面已收到環路保護封包並停用自身以防止環路。
</ArgTableRow>
</ArgTable>
