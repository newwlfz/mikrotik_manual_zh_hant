---
sidebar_key: "storage/tmpfs"
sidebar_position: 13
title: "臨時檔案系統（Tmpfs）"
sidebar_label: "臨時檔案系統"
description: "tmpfs 是 RAM 中用於存放臨時檔案（例如封包捕獲檔案和下載檔案）的資料夾。其大小有上限，且其內容在重啟後會丟失。"
tags:
  - 'storage'
  - 'tmpfs'
source: https://manual.mikrotik.com/docs/7.25/storage/tmpfs
captured_at: '2026-11-04T11:21:48+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

tmpfs 是 RAM 中的一個資料夾。RouterOS 將其顯示為一塊磁碟，例如 `tmp1`，檔案可以像放入其他任何磁碟一樣放入其中。請將其用於只需要保留一段時間、不應磨損或佔滿快閃記憶體的檔案：封包捕獲檔案、指令碼下載並匯入的檔案，以及其他臨時檔案。Tmpfs 是基礎 RouterOS 軟體包的一部分，可在所有具有 `/disk` 選單的裝置上使用，而 SMIPS 裝置沒有該選單。

:::warning
路由器重啟或斷電時，tmpfs 的內容會丟失。請將要保留的檔案複製到快閃記憶體、USB 磁碟或計算機上。
:::

## 建立 RAM 資料夾 {#create-a-ram-folder}

新增一個最多可容納 100 MB 的資料夾：

```ros
/disk/add type=tmpfs tmpfs-max-size=100M
```

```ros
[admin@MikroTik] > /disk/print
Flags: M - MOUNTED
Columns: SLOT, MOUNT-POINT, MODEL, INTERFACE, SIZE, FREE, USE, FS
#   SLOT  MOUNT-POINT  MODEL  INTERFACE         SIZE         FREE  USE  FS
0 M tmp1  tmp1         tmpfs  ram        100 003 840  100 003 840  0%   tmpfs
```

第一個資料夾獲得的槽位名稱為 `tmp1`，下一個為 `tmp2`。槽位名稱是檔案路徑的開頭，例如 `tmp1/capture.pcap`，其他命令透過它來引用該資料夾。

大小使用十進位制單位：`100M` 即 100 000 000 位元組。`/disk/print` 中的大小會向上取整為完整的 4 KiB 記憶體頁，因此該資料夾顯示為 100 003 840。`tmpfs-max-size` 是該資料夾可以增長到的最大值；RAM 僅由儲存在其中的檔案使用。

## 檢查該資料夾共享了什麼 {#check-what-the-folder-shares}

在預設配置啟用了自動磁碟共享的路由器上，新的 tmpfs 一經建立就會被共享。請先檢查路由器的設定：

```ros
/disk/settings/print
```

例如，hAP ax² 的預設配置設定了 `auto-smb-sharing=yes`、`auto-media-sharing=yes` 和 `auto-media-interface=bridge`。隨後該資料夾會獲得一個供只讀 `guest` 使用者使用的 SMB 共享（該使用者無需密碼），並在 `bridge` 上獲得一個 DLNA 媒體伺服器。當 `/ip/smb` 設定為 `enabled=auto` 時，該共享還會啟動 SMB 伺服器。SMB 伺服器監聽所有介面（`interfaces=all`），只有防火牆限制誰能訪問它；預設防火牆允許 LAN 訪問。除非在 `/ip/smb/users` 中停用了 `guest` 使用者，否則任何能訪問 SMB 伺服器的人都可以以 `guest` 身份讀取該資料夾中的檔案，包括封包捕獲檔案。

當自動共享開啟時，請在關閉共享的情況下建立資料夾。該設定在重啟後仍會保留：

```ros
/disk/add type=tmpfs tmpfs-max-size=100M smb-sharing=no media-sharing=no
```

`/disk/print` 中的標誌 `s`（SMB 共享）和 `m`（媒體共享）顯示哪些資料夾被共享。此處 `tmp1` 是在自動共享開啟時建立的，而 `tmp2` 是用上一條命令建立的：

```ros
[admin@MikroTik] > /disk/print
Flags: M - MOUNTED; s - SMB-SHARING; m - MEDIA-SHARING
Columns: SLOT, MOUNT-POINT, MODEL, INTERFACE, SIZE, FREE, USE, FS
#     SLOT  MOUNT-POINT  MODEL  INTERFACE         SIZE         FREE  USE  FS
0 Msm tmp1  tmp1         tmpfs  ram        100 003 840  100 003 840  0%   tmpfs
1 M   tmp2  tmp2         tmpfs  ram        100 003 840  100 003 840  0%   tmpfs
```

資料夾的 SMB 共享是 `/ip/smb/shares` 中的一個動態條目：

```ros
[admin@MikroTik] > /ip/smb/shares/print
Flags: D - DYNAMIC; X - DISABLED; * - DEFAULT
Columns: NAME, DIRECTORY, REQUIRE-ENCRYPTION, VALID-USERS
#     NAME  DIRECTORY  REQUIRE-ENCRYPTION  VALID-USERS
0  X* pub   /pub       no
1 D   tmp1  /tmp1      no                  guest
```

停止共享一個已經共享的資料夾：

```ros
/disk/set tmp1 smb-sharing=no media-sharing=no
```

停止自動共享新的磁碟和資料夾：

```ros
/disk/settings/set auto-smb-sharing=no auto-media-sharing=no
```

要有意地使用你自己的使用者共享檔案，請參閱 [SMB](./smb.md) 和 [DLNA 媒體伺服器](./dlna.md)。

## 將封包捕獲檔案儲存在 RAM 中 {#keep-packet-captures-in-ram}

封包捕獲檔案可能增長得很快。請將其寫入 tmpfs 而不是快閃記憶體，並將 `file-limit`（單位為 KiB）保持在資料夾大小以下：`50000KiB` 約為 51 MB，可以放入 100 MB 的資料夾中。

```ros
/tool/sniffer/set file-name=tmp1/capture.pcap file-limit=50000KiB \
    filter-interface=ether1
/tool/sniffer/start
```

當捕獲到所需的封包後，停止捕獲：

```ros
/tool/sniffer/stop
```

在路由器重啟之前，使用 WinBox 或 WebFig 中的 Files 選單（參見 [在 WinBox 中管理檔案](../system-information-and-utilities/files.md#manage-files-in-winbox)）或從你的計算機使用 `scp` 下載 `tmp1/capture.pcap`：

```bash
scp admin@192.168.88.1:tmp1/capture.pcap .
```

有關過濾器和即時流式傳輸，請參閱 [封包嗅探器](../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)。

## 檢查資料夾的已用空間 {#check-how-full-the-folder-is}

`/disk/print` 的 `FREE` 和 `USE` 列顯示該資料夾已使用了多少空間。它們會在寫入後幾秒鐘更新。列出該資料夾中的檔案：

```ros
[admin@MikroTik] > /file/print where name~"^tmp1"
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME               TYPE        SIZE     LAST-MODIFIED
0 tmp1               disk                 2026-10-01 08:35:03
1 tmp1/capture.pcap  .pcap file  19.8KiB  2026-10-01 08:35:08
```

當資料夾已滿時，對其的寫入會失敗。例如，`/tool/fetch` 會以 `failure: cannot download: file too large, no space left on disk` 停止，並且不會保留部分檔案。

## 更改大小或刪除資料夾 {#change-the-size-or-delete-the-folder}

新的大小會立即生效，對已掛載的資料夾也是如此：

```ros
/disk/set tmp1 tmpfs-max-size=200M
```

刪除該資料夾及其中的所有檔案。RouterOS 不會要求確認：

```ros
/disk/remove tmp1
```

## 技術細節 {#technical-details}

### 大小限制 {#size-limit}

如果沒有 `tmpfs-max-size`（其讀取值為 `0`），該資料夾可以增長到路由器 RAM 的大約一半，例如在具有 1 GB RAM 的路由器上為 464 MB。RouterOS 會將所有 tmpfs 資料夾的最大大小相加，沒有 `tmpfs-max-size` 的資料夾按 RAM 的一半計算，當總量超過路由器所能提供的值時，會拒絕新的大小：

```text
failure: too much memory requested for tmpfs/ramdisk
```

### 記憶體使用 {#memory-use}

空的 tmpfs 不保留任何 RAM。其中的檔案會使用 RAM，並降低 `/system/resource` 中的 `free-memory`。填滿 RAM 的檔案可能導致路由器記憶體耗盡，因此請將 `tmpfs-max-size` 保持在遠低於可用記憶體的水平。

### 重啟之後 {#after-a-reboot}

`/disk` 條目及其設定會保留在配置中。重啟後，RouterOS 會在相同的槽位名稱下重新掛載該資料夾，且內容為空。該資料夾的自動 SMB 和 DLNA 共享會隨之恢復，而設定為 `smb-sharing=no` 和 `media-sharing=no` 的資料夾則保持不共享。

### 不是塊裝置 {#not-a-block-device}

tmpfs 是檔案系統，不是塊裝置，因此無法格式化：

```text
failure: cannot format nfs/smb/tmpfs/sshfs file systems
```

如需用作塊裝置的 RAM，例如作為 RAID 成員，請使用 [記憶體盤](./ramdisk.md)。

有關引數，請參閱 [`/disk` CLI 參考](../cli-reference/disk/index.md)。
