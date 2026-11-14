---
title: "RB5009UG+S+IN"
slug: /rb5009ug-plus-s-plus-in
source: https://manual.mikrotik.com/hardware/rb5009ug-plus-s-plus-in
captured_at: '2026-11-04T06:04:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/de416873eea75cb9.jpg" alt="" width={799} height={502} /></p>

## [RB5009UG+S+IN](https://mikrotik.com/product/rb5009ug_s_in) {#rb5009ugsin}

這是一款終極過載型家庭實驗室路由器，配備 USB 3.0、1G 與 2.5G 乙太網以及一個 10G SFP+ 網籠。您可以在單個 1U 機架空間中安裝四臺這樣的新型路由器！在如此小巧的尺寸下實現了前所未有的處理能力。完整規格與產品手冊請參見 [RB5009UG+S+IN 產品頁面](https://mikrotik.com/product/rb5009ug_s_in)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於機架安裝。開始安裝前請仔細閱讀安裝說明。使用不正確的硬體或不遵循正確的操作步驟，可能給人員帶來危險並損壞系統。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 請確認您的 ISP 接受硬體變更並會自動分配 IP 地址；
- 將 ISP 網線連線到 Ethernet1 埠；
- 將 PC 連線到除 Ethernet1 以外的任意埠；
- 將裝置連線到電源；
- 將網路卡設定配置為使用 DHCP 自動獲取 IP 地址；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

最大負載下的功耗可達 20 W。裝置可透過電源插孔或第一個乙太網埠接受供電：

- 直流輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 24-57 V DC。
- 第一個乙太網埠接受 Power over Ethernet 24-57 V DC。
- 側面的 2 針端子接受 24-57 V DC。
- 2 針端子：聯結器插頭 P=5.08 mm 1x2pin RA TH，鍍錫，300 V 10 A。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線纜連線到 PoE 介面卡的 PoE 埠；
- 將來自您 LAN 的乙太網線纜連線到 PoE 介面卡的 LAN 埠，注意資料和電流流向的箭頭；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help)開始，以便熟悉各種可能性。如果無法建立 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。為了恢復目的，可以從網路引導裝置，請參見 Reset 按鈕。

## 安裝 {#mounting}

本裝置設計用於室內使用，可以安裝在牆上，也可以放置在桌面上。

<p><Img src="/img/8a5382c1f81612f6.webp" alt="" width={556} height={298} /></p>

- 如示意圖所示，找到裝置兩側預留的安裝孔；
- 使用隨附的螺釘將裝置固定到牆上；
- 根據牆體材料，您可以使用鑽頭和隨附的定位銷。

本裝置沒有防水汙染保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 線纜。*本裝置的安裝和配置應由合格人員完成。*

## 機架安裝 {#rackmount}

如果希望安裝在機架上，可單獨購買額外的支架：

### RB5009 機架安裝套件 K-79 {#rb5009-rackmount-kit-k-79}

<p><Img src="/img/d12c6eeeff2b274e.webp" alt="" width={475} height={164} /></p>

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 七個 10/100/1000 千兆乙太網埠。
- 一個 2.5G 乙太網埠。
- 一個 10G SFP+ 埠。
- 一個 USB 3.0 type-A 埠。

## Reset 按鈕 {#reset-button}

RouterBOOT 重設按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 在 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。

無論使用上述哪種方式，如果在裝置接通電源之前就按住按鈕，系統將載入備用的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## LED {#led}

- Reset 按鈕後面的隱藏綠色 LED 是 USER LED
- 藍色 LED 1 是 DC1 電源 LED
- 藍色 LED 2 是 DC2 電源 LED
- 綠色 SFP+ LED 是 SFP+ 埠的連線和活動 LED
- 乙太網 RJ45 綠色 LED 是乙太網埠的連線和活動 LED
- 乙太網 RJ45 埠 1 的橙色 LED 是 PoE-in 狀態 LED
- 乙太網 RJ45 埠 2-8 的橙色 LED 在此型號上未使用

## 配件 {#accessories}

包裝中包含隨裝置提供的以下附件：

- ADAPT1_EU/US 開關電源 24V 1.5A 36W
- SET1_ K-55 緊固套裝
- PAD1_ 4 個墊片 D=7；H=1.5 mm，黑色，單面 3M988T 膠粘劑

受支援的 SFP 模組請參見 [MikroTik 有線介面相容性](/docs/wired-connections/mikrotik-wired-interface-compatibility)表。

## 規格 {#specifications}

- CPU：88F7040 1.4 GHz。
- CPU 架構：ARM 64-bit。
- CPU 核心數：4。
- RAM 容量：1 GB。
- RAM 型別：DDR4。
- 儲存：1 GB，NAND。
- 1G 乙太網埠數量：7。
- 2.5G 乙太網埠數量：1。
- 10G SFP+ 埠數量：1。
- USB 埠：1（3.0 type A）。
- 作業系統：RouterOS（License level 5）。
- 交換晶片型號：88E6393。
- 尺寸：220 x 125 x 22 mm。
- 工作溫度：-40°C 至 +60°C。

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/rb5009ug_s_in](https://mikrotik.com/product/rb5009ug_s_in)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 安全提示 {#safety-notice}

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置點。請了解您所在地區將裝置妥善運輸至指定處置點的相關程式。
