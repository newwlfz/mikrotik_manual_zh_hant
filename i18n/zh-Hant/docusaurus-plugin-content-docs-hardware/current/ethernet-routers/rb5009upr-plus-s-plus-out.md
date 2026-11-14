---
title: "RB5009UPr+S+OUT"
slug: /rb5009upr-plus-s-plus-out
source: https://manual.mikrotik.com/hardware/rb5009upr-plus-s-plus-out
captured_at: '2026-11-04T06:04:08+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/011a389be62b7e0a.jpg" alt="" width={589} height={799} /></p>

## [RB5009UPr+S+OUT](https://mikrotik.com/product/rb5009_out) {#rb5009uprsout}

我們最暢銷的過載 PoE 路由器的戶外版本。以最優價格提供充分的電源冗餘！7 個千兆乙太網埠、1 個 2.5 千兆乙太網埠、10G SFP+、1GB 記憶體、1GB NAND、現代四核 CPU、9（！）種供電選項、耐用的 IP66 防水外殼。完整規格和宣傳冊請參見 [RB5009UPr+S+OUT 產品頁面](https://mikrotik.com/product/rb5009_out)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置為戶外使用而設計。開始安裝前請仔細閱讀安裝說明。使用不正確的硬體或不遵循正確的操作步驟，可能會對人員造成危險情況並對系統造成損壞。
- 只能使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置出現故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員進行安裝。

## 快速開始 {#quickstart}

- 確保您的 ISP 允許硬體變更並會自動分配 IP 地址；
- 將您的 ISP 網線連線到第一個乙太網埠；
- 將您的 PC 連線到任意一個乙太網埠；
- 將裝置連線到電源；
- 將您的網路卡設定為使用 DHCP 自動獲取 IP 地址；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方法以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

- PoE-in：802.3af/at。
- PoE-out：802.3af/at，與透過 2-pin 端子提供的電壓相同（被動 PoE）；如果使用 44-57 V 電源，則為相容 802.3af/at。
- PoE-out 埠：Ether1 - Ether8。當輸入低於 30 V 時，每埠最大輸出為 620 mA；當輸入高於 30 V 時，為 420 mA。
- 最大總輸出：2.59 A。
- 總輸出功率：130 W。
- 總輸出電流：2.28 A。
- 直流輸入數量：2。
- 支援的輸入電壓：24-57 V（PoE-in）和 24-57 V（2-pin 端子）。
- 無附加裝置時的最大功耗：15 W。
- 最大功耗：150 W。
- 2-pin 端子：Connector Plug P=5.08 mm 1x2pin RA TH，鍍錫，300 V 10 A。

## 配置 {#configuration}

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help) 開始，以熟悉這些功能。如果 IP 連線不可用，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參見復位按鈕。

## 安裝 {#mounting}

本裝置為戶外使用而設計，可安裝在牆壁或立杆上。請確保乙太網埠朝下。

我們建議為我們的裝置使用 Cat6 網線。

*本裝置的安裝和配置應由合格人員完成。為符合 **IP66** 等級，請嚴格遵守安裝說明中的規程。*

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 七個 10/100/1000 千兆乙太網埠，支援 PoE-in 和 PoE-out。
- 一個 2.5G 乙太網埠。
- 一個 10G SFP+ 埠。
- 一個 USB 3.0 type-A 埠。

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，可讓裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。

無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## LED {#led}

- 復位按鈕後面的隱藏綠色 LED 是 USER LED
- 藍色 LED 1 是 DC1 電源 LED
- 藍色 LED 2 是 DC2 電源 LED
- 綠色 SFP+ LED 是 SFP+ 埠的鏈路和活動 LED
- 乙太網 RJ45 綠色 LED 是乙太網埠的鏈路和活動 LED
- 乙太網 RJ45 埠 1 的橙色 LED 是 PoE-in 狀態 LED
- 乙太網 RJ45 埠 2-8 的橙色 LED 在此型號上未使用

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

<p><Img src="/img/ca4b47fd9b0e4896.webp" alt="" width={553} height={236} /></p>

支援的 SFP 模組請參見 [MikroTik 有線介面相容性](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。

## 規格 {#specifications}

- CPU：四核 88F7040 1.4 GHz。
- CPU 架構：ARM 64 位。
- 記憶體大小：1 GB。
- 記憶體型別：DDR4。
- 儲存：1 GB，NAND。
- 1G 乙太網埠數量：7。
- 2.5G 乙太網埠數量：1。
- 10G SFP+ 埠數量：1。
- USB 埠：1 個（USB 3 type A）。
- 作業系統：RouterOS v7（License level 5）。
- 交換晶片型號：88E6393。
- 尺寸：222 x 239 x 57 mm。
- 工作溫度：-40°C 至 +70°C。

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/rb5009_out](https://mikrotik.com/product/rb5009_out)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

## 安全提示 {#safety-notice}

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解您所在地區將裝置妥善運輸至指定處置場所的相關規程。
