---
sidebar_key: "cli-reference/interface/wireguard"
title: "wireguard"
sidebar_label: 'wireguard'
source: https://manual.mikrotik.com/docs/cli-reference/interface/wireguard
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/wireguard {#interfacewireguard}
**型別：** 目錄

[WireGuard](../../../virtual-private-networks/wireguard.md) 在對等節點之間建立由公鑰標識的加密 IP 隧道。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">專案是否被停用。</ArgTableRow>
<ArgTableRow arg="R" typ="running">介面是否正在執行。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">隧道的名稱。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer3 最大傳輸單元。</ArgTableRow>
<ArgTableRow arg="listen-port" typ="num">WireGuard 服務用於監聽傳入會話的埠。</ArgTableRow>
<ArgTableRow arg="private-key" typ="string">base64 私鑰。如果未指定，則在建立介面時自動生成。每個網路介面都有一個私鑰和一個對等節點列表。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">指定 WireGuard UDP 套接字使用哪個 VRF 來確定加密封包的傳送或接收方式。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="public-key" typ="string">根據私鑰計算得出的 base64 公鑰。公鑰用於對等節點之間相互認證。</ArgTableRow>
</ArgTable>
