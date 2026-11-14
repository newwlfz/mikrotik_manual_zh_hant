---
sidebar_key: "cli-reference/interface/eoipv6"
sidebar_position: 8
title: "eoipv6"
sidebar_label: 'eoipv6'
source: https://manual.mikrotik.com/docs/cli-reference/interface/eoipv6
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/eoipv6 {#interfaceeoipv6}
**型別：** 目錄

[IP 上的乙太網（EoIP）](../../virtual-private-networks/eoip.md) 隧道是一種 MikroTik RouterOS 協定，用於透過 IP 網路在兩臺路由器之間建立乙太網隧道。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">隧道的名稱。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">三層最大傳輸單元。預設值：`auto` — 路由器從路徑 MTU 中減去 EoIP/IPv6 開銷（在 1500 位元組路徑上 actual-mtu 為 1444）。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">介面的媒體訪問控制（MAC）地址。可接受任意值；自動生成的地址為本地管理地址。IANA 允許自由使用 00:00:5E:80:00:00 至 00:00:5E:FF:FF:FF 範圍（私有單播）。</ArgTableRow>
<ArgTableRow arg="local-address" typ="ip6Addr">隧道報文的源地址，為路由器本地地址。預設值 — 用於到達遠端的介面地址。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=6Dvi)" mandatory="1">EoIP 隧道遠端的 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="tunnel-id" typ="num" mandatory="1">唯一的隧道識別符號，必須與隧道另一端匹配。</ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { keepalive-interval: time [1 .. ]
, [keepalive-retries] [ ,num [1 .. ]]
 }">
當遠端在 `KeepaliveInterval × KeepaliveRetries` 時間內沒有應答時，路由器會移除該介面的 running 標誌。
引數按以下格式寫入：`KeepaliveInterval,KeepaliveRetries`
其中 KeepaliveInterval 是時間間隔，KeepaliveRetries 是重試次數。
Keepalive 預設啟用（`10s,10`）。將其設定為停用值（`0,0`、`off`、`none`）會被拒絕；取消設定 `keepalive` 會將其完全關閉 — 此後當遠端停止應答時就不再移除 running 標誌。
</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">封包的 DSCP 值。Inherited 表示 DSCP 值從待封裝的封包繼承。</ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool">控制是否更改接收到的 TCP SYN 封包的 MSS 大小。啟用後，如果當前 MSS 大小超過隧道介面 MTU（考慮 TCP/IP 開銷），路由器會更改接收到的 TCP SYN 封包的 MSS 大小。接收到的封裝封包仍包含原始 MSS，只有在解封裝後才會更改 MSS。</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool">
是否在相關報文中包含 DF 位。預設值：`no`。
- `no` - 如需要則進行分片。
- `inherit` - 使用原始封包的 DF 標誌。
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security">當指定了金鑰時，路由器會為 remote-address 新增一個動態 IPsec 對等體，並配置預共享金鑰和策略（預設情況下 phase2 使用 sha1/aes128cbc）。此選單沒有 `allow-fast-path` 屬性，因此 IPsec 在這裡不會與 fast path 競爭。</ArgTableRow>
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
<ArgTableRow arg="l2mtu" typ="num">[二層最大傳輸單元](../../hardware/mtu-in-routeros.md)。EoIP 不可配置此項；顯示值為 65535。</ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ip6Addr">遠端的當前 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled) { off:1, on:2, disabled:3 }">
環路保護狀態：
- `on` - 已啟用環路保護，並且介面正在傳送和監聽環路保護封包
- `off` - 已停用環路保護
- `disabled` - 已啟用環路保護，介面已收到環路保護封包並停用自身以防止環路。
</ArgTableRow>
</ArgTable>
