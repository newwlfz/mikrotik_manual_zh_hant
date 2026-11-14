---
title: "hAP ax²"
slug: /hap-ax-2
source: https://manual.mikrotik.com/hardware/hap-ax-2
captured_at: '2026-11-04T05:58:13+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/039ae3f4916c9df7.jpg" alt="" width={601} height={799} /></p>

## [hAP ax²](https://mikrotik.com/product/hap_ax2) (C52iG-5HaxD2HaxD-TC) {#hap-ax-c52ig-5haxd2haxd-tc}

傳奇 hAP ac² 的第六代版本。支援 PoE 輸入和 PoE 輸出，無線速度更快，記憶體更大，並採用現代 CPU。市面上最小巧的全功能 AX 路由器！完整規格和宣傳冊請參見 [hAP ax² 產品頁面](https://mikrotik.com/product/hap_ax2)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於安裝在機架上。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會對人員造成危險並對系統造成損壞。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 請僅使用製造商認可的電源和附件，這些均可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置出現故障，請將其與電源斷開。最快的斷開方式是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地的國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

**暴露於射頻輻射：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 供電 {#powering}

- 直流輸入數量 2（PoE-in、DC 插孔）
- PoE-in 輸入電壓 18-28 V
- DC 插孔輸入電壓 12-28 V
- PoE-out 被動 PoE Ether1，每埠最大輸出（輸入 &lt; 30 V）：600mA
- 最大總輸出 0.6 A
- 總輸出功率 16.8 W
- 電源介面卡標稱電壓 24 V
- 電源介面卡標稱電流 1.2 A
- 最大功耗（不含附加裝置）12 W
- 最大功耗 27 W

## 設定 {#setup}

- 確保您的網際網路服務提供商（ISP）允許硬體變更並自動分配 IP 地址；
- 將 ISP 線纜連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 之外的任意埠，或透過無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者使用網頁瀏覽器中的 WebFig，或 "WinBox" 配置工具：[https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法以確保可訪問性；**
- 使用預設 IP 地址 192.168.88.1，在所選工具中開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性以及安全更新；
- 在 "QuickSet" 選單中進行以下設定：選擇您的國家/地區，以應用該國法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 配置 {#configuration}

我們建議點選 "Check for updates" 按鈕，並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從此處開始熟悉這些可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問都會被阻止）。為便於恢復，可以從網路啟動裝置，請參見"按鈕和跳線"。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼 C52iG-5HaxD2HaxD-TC。
- CPU 四核 IPQ-6010 864 MHz。
- CPU 架構 ARM 64bit。
- 記憶體大小 1 GB。
- 儲存 128 MB，NAND。
- 1G 乙太網埠數量 5。
- 帶 PoE-out 的 1G 乙太網埠數量 1。
- 交換晶片型號 IPQ-6010。
- 無線介面型號 QCN-5052（2.4 GHz）、QCN-5052（5 GHz）。
- 無線 2.4 GHz 802.11ax 雙鏈、5 GHz 802.11 802.11ax 雙鏈。
- 無線天線最大增益 2.4 GHz（4.5 dBi）、5 GHz（4 dBi）。
- 尺寸 120 x 101 x 37 mm。
- 作業系統 RouterOS，許可證級別 4。
- 工作溫度 -40°C 至 +50°C。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種 booter 選項可用：**常規 Booter（Regular Booter）** 和 **備份 Booter（Backup Booter）**。如果其中一個選項不起作用，建議對兩個選項都進行驗證。

- **常規 Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **備份 Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。根據型號不同，這可能會透過 **USR、USER、System** 或 **ACT** LED，或 SFP 埠 LED 來指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復非常有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 注意事項 {#notice}

- 任何裝置的資料手冊均可在製造商官方網站上獲取。
- 對於某些型號，請檢視貼紙上的使用者和無線密碼。
- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 請確保裝置具有鎖定軟體包（製造商提供的韌體版本），該軟體包必須應用到終端使用者裝置，以防止終端使用者重新配置。產品將標有國家程式碼 "-EG" - C52iG-5HaxD2HaxD-TC-EG。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 埃及法規韌體的無線頻率範圍限制在 2.400 – 2.4835 GHz，TX 功率限制為 20dBm（EIRP）。
- 埃及法規韌體的無線頻率範圍限制在 5.150 – 5.250 GHz，TX 功率限制為 23dBm（EIRP）。
- 埃及法規韌體的無線頻率範圍限制在 5.250 – 5.350 GHz，TX 功率限制為 20dBm（EIRP）。本裝置需要升級到最新版本，以確保符合當地主管部門的法規！終端使用者有責任遵守當地的國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解您所在地區將裝置妥善運送到指定處置場所的程式。

### 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>C52iG-5HaxD2HaxD-TC-US</td><td>TV7C52-5AXD2AXD</td></tr></tbody></table>

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業環境安裝提供合理的有害干擾防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能導致有害干擾，此時使用者需自費消除干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不會造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。

注意：本裝置的外圍裝置使用遮蔽電纜進行測試。必須使用遮蔽電纜以確保合規。

**暴露於射頻輻射：** 本 MikroTik 裝置符合 FCC 針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 38 釐米。

**FCC 法規限制僅可在室內使用。**

### 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>C52iG-5HaxD2HaxD-TC-US</td><td>7442A-C52AX</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可證 RSS 的免許可證發射器/接收器。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置內含的免許可證發射器/接收器符合加拿大創新、科學與經濟發展部（ISED）針對免許可證無線電裝置適用的 CNR 標準。允許在以下兩個條件下執行：1）裝置不得產生干擾；2）裝置必須接受任何接收到的無線電干擾，即使該干擾可能導致裝置執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

在 5150–5250 MHz 頻段執行的裝置僅限室內使用，以減少對同通道移動衛星系統的潛在有害干擾。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

**暴露於射頻輻射：** 本 MikroTik 裝置符合 IC 針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 38 釐米。

**暴露於射頻輻射：** 本 MikroTik 裝置符合 IC 針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 38 釐米。

### UKCA 標誌 {#ukca-marking}

<p><Img src="/img/387853c20d5a4c82.gif" alt="" width={2115} height={2113} /></p>

### CE 符合性宣告 {#ce-declaration-of-conformity}

<table><thead><tr><th>BG</th><th>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</th></tr></thead><tbody><tr><td>CS</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DA</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DE</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EL</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EN</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ES</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ET</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FI</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FR</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HR</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HU</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IT</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IS</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LT</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LV</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>MT</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NL</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NO</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PL</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PT</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>RO</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SK</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SL</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SV</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 C52iG-5HaxD2HaxD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr></tbody></table>

### WLAN {#wlan}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>WLAN</th><th>2400-2483.5 MHz / 20dBm</th></tr></thead><tbody><tr><td>WLAN</td><td>5150-5250 MHz / 23 dBm</td><td></td></tr><tr><td>WLAN</td><td>5250-5350 MHz / 20 dBm</td><td></td></tr><tr><td>WLAN</td><td>5470-5725 MHz / 27 dBm</td><td></td></tr><tr><td>WLAN</td><td>5725-5850 MHz / 14 dBm</td><td></td></tr><tr><td>WLAN</td><td>5850-5895 MHz / 14 dBm</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大 TX 功率限值。更多詳細資訊請參見上文的符合性宣告。

當在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限於室內使用。

<p><Img src="/img/6250b391e18aff84.webp" alt="" width={1600} height={334} /></p>

僅限 5GHz 的相關限制

<table><thead><tr><th>**（EN）技術規格 /（DE）技術規格 /（FR）技術規格 /（IT）技術規格 /（ES）技術規格 /（RU）技術規格：**</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>（EN）產品電源輸入選項（DE）產品電源輸入選項（FR）產品電源輸入選項（IT）產品電源輸入選項（ES）產品電源輸入選項（RU）產品電源輸入選項</td><td>（EN）直流介面卡輸出規格（DE）直流介面卡輸出規格（FR）直流介面卡輸出規格（IT）直流介面卡輸出規格（ES）直流介面卡輸出規格（RU）直流介面卡輸出規格</td><td>（EN）外殼 IP 等級（DE）外殼 IP 等級（FR）外殼 IP 等級（IT）外殼 IP 等級（ES）外殼 IP 等級（RU）外殼 IP 等級</td><td>（EN）工作溫度（DE）工作溫度（FR）工作溫度（IT）工作溫度（ES）工作溫度（RU）工作溫度</td><td></td></tr><tr><td>電壓，V</td><td>電流，A</td><td></td><td></td><td></td></tr><tr><td>DC 插孔（12 - 28 V DC）PoE in Ethernet（18 - 28 V DC）</td><td>24</td><td>1.2</td><td>IP20</td><td>±0°..+50°C</td></tr></tbody></table>
