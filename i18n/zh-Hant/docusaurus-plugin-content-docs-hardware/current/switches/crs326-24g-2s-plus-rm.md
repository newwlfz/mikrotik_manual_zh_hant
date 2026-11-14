---
title: "CRS326-24G-2S+RM"
slug: /crs326-24g-2s-plus-rm
source: https://manual.mikrotik.com/hardware/crs326-24g-2s-plus-rm
captured_at: '2026-11-04T09:46:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/27adf03c426b9867.jpg)

## [CRS326-24G-2S+RM](https://mikrotik.com/product/CRS326-24G-2SplusRM) {#crs326-24g-2srm}

24 個千兆埠交換器，配備 2 個 SFP+ 光籠，採用 1U 機架式外殼，支援雙啟動（RouterOS 或 SwOS）。完整規格和宣傳資料請參見 [CRS326-24G-2S+RM 產品頁面](https://mikrotik.com/product/CRS326-24G-2SplusRM)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置適合安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品適合在室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 只能使用製造商認可的電源和配件，這些均可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，即可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內，可使用隨附的機架安裝件安裝在機架式機箱中，也可以放置在桌面上。如果指定用途為機架式機箱，請使用十字螺絲刀將機架安裝耳片固定到裝置兩側：

- 將機架耳片安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如圖所示。

![](/img/837a6d2bb5f312fe.webp)

- 將裝置放入機架式機箱，並對齊孔位，使裝置能夠方便地裝入。
- 擰緊螺絲將其固定到位。本裝置不具備防水保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 網線。本裝置的安裝和配置應由具備資質的人員完成。

## 供電 {#powering}

本裝置可透過以下方式供電：

- 乙太網埠接受無源 PoE 10-30 V DC ⎓。
- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，正極針式插頭）接受 10-30 V DC⎓。當兩個輸入電源同時供電時，裝置也能正常工作。它將使用電壓最高的電源，如果該電源被移除，則會切換到另一個電源。您可以將其用於電源冗餘。兩個電源都必須處於支援的電壓範圍內。

最大負載下的功耗可達 24 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠；
- 將來自您本地網路（LAN）的乙太網線連線到 PoE 介面卡；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件可在 [https://mt.lv/help](https://mt.lv/help) 獲取。可使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方式以確保可訪問性。**

在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。

本裝置配備一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。出於恢復目的，可以從網路重新安裝裝置，請參見復位按鈕。

Marvell Prestera 交換晶片的功能在 [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) 手冊中進行了說明。

本裝置支援啟動 RouterOS（提供完整路由和交換功能）或 SwOS（僅用於交換執行）。預設情況下，裝置啟動進入 RouterOS，但您可以按如下方式切換到另一個作業系統：

- 從 SwOS 中：轉到 **System** 選單，然後點選頁面底部的 "**Boot RouterOS**" 按鈕。
- 從 RouterOS 中：開啟 **System → RouterBOARD → Settings** 並選擇 **Boot OS**。

也可以使用序列控制檯選單選擇作業系統並配置其他啟動選項。

## 規格 {#specifications}

<table><thead><tr><th>**產品程式碼**</th><th>CRS326-24G-2S+RM</th></tr></thead><tbody><tr><td>**CPU**</td><td>98DX3236, 800 MHz</td></tr><tr><td>**CPU 架構**</td><td>ARM 32bit</td></tr><tr><td>**CPU 核心數**</td><td>2</td></tr><tr><td>**交換晶片型號**</td><td>98DX3236</td></tr><tr><td>**RAM**</td><td>512 MB</td></tr><tr><td>**儲存**</td><td>16 MB Flash</td></tr><tr><td>**1G 乙太網 (RJ45)**</td><td>24</td></tr><tr><td>**10G SFP+ 埠**</td><td>2</td></tr><tr><td>**序列控制檯 (RJ45)**</td><td>1</td></tr><tr><td>**作業系統**</td><td>RouterOS / SwOS（雙啟動）</td></tr><tr><td>**工作溫度**</td><td>-40 °C 至 +60 °C</td></tr><tr><td>**外殼尺寸**</td><td>443 × 144 × 44 mm</td></tr></tbody></table>

有關 MikroTik SFP 模組相容性表，請訪問 wiki 頁面：MikroTik wired interface compatibility

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置復位為預設值。
- 當 LED 變為綠色常亮時鬆開按鈕，可清除所有配置並恢復預設值。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。

無論使用上述哪種選項，如果在裝置接通電源之前按鈕已被按下，系統都將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

連線到 **Netinstall** 時，請使用 Ethernet 1 埠。

![](/img/731f17d53e8dbc53.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。
