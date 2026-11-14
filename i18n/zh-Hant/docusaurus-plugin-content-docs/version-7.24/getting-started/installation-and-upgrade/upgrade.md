---
sidebar_key: "getting-started/installation-and-upgrade/upgrade"
sidebar_position: 2
title: "升級"
sidebar_label: "升級"
description: "本頁面介紹 MikroTik 裝置的 RouterOS 升級流程，涵蓋透過釋出鏈（Long term、Stable、Testing、Development）進行的自動更新、透過 WinBox/WebFig/FTP 進行的手動升級，以及 bootloader 升級建議。文中說明了版本編號約定、更新工作流程，以及針對關鍵安全步驟的故障排查警告。"
tags:
  - 'upgrade'
  - 'release-chains'
source: https://manual.mikrotik.com/docs/7.24/getting-started/installation-and-upgrade/upgrade
captured_at: '2026-11-04T11:29:08+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik 裝置預裝 RouterOS，因此通常不需要安裝，除非要在裸機 x86 PC 上安裝 RouterOS，或透過 CHR 映象在虛擬機器上安裝。已安裝裝置上的升級過程很簡單。

## 版本編號 {#version-numbering}

RouterOS 版本在使用句點分隔序列時按順序編號；它*不*表示小數點，並且各序列*不*具有位值意義。例如，識別符號 2.5 不是“二點五”或“到版本三的一半”；它是第二個一級修訂的第五個二級修訂。因此 v5.2 比 v5.18 舊，而 v5.18 更新。

RouterOS 版本透過多個“釋出鏈”釋出：Long term、Stable、Testing 和 Development。升級 RouterOS 時，可以選擇一個釋出鏈，從中安裝新軟體包：

- **Long term**：很少釋出，且僅包含最關鍵的修復。同一編號分支內的升級不包含新功能。當 **Stable** 版本釋出一段時間並看起來足夠穩定後，它會被提升到長期分支，替換較舊的版本，而舊版本隨後會被移入歸檔。這會連續新增新功能。
- **Stable**：每隔幾個月釋出，包含所有經過測試的新功能和修復。
- **Testing**：每隔幾周釋出，僅經過基本內部測試，不應在生產環境中使用。
- **Development**：在需要時釋出。包含原始更改，面向希望測試新功能的軟體愛好者。

<center>![](/img/f71534dc9d81988a.webp)</center>

## 標準升級 {#standard-upgrade}

軟體包升級功能會從路由器透過 HTTPS（自 v7.23 起）連線到 MikroTik 下載伺服器，並檢查所選釋出通道中是否有更新的 RouterOS 版本。此選單也可用於降級，只需將通道切換為提供較舊但更穩定版本的通道。請注意，該功能是從路由器而不是你的計算機發起連線，因此路由器本身需要具備到 MikroTik 伺服器的 HTTPS 連線能力。請確保可能位於此路由器前方的任何防火牆都允許 TCP 埠 443。

在 QuickSet 或 System → Packages 選單中點選 *Check for Updates* 按鈕後，將開啟 *Check for Updates* 視窗，其中顯示當前變更日誌或最新變更日誌（如果存在更新版本）。如果可用更新版本，將顯示 *Download* 和 *Download&Install* 按鈕。點選 *Download* 會下載最新版本（需要手動重啟裝置），而點選 *Download&Install* 會開始下載，並在下載成功後自動重啟裝置。

提供的版本取決於所選的釋出通道。並非所有版本都可用。使用檢查更新方式時，無法一步從較舊版本升級到最新版本。例如，如果執行 RouterOS v6.x，即使選擇名為 "Upgrade" 的大版本升級通道，也只會看到 v7.12.1 作為可用版本。你必須先升級到該中間版本，之後通道中才會提供更新的版本。此中間步驟也可以使用檢查更新完成；你只需在首次更新到中間版本後再次執行檢查更新。

如果安裝了自定義軟體包，下載器會考慮這一點並下載所有必要的軟體包。

:::warning
強烈建議在 RouterOS 更新後升級 bootloader。要升級 bootloader，請在 CLI 中執行 [`/system/routerboard/upgrade`](../../cli-reference/system/routerboard/upgrade.md) 命令，然後重啟。或者，在 GUI 中導航到 System → RouterBOARD 選單，點選 "Upgrade" 按鈕，然後重啟裝置。
:::

你可以透過在系統排程器中執行指令碼來**自動化**升級過程。此指令碼會向 MikroTik 升級伺服器查詢新版本。如果收到的響應為 "New version is available"，指令碼隨後會發出下面的升級命令。重要說明：如果你是在較舊版本上首次執行此指令碼，則不會生效。它可能無法看到最新版本為可用；如果你執行的是 v6.x，必須先手動選擇 "Upgrade" 通道，執行到 v7.12.1 中間版本的大版本升級，之後較新的 v7 版本才會顯示在升級通道中。

```ros
/system/package/update/check-for-updates
:delay 3s;
:if ( [/system/package/update get status] = "New version is available") do={ /system/package/update/install }
```

## 手動升級 {#manual-upgrade}

可以透過以下方式升級 RouterOS：

- WinBox – 將檔案拖放到 Files 選單。
- WebFig - 從 Files 選單上傳檔案。
- FTP - 將檔案上傳到根目錄。

:::warning
強烈建議在升級 RouterOS 後升級 bootloader。要升級 bootloader，請在 CLI 中執行 [`/system/routerboard/upgrade`](../../cli-reference/system/routerboard/upgrade.md) 命令，然後重啟。或者，在 GUI 中導航到 System → RouterBOARD 選單，點選 "Upgrade" 按鈕，然後重啟裝置。

**警告：** 無法透過序列埠線升級 RouterOS。使用此方法只能升級 [RouterBOOT](./routerboot.md#simple-upgrade)。
:::

### 手動升級過程 {#manual-upgrade-process}

- 訪問 [www.mikrotik.com](http://www.mikrotik.com)，進入 Software 頁面，然後選擇你安裝 RouterOS 的系統架構（系統架構可在 System → Resource 部分找到）。
- 下載 **routeros *(main)*** 以及裝置上已安裝的額外軟體包。
- 使用前面提到的方法之一將軟體包上傳到裝置。

如果需要跳過某個特定軟體包的升級，或者某個軟體包檔案已不再可用，請使用 [`/system/package/update/install ignore-missing`](../../cli-reference/system/package/update/install.md) 來跳過缺失的軟體包。

#### 使用 WinBox {#using-winbox}

選擇你的系統型別，並下載升級軟體包。使用 WinBox 連線到路由器。用滑鼠選中已下載的檔案，並將其拖到 Files 選單。如果其中已有一些檔案，請確保將軟體包放在根選單中，而不是 hotspot 資料夾內！上傳將開始。

<center>![](/img/0dc7b4abcd83694c.webp)</center>

完成後 - 重啟裝置。新的版本號將顯示在 Winbox 標題欄和 Packages 選單中

#### 使用 S/FTP {#using-sftp}

- 開啟你常用的 S/FTP 程式，選擇軟體包，並將其上傳到路由器。
- 如果需要，你可以檢查檔案是否已成功傳輸到路由器（可選）。

```ros
[admin@MikroTik] >/file/print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME                  TYPE       SIZE     CREATION-TIME       
0  routeros-7.9-arm.npk  package    13.0MiB  2023-05-18 16:16:18
1  pub                   directory           2022-11-04 11:22:19
2  ramdisk               directory           1970-01-01 03:00:24
```

- 重啟路由器以開始升級過程。

```ros
[admin@MikroTik] >/system/reboot
Reboot, yes? [y/N]: y

```

- 重啟後，你的路由器將是最新版本，你可以在此選單中檢查：

```ros
/system/package/print

```

- 如果路由器未正確升級，請務必檢查**日誌**

```ros
/log/print without-paging

```

## RouterOS 本地升級 {#routeros-local-upgrade}

你可以在本地網路內使用一臺擁有所有所需軟體包的裝置上的 [`/system/package/local-update`](../../cli-reference/system/package/index.md) 工具，升級一臺或多臺 MikroTik 路由器。下面是一個包含 3 臺路由器的簡單示例（同一方法也適用於擁有無限多臺路由器的網路）：

- 在主路由器的 Files 選單下放置所需軟體包：

<center>![](/img/33416bc0f10bc51a.webp)</center>

**可選**，你可以在主裝置之間設定一臺映象裝置；如果不需要，請跳過此步驟：

- 選擇 Local Package Sources 並啟用 Mirror device。將 Primary Server 設定為軟體包所在位置，10.155.136.50。Check Interval 的 **minimum** 設定可設為 00:07:12，屆時裝置將使用 Winbox 連線到主裝置並檢查軟體包。  
  如果有新的軟體包可用，它將開始下載；請注意，下載過程較慢，在使用大量檔案時可能需要一些時間。如果出現某些失敗，下載將在下次 Check 時繼續。

<center>![](/img/19a7104b3178b5ef.webp)</center>

- 將建立一個新的 `packs` 資料夾，映象裝置將在其中儲存軟體包：

<center>![](/img/f4440913970c962d.webp)</center>

- 在將被更新的裝置上新增新的軟體包源，在本示例中我們使用映象裝置 10.155.136.71：

<center>![](/img/5f508bcb1902b63e.webp)</center>

- 在 Local Update packages 標籤頁中點選 **Refresh** 後，使用 Winbox 的裝置將嘗試連線到源並檢查是否有新軟體包。

<center>![](/img/b1034914a72f4b14.webp)</center>

- 選擇軟體包並點選 **Download**，下載完成後，裝置需要重啟才能更新。

<center>![](/img/0f893624b863b331.webp)</center>

- 使用 `/system/package/local-update/refresh` 在指令碼中自動化此操作。例如，可以使用 Fetch 工具從我們的網頁下載軟體包：

```ros
/tool/fetch url=https://download.mikrotik.com/routeros/7.16.1/routeros-7.16.1-arm.npk
```
