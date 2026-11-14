---
title: "CRS354-48P-4S+2Q+RM"
slug: /crs354-48p-4s-plus-2q-plus-rm
source: https://manual.mikrotik.com/hardware/crs354-48p-4s-plus-2q-plus-rm
captured_at: '2026-11-04T09:46:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/e66c7c05186d738d.jpg)

CRS354 是一款網路交換器，具有 48 個千兆埠（可為你的裝置提供 PoE 供電）、四個 10G SFP+ 埠、兩個 40G QSFP+ 埠。該裝置開箱即可作為交換器使用。完整規格和宣傳冊請參見 [CRS354-48P-4S+2Q+RM 產品頁面](https://mikrotik.com/product/crs354_48p_4s_2q_rm)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵循所有國家法律和法規。裝置的安裝必須符合當地和國家的電氣規範。本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或未遵循正確的操作步驟，可能會給人員帶來危險並損壞系統。本產品僅供室內安裝。請使本產品遠離水、火、潮溼或高溫環境。只能使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

該裝置的所有介面均已處於交換狀態。

- 將你的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 以開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇你的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，你可以確保獲得最佳效能、穩定性和安全更新；
- 設定你的路由器密碼。

## 安裝 {#mounting}

該裝置設計用於室內使用，可使用隨附的機架安裝件安裝在機架機箱中，也可以放置在桌面上。使用十字螺絲刀將機架安裝耳片安裝到裝置兩側，如果指定用於機架機箱，則還要安裝到裝置後部的兩側：

- 將支架安裝到右前側。
- 安裝右後支架。
- 將支架安裝到左前側。
- 安裝左後支架。
- 將長支架安裝到機架上，並用孔位安裝裝置，使裝置安裝得合適便捷。
- 如有需要，安裝線纜管理支架。

![](/img/97fa6fa4cd1f427d.webp)

請確保將裝置放置在乾燥且通風良好的環境中。防護等級為 IP20。我們建議為我們的裝置使用 Cat6 線纜。本裝置的安裝和配置應由具備資質的人員完成。

## 供電 {#powering}

該裝置接受 100 – 240 V AC ⏦ 輸入供電。標稱電壓 53 V。標稱電流 13.5 A。該裝置在最大負載下的功耗最高為 85 W。帶外接裝置時為 800 W。

## 電源輸出 {#power-output}

該裝置支援從乙太網 1 - 48 埠輸出 PoE 802.3af/at，你可以為支援透過乙太網供電的 MikroTik 裝置供電。每埠輸出（53V 輸出）570 mA 每埠輸出（26V 輸出）1000 mA 總輸出功率 700 W 總輸出 27 A（26 V 時），或 13,2 A（53 V 時）。

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件可在以下地址獲取：[https://mt.lv/help](https://mt.lv/help) 你可以使用網頁瀏覽器中的 WebFig 或 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方式以確保可訪問性。** **要開始設定，請在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 以開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。該裝置配有一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。出於恢復目的，可以從網路重新安裝裝置，請參閱復位按鈕。

Marvell Prestera 交換器晶片功能使用者手冊

該裝置支援啟動 RouterOS（以獲得完整的路由和交換功能）或 SwOS（僅用於交換執行）。預設情況下，裝置啟動進入 RouterOS，但你可以按如下方式切換到另一個作業系統：

- 從 SwOS 切換：轉到 System 選單，點選頁面底部的 Boot RouterOS 按鈕。
- 從 RouterOS 切換：開啟 System → RouterBOARD → Settings 並選擇 Boot OS。也可以使用序列控制檯選單選擇作業系統並配置其他啟動選項。

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 在啟動期間按住此按鈕，直到 USR LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 按住 Reset 按鈕並給裝置通電（等待直到 "USR" 指示燈閃爍然後穩定為 "On"，當 "USR" 指示燈為 "Off" 時鬆開 Reset 按鈕）——裝置將以 bootp 模式啟動，以便使用 Netinstall 重新安裝 RouterOS。**MGMT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。請在 LED 開始閃爍之前鬆開按鈕，以便僅載入備份 RouterBOOT 而不進行重設。這對於 RouterBOOT 偵錯和恢復很有用。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<table><thead><tr><th>**產品程式碼**</th><th>CRS354-48P-4S+2Q+RM</th></tr></thead><tbody><tr><td>**CPU**</td><td>QCA9531, 650 MHz</td></tr><tr><td>**CPU 架構**</td><td>MIPSBE</td></tr><tr><td>**CPU 核心數**</td><td>1</td></tr><tr><td>**交換晶片型號**</td><td>98DX3257</td></tr><tr><td>**RAM**</td><td>128 MB</td></tr><tr><td>**儲存**</td><td>32 MB Flash</td></tr><tr><td>**1G 乙太網（RJ45）**</td><td>48</td></tr><tr><td>**10G SFP+ 埠**</td><td>4</td></tr><tr><td>**40G QSFP+ 埠**</td><td>2</td></tr><tr><td>**序列控制檯（RJ45）**</td><td>1</td></tr><tr><td>**作業系統**</td><td>RouterOS v7（許可證級別 5）/ SwitchOS（雙啟動）</td></tr><tr><td>**工作溫度**</td><td>-20 °C 至 +60 °C</td></tr><tr><td>**機箱尺寸**</td><td>443 × 382 × 44 mm</td></tr><tr><td>**PoE-Out 支援**</td><td>802.3af/at，全部 48 個乙太網埠支援 Passive PoE</td></tr></tbody></table>

有關 MikroTik SFP 模組相容性和配置表，請訪問幫助頁面：MikroTik 有線介面相容性

## 配件 {#accessories}

包裝中包含以下隨裝置提供的附件：

![](/img/1b280d2928a433ba.webp)

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及更高版本。具體出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。
