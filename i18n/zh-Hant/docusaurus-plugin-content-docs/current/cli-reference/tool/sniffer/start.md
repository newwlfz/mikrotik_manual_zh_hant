---
sidebar_key: "cli-reference/tool/sniffer/start"
sidebar_position: 7
title: "start"
sidebar_label: 'start'
source: https://manual.mikrotik.com/docs/cli-reference/tool/sniffer/start
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/sniffer/start {#toolsnifferstart}
**型別：** 命令

使用 [`/tool/sniffer`](./index.md) 中的設定啟動嗅探器。過濾引數是不帶 `filter-` 字首的 `filter-*` 設定（`interface`、`ip-address`、`port`、`ip-protocol`），以及用於 `filter-vlan` 的 `vlan-id`。使用過濾引數時，本次執行僅使用給定的過濾器；已儲存的過濾器不適用，也不會改變。嗅探器執行期間，路由器會關閉 IPv4 fast path，並隨之關閉 FastTrack。捕獲的封包在 [`stop`](./stop.md) 後會保留在記憶體中，供 [`packet`](./packet.md)、[`protocol`](./protocol.md)、[`host`](./host.md) 和 [`connection`](./connection.md) 使用，保留 10 分鐘或直到下一次啟動。參見 [封包嗅探器](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="object { interface: iface_enum
 }">本次執行中要嗅探的介面。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">最多 16 個 MAC 地址，或帶掩碼的 MAC 地址；當幀的源 MAC 地址或目的 MAC 地址匹配時，該幀即匹配。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">最多 16 個源 MAC 地址，或帶掩碼的 MAC 地址。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="object { mac-address-element: super { !
, mac-address-with-mask: composite { mac: macAddr
, mask: [ macAddr]
 }
 }
 }">最多 16 個目的 MAC 地址，或帶掩碼的 MAC 地址。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="object { mac-protocol-element: super { !
, protocol: alt { mac-protocol: enum ()
, protocol-number: num [ .. 65535]
 }
 }
 }">最多 16 個 MAC（L2）協定，可按名稱或編號（0..65535）指定，例如 `ip`、`arp`、`ipv6` 或 `802.2`。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="object { ip-protocol-element: super { !
, ip-protocol: enum ()
 }
 }">最多 16 個 IP 或 IPv6 協定，可按名稱或編號指定，例如 `icmp`、`tcp` 或 `udp`。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">最多 16 個 IPv4 地址或字首；當封包的源地址或目的地址匹配時，該封包即匹配。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="src-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">最多 16 個源 IPv4 地址或字首。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="dst-ip-address" typ="object { ip-address-element: super { !
, ip-address-with-mask: composite { ip: ipAddr
, mask: [ num [ .. 32]]
 }
 }
 }">最多 16 個目的 IPv4 地址或字首。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">最多 16 個 IPv6 字首；當封包的源地址或目的地址匹配時，該封包即匹配。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="src-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">最多 16 個源 IPv6 字首。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="dst-ipv6-address" typ="object { ipv6-address-element: super { !
, ipv6-prefix: ip6Prefix
 }
 }">最多 16 個目的 IPv6 字首。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="port" typ="object { port-element: super { !
, port: enum ()
 }
 }">最多 16 個埠，可按編號或名稱（如 `ssh` 或 `telnet`）指定；當封包的源埠或目的埠匹配時，該封包即匹配。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="src-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">最多 16 個源埠，可按編號或名稱指定。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="object { port-element: super { !
, port: enum ()
 }
 }">最多 16 個目的埠，可按編號或名稱指定。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="object { vlan-element: super { !
, vlan: num [ .. 4095]
 }
 }">最多 16 個 VLAN ID（0..4095）。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="direction" typ="enum (any | tx | rx) { any:0, tx:1, rx:2 }">
本次執行中要捕獲的方向。
- `any`（預設）- 接收和傳送的封包。
- `rx` - 接收的封包。它們在防火牆之前被捕獲，因此被防火牆規則丟棄的封包仍會被捕獲。
- `tx` - 傳送的封包，在防火牆之後捕獲。
</ArgTableRow>
<ArgTableRow arg="operator-between-entries" typ="enum (or | and) { or:0, and:1 }">
本次執行中，一個過濾器的各個條目如何組合。
- `or`（預設）- 當封包匹配過濾器的任意一個條目時，該封包即匹配該過濾器。
- `and` - 僅當封包匹配過濾器的所有條目時，該封包才匹配該過濾器。
</ArgTableRow>
<ArgTableRow arg="cpu" typ="object { cpu-element: super { !
, cpu: num
 }
 }">處理該封包的 CPU 核心。在條目前面加上 `!` 可將其取反。</ArgTableRow>
<ArgTableRow arg="size" typ="object { size-element: super { !
, size-range: range [0 .. 65535]
 }
 }">封包大小或以位元組為單位的大小範圍（0..65535），例如 `1000-1500`。在條目前面加上 `!` 可將其取反。</ArgTableRow>
</ArgTable>
