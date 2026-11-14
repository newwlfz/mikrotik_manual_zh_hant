---
sidebar_key: "getting-started/installation-and-upgrade/netinstall/netinstall-package"
sidebar_position: 3
title: "Netinstall 安裝包"
sidebar_label: "Netinstall 安裝包"
description: "本頁介紹 RouterOS Netinstall 軟體包，它允許從另一臺執行 RouterOS 7.24beta1 或更新版本的路由器遠端在 MikroTik 裝置上重新安裝 RouterOS，內容涵蓋先決條件、/tool/netinstall 選單和引數、快取，以及一個 Preboot Etherboot 恢復用例。"
tags:
  - 'netinstall'
source: https://manual.mikrotik.com/docs/7.24/getting-started/installation-and-upgrade/netinstall/netinstall-package
captured_at: '2026-11-04T11:28:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**Netinstall 軟體包**是一個額外軟體包，適用於從 7.24beta1 版本開始執行 RouterOS 的所有裝置，並適用於除 SMIPS 之外的所有架構。

此軟體包允許從另一臺執行 RouterOS 的 MikroTik 裝置遠端重新安裝 RouterOS。

## 先決條件 {#prerequisites}

- RouterOS 版本 7.24beta1 及更高版本。
- Netinstall 軟體包已啟用。
- 目標 MikroTik 硬體路由器連線到與正在重新安裝的裝置相同的 L2 網段。

:::warning
預設情況下，**Netinstall 軟體包**會在根目錄中建立 `NetinstallCache` 目錄。在有 `flash` 目錄的裝置上，Netinstall 相關檔案儲存在 RAM 中。在沒有 `flash` 目錄的裝置上，這些檔案儲存在裝置的永續性儲存中。

確保 **Netinstall** 伺服器裝置有足夠的可用儲存空間或 RAM。

你也可以在 **Netinstall → Settings** 中配置外部儲存裝置，將其用作 `NetinstallCache/` 目錄。
:::

> 從 `Files` 選單中實際刪除的檔案，如果當前已快取，將會自動重新下載。要刪除快取檔案，請從 `Netinstall Cache` 選單中移除它們。
> 如果檔案在裝置重啟之前已下載，它們將被刪除。

## 安裝流程 {#installation-workflow}

1. 安裝並啟用 Netinstall 軟體包。**Netinstall 軟體包**可用於 WinBox、WebFig GUI 和 CLI，位於 **Tools** 選單下，或在 CLI 中使用 `/tools/netinstall`。

2. 配置 Netinstall 介面。新增新的 **Netinstall** 介面，設定所需引數，並讓連線到該介面的裝置以 BOOTP 模式啟動。

3. 下載或選擇所需的 RouterOS 軟體包。**Netinstall 軟體包**會自動為目標裝置架構安裝適當的 **System** 軟體包。

4. 將目標裝置啟動到 Etherboot 模式。

5. 安裝 RouterOS。

:::tip
如果未設定 **Version** 引數，**Netinstall 軟體包**將安裝當前在 **Netinstall 伺服器**上所選的 `Check for Updates` 通道中可用的最新 RouterOS 版本。
:::

必須顯式選擇額外軟體包。

## 通用配置選項 {#general-configuration-options}

| 引數 | 描述 |
| :-- | :-- |
| **Settings** | 允許設定 `NetinstallCache/` 路徑目錄。參見[先決條件警告資訊](#prerequisites)。示例：`/tool/netinstall/settings/set cache-directory=...` |

## Netinstall 引數 {#netinstall-parameters}

| 引數 | 描述 |
| :-- | :-- |
| **allow-etherboot**（yes / no；預設：**yes**） | 允許在所選介面上接收 BOOTP 請求。如果設定為 no，將忽略該裝置。 |
| **allow-flashfig**（yes / no；預設：**yes**） | 啟用 [FlashFig](../../../management-tools/flashfig.md) 功能 |
| **apply-default-configuration**（yes / no；預設：**no**） | 如果啟用，裝置將在安裝並重啟後應用預設配置指令碼。參見 `/system/default-configuration/script/print`。 |
| **auto-reboot**（none / reboot / shutdown；預設：**reboot**） | 定義裝置安裝成功完成後執行的操作。 |
| **etherboot-image** | 允許選擇先前快取的要安裝的軟體包。 |
| **etherboot-image-arch** | 指定 etherboot 映像所需的 CPU 架構。所有其他架構請求都將被忽略。如果未指定，將使用檢測到的架構。 |
| **extra-packages** | 允許新增要與 `system` 軟體包一起安裝的額外軟體包。預設將安裝 `routeros` 軟體包。 |
| **install-once**（yes / no；預設：**yes**） | 將安裝限制為每次 Netinstall 執行僅一次。該工具會跟蹤成功安裝裝置的 **MAC 地址**，並在當前會話期間忽略來自同一 **MAC 地址**的後續 **BOOTP** 請求。 |
| **interface** | 指定 **Netinstall 伺服器**的網路介面。 |
| **ip-range** | 自定義用於 netinstall 過程的 **BOOTP** IP 範圍。 |
| **keep-old-configuration**（yes / no；預設：**yes**） | 指示 Netinstall 在安裝後讀取並恢復裝置核心配置（/export；/users）。此選項不會保留使用者檔案、容器或類似資料。 |
| **mac-address** | 指定允許安裝的 MAC 地址。提供後，所有其他 BOOTP 請求都將被忽略。 |
| **mode-file** | 類似於 `Mode script`。指定在安裝後設備首次啟動時執行的一次性自定義指令碼。使用此指令碼可在裝置部署期間配置 device-mode、protected-routerboot 和其他設定。mode script 會在任何自定義或預設配置指令碼之前執行。完成後，該指令碼會自動從裝置中移除。如果該指令碼修改了 device-mode，裝置將在執行後立即重啟。 |
| **place-before** | 將規則插入到現有規則之前 |
| **remove-branding**（yes / no；預設：**no**） | 從裝置中丟棄當前已安裝的品牌包。如果未指定，則保留品牌包。出廠安裝的品牌包無法丟棄，並且始終會保留。 |
| **script-file** | 允許在安裝期間在裝置上安裝自定義預設配置指令碼。這會替換 RouterOS 提供的預設配置指令碼。參見 `/system/default-configuration/custom-script/print`。該指令碼在 RouterOS 更新期間會保留，並在後續配置重設後使用，直到裝置使用新指令碼重新安裝或該指令碼被移除。 |
| **version** | 指定要安裝的 RouterOS 版本。如果未設定 **Version** 引數，**Netinstall** 將安裝當前在 **Netinstall 伺服器**上所選的 `Check for Updates` 通道中可用的最新 RouterOS 版本。 |
| **wait**（yes / no；預設：**no**） | 使裝置保持在 etherboot 狀態，並等待使用者命令開始安裝。 |

## 快取 {#cache}

可用操作：GUI 和 CLI 均為 `Add`。

| 引數 | 描述 |
| :-- | :-- |
| **arch** | 必填引數。指定要下載的必要檔案的 CPU 架構。 |
| **packages** | 允許新增要下載到 `NetinstallCache/` 目錄的額外軟體包列表。 |
| **version** | 指定要下載的 RouterOS 版本軟體包。如果未設定 **Version** 引數，**Netinstall** 將下載當前在 **Netinstall 伺服器**上所選的 `Check for Updates` 通道中可用的最新 RouterOS 版本。 |

## 裝置 {#devices}

**Netinstall Devices** 選單顯示已透過 Netinstall 安裝的裝置列表及其狀態。

可用操作：

- 使用 `Clear` 清空列表。
- `Install` 選單。如果透過 `Install` 選單選擇了額外引數，則所有先前設定的設定都將被覆蓋。

可用的 `install` 引數：`auto-reboot`、`extra-packages`、`numbers`、`version`。

```bash
/tool/netinstall/devices> install auto-reboot=reboot extra-packages=user-manager version=7.24beta1
```

| 引數 | 描述 |
| :-- | :-- |
| **auto-reboot**（none / reboot / shutdown；預設：**reboot**） | 定義裝置安裝成功完成後執行的操作。 |
| **extra-packages** | 允許新增要與 `system` 軟體包一起安裝的額外軟體包。預設將安裝 `routeros` 軟體包。 |
| **numbers** | 允許選擇列表中的哪些裝置要重新安裝 RouterOS。 |
| **version** | 指定要下載的 RouterOS 版本軟體包。如果未設定 **Version** 引數，**Netinstall** 將安裝為介面主設定選擇的 **version**；如果未指定，則下載當前在 **Netinstall 伺服器**上所選的 `Check for Updates` 通道中可用的最新 RouterOS 版本。 |

## 使用案例 {#use-cases}

**Netinstall 軟體包**可在 [Preboot Etherboot](../../../hardware/routerboard.md#preboot-etherboot) 中使用，適用於以下場景：一臺已安裝 Netinstall 軟體包的 MikroTik 路由器專用於遠端恢復。設定 Netinstall 伺服器的 `preboot-etherboot-server=ip_address`，並在目標裝置出現任何問題時遠端重新安裝 RouterOS。

:::danger
請記住停用或嚴格過濾所建立的規則，以免在每次重啟時無意中重新安裝系統。
:::

### Netinstall 軟體包示例 {#netinstall-package-example}

```bash
[admin@MikroTik] /tool/netinstall/add interface=bridge1 keep-old-configuration=no apply-default-configuration=yes auto-reboot=reboot mac-address=01:23:45:67:89:BB extra-packages=wifi-qcom,container version=7.23.1 ip-range=192.168.88.10-192.168.88.20
```

驗證快取的軟體包：

```bash
[admin@MikroTik] /tool/netinstall/cache/print 
Columns: PATH, URL, STATUS
#  PATH                                               URL                                                                                STATUS    
0  NetinstallCache/container-7.23.1-arm64.npk  https://upgrade.mikrotik.com/routeros/7.23.1/container-7.23.1-arm64.npk  downloaded
1  NetinstallCache/linux.arm64                 https://upgrade.mikrotik.com/routeros/7.23.1/netinstk/linux.arm64        downloaded
2  NetinstallCache/linux.arm64-uefi            https://upgrade.mikrotik.com/routeros/7.23.1/netinstk/linux.arm64-uefi   downloaded
3  NetinstallCache/wifi-qcom-7.23.1-arm64.npk  https://upgrade.mikrotik.com/routeros/7.23.1/wifi-qcom-7.23.1-arm64.npk  downloaded
```

安裝後檢查裝置狀態：

```bash
[admin@MikroTik] /tool/netinstall/devices/print 
Flags: N - NETINSTALL
Columns: MAC-ADDRESS, INTERFACE, STATE, LAST-STATE-UPDATE, EXTRA-PACKAGES, VERSION, ARCH, MODEL, LAST-STATE, AUTO-REBOOT
#   MAC-ADDRESS        INTERFACE  STATE    LAST-STATE-UPDATE  EXTRA-PACKAGES  VERSION    ARCH   MODEL       LAST-STATE        AUTO-REBOOT
0 N 01:23:45:67:89:BB  bridge1    done     58s                container       7.23.1     arm64   L009UiGS   bootp reply sent  reboot     
                                                              wifi-qcom 
```

:::tip
正在尋找其他安裝方法？請參閱 [**Windows**](./netinstall-windows.md) 或 [**Linux**](./netinstall-linux.md) 的說明。
:::
