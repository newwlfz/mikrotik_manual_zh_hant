---
sidebar_key: "hardware/disks/index"
sidebar_position: 1
title: "磁碟"
sidebar_label: "磁碟"
description: "RouterOS 如何檢測、格式化和管理磁碟與分割區：槽位名稱、自動掛載、掛載點、分割區、交換空間、由 RAM 支援的資料夾、檔案系統檢查和效能測試。"
tags:
  - 'disks'
  - 'storage'
  - 'filesystem'
source: https://manual.mikrotik.com/docs/7.25/hardware/disks
captured_at: '2026-11-04T11:17:09+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

[*Disks CLI 參考*](../../cli-reference/disk/index.md)

RouterOS 會檢測連線到路由器的儲存驅動器（USB、SATA、NVMe 和 microSD 驅動器），並在啟動時或插入後自動掛載它們。你可以使用路由器支援數量的驅動器，例如用於 User Manager 資料庫、Web 代理快取、容器儲存或日誌檔案。

本頁介紹驅動器本身：如何檢測、格式化和管理驅動器。網路儲存協定（iSCSI、NFS、SMB、NVMe over TCP）、RAID 和高階檔案系統屬於 [儲存](../../storage/index.md) 包，並在 [儲存](../../storage/index.md) 章節中介紹。

:::info
**Storage 包**增加了磁碟監控、RAID、rsync、iSCSI、NVMe over TCP、NFS、SMB 用戶端以及 Btrfs 和 XFS 檔案系統。詳情請參見 [儲存](../../storage/index.md) 章節。
:::

:::danger
在從 RouterOS 裝置上物理移除磁碟之前，請始終使用 `/disk/eject`，否則資料可能丟失。
:::

## 磁碟檢測方式 {#how-disks-are-detected}

`/disk` 選單會列出所有受支援且處於工作狀態的已連線儲存裝置，包括空的驅動器插槽。每個驅動器都會根據其連線介面獲得一個插槽名稱和一個編號，例如 `usb1`、`sata1` 或 `nvme1`。

```ros
[admin@MikroTik] > /disk/print proplist=slot,model,interface,size,fs where slot=nvme9
Flags: B - BLOCK-DEVICE
Columns: SLOT, MODEL, INTERFACE, SIZE, FS
#   SLOT   MODEL        INTERFACE                   SIZE  FS
0 B nvme9  TS1TUTE210T  PCIe 2x8 GT/s  1 024 209 543 168  -
```

print 輸出中的關鍵標誌：

- `B - BLOCK-DEVICE` 標記儲存資料的裝置，因此可以對其進行格式化和使用。沒有此標誌的裝置（例如 PCIe 橋接器）僅描述磁碟佈局。
- `E - EMPTY` 標記空插槽。
- `M - MOUNTED` 標記已掛載檔案系統的磁碟或分割區。

完整的標誌列表在 [Disks CLI 參考](../../cli-reference/disk/index.md) 中描述。

具有受支援檔案系統和分割區表的驅動器會被自動掛載，並出現在 `/file` 中。要確認驅動器是否可用，請在連線後檢查它是否出現在 `/file` 中。

## 格式化磁碟 {#format-a-disk}

對新驅動器要做的第一件事就是格式化它。要格式化磁碟，請選擇檔案系統並使用插槽名稱執行 `/disk/format`。RouterOS 會請求確認，格式化驅動器並自動掛載它：

```ros
[admin@MikroTik] > /disk/format nvme9 file-system=ext4
nvme9: file-system: ext4
nvme9: mke2fs -t ext4 -L nvme9-fs /dev/nvme0n1
...
nvme9: Creating journal (262144 blocks): done
nvme9: Writing superblocks and filesystem accounting information: done
nvme9: format done
```

如果沒有標籤，RouterOS 會將檔案系統標記為 `<slot>-fs`，因此 `nvme9` 的標籤是 `nvme9-fs`。檔案系統選項：

- `ext4`  -  大多數用例的預設選擇。支援多個分割區、日誌記錄，並且速度快。
- `fat32` 和 `exfat`  -  幾乎任何裝置都可讀取，例如相機或 Android 手機。`fat32` 有 4 GB 檔案大小限制。
- `btrfs` 和 `xfs`  -  需要 [儲存](../../storage/index.md) 包的高階檔案系統。請參見 [Btrfs](../../storage/btrfs/index.md)。
- `discard` 和 `discard-secure`  -  丟棄驅動器的所有塊，不寫入檔案系統。
- `wipe` 和 `wipe-quick`  -  移除檔案系統和所有資料。`wipe` 會覆蓋資料，使其無法恢復；`wipe-quick` 僅移除檔案系統。

格式化會銷燬目標上的所有資料。對於檔案系統僅部分填充的磁碟，請使用 `file-system=wipe-quick` 快速移除它。

格式化後，驅動器會自動掛載：

```ros
[admin@MikroTik] > /disk/print where slot=nvme9
Flags: B - BLOCK-DEVICE; M - MOUNTED
Columns: SLOT, MOUNT-POINT, MODEL, INTERFACE, SIZE, FS
#    SLOT   MOUNT-POINT  MODEL        INTERFACE                   SIZE  FS
0 BM nvme9  nvme9        TS1TUTE210T  PCIe 2x8 GT/s  1 024 209 543 168  ext4
```

```ros
[admin@MikroTik] > /file/print where name~"nvme9"
Columns: NAME, TYPE, LAST-MODIFIED
# NAME              TYPE       LAST-MODIFIED
0 nvme9             disk       2026-09-25 11:47:05
1 nvme9/lost+found  directory  2026-09-25 11:47:05
```

## 掛載點 {#mount-points}

已掛載的檔案系統可透過其掛載點訪問，掛載點也是在 `/file` 中以及其他功能引用檔案時使用的路徑字首。預設情況下，掛載點是插槽名稱，因此 `nvme1` 上的檔案透過 `nvme1/...` 訪問。

如果同一驅動器在多次啟動之間可能位於不同插槽（例如在多盤位硬碟盒中），請使用 `mount-point-template` 為其指定穩定的掛載點。該模板可以組合以下變數：

- `[slot]`
- `[model]`
- `[serial]`
- `[fw-version]`
- `[fs-label]`
- `[fs-uuid]`
- `[fs]`

例如，按序列號掛載驅動器：

```ros
/disk/set nvme1 mount-point-template="[serial]"
```

變數可以組合使用，例如 `mount-point-template="[model]-[fs]"`。空模板會被拒絕。`/disk/settings` 中的 `default-mount-point-template` 設定會將模板應用於每個新磁碟和分割區。

## 分割區 {#partitions}

要將驅動器拆分為多個分割區，請在不使用分割區表的情況下格式化它，然後新增分割區。RouterOS 將分割區資訊儲存在 GUID 分割區表（GPT）中。

```ros
/disk/format nvme9 file-system=ext4
/disk/add type=partition parent=nvme9 partition-size=4G
```

```ros
[admin@MikroTik] > /disk/print where slot~"nvme9"
Flags: B - BLOCK-DEVICE; g - GUID-PARTITION-TABLE, p - PARTITION
Columns: SLOT, MODEL, INTERFACE, SIZE, FS
#    SLOT         MODEL        INTERFACE                   SIZE  FS
0 Bg nvme9        TS1TUTE210T  PCIe 2x8 GT/s  1 024 209 543 168  -
1 Bp nvme9-part1  TS1TUTE210T                     4 000 000 000  -
```

每個分割區都會獲得自己的插槽名稱，它由父級派生而來：`nvme9` 的第一個分割區是 `nvme9-part1`。`g - GUID-PARTITION-TABLE` 標誌標記父級，`p - PARTITION` 標記分割區。

- 如果沒有 `partition-size`，分割區將使用驅動器上的所有剩餘空間。
- 使用 `partition-offset` 設定分割區的起始位置（以位元組為單位）。
- 分割區的使用方式與磁碟類似：格式化、掛載並在其自己的插槽名稱下管理它。
- `/disk/format` 中的 `mbr-partition-table=yes` 會改為寫入 MBR 分割區表；僅當目標系統不接受 GPT 表時才使用它。

## 交換空間 {#swap-space}

:::info
交換空間需要 [container](../../containers/index.md) 包。
:::

交換空間保留給[容器](../../containers/index.md)，使它們能夠以超過路由器物理記憶體的記憶體執行。交換空間可以是整個分割區或一個檔案。交換空間大小限制為路由器可用 RAM 的 10 倍。

交換分割區將整個磁碟或分割區專用於交換，效能優於交換檔案：

```ros
/disk/set nvme9-part1 swap=yes
```

交換檔案位於現有檔案系統上，例如 [Btrfs](../../storage/btrfs/index.md) 磁碟上，並且只使用與其大小相同的空間：

```ros
/disk/add type=file file-path=nvme9-part1/swapfile file-size=512M swap=yes
```

交換檔案會以 `S - SWAP-ENABLED` 標誌出現在 `/disk` 中：

```ros
[admin@MikroTik] > /disk/print where slot~"nvme9"
Flags: B - BLOCK-DEVICE; M - MOUNTED, S - SWAP-ENABLED
       g - GUID-PARTITION-TABLE, p - PARTITION
Columns: SLOT, MOUNT-POINT, SIZE, FS, SWAP
#     SLOT                       MOUNT-POINT               SIZE  FS    SWAP
0 B g nvme9                                   1 024 209 543 168  -     no
1 BMp nvme9-part1                nvme9-part1      4 000 000 000  ext4  no
2  S  file-nvme9-part1-swapfile                     536 866 816  -     yes
```

## 基於 RAM 的資料夾 {#ram-backed-folder}

要將檔案儲存在 RAM 中，請新增一個 `tmpfs` 資料夾。路由器重啟或斷電時，其內容會被清空。

```ros
/disk/add type=tmpfs tmpfs-max-size=100M
```

該資料夾會作為磁碟條目出現在 `/file` 中，例如 `tmp1`。`tmpfs-max-size` 限制該資料夾可以使用的 RAM 量。在儲存空間有限的裝置上，或對於必須在重啟時清除的資料，請使用基於 RAM 的資料夾。有關大小限制、共享以及重啟後會發生什麼，請參見 [臨時檔案系統（Tmpfs）](../../storage/tmpfs.md)。

## 掛載映象 {#mount-images}

RouterOS 還可以直接掛載 `.iso` 和 `.squashfs` 映象。要掛載映象，請使用以下命令：

```ros
/disk/add type=file file-path=disk1/mycopy.iso
```

請確保將 `disk1/mycopy.iso` 改為映象所在位置對應的正確路徑。

## 磁碟日誌 {#log-on-disk}

在配置磁碟日誌記錄時，請確保手動建立要儲存日誌檔案的目錄，因為在這種情況下，不存在的目錄不會自動建立。

```ros
[admin@MikroTik] >  /system/logging/action/set disk disk-file-name=disk1/log
```

日誌檔案會出現在 `/file` 中你建立的目錄下：

```ros
[admin@MikroTik] >  /file/print where name~"disk1/log"
 # NAME                                              TYPE                             SIZE CREATION-TIME
 0 disk1/log                                        directory                             2015-07-03 12:44:09
 1 disk1/log/syslog.0.txt                           .txt file                         160 2015-07-03 12:44:11
```

:::note
防火牆和 web-proxy 等日誌主題往往會在系統 NAND 磁碟上儲存大量或快速列印的日誌，這會加速其磨損。在這種情況下，請使用附加儲存或遠端日誌記錄，或將資料儲存在 RAM 資料夾中。
:::

## 磁碟上的 Web 代理快取 {#web-proxy-cache-on-a-disk}

Web 代理將其快取儲存在磁碟上，通常是 USB 驅動器。在 `IP -> Proxy`（`/ip/proxy` 的 `cache-path` 設定）下設定快取路徑，Web 代理儲存會自動在 `/file` 中建立。如果使用不存在的目錄路徑，額外的子目錄也會自動建立：

```ros
[admin@MikroTik] >  /ip/proxy/set cache-path=usb1/cache-n-db/proxy/
```

```ros
[admin@MikroTik] >  /file/print
 # NAME                                              TYPE                             SIZE CREATION-TIME
 0 skins                                             directory                             2015-03-02 18:56:23
 1 sys-note.txt                                      .txt file                        23   2015-07-03 11:40:48
 2 usb1                                             disk                                  2015-07-03 11:35:05
 3 usb1/lost+found                                  directory                             2015-07-03 11:34:56
 4 usb1/cache-n-db                                  directory                             2015-07-03 11:41:54
 5 usb1/cache-n-db/proxy                            web-proxy store                       2015-07-03 11:42:09
```

快取配置請參見 [Web 代理](../../network-management/proxy/web-proxy.md)。

## 檢查和修復 {#check-and-repair}

`/disk/check` 和 `/disk/repair` 會對驅動器執行檔案系統檢查，相當於 `fsck`/`e2fsck`。它們適用於 ext4、Btrfs 和 XFS。仍在使用中的檔案系統無法檢查：

```ros
/disk/check nvme9-part1
Columns: OUTPUT
OUTPUT
could not unmount, stop using it first
```

當分割區上的交換檔案使其保持使用狀態時也會發生這種情況  -  請在檢查分割區前移除交換項。先解除安裝檔案系統：

```ros
/disk/set nvme9-part1 mount-filesystem=no
```

`check` 報告錯誤而不更改任何內容：

```ros
/disk/check nvme9-part1
Columns: OUTPUT
OUTPUT
e2fsck 1.46.5 (30-Dec-2021)
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
nvme9-part1-fs: 12/244320 files (0.0% non-contiguous), 166617/976562 blocks
```

`repair` 修復它發現的錯誤：

```ros
/disk/repair nvme9-part1
Columns: OUTPUT
OUTPUT
e2fsck 1.46.5 (30-Dec-2021)
nvme9-part1-fs: clean, 12/244320 files, 166617/976562 blocks
```

## 測試磁碟效能 {#test-disk-performance}

`/disk/test` 測量驅動器的持續吞吐量和 IOPS。測試在後臺執行，併為每個完成的塊列印一行，另有一個 `TOT` 行彙總結果。

```ros
/disk/test disk=nvme9-part2 direction=read pattern=sequential type=device block-size=4K duration=20
Columns: SEQ, RATE, IOPS, BYTES, DISK, THREAD, TYPE, PATTERN, DIR, BSIZE, STATE
  ...  11.7Gbps  359 651  1404.9MiB  nvme9-part2  0  device  sequential  read  4096
  ...  11.8Gbps  360 192  1407.0MiB  nvme9-part2  0  device  sequential  read  4096
R TOT  11.8Gbps  360 676  26.1GiB    nvme9-part2  0  device  sequential  read  4096
```

- `direction=read` 保持驅動器內容不變，並可在已掛載的檔案系統上執行。
- `direction=write` 會銷燬目標上的所有資料；僅對準備擦除的驅動器執行寫入測試。
- 為測試指定 `duration`，以便它自行停止；如果不指定，它會一直執行直到停止。
- 新測試會先準備一段時間  -  在開始產生數字之前，`state` 列會顯示 `clear caches`。

:::danger
磁碟效能測試可能會緩慢降低磁碟健康狀況。

寫入操作將銷燬執行該操作的驅動器上的所有資料。
:::

## 監控流量和計數器 {#monitor-traffic-and-counters}

`/disk/monitor-traffic` 顯示驅動器的即時活動：I/O 操作、傳輸位元組和速度，以總計和每秒的形式顯示：

```ros
/disk/monitor-traffic nvme9-part2 once
                  slot:    nvme9-part2
              read-ops:        113 229
   read-ops-per-second:              0
            read-bytes: 29 668 814 848
             read-rate:           0bps
           read-merges:              0
             read-time:       48s149ms
             write-ops:              0
```

`/disk/reset-counters` 會將這些計數器重設為零，包括錯誤計數器。

## 彈出和掃描 {#eject-and-scan}

在移除驅動器之前，請先將其彈出，以免資料丟失：

```ros
/disk/eject nvme9
```

已彈出的驅動器會被解除安裝，其插槽會顯示 `E - EMPTY` 標誌，直到驅動器被移除。`/disk/scan` 會重新檢測在未重啟的情況下插入或移除的驅動器，並在重新連線後恢復驅動器。

`/disk/trim` 會丟棄已掛載檔案系統的未使用塊（相當於 `fstrim`），以免 SSD 寫入效能下降。USB 驅動器不支援 trim，某些 NVMe 硬碟盒也不支援。

## S.M.A.R.T. 驅動器健康 {#smart-drive-health}

使用 S.M.A.R.T. 進行驅動器健康監控會讀取支援該功能的驅動器的診斷資訊，例如溫度、使用情況和錯誤計數器。請參見 [S.M.A.R.T. 資訊](./smart.md)。

## 相關內容 {#related}

- [儲存](../../storage/index.md)  -  RAID、網路儲存協定和高階檔案系統。
- [容器](../../containers/index.md)  -  使用磁碟空間儲存映象和交換空間。
- [S.M.A.R.T. 資訊](./smart.md)  -  驅動器健康監控。
- [Disks CLI 參考](../../cli-reference/disk/index.md)  -  `/disk` 的每個命令和引數。
