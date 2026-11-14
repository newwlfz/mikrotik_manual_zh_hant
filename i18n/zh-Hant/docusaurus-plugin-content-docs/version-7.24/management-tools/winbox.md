---
sidebar_key: "management-tools/winbox"
sidebar_position: 2
title: "WinBox"
sidebar_label: "WinBox"
description: "WinBox 是一款用於管理 MikroTik RouterOS 的 GUI 實用程式，可透過 Wine 支援 Linux/macOS，並透過 AES128-CBC-SHA 加密和 ECSRP 身份驗證提供安全連線。它提供簡單和高階兩種模式來連線路由器，並具有鄰居發現功能，可發現附近的裝置，同時避免使用不相容的協定。"
tags:
  - 'winbox'
  - 'management'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/7.24/management-tools/winbox
captured_at: '2026-11-04T11:32:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

:::info
**適用於 Linux 和 macOS 的原生 WinBox 測試版**現已可在 [MikroTik 下載頁面](https://mikrotik.com/download) 獲取！

:::

WinBox 是一個小型實用程式，可使用快速且簡單的 GUI 管理 MikroTik RouterOS。它是原生 Win32/Win64 二進位制檔案，但可以使用 Wine 在 **Linux** 和 **macOS (OSX)** 上執行。所有 WinBox 介面功能都儘可能與控制檯功能保持一致，這就是手冊中沒有 WinBox 章節的原因。某些高階和系統關鍵配置無法透過 WinBox 完成，例如更改介面上的 MAC 地址。

從 WinBox v3.14 開始，使用以下安全功能：

- WinBox.exe 使用由 SIA Mikrotīkls (MikroTik) 頒發的擴充套件驗證證書籤名。
- WinBox 使用 ECSRP 進行金鑰交換和身份驗證（需要新版 WinBox）。
- 雙方都會驗證對方知道密碼（不可能發生中間人攻擊）。
- RoMON 模式下的 WinBox 要求 Agent 為最新版本，才能連線到最新版本的路由器。
- WinBox 使用 AES128-CBC-SHA 作為加密演算法（需要 WinBox 3.14 或更高版本）。

## 啟動 WinBox {#starting-winbox}

WinBox loader 可從 [MikroTik 下載頁面](https://www.mikrotik.com/download) 下載。下載 WinBox.exe 後，雙擊它，就會彈出 WinBox loader 視窗。WinBox loader 有兩種模式：簡單模式（預設啟用）和高階模式。

### 簡單模式 {#simple-mode}

首次開啟 WinBox loader 時，將使用簡單模式佈局：

![](/img/2386fa4e45dcbbe8.webp)

要連線到路由器，請輸入路由器的 IP 或 MAC 地址，指定使用者名稱和密碼（如果有），然後單擊 **Connect** 按鈕。還可以在 IP 地址後輸入埠號，並用冒號分隔，例如 192.168.88.1:9999。埠可以在 RouterOS 的 **services** 選單中更改。

:::warning
建議儘可能使用 IP 地址。MAC 會話使用網路廣播，並非 100% 可靠。

:::

還可以使用鄰居發現來列出可用路由器。使用 **Neighbors** 標籤頁：

![](/img/8458e9e261d09be6.webp)

從發現的路由器列表中，可以單擊 IP 或 MAC 地址列來連線到該路由器。如果單擊 IP 地址，則將使用 IP 進行連線；但如果單擊 MAC Address，則將使用 MAC 地址連線到路由器。

:::info
鄰居發現還會顯示與 WinBox 不相容的裝置，例如 Cisco 路由器或任何其他使用 CDP (Cisco Discovery Protocol) 的裝置。如果嘗試連線到 SwOS 裝置，則連線將透過 Web 瀏覽器建立

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

- **Browse** - 瀏覽某個特定會話的檔案目錄。
- **Keep Password** - 如果未勾選，密碼不會儲存到列表。
- **Secure mode** - 如果勾選，WinBox 將使用 DH-2048 進行金鑰交換，並使用經過修改和加固的 RC4-drop3072 加密來保護會話。
- **Autosave session** - 自動為建立連線的裝置儲存會話。

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

這將連線到路由器 10.5.101.1，使用者為 "admin"，無密碼，並使用 session|workspace "```<own>```"。

可以使用命令列自動傳遞 connect to、user 和 password 引數，以透過 RoMON 連線到路由器。在這種情況下，必須將 RoMON Agent 儲存在受管路由器列表中，這樣 WinBox 才知道此裝置的使用者名稱和密碼：

```
winbox.exe --romon [<romon-agent> [<connect-to> [<login> [<password>]]] <session|workspace>]

```

例如（無密碼）：

```
winbox.exe --romon 10.5.101.1 D4:CA:6D:E1:B5:7D admin "" "<own>"

```

將透過 10.5.101.1 經 RoMON Agent 連線到路由器 D4:CA:6D:E1:B5:7D，使用者為 "admin"，無密碼，並應用名為 "```<own>```" 的 session|workspace。

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

- 頂部的主工具欄，使用者可以在其中新增各種資訊欄位，例如 CPU 和記憶體使用率。
- 左側的選單欄——所有可用選單和子選單的列表。此列表會根據已安裝的軟體包而變化。例如，如果 IPv6 軟體包被停用，則 **IPv6** 選單及其所有子選單將不會顯示。
- 工作區——開啟所有選單視窗的區域。

![](/img/4364a0cd0d4b63d0.webp)

標題欄顯示用於識別 WinBox 會話是與哪個路由器開啟的資訊。資訊按以下格式顯示：

```
[username]@[Router's IP or MAC] ( [RouterID] ) - WinBox [ROS version] on [RB model] ([platform])

```

從上方截圖可以看到，使用者 **krisjanis** 已登入到 IPv4/IPv6 地址為 **[fe80::4e5e:cff:fef6:c0ab%3]** 的路由器。路由器 ID 是 **3C18-Krisjanis\_GW**，當前安裝的 RouterOS 版本是 **v6.36rc6**，RouterBoard 是 **CCR1036-12G-4S**，平臺是 **tile**。

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

子視窗不能被拖出工作區。請注意上方截圖中的 **Interface** 視窗被拖出了可見工作區，並且底部出現了水平捲軸。如果任何視窗超出可見工作區邊界，就會出現垂直和/或水平捲軸。

### 子視窗選單欄 {#child-window-menu-bar}

每個子視窗都有自己的工具欄。大多數視窗具有相同的工具欄按鈕集：

- ![](/img/883766965d361780.webp) **Add** - 向列表新增新專案。
- ![](/img/93d58ae7b5d3ef41.webp) **Remove** - 從列表中刪除所選專案。
- ![](/img/75ed54893c8f6bc2.png) **Enable** - 啟用所選專案（與 console 中的 **enable** 命令相同）。
- ![](/img/d7e0e7b8749d2475.png) **Disable** - 停用所選專案（與 console 中的 **disable** 命令相同）。
- ![](/img/d5c7e3b62122a731.png) **Comment** - 新增或編輯註釋。
- ![](/img/53e2f89ba914e7ef.png)  **Sort** - 允許你根據各種引數篩選專案。 [篩選顯示的專案](#sorting-out-displayed-items)

幾乎所有視窗的工具欄右側都有一個快速搜尋輸入欄位。在此欄位中輸入的任何文字都會在所有專案中搜尋並高亮顯示，如下圖所示。

![](/img/be58bd09dcf01eb9.webp)

請注意，快速查詢輸入欄位右側有一個下拉框。對於當前開啟的 (IP Route) 視窗，此下拉框允許按路由錶快速篩選專案。例如，如果選擇了 **main**，則只會列出主路由表中的路由。
所有防火牆視窗中也有類似的下拉框，可按鏈快速篩選規則。

### 篩選顯示的專案 {#sorting-out-displayed-items}

幾乎每個視窗都有一個 **Sort** 按鈕。單擊此按鈕後，會出現多個選項，如下圖所示。

![](/img/e027e597d0b92801.webp)

該示例展示瞭如何快速篩選出位於 10.0.0.0/8 範圍內的路由：

1. 按 **Sort** 按鈕。
2. 從第一個下拉框中選擇 **Dst.Address**。
3. 從第二個下拉框中選擇 **in**。"in" 表示篩選器將檢查 DST 地址值是否在指定網路的範圍內。
4. 輸入用於比較值的網路（在我們的示例中，輸入 "10.0.0.0/8"）。
5. 這些按鈕用於向堆疊中新增或移除另一個篩選器。
6. 按 **Filter** 按鈕應用篩選器。

從截圖中可以看到，WinBox 僅篩選出位於 10.0.0.0/8 範圍內的路由。

比較運算子（截圖中編號 **3**）可能因視窗而異。例如，"IP Route" 視窗只有兩個：**is** 和 **in**。其他視窗可能具有 "is not"、"contains"、"contains not" 等運算子。

WinBox 允許構建篩選器堆疊。例如，如果需要按目標地址和閘道器篩選，則：

- 按上述示例設定第一個篩選器。
- 按 **[+]** 按鈕在堆疊中新增另一個篩選條。
- 設定第二個篩選器以按閘道器篩選。
- 按 **Filter** 按鈕應用篩選器。

也可以按 **[-]** 按鈕從堆疊中移除不必要的篩選器。

### 自定義顯示的列列表 {#customizing-list-of-displayed-columns}

預設情況下，WinBox 顯示最常用的引數。但是，有時需要檢視其他引數，例如 "BGP AS Path" 或其他 BGP 屬性，以監控路由是否被正確選擇。

WinBox 允許你為每個單獨視窗自定義顯示的列。例如，要新增 BGP AS 路徑列：

- 單擊列標題右側的小箭頭按鈕 (**1**)，或右鍵單擊路由列表。
- 在彈出的選單中轉到 **Show Columns** (**2**)，然後從子選單中選擇所需的列，在我們的例子中單擊 **BGP AS Path** (**3**)。

![](/img/a5ce6d59141eb183.webp)

對窗口布局所做的更改會被儲存，下次開啟 WinBox 時將應用相同的列順序和大小。

#### 詳細模式 {#detail-mode}

還可以啟用 **Detail mode**。在此模式下，所有引數都顯示在列中，第一列是引數名稱，第二列是引數值。

要啟用詳細模式，請右鍵單擊專案列表，然後從彈出選單中選擇 **Detail mode**

![](/img/8cf7d463cef428ca.webp)

#### 分類檢視 {#category-view}

可以按類別列出專案。在此模式下，所有專案將按字母順序或其他類別分組。例如，如果按名稱排序，專案可以按字母順序分類，也可以像下方截圖那樣按型別分類。

要啟用分類檢視，請右鍵單擊專案列表，然後從彈出選單中選擇 **Show Categories**。

![](/img/2d2eb1dc56fd6db0.webp)

### 拖放 {#drag--drop}

可以使用 WinBox 拖放功能向路由器上傳檔案或從路由器下載檔案。還可以右鍵單擊檔案並選擇 "Download" 來下載檔案。

:::info
如果 WinBox 在 Linux 上使用 wine4 執行，則拖放功能可用。兩個 WinBox 視窗之間的拖放可能會失敗。

:::

### 流量監控 {#traffic-monitoring}

WinBox 可用作即時監控每個介面、佇列或防火牆規則流量的工具。下方截圖顯示了乙太網流量監控圖。

![](/img/48c48d00be75a9d1.webp)

### 專案複製 {#item-copy}

這展示了在 WinBox 中複製專案有多麼容易。在此示例中，我們將使用 COPY 按鈕將 Dynamic PPPoE 伺服器介面變為 Static 介面。

此圖顯示了初始狀態。如你所見，DR 表示 "D"，即 Dynamic：

![](/img/19ac0a67df718be8.webp)

雙擊介面並單擊 COPY：

![](/img/79bc5f683b6c8c5e.webp)

將出現新的介面視窗，並自動建立新名稱（在此例中為 pppoe-in1）。

![](/img/28de9385ebb17cb8.webp)

在此 Down/Up 事件之後，此介面將變為 Static：

![](/img/2ae520a470539e86.webp)

## 傳輸設定 {#transferring-settings}

- 受管路由器傳輸——在 File 選單中，使用 Save As 和 Open 功能將受管路由器列表儲存到檔案，並在新工作站上再次開啟它。

- 路由器會話傳輸——在 Tools 選單中，使用 Export 和 Import 功能將現有會話儲存到檔案，並在新工作站上再次匯入它們。

## WinBox v3 鍵盤快速鍵 {#winbox-v3-keyboard-shortcuts}

| 快速鍵 | 描述 |
| :-- | :-- |
| **Ctrl** + **F** | 查詢 |
| **Ctrl** + **G** | 查詢下一個 |
| <kbd>F3</kbd> | 查詢 / 查詢下一個 |
| **Ctrl** + **M** | 新增或編輯註釋 |
| **Ctrl** + **E**  or **Num+** | 啟用所選設定 |
| **Ctrl**+ **D** or **Num-** | 停用所選設定 |
| **Ctrl** + **+** | 放大 WinBox |
| **Ctrl**+ **-** | 縮小 WinBox |
| <kbd>Tab</kbd> | 選擇下一個控制元件 |
| <kbd>Tab</kbd>+<kbd>Shift</kbd> | 選擇上一個控制元件 |
| <kbd>Space</kbd> | 選擇聚焦的控制元件 |
| <kbd>F4</kbd> or **Esc** | 關閉視窗 |
| <kbd>F6</kbd> | 聚焦上一個視窗 |
| <kbd>F6</kbd>+<kbd>Shift</kbd> | 聚焦下一個視窗 |
| <kbd>Insert</kbd> | 向列表新增新條目 |
| <kbd>Delete</kbd> | 從列表中刪除條目 |

## WinBox v4 鍵盤快速鍵 {#winbox-v4-keyboard-shortcuts}

| 快速鍵 | 描述 |
| :-- | :-- |
| **Ctrl** + **E** | 啟用所選設定 |
| **Ctrl** + **Shift** + **E** | 停用所選設定 |
| **Ctrl/CMD** + **+** | 放大 WinBox |
| **Ctrl/CMD** + **-** | 縮小 WinBox |
| **Ctrl/CMD**+ **0** | 重設縮放 |
| **Ctrl** + **Tab** | 選擇下一個標籤頁 |
| **Ctrl** + **Shift** + **Tab** | 選擇上一個標籤頁 |
| **Tab** | 選擇下一個控制元件 |
| **Shift** + **Tab** | 選擇上一個控制元件 |
| **Space** | 選擇聚焦的控制元件 |
| **Ctrl + F4**or **Alt**/**Cmd + W** | 關閉視窗 |
| **Alt** + **A**/ **Cmd** + **Shift** + **S** | 聚焦上一個視窗 |
| **Alt**/**Cmd** + **S** | 聚焦下一個視窗 |
| **Delete** | 從列表中刪除條目 |
| **Alt**/**Cmd**+ **Opt** + **F** | 全域性選單搜尋 |
| **Alt**/**Cmd** + **T** | 開啟新的 Terminal 視窗 |

## 故障排除 {#troubleshooting}

##### WinBox 無法連線到路由器的 IP 地址，裝置未顯示在 Neighbors 列表中 {#winbox-cannot-connect-to-the-routers-ip-address-devices-do-not-show-up-in-the-neighbors-list}

確保 Windows 防火牆設定為允許 WinBox 連線透過 Windows 防火牆中的專用和/或公用網路介面。可以在 *Control Panel\System and Security\Windows Defender Firewall\Allowed applications* 中更改。或者停用 Windows 防火牆。

##### 連線到路由器的 MAC 地址時收到錯誤 “(port 20561) timed out” {#i-get-an-error-port-20561-timed-out-when-connecting-to-routers-mac-address}

如果檔案和印表機共享被停用，Windows (7/8) 不允許 MAC 連線。

##### 我在 WinBox IPv4 Neighbors 列表中找不到我的裝置，或 MAC 連線失敗並顯示 "ERROR could not connect to XX-XX-XX-XX-XX-XX" {#i-cant-find-my-device-in-winbox-ipv4-neighbors-list-or-mac-connection-fails-with-error-could-not-connect-to-xx-xx-xx-xx-xx-xx}

大多數網路驅動程式不會啟用 IP 協定棧，除非你的主機裝置具有 IP 配置。請在主機裝置上設定 IPv4 配置。

*有時裝置會因快取而被發現，但 MAC 連線仍會失敗並顯示 "ERROR: could not connect to XX:XX:XX:XX:XX:XX"。*

:::warning
WinBox MAC-ADDRESS 連線要求 MTU 值設定為 1500，且不分片。其他值可能導致效能不佳——可能會發生連線丟失。

:::
