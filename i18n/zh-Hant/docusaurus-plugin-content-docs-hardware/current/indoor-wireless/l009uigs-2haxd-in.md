---
title: "L009UiGS-2HaxD-IN"
slug: /l009uigs-2haxd-in
source: https://manual.mikrotik.com/hardware/l009uigs-2haxd-in
captured_at: '2026-11-04T05:59:31+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/30c72d3372d79f11.jpg" alt="" width={799} height={685} /></p>

## [L009UiGS-2HaxD-IN](https://mikrotik.com/product/l009uigs_2haxd_in)（L009UiGS-2HaxD-IN） {#l009uigs-2haxd-in-l009uigs-2haxd-in}

L009 不僅僅是一臺路由器。該產品線比 RB2011 快多達 4 倍，它採用現代 ARM CPU 並支援容器，創新的外殼允許在單個 1U 空間內安裝多達四臺路由器，擁有更大的 RAM、PoE 以及 2.5G SFP 支援。此版本配備 2.4 GHz ax 雙鏈無線。完整規格和宣傳冊請參閱 [L009UiGS-2HaxD-IN 產品頁面](https://mikrotik.com/product/l009uigs_2haxd_in)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置旨在安裝於機架中。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的步驟可能會給人員帶來危險情況，並損壞系統。
- 本產品僅供室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 插座應安裝在裝置附近且易於觸及。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座上拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 設定 {#setup}

- 確保您的網際網路服務提供商（ISP）允許硬體更改並自動分配 IP 地址；
- 將 ISP 線纜連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 以外的任意埠，或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用位於 [https://mt.lv/winbox](https://mt.lv/winbox) 的 "WinBox" 配置工具。**提供多種配置方法以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您所在的國家/地區，以應用該國家/地區的法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 供電 {#powering}

最大負載下的功耗可達 47 W。裝置可從電源插孔或第一個乙太網埠接受供電：

- 直插式電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 24-56 V DC。
- 第一個乙太網埠支援 Power over Ethernet 802.3af/at。
- 側面的 2 針端子接受 24-56 V DC。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網線纜連線到 POE 介面卡的 POE 埠。
- 將來自您 LAN 的乙太網線纜連線到 POE 介面卡的 LAN 埠，請注意資料與電力流向的箭頭。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕。將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將要使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以讓裝置引導以進行重新安裝，請參閱按鈕和跳線部分。

## 安裝 {#mounting}

本裝置設計用於室內，可安裝在牆上，也可以放置在桌面上。

<p><Img src="/img/6c6197919537348e.webp" alt="" width={1600} height={1801} /></p>

- 如圖所示，找到裝置兩側設計的安裝孔；
- 使用隨附的螺釘將裝置固定到牆上；
- 根據牆體材質，您可以使用鑽頭和隨附的膨脹螺栓。本裝置不具備防水汙染保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 線纜。*本裝置的安裝和配置應由合格人員完成。*

## 機架安裝 {#rackmount}

如果希望採用機架安裝，可單獨購買額外的支架：

### RB5009/L009 機架安裝套件 K-79 {#rb5009l009-rackmount-kit-k-79}

<p><Img src="/img/d12c6eeeff2b274e.webp" alt="" width={475} height={164} /></p>

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼 L009UiGS-2HaxD-IN
- CPU IPQ-5018 800 MHz
- CPU 架構 ARM
- CPU 核心數 2
- RAM 大小 512 MB
- RAM 型別 DDR3L
- 儲存 128 MB，NAND
- 1G 乙太網埠數量 8
- 2.5G SFP 埠數量 1
- USB 埠 1（3.0 type A）
- PoE-in Ether1
- PoE-out Ether8
- 序列控制檯埠 RJ45
- 作業系統 RouterOS（License level 5）
- 交換晶片型號 88E6190
- 無線介面型號 IPQ-5018（2.4 GHz）
- 無線 2.4 GHz 802.11b/g/n/ax 雙鏈
- 無線天線最大增益 2.4 GHz（4 dBi）
- 尺寸 220 x 125 x 22 mm
- 工作溫度 -40°C 至 +70°C
- IP 20

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開即可啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。提供兩種 booter 選項：**Regular Booter** 和 **Backup Booter**。建議在其中一個不起作用時對兩個選項都進行驗證。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後為裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將引導進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。視型號而定，這可能由 **USR、USER、System** 或 **ACT** LED，或由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## LED {#led}

- Reset 按鈕後面的隱藏綠色 LED 是 USER LED
- 藍色 LED 1 是 DC1 電源 LED
- 藍色 LED 2 是 DC2 電源 LED
- 綠色 SFP LED 是 SFP 埠鏈路和活動 LED
- 乙太網 RJ45 綠色 LED 是乙太網埠 1Gbps 鏈路和活動 LED
- 乙太網 RJ45 埠 1 的橙色 LED 是 PoE-in 狀態 LED
- 乙太網 RJ45 埠 2-8 僅橙色 LED - 100Mbps

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- ADAPT1_EU/US 開關電源 24V 1.5A 36W
- SET1_ K-55 緊固套件
- PAD1_ 4 個墊片 D=7；H=1.5 mm，單面膠 3M988T 有關支援的 SFP 模組，請參閱 [MikroTik 有線介面相容性](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將本裝置與家庭垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請了解將裝置正確運輸到您所在地區指定處置場所的相關程式。
