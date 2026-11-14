---
sidebar_key: "cli-reference/ipv6/nd/proxy"
sidebar_position: 2
title: "proxy"
sidebar_label: 'proxy'
source: https://manual.mikrotik.com/docs/cli-reference/ipv6/nd/proxy
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/nd/proxy {#ipv6ndproxy}
**型別：** 目錄

IPv6 Neighbor Discovery 代理允許路由器或主機代表另一個節點響應 Neighbor Discovery（[RFC 4861](https://tools.ietf.org/html/rfc4861)）訊息。這使得不同網段之間的通訊就像它們位於同一鏈路上一樣。在 RouterOS 中，該代理可以針對單個 IPv6 地址啟用，並按介面生效。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="ip6Addr">代理接管的 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">代理針對該 IPv6 地址執行所在的介面。</ArgTableRow>
</ArgTable>
