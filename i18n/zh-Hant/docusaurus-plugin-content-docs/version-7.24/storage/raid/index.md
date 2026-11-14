---
sidebar_key: "storage/raid/index"
sidebar_position: 3
title: "RAID"
sidebar_label: "RAID"
description: "RouterOS 中的 RAID 技術可跨多個驅動器實現資料儲存，並提升效能與保護能力，支援 RAID 級別 0、1、4、5、6、linear 和巢狀配置。該頁面詳細介紹了 RAID 型別、塊大小、裝置數量等屬性，以及設定 RAID6 的配置示例。"
tags:
  - 'raid'
  - 'storage'
  - 'configuration'
source: https://manual.mikrotik.com/docs/7.24/storage/raid
captured_at: '2026-11-04T11:33:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](../index.md) 軟體包。
:::

RAID（獨立磁碟冗餘陣列）技術允許將資料儲存在多個磁碟上——透過將它們組合成邏輯單元，從而提高資料傳輸效能、資料保護能力，或兩者兼而有之。

在 RAID 磁碟發生故障的情況下，更換故障磁碟後會自動開始重建。

RouterOS 支援軟體 RAID 級別 0、1、4、5、6、linear 以及巢狀 RAID。

<DocCardList />

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **raid-type** | 使用的 RAID 型別（級別 0、1、4、5、6、linear 以及巢狀 RAID。） |
| **raid-chunk-size** | RAID 陣列中使用的塊或條帶的大小。 |
| **raid-device-count** | RAID 陣列中包含的裝置（磁碟）數量。 |
| **raid-master** | 建立的 RAID 主塊裝置，磁碟將被新增到其中。 |
| **raid-max-component-size** | RAID 陣列中單個元件或磁碟的最大大小。 |
| **raid-member-failed** | 將 RAID 陣列中的磁碟設定為故障狀態。在需要更換未故障磁碟時使用 |
| **raid-role** | 定義 RAID 陣列中每個裝置的角色。 |
| **raid-scrub** | 驗證並修復 RAID 陣列中的資料完整性。 |

### 配置示例（RAID6） {#configuration-example-raid6}

這是一個如何配置 RAID 的示例。大多數 RAID 型別的操作步驟相同

建立 RAID 塊裝置（在本示例中為 RAID 6）

```ros
add raid-device-count=20 raid-type=6 slot=raid1 type=raid
```

將磁碟新增到此 RAID

```ros
set nvme1 raid-master=raid1 raid-role=0
set nvme2 raid-master=raid1 raid-role=1
set nvme3 raid-master=raid1 raid-role=2
set nvme4 raid-master=raid1 raid-role=3
set nvme5 raid-master=raid1 raid-role=4
set nvme6 raid-master=raid1 raid-role=5
set nvme7 raid-master=raid1 raid-role=6
set nvme8 raid-master=raid1 raid-role=7
set nvme9 raid-master=raid1 raid-role=8
set nvme10 raid-master=raid1 raid-role=9
set nvme11 raid-master=raid1 raid-role=10
set nvme12 raid-master=raid1 raid-role=11
set nvme13 raid-master=raid1 raid-role=12
set nvme14 raid-master=raid1 raid-role=13
set nvme15 raid-master=raid1 raid-role=14
set nvme16 raid-master=raid1 raid-role=15
set nvme17 raid-master=raid1 raid-role=16
set nvme18 raid-master=raid1 raid-role=17
set nvme19 raid-master=raid1 raid-role=18
set nvme20 raid-master=raid1 raid-role=19

```

格式化 RAID 塊裝置

```ros
/disk> format raid1 file-system=ext4 
```

結果應類似於以下內容

```ros
21 BM        type=raid slot="raid1" slot-default="" parent=none uuid="f457bc79-7408-489b-8850-85923e900452" fs=ext4 model="RAID6 2-parity-disks" 
             size=17 283 541 893 120 free=17 283 538 190 336 raid-type=6 raid-device-count=20 raid-max-component-size=none raid-chunk-size=1M raid-master=none 
             raid-state="clean" nvme-tcp-export=no iscsi-export=no nfs-sharing=no smb-sharing=no media-sharing=no media-interface=none 

```

:::warning
避免在多個 RAID 陣列中使用單個物理磁碟上的多個分割區。在多個 RAID 陣列中使用同一物理磁碟可能會導致效能低下。
:::

### 示例：RAID 檢查 {#example-raid-check}

監控 RAID 陣列是否發生故障極為重要。有多種方法可以做到這一點，但最簡單的方法是建立一個指令碼，在 RAID 成員發生故障時傳送電子郵件。您可以將以下指令碼作為可用的示例：

```routeros
/system/scheduler
add interval=30s name=MRaidHealthCheckCall on-event=MraidHealthCheck policy=ftp,read,write,policy,test,sniff start-time=startup
/system/script
add dont-require-permissions=no name=MraidHealthCheck owner=admin policy=ftp,read,write,policy,test,sniff source=":global CheckRAID;\
    \n:local sysadmin; \
    \n\
    \n:set  \$sysadmin \"<servername@domain.tld>\";\
    \n\
    \n:local temp [/disk/print count-only where raid-member-failed];\
    \n:if ( \$temp > 0 ) do={\
    \n   :if ( \$CheckRAID < 1 ) do={\
    \n      /log/info message=\"ERROR: RAID has failed!\";\
    \n      /tool/e-mail/send to= \$sysadmin subject=([/system/identity/get name].\" RAID failed\") body=(\"Go check it! Value: \".\$temp);\
    \n      :set \$CheckRAID 7;\
    \n      :delay 5s;\
    \n    }\
    \n   }       \
    \n   :if ( \$CheckRAID > 0 ) do={\
    \n      :set \$CheckRAID ( \$CheckRAID -1 );\
    \n   }\
    \n"
```

您還需要配置 RouterOS 裝置的電子郵件伺服器設定：

```routeros
/tool/e-mail
set from=<raidcheck@domain.tld> port=587 server=smtp.domain.com tls=starttls
```

:::warning

請確保在 `/tool/e-mail` 下配置您的電子郵件伺服器設定，並將上述指令碼中的電子郵件地址更改為與您的電子郵件伺服器設定相匹配的值。

:::

## RAID 型別 {#raid-types}

### RAID 0 {#raid-0}

在此 RAID 中，所有資料均勻寫入所有磁碟，此配置不提供任何容錯能力，但可提供最佳效能。

![](/img/648d1b1a7e9ac005.webp)

### RAID 1 {#raid-1}

相同的資料寫入所有磁碟（資料被映象），此配置提供最佳容錯能力，但在效能方面，寫入速度將等於陣列中使用的最慢磁碟的速度。

![](/img/749039f2245fe4a2.webp)

### RAID 4 {#raid-4}

塊級資料條帶化分佈在資料磁碟上，奇偶校驗位儲存在專用磁碟上。效能將受限於奇偶校驗寫入速度。

![](/img/710561e575e1fdcb.webp)

### RAID 5 {#raid-5}

塊級資料均勻條帶化分佈在可用磁碟上。它可以從 1 塊磁碟故障中恢復。

![](/img/46c04c532fbe4a91.webp)

### RAID 6 {#raid-6}

塊級資料均勻條帶化分佈在可用磁碟上。它可以從 2 塊磁碟故障中恢復。

![](/img/f2a0c2f8196c22bb.webp)

### RAID 線性 {#raid-linear}

資料追加到多個磁碟上，將它們組合成一個單一的大磁碟。不提供冗餘，並且受限於單個磁碟的讀/寫速度。

![](/img/41c81336094120e1.webp)

### 巢狀 RAID {#nested-raid}

將多種 RAID 配置組合成另一種 RAID。例如 RAID 10（RAID 1+0）結合了磁碟映象（RAID 1）和磁碟條帶化（RAID 0）

![](/img/62c05c74537f6e74.webp)

#### 配置示例 {#configuration-example}

在本示例中，我使用 10 塊 SSD 磁碟並配置為 RAID（RAID 1+0）

建立 RAID 0 塊

```ros
add raid-device-count=5 raid-type=0 slot=raid10 type=raid
```

建立五個 RAID 1 塊，每個包含 2 個裝置，並將它們新增到之前建立的 RAID 0 塊（name=raid10）中，將其設定為 master-raid

```ros
add raid-device-count=2 raid-master=raid10 raid-role=0 raid-type=1 slot=raid0 type=raid
add raid-device-count=2 raid-master=raid10 raid-role=1 raid-type=1 slot=raid1 type=raid
add raid-device-count=2 raid-master=raid10 raid-role=2 raid-type=1 slot=raid2 type=raid
add raid-device-count=2 raid-master=raid10 raid-role=3 raid-type=1 slot=raid3 type=raid
add raid-device-count=2 raid-master=raid10 raid-role=4 raid-type=1 slot=raid4 type=raid
```

將磁碟新增到每個 RAID 塊

```ros
set nvme1 raid-master=raid0 raid-role=0
set nvme3 raid-master=raid1 raid-role=0
set nvme5 raid-master=raid2 raid-role=0
set nvme7 raid-master=raid3 raid-role=0
set nvme9 raid-master=raid4 raid-role=0

set nvme2 raid-master=raid0 raid-role=1
set nvme4 raid-master=raid1 raid-role=1
set nvme6 raid-master=raid2 raid-role=1
set nvme8 raid-master=raid3 raid-role=1
set nvme10 raid-master=raid4 raid-role=1

```

之後格式化 raid10 塊

```ros
format raid10 file-system=ext4 
```

格式化後，您應該能看到可用空間並使用該塊

```ros
23 BM        type=raid slot="raid10" slot-default="" parent=none uuid="ec3344f4-1662-49ab-b899-db1aaa217b0f" fs=ext4 model="RAID0 striped" size=9 601 967 652 864 
             free=9 597 901 369 344 raid-type=0 raid-device-count=5 raid-max-component-size=none raid-master=none raid-state="clean" nvme-tcp-export=no 
             iscsi-export=no nfs-sharing=no smb-sharing=no media-sharing=no media-interface=none 
```

基於此配置，您可以修改 RAID 10 配置以適應您所需的儲存裝置數量。

同樣，也可以建立其他巢狀 RAID 配置，遵循示例中展示的相同原則。
