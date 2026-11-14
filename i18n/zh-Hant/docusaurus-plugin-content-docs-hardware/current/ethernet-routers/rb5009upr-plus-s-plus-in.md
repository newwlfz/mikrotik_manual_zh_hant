---
title: "RB5009UPr+S+IN"
slug: /rb5009upr-plus-s-plus-in
source: https://manual.mikrotik.com/hardware/rb5009upr-plus-s-plus-in
captured_at: '2026-11-04T06:04:04+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/9719c9879f45eaa4.jpg" alt="" width={799} height={471} /></p>

## [RB5009UPr+S+IN](https://mikrotik.com/product/rb5009upr_s_in) {#rb5009uprsin}

這是我們廣受歡迎的高負載 RB5009 路由器的新版本，所有埠均支援 PoE-in 和 PoE-out。非常適合中小型 ISP。2.5 Gigabit Ethernet 與 10 Gigabit SFP+，多種供電方式。完整規格和產品手冊請參見 [RB5009UPr+S+IN 產品頁面](https://mikrotik.com/product/rb5009upr_s_in)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家和地方法律法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 確保您的 ISP 允許硬體變更並會自動分配 IP 地址；
- 將您的 ISP 網線連線到第一個 Ethernet 埠；
- 將您的 PC 連線到任意 Ethernet 埠；
- 將裝置連線到電源；
- 將您的網路卡設定為使用 DHCP 自動獲取 IP 地址；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單中，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

最大負載下的功耗可達 150 W。裝置可從電源插孔、2 針端子或任意 Ethernet 埠取電：

- 直流輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 24-57 V DC。
- PoE-in：Ether1 上為 802.3af/at，Ether2-Ether8 上為 Mode B。
- 2 針端子輸入電壓：24-57 V DC。
- PoE-out 埠：Ether1 - Ether8。當輸入低於 30 V 時每埠最大輸出為 640 mA，當輸入高於 30 V 時為 440 mA。
- 最大總輸出：2.59 A。
- 總輸出功率：130 W。
- 總輸出電流：2.28 A。
- 2 針端子：Connector Plug P=5.08 mm 1x2pin RA TH，鍍錫，300 V 10 A。

Mode B：**Ethernet 埠 2 - 8**。引腳 4 和 5 = DC+，引腳 7 和 8 = DC-。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的 Ethernet 網線連線到 PoE 介面卡的 PoE 埠；
- 將來自您 LAN 的 Ethernet 網線連線到 PoE 介面卡的 LAN 埠，注意資料和電流流向的箭頭；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help)開始，以熟悉各種可能性。如果無法建立 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下，來自 Internet 埠的所有訪問均被阻止）。為便於恢復，可以從網路啟動裝置，請參見 Reset 按鈕。

## 安裝 {#mounting}

本裝置設計用於室內使用，可安裝在牆上，也可以放置在桌面上。

<p><Img src="/img/8a5382c1f81612f6.webp" alt="" width={556} height={298} /></p>

- 如附圖所示，在裝置兩側找到預留的安裝孔；
- 使用隨附的螺絲將裝置固定到牆上；
- 根據牆面材質，您可以使用鑽頭和隨附的膨脹螺栓。

本裝置不具備防水汙染保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 網線。*本裝置的安裝和配置應由合格人員進行。*

## 機架安裝 {#rackmount}

如果期望的安裝位置是機架，可單獨購買額外的支架：

### RB5009 機架安裝套件 K-79 {#rb5009-rackmount-kit-k-79}

<p><Img src="/img/d12c6eeeff2b274e.webp" alt="" width={475} height={164} /></p>

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 七個 10/100/1000 Gigabit Ethernet 埠，支援 PoE-in 和 PoE-out。
- 一個 2.5G Ethernet 埠。
- 一個 10G SFP+ 埠。
- 一個 USB 3.0 type-A 埠。

## Reset 按鈕 {#reset-button}

RouterBOOT reset 按鈕具有以下功能。按下按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，即可將 RouterOS 配置重設為預設值。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路安全重灌 RouterOS 時需要）。

無論使用上述哪種選項，如果在裝置接通電源之前就按下按鈕，系統將載入備份的 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## LED {#led}

- Reset 按鈕後面的隱藏綠色 LED 是 USER LED
- 藍色 LED 1 是 DC1 電源 LED
- 藍色 LED 2 是 DC2 電源 LED
- 綠色 SFP+ LED 是 SFP+ 埠鏈路和活動 LED
- Ethernet RJ45 綠色 LED 是 Ethernet 埠鏈路和活動 LED
- Ethernet RJ45 埠 1 的橙色 LED 是 PoE-in 狀態 LED
- Ethernet RJ45 埠 2-8 的橙色 LED 在此型號上未使用

## 配件 {#accessories}

包裝中包含隨裝置提供的以下配件：

- ADAPT1_EU/US 開關電源 48V 2A。
- SET1_ K-55 緊固套件。
- PAD1_ 4 個墊片 D=7；H=1.5 mm，黑色，單面 3M988T 膠粘

支援的 SFP 模組請參見 [MikroTik 有線介面相容性](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。

## 規格 {#specifications}

- CPU：88F7040 1.4 GHz。
- CPU 架構：ARM 64-bit。
- CPU 核心數：4。
- RAM 容量：1 GB。
- RAM 型別：DDR4。
- 儲存：1 GB，NAND。
- 1G Ethernet 埠數量：7。
- 2.5G Ethernet 埠數量：1。
- 10G SFP+ 埠數量：1。
- USB 埠：1（3.0 type A）。
- 作業系統：RouterOS（License level 5）。
- Switch 晶片型號：88E6393。
- 尺寸：220 x 125 x 22 mm。
- 工作溫度：-40°C 至 +60°C。

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/rb5009upr_s_in](https://mikrotik.com/product/rb5009upr_s_in)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 安全提示 {#safety-notice}

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置妥善運送至指定處置場所的相關程式。
