---
sidebar_key: "cli-reference/ipv6/nd"
title: "nd"
sidebar_label: 'nd'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/nd
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/nd {#ipv6nd}
**型別：** 目錄

已配置 IPv6 鄰居發現（ND）協定。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">已停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum { all:0 }">
執行鄰居發現的介面。
-all - 在所有正在執行的介面上執行 ND。
</ArgTableRow>
<ArgTableRow arg="ra-interval" typ="super { min: time [3 .. 1250]
, [max] -time [4 .. 1800]
 }">允許從該介面傳送的未經請求的多播路由器通告之間的最小和最大間隔。</ArgTableRow>
<ArgTableRow arg="ra-delay" typ="time">從該介面傳送的多播路由器通告之間的最小時間。</ArgTableRow>
<ArgTableRow arg="mtu" typ="alt { special: enum (unspecified) { unspecified:0 }
, value: num
 }">
路由器通告中的 MTU 選項可確保當鏈路 MTU 未知時，鏈路上的所有節點使用相同的 MTU 值。
- **unspecified** - 不傳送 MTU 選項。
</ArgTableRow>
<ArgTableRow arg="reachable-time" typ="alt { special: enum (unspecified) { unspecified:0 }
, value: time [ .. 3600]
 }">RouterOS 在收到可達性確認後假定鄰居可達的時間。由鄰居不可達檢測使用（參見 [RFC 4861](https://tools.ietf.org/html/rfc4861) 第 7.3 節）。</ArgTableRow>
<ArgTableRow arg="retransmit-interval" typ="alt { special: enum (unspecified) { unspecified:0 }
, value: time
 }">重傳的鄰居請求訊息之間的時間。用於地址解析和鄰居不可達檢測（參見 [RFC 4861](https://tools.ietf.org/html/rfc4861) 第 7.2 和 7.3 節）。</ArgTableRow>
<ArgTableRow arg="ra-lifetime" typ="alt { special: enum (none) { none:0 }
, value: time [ .. 9000]
 }">設定 RA 生存期。生存期為 0 表示此路由器不是預設路由器。參見 [RFC 4861](https://tools.ietf.org/html/rfc4861) 第 6.2.1 節。</ArgTableRow>
<ArgTableRow arg="ra-preference" typ="enum (low | medium | high)">指定在路由器通告中傳達給 IPv6 主機的路由器優先順序。`ra-preference` 值可幫助主機選擇用於到達遠端目的地的預設路由器。</ArgTableRow>
<ArgTableRow arg="hop-limit" typ="alt { special: enum (unspecified) { unspecified:0 }
, value: num [ .. 255]
 }">為出站單播封包的 IPv6 頭部中的 Hop Count 欄位設定的預設值。</ArgTableRow>
<ArgTableRow arg="advertise-mac-address" typ="bool">設定後，在路由器通告中包含出站介面的鏈路層地址。</ArgTableRow>
<ArgTableRow arg="advertise-dns" typ="enum (no | yes | self)">
使用 RADVD 重新分發 DNS 伺服器資訊。

- `no` - 不通告 DNS 伺服器。
- `yes` - 通告路由器上安裝的 DNS 伺服器。
- `self` - 將介面鏈路本地地址通告為 DNS 服務提供者。
</ArgTableRow>
<ArgTableRow arg="managed-address-configuration" typ="bool">指示主機是否應使用有狀態自動配置（DHCPv6）來獲取地址。參見 [RFC 3315](https://tools.ietf.org/html/rfc3315)。</ArgTableRow>
<ArgTableRow arg="other-configuration" typ="bool">指示主機是否應使用有狀態自動配置來獲取除地址之外的附加資訊。參見 [RFC 3315](https://tools.ietf.org/html/rfc3315)。</ArgTableRow>
<ArgTableRow arg="dns" typ="multi { address: address (flags=6)
 }">指定主機為配置 DNS 伺服器而接收的一個或多個 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="pref64" typ="object { pref64: ip6Prefix
 }">指定主機作為 NAT64 字首接收的一個或多個位於 /32、/40、/48、/56、/64 或 /96 子網內的 IPv6 字首。</ArgTableRow>
</ArgTable>
