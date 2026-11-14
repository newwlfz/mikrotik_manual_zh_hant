---
title: "Chateau LTE18 ax"
slug: /chateau-lte18-ax
source: https://manual.mikrotik.com/hardware/chateau-lte18-ax
captured_at: '2026-11-04T09:45:21+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/38e74cc92402c55b.jpg)

## [Chateau LTE18 ax](https://mikrotik.com/product/chateaulte18_ax) (S53UG+5HaxD2HaxD-TC&EG18-EA) {#chateau-lte18-ax-s53ug5haxd2haxd-tceg18-ea}

最好的家用 AP 變得更好了。這是 Chateau LTE18 的第 6 代版本。無線速度更快、CPU 更強，而且現在還配備了 2.5 千兆乙太網！完整規格和宣傳手冊請參見 [Chateau LTE18 ax 產品頁面](https://mikrotik.com/product/chateaulte18_ax)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 未使用正確的硬體或未遵循正確的操作步驟，可能會給人員帶來危險處境並損壞系統。
- 本產品僅供室內安裝使用。請讓本產品遠離水、火、潮溼或高溫環境。
- 請僅使用製造商認可的電源和配件，可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

請按照以下簡要步驟設定您的裝置：

![](/img/cbc5361d4144eab4.webp)

- 將外接天線連線到 SMA 接頭（天線隨包裝提供，請參見“天線使用”）；
- 將 micro SIM 卡插入裝置下方的卡槽，SIM 卡不隨包裝提供；

![](/img/9619076cdc698366.webp)

- 將裝置連線到電源；
- 透過任意一個乙太網埠或無線網路“MikroTik-...”連線到裝置（請務必在標籤上核對無線密碼）；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用 [https://mt.lv/winbox](https://mt.lv/winbox) 上的“WinBox”配置工具。**提供多種配置方式以確保可訪問性；**
- 使用預設 IP 地址 192.168.88.1 在所選的工具中開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇“Neighbors”標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為“admin”，沒有密碼（或者，對於某些型號，請在標籤上核對使用者密碼和無線密碼）；
- 選擇“Check for updates”按鈕，將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡或設定 eSIM，並且具備有效的網際網路連線，更新才能正常工作；
- 如需手動更新裝置，請訪問 [https://mikrotik.com/products](https://mikrotik.com/products) 上的產品頁面找到您的產品。所需的軟體包可在“Support&Downloads”選單下獲取；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的“Files”選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在“QuickSet”選單中進行以下設定：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 使用移動應用程式連線 {#connecting-with-a-mobile-app}

使用您的智慧手機透過 WiFi 訪問路由器。

![](/img/9bcba09a7b6a0d53.webp)

- 插入 SIM 卡併為裝置通電。
- 用智慧手機掃描二維條碼，並選擇您首選的作業系統。
- 連線到無線網路。SSID 以 MikroTik 開頭，並帶有裝置 MAC 地址的最後幾位數字。
- 開啟應用程式。
- 預設情況下，IP 地址和使用者名稱將已預先填入。
- 選擇 Connect，透過無線網路建立到裝置的連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/448fe884f3fe7820.webp)

- 復位按鈕。
- DC 電源插孔 2.0 mm。
- 五個千兆埠，支援自動交叉/直通線纜校正（Auto MDI/X）。連線其他網路裝置時，直通線或交叉線均可使用。
- USB type-A。
- Micro SIM 卡插槽。
- Mode 按鈕。
- 對於帶天線的型號，不提供外接 SMA 天線接頭的蓋板。
- WPS Sync 按鈕。
- 產品程式碼 S53UG+5HaxD2HaxD-TC&EG18-EA。
- CPU 四核 IPQ-6010 1.8 GHz。
- CPU 架構 ARM 64bit。
- RAM 大小 1 GB。
- RAM 型別 DDR3L。
- 儲存 128 MB，NAND。
- 1G 乙太網埠數量 4。
- 2.5G 乙太網埠數量 1。
- Micro SIM 插槽 1。
- USB 1 個 USB 3.0 type A。
- 交換晶片型號 IPQ-6010。
- 無線介面型號 QCN-5022（2.4 GHz）、QCN-5052（5 GHz）。
- 無線 2.4 GHz 802.11ax 雙鏈、5 GHz 802.11ax 雙鏈。
- 無線天線最大增益 2.4 GHz（3 dBi）、5 GHz（6 dBi）。
- LTE 類別 18（下行 1.2Gbps，上行 150Mbps）。
- LTE 調變解調器 EG18-EA。
- TAC 86981604。
- LTE 天線增益 4 dBi。
- LTE FDD 頻段 1（2100MHz）/ 3（1800MHz）/ 5（850MHz）/ 7（2600MHz）/ 8（900 MHz）/ 20（800MHz）/ 28（700MHz）。
- LTE TDD 頻段 38（2600MHz）/ 40（2300MHz）/ 41（2500MHz）。
- 3G 類別 R8（下行 42.2Mbps，上行 11.2Mbps）。
- 3G 頻段 1（2100MHz）/ 3（1800MHz）/ 5（850MHz）/ 8（900MHz）。
- 尺寸 240 x 156 x 44 mm。
- 作業系統 RouterOS v7，許可證級別 4。
- 工作溫度 -40°C 至 +65°C。

## 安裝 {#mounting}

本裝置設計用於室內，可放置在桌面上使用。

您應使用 CAT5 遮蔽電纜。在使用和安裝本裝置時，請注意最大允許暴露量（MPE）安全距離，即輻射體與您的身體之間至少保持 20 釐米的距離。

## 供電 {#powering}

- DC 輸入數量 1。
- DC 插孔輸入電壓 12-28 V。
- 電源介面卡標稱電壓 24 V。
- 電源介面卡標稱電流 1.2 A。
- 無附加裝置時最大功耗 16 W。
- 最大功耗 19 W。

## 配置 {#configuration}

可透過網頁瀏覽器使用 WebFig、WinBox 工具 [https://mt.lv/winbox](https://mt.lv/winbox) 或移動應用程式完成配置。提供多種方式以確保可訪問性。

- 要訪問 WebFig，請在瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1)。
- 對於 WinBox，請下載該工具，進入 Neighbors 標籤頁，然後選擇 MAC 地址。預設使用者名稱為“admin”，**密碼在裝置標籤上查詢**。您應經常檢查更新，以確保 RouterOS 軟體保持最新，從而獲得最佳效能和穩定性。在 WinBox 或 WebFig 中選擇“Check for updates”按鈕即可更新到最新版本。

必須插入有效的 SIM 卡或設定 eSIM，並且具備有效的網際網路連線，更新才能正常工作。

RouterOS 提供了本文件所述內容之外的廣泛配置選項。我們建議訪問 [https://mt.lv/help](https://mt.lv/help) 探索這些功能。

出於恢復目的，可以引導裝置進行重新安裝，請參見章節（連結）。

## Mode 按鈕 {#mode-button}

Mode 按鈕位於裝置背面右側。Mode 按鈕的預設配置為 dark mode —— 關閉所有 LED。可在 RouterOS 中配置該按鈕以執行任何使用者指定的指令碼。

## Sync 按鈕 {#sync-button}

Sync 按鈕位於裝置頂部。如果無線介面上已配置 WPS Sync 按鈕，則可用於連線新的用戶端。

![](/img/c76f6511aa4e14f0.webp)

- 按住 WPS 按鈕 1 – 5 秒，以為無線介面啟用 WPS。

## 前面板 LED 狀態 {#front-led-status}

![](/img/9ba5b3e5c27a0830.webp)

- 無線網路活動。
- 乙太網埠活動。
- 系統 LED。
- 訊號強度。蜂窩連線技術取決於系統 LED 顏色：紅色：GSM 黃色：3G 藍色：LTE 綠色：5G NSA 紫色：5G SA

當 LTE 未連線到網路時，系統 LED 會閃爍紅光，表示 LTE 連線存在某些問題。如果 LTE 介面被有意停用（未使用），系統 LED 將發出藍光。

## SIM 卡槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議使用轉接器。

## 復位按鈕 {#reset-button}

復位按鈕有三項功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在將尋找 CAPsMAN 伺服器（共 10 秒）。
- 要使用 Netinstall 實用程式重新安裝 RouterOS，請使裝置進入 BOOTP 模式。有兩種引導器可用：常規引導器和備用引導器。常規引導器 —— 為裝置通電，等待 1-2 秒，然後按下並按住復位按鈕。等待直到系統 LED 閃爍綠光，然後變為常亮“On”。當綠色 LED 變為“Off”時，鬆開復位按鈕 —— 裝置將進入 BOOTP 模式。
- 備用引導器 —— 關閉裝置電源，按下並按住復位按鈕，然後為其通電。等待直到系統 LED 閃爍綠光，然後變為常亮“On”。當綠色 LED 變為“Off”時，鬆開復位按鈕 —— 裝置將使用備用引導器進入 BOOTP 模式。無論使用上述哪種方式，如果在裝置通電之前就按下了按鈕，系統將載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

Netinstall 執行 Netinstall 時，請確保兩個 RouterOS 都使用最新的 v7 版本。將您的 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- ADAPT1_ EU/US 開關電源 24V，1.2A。
- CAB3_ CAT5E UTP 扁平電纜，8P8C，AWG32，1.5m。

## 天線使用 {#antenna-usage}

SMA 接頭用於 LTE 天線。

外接天線插座位於裝置背面。裝置隨附已連線的無線天線，LTE 天線不隨包裝提供。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。
