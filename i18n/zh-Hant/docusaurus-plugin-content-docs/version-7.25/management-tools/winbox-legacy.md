---
sidebar_key: "management-tools/winbox-legacy"
sidebar_position: 3
title: "WinBox v3（舊版）"
sidebar_label: "WinBox v3"
description: "WinBox v3 是一個用於管理 MikroTik RouterOS 的 GUI 工具，可透過 Wine 支援 Linux/macOS。本舊版頁面介紹基於 Wine 的 WinBox v3——如需原生跨平臺體驗，請使用 WinBox v4。"
tags:
  - 'winbox'
  - 'legacy'
  - 'v3'
  - 'management'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/7.25/management-tools/winbox-legacy
captured_at: '2026-11-04T11:20:34+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::warning
本頁面介紹的是舊版 WinBox v3（基於 Wine）應用程式。MikroTik 現在提供 **WinBox v4**，這是一款適用於 Windows、Linux 和 macOS 的原生跨平臺應用程式。當前版本請參閱 [WinBox v4 文件](./winbox.md)。
:::

WinBox 是一個小型實用程式，可透過快速簡單的 GUI 管理 MikroTik RouterOS。它是原生 Win32/Win64 二進位制檔案，但也可以透過 Wine 在 **Linux** 和 **macOS (OSX)** 上執行。所有 WinBox 介面功能都儘可能與控制檯功能保持一致，因此手冊中沒有 WinBox 章節。某些高階且對系統至關重要的配置無法透過 WinBox 完成，例如更改介面的 MAC 地址。

從 WinBox v3.14 開始，使用以下安全功能：

- WinBox.exe 已使用由 SIA Mikrotīkls (MikroTik) 頒發的擴充套件驗證證書籤名。
- WinBox 使用 ECSRP 進行金鑰交換和身份驗證（需要較新的 WinBox 版本）。
- 雙方都會驗證對方知道密碼（無法進行中間人攻擊）。
- 在 RoMON 模式下，WinBox 要求代理為最新版本，才能連線到最新版本的路由器。
- WinBox 使用 AES128-CBC-SHA 作為加密演算法（需要 WinBox v3.14 及更高版本）。

## 啟動 WinBox {#starting-winbox}

WinBox 載入器可從 [MikroTik 下載頁面](https://www.mikrotik.com/download) 下載。下載 WinBox.exe 後，雙擊它，WinBox 載入器視窗就會彈出。WinBox 載入器有兩種模式：預設啟用的簡單模式，以及高階模式。

### 簡單模式 {#simple-mode}

首次開啟 WinBox 載入器時，會使用簡單模式佈局：

![](/img/2386fa4e45dcbbe8.webp)

要連線到路由器，請輸入路由器的 IP 或 MAC 地址，指定使用者名稱和密碼（如果有），然後選擇 **連線** 按鈕。也可以在 IP 地址後輸入埠號，並用冒號分隔，例如 192.168.88.1:9999。埠可在 RouterOS 的 **services** 選單中更改。

:::warning
建議儘可能使用 IP 地址。MAC 會話使用網路廣播，並非 100% 可靠。

:::

還可以使用鄰居發現來列出可用路由器。使用 **Neighbors** 標籤頁：

![](/img/8458e9e261d09be6.webp)

從發現的路由器列表中，你可以選擇 IP 或 MAC 地址列來連線到該路由器。如果選擇 IP 地址，則使用 IP 進行連線；但如果選擇 MAC 地址，則使用 MAC 地址連線到路由器。

:::info
鄰居發現還會顯示與 WinBox 不相容的裝置，例如 Cisco 路由器或任何其他使用 CDP（Cisco Discovery Protocol）的裝置。如果您嘗試連線到 SwOS 裝置，則連線將透過 Web 瀏覽器建立
:::

#### 按鈕/複選框及其他欄位 {#buttonscheck-boxes-and-other-fields}

- **Connect** - 連線到路由器。
- **Connect To RoMON** - 連線到 [RoMON](./romon.md) Agent。
- **Add/set** - 在 **Managed** 標籤頁中儲存/編輯任何已儲存的路由器條目。
- **Open In New Window** - 讓 loader 在後臺保持開啟，併為每個已連線的裝置開啟新視窗。
- **Connect To:** - 路由器的目標 IP 或 MAC 地址。
- **Login** - 用於身份驗證的使用者名稱。
- **Password** - 用於身份驗證的密碼。
- **Keep Password** - 如果未勾選，密碼不會儲存到列表。

#### 選單項 {#menu-items}

- **File**
  - **New** - 在指定位置建立新的受管路由器列表
  - **Open** - 開啟受管路由器列表檔案
  - **Save As** - 將當前受管路由器列表儲存到檔案
  - **Exit** - 退出 WinBox loader

- **Tools**
  - **Advanced Mode** - 啟用/停用高階模式檢視
  - **Import** - 匯入已儲存的會話檔案
  - **Export** - 匯出已儲存的會話檔案
  - **Move Session Folder** - 更改儲存會話檔案的路徑
  - **Clear cache** - 清除 WinBox 快取
  - **Check For Updates** - 檢查 WinBox loader 的更新

### 高階模式 {#advanced-mode}

透過 *Tools → Advanced Mode* 啟用**高階模式**後，會顯示額外的 WinBox loader 引數：

![](/img/65025ace540ede2e.webp)

#### 按鈕/複選框及其他欄位 {#buttonscheck-boxes-and-other-fields-1}

按鈕/複選框

- **瀏覽** - 瀏覽檔案目錄以查詢特定會話。
- **保留密碼** - 如果未勾選，則不會將密碼儲存到列表。
- **安全模式** - 如果勾選，WinBox 使用 DH-2048 進行金鑰交換，並使用修改並加固的 RC4-drop3072 加密來保護會話。
- **自動儲存會話** - 自動為已連線的裝置儲存會話。

欄位：

- **Session** - 已儲存的路由器會話。
- **Note** - 分配給已儲存路由器條目的備註。
- **Group** - 已儲存路由器條目所屬的組。
- **RoMON Agent** - 從可用裝置列表中選擇 RoMON Agent。

:::danger
受管路由器列表是加密的，但**如果**沒有為其設定主密碼，它仍然可以被另一個 WinBox 載入！

:::

### 命令列 {#command-line}

可以使用命令列自動傳遞 connect to、user、password 和 session（WinBox 4 中為 "workspace"）引數：

```
winbox.exe [<connect-to> [<login> [<password>]] <session|workspace>]

```

例如（無密碼）：

```
winbox.exe 10.5.101.1 admin "" "<own>"

```

這會以使用者 "admin"、無密碼連線到路由器 10.5.101.1，並使用 session|workspace "```<own>```"。

可以使用命令列自動傳遞 connect to、user 和 password 引數，以透過 RoMON 連線到路由器。在這種情況下，必須將 RoMON 代理儲存在受管路由器列表中，以便 WinBox 知道此裝置的使用者名稱和密碼：

```
winbox.exe --romon [<romon-agent> [<connect-to> [<login> [<password>]]] <session|workspace>]

```

例如（無密碼）：

```
winbox.exe --romon 10.5.101.1 D4:CA:6D:E1:B5:7D admin "" "<own>"

```

透過 10.5.101.1 使用 RoMON 代理，以使用者 "admin"、無密碼連線到路由器 D4:CA:6D:E1:B5:7D，並應用名為 "```<own>```" 的 session|workspace。

### IPv6 連線 {#ipv6-connectivity}

WinBox 支援 IPv6 連線。要連線到路由器的 IPv6 地址，必須將其放在方括號中，與在 Web 瀏覽器中連線到 IPv6 伺服器時相同。示例：

[db8::1]

連線到鏈路本地地址時，必須在 % 後輸入介面索引：

[0:a00:27ff:fe70::e88c%2]

當需要將 WinBox 連線到非預設埠時，埠號設定在方括號之後：

WinBox 鄰居發現能夠發現啟用 IPv6 的路由器。每個啟用 IPv6 的路由器有兩個條目，一個條目使用 IPv4 地址，另一個使用 IPv6 鏈路本地地址。你可以輕鬆選擇要連線到哪一個。

### 在 macOS 上執行 WinBox {#run-winbox-on-macos}

從 macOS 10.15 Catalina 開始，Apple 已移除對 32 位應用程式的支援，這意味著不再可能在此作業系統中使用常規 Wine 和常規 WinBox。Wine 已提供適用於 macOS 的 64 位版本，MikroTik 也釋出了特殊的 [WinBox64.exe](https://mt.lv/winbox64) 版本。

要執行 WinBox64，需要執行以下步驟：

1. 從 [Wine macOS builds 頁面](https://github.com/Gcenx/macOS_Wine_builds/releases) 安裝最新版 Wine（wine-devel-7.X-osx64.tar.xz），並確保已從 MikroTik 下載頁面下載 [WinBox64.exe 可執行檔案](https://mt.lv/winbox64)。
2. 使用“開啟方式” > Wine64.app 啟動 WinBox64.exe。

### 在 Linux 上執行 WinBox {#run-winbox-on-linux}

可以透過使用 Wine 模擬軟體在 Linux 上執行 WinBox。請確保已安裝 Microsoft 字型包，否則可能會看到失真。

## 介面概覽 {#interface-overview}

WinBox 介面的設計目標是讓大多數使用者覺得直觀。介面包括：

- 頂部的主工具欄，使用者可在其中新增各種資訊欄位，例如 CPU 和記憶體使用率。
- 左側的選單欄 - 所有可用選單和子選單的列表。此列表會根據已安裝的軟體包而變化。例如，如果 IPv6 軟體包被停用，則不會顯示 **IPv6** 選單及其所有子選單。
- 工作區 - 開啟所有選單視窗的區域。

![](/img/4364a0cd0d4b63d0.webp)

標題欄顯示用於識別 WinBox 會話是與哪個路由器開啟的資訊。資訊按以下格式顯示：

```
[username]@[Router's IP or MAC] ( [RouterID] ) - WinBox [ROS version] on [RB model] ([platform])

```

從截圖中可以看到，使用者 **krisjanis** 已登入到 IPv4/IPv6 地址為 **[fe80::4e5e:cff:fef6:c0ab%3]** 的路由器。路由器 ID 為 **3C18-Krisjanis\_GW**，當前安裝的 RouterOS 版本為 **v6.36rc6**，RouterBoard 為 **CCR1036-12G-4S**，平臺為 **tile**。

主工具欄左側有：

- **Undo**
- **Redo**
- **Safe Mode**
- 當前載入的會話

有關安全模式和撤銷已執行操作的更多資訊，請閱讀[本文](../getting-started/configuration-management/index.md)。

右側有：

- 一個指示器，顯示 WinBox 會話是否使用加密。
- 以綠色條顯示的 WinBox 流量指示器。
- 自定義資訊欄位，使用者可以透過右鍵單擊工具欄並從列表中選擇可用資訊欄位來新增。

## 工作區與子視窗 {#work-area-and-child-windows}

WinBox 具有 MDI 介面，這意味著所有選單配置（子）視窗都附加到主（父）WinBox 視窗，並顯示在工作區中。

![](/img/f29744586ba9cec8.webp)

子視窗不能被拖出工作區。在截圖中，**介面** 視窗被拖出可見工作區，底部出現了水平捲軸。如果任何視窗位於可見工作區邊界之外，則會出現垂直和/或水平捲軸。

### 子視窗選單欄 {#child-window-menu-bar}

每個子視窗都有自己的工具欄。大多數視窗具有相同的工具欄按鈕集：

- ![](/img/883766965d361780.webp) **Add** - 向列表新增新專案。
- ![](/img/93d58ae7b5d3ef41.webp) **Remove** - 從列表中刪除所選專案。
- ![](/img/75ed54893c8f6bc2.png) **Enable** - 啟用所選專案（與 console 中的 **enable** 命令相同）。
- ![](/img/d7e0e7b8749d2475.png) **Disable** - 停用所選專案（與 console 中的 **disable** 命令相同）。
- ![](/img/d5c7e3b62122a731.png) **Comment** - 新增或編輯註釋。
- ![](/img/53e2f89ba914e7ef.png)  **Sort** - 允許你根據各種引數篩選專案。 [篩選顯示的專案](#sorting-out-displayed-items)

幾乎所有視窗的工具欄右側都有一個快速搜尋輸入欄位。在此欄位中輸入的任何文字都會在所有專案中搜尋並高亮顯示，如下面的截圖所示。

![](/img/be58bd09dcf01eb9.webp)

請注意，在快速查詢輸入欄位右側有一個下拉框。對於當前開啟的 (IP 路由) 視窗，此下拉框允許按路由錶快速篩選專案。例如，如果選擇了 **main**，則只列出主路由表中的路由。
所有防火牆視窗中也有類似的下拉框，用於按鏈快速篩選規則。

### 篩選顯示的專案 {#sorting-out-displayed-items}

幾乎每個視窗都有一個 **排序** 按鈕。選擇此按鈕時，會出現多個選項，如下面的截圖所示。

![](/img/e027e597d0b92801.webp)

該示例展示瞭如何快速篩選出位於 10.0.0.0/8 範圍內的路由：

1. 按 **排序** 按鈕。
2. 從第一個下拉框中選擇 **Dst.Address**。
3. 從第二個下拉框中選擇 **in**。 "in" 表示篩選器檢查目標地址值是否在指定網路的範圍內。
4. 輸入用於比較值的網路（在我們的示例中輸入 "10.0.0.0/8"）。
5. 這些按鈕用於向篩選器堆疊中新增或移除另一個篩選器。
6. 按 **篩選** 按鈕應用篩選器。

從截圖中可以看到，WinBox 僅篩選出位於 10.0.0.0/8 範圍內的路由。

比較運算子（截圖中編號 **3**）可能因視窗而異。例如，"IP Route" 視窗只有兩個：**is** 和 **in**。其他視窗可能具有 "is not"、"contains"、"contains not" 等運算子。

WinBox 允許構建篩選器堆疊。例如，如果需要按目標地址和閘道器篩選，則：

- 按上一示例所述設定第一個篩選器。
- 按 **[+]** 按鈕在堆疊中新增另一個篩選器欄。
- 設定第二個篩選器以按閘道器篩選。
- 按 **篩選** 按鈕應用篩選器。

也可以按 **[-]** 按鈕從堆疊中移除不必要的篩選器。

### 自定義顯示的列列表 {#customizing-list-of-displayed-columns}

預設情況下，WinBox 顯示最常用的引數。但是，有時需要檢視其他引數，例如 "BGP AS Path" 或其他 BGP 屬性，以監控路由是否被正確選擇。

WinBox 允許你為每個單獨視窗自定義顯示的列。例如，要新增 BGP AS 路徑列：

- 選擇列標題右側的小箭頭按鈕（**1**），或右鍵單擊路由列表。
- 從彈出選單轉到 **顯示列**（**2**），然後從子選單中選擇所需的列，在我們的例子中選擇 **BGP AS Path**（**3**）。

![](/img/a5ce6d59141eb183.webp)

對窗口布局所做的更改會被儲存，下次開啟 WinBox 時將應用相同的列順序和大小。

#### 詳細模式 {#detail-mode}

還可以啟用 **Detail mode**。在此模式下，所有引數都顯示在列中，第一列是引數名稱，第二列是引數值。

要啟用詳細模式，請右鍵單擊專案列表，然後從彈出選單中選擇 **詳細模式**

![](/img/8cf7d463cef428ca.webp)

#### 分類檢視 {#category-view}

可以按分類列出專案。在此模式下，所有專案按字母順序或其他分類分組。例如，如果按名稱排序，專案可以按字母順序分類；專案也可以像下面的截圖那樣按型別分類。

要啟用分類檢視，請右鍵單擊專案列表，然後從彈出選單中選擇 **顯示分類**。

![](/img/2d2eb1dc56fd6db0.webp)

### 拖放 {#drag--drop}

可以使用 WinBox 拖放功能向路由器上傳檔案或從路由器下載檔案。還可以右鍵單擊檔案並選擇 "Download" 來下載檔案。

:::info
如果 WinBox 在 Linux 上使用 wine4 執行，則拖放功能可用。兩個 WinBox 視窗之間的拖放可能會失敗。

:::

### 流量監控 {#traffic-monitoring}

WinBox 可用作即時監控每個介面、佇列或防火牆規則流量的工具。以下截圖顯示了乙太網流量監控圖。

![](/img/48c48d00be75a9d1.webp)

### 專案複製 {#item-copy}

這展示了在 WinBox 中複製專案是多麼容易。在此示例中，使用複製按鈕將動態 PPPoE 伺服器介面變為靜態介面。

此圖顯示了初始狀態。如你所見，DR 表示 "D"，即 Dynamic：

![](/img/19ac0a67df718be8.webp)

雙擊介面並選擇複製：

![](/img/79bc5f683b6c8c5e.webp)

會出現新的介面視窗，並自動建立新名稱（在本例中為 pppoe-in1）。

![](/img/28de9385ebb17cb8.webp)

在此 Down/Up 事件之後，此介面變為靜態：

![](/img/2ae520a470539e86.webp)

## 傳輸設定 {#transferring-settings}

- 受管路由器傳輸——在 File 選單中，使用 Save As 和 Open 功能將受管路由器列表儲存到檔案，並在新工作站上再次開啟它。

- 路由器會話傳輸——在 Tools 選單中，使用 Export 和 Import 功能將現有會話儲存到檔案，並在新工作站上再次匯入它們。

## WinBox v3 鍵盤快速鍵 {#winbox-v3-keyboard-shortcuts}

| 快速鍵 | 描述 |
| :-- | :-- |
| <kbd>Control</kbd>+<kbd>F</kbd> | 查詢 |
| <kbd>Control</kbd>+<kbd>G</kbd> | 查詢下一個 |
| <kbd>F3</kbd> | 查詢 / 查詢下一個 |
| <kbd>Control</kbd>+<kbd>M</kbd> | 新增或編輯註釋 |
| <kbd>Control</kbd>+<kbd>E</kbd> or <kbd>Num+</kbd> | 啟用所選設定 |
| <kbd>Control</kbd>+<kbd>D</kbd> or <kbd>Num-</kbd> | 停用所選設定 |
| <kbd>Control</kbd>+<kbd>+</kbd> | 放大 WinBox |
| <kbd>Control</kbd>+<kbd>-</kbd> | 縮小 WinBox |
| <kbd>Tab</kbd> | 選擇下一個控制元件 |
| <kbd>Tab</kbd>+<kbd>Shift</kbd> | 選擇上一個控制元件 |
| <kbd>Space</kbd> | 選擇聚焦的控制元件 |
| <kbd>F4</kbd> or <kbd>Esc</kbd> | 關閉視窗 |
| <kbd>F6</kbd> | 聚焦上一個視窗 |
| <kbd>F6</kbd>+<kbd>Shift</kbd> | 聚焦下一個視窗 |
| <kbd>Insert</kbd> | 向列表中新增新條目 |
| <kbd>Delete</kbd> | 從列表中刪除條目 |

## WinBox v4 鍵盤快速鍵 {#winbox-v4-keyboard-shortcuts}

| 快速鍵 | 描述 |
| :-- | :-- |
| <kbd>Control</kbd>+<kbd>E</kbd> | 啟用所選設定 |
| <kbd>Control</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd> | 停用所選設定 |
| <kbd>Control/CMD</kbd>+<kbd>+</kbd> | 放大 WinBox |
| <kbd>Control/CMD</kbd>+<kbd>-</kbd> | 縮小 WinBox |
| <kbd>Control/CMD</kbd>+<kbd>0</kbd> | 重設縮放 |
| <kbd>Control</kbd>+<kbd>Tab</kbd> | 選擇下一個標籤頁 |
| <kbd>Control</kbd>+<kbd>Shift</kbd>+<kbd>Tab</kbd> | 選擇上一個標籤頁 |
| <kbd>Tab</kbd> | 選擇下一個控制元件 |
| <kbd>Shift</kbd>+<kbd>Tab</kbd> | 選擇上一個控制元件 |
| <kbd>Space</kbd> | 選擇聚焦的控制元件 |
| <kbd>Control</kbd>+<kbd>F4</kbd> or <kbd>Alt</kbd>/<kbd>Cmd</kbd>+<kbd>W</kbd> | 關閉視窗 |
| <kbd>Alt</kbd>+<kbd>A</kbd> / <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd> | 聚焦上一個視窗 |
| <kbd>Alt</kbd>/<kbd>Cmd</kbd>+<kbd>S</kbd> | 聚焦下一個視窗 |
| <kbd>Delete</kbd> | 從列表中刪除條目 |
| <kbd>Alt</kbd>/<kbd>Cmd</kbd>+<kbd>Opt</kbd>+<kbd>F</kbd> | 全域性選單搜尋 |
| <kbd>Alt</kbd>/<kbd>Cmd</kbd>+<kbd>T</kbd> | 開啟新的終端視窗 |

## 故障排除 {#troubleshooting}

### WinBox 無法連線到路由器的 IP 地址，裝置未出現在鄰居列表中 {#winbox-cannot-connect-to-the-routers-ip-address-devices-do-not-show-up-in-the-neighbors-list}

確保 Windows 防火牆設定為允許 WinBox 連線透過 Windows 防火牆中的專用和/或公用網路介面。可以在 *Control Panel\System and Security\Windows Defender Firewall\Allowed applications* 中更改。或者停用 Windows 防火牆。

### 連線到路由器的 MAC 地址時，我收到錯誤“(port 20561) timed out” {#i-get-an-error-port-20561-timed-out-when-connecting-to-the-routers-mac-address}

如果檔案和印表機共享被停用，Windows (7/8) 不允許 MAC 連線。

### 我無法在 WinBox IPv4 鄰居列表中找到我的裝置，或者 MAC 連線失敗並顯示“ERROR could not connect to XX-XX-XX-XX-XX-XX” {#i-cant-find-my-device-in-winbox-ipv4-neighbors-list-or-mac-connection-fails-with-error-could-not-connect-to-xx-xx-xx-xx-xx-xx}

大多數網路驅動程式只有在主機裝置具有 IP 配置時才會啟用 IP 協定棧。請在主機裝置上設定 IPv4 配置。

*有時裝置會因為快取而被發現，但 MAC 連線仍然失敗並顯示“ERROR: could not connect to XX:XX:XX:XX:XX:XX”。*

:::warning
WinBox MAC-ADDRESS 連線要求 MTU 值設定為 1500，且不分片。其他值可能導致效能不佳——可能會發生連線丟失。

:::
