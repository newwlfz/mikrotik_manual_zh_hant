---
sidebar_key: "network-management/cloud/index"
sidebar_position: 5
title: "雲"
sidebar_label: "雲"
description: "MikroTik Cloud 部分提供 Back To Home（遠端回家）、DDNS、檔案共享及其他雲輔助服務的配置，並附有關於啟用/停用 DDNS、觸發更新以及管理用於遠端訪問的 IP 地址的詳細說明。"
tags:
  - 'ddns'
  - 'ntp'
  - 'backup'
source: https://manual.mikrotik.com/docs/7.24/network-management/cloud
captured_at: '2026-11-04T11:32:31+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 MikroTik 雲功能。使用這些功能可以配置 Back To Home、雲通訊、檔案共享以及其他雲輔助服務。

<DocCardList />

MikroTik 為連線到網際網路的 RouterBOARD 裝置提供多項服務。這些服務旨在減少配置、設定、控制、維護或監控裝置時的不便。下方列出了 IP/Cloud 可提供的更詳細可用服務列表。

## 服務 {#services}

:::danger
請注意，如果路由器有多個公網 IP 地址和/或多個網際網路閘道器，用於與 MikroTik 雲伺服器通訊的確切 IP 可能不符合預期！

**警告：** IP/Cloud 需要為 Cloud Hosted Router (CHR) 購買付費永久許可證。

**警告：** x86 系統不支援雲服務。
:::

### DDNS {#ddns}

DDNS 或動態 DNS 是一項定期更新 A 記錄的 IPv4 地址和 AAAA 記錄的 IPv6 地址的服務。當你的 ISP 提供了會定期變化的動態 IP 地址，但你始終需要一個可用於遠端連線裝置的地址時，這樣的服務非常有用。下面你可以找到與 IP/Cloud 的 DDNS 服務相關的操作詳情：

- 檢查傳出 IP 地址變化：每 60 秒一次。
- 等待 MikroTik 雲伺服器的響應：15 秒。
- DDNS 記錄 TTL：60 秒。
- 使用 UDP 埠 15252 向 **cloud2.mikrotik.com** 傳送加密封包。

從 RouterOS v6.43 開始，如果你的裝置能夠使用 IPv6 訪問 **cloud2.mikrotik.com**，則會為你的公網 IPv6 地址建立 DNS **AAAA** 記錄。如果你的裝置只能使用 IPv4 訪問 cloud2.mikrotik.com，則只會為你的公網 IPv4 地址建立 DNS **A** 記錄。對於低於 6.44 的舊版 RouterOS，使用 cloud.mikrotik.com。

要啟用 DDNS 服務：

```ros
[admin@MikroTik] /ip/cloud/set ddns-enabled=yes
[admin@MikroTik] /ip/cloud/print
         ddns-enabled: yes
 ddns-update-interval: none
          update-time: yes
       public-address: 159.148.147.196
  public-address-ipv6: 2a02:610:7501:1000::2
             dns-name: 529c0491d41c.sn.mynetname.net
               status: updated
```

:::warning
啟用該服務後，DNS 名稱將永久儲存在 MikroTik 雲伺服器上，並且該 DNS 名稱將解析為你的 RouterOS 例項最後傳送給 MikroTik 雲伺服器的 IP。
:::

要停用 DDNS 服務：

```ros
/ip/cloud/set ddns-enabled=auto
```

:::warning
在 7.17 之前，ddns-enabled 的預設值為 "no"。在包括 7.17 及更高版本中，如果要停用 DDNS，請確保先停用 [Back To Home](./back-to-home.md) 功能（如果已啟用），然後設定 "ddns-enabled=auto"

**警告：** 一旦停用該服務，你的裝置就會向 MikroTik 雲伺服器傳送命令以刪除已儲存的 DNS 名稱。
:::

要手動觸發 DNS 更新：

```ros
[admin@MikroTik] > /ip/cloud/force-update
```

:::warning
要實際使用雲伺服器提供的 DNS 名稱連線到裝置，使用者必須配置路由器防火牆，允許從 WAN 埠進行此類訪問。（預設 MikroTik 配置不允許從 WAN 埠訪問 WebFig、WinBox 等服務）。
:::

### 更新時間 {#update-time}

裝置上的正確時間很重要，時間不正確會導致系統日誌出現問題、破壞到裝置的 HTTPS 連線、破壞隧道連線以及其他問題。要更新系統時鐘，你可以使用 [NTP](../../system-information-and-utilities/ntp.md) 或 [SNTP](../../system-information-and-utilities/ntp.md)，但這需要你為 NTP 伺服器指定 IP 地址。在大多數情況下，僅僅為了在裝置上設定正確時間，並不需要 NTP/SNTP；為簡單起見，你可以使用 IP Cloud 的更新時間服務。下面你可以找到與 IP/Cloud 的更新時間服務相關的操作詳情：

- 近似時間（精度為幾秒，取決於 UDP 封包延遲）。
- 在重啟後以及每次 DDNS 更新期間更新時間（當路由器的 WAN IP 地址發生變化或使用 force-update 命令後）。
- 使用 UDP/15252 埠向 **cloud2.mikrotik.com** 傳送加密封包。
- 根據路由器的公網 IP 地址和我們的商業資料庫檢測時區。

要啟用時間更新服務：

```ros
[admin@MikroTik] > /ip/cloud/set update-time=yes 
```

要啟用自動時區檢測：

```ros
[admin@MikroTik] > /system/clock/set time-zone-autodetect=yes 
```

:::warning
如果 `/ip/cloud/update-time` 設定為 `auto`，則裝置時鐘將使用 MikroTik 雲伺服器時間進行更新（如果沒有啟用 [NTP](../../system-information-and-utilities/ntp.md) 或 [SNTP](../../system-information-and-utilities/ntp.md) 用戶端）。
:::

### 備份 {#backup}

可以將裝置的 [備份](../../getting-started/configuration-management/backup.md) 儲存在 MikroTik 雲伺服器上。備份服務允許你上傳加密的備份檔案、下載該檔案，並在裝置能夠訪問 MikroTik 雲伺服器時將該備份檔案應用到裝置。下面你可以找到與 IP/Cloud 的備份服務相關的操作詳情：

- 每臺裝置 1 個免費備份槽位。
- 允許的備份大小：15MB。
- 使用 UDP/15252 和 TCP/15252 埠向 **cloud2.mikrotik.com** 傳送加密封包。

要建立新備份並將其上傳到 MikroTik 雲伺服器：

```ros
[admin@MikroTik] > /system/backup/cloud/upload-file action=create-and-upload password=test123!!!
[admin@MikroTik] > /system/backup/cloud/print 
 0 name="cloud-20180921-162649" size=13.2KiB ros-version="6.44beta9" date=2018-09-21 16:26:49 status="ok" secret-download-key="AbCdEfGhIjKlM1234567890" 
```

:::warning
`create-and-upload` 動作命令將建立新的系統備份檔案，使用提供的密碼透過 AES 加密該備份檔案並上傳。對於 `upload` 動作命令，password 屬性不起作用，因為 `upload` 動作命令僅上傳已建立的系統備份檔案。
:::

要下載已上傳的備份檔案並將其儲存到裝置記憶體：

```ros
[admin@MikroTik] > /system/backup/cloud/download-file action=download number=0
### OR
[admin@MikroTik] > /system/backup/cloud/download-file action=download secret-download-key=AbCdEfGhIjKlM1234567890
```

:::warning
**警告：** secret-download-key 是一個唯一識別符號，可用於將你的加密備份下載到其他裝置。由於你可以使用 secret-download-key 從任何位置和任何裝置下載加密備份，因此應儘量對此識別符號保密。下載的備份仍使用 AES 加密；但仍請確保使用強密碼！
:::

要刪除已上傳的備份：

```ros
/system/backup/cloud/remove-file number=0
```

要使用新的備份檔案替換現有檔案，請使用以下命令：

```ros
/system/backup/cloud/upload-file action=create-and-upload replace=_your_previously_created_backup_file_ password=test123!!!
```

要上傳現有的備份檔案（之前建立的）：

```ros
[admin@MikroTik] > /system/backup/save encryption=aes-sha256 name=old_backup password=test123!!!
[admin@MikroTik] > /system/backup/cloud/upload-file action=upload src-file=old_backup.backup
[admin@MikroTik] > /system/backup/cloud/print 
 0 name="cloud-20180921-164044" size=13.2KiB ros-version="6.44beta9" date=2018-09-21 16:40:44 status="ok" secret-download-key="AbCdEfGhIjKlM1234567890"
```

:::warning
確保備份使用 AES 加密，否則 IP/Cloud 將拒絕備份上傳。由於每臺裝置只有 1 個免費備份槽位，你需要先刪除現有備份再上傳新備份。
:::

### Back To Home {#back-to-home}

有關 Back to Home (BTH) 服務的更多資訊，請參閱單獨的[文件頁面](./back-to-home.md)。

### 檔案共享 {#file-share}

有關 File Share 服務的更多資訊，請參閱單獨的[文件頁面](./file-share.md)。

### 中繼服務 {#relay-service}

Back to Home 和 File Share 都部分依賴 MikroTik 雲中繼服務。透過中繼服務的所有傳輸都是端到端加密的，中繼純粹是為了便於連線，並且設計為永遠不需要解密使用者資料或元資料。有關每個服務如何使用中繼的詳細資訊，請參閱各自的手冊。

## 屬性 {#properties}

**子選單：** `/ip/cloud`

| 屬性 | 描述 |
| :-- | :-- |
| **ddns-enabled** (*yes \| auto*；預設值：**auto**) | 如果設定為 `yes`，裝置將向 MikroTik 雲伺服器傳送加密訊息。伺服器隨後會解密該訊息並驗證傳送方是否為真實的 MikroTik 裝置。如果一切正常，MikroTik 雲伺服器將為該裝置建立 DDNS 記錄並向裝置傳送響應。路由器上的 IP/Cloud 服務每分鐘都會檢查 WAN IP 地址是否與傳送給 MikroTik 雲伺服器的地址匹配，並在 IP 地址發生變化時向雲伺服器傳送加密更新。如果設定為 auto，則僅當啟用 [Back To Home](../../system-information-and-utilities/ntp.md) 時才會啟用 ddns。**重要：** 在 7.17 版本之前，預設值為 "no"。     |
| **ddns-update-interval** (*time，最小 60 秒*；預設值：**none**) | 如果設定，DDNS 將按設定的間隔嘗試連線 IP Cloud 伺服器。如果設定為 **none**，它將繼續在內部檢查 IP 地址更新，並根據需要連線 IP Cloud 伺服器。如果所使用的 IP 地址不在路由器本身上，因而無法作為路由器內部值進行檢查，則該選項很有用。 |
| **update-time** (*yes \| no*；預設值：**yes**) | 如果設定為 `yes`，則路由器時鐘將被設定為雲伺服器提供的時間，**前提是**未啟用 [NTP](../../system-information-and-utilities/ntp.md) 或 [SNTP](../../system-information-and-utilities/ntp.md) 用戶端。如果設定為 `no`，則 IP/Cloud 服務將永遠不會更新裝置時鐘。如果 update-time 設定為 `yes`，即使 ddns-enabled 設定為 auto，時鐘也會更新。 |
| **public-address** (*只讀：address*) | 顯示已傳送到雲伺服器的裝置 IPv4 地址。僅在至少一個 IP Cloud 請求成功完成後，此欄位才可見。 |
| **public-address-ipv6** (*只讀：address*) | 顯示已傳送到雲伺服器的裝置 IPv6 地址。僅在至少一個 IP Cloud 請求成功完成後，此欄位才可見。 |
| **warning** (*只讀：string*) | 如果裝置傳送的 IP 地址與 MikroTik 雲伺服器所見的 UDP 封包頭中的 IP 地址不同，則顯示警告訊息。通常，當裝置位於 NAT 後面時會發生這種情況。示例："DDNS 伺服器收到來自 IP `123.123.123.123` 的請求，但你的本地 IP 是 `192.168.88.23`；DDNS 服務可能無法正常工作" |
| **dns-name** (*只讀：name*) | 顯示分配給裝置的 DNS 名稱。該名稱由 12 個字元的序列號後接 *.sn.mynetname.net* 組成。僅在至少一個 ddns-request 成功完成後，此欄位才可見。 |
| **status** (*只讀：string*) | 包含描述當前 dns-service 狀態的文字字串。這些訊息本身已說明含義：updating...updatedError: no Internet connectionError: request timed outError: REJECTED. Contact MikroTik supportError: internal error - should not happen. One possible cause is if the router runs out of memory |

### 高階 {#advanced}

**子選單：** `/ip/cloud/advanced`

| 屬性 | 描述 |
| :-- | :-- |
| **use-local-address** (*yes \| no*；預設值：**no**) | 預設情況下，DNS 名稱將分配給檢測到的公網地址（來自 UDP 封包頭）。如果你希望傳送你的“本地”或“內部” IP 地址，請將其設定為 `yes`。 |

### 雲備份 {#cloud-backup}

**子選單：** `/system/backup/cloud`

下面你可以找到與特定命令相關的命令和屬性；其他屬性不會有任何效果：

- download-file

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*download*) | 從 MikroTik 雲伺服器下載已上傳的備份檔案。 |
| **number** (*integer*) | 指定 MikroTik 雲伺服器上的備份槽位。免費備份槽位始終位於 `0th` 槽位。 |
| **secret-download-key** (*string*) | 可用於下載已上傳備份檔案的唯一識別符號。下載已上傳的備份檔案時，你不必使用上傳該備份的同一裝置。在新裝置上部署備份時很有用。 |

- remove-file

| 屬性 | 描述 |
| :-- | :-- |
| **number** (*integer*) | 刪除指定備份槽位中的備份檔案。免費備份槽位始終位於 `0th` 槽位。 |

- upload-file

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*create-and-upload*) | 將備份檔案上傳到 MikroTik 雲伺服器。<code>create-and-upload</code> - 使用指定密碼建立新的備份檔案並上傳<code>upload</code> - 上傳已建立的系統備份檔案。 |
| **name** (*string*) | 指定將在已上傳備份列表中顯示的備份名稱。這**不是**源備份的名稱，此名稱僅用於視覺化展示。 |
| **src-file** (*file*) | 要上傳的備份檔名，該備份檔案是使用 `/system/backup` 建立的。此屬性僅在 action 設定為 `upload` 時生效。 |
| **password** (*string*) | 使用指定密碼建立、加密並上傳備份檔案。此屬性僅在 action 設定為 `create-and-upload` 時生效。 |
