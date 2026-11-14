---
title: "L009UiGS-RM"
slug: /l009uigs-rm
source: https://manual.mikrotik.com/hardware/l009uigs-rm
captured_at: '2026-11-04T05:59:31+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/829210e28aa7893b.jpg" alt="" width={799} height={296} /></p>

## [L009UiGS-RM](https://mikrotik.com/product/l009uigs_rm) {#l009uigs-rm}

L009 不僅僅是一臺路由器。該產品線比 RB2011 快達 4 倍，配備支援容器的現代 ARM CPU、創新的外殼設計，可在單個 1U 空間內安裝多達四臺路由器，並擁有更大的 RAM、PoE 和 2.5G SFP 支援。此版本附帶 1U 機架安裝配件。完整規格和手冊請參見 [L009UiGS-RM 產品頁面](https://mikrotik.com/product/l009uigs_rm)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應依照所有國家法律法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 確保您的 ISP 允許硬體變更，並會自動分配 IP 地址；
- 將 ISP 線纜連線到第一個乙太網埠；
- 將您的 PC 連線到任意一個乙太網埠；
- 將裝置連線到電源；
- 將網路卡設定為使用 DHCP 自動獲取 IP 地址；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 完成。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 以開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中，選擇您所在的國家以應用國家法規設定；
- 設定路由器密碼。

## 供電 {#powering}

最大負載下的功耗可達 40 W。裝置可從電源插孔或第一個乙太網埠獲取電源：

- 直流輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 24-56 V DC。
- 第一個乙太網埠支援 Power over Ethernet 802.3af/at。
- 側面的 2 引腳端子接受 24-56 V DC。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線纜連線到 PoE 介面卡的 PoE 埠；
- 將來自您 LAN 的乙太網線纜連線到 PoE 介面卡的 LAN 埠，注意資料和電力流向的箭頭；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help) 開始，以熟悉各種可能性。如果無法建立 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都會被阻止）。為便於恢復，可以從網路引導裝置，請參閱復位按鈕部分。

## 安裝 {#mounting}

本裝置設計用於室內使用，可以安裝在牆上，也可以放置在桌面上。

<p><Img src="/img/c9aa03e44924a564.webp" alt="" width={1600} height={828} /></p>

- 如圖所示，在裝置兩側找到設計的安裝孔；
- 使用隨附的螺絲將裝置固定到牆上；
- 根據牆體材料，您可以使用鑽頭和隨附的膨脹管。

本裝置沒有防水保護，請確保將裝置放置在乾燥通風的環境中。我們建議為我們的裝置使用 Cat6 線纜。*本裝置的安裝和配置應由合格人員完成。*

## 機架安裝 {#rackmount}

如果需要採用機架安裝方式，可另行購買額外的支架：

### RB5009/L009 機架安裝套件 K-79 {#rb5009l009-rackmount-kit-k-79}

<p><Img src="/img/d12c6eeeff2b274e.webp" alt="" width={475} height={164} /></p>

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 八個 10/100/1000 千兆乙太網埠。
- 一個 2.5G SFP 埠。
- 一個 USB 3.0 type-A 埠。
- RJ45 序列埠控制檯埠。
- Ether1 上的 PoE-in 和 Ether8 上的 PoE-out。

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置復位為預設值。
- 在 LED 熄滅後（約 20 秒）鬆開按鈕，可讓裝置查詢 Netinstall 伺服器（透過 Ether1 從網路重新安裝 RouterOS 時需要）。

無論使用上述哪種方式，如果在裝置接通電源之前按住按鈕，系統都將載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## LED {#led}

- 復位按鈕後面的隱藏綠色 LED 是 USER LED
- 藍色 LED 1 是 DC1 電源 LED
- 藍色 LED 2 是 DC2 電源 LED
- 綠色 SFP LED 是 SFP 埠鏈路和活動 LED
- 乙太網 RJ45 綠色 LED 是乙太網埠 1Gbps 鏈路和活動 LED
- 乙太網 RJ45 埠 1 的橙色 LED 是 PoE-in 狀態 LED
- 乙太網 RJ45 埠 2-8 的橙色 LED 僅表示 100Mbps

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- ADAPT1_EU/US 開關電源 24V 1.5A 36W
- SET1_ K-55 固定套件
- PAD1_ 4 個墊片 D=7；H=1.5 mm，單面膠 3M988T

請參見 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 規格 {#specifications}

- CPU：IPQ-5018 800 MHz。
- CPU 架構：ARM。
- CPU 核心數：2。
- RAM 容量：512 MB。
- RAM 型別：DDR3L。
- 儲存：128 MB，NAND。
- 1G 乙太網埠數量：8。
- 2.5G SFP 埠數量：1。
- USB 埠：1（3.0 type A）。
- PoE-in：Ether1。
- PoE-out：Ether8。
- 序列埠控制檯埠：RJ45。
- 作業系統：RouterOS（License level 5）。
- 交換晶片型號：88E6190。
- 尺寸：220 x 125 x 22 mm。
- 工作溫度：-40°C 至 +70°C。
- IP 防護等級：IP20。

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/l009uigs_rm](https://mikrotik.com/product/l009uigs_rm)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 安全提示 {#safety-notice}

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處理，例如送至指定的廢棄物處理場所。請了解您所在地區將裝置正確運送至指定處理場所的相關程式。
