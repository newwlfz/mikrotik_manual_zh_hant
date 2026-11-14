---
sidebar_key: "storage/rsync"
sidebar_position: 9
title: "Rsync"
sidebar_label: "Rsync"
description: "RouterOS 中的 Rsync 允許使用 ipsec 加密在系統之間進行高效的檔案同步，並支援可配置的本地/遠端路徑以及上傳/下載模式。設定密碼時會建立動態 IPsec 條目，確保透過 TCP/8291 和 UDP/500 進行安全傳輸。"
tags:
  - 'rsync'
  - 'ipsec'
  - 'file-sync'
source: https://manual.mikrotik.com/docs/7.24/storage/rsync
captured_at: '2026-11-04T11:33:15+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

`rsync`（Remote Sync）是 Unix 系統中使用的強大檔案同步和檔案傳輸程式。它可以在不同系統之間或同一系統內高效地傳輸和同步檔案及目錄。

如果修改了檔案，則只傳輸檔案中的更改，從而減少資料傳輸量。RouterOS 的 RSYNC 實現使用 ipsec 進行資料傳輸（如果設定了密碼）。配置完成後，你將看到動態 ipsec 條目。

Rsync 設定可在 `file/sync` 選單中找到。

:::warning

TCP/873 埠用於 rsync 控制連線（如果狀態中未開啟（*file sync print*），你將卡在 making control connection to *192.168.88.2*）

UDP/500 埠和協定 50（ipsec-esp）用於建立安全連線並開始傳輸（如果狀態中未開啟（*file sync print*），你將卡在 initializing transfer）

:::

## 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **local-path** | 檔案/資料夾路徑。用於 *Upload* 模式，設定要上傳到裝置的檔案/資料夾路徑 |
| **mode** | 設定是要下載/上傳檔案（同步方向） |
| **password** | 目標裝置密碼 |
| **remote-address** | 目標裝置 IP |
| **remote-path** | 檔案/資料夾路徑。與 *download* 模式一起使用，設定目標裝置上要下載的路徑 |
| **user** | 目標裝置使用者名稱 |

## 配置示例 {#configuration-example}

基本配置非常簡單。在主機裝置上，你需要新增要同步到另一臺裝置的檔案、IP、使用者名稱/密碼以及模式。

```ros
/file/sync
add local-path=/ipv6route.txt.rsc mode=upload remote-address=192.168.88.2 remote-path=RAID/

```

如果配置正確，你將在主機裝置上看到：

```ros
0 192.168.88.2  upload  /ipv6route.txt.rsc  RAID/        in sync
```

在用戶端裝置上：

```ros
#   REMOTE-ADDRESS   MODE      LOCAL-PATH  REMOTE-PATH         STATUS 
0 D 192.168.88.1 download  RAID/       /ipv6route.txt.rsc  in sync
```

### IPSec 動態條目 {#ipsec-dynamic-entries}

當 rsync 配置了密碼時，它會為安全傳輸建立動態 IPSec 條目：

```ros
#     PEER                     TUNNEL  SRC-ADDRESS       DST-ADDRESS       PROTOCOL  ACTION   LEVEL    PH2-COUNT
;;; file-sync-10.155.145.11
1  D  file-sync-10.155.145.11  no      10.155.145.17/32  10.155.145.11/32  tcp       encrypt  require          1

/ip/ipsec/peer> print
 0  D  name="file-sync-10.155.145.11" address=10.155.145.11/32 local-address=10.155.145.17 profile=default exchange-mode=main send-initial-contact=yes
/ip/ipsec/identity> print
 0 D  ;;; file-sync-10.155.145.11
      peer=file-sync-10.155.145.11 auth-method=pre-shared-key secret="secret" generate-policy=no
```
