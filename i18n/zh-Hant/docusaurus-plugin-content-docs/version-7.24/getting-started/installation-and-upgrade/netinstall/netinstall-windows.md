---
sidebar_key: "getting-started/installation-and-upgrade/netinstall/netinstall-windows"
sidebar_position: 1
title: "Windows 版 Netinstall"
sidebar_label: "Windows 版 Netinstall"
description: "本頁介紹如何在 Windows 上使用 Netinstall 工具在 MikroTik 裝置上安裝或重新安裝 RouterOS，涵蓋前提條件、使用靜態 IP 進行網路準備、以 Etherboot 模式啟動裝置、安裝引數以及安裝後步驟。"
tags:
  - 'netinstall'
source: https://manual.mikrotik.com/docs/7.24/getting-started/installation-and-upgrade/netinstall/netinstall-windows
captured_at: '2026-11-04T11:29:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南介紹如何在 Windows 計算機上使用 Netinstall 實用程式在 MikroTik 裝置上安裝 RouterOS。

## 先決條件 {#prerequisites}

:::tip
在執行 Netinstall 工具之前，請確保已在計算機的介面上設定靜態 IP 地址。
:::

- 從[下載頁面](https://mikrotik.com/download)下載 **Netinstall** 實用程式（Stable、Testing 或 Development 版本）。
- 從[下載頁面](https://mikrotik.com/download)下載 RouterOS **System Package**，以及你需要或特定裝置必須使用的所有額外軟體包（例如 wireless、wifi-qcom、container 等）。

:::tip
選擇標記為 **LongTerm** 或 **Stable** 的 RouterOS 版本。選擇適當的架構（ARM64、ARM、MIPSBE、TILE 等）。如果不確定，請下載適用於所有架構的 RouterOS 軟體包——Netinstall 會自動為你的裝置選擇正確的軟體包。
:::

該工具要求目標裝置以 BOOTP 模式啟動，才能被檢測和訪問。

### 可用操作與引數 {#available-actions-and-parameters}

| 控制元件/操作 | 說明 |
| :-- | :-- |
| **Net booting** | 啟用、停用並配置 Netinstall 內建 BOOTP 和 TFTP 伺服器的 IP 定址。這是使用 Netinstall 用戶端對 MikroTik 裝置進行網路啟動所必需的。 |
| **Shutdown** | 關閉已啟動到 Netinstall 模式的所選 MikroTik 裝置。 |
| **Reboot** | 重啟已啟動到 Netinstall 模式的所選 MikroTik 裝置。 |
| **Install** | 使用指定選項在所選 MikroTik 裝置上執行 RouterOS 安裝。 |
| **Cancel** | 取消當前正在進行的安裝。 |
| **Routers/Drives** | 顯示可用於安裝的裝置。裝置只有在以 Netinstall 模式啟動後才會出現在此列表中。 |
| **Packages** | 允許選擇包含 RouterOS 軟體包檔案的目錄，並建立軟體包集以供後續安裝使用。 |

### Netinstall 引數 {#netinstall-parameters}

| 引數 | 說明 |
| :-- | :-- |
| **Auto Reboot** | 定義裝置安裝成功完成後執行的操作。 |
| **Software ID** | 顯示當前裝置的 Software ID。 |
| **Key** | 允許在安裝期間指定並安裝新的許可證金鑰。預設情況下，Netinstall 會保留從裝置檢測到的許可證金鑰。 |
| **Keep Old Configuration** | 指示 Netinstall 在安裝後讀取並恢復裝置核心配置（/export; /users）。此選項不會保留使用者檔案、容器或類似資料。 |
| **Keep Branding** | 指示 Netinstall 保留裝置上的 branding 軟體包（如果存在）。出廠安裝的 branding 軟體包無法丟棄，並且始終會被保留。 |
| **Apply Default Config** | 如果啟用，裝置將在安裝並重啟後應用預設配置指令碼。參見 `/system/default-configuration/script/print`。 |
| **Configure Script** | 允許在安裝期間在裝置上安裝自定義預設配置指令碼。這會替換 RouterOS 提供的預設配置指令碼。參見 `/system/default-configuration/custom-script/print`。該指令碼會在 RouterOS 更新期間保留，並在後續配置重設後使用，直到使用新指令碼重新安裝裝置或刪除該指令碼。從 RouterOS 7.10beta8 開始，該指令碼可以使用只讀變數 `$defconfPassword` 和 `$defconfWifiPassword` 訪問出廠設定的密碼。 |
| **Mode Script** | 指定一個一次性自定義指令碼，該指令碼在安裝後設備首次啟動時執行。使用此指令碼可在裝置部署期間配置 **device‑mode**、**protected‑routerboot** 和其他設定。mode 指令碼會在任何自定義或預設配置指令碼之前執行。完成後，指令碼會自動從裝置中刪除。如果指令碼修改了 device-mode，裝置會在執行後立即重啟。**此功能需要 RouterOS 和 Netinstall 7.22 或更新版本。** |
| **IP Address / Gateway / Baudrate** | Netinstall 會自動建立一個包含指定引數的 Configure 指令碼，用於透過 IPv4 連線或序列控制檯進行初始裝置配置。此引數僅在安裝到空配置（即未指定其他配置選項）時可用。 |

>Configure 和 Mode 指令碼是[常規/匯入檔案](../../configuration-management/index.md#configuration-export-and-import)，接受有效的 MikroTik RouterOS CLI 命令。

## 準備計算機網路 {#prepare-your-computer-network}

1. 停用計算機上的所有網路介面（WiFi、Ethernet、LTE 或任何其他連線），但用於安裝的 Ethernet 介面除外。Netinstall 僅在一個活動介面下工作。
    :::warning
    強烈建議停用所有其他網路介面，以確保 Netinstall 選擇正確的網路介面。
    :::

2. 為你的 Ethernet 介面配置靜態 IP 地址：

    - 開啟 **Start** 並選擇 **Settings**。

    ![](/img/e177e8b51de21f60.png)

    - 轉到 **Network & Internet** 並選擇 **Change adapter options**。

    ![](/img/41f294009d807abb.png)
    ![](/img/a45897907aee8b35.png)

    - 右鍵單擊你的 **Ethernet** 介面，然後選擇 **Properties**。

    ![](/img/8f42bc4977e9dc89.png)

    - 選擇 **Internet Protocol Version 4 (TCP/IPv4)**，然後單擊 **Properties**。

    ![](/img/fb1a3c22a8a034d2.png)

    - 勾選 **Use the following IP address** 並配置：IP 地址 `192.168.88.1`，子網掩碼 `255.255.255.0`。

    ![](/img/0c4b10ebe6db913b.png)

:::tip
Netinstall 也可以在本地網路上執行。在這種情況下，你可以跳過設定靜態 IP 地址，但如果你不熟悉 Netinstall，強烈建議設定靜態 IP 地址。
:::

## 啟動 Netinstall {#start-netinstall}

1. 將 Netinstall `.zip` 檔案解壓到方便的位置。

   ![](/img/baa819290ebdda2c.png)
   ![](/img/dad9c0e9fbc429ef.png)

2. 確保你的 Ethernet 介面已連線，然後啟動 `Netinstall.exe`。
   :::danger
   Netinstall 需要管理員許可權。請接受許可權提示，以便 Netinstall 正常工作。

   **提示：** 如果你嚴格按照本指南操作，你的計算機應該沒有 Internet 連線。Windows 10 可能會顯示有關驗證應用的警告——單擊 **Run** 繼續。
   :::

3. 出現提示時，允許 Netinstall 訪問 **Public** 網路。

   ![](/img/868d42c748b371f1.png)

4. 配置 **Net booting** 設定：
   - 設定 **Client IP** 地址（必須唯一，且未被網路中的任何其他裝置使用，包括你的計算機）。
   - 使用與計算機靜態 IP 處於同一子網，但不同於計算機地址的 IP 地址。

   ![](/img/3cb60e47476f22b8.png)

## 連線裝置 {#connect-the-device}

1. 使用乙太網線將裝置直接連線到計算機（中間不要有其他裝置）。
2. 將乙太網線插入裝置的 **Ether1** 埠或標有 **BOOT** 的埠。
   :::danger
   某些計算機（尤其是 USB 乙太網介面卡）可能會產生額外的鏈路抖動，導致 Netinstall 無法檢測到處於 Etherboot 模式的裝置。如果發生這種情況，請在裝置和計算機之間使用交換器，或使用處於橋接模式的 RouterOS 路由器。如果使用橋接模式的路由器，請停用橋接介面上的任何 DHCP 用戶端，並停用 [檢測網際網路](../../../diagnostics-monitoring-and-troubleshooting/detect-internet.md) 功能。

   Netinstall 使用 BOOTP 封包，這些封包使用與 DHCP 封包相同的埠號。如果使用交換器，請確保橋接埠未被其他網路裝置阻塞。如果啟用了 DHCP snooping，請在面向 Netinstall PC 的橋接埠上啟用 "trusted"。
   :::

3. 給裝置上電，並將其置於 Etherboot 模式。

## 安裝 RouterOS {#install-routeros}

1. 等待裝置出現在 Netinstall 中。

2. 選擇裝置並單擊 **Browse**。導航到 RouterOS 軟體包所在位置，然後按 **OK**。

   ![](/img/cdce5835cc961661.png)

3. **"Keep old configuration"** 過程會從路由器下載配置資料庫，重新安裝路由器（包括格式化磁碟），然後將配置上傳回去。此過程僅適用於配置本身，不會影響檔案，包括 User Manager 資料庫、Dude 資料庫等資料庫。

   ![](/img/3c8668518faad329.png)

4. **"Keep branding"** 選項允許你保留裝置上已安裝的 branding 軟體包，而無需使用 Netinstall 重新安裝它。

   ![](/img/a9503edb1445efa4.png)

   :::tip
   使用 **Configure script** 選項時，建議在執行配置之前引入[延遲](../../configuration-management/index.md#startup-delay)。
   :::

5. 選擇所需的 RouterOS 軟體包，然後按 **Install**。

   ![](/img/0965aedf27576b5a.png)

6. 等待安裝完成。根據 Netinstall 版本和裝置的不同，可能需要手動重啟。

   ![](/img/d57d515d46955d0e.png)
   :::warning
   如果你下載了適用於多個架構的 RouterOS 軟體包，Netinstall 只會在選擇裝置後顯示適合該裝置的架構軟體包。不受支援的軟體包不會出現在視窗中。

   如果安裝沒有開始（進度條不移動或未顯示狀態），請嘗試關閉並重新開啟 Netinstall，或再次將裝置置於 Etherboot 模式。如果問題仍然存在，請嘗試在其他計算機上使用 Netinstall。
   :::

## 安裝後 {#post-installation}

使用 Netinstall 後，裝置會重設為預設設定（除非你指定不應用預設配置或 Keep old configuration）。出於安全原因，某些裝置在使用預設配置時無法透過 **Ether1** 埠訪問。有關詳細資訊，請參閱[預設配置](../../configuration-management/default-configurations.md)。

## 完成設定 {#complete-setup}

你的裝置現已準備就緒。根據需要配置裝置，並將其重新連線到網路。

[首次配置](../../first-time-configuration.md)

:::tip
正在尋找其他安裝方法？請參閱 [**Linux**](./netinstall-linux.md) 或 [Netinstall 安裝包](./netinstall-package.md) 說明。
:::
