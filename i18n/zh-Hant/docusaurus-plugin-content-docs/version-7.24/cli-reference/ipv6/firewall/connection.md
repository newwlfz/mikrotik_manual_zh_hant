---
sidebar_key: "cli-reference/ipv6/firewall/connection"
sidebar_position: 2
title: "connection"
sidebar_label: "connection"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ipv6/firewall/connection
captured_at: '2026-11-01T21:29:08+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/firewall/connection {#ipv6firewallconnection}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="E" typ="expected">expected</ArgTableRow>
<ArgTableRow arg="S" typ="seen-reply">seen-reply</ArgTableRow>
<ArgTableRow arg="A" typ="assured">assured</ArgTableRow>
<ArgTableRow arg="C" typ="confirmed">confirmed</ArgTableRow>
<ArgTableRow arg="D" typ="dying">dying</ArgTableRow>
<ArgTableRow arg="F" typ="fasttrack">fasttrack</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offload">hw-offload</ArgTableRow>
<ArgTableRow arg="s" typ="srcnat">srcnat</ArgTableRow>
<ArgTableRow arg="d" typ="dstnat">dstnat</ArgTableRow>
<ArgTableRow arg="h" typ="uses-helper">uses-helper</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="protocol" typ="enum ()">連線協定。</ArgTableRow>
<ArgTableRow arg="src-address" typ="ip6Addr">連線的源 IP 地址。</ArgTableRow>
<ArgTableRow arg="src-port" typ="num">連線的源埠。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="ip6Addr">連線的目標 IP 地址。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="num">連線的目標埠。</ArgTableRow>
<ArgTableRow arg="reply-src-address" typ="ip6Addr">回覆源 IP 地址。</ArgTableRow>
<ArgTableRow arg="reply-src-port" typ="num">回覆源埠。</ArgTableRow>
<ArgTableRow arg="reply-dst-address" typ="ip6Addr">回覆目標 IP 地址。</ArgTableRow>
<ArgTableRow arg="reply-dst-port" typ="num">回覆目標埠。</ArgTableRow>
<ArgTableRow arg="tcp-state" typ="enum (none | syn-sent | syn-recv | established | fin-wait | close-wait | last-ack | time-wait | close | listen) { none:0, syn-sent:1, syn-recv:2, established:3, fin-wait:4, close-wait:5, last-ack:6, time-wait:7, close:8, listen:9 }">TCP 連線狀態。</ArgTableRow>
<ArgTableRow arg="icmp-type" typ="num">ICMP 型別。</ArgTableRow>
<ArgTableRow arg="icmp-code" typ="num">ICMP 程式碼。</ArgTableRow>
<ArgTableRow arg="icmp-id" typ="num">ICMP ID.</ArgTableRow>
<ArgTableRow arg="gre-protocol" typ="num">GRE 協定。</ArgTableRow>
<ArgTableRow arg="gre-version" typ="num">GRE 版本。</ArgTableRow>
<ArgTableRow arg="gre-key" typ="num">GRE 金鑰。</ArgTableRow>
<ArgTableRow arg="connection-type" typ="string">連線型別。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">連線超時。</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="string">連線標記。</ArgTableRow>
<ArgTableRow arg="orig-packets" typ="num">原始方向封包數量。</ArgTableRow>
<ArgTableRow arg="orig-bytes" typ="num">原始方向位元組數。</ArgTableRow>
<ArgTableRow arg="orig-fasttrack-packets" typ="num">原始方向 fasttrack 封包數量。</ArgTableRow>
<ArgTableRow arg="orig-fasttrack-bytes" typ="num">原始方向 fasttrack 位元組數。</ArgTableRow>
<ArgTableRow arg="repl-packets" typ="num">回覆方向封包數量。</ArgTableRow>
<ArgTableRow arg="repl-bytes" typ="num">回覆方向位元組數。</ArgTableRow>
<ArgTableRow arg="repl-fasttrack-packets" typ="num">回覆方向 fasttrack 封包數量。</ArgTableRow>
<ArgTableRow arg="repl-fasttrack-bytes" typ="num">回覆方向 fasttrack 位元組數。</ArgTableRow>
<ArgTableRow arg="orig-rate" typ="num">原始方向速率。</ArgTableRow>
<ArgTableRow arg="repl-rate" typ="num">回覆方向速率。</ArgTableRow>
</ArgTable>
