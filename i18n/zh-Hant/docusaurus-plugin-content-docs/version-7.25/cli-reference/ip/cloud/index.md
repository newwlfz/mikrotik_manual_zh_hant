---
sidebar_key: "cli-reference/ip/cloud/index"
sidebar_position: 5
title: "cloud"
sidebar_label: 'cloud'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/cloud
captured_at: '2026-11-01T21:23:47+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/cloud {#ipcloud}
**型別：** 設定目錄

MikroTik 雲服務的設定：DDNS 名稱、啟動時的時間更新以及 Back To Home（遠端回家）。路由器透過 UDP 埠 15252 向 `cloud2.mikrotik.com` 傳送請求。有關概述和示例，請參見 [雲](../../../network-management/cloud/index.md) 和 [Back To Home](../../../network-management/cloud/back-to-home.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ddns-enabled" typ="enum (auto | yes)">
路由器是否在雲伺服器上註冊 DNS 名稱（`dns-name`），並使其始終指向路由器的公網地址。
- `auto`（預設）- 僅在啟用 Back To Home（`back-to-home-vpn=enabled`）時 DDNS 才開啟。當 DDNS 關閉時，路由器請求雲伺服器刪除該名稱，該名稱會在幾分鐘內停止解析。
- `yes` - DDNS 始終開啟。在 NAT 之後，路由器每分鐘傳送一次更新。
</ArgTableRow>
<ArgTableRow arg="ddns-update-interval" typ="alt { ddns-update-interval: enum (none) { none:0 }
, ddns-update-interval: time [1m .. ]
 }">路由器向雲伺服器傳送 DDNS 更新的間隔，此外還有路由器自行決定傳送的更新。使用 `none` 時，路由器只發送自己的更新；在 NAT 之後，即每分鐘一次。最小值：1 分鐘。預設值：none。</ArgTableRow>
<ArgTableRow arg="update-time" typ="bool">路由器啟動時是否從雲伺服器設定其時鐘。僅在 NTP 用戶端（`/system/ntp/client`）被停用時才會這樣做，在 `ddns-enabled=auto` 時也是如此，並會記錄 `cloud change time <old> => <new>`。DDNS 更新和 `force-update` 不會設定時鐘。時區由 `/system/clock` 中的 `time-zone-autodetect` 單獨設定。預設值：yes.</ArgTableRow>
<ArgTableRow arg="back-to-home-vpn" typ="enum (revoked-and-disabled | enabled)" syscap="cloud-vpn">
是否執行 Back To Home。
- `revoked-and-disabled`（預設）- Back To Home 已關閉。設定此項會刪除 `back-to-home-vpn` 介面及其對等體、地址和動態防火牆規則，以及 [`back-to-home-user`](./back-to-home-user/index.md) 中的所有使用者，並請求雲伺服器刪除 `vpn-dns-name`。再次啟用 Back To Home 會建立新的金鑰和新埠，因此每個用戶端都需要新的配置。
- `enabled` - 建立 WireGuard 介面 `back-to-home-vpn`，地址為 192.168.216.1/24 和 fc00:0:0:216::1/64，新增動態防火牆和 NAT 規則，註冊 `vpn-dns-name`，並在無法直接訪問路由器時連線到中繼。使用 `ddns-enabled=auto` 時，DDNS 也會開啟。
</ArgTableRow>
<ArgTableRow arg="vpn-prefer-relay-code" typ="string" syscap="cloud-vpn">要使用的中繼區域程式碼，來自 `vpn-relay-regions`，例如 `EUR1`。當它為空時，路由器使用往返時間最低的中繼（`vpn-relay-rtts`）。預設值：空。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="public-address" typ="ipAddr">雲伺服器所看到的路由器公網 IPv4 地址，即路由器請求的源地址。在 NAT 之後，這是 NAT 裝置的地址。在雲伺服器首次回覆後顯示，即使只進行時間更新時也會顯示。</ArgTableRow>
<ArgTableRow arg="public-address-ipv6" typ="ip6Addr">雲伺服器所看到的路由器公網 IPv6 地址。當路由器透過 IPv6 訪問雲伺服器時顯示。</ArgTableRow>
<ArgTableRow arg="dns-name" typ="string">路由器的 DNS 名稱：其序列號的小寫形式後接 `.sn.mynetname.net`。在名稱註冊後顯示。它解析為 `public-address`，或在 [`advanced`](./advanced.md) 中設定 `use-local-address=yes` 時解析為路由器的本地地址，TTL 為 60 秒。</ArgTableRow>
<ArgTableRow arg="status" typ="string">
對雲伺服器最後一次請求的狀態，例如：
- `updating...` - 路由器已傳送請求並正在等待回覆。若無回覆，它會以逐漸增大的間隔持續重試。
- `updated` - 雲伺服器已確認最後一次請求。
- `failed to connect` - 雲伺服器沒有應答。
</ArgTableRow>
<ArgTableRow arg="vpn-dns-name" typ="string" syscap="cloud-vpn">Back To Home 端點的 DNS 名稱：序列號的小寫形式後接 `.vpn.mynetname.net`。它解析為路由器的公網地址，或在無法直接訪問路由器時解析為路由器所使用的中繼。用戶端配置將其用作端點。</ArgTableRow>
<ArgTableRow arg="vpn-port" typ="num" syscap="cloud-vpn">`back-to-home-vpn` WireGuard 介面的 UDP 埠。由路由器在啟用 Back To Home 時選取。</ArgTableRow>
<ArgTableRow arg="vpn-status" typ="string" syscap="cloud-vpn">Back To Home 的狀態，例如 `running`。</ArgTableRow>
<ArgTableRow arg="vpn-relay-rtts" typ="multi { code: string
 }" syscap="cloud-vpn">透過 IPv4 和 IPv6 到每個中繼區域的往返時間，例如 `EUR1(ip4: 0.976ms, ip6: timeout)`。</ArgTableRow>
<ArgTableRow arg="vpn-relay-ipv4-status" typ="string" syscap="cloud-vpn">用戶端透過 IPv4 訪問路由器的方式：當用戶端能連線到路由器的公網地址時為 `reachable directly (region: EUR1 ip: <relay address> rtt: 0.761ms)`，當用戶端透過中繼連線時為 `reachable via relay (region: EUR1 ...)`。</ArgTableRow>
<ArgTableRow arg="vpn-relay-ipv6-status" typ="string" syscap="cloud-vpn">用戶端透過 IPv6 訪問路由器的方式，格式與 `vpn-relay-ipv4-status` 相同，例如路由器沒有 IPv6 網際網路訪問時的 `connecting (...)`。</ArgTableRow>
<ArgTableRow arg="vpn-relay-regions" typ="multi { code: string
 }" syscap="cloud-vpn">路由器可以使用的中繼區域，例如 `EUR1` 和 `USA1`。在 `vpn-prefer-relay-code` 中使用此列表中的程式碼。</ArgTableRow>
<ArgTableRow arg="vpn-relay-addresses" typ="multi { address: ipAddr
 }" syscap="cloud-vpn">中繼伺服器的 IPv4 地址，每個區域一個。</ArgTableRow>
<ArgTableRow arg="vpn-relay-addresses-ipv6" typ="multi { address: ip6Addr
 }" syscap="cloud-vpn">中繼伺服器的 IPv6 地址，每個區域一個。</ArgTableRow>
<ArgTableRow arg="vpn-private-key" typ="string" syscap="cloud-vpn">`back-to-home-vpn` WireGuard 介面的私鑰。</ArgTableRow>
<ArgTableRow arg="vpn-public-key" typ="string" syscap="cloud-vpn">`back-to-home-vpn` WireGuard 介面的公鑰。用戶端配置將其用作路由器對等體的金鑰。</ArgTableRow>
<ArgTableRow arg="vpn-peer-private-key" typ="string" syscap="cloud-vpn">`vpn-wireguard-client-config` 中內建用戶端配置的私鑰。</ArgTableRow>
<ArgTableRow arg="vpn-peer-public-key" typ="string" syscap="cloud-vpn">內建用戶端配置的公鑰。路由器在 `back-to-home-vpn` 上有一個使用此金鑰的動態對等體。</ArgTableRow>
<ArgTableRow arg="vpn-interface" typ="iface_enum" syscap="cloud-vpn">Back To Home 的 WireGuard 介面，即 `back-to-home-vpn`。</ArgTableRow>
<ArgTableRow arg="vpn-wireguard-client-config" typ="string" syscap="cloud-vpn">內建用戶端的 WireGuard 配置，包含地址 192.168.216.2 和 fc00:0:0:216::2 以及路由器使用的 DNS 伺服器。在一臺裝置上的 WireGuard 應用中匯入它。若要更多裝置，請在 [`back-to-home-user`](./back-to-home-user/index.md) 中新增使用者。</ArgTableRow>
<ArgTableRow arg="vpn-wireguard-client-config-qrcode" typ="pic" syscap="cloud-vpn">以二維條碼形式表示的 `vpn-wireguard-client-config`，用於手機上的 WireGuard 應用。</ArgTableRow>
<ArgTableRow arg="warning" typ="string">關於路由器設定的警告，例如 `Router is behind a NAT. Remote connection might not work.` 僅在存在警告時顯示。</ArgTableRow>
</ArgTable>
