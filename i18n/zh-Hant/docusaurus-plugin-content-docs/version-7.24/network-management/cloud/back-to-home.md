---
sidebar_key: "network-management/cloud/back-to-home"
sidebar_position: 1
title: "Back To Home（遠端回家）"
sidebar_label: "Back To Home"
description: "Back To Home 可從任何位置安全地透過 VPN 訪問你的路由器，即使它沒有公網 IP 或位於 NAT 之後。它使用 MikroTik 中繼伺服器進行間接連線，確保端到端加密且不暴露金鑰。該功能同時支援智慧手機應用和手動 RouterOS 配置，包括與訪客共享隧道，或透過 WireGuard 為計算機共享隧道。"
tags:
  - 'cloud'
  - 'back-to-home'
  - 'vpn'
source: https://manual.mikrotik.com/docs/7.24/network-management/cloud/back-to-home
captured_at: '2026-11-03T15:24:31+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/ip/cloud` **所需軟體包：** `routeros`  
**所需 RouterOS 版本：** v7.12 及更新版本  
**硬體要求：** ARM/ARM64/TILE 架構裝置

Back To Home 是一項便捷功能，可讓你的裝置從世界任何地方安全地透過 VPN 訪問你的路由器和網路，即使你的路由器沒有公網 IP 地址、位於 NAT 或防火牆之後。

配置透過 MikroTik Back to Home 應用完成（[Android](https://play.google.com/store/apps/details?id=com.mikrotik.android.freevpn)，[iPhone](https://apps.apple.com/lv/app/mikrotik-back-to-home/id6450679198)）。

如果 VPN 伺服器（你的家庭路由器）有公網 IP 地址，VPN 應用會在手機和路由器之間建立直接 VPN 連線。然而，如果路由器無法從網際網路直接訪問，連線將透過 MikroTik 中繼伺服器建立。連線始終是端到端加密的。中繼伺服器或任何其他裝置都無法訪問加密金鑰。本質上，中繼只幫助你的裝置連線到路由器。連線將顯示為從你的路由器發出，而不是從中繼發出。*如果透過中繼連線，速度可能會受到限制。*

此功能是一個便捷選項，可用於從某些內容不可用的位置訪問你的家庭網路或檢視你所在國家/地區可用的內容。它並非用於匿名；它用於簡單的一鍵訪問你的家庭網路。如需更精細的安全控制，我們建議你使用高階 RouterOS 選項手動配置並保護 VPN 連線。

#### 使用應用啟用 BTH {#enabling-bth-using-the-app}

要設定 Back to Home，你需要一部裝有 BTH 應用的智慧手機，並且應在家中連線到路由器的 WiFi 網路。

- 使用手機連線到路由器的 Wi-Fi。
- 開啟 Back to Home 應用（[Android](https://play.google.com/store/apps/details?id=com.mikrotik.android.freevpn)，[iPhone](https://apps.apple.com/lv/app/mikrotik-back-to-home/id6450679198)）。
- 點選“新建”。
- 輸入路由器的本地 IP 地址（最可能是 `192.168.88.1`）、使用者名稱和密碼，然後點選“連線”。
- 為隧道命名，然後點選“建立隧道”。
- 你的手機將請求允許新增新的 VPN 設定。使用手機 PIN 碼批准。
- 設定完成。現在你可以斷開路由器的 Wi-Fi，並連線到任何其他網路，例如 LTE/5G，或者直接離開家。
- 點選“連線”按鈕可切換所選隧道的連線狀態。

| ![](/img/92c286a69409ae4a.png) | ![](/img/f76d4d2890e0ad03.png) | ![](/img/c031432eb344d15d.png) | ![](/img/058c3ee8a44419ef.png) | ![](/img/a6ecd2514c3ab975.png) |
| :-- | :-- | :-- | :-- | :-- |
| 點選“新建” | 提供路由器憑據 | 已建立連線 | 允許新增 VPN | 如果裝置不受支援，則會顯示錯誤 |

#### 與其他手機使用者共享 BTH 連線 {#sharing-the-bth-connection-with-another-phone-user}

可以為你的朋友和家人建立訪客隧道。你甚至可以指定是否要讓這些人也訪問你的本地網路，還是應限制他們僅透過你的路由器使用網際網路。建立共享隧道後，你可以透過手機上的任何聊天應用傳送邀請連結，或當面給朋友出示二維條碼（這兩種情況下，朋友都必須也安裝 BTH 應用）。如果你想從另一部手機或計算機透過 WireGuard(TM) 應用連線到你的路由器，也可以。只需選擇共享 WireGuard(TM) 配置檔案，然後在 WireGuard(TM) 應用中開啟該檔案。

| ![](/img/e232bdab9ab338c9.png) | ![](/img/6421c4b61331555b.png) | ![](/img/353315d345096ef1.png) | ![](/img/b4c0f951101195d7.png) | ![](/img/738264b205e8ebef.jpg) | ![](/img/6a5bfecaf09f48b8.jpg) |
| :-- | :-- | :-- | :-- | :-- |  :-- |
| 管理共享 | 先連線到你的隧道 | 連線後，建立共享 | 提供名稱和訪問級別 | 共享表單開啟 | 透過 WhatsApp、Signal 等傳送邀請連結 |

要與某人共享你的隧道：

- 作為所有者，連線到你的 BTH 隧道。
- 點選隧道旁邊的“...”圖示，然後點選“管理共享”。
- 輸入路由器的管理密碼，因為你將修改路由器配置。
- 在共享管理器中點選“建立”。
- 在“隧道名稱”中輸入你朋友的名字，因為將為他們建立新隧道。
- 指定這個新訪客隧道的到期日期。
- 指定該使用者是否需要訪問你家的內部網路。如果他們只想使用此隧道訪問網際網路，請不要勾選此項。
- 按下“建立隧道”後，手機的共享表單會開啟。選擇傳送邀請連結的方式。
- 對方點選此連結後，要麼會被引導安裝 BTH 應用，要麼 BTH 應用會開啟，並允許他們在手機上設定這個新的訪客隧道。

#### 透過 WireGuard(TM) 應用與計算機共享 BTH 隧道 {#sharing-the-bth-tunnel-with-a-computer-via-the-wireguardtm-app}

由於 PC 沒有 BTH 應用，你可以使用 [WireGuard(TM) 應用](https://www.wireguard.com/install/)連線到共享隧道。你甚至可以透過“邀請”你的計算機連線，與你自己共享你的連線。

我們來建立一個新的共享，這次是為你自己建立，用於從 PC 使用。

| ![](/img/9d365f253bf85b29.png) | ![](/img/843740bbf52b8610.png) | ![](/img/ba48cd0759804581.png) | ![](/img/22b3243b2607de84.png) | ![](/img/22b3243b2607de84.png) | ![](/img/89fd75da1cb0724b.png) |
| :-- | :-- | :-- | :-- | :-- |  :-- |
| 建立 | 指定名稱和訪問級別 | 你現在有兩個共享 | 點選“...”傳送邀請 | 選擇“共享 WireGuard 配置檔案” | 透過 AirDrop 傳送到你的 macOS，或透過電子郵件傳送該檔案 |

在你的計算機上安裝 WireGuard 應用，然後點選“從檔案匯入隧道”

![](/img/7b87bb190f4a06d9.jpg)

---

#### 在 RouterOS 中手動配置 BTH（可選，如果你沒有智慧手機） {#configuring-bth-manually-in-routeros-optional-if-no-smartphone-is-available-to-you}

:::info
重要提示

請注意，**使用 Back to Home 無需在 RouterOS 中配置任何內容**。只需使用 BTH 應用（見上文）即可啟用。Back to Home 的重點就是避免使用 Winbox 或命令列。以下說明僅用於偵錯或經驗豐富的管理員。
:::

1. 連線到路由器
2. 啟用 DDNS Cloud 服務：``/ip/cloud/set ddns-enabled=yes``
3. 啟用 Back To Home：``/ip/cloud/set back-to-home-vpn=enabled``
4. 列印隧道配置：``/ip/cloud/print``
5. 掃描二維條碼（``vpn-wireguard-client-config-qrcode``），或複製配置（``vpn-wireguard-client-config``），然後在首選的 WireGuard® 用戶端中輸入。同一時間只能有一個用戶端使用此配置。  

   :::warning
配置 Back To Home 後 - 會自動建立一個額外的對等條目，可透過執行命令 *`/ip/cloud/print`* 檢視。這是為了讓 VPN 在裝置無法訪問公網 IP 地址並選擇使用 MikroTik 的中繼伺服器建立連線的情況下正常工作。  
   如果你的裝置可以訪問公網 IP 地址，則生成的對等條目會被忽略：

   ```
   [Peer]
   PublicKey = //////////////////////////////////////////8=
   AllowedIPs = 0.0.0.0/32
   Endpoint = example.com:12345
   PersistentKeepalive = 15 
   ```
   :::

#### 移除和停用連線 {#removing-and-disabling-connections}

在智慧手機應用中，VPN 配置會新增到系統 VPN 設定。因此，Back to Home 應用只充當嚮導。它向作業系統提供所需的配置（這就是 iPhone 會警告你正在更改系統配置的原因）。

要移除已建立的連線，請進入智慧手機的設定應用，並在那裡移除 VPN 連線。

在 MikroTik 路由器側，你應在 Wireguard 選單中手動刪除新增的 Peers。請注意，“revoke-and-disable”按鈕不能用來“暫停”Back to Home 功能的使用。一旦你在 RouterOS 中執行 revoke-and-disable，所有 Peers 將與 Cloud / Relay 伺服器解除關聯，並且你將必須從智慧手機應用重新建立連線。因此，一旦你在 RouterOS 的 IP Cloud 選單中使用了“revoke-and-disable”選項，還需要從 Wireguard 選單中刪除這些 Peers，因為它們無法再次使用。

## 屬性參考 {#property-reference}

### IP Cloud {#ip-cloud}

**子選單：** `/ip/cloud`

Back to Home 與 IP Cloud 共用此選單。Back to Home 引數：

| 屬性 | 描述 |
| :-- | :-- |
| **back-to-home-vpn** (*enabled \| revoked-and-disabled*; Default: **revoked-and-disabled**) | 啟用或撤銷並停用 Back to Home 服務。為使 BTH 正常工作，ddns-enabled 不能設定為 no。 |
| **vpn-dns-name** (*read-only: string*) | 顯示分配給裝置的 DNS 名稱。該名稱由產品序列號加上 *.vpn.mynetname.net* 組成。只有在至少一個 ddns-request 成功完成後，此欄位才可見。 |
| **vpn-port** (*read-only: integer*) | BTH VPN 使用的埠。 |
| **vpn-status** (*read-only: string*) | 包含描述當前 BTH 狀態的文字字串。 |
| **vpn-relay-rtts** (*read-only;* "region (ip4: time(**ms**), ip6: time (**ms)**") | 每個可用中繼的往返時間，單位為毫秒；IPv4 和 IPv6 的值都會顯示。 |
| **vpn-relay-ipv4-status** (*read-only: string*) | 到中繼的連線狀態以及有關中繼的詳細資訊 |
| **vpn-relay-ipv6-status**(*read-only: string*) | 到中繼的連線狀態以及有關中繼的詳細資訊 |
| **vpn-relay-regions** (*read-only: string*) | 可用的 VPN 中繼區域，可在 vpn-prefer-relay-code 中引用。此處將顯示所有可用的中繼。 |
| **vpn-relay-addressess**(*read-only: string*) | 中繼的 IPv4 地址 |
| **vpn-relay-addressess-ipv6** (*read-only: string*) | 中繼的 IPv6 地址 |
| **vpn-private-key** (*read-only: string*) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | BTH 的私鑰 |
| **vpn-public-key** (*read-only: string*) | BTH 的公鑰 |
| **vpn-peer-private-key**(*read-only: string*) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | Peer 私鑰 |
| **vpn-peer-public-key** (*read-only: string*) | Peer 公鑰 |
| **vpn-prefer-relay-code** (*string;*) | 你可以輸入一個用於 BTH 連線的首選中繼程式碼；如果未設定，將選擇 RTT 最小的中繼。 |
| **vpn-interface** (*read-only: string*) | 為 Back to Home WireGuard® 隧道建立的介面名稱。 |
| **vpn-wireguard-client-config** (*read-only: string*) | 可輸入到你的首選 WireGuard® 用戶端中的配置。同一時間只能有一個用戶端使用此配置。 |
| **vpn-wireguard-client-config-qrcode** (*read-only*) | 可供你的首選 WireGuard® 用戶端掃描的二維條碼。同一時間只能有一個用戶端使用此配置。 |

:::info
使用 vpn-wireguard-client-config 或 vpn-wireguard-client-config-qrcode 時，這兩個選項是等效的；你只需將其中一個匯入到你的 WireGuard 用戶端裝置即可。
:::

### Back to Home 使用者 {#back-to-home-users}

**子選單：** `/ip/cloud/back-to-home-user`

自 RouterOS 7.14 起，選單 `/ip/cloud/back-to-home-user` 中提供了新的 Back to Home 專用使用者管理器，你可以在其中檢視 Back to Home 移動應用新增的所有使用者、更改他們的防火牆首選項，並新增新使用者。

```
[boss@mikrotik-ax] /ip/cloud/back-to-home-user> print detail   
Flags: X - disabled; A - active   
  
 0  A name="user1" slot=3 expires=never client-address=192.168.216.3/32,fc00:0:0:216::3/128 allow-lan=no   
      private-key="OHqR2BZXJp0N6//3JzzoJhBJVb0rrSxV0dxQL/2UdXY=" public-key="Na7oEq9XLdeK8ouCUX+tC4FIM51vEnZ7mLiFqG9xiUQ="   
  
[boss@mikrotik-ax] /ip/cloud/back-to-home-user>
```

在此選單中新增使用者時，你可以使用命令 `/interface/wireguard/peers/show-client-config user1` 檢視他們的 Wireguard 配置和二維條碼。

`Allow-lan=no` 會將使用者加入一個防火牆地址列表，該列表只允許網際網路訪問，但阻止使用者訪問你的內部網路。請注意，使用者新增後到期日期無法更改。

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string*) | BTH 使用者的說明性名稱 |
| **expires**(string; never \| date: *"YYYY-MM-DD HH:MM:SS";*  Default: **never***)* | 使用者的到期時間和日期。使用者建立後無法更改 |
| **client-address**(string: IPv4 \| IPv6) | 用戶端地址。如果未指定，將自動生成一個 |
| **allow-lan**(string: yes \| no; Default: **no**) | 會將使用者加入一個防火牆地址列表，該列表只允許網際網路訪問，但阻止使用者訪問你的內部網路 |
| **private-key**(string;) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 使用者的私鑰；如果未手動設定，將由系統生成 |
| **public-key**(string;) | 使用者的公鑰；如果未手動設定，將由系統生成 |
