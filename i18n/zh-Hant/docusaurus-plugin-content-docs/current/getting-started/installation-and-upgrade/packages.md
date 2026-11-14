---
sidebar_key: "getting-started/installation-and-upgrade/packages"
sidebar_position: 4
title: "軟體包"
sidebar_label: "軟體包"
description: "RouterOS 將功能組織為以 .npk 為副檔名的軟體包，其中包括核心的 routeros 套件以及 Containers 或 The Dude 等可選附加包。無線裝置需要根據硬體安裝特定的軟體包，安裝方式包括手動下載和直接從路由器更新。"
tags:
  - 'packages'
  - 'system-packages'
source: https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/packages
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

RouterOS 的功能以軟體包的形式組織，軟體包是副檔名為 `.npk` 的檔案。大多數功能捆綁在 ***routeros*** 軟體包中，而某些功能則以單獨的軟體包提供。安裝額外的 `.npk` 軟體包可啟用特定功能，例如 Containers 或 The Dude。軟體包檔案僅由 MikroTik 提供，第三方無法建立。你可以從我們的下載頁面下載額外軟體包，或直接從路由器中新增它們。

## 最低要求 {#minimum-requirements}

RouterOS 在最低限度下只需系統軟體包即可執行，但對於大多數裝置而言，安裝 "routeros" 捆綁包後才能獲得標準執行和功能。

對於無線裝置，根據你所使用的硬體，有多個無線軟體包可用：

- 從 RouterOS 7.13 開始，簡單家用路由器的基本執行需要 ***routeros***（系統）軟體包以及以下無線軟體包之一：
  1. 802.11ax WiFi AP 需要無線驅動，由 ***wifi-qcom*** 軟體包提供（對於 7.13 之前的 RouterOS 版本，它被稱為 *wifiwave2* 軟體包）。
  2. 上一代 WiFi AP 需要 ***wireless*** 軟體包。

有關使用哪個無線軟體包的更多資訊，請參見[無線手冊](../../wireless/index.md)。

其他軟體包是可選的，家用路由器並不需要。只有在確定其用途時才安裝它們。

## 安裝軟體包 {#installing-packages}

### 手動下載 {#manual-download}

要手動下載並安裝額外軟體包，請從 [MikroTik 下載](https://mikrotik.com/download) 頁面下載所需的軟體包，並根據在 System/Resources 選單中找到的裝置架構選擇 RouterOS 部分。解壓壓縮包，並使用任意便捷方法將所需軟體包上傳到路由器，然後重啟路由器。

### 直接從路由器下載 {#download-directly-from-the-router}

你可以使用 *System Packages* 部分直接從路由器下載並安裝額外軟體包。

1. 執行 ***Check For Updates*** 命令後，可用的軟體包將列在 *Packages* 列表中，但它們會顯示為已停用。可用軟體包列表來自 MikroTik 下載伺服器。這些軟體包可用，但尚未位於你的路由器上（由標誌 X（Disabled）和 A（Available）指示）。
2. 要下載額外軟體包，首先選擇該軟體包並選擇 ***Enable***。
3. 要讓路由器下載該軟體包，請選擇 ***Apply Changes***，裝置將要求重啟。

| 軟體包列表 | 使用 "Check for updates" 載入列表後 | 啟用軟體包 | 選擇 "Apply Changes" |
| :--- | :--- | :--- | :--- |
| [![](/img/56103c4552609cc3.png)](/img/56103c4552609cc3.png) | [![](/img/3b65fadd6caf7a14.png)](/img/3b65fadd6caf7a14.png) | [![](/img/b3db506cdc92e62e.png)](/img/b3db506cdc92e62e.png) | [![](/img/99456de9dc22c996.png)](/img/99456de9dc22c996.png) |

### 驗證安裝 {#verification-of-install}

為確保軟體包安裝成功，請在裝置重啟後檢查 "Log" 部分。如果軟體包安裝成功，你會看到一條相關訊息。如果存在衝突或某項要求未滿足，將會進行說明，以便你可以採取進一步措施加以糾正。

![](/img/bad3f8fc7b0b7e41.webp)日誌條目中的成功資訊![](/img/233ed154de2c0342.webp)日誌條目中的失敗資訊

### 系統軟體包 {#system-packages}

| **軟體包** | 描述 |
| :--- | :--- |
| **routeros-arm** (*arm*) | 用於 arm 裝置的系統軟體包。 |
| **routeros-arm64** (*arm64*) | 用於 arm64 裝置的系統軟體包。 |
| **routeros-mipsbe** (*mipsbe*) | 用於 mipsbe 裝置的系統軟體包。 |
| **routeros-mmips** (*mmips*) | 用於 mmips 裝置的系統軟體包。 |
| **routeros-smips** (*smips*) | 用於 smips 裝置的系統軟體包。 |
| **routeros-tile** (*tile*) | 用於 tile 裝置的系統軟體包。 |
| **routeros-ppc** (*ppc*) | 用於 ppc 裝置的系統軟體包。 |
| **routeros** (*x86, CHR*) | 用於 x86 安裝和 CHR 環境的系統軟體包。 |

### 額外軟體包 {#extra-packages}

| 軟體包（支援的架構） | 描述 |
| :--- | :--- |
| **calea** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | 由於美國“通訊協助執法法案”而用於特定用途的資料收集工具。 |
| **cmr** (*arm, arm64, x86*) | [CMR](../../management-tools/cmr.md) 是用於 RouterOS 裝置群的集中監控平臺。 |
| **container** (*arm, arm64, x86, CHR*) | Linux 容器的 [容器](../../containers/index.md) 實現，允許使用者在 RouterOS 中執行容器化環境。 |
| **dude** (*arm, arm64, mmips, tile, x86, CHR*) | 用於監控網路環境的 [Dude](../../management-tools/dude.md) 工具。 |
| **extra-nic** (*arm64*) | ARM64 CPU 架構網路介面卡（NIC）支援，建議用於非 MikroTik 板卡上的 UEFI 安裝。 |
| **gps** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | [全球定位系統](../../mobile-networking/gps/index.md)裝置支援。 |
| **iot** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | 啟用： <br/><ul><li>[MQTT](../../internet-of-things/mqtt/index.md)</li><li>[LoRa](../../internet-of-things/lora/general-properties.md)（適用於配備 LR8/9/2 miniPCIe 卡的裝置）</li><li>[藍牙](../../internet-of-things/bluetooth/index.md)（適用於配備 Bluetooth 晶片的裝置）</li><li>[GPIO](../../internet-of-things/gpio/index.md)（適用於配備 GPIO 引腳的裝置）</li><li><a href="https://help.mikrotik.com/docs/pages/viewpage.action?pageId=61046813" rel="nofollow">Modbus</a>（適用於配備 RS485 埠的裝置）</li></ul> |
| **iot-bt-extra** (*arm, arm64*) | 適用於 ARM 和 ARM64 裝置的軟體包，可啟用 USB Bluetooth 介面卡（必須支援 LE 4.0+）。 <br/> *<strong>注意：</strong>並非所有介面卡都經過測試。我們無法事先保證特定介面卡可以工作。 |
| **lora** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | 用於支援 [LoRa](../../internet-of-things/lora/general-properties.md) 的佔位軟體包。LoRa 軟體包不再是必需的，僅出於相容性原因保留。LoRa 功能已移至 iot 軟體包。 |
| **lte** (*mipsbe*) | 僅 SXT LTE（RBSXTLTE3-7）所需的軟體包，其中包含內建 LTE 介面的驅動程式。 |
| **rose-storage** (*arm, arm64, tile, x86, CHR*) | RouterOS 中額外的[企業資料中心功能](../../storage/index.md)，支援磁碟監控、改進的格式化、RAIDs、rsync、iSCSI、NVMe over TCP、NFS 和改進的 SMB。 |
| **switch-marvell** (*arm64*) | CRS8xx 系列交換器所需的驅動程式軟體包。 |
| **tr069-client** (*arm, arm64, mipsbe, mmips, smips, tile, ppc, x86, CHR*) | [TR069 用戶端](../../management-tools/tr-069.md)軟體包。 |
| **ups** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | [APC UPS 管理](../../system-information-and-utilities/ups.md)介面。 |
| **user-manager** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | [使用者管理器](../../authentication-authorization-accounting/user-manager.md) 伺服器，用於控制 Hotspot 和其他服務使用者。 |
| **wifi-mediatek** (*arm*) | 受支援的 MediaTek 無線硬體所需的 MediaTek WiFi 驅動程式。 |
| **wifi-qcom** (*arm, arm64*) | 802.11ax 介面所需的驅動程式軟體包。於 7.13 中引入。[WiFi CAPsMAN](../../wireless/wifi/index.md#wifi-capsman) 支援隨系統軟體包提供。 |
| **wifi-qcom-ac** (*arm*) | 適用於相容 802.11ac 介面的可選 [WiFi](../../wireless/wifi/index.md) 驅動程式軟體包。於 7.13 中引入。 |
| **wifi-qcom-be** (*arm64*) | WiFi-7 802.11be 硬體所需的驅動程式軟體包。 |
| **wireless** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | 用於管理 WiFi（最高 802.11ac）和 60GHz 無線介面的實用程式和驅動程式。此軟體包在 7.12 及之前的版本中捆綁在 RouterOS 內。從 7.13 開始，它是一個單獨的軟體包。 <br/> <strong>wireless</strong> 軟體包與 <strong>wifi-qcom</strong> 和 <strong>wifi-qcom-ac</strong> 軟體包衝突——它們不能同時處於活動狀態。 |
| **zerotier** (*arm, arm64*) | 啟用 [ZeroTier](../../virtual-private-networks/zerotier.md) 功能。 |

## 自動安裝 {#auto-install}

你還可以在使用 FTP 或 SFTP 將軟體包上傳到路由器後自動安裝它們。軟體包檔案的副檔名必須命名為 `*.auto.npk`。檔案上傳後，路由器將自動重啟以安裝該軟體包。這對於指令碼編寫和自動化非常有用。

檔名中的 `.auto.npk` 副檔名是軟體包自動安裝的必需條件。

## 使用軟體包 {#working-with-packages}

___

### 列出軟體包 {#list-packages}

*zerotier* 軟體包已停用，但已安裝；*iot* 軟體包在伺服器上可用，但尚未下載到路由器並啟用；*dude* 軟體包已安排解除安裝。

```ros
/system/package/print 
Flags: X - DISABLED; A - AVAILABLE
Columns: NAME, VERSION, SCHEDULED, BUILD-TIME, SIZE
#    NAME            VERSION     SCHEDULED                      BUILD-TIME           SIZE  
0    wireless        7.24beta1                                  2026-05-26 10:47:52  1388.1KiB
1 X  container       7.24beta1                                  2026-05-26 10:47:52  1156.1KiB
2    routeros        7.24beta1                                  2026-05-26 10:47:52  11.0MiB  
3    zerotier        7.24beta1                                  2026-05-26 10:47:52  372.1KiB 
4 XA calea                                                                           20.1KiB  
5 XA gps                                                                             24.1KiB  
6 XA iot                                                                             788.1KiB 
7 XA openflow                                                                        76.1KiB  
8 XA tr069-client                                                                    120.1KiB 
9 XA ups                                                                             44.1KiB  
```

### 安裝軟體包 {#install-package}

```ros
/system/package/enable gps,zerotier,container
/system/package/apply-changes
Apply scheduled changes and reboot device? [y/N]: 

```

### 解除安裝軟體包 {#uninstall-package}

```ros
/system/package/uninstall gps,container;
/system/package/apply-changes
Apply scheduled changes and reboot device? [y/N]: 
```

### 停用軟體包 {#disable-package}

```ros
/system/package/disable container; 
/system/package/apply-changes
Apply scheduled changes and reboot device? [y/N]:
```

### 取消解除安裝或停用操作 {#cancel-the-uninstall-or-disable-action}

```ros
/system/package/unschedule container;
```

### 降級 {#downgrade}

```ros
/system/package/downgrade; /system/reboot;
Router will be rebooted. Continue? [y/N]: 
```
