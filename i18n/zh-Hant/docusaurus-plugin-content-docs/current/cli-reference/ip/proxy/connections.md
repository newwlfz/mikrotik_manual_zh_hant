---
sidebar_key: "cli-reference/ip/proxy/connections"
sidebar_position: 5
title: "connections"
sidebar_label: 'connections'
source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy/connections
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/connections {#ipproxyconnections}
**型別：** 目錄

Web Proxy 的已開啟連線。來自用戶端的每個連線和到伺服器的每個連線各佔一行。代理在收到響應後會保持到伺服器的連線開啟，並將其用於後續請求。有關概述，請參閱 [Web 代理](../../../network-management/proxy/web-proxy.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="S" typ="server">server。從代理到伺服器的連線。</ArgTableRow>
<ArgTableRow arg="C" typ="client">client。從用戶端到代理的連線。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="src-address" typ="alt { ip4: ipAddr
, ip6: ip6Addr
 }">該連線所服務的用戶端地址。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ip4: ipAddr
, ip6: ip6Addr
 }">伺服器的地址。</ArgTableRow>
<ArgTableRow arg="last-protocol" typ="enum (HTTP/1.0 | HTTP/1.1 | FTP) { HTTP/1.0:1, HTTP/1.1:2, FTP:3 }">連線上最後一個請求的協定：`HTTP/1.0`、`HTTP/1.1` 或 `FTP`。</ArgTableRow>
<ArgTableRow arg="state" typ="enum (rx-header | resolving | connecting | waiting | rx-body | tx-header | tx-body | idle) { rx-header:0, resolving:1, connecting:2, waiting:3, rx-body:4, tx-header:5, tx-body:6, idle:7 }">
連線的狀態，例如：
- `waiting` - 用戶端連線等待來自伺服器的響應。
- `rx-header` - 伺服器連線接收響應的頭部。
- `idle` - 伺服器連線已開啟且沒有請求。
</ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num">路由器在此連線上傳送的位元組數。</ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num">路由器在此連線上接收的位元組數。</ArgTableRow>
</ArgTable>
