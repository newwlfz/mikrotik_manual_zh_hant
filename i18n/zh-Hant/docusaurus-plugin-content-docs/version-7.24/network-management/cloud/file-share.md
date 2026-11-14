---
sidebar_key: "network-management/cloud/file-share"
sidebar_position: 3
title: "檔案共享"
sidebar_label: "檔案共享"
description: "檔案共享功能允許透過 HTTPS 共享 USB/NVME 驅動器並可選支援檔案上傳，同時使用自動生成的域名和證書，從而在 MikroTik 路由器上實現可透過網際網路安全訪問的儲存。"
tags:
  - 'file-sharing'
  - 'https'
  - 'cloud'
source: https://manual.mikrotik.com/docs/7.24/network-management/cloud/file-share
captured_at: '2026-11-04T11:32:57+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

檔案共享功能允許你使用路由器的外部儲存，與網際網路上的任何人共享檔案。只需將 USB、nVME 或任何受支援的驅動器連線到裝置，然後將整個目錄路徑新增到檔案共享選單中。路由器將使用 MikroTik 雲服務為你的路由器簽發 HTTPS 證書和域名。隨後你可以分發給任何人的 URL 將顯示在檔案共享選單中。你還可以啟用允許任何人向你的路由器上傳檔案的功能。該 URL 是隨機生成的，因此雖然任何知道連結的人都可以使用它，但只要你妥善保管，就只有擁有該連結的人才能使用它。

### 新增共享 {#adding-shares}

首先，連線你的 USB 驅動器，並確定要共享目錄的檔案路徑：

```shell
[user@RouterOS] > /file/print
 # NAME                                                                           TYPE             SIZE LAST-MODIFIED
 0 web                                                                            directory             2025-01-23 09:29:42
 1 usb1                                                                           disk                  2025-01-22 09:45:57
 2 pub                                                                            directory             2025-01-23 09:24:41
 3 skins                                                                          directory             2024-12-10 08:19:27
 4 pub/index.html                                                                 .html file        670 2025-01-23 09:24:41
 5 skins/default.json                                                             .json file        151 2024-07-15 10:20:11
 6 usb1/Secret Files                                                        	  directory             2024-03-18 09:01:41
 7 usb1/forum                                                                     directory             2025-01-22 10:58:20
 8 usb1/Secret Files/Home Video.srt                 							                .srt file         267 2020-06-01 11:29:14
 9 usb1/Secret Files/Home Video.mp4                 							                .mp4 file   1584.4MiB 2020-06-01 11:34:33
10 usb1/forum/cat.jpeg                                                            .jpeg file  4307.7KiB 2025-01-22 09:38:55
11 usb1/forum/cat1.jpeg                                                           .jpeg file   231.8KiB 2025-01-22 10:58:20
12 usb1/forum/cat2.jpeg                                                           .jpeg file   129.6KiB 2025-01-22 10:58:20
13 usb1/forum/cat3.jpeg                                                           .jpeg file   263.8KiB 2025-01-22 10:58:20
14 usb1/forum/cat4.jpeg                                                           .jpeg file   438.4KiB 2025-01-22 10:58:20
15 web/index.html                                                                 .html file       1473 2025-01-23 09:29:42
```

導航到 `/ip/cloud/back-to-home-file`。共享**目錄**時，必須指定**路徑**和**過期日期**，還可以授予**上傳許可權**。共享**檔案**時，只需提供**路徑**和**過期日期**。

```shell
[user@RouterOS] /ip/cloud/back-to-home-file> add path="usb1/Secret Files/" expires=never allow-uploads=yes
[user@RouterOS] /ip/cloud/back-to-home-file> add path="usb1/Secret Files/Home Video.mp4" expires=never
[user@RouterOS] /ip/cloud/back-to-home-file> print
Columns: PATH, URL, DIRECT-URL, EXPIRES, DOWNLOADS
# PATH                      URL                                                        DIRECT-URL                                                    EXPIRES  DOWNLOADS
0 /usb1/Secret Files  https://acf017skgys.routingthecloud.net/s/4MPgHbEZCZYGVtp  https://acf017skgys.routingthecloud.net/s/4MPgHbEZCZYGVtp?dl        never            5
1 /usb1/Secret Files/Home Video.mp4      https://acf017skgys.routingthecloud.net/s/K8zkh1UjKuqtEQ0  https://acf017skgys.routingthecloud.net/s/K8zkh1UjKuqtEQ0?dl         never            2
[user@RouterOS] /ip/cloud/back-to-home-file>
```

現在，如果你複製“URL”，就可以將其分享給其他人，無論他們身在何處，也無論你的路由器是否有公網 IP。

當你將 URL 傳送給朋友後，他們就能看到共享目錄中的所有檔案並下載它們。如果你在建立共享時啟用了上傳，他們還可以向你的路由器上傳檔案。請妥善保管此 URL，或指定 “expires” 日期，以避免其他人訪問這些檔案。

![](/img/6ec257a71bcc9cad.png)

| 屬性 | 描述 |
| :-- | :-- |
| **enable**（預設） | 啟用檔案共享功能。新增第一個共享後，檔案共享服務將被啟用。如果沒有任何共享，檔案共享服務將保持停用。 |
| **disabled**（*yes \| no;* 預設：**no**） | 停用檔案共享功能。 |
| **allow-uploads**（*yes \| no;* 預設：**no**） | 啟用允許任何人向你的路由器上傳檔案的選項。 |
| **expires**（預設：**never**） | 共享過期日期。格式：ISO 8601 (2025-01-25 00:00:00) 示例：`/ip/cloud/back-to-home-file/set` 0 expires="2025-01-25 07:15:00" |
| **path** | 設定要共享檔案的路徑。  示例："/ip/cloud/back-to-home-file/add path=mypath/myfile" |

### WinBox 圖形介面 {#winbox-gui}

要共享檔案，請訪問位於 IP → Cloud“Configuration”部分下的“File Shares”選單。

![](/img/45b359a8acbe106a.png)

要建立新共享，請設定 “Path”、“Expires” 和 “Auto uploads” 選項。

![](/img/42deef3f2e945b64.png)

```ros
[admin@MikroTik] > /ip/cloud/back-to-home-file/print detail 
Flags: X - disabled; I - invalid 
 0    path=/mypath/myfile allow-uploads=no expires=2025-01-25 07:15:00 key="*********" 
      url="https://*********.routingthecloud.net/s/*********" direct-url="https://*********.routingthecloud.net/s/*********" 
      downloads=0
```

:::info
安全警告

該 URL 是隨機生成的，因此雖然任何知道連結的人都可以使用它，但只要你妥善保管，就只有擁有該連結的人才能使用它。
:::

檔案共享使用 HTTPS（TCP 埠 443），但如果你已手動配置 WebFig 也使用 HTTPS，那麼檔案共享將自動僅透過我們的雲中繼服務工作，因為同一裝置上不能有兩個服務使用同一埠。預設情況下未啟用 www-ssl，因此檔案共享預設直接工作，下載時不使用中繼。啟用檔案共享絕不會影響你的 WebFig 配置，也不會將其暴露到公網。

對於檔案共享功能，當用戶想與某人共享檔案時，如果你的路由器可從網際網路直接訪問（由中繼伺服器檢查），操作順序如下：

- 路由器在本地生成私鑰和證書。
- 證書籤名在路由器上使用標準 ACME 協定完成（使用 DNS-01 質詢，後端為 LetsEncrypt）。
- 透過臨時新增 DNS TXT 記錄（標準流程），將 DNS-01 質詢傳送到 MikroTik 雲 DNS 伺服器。
- DNS 名稱解析到路由器。
- 使用私有證書開放安全的 443 埠。

### 中繼服務 {#relay-service}

如果裝置無法從網際網路直接訪問，它將選擇使用 MikroTik 託管的 Relay 服務。

- 路由器檢查其從網際網路的可達性。
- 如果需要中繼連線，則將 DNS 更新為中繼 IP。
- 路由器根據延遲選擇最近的中繼。
- 如果路由器使用中繼，則與中繼保持連線。yyyyyy.routingthecloud.net 解析到中繼。當用戶端透過中繼建立連線時，會解析 TLS Client Hello 以獲取目標路由器，並將整個 HTTPS 請求直接轉發到路由器。
- 中繼無法解密你的資料，因為帶有私鑰的證書僅存在於路由器上。
