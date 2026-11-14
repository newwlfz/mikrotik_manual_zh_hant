---
title: "CRS309-1G-8S+IN"
slug: /crs309-1g-8s-plus-in
source: https://manual.mikrotik.com/hardware/crs309-1g-8s-plus-in
captured_at: '2026-11-04T09:46:07+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/50559d4a3b03e7db.jpg)

## [CRS309-1G-8S+IN](https://mikrotik.com/product/crs309_1g_8s_in) {#crs309-1g-8sin}

本裝置是一臺配有八個 SFP+ 埠和一個千兆埠的網路交換器。它已完成配置，所有埠都已交換連通。完整規格和宣傳資料請參見 [CRS309-1G-8S+IN 產品頁面](https://mikrotik.com/product/crs309_1g_8s_in)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置應安裝在機架中。安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品僅供室內安裝使用。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快速的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 安裝本裝置或將其放置在平坦表面上，參見安裝；
- 選擇你的供電方案，參見供電；
- 將你的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 配置應使用 Web 瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 完成。**提供多種配置方式以確保可訪問性；**
- 在 Web 瀏覽器中開啟 https://192.168.88.1 以開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視標籤上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇你的型號，並在 "Downloads" 部分中找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定你的路由器密碼。

## 安裝 {#mounting}

![](/img/27bf22aa32ecbced.webp)

本裝置設計用於室內，可使用隨附的機架安裝件安裝在機架式機箱中，也可以放置在桌面上。如果希望放置在平坦表面上，請在路由器底部貼上橡膠腳墊；如果指定用於機架式機箱，請使用十字螺絲刀將機架耳固定在裝置兩側。

- 將機架耳固定到裝置兩側，並擰緊四顆螺絲將其固定到位，如右圖所示。
- 將裝置放入機架式機箱並對準孔位，使裝置能夠方便地安裝。
- 擰緊螺絲將其固定到位。本裝置的 IP 防護等級為 IPX0。本裝置不具備防水汙染保護，請確保將裝置放置在乾燥通風的環境中。我們建議為我們的裝置使用遮蔽 Cat5/6 網線。*本裝置的安裝和配置應由具備資質的人員完成。*

## 供電 {#powering}

本裝置可透過直插式電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 12-57 V DC ⎓ 輸入。乙太網埠 1 支援 802.3af/at 和無源 PoE 供電輸入（18-57 V DC）。本裝置在最大負載下的功耗最高為 23 W。可以同時連線兩路電源輸入，它們將以故障切換模式工作（電壓較高的輸入將作為主電源）。使用 802.3af/at 為本裝置供電時，為獲得最佳相容性，我們建議不要使用接地。

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件可在 [https://mt.lv/help](https://mt.lv/help) 獲取。本裝置可使用 Web 瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方式以確保可訪問性。**

在 Web 瀏覽器中開啟 https://192.168.88.1 以開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視標籤上的使用者和無線密碼）。

本裝置配備一個 RS-232 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。出於恢復目的，可以從網路重新安裝裝置，參見復位按鈕。

Marvell Prestera 交換晶片的功能在 [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) 手冊中介紹。

本裝置支援啟動 RouterOS（用於完整的路由和交換功能）或 SwOS（僅用於交換執行）。預設情況下，裝置啟動進入 RouterOS，但你可以按如下方式切換到另一個作業系統：

- 從 SwOS：進入 **System** 選單，點選頁面底部的 "**Boot RouterOS**" 按鈕。
- 從 RouterOS：開啟 **System → RouterBOARD → Settings** 並選擇 **Boot OS**。

也可以使用序列埠控制檯選單選擇作業系統並配置其他啟動選項。

## 復位按鈕 {#reset-button}

- 要重設配置，請斷開裝置電源，按住復位按鈕，並在 USER (USR) LED 開始閃爍時鬆開。
- 要載入備份載入程式，請在接通電源之前按住復位按鈕，然後三秒後鬆開。
- 要啟動 Netinstall 過程（以 BOOTP 模式啟動裝置以重新安裝 RouterOS），請按住復位按鈕，給裝置上電，並等待 USER (USR) LED 閃爍後變為常亮。當 USR LED 熄滅時，鬆開復位按鈕。

無論使用上述哪種方式，只要在給裝置通電之前按下按鈕，系統就會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## LED 指示燈 {#led-indicators}

- 當路由器透過 DC 插孔或 PoE 供電時，電源 LED 點亮。
- 使用者 LED 可從 RouterOS 進行配置。
- 埠 LED 指示各個乙太網和 SFP 埠的活動狀態。

## 規格 {#specifications}

<table><thead><tr><th>**產品程式碼**</th><th>CRS309‑1G‑8S+IN</th></tr></thead><tbody><tr><td>**CPU**</td><td>98DX8208, 800 MHz</td></tr><tr><td>**CPU 架構**</td><td>ARM 32bit</td></tr><tr><td>**CPU 核心數**</td><td>2</td></tr><tr><td>**交換晶片型號**</td><td>98DX8208</td></tr><tr><td>**RAM**</td><td>512 MB</td></tr><tr><td>**儲存**</td><td>16 MB Flash</td></tr><tr><td>**1G 乙太網 (RJ45)**</td><td>1</td></tr><tr><td>**10G SFP+ 埠**</td><td>8</td></tr><tr><td>**作業系統**</td><td>RouterOS / SwOS (雙啟動)</td></tr><tr><td>**工作溫度**</td><td>‑40 °C 至 +70 °C</td></tr><tr><td>**外殼尺寸**</td><td>272 × 191 × 44 mm</td></tr></tbody></table>

## 配件 {#accessories}

包裝內含以下隨裝置附帶的配件：

![](/img/8c36c3fbb0b4f6fe.webp)

受支援的 SFP 模組請參見 [MikroTik wired interface compatibility](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。

## 作業系統支援 {#operating-system-support}

本裝置支援與 SwOS 2.9 及更高版本以及 RouterOS 7 或更高版本的雙啟動。具體的出廠安裝 RouterOS 版本可在 RouterOS 選單的 /system resource 下檢視。其他作業系統未經測試，也不受官方支援。
