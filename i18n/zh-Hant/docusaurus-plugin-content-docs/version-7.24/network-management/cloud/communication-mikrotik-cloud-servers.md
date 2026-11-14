---
sidebar_key: "network-management/cloud/communication-mikrotik-cloud-servers"
sidebar_position: 2
title: "與 MikroTik 雲服務通訊"
sidebar_label: "與 MikroTik 雲服務通訊"
description: "本頁詳細說明 MikroTik RouterOS 與雲伺服器及 Mikrotik 服務的連線，列出每種連線型別的子選單、域名、預設狀態以及停用通訊的方法。"
tags:
  - 'cloud'
  - 'backup'
source: https://manual.mikrotik.com/docs/7.24/network-management/cloud/communication-mikrotik-cloud-servers
captured_at: '2026-11-04T11:32:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本表列出了 RouterOS 可能向 MikroTik 伺服器發起的所有連線資訊，以及如何停用此類連線的說明。

| 子選單 | 域名 | 預設啟用/活動 | 確保通訊被停用/非活動 |
| :-- | :-- | :-- | :-- |
| **system clock time-zone-autodetect** | cloud2.mikrotik.com | yes | `/system/clock/set` time-zone-autodetect=no（[參見時鐘文件](../../system-information-and-utilities/clock.md)） |
| **system backup cloud** | cloud2.mikrotik.com | no | 通訊僅由 upload-file、download-file、remove-file 命令觸發。（[參見備份](./index.md#cloud-backup)） |
| **ip cloud update-time** | cloud2.mikrotik.com | yes | `/ip/cloud/set` update-time=no（[參見更新時間](./index.md#update-time)） |
| **ip cloud ddns-enabled** | cloud2.mikrotik.com | no | `/ip/cloud/set` ddns-enabled=auto（[參見 DDNS](./index.md#ddns)） |
| **ip cloud back-to-home-vpn** | cloud2.mikrotik.com | no | `/ip/cloud/set` back-to-home-vpn=revoked-and-disabled（[參見 BTH VPN](./back-to-home.md#ip-cloud)） |
| **ip cloud back-to-home-file** | cloud2.mikrotik.com | no | 通訊僅由在 "ip cloud back-to-home-file" 中啟用或停用檔案共享觸發。（[參見檔案共享](./file-share.md)） |
| **system license** | licence.mikrotik.com | 是（僅對 [CHRs](../../getting-started/routeros-licensing/chr/index.md) 相關） | 對於 CHRs 而言，無法使用 RouterOS 中的特定命令或設定來停用與許可證伺服器的通訊。（[參見 CHR 許可證](../../getting-started/routeros-licensing/chr/chr-licensing.md)） |
| **interface lte firmware-upgrade** | upgrade.mikrotik.com | no | 通訊僅由 firmware-upgrade 命令觸發。（[參見 LTE 韌體升級](../../mobile-networking/lte-5g.md#modem-firmware-upgrade-command)） |
| **interface detect-internet** | cloud.mikrotik.com | no | `/interface/detect-internet/set` detect-interface-list=none（[參見檢測 Internet](../../diagnostics-monitoring-and-troubleshooting/detect-internet.md)） |
| **system package update** | upgrade.mikrotik.com | no | 通訊僅由 check-for-updates 命令以及從升級伺服器下載軟體包來發起。（[參見軟體包更新](../../getting-started/installation-and-upgrade/packages.md)） |
| **system swos upgrade** | upgrade.mikrotik.com | no | 通訊僅由 upgrade 命令觸發。（[參見 SWOS 升級](../../bridging-and-switching/marvell-prestera-switch-chip-features.md#configuring-swos-using-routeros)） |
