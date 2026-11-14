---
sidebar_key: "management-tools/winbox"
sidebar_position: 2
title: "WinBox"
sidebar_label: "WinBox"
description: "WinBox v4 是一款原生跨平臺 GUI 工具，用於在 Windows、Linux 和 macOS 上管理 MikroTik RouterOS。它以原生應用取代了基於 Wine 的舊版 WinBox v3，透過 AES128-CBC-SHA 加密和 ECSRP 認證提供安全連線。"
tags:
  - 'winbox'
  - 'management'
  - 'v4'
  - 'native'
source: https://manual.mikrotik.com/docs/management-tools/winbox
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

WinBox 是一款實用工具，可透過快速、簡單的 GUI 管理 MikroTik RouterOS。WinBox v4 是原生應用程式，可用於 Windows、Linux 和 macOS——無需 Wine 或模擬器。所有 WinBox 介面功能都儘可能貼近控制檯功能，因此手冊中沒有單獨的 WinBox 章節。

WinBox 透過 TCP 埠 8291 連線到路由器的 `winbox` 服務。要將 WinBox 遷移到其他埠，請更改該服務的埠，然後在連線時將埠新增到地址中，例如 `192.168.88.1:9999`：

```ros
/ip/service/set winbox port=9999
```

要限制可連線的地址，請參閱 [服務](../system-information-and-utilities/services.md#limit-who-can-use-a-service)。

使用以下安全功能：

- WinBox 使用由 SIA Mikrotīkls (MikroTik) 頒發的擴充套件驗證證書進行簽名。
- WinBox 使用 ECSRP 進行金鑰交換和身份驗證。
- 雙方都會驗證對方知道密碼（不可能發生中間人攻擊）。
- WinBox 使用 AES128-CBC-SHA 作為加密演算法。

:::info
WinBox v4 取代了基於 Windows 的舊版 WinBox v3。如果您仍在使用舊版本，請參閱 [WinBox v3（舊版）](./winbox-legacy.md) 頁面。
:::

## 下載和安裝 {#download-and-installation}

從 [MikroTik 下載頁面](https://mikrotik.com/download/winbox) 下載 WinBox。

#### Windows {#windows}

1. 下載包含 `WinBox.exe` 的 ZIP 壓縮包。
2. 將壓縮包解壓到你選擇的資料夾。
3. 執行 `WinBox.exe`——無需安裝。

#### Linux {#linux}

1. 下載包含 Linux 二進位制檔案的 ZIP 壓縮包。
2. 將壓縮包解壓到你選擇的資料夾。
3. 從終端或檔案管理器執行該二進位制檔案。

#### macOS {#macos}

1. 下載 DMG 軟體包。
2. 開啟 `.dmg` 檔案，並將 WinBox 拖到 Applications 資料夾。
3. 從 Applications 資料夾啟動 WinBox。

:::warning
將 ZIP 壓縮包內容解壓到一個僅包含這些檔案的自包含子資料夾中。這是自更新功能正常工作所必需的，並且適用於 Windows 和 Linux 版本的 WinBox。
:::

## 登入介面 {#login-interface}

本節介紹登入介面。這是啟動 WinBox 應用程式後看到的第一個介面。你可以在此使用登入部分手動連線到 RouterOS 裝置，或使用 **Saved** 標籤頁中儲存的憑據。為了更方便地發現在連線到執行 WinBox 的 PC 的 L2 網路中的裝置，可以使用 **Neighbors** 標籤頁。
登入介面（[參見圖 1](#figure-1---login-interface)）可分為兩個部分：

- **登入部分** - 左側的部分，用於連線到 RouterOS。
- **裝置列表部分** - 右側的部分，包含已儲存或已發現的裝置，並可進一步分為三個標籤頁。
  - **Saved** - 使用者儲存的裝置。
  - **Neighbors** - 已發現的裝置。
  - **RoMON** - 透過 RoMON 發現的裝置。

上述部分未涵蓋的元素可在[表 3](#table-3---miscellaneous-elements)中找到。

#### 圖 1 - 登入介面 {#figure-1---login-interface}

![](/img/e5b14400c07856b6.webp)

### 登入部分 {#login-section}

登入部分（[參見圖 2](#figure-2---login-section)）用於輸入裝置憑據並連線到裝置。每個登入部分元素的詳細說明可在[表 1](#table-1---login-section-elements)中找到。

#### 圖 2 - 登入部分 {#figure-2---login-section}

![](/img/bbe8c5cff10d0a59.webp)

#### 表 1 - 登入部分元素 {#table-1---login-section-elements}

| 元素 | 描述 |
| :-- | :-- |
| ![](/img/ba6119c88366e59f.webp) | **Connect to** - 地址欄位。支援的地址格式包括：MAC、IPv4、[IPv6]、域名。（IPv6 必須專門放在方括號中使用）你還可以在 IP 地址後輸入自定義埠，用冒號分隔（例如 `192.168.88.1:9999`）。埠可在 RouterOS 的 [服務](../system-information-and-utilities/services.md) 選單中更改。|
| ![](/img/48b728812eb60cb5.webp) | **Login** - 使用者名稱欄位。 |
| ![](/img/4c715bee1070dff3.webp) | **Password** - 密碼欄位。“Remember password”複選標記可用於在會話之間儲存密碼。|
| ![](/img/12aefa4d5651b1ce.webp) | **Workspace** - 工作區選擇下拉選單。（參見 [Workspaces](#workspaces) 章節）|
| ![](/img/dea95d1cb5b5575b.webp) | **RoMON Agent** - RoMON Agent 選擇下拉選單。允許透過 RoMON“代理”使用 MAC 地址連線到裝置。更多資訊請參見 [RoMON 文件](./romon.md)。 |
| ![](/img/56461866eb1dea40.webp) | <strong>Connect</strong> - 連線按鈕組： <br/> - <strong>Connect</strong> - 發起與路由器的連線 <br/> - <strong>Connect to RoMON</strong> - 發起與 RoMON“代理”的連線。更多資訊請參見 <a href="/zh-Hans/docs/7.25/management-tools/romon">RoMON 文件</a>。 <br/> - <strong>Open in new</strong> - 啟用後，在新視窗中開啟路由器的配置介面。（僅適用於 <strong>Connect</strong> 按鈕，不適用於 <strong>Connect to RoMON</strong> 按鈕） |
| ![](/img/655213734ab64f3e.webp) | <strong>Save to list</strong> - 允許將路由器憑據儲存到 Saved 列表。附加引數： <br/> - <strong>Group</strong> - 該條目所屬的分組，便於對已儲存條目進行排序 <br/> - <strong>Comment</strong> - 允許新增裝置描述或其他有用資訊 <br/> - <strong>with password</strong> - 啟用後，密碼將與其他憑據一同儲存。停用後，每次使用已儲存條目時都必須手動輸入密碼。 |

:::warning
連線裝置時，儘可能使用 IP 地址。MAC 會話使用網路廣播，並非 100% 可靠。
:::

### 裝置列表部分 {#device-list-section}

裝置列表部分用於瀏覽已儲存和已發現裝置的列表。

#### 圖 3 - 已儲存裝置列表 {#figure-3---saved-device-list}

![](/img/a8f52a86752298fa.webp)

將經常訪問的路由器儲存在 **Saved** 標籤頁中。每個條目可包含：

- **Address** - 地址欄位。支援的地址格式有：MAC、IPv4、[IPv6]、域名。（IPv6 應專門放在方括號中使用）你還可以在 IP 地址後輸入自定義埠，埠以冒號分隔（例如 `192.168.88.1:9999`）。埠可在 RouterOS [服務](../system-information-and-utilities/services.md) 選單中更改。
- **User** - 用於身份驗證的使用者名稱。
- **Password** - 用於身份驗證的密碼。（出於安全原因，不在表中顯示）
- **Group** - 條目所屬的組。
- **Comment** - 裝置描述或其他有用資訊。

資料庫路徑（在[圖 3](#figure-3---saved-device-list)的右下角）顯示當前開啟的裝置列表的 .cdb 檔案在你 PC 上的儲存位置。此列表中的所有 **Actions** 都用於該資料庫管理。

此列表可用的 **Actions**：

- **Open** - 從你選擇的已匯出 .cdb 檔案開啟已儲存裝置列表
- **Move** - 將當前 .cdb 檔案移動到你選擇的其他目錄
- **Import** - 用你選擇的已匯出 .cdb 檔案中的已儲存裝置列表覆蓋當前 .cdb 檔案
- **Export** - 從當前 .cdb 檔案匯出已儲存裝置列表，以便與 **Import** 或 **Open** 一起使用
- **Set file password** - 使用密碼加密當前 .cdb 檔案

#### 已儲存裝置列表加密 {#saved-device-list-encryption}

WinBox 提供 **Set file password** 操作，可對當前 `.cdb` 檔案中的所有已儲存密碼進行加密。最近使用的密碼無法加密。為避免儲存該密碼，請保持 **Remember password** 複選框未選中。

如需額外保護，請使用作業系統內建工具（例如 Windows 上的 BitLocker 或 EFS，以及 macOS 上的 FileVault）加密 WinBox 資料夾，並保護其免遭未經授權的訪問。

#### 圖 4 - Neighbors 裝置列表 {#figure-4---neighbors-device-list}

![](/img/f861803256688a4f.webp)

使用 **Neighbors** 標籤頁發現網路中的可用路由器。從列表中選擇一個路由器，然後選擇 **Connect**。單擊 IP 或 MAC 地址列，以選擇要用於連線的地址。

此列表可用的 **Actions**：

- **Refresh** - 重新整理已發現裝置列表

:::info
鄰居發現還會顯示與 WinBox 不相容的裝置，例如使用 CDP（Cisco Discovery Protocol）的 Cisco 路由器。連線到 SwOS 裝置時，會改為開啟 Web 瀏覽器。
:::

#### 圖 5 - RoMON Neighbor 裝置列表 {#figure-5---romon-neighbor-device-list}

![](/img/70c9d9bc33e0ea08.webp)

使用 **RoMON Neighbors** 標籤頁發現可透過 RoMON 覆蓋網路訪問的路由器。從列表中選擇一個路由器，然後選擇 **Connect**，以透過所選代理使用 MAC 地址開啟 RoMON 會話。有關代理選擇，請參閱[表 1](#table-1---login-section-elements)中的 **RoMON Agent** 欄位說明。有關更多資訊，請參閱專門的 [RoMON 文件](./romon.md)。

## 配置介面 {#configuration-interface}

輸入路由器憑據或使用已儲存憑據並透過[**登入介面**](#login-interface)連線後，你將進入配置介面，如[圖 6](#figure-6---configuration-interface)所示。WinBox v4 配置介面包括：

- **工具欄部分** - 位於頂部，包含常規 WinBox 導航按鈕。
- **側邊欄部分** - 位於左側，列出所有可用選單和子選單。該列表會根據已安裝的軟體包而變化（例如，啟用 container 軟體包會新增 Container 和 App 選單）。
- **工作區部分** - 位於中間，是開啟所有內部視窗的區域。
- **資源部分** - 位於底部，包含常規裝置資訊。

#### 圖 6 - 配置介面 {#figure-6---configuration-interface}

![](/img/9487ac4fc8b26c67.webp)

### 工具欄部分 {#toolbar-section}

#### 圖 7 - 工具欄部分 {#figure-7---toolbar-section}

![](/img/a1c460b7b30803b1.webp)

#### 表 2 - 工具欄部分元素 {#table-2---toolbar-section-elements}

| 元素 | 描述 |
| :-- | :-- |
| ![](/img/82d638632d765377.webp) | **Workspace** - 工作區選擇下拉選單。（參見[工作區](#workspaces)部分） |
| ![](/img/c5590c05291411a9.webp) | **Opened windows list** - 當前所有已開啟的 WinBox 內部視窗的列表。此列表可讓你輕鬆選擇所需視窗或關閉不需要的視窗。  **子選單：**  ![](/img/31a6ee2e3745027e.webp) |
| ![](/img/ca4dde25f5a3d02f.webp) | **Menu search** - 允許按名稱搜尋選單。要搜尋生效，你需要輸入 **至少三個符號**。  **子選單：**  ![](/img/e8cfa85a2dbd7ae0.webp) |
| ![](/img/1a16e9dba6871eee.webp) | **Undo** 和 **Redo** - **Undo**（左側按鈕）還原上一次更改，**Redo**（右側按鈕）重新應用該更改。可撤銷的命令最大數量為 100。有關更多資訊，可參閱[**配置管理**文件](../getting-started/configuration-management/index.md#configuration-undo-and-redo)。 |
| ![](/img/7772d6a7b2259bff.webp) | **Safe Mode toggle** - 允許啟用 **Safe Mode**，以防止意外的會話斷開。有關更多資訊，請參閱[**Safe Mode** 文件](./console.md#safe-mode)。 |
| ![](/img/73de7b2a545bddb3.webp) | **Disconnect** - 結束當前會話並返回[**登入介面**](#login-interface)。 |

### 側邊欄部分 {#sidebar-section}

側邊欄（[參見圖 8](#figure-8---sidebar-section)）包含所有可用選單和子選單的列表。該列表會根據已安裝的軟體包而變化。

#### 圖 8 - 側邊欄部分 {#figure-8---sidebar-section}

![](/img/cfba656236b5208e.webp)

### 工作區部分 {#work-area-section}

工作區是 WinBox 視窗的中央部分，所有內部（子）視窗都會在此顯示。

#### 圖 9 - 工作區部分 {#figure-9---work-area-section}

![](/img/0eeeabd5a073c0a3.webp)

### 使用子視窗 {#working-with-child-windows}

WinBox 具有 MDI 介面，這意味著所有選單配置（子）視窗都附加到主（父）WinBox 視窗，並顯示在工作區中。

#### 標籤頁工具欄 {#tab-toolbar}

每個標籤頁都有一個帶有常用操作的工具欄：

- **New** - 向列表新增新條目。
- **Remove** - 從列表中移除所選條目。
- **Enable** - 啟用所選條目。
- **Disable** - 停用所選條目。
- **Comment** - 新增或編輯註釋。
- **Sort** - 對顯示的條目進行排序和篩選。

幾乎所有標籤頁的工具欄右側都有一個快速搜尋欄位。輸入文字會搜尋所有條目並突出顯示匹配項。

#### 排序和篩選 {#sorting-and-filtering}

選擇 **Sort** 按鈕以顯示篩選選項：

1. 從第一個下拉框中選擇一列。
2. 從第二個下拉框中選擇比較運算子（例如 **is**、**in**、**is not**、**contains**）。
3. 輸入要比較的值。
4. 選擇 **Filter** 以應用。

WinBox 支援疊加多個篩選器。選擇 **[+]** 新增另一個篩選器，選擇 **[-]** 移除一個篩選器。

#### 列自定義 {#column-customization}

要自定義顯示的列：

1. 選擇列標題右側的箭頭按鈕，或右鍵單擊條目列表。
2. 轉到 **Show Columns** 並選擇所需的列。

更改會被儲存，並在會話之間保留。

### 資源部分 {#resources-section}

顯示路由器的一般資訊和資源。部分欄位是互動式的——單擊欄位會在配置介面中開啟相關部分。

#### 圖 10 - 資源部分 {#figure-10---resources-section}

![](/img/7d693f711275df43.webp)

從左到右的欄位如下：

- 路由器標識
- 路由器 IP 地址
- 路由器架構
- 路由器型號
- 路由器上安裝的 RouterOS 版本
- 路由器 CPU 利用率（百分比）
- 路由器 RAM 空閒/已用/總計
- 路由器執行時間
- 路由器時鐘

## WinBox 常規設定及其他 {#general-winbox-settings-and-more}

本節介紹 WinBox GUI 設定以及其他段落未涵蓋的雜項元素（[參見表 3](#table-3---miscellaneous-elements)）。

#### 表 3 - 雜項元素 {#table-3---miscellaneous-elements}

| 元素 | 描述 |
| :-- | :-- |
| ![](/img/656345c7a9ef49c4.webp) | **Create new session** - 位於右上角。此按鈕會開啟新的 WinBox 視窗。 |
| ![](/img/07c12793af5f66be.webp) | <strong>Settings/App information</strong> - 位於右上角。開啟包含以下元素的下拉選單： <br/> - <strong>Settings</strong> - <a href="#gui-settings-menu">GUI Settings 選單</a><br/> - <strong>Shortcuts</strong> - 可用快速鍵組合的資訊（<a href="#keyboard-shortcuts">參見 Keyboard Shortcuts</a>） <br/> - <strong>About</strong> - 應用程式資訊，例如版本、實用連結、許可證資訊 <br/> - <strong>Quit</strong> - 關閉 WinBox 應用程式 |
| ![](/img/2c3ee497272e4f8b.webp) | **WinBox update notification** - 位於右上角。**僅在 WinBox 有更新時顯示**，允許無需訪問 [MikroTik 網站](https://mikrotik.com/winbox) 即可下載最新版本的 WinBox。 |
| ![](/img/8ce5670532f5a0cd.webp) | **RouterOS update notification** - 位於右上角。**僅在 RouterOS 有更新時於 [配置介面](#configuration-interface) 中顯示**，允許無需訪問 [package 選單](../getting-started/installation-and-upgrade/packages.md#download-directly-from-the-router) 或手動上傳軟體包即可下載最新版本的 RouterOS。 |

### GUI 設定選單 {#gui-settings-menu}

WinBox v4 提供高階 GUI 自定義選單（[參見圖 11](#figure-11---gui-settings-menu)），允許更改 WinBox 顯示資訊的多個屬性。每項設定的詳細說明可在[表 4](#table-4---gui-settings-elements)中找到。

#### 圖 11 - GUI 設定選單 {#figure-11---gui-settings-menu}

![](/img/e6a73a80d0319a42.webp)

#### 表 4 - GUI 設定元素 {#table-4---gui-settings-elements}

| 元素 | 描述 |
| :-- | :-- |
| ![](/img/0071d3c081c5a292.webp) | **Hide password** - 將 RouterOS 敏感欄位的內容替換為星號。（[敏感引數列表](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)） |
| ![](/img/06422c69914305bc.webp) | **Comment Type** - 選擇註釋是顯示為條目的標題，還是顯示為單獨的列。 |
| ![](/img/e67aafe2f19cae6f.webp) | **Comment column in front** - 當選擇 Comment 列型別時，確保註釋位於所有其他列之前。 |
| ![](/img/73aae9524b6ca127.webp) | **Table tools position** - 選擇特定表格的工具是顯示在內部 WinBox 視窗的右側，還是作為帶有下拉選單的單個按鈕顯示在內部 WinBox 視窗的工具欄中。 |
| ![](/img/075ca22f0c8c32e9.webp) | **Table column separator** - 選擇是否顯示分隔各列的垂直線。|
| ![](/img/210763d1255cb84f.webp) | **Table row height** - 取值 0 到 20，更改行的垂直內邊距，較高的值提供更大的內邊距，從而更好地區分各行。|
| ![](/img/bd0d81c08a1832e3.webp) | **Dark mode** - 為應用程式啟用更深的配色方案。 |
| ![](/img/88c1305c38d4babe.webp) | **Resource panel** - 選擇是否在配置介面的 WinBox 視窗底部顯示路由器資源/身份資訊。|
| ![](/img/391a3e5a7443b343.webp) | <strong>GUI font</strong> - 允許選擇在整個 WinBox 應用程式中使用的字型。附加引數： <br/> - <strong>Regular</strong> - 取值 300 到 600，允許更改整個 WinBox 應用程式中常規文字的粗細 <br/> - <strong>Bold</strong> - 取值 -100 到 300，允許更改整個 WinBox 應用程式中粗體文字的粗細 <br/> - <strong>Spacing</strong> - 取值 -1 到 1，允許更改字元之間的間距。 |
| ![](/img/be14a9269e933e94.webp) | **GUI scaling** - 取值 67% 到 250%，允許更改 UI 的大小。在右下角開啟子選單。  **子選單：**  ![](/img/1b600d643de7ea0e.webp)  - **Global zoom** - 同時更改 **UI size** 和 **Spacing**  - **UI size** - 更改 UI 元素的大小  - **Spacing** - 更改 UI 元素之間的間距 |
| ![](/img/ee1eeeac8942be20.png) | **Buffer size** - 終端回滾緩衝區中保留的最大行數（100 到 100000）。僅對新開啟的終端生效。 |

### 工作區 {#workspaces}

WinBox v4 引入了工作區，取代 WinBox v3 的會話系統。工作區允許你將連線組織到獨立環境中。每個工作區都維護自己的一組開啟的連線和視窗。

## 鍵盤快速鍵 {#keyboard-shortcuts}

本節介紹不同版本的 WinBox 在各自作業系統上的鍵盤快速鍵。

#### Linux/Windows 快速鍵 {#linuxwindows-shortcuts}

| 快速鍵 | 描述 |
| :-- | :-- |
| **應用程式** | |
| Ctrl + + / Ctrl + = / Ctrl + Scroll up | 放大 |
| Ctrl + - / Ctrl + Scroll down | 縮小 |
| Ctrl + 0 | 重設縮放 |
| F11 | 切換全屏 |
| **工作區** | |
| Alt + F | 選單搜尋 |
| Alt + W / Ctrl + F4 / Esc | 關閉活動視窗 |
| Alt + S | 切換活動視窗 |
| Alt + A | 向後切換活動視窗 |
| Alt + T | 開啟新的終端視窗 |
| Ctrl + Tab | 活動視窗中的下一個標籤頁 |
| Ctrl + Shift + Tab | 活動視窗中的上一個標籤頁 |
| **表格** | |
| Ctrl + F | 查詢文字 |
| Ctrl + A | 選擇所有行 |
| Insert / Ctrl + N | 新增新條目 |
| Delete | 移除所選行 |
| Ctrl + E | 啟用所選行 |
| Ctrl + Shift + E | 停用所選行 |
| Ctrl + M | 為所選行添加註釋 |
| Enter | 開啟當前行 |
| F5 | 重新載入 |
| End | 將游標移到末尾 |
| Home | 將游標移到頂部 |
| Page Down | 將游標向下移動一頁 |
| Page Up | 將游標向上移動一頁 |
| Shift + Click | 多列排序 |
| **表單** | |
| Shift + Click | 多標籤頁展開 |

#### macOS 快速鍵 {#macos-shortcuts}

| 快速鍵 | 描述 |
| :-- | :-- |
| **應用程式** | |
| ⌘ + + / ⌘ + = / ⌘ + Scroll up | 放大 |
| ⌘ + - / ⌘ + Scroll down | 縮小 |
| ⌘ + 0 | 重設縮放 |
| F11 | 切換全屏 |
| ⌘ + M | 最小化應用 |
| **工作區** | |
| ⌥ + ⌘ + F | 選單搜尋 |
| ⌘ + W / ⌘ + F4 / Esc | 關閉活動視窗 |
| ⌘ + S | 切換活動視窗 |
| ⌘ + Shift + S | 向後切換活動視窗 |
| ⌘ + T | 開啟新的終端視窗 |
| Ctrl + Tab | 活動視窗中的下一個標籤頁 |
| Ctrl + Shift + Tab | 活動視窗中的上一個標籤頁 |
| **表格** | |
| ⌘ + F | 查詢文字 |
| ⌘ + A | 選擇所有行 |
| Insert / ⌘ + N | 新增新條目 |
| Fn + Backspace | 移除所選行 |
| ⌘ + E | 啟用所選行 |
| ⌘ + Shift + E | 停用所選行 |
| ⌘ + Shift + M | 為所選行添加註釋 |
| Enter | 開啟當前行 |
| F5 | 重新載入 |
| End | 將游標移到末尾 |
| Home | 將游標移到頂部 |
| Page Down | 將游標向下移動一頁 |
| Page Up | 將游標向上移動一頁 |
| Shift + Click | 多列排序 |
| **表單** | |
| Shift + Click | 多標籤頁展開 |

## 故障排除 {#troubleshooting}

##### WinBox 無法連線到路由器的 IP 地址，裝置未顯示在 Neighbors 列表中 {#winbox-cannot-connect-to-the-routers-ip-address-devices-do-not-show-up-in-the-neighbors-list}

確保防火牆已設定為允許 WinBox 連線透過 Private 和/或 Public 網路介面。在 Windows 上，可在 *Control Panel\System and Security\Windows Defender Firewall\Allowed applications* 中配置。

##### MAC 連線失敗，錯誤為“(port 20561) timed out” {#mac-connection-fails-with-error-port-20561-timed-out}

如果停用檔案和印表機共享，Windows 不允許 MAC 連線。

##### MAC 連線失敗，並顯示“ERROR could not connect to XX-XX-XX-XX-XX-XX” {#mac-connection-fails-with-error-could-not-connect-to-xx-xx-xx-xx-xx-xx}

大多數網路驅動程式需要先進行 IP 配置，才能啟用 IP 協定棧。請在主機裝置上設定 IPv4 配置。

:::warning
WinBox MAC 地址連線要求 MTU 值設定為 1500，且不分片。其他值可能導致效能不佳或連線中斷。
:::
