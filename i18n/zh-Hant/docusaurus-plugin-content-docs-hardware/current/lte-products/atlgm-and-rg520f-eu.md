---
title: "ATLGM 和 RG520F-EU"
slug: /atlgm-and-rg520f-eu
source: https://manual.mikrotik.com/hardware/atlgm-and-rg520f-eu
captured_at: '2026-11-04T09:40:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/d270e1ee055a4eed.jpg)

## [ATL 5G R16](https://mikrotik.com/product/atl_5g_r16)（ATLGM&RG520F-EU） {#atl-5g-r16-atlgmrg520f-eu}

這是我們首款內建 eSIM 支援的室外 5G 裝置，配備強勁的定向天線和先進的 Release 16 調變解調器——非常適合農村、城市和 IoT 部署場景。它具備千兆乙太網、PoE-in，開箱即可使用 MikroTik 連線功能，是隨時隨地獲得快速、靈活網際網路的智慧且堅固之選。透過 IP66 認證。完整規格和宣傳冊請參見 [ATL 5G R16 產品頁面](https://mikrotik.com/product/atl_5g_r16)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 在任何牆面安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於在室外安裝在立杆上。開始安裝前請仔細閱讀安裝說明。未能使用正確的硬體和配置或遵循正確的操作流程，可能導致人員處於危險境地並對系統造成損壞。
- 只能使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內工作、輸出功率和佈線要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能會引起無線電干擾，此時使用者可能需要採取適當的措施。
- 為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置妥善運送到指定處置場所的相關程式。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，與您的身體、職業使用者或公眾的距離不得小於 30 釐米。

## 快速開始 {#quickstart}

- 開啟乙太網埠蓋；
- 將 Micro SIM 卡晶片朝上插入卡槽；如果您想使用 eSIM，請閱讀 eSIM 部分；
- 使用乙太網線將裝置連線到隨附的 PoE 供電器上的資料+電源端；
- 將 PoE 供電器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 透過 WebFig 或 WinBox 工具使用 Web 瀏覽器配置您的裝置，地址為 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.188.1](https://192.168.188.1) 訪問 WebFig；對於 WinBox，請下載該工具，轉到 Neighbors 標籤頁，然後選擇 MAC 地址。使用者名稱為 "admin"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 選擇 "Check for updates" 按鈕，將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡或已設定 eSIM，並且需要有效的網際網路連線。
- 如需手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 找到您的產品。所需的軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 設定路由器密碼。

![](/img/1acbe30d4d490952.webp)

## 供電 {#powering}

- 直流輸入數量：1 (PoE-IN)。
- PoE 輸入：802.3 af/at。
- PoE 輸入電壓：12-56 V。
- 電源介面卡額定電流：0.8 A。
- 無配件時的最大功耗：10 W。
- 最大功耗：10 W。

## 安裝 {#mounting}

- 將隨附的金屬安裝環滑入天線反射盤背面的兩個槽中。
- 將裝置安裝到立杆上，乙太網埠朝下。
- 使用 PH2 螺絲刀擰緊安裝環。
- 使用紮帶將乙太網線固定到立杆上，距離裝置不超過一米，以免線纜被從埠中拉出。如需使用預製好的乙太網線，必須先切開橡膠密封圈。或者，在連線 RJ45 接頭之前將線纜穿過橡膠密封圈。請勿在沒有橡膠密封圈的情況下使用線纜，否則會破壞 IP66 防護等級。
- 檢查安裝角度和位置。在室外安裝時，請確保所有線纜開口朝下。使用 POE 供電器並正確接地，本裝置在埠蓋下方設有專門設計的接地聯結器。建議使用遮蔽 Cat5/6 線纜。本裝置的 IP 防護等級為 IP66。

## 配置 {#configuration}

可以透過 Web 瀏覽器使用 WebFig 進行配置，也可使用 WinBox 工具 [https://mt.lv/winbox](https://mt.lv/winbox)，提供多種方法以確保可訪問性。

- 要訪問 WebFig，請在瀏覽器中開啟 [https://192.168.188.1](https://192.168.188.1)。
- 對於 WinBox，請下載該工具，轉到 Neighbors 標籤頁，然後選擇 MAC 地址。預設使用者名稱為 "admin"，**密碼請檢視裝置貼紙**。您應經常檢查更新，以確保您的 RouterOS 軟體保持最新，獲得最佳效能和穩定性。在 WinBox 或 WebFig 中選擇 "Check for updates" 按鈕以更新到最新版本。

必須插入有效的 SIM 卡或已設定 eSIM，並具備有效的網際網路連線，更新才能正常工作。

RouterOS 提供了本文件所述內容之外的廣泛配置選項。我們建議訪問 [https://mt.lv/help](https://mt.lv/help) 探索這些功能。

為便於恢復，可以引導裝置進行重新安裝，請參見相關章節。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

![](/img/f302bf1cf0939e79.webp)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼：**ATLGM&RG520F-EU.**
- CPU 雙核：88F3720 800 MHz
- CPU 架構：ARM 64bit
- RAM 大小：512 MB
- RAM 型別：DDR3L
- 儲存：32 MB，Flash
- 1G 乙太網埠數量：1
- LTE 類別：20（下行 2.0 Gbps，上行 200 Mbps）
- LTE 調變解調器：RG520F-EU
- TAC：86945405
- 5G SA 類別：下行 4.2 Gbps，上行 900 Mbps。
- 5G NSA 類別：下行 5.0 Gbps，上行 650 Mbps。
- 3G 類別：R8（下行 42.2Mbps，上行 5.76Mbps）。
- MIMO 下行：4x4。
- 5G SA FDD 頻段：1 (2100 MHz) / 3 (1800 MHz) / 5 (850 MHz) / 7 (2600 MHz) / 8 (900 MHz) / 20 (800 MHz) / 28 (700 MHz)。
- 5G SA TDD 頻段：38 (2600 MHz) / 40 (2300 MHz) / 41 (2500 MHz) / 75 (1500 MHz) / 76 (1500 MHz) / 77 (3700 MHz) / 78 (3500 MHz)。
- 5G NSA FDD 頻段：1 (2100 MHz) / 3 (1800 MHz) / 5 (850 MHz) / 7 (2600 MHz) / 8 (900 MHz) / 20 (800 MHz) / 28 (700 MHz)。
- 5G NSA TDD 頻段：40 (2300 MHz) / 41 (2500 MHz) / 77 (3700 MHz) / 78 (3500 MHz) / 76 (1500 MHz) / 38 (2600 MHz) / 75 (1500 MHz)。
- LTE FDD 頻段：20 (800MHz) / 28 (700MHz) / 3 (1800MHz) / 5 (850MHz) / 7 (2600MHz) / 8 (900 MHz) / 1 (2100MHz) / 32 (1500 MHz)。
- LTE TDD 頻段：40 (2300MHz) / 38 (2600MHz) / 41 (2500MHz) / 42 (3500MHz)。
- 3G 頻段：1 (2100MHz) / 5 (850MHz) / 8 (900MHz)。
- 尺寸：311 x 311 x 179 mm。
- 作業系統：RouterOS 版本 7，許可證級別 3
- 工作溫度 -40°C 至 +70°C

## SIM 卡槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議使用轉接器。

## eSIM 設定 {#esim-settings}

預設情況下，裝置配置為使用 SIM 卡槽。要使用板載 eSIM，請使用以下命令切換卡槽：**/interface/lte/settings/set sim-slot=esim**

單個 eSIM 晶片可以儲存多個 eSIM 配置檔案，最大配置檔案數量取決於所使用的 eSIM 晶片。

詳情請參見 [LTE eSIM](/docs/mobile-networking/lte-5g#lte-esim) 頁面。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置將開始查詢 CAPsMAN 伺服器（共 10 秒）。
- 使用 Netinstall 重新安裝 RouterOS。要使用 Netinstall 實用程式重新安裝 RouterOS，請將裝置進入 BOOTP 模式。可用的載入程式有兩種：常規載入程式和備份載入程式。常規載入程式 - 給裝置上電，等待 1-2 秒，然後按住復位按鈕。等待直到 "USR" LED 閃爍，隨後變為常亮 "On"。當 "USR" LED 變為 "Off" 時，鬆開復位按鈕 - 裝置將進入 BOOTP 模式。
- 備份載入程式 – 關閉裝置電源，按住復位按鈕，然後給裝置上電。等待直到 "USR" LED 閃爍，隨後變為常亮 "On"。當 "USR" LED 變為 "Off" 時，鬆開復位按鈕 - 裝置將使用備份載入程式進入 BOOTP 模式。無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都會載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

Netinstall執行 Netinstall 時，請確保 ROS 檔案和 Netinstall 軟體都使用最新的 v7 版本。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統未經測試。

有關重要的安全說明和法規認證資訊，請參閱 [https://mikrotik.com/products](https://mikrotik.com/products) 上提供的 Safety and Regulatory Information 文件。導航至： Support & Downloads → Safety and Regulatory Information
