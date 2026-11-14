---
sidebar_key: "getting-started/installation-and-upgrade/netinstall/netinstall-linux"
sidebar_position: 2
title: "Linux 版 Netinstall"
sidebar_label: "Linux 版 Netinstall"
description: "本頁介紹 netinstall-cli，這是 MikroTik Netinstall 實用工具的 Linux 命令列版本，涵蓋用於單臺和多臺裝置重灌的所有命令列選項、指令碼和配置標誌、網路選項，以及一個分步安裝示例。"
tags:
  - 'netinstall'
source: https://manual.mikrotik.com/docs/7.24/getting-started/installation-and-upgrade/netinstall/netinstall-linux
captured_at: '2026-11-04T11:28:43+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Netinstall 的 Linux 版本 `netinstall-cli` 是一個命令列工具，提供的功能與 Windows 版本幾乎相同。

:::tip
在執行 netinstall 工具之前，請確保已在計算機的介面上設定靜態 IP 地址。

```bash
sudo ip addr add 192.168.88.2/24 dev <interface>
sudo ip link set <interface> up
```
:::

:::info
此工具需要 root 許可權。必須以 root 身份執行，或使用 `sudo` 執行。
:::

## netinstall-cli 命令列選項 {#netinstall-cli-command-line-options}

`netinstall-cli` 命令語法為：

```
netinstall-cli [-r] [-e] [-b] [-m [-o]] [-f] [-c] [-v] [--reboot] [--shutdown] [-k <keyfile>] [-s <userscript>] [-sm <modescript>] [--mac <mac address>] {-i <interface> | -a <client-ip>} [PACKAGE]+ 
```

## 通用選項 {#general-options}

| 引數 | 描述 |
| :-- | :-- |
| **-r** | 重新安裝裝置並應用預設配置指令碼。 |
| **-e** | 重新安裝裝置但不應用預設配置指令碼，使裝置保留空配置。 |
| **-b** | 丟棄裝置上當前安裝的品牌包。如果未指定，則保留品牌包。出廠安裝的品牌包無法丟棄，且始終會保留。 |
| **-f** | 忽略儲存大小限制。預設情況下，netinstall-cli 會檢查路由器的儲存容量。如果所選軟體包的總大小超過可用儲存空間，則會顯示錯誤：**"Ignoring XX:XX:XX:XX:XX:XX, not enough space (override with -f)"** |
| **-c** | 允許同一臺計算機上同時執行多個 Netinstall 例項。 |
| **-v** | 啟用詳細模式以輸出詳細資訊。 |

### 多裝置重灌選項 {#multiple-device-reinstallation-options}

| 引數 | 描述 |
| :-- | :-- |
| **-m** | 啟用多裝置重灌。同一裝置將按照收到的 BOOTP 請求次數重複重灌。 |
| **-o** | 將安裝限制為每次 Netinstall 執行僅一次。該工具會跟蹤成功安裝裝置的 MAC 地址，並在當前會話期間忽略來自同一 MAC 地址的後續 BOOTP 請求。 |

**組合行為：**

- 未指定 `-m` 且未指定 `-o`：僅進行一次成功安裝，然後 Netinstall 關閉。
- 僅指定 `-m`：啟用多次重灌；同一裝置會重複重灌。
- 僅指定 `-o`：與未指定標誌相同；每次執行僅一次安裝，然後關閉。
- 同時指定 `-m` 和 `-o`：啟用多次重灌，但每個裝置在每個會話中僅安裝一次。

### 指令碼和配置選項 {#script-and-configuration-options}

| 引數 | 描述 |
| :-- | :-- |
| **--reboot** | 重啟已引導進入 Netinstall 模式的所選 MikroTik 裝置。 |
| **--shutdown** | 關閉已引導進入 Netinstall 模式的所選 MikroTik 裝置。 |
| **-k \<keyfile>** | 向裝置提供 .KEY 格式的許可證金鑰檔案（可選）。 |
| **-s \<userscript>** | 允許在安裝期間向裝置安裝自定義預設配置指令碼。這會替換 RouterOS 提供的預設配置指令碼。請參閱 `/system/default-configuration/custom-script/print`。該指令碼在 RouterOS 更新期間會保留，並在後續配置重設後使用，直到裝置使用新指令碼重新安裝或該指令碼被移除。 |
| **-sm \<modescript>** | 指定在裝置安裝後首次啟動時執行的一次性自定義指令碼。可使用此指令碼配置 device-mode、protected-routerboot 和其他部署設定。模式指令碼會在任何自定義或預設配置指令碼之前執行，並在執行後自動移除。如果該指令碼修改了 device-mode，裝置會立即重啟。**需要 RouterOS 和 Netinstall 版本 7.22 或更高版本。** |

### 網路選項 {#network-options}

| 引數 | 描述 |
| :-- | :-- |
| **--mac \<mac address>** | 指定允許安裝的 MAC 地址。指定後，將忽略所有其他 BOOTP 請求。 |
| **-i \<interface>** | 指定用於安裝的網路介面（可選，推薦）。 |
| **-a \<client-ip>** | 指定 Netinstall 伺服器分配給裝置的特定 IP 地址。除非使用 `-i` 引數（允許自動分配），否則此項為必填。 |

### 軟體包選擇 {#package-selection}

| 引數 | 描述 |
| :-- | :-- |
| **PACKAGES** | 指定要以 .NPK 格式安裝到裝置上的 RouterOS 軟體包列表。此引數為必填項。**system package** 必須列在首位。 |

:::warning
**配置保留行為：**

當未指定 `-r` 也未指定 `-e` 時，netinstall-cli 會在保留當前配置的情況下重新安裝 RouterOS。它會從路由器下載現有配置資料庫，在重灌期間重新格式化磁碟，然後將配置上傳回裝置。這與 Netinstall GUI 中的 **“保留舊配置”** 選項一致。

注意：此過程僅適用於配置本身。User Manager 資料庫、Dude 資料庫等單獨儲存的檔案和資料庫以及其他資料不會被保留。
:::

## Linux Netinstall 示例 {#linux-netinstall-example}

從 [MikroTik 下載頁面](https://mikrotik.com/download) 下載該工具：

```bash
wget https://download.mikrotik.com/routeros/[VERSION]/netinstall-[VERSION].tar.gz
```

解壓歸檔檔案：

```bash
tar -xzf netinstall-[VERSION].tar.gz
```

配置網路介面（將 eth0 替換為你的介面名稱）：

```bash
sudo ip link set eth0 down
sudo ip addr add 192.168.88.2/24 dev eth0
sudo ip link set eth0 up
```

執行安裝。該工具需要 root 許可權，請使用 sudo：

```bash
sudo ./netinstall-cli [-parameters] [address/interface] routeros-[architecture]-[package VERSION].npk
```

```bash
sudo ./netinstall-cli -i eth0 -v -e  routeros-7.23.1-arm64.npk wifi-qcom-7.23.1-arm64.npk container-7.23.1-arm64.npk 
Version: 7.24beta1(2026-05-26 11:17:51)
Will apply empty config
Waiting for Link-UP on eth0
Using client IP 192.168.88.3
Waiting for RouterBOARD...
Received a BOOTP request from 01:23:45:67:89:AA (arm64)
Assigned 192.168.88.3 to 01:23:45:67:89:AA
blksize 1452
Booting device 01:23:45:67:89:AA into setup mode
Formatting device 01:23:45:67:89:AA
Sending packages to device 01:23:45:67:89:AA
Packages sent to device 01:23:45:67:89:AA
Rebooting device 01:23:45:67:89:AA
Successfully finished installing device 01:23:45:67:89:AA
```

:::tip
想了解其他安裝方法？請參閱 [**Windows**](./netinstall-windows.md) 或 [Netinstall 安裝包](./netinstall-package.md) 說明。
:::
