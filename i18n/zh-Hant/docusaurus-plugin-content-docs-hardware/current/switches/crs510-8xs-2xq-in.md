---
title: "CRS510-8XS-2XQ-IN"
slug: /crs510-8xs-2xq-in
source: https://manual.mikrotik.com/hardware/crs510-8xs-2xq-in
captured_at: '2026-11-04T09:46:59+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/da327122ff8856a5.jpg)

一臺用途廣泛的 100 Gigabit 交換器，兼具速度、價效比與多樣化的連線選項。2 個 100 Gigabit QSFP28 埠、8 個 25 Gigabit SFP28 埠、雙熱插拔電源。完整規格與產品手冊請參閱 [CRS510-8XS-2XQ-IN 產品頁面](https://mikrotik.com/product/crs510_8xs_2xq_in)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵守所有國家法律和法規。裝置的安裝必須符合當地和國家的電氣規範。本裝置設計用於機架安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟，可能會給人員帶來危險並損壞系統。本產品僅供室內安裝使用。請讓本產品遠離水、火、潮溼或高溫環境。僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法，以確保可訪問性；**
- 在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內使用，可使用隨附的機架安裝件安裝在機架機箱中，也可以放置在桌面上。如果希望放置在平坦表面上，請在路由器底部貼上橡膠腳墊；如果指定用於機架機箱，請使用十字螺絲刀在裝置兩側安裝機架耳件：

- 如圖所示，將機架耳件安裝到裝置兩側，並擰緊四顆螺絲將其固定到位。
- 將裝置放入機架機箱並對準孔位，使裝置順利安裝。
- 擰緊螺絲將其固定到位。

![](/img/27bf22aa32ecbced.webp)

本裝置的 IP 防護等級為 IPX0。該裝置不具備防水汙染保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用遮蔽 Cat5/6 網線。本裝置的安裝*與配置應由合格人員進行。*

## 配置 {#configuration}

RouterOS 的完整文件可在以下地址獲取：[https://mt.lv/help](https://mt.lv/help) 您可以使用網頁瀏覽器中的 WebFig 或 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方法，以確保可訪問性。** **要開始設定，請在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）。本裝置配備一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。出於恢復目的，可以從網路重新安裝裝置，請參見 Reset 按鈕。

Marvell Prestera 交換晶片功能使用者手冊

## 供電 {#powering}

- DC 輸入數量 3（PoE-in、DC 插孔、2 針端子）
- PoE-in 輸入電壓 43-57 V Passive PoE 或 802.3bt Class 6
- DC 插孔輸入電壓 36-57 V
- 2 針端子輸入電壓 36-57 V
- AC 輸入數量 2
- AC 輸入範圍 100-240 V
- 頻率 47-63 Hz
- 無附件時最大功耗 27 W
- 最大功耗 45 W

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品代號 CRS510-8XS-2XQ-IN
- CPU QCA9531 650 MHz
- CPU 架構 MIPSBE
- CPU 核心數 1
- RAM 容量 128 MB
- 儲存 32 MB，Flash
- 100M 乙太網埠數量 1
- 25G SFP28 埠數量 8
- 100G QSFP28 埠數量 2
- 交換晶片型號 98DX4310
- 尺寸 320 x 185 x 44 mm
- 作業系統 RouterOS v7，許可證級別 5
- 工作溫度 -40°C 至 +70°C

## Reset 按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並恢復預設值。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置搜尋 Netinstall 伺服器（透過網路安全重灌 RouterOS 時需要）。無論使用上述哪種方式，如果在裝置接通電源之前就按住了按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下附件：

![](/img/ef3af0d9213c99f8.webp)

有關 MikroTik SFP 模組相容性和配置表，請訪問幫助頁面：MikroTik 有線介面相容性

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。
