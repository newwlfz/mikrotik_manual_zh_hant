---
sidebar_key: "network-management/cloud/communication-mikrotik-cloud-servers"
sidebar_position: 3
title: "與 MikroTik 雲服務通訊"
sidebar_label: "與 MikroTik 雲服務通訊"
description: "RouterOS 與 MikroTik 伺服器建立的每個連線：啟動它的選單、伺服器、是否預設執行，以及如何將其關閉。"
tags:
  - 'cloud'
  - 'backup'
source: https://manual.mikrotik.com/docs/7.25/network-management/cloud/communication-mikrotik-cloud-servers
captured_at: '2026-11-04T11:20:44+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 僅會為下表中列出的服務連線到 MikroTik 伺服器。預設情況下，路由器在啟動時會向雲伺服器請求時間和時區，而 Cloud Hosted Router (CHR) 會檢查其許可證。其他所有服務只有在您啟用它或執行相應命令後才會執行。

| 選單 | 伺服器 | 預設開啟 | 如何關閉 |
| :-- | :-- | :-- | :-- |
| `/system/clock` `time-zone-autodetect` | `cloud2.mikrotik.com` | yes | `/system/clock/set time-zone-autodetect=no`（參見[時鐘](../../system-information-and-utilities/clock.md)） |
| `/ip/cloud` `update-time` | `cloud2.mikrotik.com` | yes | `/ip/cloud/set update-time=no`（參見[時間更新](./index.md#time-update)） |
| `/ip/cloud` `ddns-enabled` | `cloud2.mikrotik.com` | no | `/ip/cloud/set ddns-enabled=auto`，並關閉 Back To Home（遠端回家）（參見 [DDNS](./index.md#ddns)） |
| `/ip/cloud` `back-to-home-vpn` | `cloud2.mikrotik.com` 和中繼伺服器 | no | `/ip/cloud/set back-to-home-vpn=revoked-and-disabled`（參見 [Back To Home](./back-to-home.md)） |
| `/ip/cloud/back-to-home-file` | `cloud2.mikrotik.com` 和中繼伺服器 | no | 移除所有檔案共享（參見[檔案共享](./file-share.md)） |
| `/system/backup/cloud` | `cloud2.mikrotik.com` | no | 僅針對 `print`、`upload-file`、`download-file` 和 `remove-file` 命令執行（參見[雲備份](./cloud-backup.md)） |
| `/system/license` | `licence.mikrotik.com` | 僅在 CHR 上 | 在 CHR 上無法關閉（參見 [CHR 許可](../../getting-started/routeros-licensing/chr/chr-licensing.md)） |
| `/interface/lte` `firmware-upgrade` | `upgrade.mikrotik.com` | no | 僅針對 `firmware-upgrade` 命令執行（參見 [LTE 韌體升級](../../mobile-networking/lte-5g.md#modem-firmware-upgrade-command)） |
| `/interface/detect-internet` | `cloud.mikrotik.com` | no | `/interface/detect-internet/set detect-interface-list=none`（參見[檢測 Internet](../../diagnostics-monitoring-and-troubleshooting/detect-internet.md)） |
| `/system/package/update` | `upgrade.mikrotik.com` | no | 僅針對 `check-for-updates` 命令和軟體包下載執行（參見[軟體包](../../getting-started/installation-and-upgrade/packages.md)） |
| `/system/swos` `upgrade` | `upgrade.mikrotik.com` | no | 僅針對 `upgrade` 命令執行（參見 [SwOS 升級](../../bridging-and-switching/marvell-prestera-switch-chip-features.md#configuring-swos-using-routeros)） |

## 技術細節 {#technical-details}

路由器會使用以下埠：

- `cloud2.mikrotik.com`：DDNS 使用 UDP 埠 15252，雲備份使用 TCP 埠 15252。該名稱會解析為多個地址，當某臺伺服器不響應時，路由器會嘗試另一個地址。
- `cloud.mikrotik.com`：檢測 Internet 使用 UDP 埠 30000。
