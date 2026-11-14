---
title: "CRS305-1G-4S+IN"
slug: /crs305-1g-4s-plus-in
source: https://manual.mikrotik.com/hardware/crs305-1g-4s-plus-in
captured_at: '2026-11-04T09:46:07+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/7ff531321da06c88.jpg)

## [CRS305-1G-4S+IN](https://mikrotik.com/product/crs305_1g_4s_in) {#crs305-1g-4sin}

本裝置是一臺由 RouterOS 驅動的 10 Gigabit SFP+ 交換器。它具有兩路冗餘 DC 輸入。裝置帶有四個 SFP+ 插槽（模組不包含在內），用於高效能 10GbE 連線（也支援 1.25 Gbit 模組），另有 1GbE 銅纜埠用於管理。裝置開箱即可作為交換器使用。完整規格和產品手冊請參見 [CRS305-1G-4S+IN 產品頁面](https://mikrotik.com/product/crs305_1g_4s_in)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準操作規範。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置適合安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 請僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，操作風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員進行安裝。

## 快速開始 {#quickstart}

- 將您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內使用，可放置在平整表面上，或安裝在牆上；安裝在牆上時，請確保線纜入口朝下。對於我們的裝置，我們建議使用 Cat5/6 遮蔽電纜。距離以 mm 為單位。

![](/img/33a15afc2ea65ae1.webp)

## 供電 {#powering}

裝置可透過兩個 DC 電源插孔（冗餘故障轉移）或第一個乙太網埠供電：

- 直接輸入電源插孔 DC1、DC2（外徑 5.5 mm、內徑 2 mm，母頭，中心正極）接受 DC ⎓ 12-57 V 直流電。
- 第一個乙太網埠接受 DC ⎓ 12-57 V 範圍內的無源或 802.3af/at Power over Ethernet 供電。在使用全部 RJ10 銅纜模組的情況下，本裝置在最大負載下配合光纖 SFP 模組的功耗為 10 W，最高可達 18 W。使用 802.3af/at 為本裝置供電時，為獲得最佳相容性，我們建議不要接地。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將一根乙太網電纜從裝置連線到 PoE 介面卡的 **PoE+DATA** **（PoE-out）** 埠。
- 將一根來自本地網路（LAN）的乙太網電纜連線到 PoE 介面卡的 **DATA** 埠。
- 將電源線連線到介面卡，然後插入電源插座。

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件可在 [https://mt.lv/help](https://mt.lv/help) 獲取。裝置可使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方式以確保可訪問性。**

在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。

裝置配備一個 RS-232 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。為便於恢復，可以從網路重新安裝裝置，請參見 Reset 按鈕。

Marvell Prestera 交換晶片的功能在 [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) 手冊中有相關說明。

裝置支援啟動 RouterOS（提供完整的路由和交換功能）或 SwOS（僅提供交換功能）。預設情況下，裝置啟動進入 RouterOS，但您可以按如下方式切換到另一個作業系統：

- 從 SwOS：進入 **System** 選單，點選頁面底部的 "**Boot RouterOS**" 按鈕。
- 從 RouterOS：開啟 **System → RouterBOARD → Settings** 並選擇 **Boot OS**。

也可以使用序列埠控制檯選單選擇作業系統並配置其他啟動選項。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 四個 SFP+ 插槽，同時支援 1.25 Gb SFP 和 10 Gb SFP+ 模組。
- 一個千兆乙太網埠，建議用於管理（支援 Auto MDI/X，因此您可以使用直通或交叉電纜連線其他網路裝置）。乙太網埠（ETH/BOOT）也可用於透過 Netinstall 進行網路啟動和恢復。

## Reset 按鈕 {#reset-button}

- 如需重設配置，請斷開裝置電源，按住 Reset 按鈕，當 USER (USR) LED 開始閃爍時鬆開。
- 如需載入備份載入程式，請在通電前按住 Reset 按鈕，三秒後鬆開。
- 如需啟動 Netinstall 過程（以 BOOTP 模式啟動裝置以重新安裝 RouterOS），請按住 Reset 按鈕，給裝置通電，等待 USER (USR) LED 閃爍後變為常亮。當 USR LED 熄滅時，鬆開 Reset 按鈕。

無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>說明</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>CRS305-1G-4S+IN</td></tr><tr><td>**架構**</td><td>ARM 32-bit</td></tr><tr><td>**CPU**</td><td>98DX3236, 2 core, 800 MHz</td></tr><tr><td>**交換晶片型號**</td><td>98DX3236</td></tr><tr><td>**RAM**</td><td>512 MB</td></tr><tr><td>**儲存**</td><td>16 MB, Flash</td></tr><tr><td>**10/100/1000 乙太網埠**</td><td>1</td></tr><tr><td>**SFP+ 埠**</td><td>4（每埠最高 10 Gbit）</td></tr><tr><td>**PoE-in**</td><td>802.3af/at, 12-57 V</td></tr><tr><td>**DC 插孔輸入電壓**</td><td>12-57 V</td></tr><tr><td>**最大功耗**</td><td>18 W</td></tr><tr><td>**不含附加模組時的最大功耗**</td><td>10 W</td></tr><tr><td>**尺寸**</td><td>141 × 115 × 28 mm</td></tr><tr><td>**工作溫度**</td><td>-40 °C 至 +70 °C</td></tr><tr><td>**作業系統**</td><td>RouterOS / SwOS（雙啟動）</td></tr><tr><td>**認證**</td><td>CE, EAC, ROHS</td></tr><tr><td>**IP 防護等級**</td><td>IP20</td></tr></tbody></table>

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/crs305_1g_4s_in](https://mikrotik.com/product/crs305_1g_4s_in)

## 配件 {#accessories}

包裝中包含隨裝置提供的以下配件：

![](/img/501df1fa4bf174b9.webp)

受支援的 SFP 模組請參見 [MikroTik wired interface compatibility](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及更高版本。具體的出廠預裝版本列在 /system resource 中。其他作業系統尚未經過測試。
