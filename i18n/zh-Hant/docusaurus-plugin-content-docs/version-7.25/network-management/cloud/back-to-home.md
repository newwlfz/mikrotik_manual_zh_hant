---
sidebar_key: "network-management/cloud/back-to-home"
sidebar_position: 1
title: "Back To Home（遠端回家）"
sidebar_label: "Back To Home"
description: "Back To Home 可將 RouterOS 裝置變為可從任何位置訪問的 WireGuard VPN 伺服器，即使位於 NAT 之後也可透過 MikroTik 中繼訪問。使用手機應用進行設定，與他人和計算機共享隧道，或在 RouterOS 中管理使用者。"
tags:
  - 'cloud'
  - 'back-to-home'
  - 'vpn'
source: https://manual.mikrotik.com/docs/7.25/network-management/cloud/back-to-home
captured_at: '2026-11-04T11:25:56+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
Back To Home 可在搭載 ARM、ARM64 或 TILE CPU 的裝置上執行，需要 RouterOS 7.12 及更高版本。
:::

Back To Home 會把路由器變成 WireGuard VPN 伺服器，讓你可以從任何地方訪問它，即使路由器沒有公網 IP 地址或位於 NAT 之後。你可以使用 Back To Home 應用（[Android](https://play.google.com/store/apps/details?id=com.mikrotik.android.freevpn)、[iPhone](https://apps.apple.com/lv/app/mikrotik-back-to-home/id6450679198)）進行設定，該應用還可以與其他人和計算機共享訪問許可權。

當路由器有公網 IP 地址時，手機直接連線到它。否則，連線會經由 MikroTik 中繼伺服器。這兩種情況下連線都是端到端加密的，中繼無法讀取流量（參見[路由器如何連線到雲](./index.md#how-the-router-reaches-the-cloud)）。透過中繼時，速度可能較低。你的流量會從你的路由器發往網際網路，因此網站看到的是你的家庭地址。

Back To Home 旨在實現對家庭網路的簡單訪問，而不是用於匿名。若要對 VPN 訪問進行更精細的控制，請自行配置 [WireGuard](../../virtual-private-networks/wireguard.md)。

## 使用應用設定 Back To Home {#set-up-back-to-home-with-the-app}

你需要一部安裝了 Back To Home 應用的手機，並連線到路由器的本地網路，例如其 Wi-Fi。

1. 將手機連線到路由器的 Wi-Fi 網路。
2. 開啟 Back To Home 應用。
3. 選擇 **Create new**。
4. 輸入路由器的本地 IP 地址（預設配置中為 `192.168.88.1`）、路由器的使用者名稱和密碼，然後選擇 **Connect**。
5. 輸入隧道的名稱，然後選擇 **Create tunnel**。
6. 允許手機新增 VPN 配置。

隧道已就緒。斷開與路由器 Wi-Fi 的連線，然後在應用中選擇 **Connect**，即可從任何其他網路（例如移動資料）開啟隧道。

| ![Back To Home 應用起始介面，帶有 Create new 按鈕](/img/6264d45373704811.webp) | ![Create tunnel 介面，包含路由器地址、使用者名稱和密碼欄位](/img/006392895dc00a62.webp) | ![應用已連線到路由器，並詢問隧道名稱](/img/f410b5c8e4fbc964.webp) | ![手機請求允許新增 VPN 配置](/img/aa81c2e520c6ef66.webp) | ![錯誤訊息：此裝置不支援 Back To Home](/img/8e9ea14b99f4ed8b.webp) |
| :-- | :-- | :-- | :-- | :-- |
| 選擇 **Create new** | 輸入路由器地址和憑據 | 為隧道命名 | 允許 VPN 配置 | 不支援 Back To Home 的裝置上出現錯誤 |

## 與他人共享隧道 {#share-the-tunnel-with-other-people}

你可以為朋友和家人建立帶到期日期的訪客隧道。對於每個訪客隧道，你可以選擇對方是能訪問你的家庭網路，還是隻能透過你的路由器使用網際網路。對方需要安裝 Back To Home 應用。

1. 連線到自己的隧道。
2. 在隧道旁選擇 **...**，然後選擇 **Manage shares**。
3. 輸入路由器的使用者名稱和密碼。應用會更改路由器配置。
4. 選擇 **Create**。
5. 輸入訪客隧道的名稱，例如對方的姓名。
6. 設定到期日期。
7. 如果對方應能訪問你的本地網路，請開啟 **Home network access**。如果僅用於網際網路訪問，請保持關閉。
8. 選擇 **Create tunnel**。手機的分享面板會開啟。
9. 傳送邀請連結，例如透過聊天應用傳送。

當對方開啟連結時，Back To Home 應用會開啟並新增隧道，或先請對方安裝應用。若要當面邀請某人，請在共享項旁選擇 **...**，然後選擇 **View QR invite**。

| ![隧道選單，包含 Edit 和 Manage shares 項](/img/5fce1b68f8bd3617.webp) | ![Manage shares 請求輸入路由器使用者名稱和密碼](/img/0a9d02f5b8733988.webp) | ![共享管理器，尚無共享隧道](/img/17067b05d75b75d9.webp) | ![共享表單，包含隧道名稱、到期日期和家庭網路訪問](/img/b5756e5046aba347.webp) | ![用於 Back To Home 邀請連結的手機分享面板](/img/affcadf2f50e7495.webp) | ![邀請連結已貼上到聊天應用中](/img/4e48e6aaec7f79a0.webp) |
| :-- | :-- | :-- | :-- | :-- |  :-- |
| 選擇 **Manage shares** | 輸入路由器憑據 | 選擇 **Create** | 為共享命名並設定其訪問許可權 | 分享面板開啟 | 傳送邀請連結 |

## 使用 WireGuard 應用連線計算機 {#connect-a-computer-with-the-wireguard-app}

Back To Home 應用僅適用於手機。在計算機上，請使用 [WireGuard 應用](https://www.wireguard.com/install/) 以及你為自己建立的共享：

1. 按上一節所述為計算機建立共享。
2. 在新共享旁選擇 **...**，然後選擇 **Share WireGuard config file**。
3. 將檔案傳送到計算機，例如使用 AirDrop 或作為電子郵件附件傳送。
4. 在計算機上的 WireGuard 應用中，選擇 **Import Tunnel(s) from File** 並選擇該檔案。

| ![共享管理器，包含一個共享和 Create 按鈕](/img/46d1d2abcf921af8.webp) | ![用於計算機的共享表單，沒有到期日期並啟用了家庭網路訪問](/img/ff48e9c096c9478d.webp) | ![共享管理器，包含兩個共享](/img/e68860cd498d3695.webp) | ![共享選單，包含 Share URL invite、View QR invite 和 Share WireGuard config file 項](/img/667f7d8123a9bebb.webp) | ![用於 WireGuard 配置檔案的手機分享面板](/img/194bff3a2acfef27.webp) | ![macOS 上的 WireGuard 應用，包含 Import Tunnel(s) from File 選單項](/img/96cd7f04a76dc084.webp) |
| :-- | :-- | :-- | :-- | :-- |  :-- |
| 選擇 **Create** | 為共享命名並設定其訪問許可權 | 列表中的新共享 | 選擇 **Share WireGuard config file** | 將檔案傳送到計算機 | 在 WireGuard 應用中匯入該檔案 |

## 在 RouterOS 中管理 Back To Home {#manage-back-to-home-in-routeros}

使用應用時，你無需在 RouterOS 中配置任何內容。如果不使用應用，例如僅連線一臺計算機，請先啟用 Back To Home：

```ros
/ip/cloud/set back-to-home-vpn=enabled
```

等待 `/ip/cloud/print` 顯示 `vpn-status: running`，這需要幾秒鐘。在此之前，新增使用者會失敗並提示 `back-to-home vpn not enabled`。然後新增使用者並列印其配置：

```ros
/ip/cloud/back-to-home-user/add name=laptop allow-lan=yes
/ip/cloud/back-to-home-user/show-client-config [find name=laptop]
```

最後一條命令會列印該使用者的 WireGuard 配置及其二維條碼。在裝置上的 [WireGuard 應用](https://www.wireguard.com/install/) 中匯入它：

```text
 # Name = laptop
 # CloudDDNS = hf1234abcd5.sn.mynetname.net
 [Interface]
 PrivateKey = <private key of the user>
 Address = 192.168.216.3/32, fc00:0:0:216::3/128
 MTU = 1420
 [Peer]
 PublicKey = <vpn-public-key of the router>
 AllowedIPs = 0.0.0.0/0, ::/0
 Endpoint = hf1234abcd5.vpn.mynetname.net:24957
 PersistentKeepalive = 30
 [Peer]
 PublicKey = //////////////////////////////////////////8=
 AllowedIPs = 0.0.0.0/32
 Endpoint = hf1234abcd5.sn.mynetname.net:24957
 PersistentKeepalive = 15
```

第一個 peer 是路由器。第二個 peer 使用佔位金鑰，不承載流量。

每個使用者都是獨立的 WireGuard 用戶端，擁有自己的金鑰和地址：

- `allow-lan=no`（預設值）使使用者只能透過路由器訪問網際網路。設定為 `yes` 時，使用者還可以訪問你的本地網路。
- `client-allowed-address` 限制用戶端透過隧道傳送的流量範圍，例如 `client-allowed-address=192.168.88.0/24` 表示僅訪問本地網路。預設情況下，用戶端透過隧道傳送所有流量。
- `client-dns` 設定用戶端配置中的 DNS 伺服器。
- `expires` 可接受 `never`、日期或時間間隔（例如 `7d`）。建立使用者後無法更改該值：請改為重新建立使用者。

## 關閉 Back To Home {#turn-off-back-to-home}

應用會將隧道新增到手機的 VPN 設定中。要從手機中移除隧道，請在手機的 VPN 設定中將其刪除。這不會更改路由器。

要在路由器上關閉 Back To Home：

```ros
/ip/cloud/set back-to-home-vpn=revoked-and-disabled
```

路由器會刪除所有 Back To Home 使用者並吊銷金鑰。再次啟用 Back To Home 時，路由器會建立新金鑰和新埠，因此你需要重新設定每部手機和每臺計算機。

## 技術細節 {#technical-details}

### Back To Home 向路由器新增的內容 {#what-back-to-home-adds-to-the-router}

當你透過應用或使用 `/ip/cloud/set back-to-home-vpn=enabled` 啟用 Back To Home 時，RouterOS 會新增：

- 一個名為 `back-to-home-vpn` 的 WireGuard 介面，它監聽 `/ip/cloud` 中 `vpn-port` 顯示的 UDP 埠。
- 該介面上的地址 192.168.216.1/24 和 fc00:0:0:216::1/64。每個用戶端會從這些網路中獲得接下來的可用地址。
- IPv4 和 IPv6 的動態防火牆規則：一條接受 WireGuard 埠的 input 規則，一條針對來自隧道的流量進行 masquerade 的規則，以及一條丟棄受限使用者發往 `LAN` 介面列表的流量的 forward 規則。
- DNS 名稱 `<serial number>.vpn.mynetname.net`，用戶端將其用作端點。它會解析為路由器的公網地址，或路由器使用的中繼。使用預設值 `ddns-enabled=auto` 時，DDNS 也會開啟。

IPv6 地址 fc00:0:0:216::1/64 使用 `advertise=yes` 建立。路由器是否在隧道介面上為其傳送路由器通告取決於 `/ipv6/nd` 設定。

僅可使用網際網路的使用者（`allow-lan=no`）位於動態地址列表 `back-to-home-lan-restricted-peers` 中。該限制依賴於預設配置中的 `LAN` 介面列表，因此請將你的本地介面保留在該列表中。

吊銷會移除 `back-to-home-vpn` 介面及其 peer、地址和防火牆規則，以及所有使用者，並請求雲伺服器刪除 `vpn.mynetname.net` 名稱。

### 直連和中繼連線 {#direct-and-relayed-connections}

`/ip/cloud` 中的 `vpn-relay-ipv4-status` 和 `vpn-relay-ipv6-status` 顯示用戶端如何到達路由器。狀態為 `reachable directly` 時，`vpn.mynetname.net` 名稱會解析為路由器的公網地址，用戶端直接連線到路由器本身。狀態為 `reachable via relay` 時，該名稱會解析為中繼，由中繼轉發加密流量。File Share 會單獨決定：它可以使用中繼，而 Back To Home 同時直連，例如當 `www-ssl` 使用 TCP 埠 443 時（參見 [檔案共享](./file-share.md)）。

Back To Home 應用建立的隧道是 `/ip/cloud/back-to-home-user` 中的使用者。應用會將 `name` 設定為手機的型號識別符號，例如 `iPhone18,1`，並將 comment 設定為應用中顯示的隧道名稱。

### 用戶端配置 {#client-configuration}

以 `#` 開頭的行是註釋，因為 WireGuard 配置沒有用於隧道名稱的欄位。`# Name` 攜帶使用者的註釋；如果使用者沒有註釋，則攜帶其名稱。Back To Home 應用在匯入配置時會將 `# Name` 用作隧道名稱。其他 WireGuard 用戶端會忽略這些行，因此同一配置可在任何 WireGuard 應用中使用。

用戶端配置中的第二個 peer 使用佔位金鑰和 `AllowedIPs = 0.0.0.0/32`，因此不承載流量。用戶端即使沒有它也能連線，透過中繼時也是如此。

`/ip/cloud` 還在 `vpn-wireguard-client-config` 和 `vpn-wireguard-client-config-qrcode` 中提供內建用戶端配置。它一次只能用於一臺裝置，因為 WireGuard 透過金鑰識別用戶端。若要用於更多裝置，請為每臺裝置新增一個使用者。

### 與雲伺服器通訊 {#contact-with-the-cloud-server}

啟用 Back To Home 需要幾秒鐘，期間路由器會聯絡雲伺服器：`vpn-status` 會從 `checking rtt` 變為 `running`。

吊銷會立即移除路由器上的所有內容，即使雲伺服器沒有響應（`/ip/cloud` 中的 `status` 顯示 `failed to connect`）。此時 `vpn.mynetname.net` 和 `sn.mynetname.net` 名稱會保持註冊狀態，直到雲伺服器收到刪除請求。要刪除它們，請在路由器能夠訪問雲伺服器時啟用 Back To Home，然後再次吊銷。

有關所有屬性，請參閱 CLI 參考中的 [`/ip/cloud`](../../cli-reference/ip/cloud/index.md) 和 [`/ip/cloud/back-to-home-user`](../../cli-reference/ip/cloud/back-to-home-user/index.md)。
