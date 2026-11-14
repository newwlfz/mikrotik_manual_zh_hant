---
sidebar_key: "storage/dlna"
sidebar_position: 2
title: "DLNA 媒體伺服器"
sidebar_label: "DLNA 媒體伺服器"
description: "DLNA 媒體伺服器透過一個介面，將磁碟資料夾中的影片、音樂和圖片檔案共享給電視、手機和播放器。它涵蓋將伺服器限制到單個裝置、磁碟共享所建立的伺服器，以及播放器如何找到該伺服器。"
tags:
  - 'dlna'
  - 'media-server'
  - 'upnp'
source: https://manual.mikrotik.com/docs/storage/dlna
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

DLNA（Digital Living Network Alliance，數字生活網路聯盟）是一組網路協定，裝置用它來共享影片、照片和音樂等數字媒體。DLNA 構建在 UPnP（Universal Plug and Play，通用即插即用）之上，後者為裝置提供發現和控制能力：裝置透過 SSDP（Simple Service Discovery Protocol，簡單服務發現協定）相互發現，透過 SOAP（Simple Object Access Protocol，簡單物件訪問協定）交換控制訊息，並用 XML 描述自身及其服務。

RouterOS 媒體伺服器把磁碟上某個資料夾中的媒體檔案共享給電視、手機和 VLC 等播放器應用，該磁碟可以是 USB 磁碟、其他磁碟或 [tmpfs](./tmpfs.md) 資料夾。每個伺服器執行在一個介面上。該介面上的播放器按名稱找到伺服器，並播放路由器上的檔案。路由器按原樣提供檔案，不做轉換，因此播放器必須支援該檔案格式。

:::info
媒體伺服器在 SMIPS 裝置上不可用，這類小型 MIPS 裝置在 `/system/resource/print` 中的 `architecture-name` 為 `smips`。
:::

## 與區域網路中的電視共享 USB 磁碟 {#share-a-usb-disk-with-the-tvs-on-the-lan}

為 LAN 網橋上 USB 磁碟的 `media` 資料夾新增一個伺服器：

```ros
/ip/media/add friendly-name="Office media" interface=bridge \
    path=usb1/media
```

```ros
[admin@MikroTik] > /ip/media/print
Columns: INTERFACE, FRIENDLY-NAME, PATH, ALLOWED-IP, STATUS
# INTERFACE  FRIENDLY-NAME  PATH        ALLOWED-IP  STATUS
0 bridge     Office media   usb1/media  0.0.0.0     Running
```

區域網路中的播放器會把該伺服器列為 `Office media`。作為網橋埠的 Wi-Fi 介面上的裝置也位於 `bridge` 上。`usb1/media` 下的資料夾會顯示為資料夾。

`path` 也可以是磁碟的根資料夾，例如 `path=usb1`。務必設定 `path`：沒有設定它的伺服器會共享路由器的整個檔案列表，包括所有磁碟和資料夾。

伺服器會列出影片、音樂和圖片檔案，例如 `.mp4`、`.mkv`、`.mp3`、`.flac` 和 `.jpg` 檔案；其他檔案（例如 `.txt` 檔案）不會被列出。它只通過小寫副檔名識別媒體檔案，因此請重新命名副檔名為大寫的檔案（例如相機常寫出的 `.MP4` 或 `.JPG`）。與影片同名的 `.srt` 檔案（例如與 `holiday.mp4` 同目錄的 `holiday.srt`）會作為該影片的字幕一併提供。之後複製到該資料夾的檔案會在播放器下次開啟該資料夾時出現。

## 將伺服器限制為單個裝置 {#limit-a-server-to-one-device}

在啟用了自動媒體共享的路由器上（例如 hAP ax² 的預設配置），磁碟已經有一個動態伺服器，網橋上的每臺裝置都可以使用它（在關於為磁碟自動建立的伺服器一節中描述）。動態伺服器無法修改（`failure: can't edit dynamic object`），因此在新增受限伺服器之前先將其關閉：

```ros
/disk/set usb1 media-sharing=no
```

預設情況下，介面上的每臺裝置都可以使用伺服器。要將伺服器限制為單個裝置，請設定以下之一：

- `allowed-ip` - 裝置的 IP 地址。它只接受一個地址；子網會被拒絕。請為裝置分配靜態 DHCP 租約，使其地址不會改變（參見 [Leases](../network-management/dhcp/server.md#leases)）。
- `allowed-hostname` - 裝置在本路由器 DHCP 伺服器上 DHCP 租約的主機名。名稱必須完全匹配，包括大小寫。

伺服器只能採用兩者之一：同時設定兩者會失敗並提示 `failure: can't set both allowed IP and allowed hostname`。伺服器會拒絕其他裝置，因此它們看不到其檔案。

例如，只給兒童房的電視提供兒童影片，給客廳的電視提供其餘影片。每臺電視都有自己的伺服器：

```ros
/ip/media/add friendly-name=adults interface=bridge \
    path=usb1/media/adults allowed-hostname=Living-Room-TV
/ip/media/add friendly-name=kids interface=bridge \
    path=usb1/media/kids allowed-hostname=Kids-Room-TV
```

```ros
[admin@MikroTik] > /ip/media/print
Columns: INTERFACE, FRIENDLY-NAME, PATH, ALLOWED-IP, ALLOWED-HOSTNAME, STATUS
# INTERFACE  FRIENDLY-NAME  PATH               ALLOWED-IP  ALLOWED-HOSTNAME  STATUS
0 bridge     adults         usb1/media/adults  0.0.0.0     Living-Room-TV    Running
1 bridge     kids           usb1/media/kids    0.0.0.0     Kids-Room-TV      Running
```

要查詢裝置的主機名，請檢視其租約的 `HOST-NAME` 列：

```ros
/ip/dhcp-server/lease/print
```

在 DHCP 請求中不傳送主機名的裝置，其 `HOST-NAME` 為空，無法匹配 `allowed-hostname`。請改用 `allowed-ip` 和靜態租約來限制這類裝置。

:::note
`allowed-ip` 和 `allowed-hostname` 不是訪問控制。它們只檢查請求的源地址或裝置在 DHCP 中傳送的主機名。伺服器不要求密碼，檔案透過明文 HTTP 傳輸，因此網路上的任何裝置都可以冒用另一臺裝置的地址或主機名。若要阻止某些裝置獲取檔案，請將它們放在具有獨立伺服器的單獨網路中，或透過帶使用者和密碼的 [SMB](./smb.md) 共享。
:::

## 為磁碟自動建立的伺服器 {#servers-created-for-disks-automatically}

RouterOS 也會自行新增媒體伺服器：

- 對於在 `/disk` 中設定了 `media-sharing=yes` 的磁碟。
- 當 `/disk/settings` 中 `auto-media-sharing=yes` 時，對於每個新磁碟和 [tmpfs](./tmpfs.md#check-what-the-folder-shares) 資料夾。例如，hAP ax² 的預設配置會設定 `auto-media-sharing=yes` 和 `auto-media-interface=bridge`。

這樣的伺服器是 `media-interface`（或 `auto-media-interface`）所指定介面上的動態條目（標誌 `D`），名稱由路由器標識和磁碟插槽組成，例如 `MikroTik usb1 media`。其 `allowed-ip` 為 `0.0.0.0`，因此該介面上的每臺裝置都可以讀取該磁碟的媒體檔案。動態伺服器無法編輯或刪除。要限制它，請停止該磁碟的媒體共享並新增靜態伺服器。

要停止某個磁碟的伺服器：

```ros
/disk/set usb1 media-sharing=no
```

要停止為之後新增的磁碟自動建立的伺服器：

```ros
/disk/settings/set auto-media-sharing=no
```

相同的設定還會透過 SMB 共享磁碟，提供給無需密碼的 `guest` 使用者（參見 [臨時檔案系統（Tmpfs）](./tmpfs.md#check-what-the-folder-shares)）。要針對某個磁碟以及之後新增的磁碟停止該行為：

```ros
/disk/set usb1 smb-sharing=no
/disk/settings/set auto-smb-sharing=no
```

## 檢查與故障排除 {#check-and-troubleshoot}

首先檢查伺服器是否存在並正在執行。`/ip/media/print` 在 `STATUS` 中顯示每個伺服器的狀態：

- `Running` - 伺服器宣告自身並提供檔案。
- `Error, can't find directory` - `path` 中的資料夾不存在。請在 `/file/print` 中檢查磁碟插槽和資料夾名稱。

伺服器執行時，`/ip/service/print` 會顯示其在 UDP 埠 1900 和 TCP 埠 2828 上的動態 `upnp` 監聽器。要從計算機測試伺服器，請使用 VLC 等播放器，它會在本地網路部分列出 UPnP 媒體伺服器。

當播放器未列出伺服器時：

- 播放器必須位於伺服器的 `interface` 上。其他子網或 VLAN 中的播放器無法發現伺服器，因為 SSDP 發現訊息只在一個網路內傳播。請在該介面上新增一個具有相同 `path` 的第二個伺服器。
- 路由器的防火牆必須接受來自播放器的 UDP 埠 1900 和 TCP 埠 2828。預設防火牆接受來自 LAN 的所有流量。
- `allowed-ip` 或 `allowed-hostname` 必須與播放器匹配。不匹配的裝置什麼也看不到。
- 再次開啟播放器的伺服器列表，或重啟播放器，使其重新搜尋伺服器。

當列表中缺少某個檔案時，請檢查它是否為副檔名為小寫的影片、音樂或圖片檔案。其他檔案不會被列出。

## 技術細節 {#technical-details}

### 發現 {#discovery}

伺服器透過向 UPnP 組播組 `239.255.255.250:1900` 傳送 SSDP `NOTIFY` 訊息來宣告自身，作為具有 `ContentDirectory:1` 和 `ConnectionManager:1` 服務的 `urn:schemas-upnp-org:device:MediaServer:1` 裝置。它還會應答播放器為查詢伺服器而傳送的 `M-SEARCH` 請求。訊息中帶有 `CACHE-CONTROL: max-age=3600` 和伺服器描述的地址，例如 `LOCATION: http://192.168.88.1:2828/mediaserver_description-1.xml`。檔名中的數字對每個伺服器條目都不同。

### 內容 {#content}

播放器透過 ContentDirectory 服務瀏覽資料夾，並透過 TCP 埠 2828 以 HTTP 下載檔案。每個資料夾是一個容器，每個媒體檔案是一個條目，帶有其媒體型別，例如 `video/mp4`、`audio/mpeg` 或 `image/jpeg`。字幕檔案是其影片的一個額外 `text/srt` 資源。

### 縮圖 {#thumbnails}

`/ip/media/settings` 設定資料夾的封面圖片：

```ros
/ip/media/settings/set thumbnails=folder.jpg
```

名為 `folder.jpg` 的檔案此後不再作為圖片列出，而成為其資料夾中其他檔案的封面圖片。`thumbnails` 接受以逗號分隔的檔名列表。

### 介面繫結 {#interface-binding}

伺服器會處理到達其介面的請求，也包括來自其他子網、其流量經該介面路由到路由器的裝置。監聽器接受所有介面上的連線，但到達其他介面的伺服器請求會得到 HTTP 404 錯誤，無論使用哪個路由器地址。防火牆負責阻擋 WAN：預設防火牆會丟棄來自 WAN 的輸入。

有關所有引數，請參見 [`/ip/media`](../cli-reference/ip/media/index.md) 和 [`/ip/media/settings`](../cli-reference/ip/media/settings.md) 的 CLI 參考。
