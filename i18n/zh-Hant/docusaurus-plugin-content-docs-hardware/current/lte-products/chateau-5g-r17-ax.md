---
title: "Chateau 5G R17 ax"
slug: /chateau-5g-r17-ax
source: https://manual.mikrotik.com/hardware/chateau-5g-r17-ax
captured_at: '2026-11-04T09:45:14+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/58927a682e31d536.jpg)

## [Chateau 5G R17 ax](https://mikrotik.com/product/chateau_5g_r17_ax)（S53UG+5HaxD2HaxD-TC&RG650E-EU） {#chateau-5g-r17-ax-s53ug5haxd2haxd-tcrg650e-eu}

即刻上網——即使沒有 SIM 卡也能使用。這款標誌性的 MikroTik 5G 家用路由器迎來了迄今最智慧的一次升級……完整的 eSIM 支援！完整規格與產品手冊請參見 [Chateau 5G R17 ax 產品頁面](https://mikrotik.com/product/chateau_5g_r17_ax)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品僅供室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢棄物處置點。請了解將裝置妥善運輸至您所在地區指定處置點的相關程式。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。安裝和操作本 MikroTik 裝置時，其與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

按照以下快速步驟設定您的裝置：

![](/img/cbc5361d4144eab4.webp)

- 按裝置上指示的位置將 SIM 卡插入卡槽；如果您想使用 eSIM，請閱讀 eSIM 章節；

![](/img/9619076cdc698366.webp)

- 將裝置連線到電源；
- 透過任一乙太網埠或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在所選工具中，使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 選擇 "Check for updates" 按鈕並將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡或設定好 eSIM，並具備有效的網際網路連線，更新才能正常工作；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中進行以下設定：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 使用移動應用程式連線 {#connecting-with-a-mobile-app}

使用您的智慧手機透過 WiFi 訪問路由器。

![](/img/9bcba09a7b6a0d53.webp)

- 按裝置上指示的位置將 SIM 卡插入卡槽並開啟裝置電源；如果您想使用 eSIM，請閱讀 eSIM 章節；
- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟該應用程式。
- 選擇 Connect，透過無線網路與您的裝置建立連線（請檢視貼紙上的無線密碼）。
- 使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。
- 選擇 Quick Setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要設定。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/448fe884f3fe7820.webp)

- (link)DC 插孔 2.0 mm。
- 四個千兆埠和一個 2.5 千兆埠，支援自動交叉/直通線纜校正（Auto MDI/X）。連線其他網路裝置時可以使用直通線或交叉線。
- USB type-A。
- (link) 用於 Micro SIM 卡。
- Mode 按鈕。
- 帶天線的型號不提供外部 SMA 天線介面蓋。
- WPS (link)
- 產品程式碼：**S53UG+5HaxD2HaxD-TC&RG650E-EU**。
- CPU：四核 IPQ-6010 1.8 GHz。
- CPU：架構 ARM 64bit。
- RAM 容量：1 GB。
- RAM 型別：DDR3L。
- 儲存：128 MB，NAND。
- 1G 乙太網埠數量：4。
- 2.5G 乙太網埠數量：1。
- Micro SIM 插槽：1。
- eSIM。
- USB：1 個 USB 3.0 type A。
- 交換晶片型號：IPQ-6010。
- 無線介面型號：QCN-5022（2.4 GHz）、QCN-5052（5 GHz）。
- 無線：2.4 GHz 802.11b/g/n/ax 雙鏈，5 GHz 802.11a/n/ac/ax 雙鏈。
- LTE 類別：20（下行 2.0 Gbps，上行 211 Mbps）。
- LTE 調變解調器：RG650E-EU。
- TAC：86896506。
- 5G SA 類別：下行 7.01 Gbps，上行 1.25 Gbps。
- 5G NSA 類別：下行 5.47 Gbps，上行 730 Mbps。
- 3G 類別：R8（下行 42.2Mbps，上行 5.76Mbps）。
- MIMO DL：4x4。
- MIMO UL：1x1（5G SA MIMO UL 2x2）。
- 5G SA FDD 頻段：1（2100 MHz）/ 3（1800 MHz）/ 5（850 MHz）/ 7（2600 MHz）/ 8（900 MHz）/ 20（800 MHz）/ 26（850 MHz）/ 28（700 MHz）/ 67（700 MHz）/ 75（1500 MHz）/ 76（1500 MHz）。
- 5G SA TDD 頻段：38（2600 MHz）/ 40（2300 MHz）/ 41（2500 MHz）/ 77（3700 MHz）/ 78（3500 MHz）。
- 5G NSA FDD 頻段：1（2100 MHz）/ 3（1800 MHz）/ 5（850 MHz）/ 7（2600 MHz）/ 8（900 MHz）/ 20（800 MHz）/ 26（850 MHz）/ 28（700 MHz）/ 67（700 MHz）/ 75（1500 MHz）/ 76（1500 MHz）。
- 5G NSA TDD 頻段：38（2600 MHz）/ 40（2300 MHz）/ 41（2500 MHz）/ 77（3700 MHz）/ 78（3500 MHz）。
- LTE FDD 頻段：1（2100MHz）/ 3（1800MHz）/ 5（850MHz）/ 7（2600MHz）/ 8（900 MHz）/ 20（800MHz）/ 28（700MHz）/ 32（1500 MHz）。
- LTE TDD 頻段：38（2600MHz）/ 41（2500MHz）/ 42（3500MHz）/ 40（2300MHz）/ 43（3700MHz）。
- 3G 頻段：1（2100MHz）/ 5（850MHz）/ 8（900MHz）。
- 尺寸：240 x 156 x 44 mm。
- 作業系統 RouterOS：v7，許可證級別 4。
- 工作溫度：-40°C 至 +70°C。

## 安裝 {#mounting}

本裝置設計為室內使用，可放置在桌面上。

您應使用 CAT5 遮蔽網線。使用和安裝本裝置時，請注意最大允許暴露量（MPE）安全距離，輻射體與您身體之間至少保持 20 釐米。

## 供電 {#powering}

- DC 輸入數量 1。
- DC 插孔輸入電壓 12-28 V。
- 電源介面卡標稱電壓 24 V。
- 電源介面卡標稱電流 1.2 A。
- 不含附件時的最大功耗為 18 W。
- 最大功耗 27 W。

## 配置 {#configuration}

配置可透過網頁瀏覽器使用 WebFig、WinBox 工具 [https://mt.lv/winbox](https://mt.lv/winbox) 或 (link) 完成。提供多種方法以確保可訪問性。

- 要訪問 WebFig，請在瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1)。
- 對於 WinBox，請下載該工具，轉到 Neighbors 標籤頁，然後選擇 MAC 地址。預設使用者名稱為 "admin"，**請在裝置貼紙上查詢密碼**。您應經常檢查更新，以確保您的 RouterOS 軟體保持最新，從而獲得最佳效能和穩定性。在 WinBox 或 WebFig 中選擇 "Check for updates" 按鈕即可更新到最新版本。

必須插入有效的 SIM 卡或設定好 eSIM，並具備有效的網際網路連線，更新才能正常工作。

除了本文件所述內容之外，RouterOS 還提供許多其他配置選項。更多詳情，請訪問 [https://mt.lv/help](https://mt.lv/help)。為便於恢復，裝置可引導進入重灌模式。有關說明，請參見 (link) 章節。

## Mode 按鈕 {#mode-button}

Mode 按鈕位於裝置背面右側。預設情況下，Mode 按鈕配置為控制深色模式。

要關閉所有 LED，請短按一次 Mode 按鈕。要重新開啟 LED，請再次按下該按鈕。

該按鈕也可在 RouterOS 中配置為執行使用者自定義指令碼。

## Sync 按鈕 {#sync-button}

Sync 按鈕位於裝置頂部。如果在無線介面上配置了 WPS Sync 按鈕，則可用其連線新用戶端。

![](/img/c76f6511aa4e14f0.webp)

- 按住 WPS 按鈕 1 – 5 秒，即可為無線介面啟用 WPS。

## 前面板 LED 狀態 {#front-led-status}

![](/img/9ba5b3e5c27a0830.webp)

- 無線網路活動。
- 乙太網埠活動。
- 系統 LED。
- 訊號強度。蜂窩連線技術由系統 LED 顏色表示：紅：GSM 黃：3G 藍：LTE 綠：5G NSA 紫：5G SA

當 LTE 未連線到網路時，系統 LED 將閃紅光，表示 LTE 連線存在某種問題。如果 LTE 介面被有意停用（未使用），系統 LED 將發出藍光。

## SIM 卡槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議配合轉接卡使用。

## eSIM 設定 {#esim-settings}

預設情況下，裝置配置為使用 SIM 卡槽。要使用板載 eSIM，請使用以下命令切換卡槽：**/interface/lte/settings/set sim-slot=esim**

單個 eSIM 晶片可以儲存多個 eSIM 配置檔案，最大配置檔案數量取決於所使用的 eSIM 晶片。

詳情請參見 [LTE eSIM](/docs/mobile-networking/lte-5g#lte-esim) 頁面。

## Reset 按鈕 {#reset-button}

Reset 按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置將開始查詢 CAPsMAN 伺服器（共 10 秒）。
- 要使用 Netinstall 實用程式重新安裝 RouterOS，請使裝置進入 BOOTP 模式。有兩種載入程式可用：常規載入程式和備用載入程式。常規載入程式 - 開啟裝置電源，等待 1-2 秒，然後按下並按住 Reset 按鈕。等待系統 LED 閃爍綠光，然後變為常亮 "On"。當綠色 LED 變為 "Off" 時，鬆開 Reset 按鈕 - 裝置將進入 BOOTP 模式。
- 備用載入程式 – 關閉裝置電源，按下並按住 Reset 按鈕，然後開啟電源。等待系統 LED 閃爍綠光，然後變為常亮 "On"。當綠色 LED 變為 "Off" 時，鬆開 Reset 按鈕 - 裝置將使用備用載入程式進入 BOOTP 模式。無論使用上述哪種方式，如果在裝置通電前按鈕已被按下，系統將載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

Netinstall 執行 Netinstall 時，請確保同時使用最新 v7 版本的 ROS 檔案和 Netinstall 軟體。

## 配件 {#accessories}

包裝內包含隨裝置提供的以下配件：

- ADAPT1_ EU/US 開關電源 24V，1.2A。
- CAB3_ CAT5E UTP 扁平網線，8P8C，AWG32，1.5m。

## 取下後蓋以接觸 PCB {#removing-back-cover-to-access-pcb}

如果需要接觸 PCB，可以取下後蓋。

- 取下中央螺絲；

![](/img/3c40f644b6453592.webp)

- 使用小螺絲刀在標記處撬開後蓋板；
- 繼續向上撬開；

![](/img/ef5c2817560d190a.webp)

- 最後將整個後蓋板取下。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

有關重要的安全說明和法規認證，請參閱每個產品隨附的《安全與法規資訊》文件：Documents→ Safety and Regulatory Information
