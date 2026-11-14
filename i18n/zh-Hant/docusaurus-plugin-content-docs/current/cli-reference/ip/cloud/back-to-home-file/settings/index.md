---
sidebar_key: "cli-reference/ip/cloud/back-to-home-file/settings"
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/cli-reference/ip/cloud/back-to-home-file/settings
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/cloud/back-to-home-file/settings {#ipcloudback-to-home-filesettings}
**系統能力：** cloud-vpn
**型別：** 設定目錄

File Share 服務的狀態：其 DNS 名稱、證書以及與中繼伺服器的連線。該服務在 [`/ip/cloud/back-to-home-file`](../index.md) 中建立第一個共享時啟動，並在最後一個共享被移除時停止。有關說明，請參閱 [File Share 的工作原理](../../../../../network-management/cloud/file-share.md#how-file-share-works)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="prefer-relay-code" typ="string">要優先使用的中繼區域程式碼，取自 `relay-regions`，例如 `EUR1`。為空時，路由器會根據往返時間（`relay-rtts`）選擇中繼。預設值：空。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">當至少存在一個共享且服務執行時為 `yes`。移除最後一個共享後變為 `no`。</ArgTableRow>
<ArgTableRow arg="dns-name" typ="string">共享提供服務所使用的名稱：`<serial>.routingthecloud.net`，其中序列號為小寫。當路由器使用中繼時，該名稱會解析到中繼。</ArgTableRow>
<ArgTableRow arg="status" typ="string">
服務狀態，例如：
- `getting cert status: requesting SSL certificate`、`requesting validation`、`requesting authorization`、`requesting order finalization` - 路由器正在獲取 Let's Encrypt 證書。
- `running` - 服務正在執行。
</ArgTableRow>
<ArgTableRow arg="relay-rtts" typ="multi { code: string
 }">透過 IPv4 和 IPv6 到每個中繼區域的往返時間，例如 `EUR1 (ip4: 1.103ms, ip6: timeout)`。</ArgTableRow>
<ArgTableRow arg="relay-ipv4-status" typ="string">透過 IPv4 與中繼的連線，例如 `connected (region: EUR1 ip: <relay address> rtt: 1.103ms reachable: unknown )`。</ArgTableRow>
<ArgTableRow arg="relay-ipv6-status" typ="string">透過 IPv6 與中繼的連線，例如路由器測量往返時間時的 `testing rtt`。</ArgTableRow>
<ArgTableRow arg="relay-regions" typ="multi { code: string
 }">路由器可以使用的中繼區域，例如 `EUR1` 和 `USA1`。在 `prefer-relay-code` 中使用此列表中的程式碼。</ArgTableRow>
<ArgTableRow arg="relay-addresses" typ="multi { address: ipAddr
 }">中繼伺服器的 IPv4 地址，每個區域一個。</ArgTableRow>
<ArgTableRow arg="relay-addresses-ipv6" typ="multi { address: ip6Addr
 }">中繼伺服器的 IPv6 地址，每個區域一個。</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)">共享使用的證書，位於 `/certificate` 中的 `fileshare-<serial>.routingthecloud.net`。執行 `remove-certificate` 後為 `none`。</ArgTableRow>
</ArgTable>
