---
sidebar_key: "network-management/cloud/file-share"
sidebar_position: 4
title: "檔案共享"
sidebar_label: "檔案共享"
description: "File Share 透過 HTTPS 藉助秘密連結提供路由器儲存中的目錄或單個檔案，使用 Let's Encrypt 證書和 routingthecloud.net 名稱，可直接提供或透過 MikroTik 中繼提供，並可選支援上傳。"
tags:
  - 'file-sharing'
  - 'https'
  - 'cloud'
source: https://manual.mikrotik.com/docs/7.25/network-management/cloud/file-share
captured_at: '2026-11-04T11:21:03+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

File Share 透過一個連結把路由器儲存（例如 USB 驅動器）上的目錄或單個檔案釋出到網際網路上。路由器透過 HTTPS 在 `https://<serial>.routingthecloud.net/s/<key>` 上提供每個共享，其中 `<serial>` 是路由器的序列號，`<key>` 是該共享的隨機金鑰。路由器會自動為該名稱獲取 Let's Encrypt 證書。當無法從網際網路直接訪問路由器時，連線會經由 MikroTik 中繼伺服器（參見[路由器如何連線到雲](./index.md#how-the-router-reaches-the-cloud)）。訪問者只需要該連結，並且你還可以允許他們上傳檔案。

## 共享目錄或檔案 {#share-a-directory-or-file}

用 `/file/print` 找到目錄或檔案的路徑，然後新增共享。第一個共享會讓路由器申請其證書，在證書就緒之前該共享會顯示 `I` 標誌，通常在一分鐘內完成：

```ros
[admin@MikroTik] > /ip/cloud/back-to-home-file/add path=usb1/photos expires=never
[admin@MikroTik] > /ip/cloud/back-to-home-file/print detail
Flags: I - INVALID
0 I ;;; getting cert status: requesting SSL certificate
    path=/usb1/photos allow-uploads=no expires=never
    key="Ab3dE5gH7jK9mNp"
    url="https://hf1234abcd5.routingthecloud.net/s/Ab3dE5gH7jK9mNp"
    direct-url="https://hf1234abcd5.routingthecloud.net/s/Ab3dE5gH7jK9mNp?dl"
    downloads=0
```

當 `I` 標誌消失後，把 `url` 傳送給應當獲取這些檔案的人。任何擁有該連結的人都能開啟共享，因此請對連結保密，併為只需臨時使用的共享設定 `expires`。

- 目錄共享會開啟一個列出該目錄中檔案的頁面。訪問者可以下載單個檔案或整個目錄。`direct-url`（帶 `?dl` 的 `url`）會把整個目錄下載為 `download.zip`。
- 檔案共享會開啟該檔案的頁面。其 `direct-url` 會下載檔案本身。

共享頁面的標題會顯示路由器的標識（`/system/identity`），頁面資料中還包含路由器的板卡型號。

`expires` 接受 `never`、諸如 `"2026-10-01 00:00:00"` 的日期時間，或諸如 `1h`、`7d` 的時間間隔。路由器會把間隔轉換為共享過期的日期。`downloads` 統計該共享的直接下載次數。開啟頁面不計入其中。

若要臨時停止某個共享而不刪除它，可將其停用。在你重新啟用該共享之前，其連結會返回 HTTP 404：

```ros
/ip/cloud/back-to-home-file/disable 0
```

## 允許上傳 {#allow-uploads}

使用 `allow-uploads=yes` 時，目錄共享的訪問者可以向該目錄上傳檔案並在其中建立資料夾。不設定它時，路由器以 HTTP 403 拒絕上傳。檔案共享不提供上傳功能。

```ros
/ip/cloud/back-to-home-file/add path=usb1/inbox expires=7d allow-uploads=yes
```

上傳的檔案會佔用路由器的儲存空間，因此只對你信任的人、並且只在你需要的時間內允許上傳。

## WinBox {#winbox}

要在 WinBox 中共享檔案，請開啟 **IP** > **Cloud**，並在 **Configuration** 下選擇 **Back To Home（遠端回家） Files**。

![WinBox IP Cloud window with Back To Home Files under Configuration](/img/20ecb78186cbd59e.webp)

選擇 **New**，設定 **Path** 和 **Expires**，並選擇 **Allow Uploads** 以允許訪問者上傳檔案。

![WinBox Back To Home Files list and the form for a new file share](/img/8925fa4f0ef06036.webp)

共享目錄會在訪問者的網頁瀏覽器中開啟：

![Shared directory in a web browser with the Upload files and Download all buttons](/img/a6882989aec31383.webp)

## 停止 File Share {#stop-file-share}

只要至少存在一個共享，File Share 就會執行。當你刪除最後一個共享時，服務會停止，中繼也不再向路由器轉發連線：

```ros
/ip/cloud/back-to-home-file/remove [find]
```

證書會保留在路由器上，因此下一個共享無需重新申請即可啟動。若要同時刪除證書，請在刪除所有共享後執行 `remove-certificate`。當存在共享時，該命令會失敗並提示 `cannot remove certificate while file shares active`。之後下一個共享會申請新證書。

```ros
/ip/cloud/back-to-home-file/settings/remove-certificate
```

## 技術細節 {#technical-details}

### File Share 的工作方式 {#how-file-share-works}

當你新增第一個共享時，路由器會建立私鑰，並使用 ACME 協定為 `<serial>.routingthecloud.net` 申請 Let's Encrypt 證書。它透過 MikroTik 雲完成 DNS-01 驗證，因此無需為此開放埠，在 NAT 後也是如此。`/ip/cloud/back-to-home-file/settings` 中的 `status` 會顯示各個步驟，從 `getting cert status: requesting SSL certificate` 到 `requesting validation`、`requesting authorization` 和 `requesting order finalization`，直至 `running`。私鑰保留在路由器上，因此訪問者的 TLS 連線終結於路由器，經中繼時也是如此。

路由器會請求中繼伺服器測試是否可以從網際網路直接訪問路由器。當無法直接訪問時（例如在 NAT 之後），路由器會保持與中繼的連線，該名稱會解析到中繼。中繼會把訪問者的加密連線轉發給路由器，而路由器不會在自己的地址上監聽 TCP 埠 443。當其他服務（例如 `www-ssl`，即透過 HTTPS 訪問 WebFig）已佔用路由器上的 TCP 埠 443 時，File Share 也會使用中繼。`/ip/cloud/back-to-home-file/settings` 中的 `relay-ipv4-status` 和 `relay-ipv6-status` 顯示與中繼的連線狀態。

具有 `file-access` 的 [Back To Home](./back-to-home.md) 使用者使用同一服務。新增這類使用者同樣會讓路由器申請證書。

### 路由器上會發生哪些變化 {#what-changes-on-the-router}

- 共享的檔案和目錄在 `/file/print` 中顯示 `S`（shared）標誌；`/file/print where shared` 會列出它們。
- 證書以 `fileshare-<serial>.routingthecloud.net` 的名稱儲存在 `/certificate` 中。它由 ACME 用戶端管理，路由器會安排其續期；`certificate,info` 日誌會顯示其建立、匯入的時間以及下次更新的時間。
- 刪除最後一個共享後，`/ip/cloud/back-to-home-file/settings` 中的 `enabled` 為 `no`，但 `dns-name` 仍保留在設定中。

有關所有屬性，請參閱 CLI 參考中的 [`/ip/cloud/back-to-home-file`](../../cli-reference/ip/cloud/back-to-home-file/index.md) 和 [`/ip/cloud/back-to-home-file/settings`](../../cli-reference/ip/cloud/back-to-home-file/settings/index.md)。
