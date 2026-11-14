---
sidebar_key: "storage/rsync"
sidebar_position: 9
title: "Rsync"
sidebar_label: "Rsync"
description: "RouterOS 中的 Rsync 允許系統之間進行高效的檔案同步，可配置本地/遠端路徑以及上傳/下載模式。設定密碼後會建立動態 IPsec 條目，確保透過 TCP/873 和 UDP/500 進行安全傳輸。"
tags:
  - 'rsync'
  - 'ipsec'
  - 'file-sync'
source: https://manual.mikrotik.com/docs/7.25/storage/rsync
captured_at: '2026-11-04T11:21:40+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info
此功能需要 [儲存](./index.md) 軟體包。
:::

`rsync`（Remote Sync）是一個功能強大的檔案同步和檔案傳輸程式。它可以在不同系統之間或同一系統內高效地傳輸和同步檔案與目錄。

如果修改了檔案，只會傳輸更改的部分，從而減少資料傳輸量。RouterOS 的 rsync 實現在設定了密碼時使用 IPsec 進行資料傳輸。配置完成後，你會看到動態 IPsec 條目（見下文）。

Rsync 同步條目可以在 `/file/sync` 選單中找到，接收端路由器必須執行 rsync 守護程式，並在 `/file/rsync-daemon` 下啟用。

:::warning

TCP/873 埠用於 rsync 控制連線（如果未開放，`/file/sync/print` 會卡在 `making control connection to <ip>`）。

UDP/500 埠和協定 50（ipsec-esp）用於建立安全連線並開始傳輸（如果未開放，`/file/sync/print` 會卡在 `initializing transfer`）。
:::

## 配置示例 {#configuration-example}

基本配置很簡單：在主機裝置上新增要同步到另一臺裝置的檔案，指定遠端裝置的 IP 以及同步模式。遠端裝置必須啟用 rsync 守護程式：

```ros
# 远程设备（接收传输）：
/file/rsync-daemon/set enabled=yes
```

```ros
# 主机设备（发起同步）：
/file/sync/add local-path=/ipv6route.txt.rsc mode=upload remote-address=192.168.88.2 remote-path=RAID/
```

如果配置正確，主機裝置上的條目會顯示 `in sync`：

```ros
0 192.168.88.2  upload  /ipv6route.txt.rsc  RAID/        in sync
```

在遠端裝置上：

```ros
#   REMOTE-ADDRESS   MODE      LOCAL-PATH  REMOTE-PATH         STATUS 
0 D 192.168.88.1 download  RAID/       /ipv6route.txt.rsc  in sync
```

### IPsec 動態條目 {#ipsec-dynamic-entries}

當 rsync 配置了密碼時，它會建立動態 IPsec 條目以進行安全傳輸：

```ros
#     PEER                     TUNNEL  SRC-ADDRESS       DST-ADDRESS       PROTOCOL  ACTION   LEVEL    PH2-COUNT
;;; file-sync-10.155.145.11
1  D  file-sync-10.155.145.11  no      10.155.145.17/32  10.155.145.11/32  tcp       encrypt  require          1

/ip/ipsec/peer print
 0  D  name="file-sync-10.155.145.11" address=10.155.145.11/32 local-address=10.155.145.17 profile=default exchange-mode=main send-initial-contact=yes
/ip/ipsec/identity print
 0 D  ;;; file-sync-10.155.145.11
      peer=file-sync-10.155.145.11 auth-method=pre-shared-key secret="secret" generate-policy=no
```
