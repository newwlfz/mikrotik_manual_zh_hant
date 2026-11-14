---
sidebar_key: "cli-reference/interface/eoip"
sidebar_position: 7
title: "eoip"
sidebar_label: 'eoip'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/eoip
captured_at: '2026-11-01T21:22:30+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/eoip {#interfaceeoip}
**型別：** 目錄

[IP 上的乙太網（EoIP）](../../virtual-private-networks/eoip.md) 隧道是一種 MikroTik RouterOS 協定，用於透過 IP 網路在兩臺路由器之間建立乙太網隧道。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">介面名稱。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">三層最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">介面的媒體訪問控制地址。地址編號管理機構 IANA 允許自由使用 00:00:5E:80:00:00 - 00:00:5E:FF:FF:FF 範圍內的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">隧道報文的源地址，位於路由器本地。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=4Dv)" mandatory="1">EoIP 隧道遠端的 IP 地址。</ArgTableRow>
<ArgTableRow arg="tunnel-id" typ="num" mandatory="1">唯一的隧道識別符號，必須與隧道另一端匹配。</ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { keepalive-interval: time [1 .. ]
, [keepalive-retries] [ ,num [1 .. ]]
 }">
keepalive 引數設定時間間隔，在此期間即使隧道遠端斷開，隧道執行標誌仍保持不變。如果配置的時間和重試次數都已用盡，則移除介面執行標誌。  
引數按以下格式書寫：`KeepaliveInterval,KeepaliveRetries`  
 其中 KeepaliveInterval 是時間間隔，KeepaliveRetries 是重試次數。  
預設情況下 keepalive 設定為 10 秒和 10 次重試。
</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">報文的 DSCP 值。Inherited 表示 DSCP 值繼承自要被封裝的報文。</ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool">控制是否更改接收到的 TCP SYN 報文的 MSS 大小。啟用後，如果當前 MSS 大小超過隧道介面 MTU（考慮 TCP/IP 開銷），路由器會更改接收到的 TCP SYN 報文的 MSS 大小。接收到的封裝報文仍包含原始 MSS，只有在解封裝之後才會更改 MSS。</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool">
是否在相關報文中包含 DF 位。
- `no` - 如有需要則進行分片。
- `inherit` - 使用原始報文的 DF 標誌。
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security">指定金鑰後，路由器會向 remote-address 新增一個動態 IPsec 對等體，並附帶預共享金鑰和策略（預設情況下 phase2 使用 sha1/aes128cbc）。</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">是否允許 FastPath 處理。如果使用 IPsec 隧道，則必須停用。</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }">[地址解析協定](../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together) 模式。</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">ARP 條目的超時時間間隔。</ArgTableRow>
<ArgTableRow arg="arp-accept" typ="bool">是否接受無償 ARP 應答。</ArgTableRow>
<ArgTableRow arg="loop-protect" typ="enum (default | off | on) { default:0, off:1, on:2 }">啟用或停用所選介面上的環路保護。`default` 的作用與關閉相同。</ArgTableRow>
<ArgTableRow arg="loop-protect-send-interval" typ="time">設定所選介面上傳送環路保護報文的頻率。</ArgTableRow>
<ArgTableRow arg="loop-protect-disable-time" typ="time">設定檢測到環路時停用所選介面的時長。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num">隧道的實際最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num">[Layer2 最大傳輸單元](../../hardware/mtu-in-routeros.md)。對於 EoIP 不可配置。</ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ipAddr">遠端的當前 IPv4 地址。</ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled) { off:1, on:2, disabled:3 }">
環路保護狀態：
- `on` - 環路保護已啟用，介面正在傳送並監聽環路保護報文
- `off` - 環路保護已停用
- `disabled` - 環路保護已啟用，介面已收到環路保護報文並停用了自身以防止環路。
</ArgTableRow>
</ArgTable>
