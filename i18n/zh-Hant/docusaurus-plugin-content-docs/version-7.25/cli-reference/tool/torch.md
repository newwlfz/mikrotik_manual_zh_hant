---
sidebar_key: "cli-reference/tool/torch"
sidebar_position: 23
title: "torch"
sidebar_label: 'torch'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/torch
captured_at: '2026-11-01T21:26:01+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/torch {#tooltorch}
**型別：** 命令

顯示當前經過某個介面的流量，按地址、協定、埠和 DSCP 分組為流，並顯示每個流在兩個方向上的速率。Torch 會看到防火牆之前的封包，並在執行期間關閉 IP 快速路徑。它會一直執行，直到透過 Ctrl-C 停止，或直到 `duration` 結束。有關示例以及如何閱讀輸出，請參閱 [Torch](../../diagnostics-monitoring-and-troubleshooting/torch.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum">要監視的介面。名稱可以不帶 `interface=` 給出，例如 `/tool/torch bridge`。</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, src-address: ipPrefix
 }">僅顯示其 `src-address` 位於此 IPv4 字首中的流。流的 `src-address` 是介面遠端一側的地址，即介面接收其流量的一側。預設值：any。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, dst-address: ipPrefix
 }">僅顯示其 `dst-address`（流的另一端）位於此 IPv4 字首中的流。預設值：any。</ArgTableRow>
<ArgTableRow arg="src-address6" typ="super { !
, src-address6: ip6Prefix
 }">`src-address` 的 IPv6 字首，即介面遠端一側。預設值：any。</ArgTableRow>
<ArgTableRow arg="dst-address6" typ="super { !
, dst-address6: ip6Prefix
 }">`dst-address` 的 IPv6 字首，即流的另一端。預設值：any。</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="enum (any) { any:3 }">僅顯示此 MAC 協定的流，例如 `ip`。預設值：any。</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (any) { any:256 }">僅顯示此 IP 協定的流，例如 `tcp`。預設值：any。</ArgTableRow>
<ArgTableRow arg="port" typ="enum (any) { any:0 }">僅顯示以此埠作為 `src-port` 或 `dst-port` 的流，可為一個埠或 `any`。該過濾器適用於有埠的流：沒有埠的流（例如 ICMP）仍會顯示。預設值：any。</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="alt { number: num [ .. 4095]
, enum: enum (any) { any:0xffff }
 }">僅顯示具有此 VLAN ID 的幀，`0..4095`，或 `any`。父介面上的帶標籤幀即使沒有此過濾器也會獲得 `VLAN-ID` 列。預設值：any。</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">僅顯示具有此 DSCP 值的流，`0..63`，例如 `46` 表示 Expedited Forwarding。預設值：any。</ArgTableRow>
<ArgTableRow arg="cpu" typ="num">使用 `any` 時，會新增 `CPU` 列：每個處理過某個流的封包的 CPU 佔一行。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="cpu" typ="num">處理該行封包的 CPU。使用 `cpu=any` 時顯示。</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">流的 VLAN ID。在父介面上對帶標籤幀顯示；在 VLAN 介面本身上，幀不帶標籤，因此該列不會出現。</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="enum ()">流的 MAC 協定，例如 `ip`。</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum ()">流的 IP 協定，例如 `tcp`、`udp` 或 `icmp`。</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">流的 DSCP 值。</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }">介面遠端一側的地址：即介面接收其流量的一側，即使會話由路由器發起也是如此。</ArgTableRow>
<ArgTableRow arg="src-port" typ="enum ()">位於 `src-address` 一側的埠，適用於 TCP 和 UDP 流，並顯示其服務名稱。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ip: ipAddr
, ipv6: ip6Addr
 }">流的另一端。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="enum ()">位於 `dst-address` 一側的埠，適用於 TCP 和 UDP 流，並顯示其服務名稱，例如 `2000 (btserv)`。</ArgTableRow>
<ArgTableRow arg="tx" typ="num">介面發往 `src-address` 的流量速率，單位為位元每秒。</ArgTableRow>
<ArgTableRow arg="rx" typ="num">介面從 `src-address` 接收的流量速率，單位為位元每秒。</ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num">介面每秒發往 `src-address` 的封包數。</ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num">介面每秒從 `src-address` 接收的封包數。</ArgTableRow>
</ArgTable>
