---
title: "CRS317-1G-16S+RM"
slug: /crs317-1g-16s-plus-rm
source: https://manual.mikrotik.com/hardware/crs317-1g-16s-plus-rm
captured_at: '2026-11-04T09:46:24+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/84737252c152a168.jpg)

## [CRS317-1G-16S+RM](https://mikrotik.com/product/crs317_1g_16s_rm) {#crs317-1g-16srm}

智慧交換器，1 個千兆 LAN 口，16 個 SFP+ 籠，雙核 800MHz CPU，1GB 記憶體，1U 機架式被動散熱機箱，雙電源。完整規格與宣傳冊請參閱 [CRS317-1G-16S+RM 產品頁面](https://mikrotik.com/product/crs317_1g_16s_rm)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終廢棄處理應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟可能導致對人員的危險情況以及對系統的損壞。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 用您的 PC 連線到任意乙太網口；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內使用，可使用隨附的機架安裝件安裝在機架機箱中，也可以放置在桌面上。如果希望放置在平整表面上，請在路由器底部貼上橡膠腳墊；如果指定用於機架機箱，請使用十字螺絲刀在裝置兩側安裝機架掛耳：

- 將機架掛耳安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如圖所示。
- 將裝置放入機架機箱並對齊孔位，使裝置安裝順暢。

![](/img/837a6d2bb5f312fe.webp)

- 擰緊螺絲將其固定到位。

本裝置的 IP 防護等級為 IP0。裝置沒有防水汙染保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 網線。本裝置的安裝和配置應由具備資質的人員完成。

## 供電 {#powering}

本裝置可透過兩個 IEC C14 標準介面供電，支援 AC 110/240 V ⏦。同一時間只有一個 PSU 處於工作狀態，第二個用於冗餘。不含 PoE 注入器。本裝置在最大負載下的功耗最高為 44W。

本裝置配有被動散熱器，正常負載下將靜音執行，但在緊急情況下，如果環境溫度高於正常水平，兩個冗餘風扇會自動開啟以保持裝置冷卻。本裝置已透過測試，可在 -20 ℃ 至 +60 ℃ 的環境溫度下工作。

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件可在 [https://mt.lv/help](https://mt.lv/help) 獲取。本裝置可使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方式以確保可訪問性。**

在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。

本裝置配備一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。出於恢復目的，可以從網路重新安裝裝置，請參閱復位按鈕。

Marvell Prestera 交換晶片的特性在 [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) 手冊中有描述。

本裝置支援啟動 RouterOS（用於完整的路由和交換功能）或 SwOS（僅用於交換操作）。預設情況下，裝置啟動進入 RouterOS，但您也可以按如下方式切換到另一個作業系統：

- 從 SwOS：進入 **System** 選單，然後單擊頁面底部的 "**Boot RouterOS**" 按鈕。
- 從 RouterOS：開啟 **System → RouterBOARD → Settings** 並選擇 **Boot OS**。

也可以使用序列埠控制檯選單來選擇作業系統並配置其他啟動選項。

## 規格 {#specifications}

<table><thead><tr><th>**產品程式碼**</th><th>CRS317‑1G‑16S+RM</th></tr></thead><tbody><tr><td>**CPU**</td><td>98DX8216, 800 MHz</td></tr><tr><td>**CPU 架構**</td><td>ARM 32bit</td></tr><tr><td>**CPU 核心數**</td><td>2</td></tr><tr><td>**交換晶片型號**</td><td>98DX8216</td></tr><tr><td>**記憶體**</td><td>1 GB</td></tr><tr><td>**儲存**</td><td>16 MB Flash</td></tr><tr><td>**1G 乙太網 (RJ45)**</td><td>1</td></tr><tr><td>**10G SFP+ 埠**</td><td>16</td></tr><tr><td>**序列埠控制檯 (RJ45)**</td><td>1</td></tr><tr><td>**作業系統**</td><td>RouterOS（license level 6）/ SwOS（雙啟動）</td></tr><tr><td>**工作溫度**</td><td>‑20 °C 至 +60 °C</td></tr><tr><td>**機箱尺寸**</td><td>443 × 224 × 44 mm</td></tr></tbody></table>

## 復位按鈕 {#reset-button}

- 要復位配置，請斷開裝置電源，按住復位按鈕，並在 USER (USR) LED 開始閃爍時鬆開。
- 要載入備份載入程式，請在通電前按住復位按鈕，三秒後鬆開。
- 要啟動 Netinstall 過程（以 BOOTP 模式啟動裝置以重新安裝 RouterOS），請按住復位按鈕，給裝置通電，等待 USER (USR) LED 閃爍後變為常亮。當 USR LED 熄滅時，鬆開復位按鈕。

無論使用上述哪種方式，如果在裝置通電前按住按鈕，系統都會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## SwOS 復位與重灌 {#swos-reset-and-reinstall}

CRS317-1G-16S+ 內建備份 SwOS 韌體，可在標準韌體損壞或升級失敗時載入：

- 在 CRS317-1G-16S+ 啟動時按住復位按鈕幾秒鐘，會復位配置並載入備份 SwOS 韌體。
- 載入備份 SwOS 韌體後，可以使用網頁瀏覽器連線到 192.168.88.1 並安裝新的 SwOS 韌體。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

![](/img/521a0300a1918465.webp)

請訪問 wiki 頁面檢視 MikroTik SFP 模組相容性表：MikroTik 有線介面相容性。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統未經過測試。
