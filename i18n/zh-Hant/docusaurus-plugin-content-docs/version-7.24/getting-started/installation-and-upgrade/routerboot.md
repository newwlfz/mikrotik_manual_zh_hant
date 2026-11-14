---
sidebar_key: "getting-started/installation-and-upgrade/routerboot"
sidebar_position: 6
title: "RouterBOOT"
sidebar_label: "RouterBOOT"
description: "RouterBOOT 負責管理 MikroTik 硬體上的 RouterOS 啟動，具有主載入器和備用載入器，並提供 force-backup-booter 選項。復位按鈕具有多種功能，包括重設配置、啟用 CAPs 模式以及搜尋 Netinstall 伺服器。對於具有特定設定的 RouterBOARD 裝置，可使用序列埠控制檯訪問。"
tags:
  - 'routerboot'
  - 'configuration-management'
  - 'firmware-upgrade'
source: https://manual.mikrotik.com/docs/7.24/getting-started/installation-and-upgrade/routerboot
captured_at: '2026-11-04T11:28:49+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterBOOT 負責在 MikroTik 硬體裝置（例如接入點、路由器及其他型號）中啟動 RouterOS。由於 MikroTik 在此處及其他地方已經推出了許多新的硬體系列，因此當使用 RouterBOARD 這一術語時，它同樣適用於所有其他執行 RouterOS 的硬體系列。

### 主載入器和備份載入器 {#main-and-backup-loaders}

預設情況下，使用主（常規）載入器，但 RouterBOARD 裝置還有一個輔助（備份）引導載入器，可在主載入器無法工作時使用。可以透過 RouterOS 中的配置設定來呼叫備份載入器：

```ros
/system/routerboard/settings/set force-backup-booter=yes
```

也可以在按住 RESET 按鈕的同時開啟裝置來使用備份引導器。只能升級主 RouterBOOT，因此如果失敗，可以使用備份引導器啟動裝置並降級主載入器。有關升級說明，請遵循 [RouterBOARD#UpgradingRouterBOOT](../../hardware/routerboard.md) 中的單獨說明。

### RouterBOARD 復位按鈕 {#routerboard-reset-button}

RouterBOOT 復位按鈕有三個功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置（總計 5 秒）。
- 再按住 5 秒，直到 LED 變為常亮，然後鬆開以開啟 CAPs 模式（總計 10 秒）。
- 或者再按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器。

:::warning
如果在接通電源之前按住按鈕，除上述所有操作外，還將使用備份 RouterBOOT。要在不載入備份載入器的情況下執行上述操作，請在給裝置接通電源後立即按下按鈕。
:::

[重設密碼](https://help.mikrotik.com/docs/spaces/RKB/pages/328274/Reset+the+password)

[https://www.youtube.com/watch?v=6Unz92rABs8](https://www.youtube.com/watch?v=6Unz92rABs8)

### 用於 **Wireless Wire** 套件的配置重設 {#configuration-reset-for-wireless-wire-kits}

reset 按鈕的功能與其他裝置相同，詳細說明見 [/docs/Getting%20Started/routeros-configuration-reset](../configuration-management/routeros-configuration-reset.md)

啟動時按住按鈕 5 秒（USR LED 燈開始閃爍）——重設為受密碼保護的狀態。

啟動時按住按鈕 10 秒（USR LED 閃爍後變為常亮）——完全移除配置。

### 配置 {#configuration}

對於帶有序列控制檯聯結器的 RouterBOARD 裝置，可以訪問 RouterBOOT 載入器配置選單。所需線纜在 [序列控制檯](../../management-tools/serial-console.md) 手冊中有說明。RouterBOARD 序列埠配置為 **115200bit/s**、**8 個數據位**、**1 個停止位**和**無校驗**。我們建議停用硬體流控制。

此示例展示了 RouterBOOT 7.4beta4 中可用的選單：

```ros
RouterBOOT booter 7.4beta4

CRS328-24P-4S+

built by build at 2022-06-15 11:34:09 from revision 73B4521C

CPU frequency: 800 MHz
  Memory size: 512 MiB
 Storage size:  16 MiB

Press Ctrl+E to enter etherboot mode
Press any key within 2 seconds to enter setup

RouterBOOT-7.4beta4
What do you want to configure?
   d - boot delay
   k - boot key
   s - serial console
   n - silent boot
   o - boot device
   z - extra kernel parameters
   r - reset booter configuration
   e - format storage
   w - repartition nand
   g - upgrade firmware
   i - board info
   p - boot protocol
   b - booter options
   j - boot os
   t - hardware tests
   l - erase license
   x - exit setup
your choice: 
```

這些選項的含義不言自明。

| 字母 | 描述 | 說明 |
| :-- | :-- | :-- |
| d | 啟動延遲 | 延遲啟動 RouterOS，以便介面初始化 |
| k | 啟動按鍵 | 用於開啟配置選單的按鈕 |
| s | 序列控制檯 | 設定序列埠的波特率 |
| n | 靜默啟動 | 抑制序列埠上的所有輸出，以防某些裝置連線到該埠（例如 GPS 裝置或溫度監控器） |
| o | 啟動裝置 | 允許啟用 Netinstall 啟動 |
| z | 額外核心引數 |  |
| r | 重設引導器配置 | 重設此選單中的設定。**警告，沒有確認！** |
| e | 格式化儲存 | 銷燬 NAND 上的所有資料，包括 RouterOS 配置和許可證 |
| w | 重新分割區 NAND | 有關更多資訊，請參閱 [分割區](../../system-information-and-utilities/partitions.md) 文件 |
| y | 活動分割區 | 選擇要嘗試從中載入 RouterOS 的活動分割區 |
| g | 升級韌體 | 允許透過網路或 XModem 協定升級 RouterBOOT 版本 |
| i | 板卡資訊 |  |
| p | 啟動協定 |  |
| b | 引導器選項 | 選擇預設使用的引導載入器 |
| t | 執行記憶體測試 |  |
| j | 啟動作業系統 |  |
| l | 擦除許可證 |  |
| x | 退出設定 |  |

按下相應的鍵盤字母將顯示進一步選項的列表；如下所示：

```
# d - boot delay:

Select boot delay:
   1 - 1s
 * 2 - 2s
   3 - 3s
   4 - 4s
   5 - 5s
   6 - 6s
   7 - 7s
   8 - 8s
   9 - 9s

# k - boot key:

Select key which will enter setup on boot:
 * 1 - any key
   2 - <Delete> key only

# s - serial console:

Select baud rate for serial console:
 * 1 - 115200
   2 - 57600
   3 - 38400
   4 - 19200
   5 - 9600
   6 - 4800
   7 - 2400
   8 - 1200
   9 - off

# n - silent boot:

Silent boot:
   0 - off
 * 1 - on

# o - boot device:

Select boot device:
   e - boot over Ethernet
 * n - boot from NAND, if fail then Ethernet
   1 - boot Ethernet once, then NAND
   o - boot from NAND only
   b - boot chosen device
   f - boot Flash Configure Mode
   3 - boot Flash Configure Mode once, then NAND

# f - cpu frequency:

Select CPU frequency:
   a -  200MHz
   b -  400MHz
   c -  600MHz
   d -  800MHz
   e - 1000MHz
 * f - 1200MHz

# r - reset booter configuration:

# e - format nand:

Do you really want to format your storage device?
that would result in losing all your data
type "yes" to confirm: 

# w - repartition nand:

Select partition count:
   1 - partition
 * 2 - partitions
   3 - partitions
   4 - partitions

# y - active partition:

Select active partition:
 * 0 - partition
   1 - partition

# g - upgrade firmware:

Upgrade firmware options:
   e - upgrade firmware over ethernet
   s - upgrade firmware over serial port

# i - board info:

Board Info:

        Board type: CCR1009-8G-1S-1S+
     Serial number: 48FF01DDE6FD
  Firmware version: 3.19
     CPU frequency: 1200 MHz
       Memory size: 2048 MiB
         NAND size: 128 MiB
        Build time: 2014-09-23 15:02:34
  eth1 MAC address: 00:0C:42:00:BE:4A
  eth2 MAC address: 00:0C:42:00:BE:4B
  eth3 MAC address: 00:0C:42:00:BE:4C
  eth4 MAC address: 00:0C:42:00:BE:4D
  eth5 MAC address: 00:0C:42:00:BE:4E
  eth6 MAC address: 00:0C:42:00:BE:4F
  eth7 MAC address: 00:0C:42:00:BE:50
  eth8 MAC address: 00:0C:42:00:BE:51
  eth9 MAC address: 00:0C:42:00:BE:52
 eth10 MAC address: 00:0C:42:00:BE:53

# p - boot protocol:

Choose which boot protocol to use:
 * 1 - bootp protocol
   2 - dhcp protocol

# b - booter options:

Select which booter you want to load:
 * 1 - load regular booter
   2 - force backup-booter loading

#t - do memory testing:

launches built in memory test!

# x - exit setup:

Exit bios configuration menu and continues with system startup.

```

### 簡單升級 {#simple-upgrade}

可以透過以下方式從 RouterOS 升級 RouterBOOT：

- 執行命令 *`/system/routerboard/upgrade`*。
- 重啟路由器以應用升級（*`/system/reboot`*）。

```ros
[admin@admin] > /system/routerboard/upgrade 
Do you really want to upgrade firmware? [y/n] 

```

:::warning
每個 ROS 版本都包含新的 RouterBoot 版本。執行 ROS 升級後，我們始終建議也升級 RouterBoot。
:::

### 檢查 RouterBOOT 版本 {#checking-routerboot-version}

此命令顯示裝置的當前 RouterBOOT 版本，以及 *routeros-x.yy.npk* 包中包含的可用升級，或者如果你上傳了與裝置型號對應的 *\*.FWF* 檔案：

```ros
[admin@admin] >  /system/routerboard/print 
                ;;; Firmware upgraded successfully, please reboot for changes 
                    to take effect!
       routerboard: yes
        board-name: hAP ac
             model: RouterBOARD 962UiGS-5HacT2HnT
     serial-number: 6737057562DD
     firmware-type: qca9550L
  factory-firmware: 3.29
  current-firmware: 6.49.5
  upgrade-firmware: 7.4beta5 

```

在這種情況下，你會發現當前 RouterOS 版本中已經包含**更新版本**的引導載入器韌體，並且它已更新並需要重啟。

:::warning
也可以透過上傳舊版本的 \*.FWF 檔案進行降級，在聯絡 MikroTik 支援進行故障排除時可能需要這樣做。
:::
