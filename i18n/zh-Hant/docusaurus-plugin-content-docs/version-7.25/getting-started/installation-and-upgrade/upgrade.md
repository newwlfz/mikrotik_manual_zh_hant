---
sidebar_key: "getting-started/installation-and-upgrade/upgrade"
sidebar_position: 2
title: "升級"
sidebar_label: "升級"
description: "本頁介紹 MikroTik 裝置的 RouterOS 升級流程，涵蓋藉助釋出分支（Long term、Stable、Testing、Development）進行的自動更新、透過 WinBox/WebFig/FTP 進行的手動升級，以及 bootloader 升級建議。頁面還說明了版本號命名規則、更新工作流程，以及針對關鍵安全步驟的故障排除警告。"
tags:
  - 'upgrade'
  - 'release-chains'
source: https://manual.mikrotik.com/docs/7.25/getting-started/installation-and-upgrade/upgrade
captured_at: '2026-11-04T11:17:00+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik 裝置預裝 RouterOS，因此通常不需要安裝，除非是在裸機 x86 PC 或使用 CHR 映象的虛擬機器上安裝 RouterOS。已安裝裝置上的升級過程很直接。

## 版本編號 {#version-numbering}

RouterOS 版本按順序編號，其中用句點分隔序列；它*不*表示小數點，序列也*不*具有位值意義。例如，識別符號 2.5 並不是“二點五”或“到版本三的一半”；它是第二個一級修訂版的第五個二級修訂版。因此 v5.2 比 v5.18 舊，而 v5.18 更新。

RouterOS 版本透過多個“釋出鏈”釋出：Long term、Stable、Testing 和 Development。升級 RouterOS 時，可以選擇一個釋出鏈，從中安裝新軟體包：

- **Long term**：很少釋出，並且僅包含最關鍵修復。同一編號分支內的升級不包含新功能。當 **Stable** 版本釋出一段時間並看起來足夠穩定後，它會被提升到長期分支，替換較舊的版本，而較舊版本隨後會被移到歸檔中。這會連續新增新功能。
- **Stable**：每隔幾個月釋出，包含所有經過測試的新功能和修復。
- **Testing**：每隔幾周釋出，僅經過基本內部測試，不應在生產環境中使用。
- **Development**：在需要時釋出。包含原始更改，供軟體愛好者測試新功能。

<center>![](/img/f71534dc9d81988a.webp)</center>

## 標準升級 {#standard-upgrade}

軟體包升級功能會從路由器透過 HTTPS 連線到 MikroTik 下載伺服器，並檢查所選釋出通道中是否有更新的 RouterOS 版本可用。此選單也可用於降級，只需將通道更改為提供較舊但更穩定版本的通道。該功能從路由器而不是您的計算機發起連線，因此路由器本身需要具備到 MikroTik 伺服器的 HTTPS 連線能力。

在 QuickSet 或 System → Packages 選單中選擇 *Check for Updates* 按鈕後，將開啟 *Check for Updates* 視窗，其中顯示當前更新日誌或最新更新日誌（如果存在更新版本）。如果有更新版本可用，將顯示 *Download* 和 *Download&Install* 按鈕。選擇 *Download* 會下載最新版本（需要手動重啟裝置），而選擇 *Download&Install* 會開始下載，並在下載成功後自動重啟裝置。

提供的版本取決於所選的釋出通道。並非所有版本都可能可用。使用檢查更新方式無法一步從較舊版本升級到最新版本。例如，如果執行的是 RouterOS v6.x，即使選擇名為 "Upgrade" 的主版本升級通道，您也只會看到 v7.12.1 作為可用版本。您必須首先升級到該中間版本，之後通道中才會提供更新的版本。這個中間步驟也可以透過檢查更新來完成；只需在首次更新到中間版本後重複檢查更新即可。

如果安裝了自定義軟體包，下載器會考慮這一點並下載所有必要的軟體包。

### 檢查更新設定 {#check-for-updates-settings}

可以在 System → Packages → Check for Updates 視窗中，或使用 [`/system/package/update/set`](../../cli-reference/system/package/update/index.md) 命令來微調與 MikroTik 下載伺服器的連線：

- **Channel**：檢查新版本時要使用的升級通道。[釋出鏈](#version-numbering)在版本編號部分中進行了說明。
- **Mode**：用於連線 MikroTik 下載伺服器的協定。僅在您的網路阻止 HTTPS 時使用 `http`。建議使用 HTTPS。
- **IP version**：連線 MikroTik 下載伺服器時首選的 IP 版本。
- **Check certificate**：是否以及如何驗證伺服器 SSL 證書。始終使用 `yes` 以確保安全連線。可以使用 `yes-without-crl` 跳過 CRL 驗證。

```ros
/system/package/update/set channel=stable mode=https ip-version=auto check-certificate=yes
```

:::warning
強烈建議在 RouterOS 更新後升級載入程式。要升級載入程式，請在 CLI 中執行 [`/system/routerboard/upgrade`](../../cli-reference/system/routerboard/upgrade.md) 命令，然後重啟。或者，在 GUI 中導航到 System → RouterBOARD 選單，選擇 "Upgrade" 按鈕，然後重啟裝置。
:::

您可以透過在系統排程器中執行指令碼來**自動化**升級過程。此指令碼會查詢 MikroTik 升級伺服器以獲取新版本。如果收到的響應為 "New version is available"，指令碼隨後會執行下面的升級命令。如果您是在較舊版本上首次執行此操作，則不會生效。它可能無法將最新版本視為可用；如果您執行的是 v6.x，您需要先手動選擇 "Upgrade" 通道，執行到 v7.12.1 中間版本的主版本升級，之後更新的 v7 版本才會顯示在升級通道中。

```ros
/system/package/update/check-for-updates
:delay 3s;
:if ( [/system/package/update get status] = "New version is available") do={ /system/package/update/install }
```

### 故障排除 {#troubleshooting}

如果裝置未檢測到可用的升級，請確認它能夠解析並訪問升級伺服器。

```ros
:put [:resolve upgrade.mikrotik.com]
```

結果應為 `159.148.147.251`。如果該地址無法解析或解析為其他 IP，請檢查你的 DNS 設定。更多資訊請參閱 [DNS](../../network-management/dns.md) 文章。

確認 DNS 解析正常後，請驗證裝置能夠訪問伺服器：

```ros
/tool/ping address=159.148.147.251
```

如果 ping 失敗，請檢查您的防火牆規則、路由或上游連線。

確認 IP 連線正常工作後，請驗證 443 埠是否可達：

```ros
[admin@MikroTik] > /system/telnet 159.148.147.251 port=443
Connecting to 159.148.147.251
Connected to 159.148.147.251
```

## 手動升級 {#manual-upgrade}

可以透過以下方式升級 RouterOS：

- WinBox – 將檔案拖放到 Files 選單。
- WebFig - 從 Files 選單上傳檔案。
- FTP - 將檔案上傳到根目錄。

:::warning
強烈建議在升級 RouterOS 後升級引導載入程式。要升級引導載入程式，請在 CLI 中執行 [`/system/routerboard/upgrade`](../../cli-reference/system/routerboard/upgrade.md) 命令，然後重啟。或者，導航到 GUI 的 System → RouterBOARD 選單，選擇“Upgrade”按鈕，然後重啟裝置。

**警告：** 無法透過序列電纜升級 RouterOS。使用此方法只能升級 [RouterBOOT](./routerboot.md#simple-upgrade)。
:::

### 手動升級過程 {#manual-upgrade-process}

- 訪問 [www.mikrotik.com](http://www.mikrotik.com)，導航到 Software 頁面，然後選擇您安裝 RouterOS 的系統架構（系統架構可在 System → Resource 部分中找到）。
- 下載 **routeros *(main)*** 以及裝置上安裝的額外軟體包。
- 使用上述方法之一將軟體包上傳到裝置。

如果需要跳過某個特定軟體包的升級，或者某個軟體包檔案已不再可用，請使用 [`/system/package/update/install ignore-missing`](../../cli-reference/system/package/update/install.md) 來跳過缺失的軟體包。

#### 使用 WinBox {#using-winbox}

選擇您的系統型別並下載升級軟體包。使用 WinBox 連線到路由器。用滑鼠選擇已下載的檔案，並將其拖到 Files 選單。如果已經存在一些檔案，請確保將軟體包放在根選單中，而不是 hotspot 資料夾內！上傳將開始。

<center>![](/img/0dc7b4abcd83694c.webp)</center>

完成後，重啟裝置。新的版本號將顯示在 WinBox 標題和 Packages 選單中。

#### 使用 S/FTP {#using-sftp}

- 開啟 S/FTP 用戶端，選擇軟體包，並將其上傳到路由器。
- 您可以檢查檔案是否已成功傳輸到路由器（可選）。

```ros
[admin@MikroTik] >/file/print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME                  TYPE       SIZE     CREATION-TIME       
0  routeros-7.9-arm.npk  package    13.0MiB  2023-05-18 16:16:18
1  pub                   directory           2022-11-04 11:22:19
2  ramdisk               directory           1970-01-01 03:00:24
```

- 重啟裝置以開始升級。

```ros
[admin@MikroTik] >/system/reboot
Reboot, yes? [y/N]: y

```

- 重啟後，您的路由器將是最新版本，您可以在此選單中檢查：

```ros
/system/package/print

```

- 如果路由器未正確升級，請務必檢查 **日誌**

```ros
/log/print without-paging

```

## RouterOS 本地升級 {#routeros-local-upgrade}

您可以透過在一臺擁有所有所需軟體包的裝置上使用 [`/system/package/local-update`](../../cli-reference/system/package/local-update/index.md) 工具，來升級本地網路中的一臺或多臺 MikroTik 路由器。下面是一個包含 3 臺路由器的簡單示例（相同方法適用於具有任意數量路由器的網路）：

- 在主路由器的 Files 選單下放置所需軟體包：

<center>![](/img/33416bc0f10bc51a.webp)</center>

**可選：** 您可以在主裝置之間設定一臺映象裝置。如果不需要，請跳過此步驟：

- 選擇 Local Package Sources 並啟用 Mirror device。設定軟體包所在的 Primary Server（10.155.136.50）。Check Interval 的 **minimum** 設定可設為 00:07:12，裝置將按此時間間隔使用 WinBox 連線到主裝置並檢查軟體包。  
  如果有新的軟體包可用，它將開始下載。當使用許多檔案時，下載過程較慢，可能需要一些時間。如果出現某些失敗，下載將在下一次 Check 時繼續。

<center>![](/img/19a7104b3178b5ef.webp)</center>

- 將建立一個新的 `packs` 資料夾，映象裝置將在其中儲存軟體包：

<center>![](/img/f4440913970c962d.webp)</center>

- 在將被更新的裝置上新增新的軟體包源，在本示例中我們使用映象裝置 10.155.136.71：

<center>![](/img/5f508bcb1902b63e.webp)</center>

- 當您在 Local Update packages 標籤頁中選擇 **Refresh** 時，WinBox 中的裝置將連線到源並檢查是否有新的軟體包。

<center>![](/img/b1034914a72f4b14.webp)</center>

- 選擇軟體包並選擇 **Download**。下載完成後，重啟裝置。

<center>![](/img/0f893624b863b331.webp)</center>

- 使用 `/system/package/local-update/refresh` 在指令碼中自動化此操作。可以使用 Fetch 工具從我們的網頁下載軟體包，例如：

```ros
/tool/fetch url=https://download.mikrotik.com/routeros/7.16.1/routeros-7.16.1-arm.npk
```
