---
sidebar_key: "containers/apps/index"
sidebar_position: 2
title: "應用"
sidebar_label: "應用"
description: "Apps 選單提供一個預配置應用程式目錄，這些應用程式可透過容器部署，具備自動的 RouterOS 配置，並支援多個容器登錄檔。它需要安裝 Container 軟體包，初始設定時需要物理訪問許可權，並且包含安全方面的考量，例如證書驗證和硬體裝置管理。"
tags:
  - 'container'
  - 'apps'
  - 'security'
source: https://manual.mikrotik.com/docs/7.24/containers/apps
captured_at: '2026-11-04T11:27:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

#### 概述 {#summary}

**子選單：** `/app`  
**所需軟體包：** `container`

App 選單提供了一個應用目錄，只需點選幾下即可部署其中的應用。每個應用可以包含一個或多個預配置容器，並且會自動應用必要的 RouterOS 配置，例如防火牆規則和地址轉換。此目錄由 MikroTik 準備和維護，但容器映象來自多個登錄檔，例如 Docker Hub、GCR 和 Quay。

不過，可以在啟用應用之前編輯配置引數，並且始終可以檢視所應用的 yaml 檔案。

#### 要求 {#requirements}

App 系統繼承與 Container 軟體包相同的要求：

- **架構支援：** arm64 和 x86 架構。
- **容器軟體包：** 必須已安裝。
- **裝置模式：** 必須啟用容器模式（需要物理訪問並重設裝置）。
- **外部儲存：** 強烈建議使用外部儲存以獲得最佳效能。
- **記憶體要求：** 為容器操作提供足夠的 RAM（16MB SPI flash 裝置可能需要外部儲存來存放映象）。
- **架構限制：** 不支援搭載 EN7562CT CPU 的裝置（例如 hEX Refresh）。

#### 安全注意事項 {#security-considerations}

與底層 Container 系統一樣，App 選單也繼承其安全影響：

- 初次啟用容器支援需要物理訪問。
- 啟用後，容器可以遠端管理。
- 裝置被攻陷後，可利用容器安裝惡意軟體。
- 裝置安全性等同於執行容器時的安全性。
- 第三方容器映象可能引入安全漏洞。

## 屬性 {#properties}

| 屬性 | 型別 | 預設值 | 描述 |
| :-- | :-- | :-- | :-- |
| **auto-update** | *yes* &#124; *no* | *no* | 啟用或停用在新容器映象版本可用時自動更新。 |
| **check-certificate** | *yes* &#124; *no* | *yes* | 在拉取容器映象前驗證登錄檔證書。 |
| **container-command-lines** | *string* | *（空）* | 指定啟動容器時傳遞給應用程式的命令列引數。 |
| **devices** | *string* | *（空）* | 指定要直通給容器應用程式的額外硬體裝置。 |
| **environment** | *string* | *（空）* | 定義可供執行中應用程式使用的環境變數。指定為鍵值對列表。 |
| **extra-mounts** | *string* | *（空）* | 指定要附加到容器的額外掛載點。 |
| **firewall-redirects** | *string* | *（空）* | 配置從主機裝置到容器的埠重定向。 |
| **network** | *default* &#124; *lan* &#124; *internal* | *default* | 指定容器將使用的網路：**internal**（位於 NAT 之後）、**lan**（在 LAN 網路上）或 **default**（因應用程式而異；可以是 internal 或 lan）。 |
| **network-outgoing-access** | *yes* &#124; *no* | *yes* | 允許特定容器應用程式進行網路出站訪問；設定為 `no` 時，會建立一條 mangle drop 規則。 |
| **pvid** | *integer* | *1* | 設定網橋中容器虛擬乙太網介面的埠 VLAN ID（PVID）。 |
| **required-hw-devices** | *string* | *（空）* | 容器啟動前必須存在於主機上的硬體裝置。僅在新增 YAML 配置後可配置此屬性。 <br/><br/><strong>Compose 格式：</strong><code>[host-hw-device]:[device-in-app]</code> |
| **required-mounts** | *string* | *（空）* | 容器啟動前必須掛載的目錄。僅在新增 YAML 配置後可配置此屬性。 <br/><br/><strong>Compose 格式：</strong><code>[dir-on-host]:[dir-in-app]</code> |
| **use-https** | *yes* &#124; *no* | *yes* | 對應用程式 URL 使用 HTTPS。此選項在不支援雲服務的裝置上不會生效。 |
| **yaml** | *string* | *（空）* | 提供應用程式的 YAML 組合配置。有關配置示例，請參閱文件。 |

## 只讀屬性 {#read-only-properties}

| 屬性 | 型別 | 預設值 | 描述 |
| :-- | :-- | :-- | :-- |
| **app-size** | | | 應用的總大小。 |
| **app-store-url** | *string* | | 安裝該應用時所用應用商店的 URL。 |
| **cpu-usage** | | | 應用當前的 CPU 使用率百分比。 |
| **custom** | *yes* &#124; *no* | | 指示該應用是否為使用者建立的自定義應用。 |
| **data-size** | | | 應用儲存的資料大小。 |
| **default-credential** | *string* | | 應用所需的預設憑據。 |
| **default-network** | *lan* &#124; *internal* | | 應用使用的預設網路。有效值為 `lan` 或 `internal`。 |
| **description** | *string* | | YAML 配置的 `descr` 引數中定義的應用描述。 |
| **from-app-store** | *yes* &#124; *no* | | 指示該應用是否從自定義應用商店安裝。 |
| **interface** | *string* | | 應用使用的 VETH 介面。 |
| **ip-address** | *IP* | | 分配給 VETH 介面的 IP 地址。 |
| **memory-current** | | | 應用當前使用的記憶體量。 |
| **name** | *string* | | YAML 配置的 `name` 引數中定義的應用名稱。 |
| **project-page** | *string* | | YAML 配置的 `page` 引數中定義的應用專案頁面 URL。 |
| **running** | | | 指示應用當前是否正在執行。 |
| **status** | *acquire veth* &#124; *configuring container(s)* &#124; *downloading/extracting* &#124; *starting* | | 應用的當前狀態。可能的值表示應用正在獲取 VETH 介面、配置容器、下載/解壓或啟動。 |
| **ui-url** | *string* | | 為應用 Web 介面生成的 URL（如果可用）。 |
| **variables-to-be-used-in-environment** | | | 應用環境中存在的所有變數的列表。 |

#### 設定嚮導 {#setup-wizard}

App 選單包含設定嚮導（GUI 中的“Setup”按鈕，或命令 `/app/setup`）。此嚮導會自動完成所有網路、儲存和登錄檔設定，否則這些設定需要多個手動步驟。

##### 第 1 步：儲存選擇 {#step-1-storage-selection}

選擇用於安裝應用的儲存磁碟。系統會自動檢測可用的已格式化磁碟驅動器（例如 nvme1、usb1、disk1 及類似裝置）。如果列表中沒有合適的磁碟，必須先使用 ext4 或 btrfs 檔案系統格式化磁碟，然後透過 `/disk` 選單掛載它。

**要求：**

- 建議順序讀寫速度至少為 100 MB/s。
- 建議隨機 IOPS（每秒輸入/輸出運算元）至少為 10,000。
- 在繼續之前，使用 `/disk/test` 命令驗證儲存效能。
- 強烈建議使用外部儲存裝置以獲得最佳效能。

##### 第 2 步：網橋配置 {#step-2-bridge-configuration}

選擇用於容器網路的 LAN 網橋介面。此配置會啟用自動埠轉發和本地網路上的應用自動發現。設定嚮導會自動配置以下內容：

- 建立虛擬乙太網（veth）介面
- 將 veth 介面新增到已配置的網橋
- 用於出站連線的 NAT 規則

##### 第 3 步：IP 配置 {#step-3-ip-configuration}

定義路由器的 IP 地址以允許訪問應用。系統會自動檢測主 IP 地址；不過，對於複雜網路設定，也支援手動配置。指定的 IP 地址用於以下目的：

- 生成應用 UI URL。
- 建立自動埠轉發規則。
- 提供 WebFig 整合連結。

##### 完成 {#completion}

完成設定嚮導後，App 系統即可立即使用。你可以直接透過介面啟用應用。系統會自動處理所有底層容器配置。

#### 配置 {#configuration}

可透過 `/app/settings` 訪問 App 配置，與手動容器配置相比，它提供了簡化的設定

## 屬性 {#properties-1}

| 屬性 | 型別 | 預設值 | 描述 |
| :-- | :-- | :-- | :-- |
| **app-store-urls** | *string* | *（空）* | 自定義應用商店的 URL。該 URL 必須指向一個 YAML 陣列，其中每個應用都是該陣列中的一個元素。 |
| **auto-update** | *yes* &#124; *no* | *no* | 為所有已安裝的應用軟體包啟用自動更新的全域性設定。 |
| **disk** | *string* | *（空）* | 指定將用於儲存操作的磁碟的全域性設定。 |
| **download-path** | *string* | *（空）* | 手動指定所有下載內容將儲存的目錄路徑。 |
| **lan-bridge** | *string* | *（空）* | 手動指定代表區域網路（LAN）的網橋介面。 |
| **media-path** | *string* | *（空）* | 手動指定所有媒體檔案將儲存的目錄路徑。 |
| **registry-mirrors** | *string* | *（空）* | 指定用於容器映象獲取的一個或多個登錄檔映象 URL 地址。 |
| **router-ip** | *IP* | *（空）* | 手動指定可訪問當前 RouterOS 裝置的 IP 地址。 |
| **show-in-webfig** | *yes* &#124; *no* | *yes* | 控制是否在 WebFig 登入頁面上顯示指向已啟用應用的連結。 |

### 自動配置的設定 {#auto-configured-settings}

某些引數最初會根據網路檢測自動配置。如有需要，始終可以手動覆蓋這些值。

| 屬性 | 型別 | 預設值 | 描述 |
| :-- | :-- | :-- | :-- |
| **assumed-router-ip** | *IP* | *（已檢測）* | 自動檢測到的 RouterOS 裝置的網路 IP 地址。 |
| **assumed-lan-bridge** | *string* | *（已檢測）* | 自動檢測到的用於 LAN 連線的網橋介面。 |
| **assumed-media-path** | *string* | *disk/media* | 預設媒體儲存路徑，通常位於系統磁碟上。 |
| **assumed-download-path** | *string* | *disk/media/downloads* | 預設下載目錄路徑，通常位於媒體儲存區域內。 |

#### 應用管理 {#application-management}

應用透過 `/app` 介面進行管理，提供與底層 `/container` 系統類似的狀態監控和生命週期控制：

```
/app> print 
Flags: X - DISABLED, R - RUNNING
Columns: NAME, UI-URL, MEMORY-CURRENT, APP-SIZE, DATA-SIZE, CATEGORY, DESCRIPTION
```

##### 狀態指示符和元資料 {#status-indicators-and-metadata}

- **標誌：**
  - X（DISABLED）- 可以表示兩種狀態：未下載/未安裝（APP-SIZE 和 DATA-SIZE 將為空），或已下載但已停用（APP-SIZE 和 DATA-SIZE 顯示儲存佔用）。
  - R（RUNNING）- 應用正在執行且可訪問。
- **UI-URL：** 應用執行時可直接訪問 Web 介面的 URL。
- **MEMORY-CURRENT：** 即時記憶體消耗，單位為 MiB（僅在執行時）。
- **APP-SIZE：** 容器映象儲存消耗，單位為 MiB（下載後顯示已用空間）。
- **DATA-SIZE：** 應用持久資料大小，單位為 KiB/MiB（顯示配置和使用者資料）。
- **CATEGORY：** 應用功能分類。
- **DESCRIPTION：** 應用功能描述。

##### 應用生命週期管理 {#application-lifecycle-management}

### 部署過程 {#deployment-process}

與需要多個配置步驟（veth 介面、網橋設定、環境變數、掛載和防火牆規則）的手動容器部署不同，App 部署會自動完成整個過程：

1. **選擇：** 透過 CLI 或 WebFig 從目錄中選擇一個應用。
2. **下載：** 自動下載並解壓容器映象。
3. **網路設定：** 自動配置 veth 介面和網橋。
4. **埠轉發：** 自動建立用於 Web 訪問的防火牆規則。
5. **啟動：** 使用預配置設定初始化容器。
6. **訪問：** UI-URL 變為可用，可立即訪問 Web 介面。

#### 清理命令 {#cleanup-command}

清理命令會完全移除應用，包括所有關聯資料。此操作具有破壞性且不可逆：

```
/app> cleanup pihole 
App data will be lost, continue? [y/N]:
```

**清理過程：**

1. 停止正在執行的容器。
2. 移除所有應用資料和配置檔案。
3. 從儲存中刪除容器映象。
4. 將應用重設為未安裝狀態（APP-SIZE 和 DATA-SIZE 為空）。
5. 移除該應用特定的網路配置。

:::warning

所有使用者資料、配置設定和應用狀態都將永久丟失。清理後，應用將返回其原始目錄狀態，並需要完全重新配置。

:::

#### 使用者可新增的應用 {#user-addable-apps}

從 RouterOS v7.22 開始，你可以使用 compose YAML 檔案建立自己的自定義應用。這使有經驗的使用者能夠構建適合其特定網路需求的解決方案。

工作原理：

- 你編寫一個 compose YAML 檔案，用於定義應用的結構和行為
- RouterOS 處理此檔案以構建可用的應用軟體包
- 你的自定義應用可以使用 RouterOS 功能和 API

為什麼使用它：

- 精確構建你的網路所需的內容
- 無需等待官方應用釋出
- 非常適合自動化、自定義路由或專用服務
- 宣告式設定使管理更容易

## 使用 YAML 建立自定義應用 {#creating-a-custom-app-with-yaml}

你可以使用 YAML 配置檔案建立自定義容器應用。此示例演示如何設定一個執行 iperf3 伺服器以進行網路效能測試的 Alpine Linux 容器。

### YAML 配置示例 {#yaml-configuration-example}

```routeros
name: alpine-iperf
descr: Alpine Linux container running iperf3 server
page: https://iperf.fr/
category: network
default-credential: none
services:
  iperf:
    image: docker.io/alpine:latest
    ports:
      - 5201:5201:tcp
      - 5201:5201:udp
    command: /bin/sh -c "apk add --no-cache iperf3 && iperf3 -s"
```

### 配置欄位參考 {#configuration-field-reference}

| 欄位 | 描述 |
|---|---|
| `name` | 自定義應用的唯一識別符號 |
| `descr` | 應用功能的可讀描述 |
| `page` | 專案官方文件或網站的 URL |
| `category` | 分類分組（例如 network、system、utilities） |
| `default-credential` | 認證要求（none，或指定使用者名稱/密碼） |
| `services` | 容器服務定義 |
| `image` | 用於容器的 Docker 映象 |
| `ports` | 格式為 `host:container:protocol` 的埠對映 |
| `command` | 在容器內執行的啟動命令 |

### 此示例如何工作 {#how-this-example-works}

1. **基礎映象：** 使用來自 Docker Hub 的官方 Alpine Linux 映象
2. **軟體包安裝：** 安裝 iperf3 網路效能測試工具
3. **伺服器模式：** 以伺服器模式（`-s` 標誌）執行 iperf3，以接受用戶端連線
4. **埠暴露：** 將 TCP 和 UDP 埠 5201（iperf3 的預設埠）對映到主機

此配置會建立一個充當網路吞吐量測試伺服器的容器，讓你可以測量用戶端與該容器之間的頻寬。

## 新增自定義應用 {#adding-a-custom-app}

建立自定義應用有兩種方式：匯入 .yml 檔案，或建立空白應用並直接編輯其 YAML。

在此示例中，我們將新增之前使用 compose 檔案建立的 alpine-iperf 應用。為便於使用，我們會將其放入 LAN 網橋，以便網路中的裝置無需 NAT 即可輕鬆訪問它。

### 方法 1：建立空白應用並編輯 YAML {#method-1-create-a-blank-app-and-edit-yaml}

首先，建立應用並將其分配到 LAN 網路：

```routeros
/app/add network=lan
```

預設情況下，應用將命名為“app”。

接下來，新增 YAML 配置。在終端中執行：

```routeros
/app/edit app yaml
```

這會開啟一個文字編輯器，你可以在其中貼上 YAML。粘貼後，按 <kbd>Control</kbd>+<kbd>O</kbd> 儲存更改。最後，啟用應用以使其開始執行。

### 方法 2：從檔案匯入 {#method-2-import-from-a-file}

或者，將 compose 文字儲存到檔案並上傳到裝置。然後，使用以下命令將該檔案設定為應用的 YAML：

```routeros
/app/add yaml=[/file/get alpine-iperf.yml contents]
```

當你已有準備好匯入的預配置 YAML 檔案時，此方法很有用。

#### 提示和最佳實踐 {#tips-and-best-practices}

- **儲存：** 為獲得最佳效能和更大容量，請考慮使用外部儲存裝置，例如 USB 驅動器、SATA 驅動器或 NVMe SSD。

- **記憶體：** 在終端中執行 `/app/print` 命令來跟蹤應用的記憶體消耗。

- **更新：** 僅在需要且認為必要時更新系統。雖然自動更新可以提供安全補丁和新功能，但在啟用或應用更新之前，評估你的特定用例是否需要更新很重要。

- **網路：** 應用會自動管理埠轉發，並生成用於外部訪問的必要 URL。

- **資料永續性：** 你的應用資料儲存在指定儲存路徑中，即使應用重啟或系統重啟後也會保持不變。
