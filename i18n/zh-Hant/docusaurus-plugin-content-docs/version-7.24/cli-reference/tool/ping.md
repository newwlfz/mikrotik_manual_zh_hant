---
sidebar_key: "cli-reference/tool/ping"
sidebar_position: 15
title: "ping"
sidebar_label: "ping"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/ping
captured_at: '2026-11-01T21:30:19+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/ping {#toolping}
**型別：** 命令

完整文件請參閱 [Ping](../../diagnostics-monitoring-and-troubleshooting/ping.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="address (flags=46v%Dm)">目標主機的 IP 地址或 DNS 名稱。請參閱 [address flags](../index.md#address-flags)</ArgTableRow>
<ArgTableRow arg="interval" typ="time">ICMP echo 請求之間的時間間隔</ArgTableRow>
<ArgTableRow arg="size" typ="num">ICMP 資料負載的大小，以位元組為單位</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">ICMP 封包的 Time to Live 值</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">在 IP 頭部中設定的 DSCP 值，用於 QoS 標記</ArgTableRow>
<ArgTableRow arg="do-not-fragment" typ="switch">在 IP 頭部中設定 Don't Fragment 標誌</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip-src-address: ipAddr
, ip6-src-address: ip6Addr
 }">用於 ICMP echo 請求的源 IP 地址</ArgTableRow>
<ArgTableRow arg="arp-ping" typ="bool">使用 ARP 請求代替 ICMP echo 來發現主機</ArgTableRow>
<ArgTableRow arg="count" typ="num">要傳送的 ICMP echo 請求數量</ArgTableRow>
<ArgTableRow arg="nd-ping" typ="bool"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">傳送 ping 所使用的介面</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">用於路由 ping 請求的 VRF 表</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="seq" typ="num">ping 響應的序列號</ArgTableRow>
<ArgTableRow arg="host" typ="alt { ipv6-address: ip6Addr
, mac-address: macAddr
, ip-address: ipAddr
 }">響應主機的 IP 或 MAC 地址</ArgTableRow>
<ArgTableRow arg="size" typ="num">接收到的 ICMP 封包的大小，以位元組為單位</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">從接收到的封包中獲取的 Time to Live 值</ArgTableRow>
<ArgTableRow arg="time" typ="time">ping 探測的往返時間</ArgTableRow>
<ArgTableRow arg="status" typ="string">ping 響應的狀態</ArgTableRow>
<ArgTableRow arg="sent" typ="num">已傳送的 ICMP echo 請求總數</ArgTableRow>
<ArgTableRow arg="received" typ="num">已接收的 ICMP echo 應答總數</ArgTableRow>
<ArgTableRow arg="packet-loss" typ="num">丟包百分比</ArgTableRow>
<ArgTableRow arg="min-rtt" typ="time">測得的最小往返時間</ArgTableRow>
<ArgTableRow arg="avg-rtt" typ="time">測得的平均往返時間</ArgTableRow>
<ArgTableRow arg="max-rtt" typ="time">測得的最大往返時間</ArgTableRow>
</ArgTable>
