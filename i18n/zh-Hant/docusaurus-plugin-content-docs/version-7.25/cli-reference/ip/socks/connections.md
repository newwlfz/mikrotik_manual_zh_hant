---
sidebar_key: "cli-reference/ip/socks/connections"
sidebar_position: 2
title: "connections"
sidebar_label: 'connections'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/socks/connections
captured_at: '2026-11-01T21:24:26+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/socks/connections {#ipsocksconnections}
**型別：** 目錄

活動代理連線的只讀列表。在代理連線開啟期間，會存在一個條目。有關更多資訊，請參閱 [SOCKS](../../../network-management/socks/index.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="composite { address: alt { addr-ipv4: ipAddr
, addr-ipv6: ip6Addr
 }
, port: num
 }">SOCKS 用戶端的地址和埠。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { address: alt { addr-ipv4: ipAddr
, addr-ipv6: ip6Addr
, addr-domain: string
 }
, port: num
 }">所請求的目標地址和埠。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (unknown | out | in) { unknown:0, out:1, in:2 }">
連線型別。
- `unknown` - 連線剛剛發起。
- `out` - 連線正在被中繼到所請求的目標。
- `in` - 連線是傳入的。
</ArgTableRow>
<ArgTableRow arg="tx" typ="num">在此連線上中繼到目標的位元組數。</ArgTableRow>
<ArgTableRow arg="rx" typ="num">在此連線上從目標接收的位元組數。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="user" typ="enum">用戶端進行身份驗證所使用的 [`users`](./users.md) 中的使用者名稱。當 `auth-method=none` 時為空。</ArgTableRow>
</ArgTable>
