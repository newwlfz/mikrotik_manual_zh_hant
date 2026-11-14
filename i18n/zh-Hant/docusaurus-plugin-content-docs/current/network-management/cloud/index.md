---
sidebar_key: "network-management/cloud"
title: "雲"
sidebar_label: "雲"
description: "RouterOS 中的 MikroTik 雲服務：為路由器提供 DDNS 名稱、啟動時的時鐘和時區、雲備份、Back To Home（遠端回家） VPN 和檔案共享。哪些服務預設開啟，以及路由器如何連線到 MikroTik 雲伺服器。"
tags:
  - 'cloud'
  - 'ddns'
  - 'ntp'
source: https://manual.mikrotik.com/docs/network-management/cloud
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik 為 RouterOS 裝置提供免費的雲服務。這些服務為路由器提供 DNS 名稱、設定其時鐘和時區、儲存備份，並讓你能夠訪問家庭網路或共享路由器上的檔案，即使路由器沒有公網 IP 地址。路由器始終主動向 MikroTik 伺服器發起連線，因此這些服務都不需要在其他裝置上做埠轉發。

## 服務 {#services}

| 服務 | 選單 | 預設開啟 | 用途 |
| :-- | :-- | :-- | :-- |
| DDNS | `/ip/cloud` | no | 獲取一個跟隨路由器公網 IP 地址的 DNS 名稱。 |
| 時間更新 | `/ip/cloud`、`/system/clock` | yes | 在路由器啟動時設定時鐘和時區。 |
| [雲備份](./cloud-backup.md) | `/system/backup/cloud` | no | 將加密備份儲存到 MikroTik 伺服器上。 |
| [Back To Home](./back-to-home.md) | `/ip/cloud` | no | 透過 WireGuard VPN 從手機或計算機訪問你的家庭網路。 |
| [檔案共享](./file-share.md) | `/ip/cloud/back-to-home-file` | no | 透過 HTTPS 連結共享路由器儲存中的檔案。 |

[與 MikroTik 雲服務的通訊](./communication-mikrotik-cloud-servers.md)列出了 RouterOS 與 MikroTik 伺服器建立的所有連線，以及如何關閉每一個連線。

:::info
雲服務可在 MikroTik 裝置以及擁有付費永久許可證的 Cloud Hosted Router（CHR）上使用。x86 版本的 RouterOS 不提供這些服務。
:::

## DDNS {#ddns}

動態 DNS（DDNS）為路由器提供一個位於 `sn.mynetname.net` 下的 DNS 名稱，該名稱會跟隨路由器的公網 IP 地址。當你的 ISP 更改地址時，可以用它透過名稱訪問路由器。

要啟用 DDNS 並檢視名稱：

```ros
[admin@MikroTik] > /ip/cloud/set ddns-enabled=yes
[admin@MikroTik] > /ip/cloud/print
          ddns-enabled: yes
  ddns-update-interval: none
           update-time: yes
        public-address: 203.0.113.10
              dns-name: hf1234abcd5.sn.mynetname.net
                status: updated
      back-to-home-vpn: revoked-and-disabled
```

該名稱對裝置保持不變，路由器會自動保持其更新。要立即傳送更新，例如在更改網際網路連線之後：

```ros
/ip/cloud/force-update
```

該名稱只是讓路由器更容易被找到。它不會開放任何訪問許可權：預設防火牆會丟棄來自網際網路的、發往路由器的連線。要遠端訪問路由器，請使用 [Back To Home](./back-to-home.md)，或[在防火牆中放行這些服務](../../getting-started/securing-your-router.md#opening-management-access-from-wan-advanced)。你還可以為該名稱獲取 [Let's Encrypt 證書](../../authentication-authorization-accounting/certificates.md#lets-encrypt-certificate)。

要讓該名稱解析為路由器自身的地址而不是公網地址，例如在內部網路中透過名稱訪問路由器：

```ros
/ip/cloud/advanced/set use-local-address=yes
```

要關閉 DDNS：

```ros
/ip/cloud/set ddns-enabled=auto
```

隨後路由器會請求雲伺服器刪除該名稱。使用 `auto` 時，只要 Back To Home 處於啟用狀態，DDNS 就會保持開啟，因此如果你使用了 Back To Home，請先將其關閉。

## 時間更新 {#time-update}

路由器啟動時會從雲伺服器設定其時鐘和時區，除非已啟用 [NTP 用戶端](../../system-information-and-utilities/ntp.md)。此功能不需要 DDNS。雲端時間是近似值：要獲得準確的時鐘，請使用 NTP 用戶端。

要阻止路由器向雲端請求時間和時區：

```ros
/ip/cloud/set update-time=no
/system/clock/set time-zone-autodetect=no
```

## 技術細節 {#technical-details}

### 路由器如何連線到雲端 {#how-the-router-reaches-the-cloud}

路由器向 `cloud2.mikrotik.com` 的 UDP 埠 15252 傳送加密請求。雲伺服器會用它收到請求的地址進行回覆，路由器將其顯示在 `public-address` 中；當路由器還透過 IPv6 連線到該伺服器時，也會顯示在 `public-address-ipv6` 中。在 NAT 之後，這是 NAT 裝置的公網地址，而不是路由器上的地址。在具有多條網際網路連線的路由器上，它是通往 `cloud2.mikrotik.com` 的路由所使用的那條連線的地址。

當無法從網際網路直接訪問路由器時，Back To Home 和 File Share 會透過 MikroTik 中繼伺服器進行連線。路由器會與最近的中繼保持一條開啟的連線，用戶端透過該連線訪問路由器。流量始終保持端到端加密：金鑰只存在於路由器和用戶端上，因此中繼無法讀取資料。

### DDNS 更新 {#ddns-updates}

- 該名稱由裝置序列號的小寫形式加上 `.sn.mynetname.net` 構成。它解析為 `public-address`，生存時間（TTL）為 60 秒；當路由器還有 `public-address-ipv6` 時，也會解析為該地址。
- 在 NAT 之後，路由器無法在自己的介面上看到其公網地址，此時路由器每分鐘傳送一次更新。
- 在 DDNS 關閉時（沒有 Back To Home 的 `ddns-enabled=auto`），`force-update` 不會執行任何操作。
- 當 DDNS 關閉時，路由器會向雲伺服器傳送刪除請求，該名稱會在幾分鐘內停止解析。
- 使用 `use-local-address=yes` 時，該名稱解析為路由器傳送請求時所使用的地址，而 `public-address` 仍顯示公網地址。
- 當雲伺服器沒有響應時，`status` 顯示 `updating...`，路由器會以逐漸增大的間隔重試。`failed to connect` 表示某個請求沒有得到回覆。

### 啟動時的時間更新 {#time-update-at-startup}

- 路由器在啟動後會向雲伺服器請求一次時間，即使使用 `ddns-enabled=auto` 也是如此。DDNS 更新和 `force-update` 不會再次設定時鐘。
- 當 NTP 用戶端啟用時，路由器不使用雲端時間，即使 NTP 用戶端無法連線到任何伺服器。
- 路由器會記錄每次時鐘變更，例如：

  ```text
  system,critical,info cloud change time Sep/24/2026 03:01:57 => Sep/24/2026 06:25:50
  ```

- 對於 `time-zone-autodetect`，雲伺服器會查詢路由器公網 IP 地址所在的位置，路由器會應用該時區，包括夏令時。

有關所有屬性，請參閱 CLI 參考中的 [`/ip/cloud`](../../cli-reference/ip/cloud/index.md) 和 [`/ip/cloud/advanced`](../../cli-reference/ip/cloud/advanced.md)。
