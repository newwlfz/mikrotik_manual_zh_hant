---
sidebar_key: "hardware/disks/index"
sidebar_position: 1
title: "磁碟"
sidebar_label: "磁碟"
description: "本頁介紹 MikroTik RouterOS 中的磁碟管理，涵蓋儲存裝置檢測、格式化、交換空間和 S.M.A.R.T. 監控。它說明了如何新增外部驅動器、管理掛載點、使用各種檔案系統格式化磁碟以及使用 RAID 功能。它還強調了安全彈出磁碟以防止資料丟失。"
tags:
  - 'disks'
  - 'storage'
  - 'filesystem'
source: https://manual.mikrotik.com/docs/7.24/hardware/disks
captured_at: '2026-11-04T11:29:18+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 RouterOS 上的物理磁碟處理——磁碟檢測、格式化、交換空間和 S.M.A.R.T.。有關網路儲存協定（iSCSI、NFS、SMB、NVMe over TCP）、RAID、檔案系統（Btrfs）以及 ROSE 包新增的其他功能，請參閱 [儲存](../../storage/index.md) 章節。

## 概述 {#summary}

**子選單：** `/disk`

此選單會列出所有已連線的儲存裝置，前提是這些裝置受支援且處於正常工作狀態。對於帶有 SD/CF/USB/SATA/NVMe 插槽的 RouterBOARD 裝置以及配備額外專用儲存驅動器的 x86 系統來說，這尤其有用，因為內建儲存通常相當小。當你需要大型 User Manager 資料庫、代理快取，或可能需要在路由器上使用 SMB 共享時，外部驅動器會很有幫助。

你可以新增任意數量的外部或輔助驅動器，併為上述每種功能用途選擇任意數量的驅動器。例如，User Manager 可以使用三個磁碟裝置，其中一個作為活動資料庫，其餘作為備份。然後你可以新增第四個磁碟，將活動資料複製到它上面，解除安裝它，拔下它，並把它移到另一臺伺服器上以繼續使用實際資料庫。這樣遷移和備份就很容易。

磁碟的名稱基於其物理連線位置。

:::info
**[儲存](../../storage/index.md)** 包增加了磁碟監控、高階檔案系統、RAID、rsync、iSCSI、NVMe over TCP、NFS 和 SMB 用戶端。詳情請參閱 [儲存](../../storage/index.md) 章節。

:::

:::danger
**在從 RouterOS 裝置上物理移除任何磁碟之前，請始終使用 `/disk/eject` 以防止資料丟失！**

:::

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **eject**| 使用分配給所選驅動器的 "slot" 安全解除安裝（彈出）該驅動器。執行此命令後，即可將其從主機裝置中移除。 |
| **format**| 啟動磁碟格式化流程的命令。包含自身的附加屬性。例如 "file-system" 和 "label"。選擇應格式化的磁碟（slot）。file-system ('exfat', 'ext4', 'fat32', 'xfs', 'btrfs', 'discard', 'discard-secure', 'wipe') - 應用可用檔案系統型別之一；也可用於丟棄儲存塊（等同於 blkdiscard）或安全擦除（覆蓋）資料。mbr-partition-table - 建立 mbr 分割區表 |
| **trim** | 為提升效能而丟棄未使用的資料塊（等同於 fstrim）。某些 NVMe 硬碟盒可能不支援磁碟 trim。 |
| **reset-counters** | 重設磁碟（slot）統計資訊 |
| **monitor-traffic** | 檢查即時磁碟效能和健康狀態統計資訊 |
| **test** | 允許對所選裝置執行效能測試（從 RouterOS 7.16 起可用）disk - 用於測試的裝置；direction - ('read','write')；duration - (int)；pattern - ('random', 'sequential')；thread-count - (int)；block-size - 用於測試的塊大小；type - ('device', 'filesystem') |
| **mount-read-only** | 設定為 *yes* 時，將已掛載磁碟設為只讀模式。 |
| **mount-point-template** | 設定檔案系統的掛載點。可以根據磁碟將掛載點設定為以下引數：[slot]（預設）- 將掛載點設定為 slot 名稱。[model] - 將掛載點設定為裝置型號名稱。[serial] - 將掛載點設定為裝置序列號。[fw-version] - 將掛載點設定為裝置韌體版本。[fs-label] - 將掛載點設定為裝置檔案系統標籤。[fs-uuid] - 將掛載點設定為裝置 UUID。[fs] - 將掛載點設定為裝置檔案系統。 `/disk/set nvme1 mount-point-template="[model]"`   此外，可以組合多個變數來建立單個掛載點：  `/disk/set nvme1 mount-point-template="[model]-[fs]"`    |

## 標誌 {#flags}

| 屬性 | 描述 |
| :-- | :-- |
| **X - disabled** | 已停用的裝置 |
| **E - empty** | 空插槽 |
| **B - BLOCK-DEVICE** | "B - BLOCK-DEVICE" 標誌表示該裝置使用塊進行輸入/輸出操作。在 RouterOS 的上下文中，這一區分至關重要，因為它有助於判斷裝置是作為資料載體執行，還是僅提供有關磁碟佈局結構的資訊。當考慮其後方帶有裝置的擴充套件器時，這一差異就變得重要。如果裝置標記為字母 "B"，則表示它可以用作儲存或記憶體。相反，沒有 "B" 標記的裝置主要用於理解磁碟結構。這讓你可以快速識別 PCIe 或 SAS 擴充套件器的存在，並檢測第一個擴充套件器中是否有驅動器。此外，它還允許你估算每個裝置所連線連線的速度。然而，"B" 標誌最顯著的好處是能夠立即指示裝置是否可格式化或用於 RAID 目的。 |
| **M - mounted** | 已掛載分割區 |
| **F - formatting** | 該裝置當前正在格式化 |
| **p - partition** | 該裝置有一個分割區 |
| **f - raid-member-failed** | 這些選項與 [ROSE](../../storage/index.md) 包一起使用。 |
| **r - raid-member** |  |
| **c - encrypted** |  |
| **g - guid-partition-table** |  |
| **t - nvme-tcp-export** |  |
| **i - iscsi-export** |  |
| **s - smb-sharing** |  |
| **n - nfs-sharing** |  |
| **O - tcg-opal-self-encryption-enabled** |  |
| **o - tcg-opal-self-encryption-supported** |  |

## 設定 {#settings}

| 屬性 | 說明 |
| :-- | :-- |
| **auto-smb-sharing** (yes \| no; Default: ) | 當在 "/disk" 中新增新的磁碟/分割區項時，啟用動態 SMB 共享 |
| **auto-smb-user** (list of strings; Default: ) | 當在 "/disk" 中新增新的磁碟/分割區項時，smb-sharing/smb-user 設定的預設值 |
| **auto-media-sharing** (yes \| no; Default: ) | 當在 "/disk" 中新增新的磁碟/分割區項時，動態啟用 DLNA |
| **auto-media-interface** (list of strings; Default: ) | 當在 "/disk" 中新增新的磁碟/分割區項時，用於 `/ip/media` 動態例項的介面 |
| **default-mount-point-template** (string, Default: ) | 為 "/disk" 中新增的每個項設定預設掛載點模板 |

:::note

### 說明 {#notes}

當 "auto-smb-sharing=yes" 且 "/ip/smb/share enabled=auto" 時，儲存裝置物理插入後 SMB 伺服器會被啟用

:::

## 示例 {#examples}

### 格式化已連線的儲存裝置 - 簡單 {#formatting-attached-storage-unit---simple}

1. 磁碟已連線，並且已由系統自動掛載。

```ros
[admin@MikroTik] > disk print
Flags: B - BLOCK-DEVICE; M, F - FORMATTING
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS
#    SLOT  MODEL           SERIAL            INTERFACE                  SIZE           FREE  FS
0 BM usb1  USB Flash Disk  FBA0911260071572  USB 2.00 480Mbps  2 004 877 312  1 921 835 008  ext4
```

```ros
[admin@MikroTik] > /file/print
 # NAME                        TYPE          SIZE CREATION-TIME
 0 skins                       directory          1970-01-01 03:00:01
 1 pub                         directory          1970-02-04 21:31:40
 2 usb1                        disk               2022-03-07 14:05:16
```

1. 格式化磁碟，可使用任一受支援的檔案系統（ext4、fat32、exfat、xfs、btrfs）。

```ros
[admin@MikroTik] > /disk/format usb1 file-system=ext4 mbr-partition-table=no
  formatted: 100%
```

1. 完成！驅動器已格式化，格式化過程結束後應會自動掛載。

### 格式化已連線的儲存裝置 - 詳細 {#formatting-attached-storage-unit---detailed}

在進行手動格式化之前，請確保儲存裝置已正確連線到你的 RouterOS 裝置。如果儲存裝置包含受支援的檔案系統和分割區表，系統會自動嘗試掛載它。掛載後，裝置會在插入後不久出現在 `/file` 選單中。

如果儲存裝置未被自動檢測或掛載，請按以下步驟操作：

1. 透過檢查磁碟選單，確認路由器能識別已連線的儲存裝置：

```ros
[admin@MikroTik] > disk print
Flags: B - BLOCK-DEVICE; M, F - FORMATTING
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS
#    SLOT  MODEL           SERIAL            INTERFACE                  SIZE           FREE  FS
0 BM usb1  USB Flash Disk  FBA0911260071572  USB 2.00 480Mbps  2 004 877 312  1 921 835 008  ext4
```

此輸出確認系統檢測到儲存驅動器，並顯示其當前檔案系統型別。

1. 透過檢查檔案選單，確認磁碟已掛載：

```ros
[admin@MikroTik] > /file/print
 # NAME     TYPE    SIZE CREATION-TIME
 0 usb1     disk         2022-03-07 14:05:16
 1 skins    directory    1970-01-01 03:00:01
 2 pub      directory    1970-02-04 21:31:40
```

1. 要格式化驅動器，請使用磁碟 slot 名稱或 ID，以及你首選的檔案系統（ext4、fat32、exfat、xfs 或 btrfs）。你還可以為裝置分配標籤，並指定是否建立 MBR 分割區表：

```ros
[admin@MikroTik] > /disk/format usb1 file-system=ext4 label=usb-flash mbr-partition-table=yes
  formatted: 100%
```

:::note
**注意：** 格式化過程會顯示進度百分比指示。較大的儲存驅動器可能需要更長時間才能完成。請等待過程結束後再移除裝置。

:::

### 建立多個磁碟分割區 {#creating-multiple-disk-partitions}

要建立多個 GPT 分割區，請在沒有分割區表的情況下格式化驅動器，然後手動新增分割區：

```ros
[admin@MikroTik] > /disk/format usb1 file-system=ext4 label=usb-flash mbr-partition-table=no
  formatted: 100%
```

```ros
[admin@MikroTik] > /disk/add type=partition parent=usb1 partition-size=200M
[admin@MikroTik] > /disk/add type=partition parent=usb1 partition-size=500M
[admin@MikroTik] > /disk/add type=partition parent=usb1 slot=usb1-last-partition
```

:::info
**說明：**

- slot 名稱（分割區或磁碟）會自動分配，但可以使用 `slot` 引數手動指定。
- 未指定分割區大小時，最後一個分割區將使用剩餘可用空間。
- 要調整分割區的起始位置，請使用 `partition-offset` 引數。

:::

### Web-Proxy 快取配置示例 {#web-proxy-cache-configuration-example}

在 IP -> Proxy 選單下輸入代理快取路徑，Web 代理儲存會自動建立在檔案選單中。如果使用不存在的目錄路徑，也會自動建立一個額外的子目錄。

```ros
[admin@MikroTik] >  /ip/proxy/set cache-path=usb1/cache-n-db/proxy/

...

[admin@MikroTik] >  /file/print
 # NAME                                              TYPE                             SIZE CREATION-TIME       
 0 skins                                             directory                             2015-03-02 18:56:23
 1 sys-note.txt                                      .txt file                        23   2015-07-03 11:40:48
 2 usb1                                             disk                                  2015-07-03 11:35:05
 3 usb1/lost+found                                  directory                             2015-07-03 11:34:56
 4 usb1/cache-n-db                                  directory                             2015-07-03 11:41:54
  5 usb1/cache-n-db/proxy                            web-proxy store                       2015-07-03 11:42:09
```

### 磁碟日誌配置示例 {#log-on-disk-configuration-example}

在配置磁碟日誌記錄時，請確保手動建立要用於儲存日誌檔案的目錄，因為在這種情況下，不存在的目錄不會自動建立。

```ros
[admin@MikroTik] >  /system/logging/action/set disk disk-file-name=disk1/log

...

[admin@MikroTik] >  /file/print where name~"disk1/log"
 # NAME                                              TYPE                             SIZE CREATION-TIME       
 0 disk1/log                                        directory                             2015-07-03 12:44:09
 1 disk1/log/syslog.0.txt                           .txt file                         160 2015-07-03 12:44:11
```

:::note
**注意：** 類似 firewall、web-proxy 以及一些其他傾向於在系統 NAND 磁碟上儲存大量日誌或快速列印日誌的日誌主題，可能會導致其更快磨損，因此在這種情況下建議使用一些已連線的儲存或遠端日誌記錄，或者將資料儲存到 RAM 資料夾中

:::

### 為資料夾分配 RAM {#allocate-ram-to-folder}

可以將資料夾連結到 RAM。資料夾會在重啟或斷電時清空。  
RAM 會填充到 tmpfs-max-size，如果未提供此變數——則最多填充可用 RAM 的 1/2。

```ros
[admin@MikroTik] >  /disk/add type=tmpfs tmpfs-max-size=100M
[admin@MikroTik] > file print 
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME            TYPE       SIZE             CREATION-TIME       
0  tmp1             disk     100 003 840        2022-12-12 11:01:48
```

### 測試磁碟效能 {#test-disk-performance}

:::danger
磁碟效能測試可能會緩慢降低磁碟健康狀態

在寫入測試中，磁碟上的所有檔案和檔案系統都將被銷燬

:::

從 7.16 開始可以執行磁碟效能測試。磁碟必須處於停用狀態，或者沒有可掛載的檔案系統（未格式化）。  
檢查可用磁碟，如果磁碟已掛載——請將其停用。

```ros
[admin@MikroTik] > /disk/print
Flags: B - BLOCK-DEVICE; M - MOUNTED
Columns: SLOT, MODEL, SERIAL, INTERFACE, SIZE, FREE, FS
#    SLOT  MODEL             SERIAL         INTERFACE                    SIZE            FREE  FS
0 BM usb1  JMicron External  DD56419883891  USB 3.10 5000Mbps  64 023 257 088  62 692 188 160  ext4

[admin@MikroTik] > disk disable usb1

[admin@MikroTik] > disk test disk=usb1 pattern=sequential  type=device thread-count=4 block-size=4K direction=write
Columns: SEQ, RATE, IOPS, DISK, TYPE, PATTERN, DIR, BSIZE, THREADS
SEQ  RATE          IOPS  DISK  TYPE    PATTERN     DIR    BSIZE  THREADS
0    1622.5Mbps  49 516  usb2  device  sequential  write   4096        4
1    26.2Mbps       800  usb2  device  sequential  write   4096        4
2    33.0Mbps     1 008  usb2  device  sequential  write   4096        4
3    11.7Mbps       360  usb2  device  sequential  write   4096        4
4    28.5Mbps       872  usb2  device  sequential  write   4096        4
5    34.6Mbps     1 056  usb2  device  sequential  write   4096        4
6    33.8Mbps     1 032  usb2  device  sequential  write   4096        4
TOT  255.7Mbps    7 806  usb2  device  sequential  write   4096        4

```

### 交換空間 {#swap-space}

可以向 RouterOS 裝置新增交換空間。當在 RouterOS 上使用[容器](../../containers/index.md)來執行需要比 RouterOS 裝置多得多的 RAM 的容器時，這很有用。你可以將磁碟（或分割區）用作交換空間，或將檔案用作交換空間。

#### 交換分割區 {#swap-partition}

交換分割區要求你的 RouterOS 裝置上連線有磁碟（或分割區）。整個磁碟（或分割區）都將用作交換空間，不能用於其他用途。請確保為交換分割區使用高速磁碟。使用交換分割區的效能比使用交換檔案更好。   |

要將磁碟（或分割區）用作交換分割區，可以使用以下命令：

```routeros
/disk/set disk1 swap=yes   
```

請確保將 `disk1` 改為你正確的磁碟名稱！

#### 交換檔案 {#swap-file}

交換檔案要求你有一個已使用檔案系統格式化的磁碟，例如 [Btrfs](../../storage/btrfs/index.md)。與交換分割區選項相比，整個磁碟（或分割區）不會用作交換空間，只會使用磁碟（或分割區）上交換檔案的大小。使用交換檔案的效能低於使用交換分割區。

要在現有檔案系統上建立交換檔案，可以使用以下命令：

```routeros
/disk/add type=file file-path=disk1/swapfile file-size=1G swap=yes
```

請確保將 `disk1` 改為你磁碟掛載的正確路徑。

### 掛載映象 {#mount-images}

RouterOS 還可以直接掛載 **.iso** 和 **.squashfs** 映象。要掛載映象，請使用以下命令：

```routeros
/disk/add type=file file-path=disk1/mycopy.iso 
```

請確保將 `disk1/mycopy.iso` 改為映象所在位置對應的正確路徑。
