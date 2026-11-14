---
sidebar_key: "cli-reference/interface/gre"
sidebar_position: 10
title: "gre"
sidebar_label: 'gre'
source: https://manual.mikrotik.com/docs/cli-reference/interface/gre
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/gre {#interfacegre}
**型別：** 目錄

[Generic Routing Encapsulation (GRE)](../../virtual-private-networks/gre.md) 是一種隧道協定，最初由 Cisco 開發，用於透過 IP 網路封裝各種網路層協定。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">隧道的名稱。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">隧道的 Layer3 最大傳輸單元。預設值：`auto` — 路由器從出介面 MTU 中減去 24 位元組的 GRE/IP 開銷（在 1500 位元組介面上 actual-mtu 為 1476）。</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">用於本地隧道端的 IP 地址。如果設定為 0.0.0.0，則使用出介面的 IP 地址。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=4Dv)" mandatory="1">遠端隧道端的 IP 地址。</ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { keepalive-interval: time [1 .. ]
, [keepalive-retries] [ ,num [1 .. ]]
 }">
keepalive 引數設定路由器檢查隧道遠端的頻率：路由器每隔 `KeepaliveInterval` 秒向遠端傳送 GRE 回顯探測，最多重複 `KeepaliveRetries` 次。最小間隔為 1 秒，0 秒設定會被拒絕；取消設定 `keepalive` 會將其關閉，但在當前 RouterOS 上這不會改變 running-flag 行為。預設情況下 keepalive 設定為 10 秒和 10 次重試。在當前 RouterOS 上，隧道在啟用期間會保持 running 標誌，即使遠端停止應答；隨後隧道流量會被丟棄，直到遠端再次響應。
引數按以下格式寫入：`KeepaliveInterval,KeepaliveRetries`
其中 KeepaliveInterval 是時間間隔，KeepaliveRetries 是重試次數。
</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">封包的 DSCP 值。Inherited 表示 DSCP 值繼承自隧道傳輸的流量。</ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool">控制是否更改收到的 TCP SYN 封包的 MSS 大小。啟用後，如果當前 MSS 大小超過隧道介面 MTU（考慮 TCP/IP 開銷），路由器會更改收到的 TCP SYN 封包的 MSS 大小。收到的封裝封包仍包含原始 MSS，只有在解封裝後才會更改 MSS。</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool">
是否在相關封包中包含 DF 位。預設值：`no` — 在 RouterOS 7 上 `yes` 會被拒絕，只有 `no` 和 `inherit` 有效。
- `no` - 如需要則進行分片。
- `inherit` - 使用原始封包的 DF 標誌。
</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security">指定 secret 後，路由器會向 remote-address 新增動態 IPsec 對等體，並帶有預共享金鑰和策略（預設情況下，phase2 使用 sha1/aes128cbc）。</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">是否允許 FastPath 處理。如果使用 IPsec 隧道，則必須停用。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num">隧道的實際最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ipAddr">遠端的當前 IP 地址。</ArgTableRow>
</ArgTable>
