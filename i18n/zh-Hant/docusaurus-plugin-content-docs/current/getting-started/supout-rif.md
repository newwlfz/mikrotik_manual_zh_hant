---
sidebar_key: "getting-started/supout-rif"
sidebar_position: 10
title: "Supout.rif"
sidebar_label: "Supout.rif"
description: "supout.rif 檔案是用於 MikroTik 支援的路由器診斷快照。可透過 CLI、WinBox 或 WebFig 建立它，將其下載並用 Supout.rif viewer 開啟。"
tags:
  - 'supout-rif'
  - 'debugging'
source: https://manual.mikrotik.com/docs/getting-started/supout-rif
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

支援輸出檔案（`supout.rif`）是供 MikroTik 支援使用的路由器診斷快照。它包含路由器的配置、日誌、程式狀態、監控命令（例如介面狀態）的輸出，以及 RouterOS 崩潰時的崩潰資料。請在問題出現時建立該檔案，以便它反映路由器當時的狀態，並透過 [MikroTik 支援](https://mikrotik.com/support) 頁面隨請求一併傳送。

在意外重啟或崩潰後，請立即建立該檔案，然後再升級或再次重啟路由器。如果檔案列表中有 `autosupout.rif` 和 `autosupout.old.rif`，也請一併傳送。

該檔案經過編碼。要檢視其內容，請登入您的 MikroTik 賬戶，並使用左側導航欄中的“Supout.rif viewer”工具上傳並分析該檔案。

## 建立檔案 {#create-the-file}

在 CLI 中，執行 [`/system/sup-output`](../cli-reference/system/sup-output.md)：

```ros
/system/sup-output
```

該命令會寫入 `supout.rif`，並顯示進度，從 `created: 42%` 一直到 `created: 100%`。在配置較大的路由器上，耗時從幾秒到更長時間不等。檔案大小取決於路由器；在家庭路由器上，該檔案通常約為 1 MB。

要使用其他名稱，請設定 `name`。當名稱沒有副檔名時，RouterOS 會新增 `.rif` 副檔名，因此 `name=supout.rif` 也會寫入 `supout.rif`。同名檔案會被替換。路徑會把檔案寫入資料夾，例如寫入 USB 磁碟：

```ros
/system/sup-output name=usb1/supout
```

如果路由器的檔案列表中有 `flash` 資料夾，則重啟時該資料夾之外的檔案會丟失。如果路由器可能在您下載檔案之前重啟，請將檔案寫入 `flash`（`name=flash/supout`）。請參閱 [檔案](../system-information-and-utilities/files.md)。

### 在設定時間建立檔案 {#create-the-file-at-a-set-time}

對於在已知時間發生的問題，例如每天晚上發生的問題，可以讓排程器建立該檔案：

```ros
/system/scheduler/add name=evening-supout start-time=20:00:00 \
    interval=1d on-event="/system/sup-output name=evening-supout"
```

每次執行都會替換前一天的檔案。在獲得所需的那次執行後，請下載 `evening-supout.rif` 並刪除該條目：

```ros
/system/scheduler/remove evening-supout
```

### WinBox {#winbox}

截圖中顯示的是 WinBox 3。在主選單中選擇 **Make Supout.rif**，然後在開啟的視窗中選擇 **Start**。該視窗會顯示檔名，並在 **Created** 中顯示進度。

![WinBox main menu with Make Supout.rif highlighted and the Make it! window with the file name supout.rif, the progress 42% and the Start button](/img/cd25509ae01612e9.webp)

檔案準備好後，會列在 **Files** 中。右鍵單擊該檔案並選擇 **Download**，或者將檔案拖到桌面。在 WinBox 4 中，請從 **Files** 下載（請參閱 [在 WinBox 中管理檔案](../system-information-and-utilities/files.md#manage-files-in-winbox)）。

![WinBox File List with supout.rif selected and Download highlighted in the right-click menu](/img/32c76482e5bb24ff.webp)

### WebFig {#webfig}

截圖中顯示的是較舊版本的 WebFig。在選單中選擇 **Make Supout.rif**。然後開啟 **Files**，並在 `supout.rif` 旁選擇 **Download**。

![WebFig Files page with Make Supout.rif highlighted in the menu and the Download button next to supout.rif](/img/24e5e1b472982cb2.webp)

## 下載檔案 {#download-the-file}

使用 WinBox 或 WebFig 中的 **Files** 下載該檔案（請參閱 [在 WinBox 中管理檔案](../system-information-and-utilities/files.md#manage-files-in-winbox)），或者從您的計算機使用 `scp` 或 SFTP 下載。這些方式需要啟用路由器的 SSH 服務，並允許從您的計算機訪問（請參閱 [服務](../system-information-and-utilities/services.md)）：

```bash
scp admin@192.168.88.1:supout.rif .
```

對於資料夾中的檔案，請給出其路徑：

```bash
scp admin@192.168.88.1:usb1/supout.rif .
```

當路由器的 FTP 服務已啟用時，也可以使用 FTP。

## 崩潰後自動生成 supout {#automatic-supout-after-a-crash}

當 RouterOS 軟體發生故障時，路由器會自行寫入 `autosupout.rif`，並將先前的檔案重新命名為 `autosupout.old.rif`。watchdog 設定 `automatic-supout` 控制此行為，且預設開啟。使用 `auto-send-supout` 時，路由器還會透過電子郵件傳送該檔案；這需要 watchdog 的電子郵件設定。watchdog 重啟不是軟體故障，不會寫入該檔案。請參閱 [看門狗](../diagnostics-monitoring-and-troubleshooting/watchdog.md)。

## 技術細節 {#technical-details}

### 輸出寬度 {#output-width}

如果檢視器顯示的檔案中的命令輸出過窄，請使用更大的 `output-width` 重新建立檔案：

```ros
/system/sup-output name=supout output-width=300
```

### 檔案格式 {#file-format}

該檔案為文字：由一系列經過編碼的段組成，每個段位於一行 `--BEGIN ROUTEROS SUPOUT SECTION` 和一行 `--END ROUTEROS SUPOUT SECTION` 之間。沒有檢視器就無法讀取這些段。

有關引數，請參閱 [`/system/sup-output`](../cli-reference/system/sup-output.md) CLI 參考。
