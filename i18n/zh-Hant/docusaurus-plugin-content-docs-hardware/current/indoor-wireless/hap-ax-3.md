---
title: "hAP ax³"
slug: /hap-ax-3
source: https://manual.mikrotik.com/hardware/hap-ax-3
captured_at: '2026-11-04T05:58:22+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/561579768b8027f5.jpg" alt="" width={799} height={646} /></p>

## [hAP ax³](https://mikrotik.com/product/hap_ax3) (C53UiG+5HPaxD2HPaxD) {#hap-ax-c53uig5hpaxd2hpaxd}

我們頂級的 AX 家用接入點。擁有您的家庭可能需要的全部處理能力和速度。第 6 代無線、2.5 千兆乙太網、PoE、WPA3 等！完整規格和宣傳冊請參閱 [hAP ax³ 產品頁面](https://mikrotik.com/product/hap_ax3)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品僅供室內安裝。請將本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證不會因不當使用裝置而發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座上拔下電源插頭。
- 客戶有責任遵守當地國家/地區法規，包括在法律允許的頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 37 釐米。

## 設定 {#setup}

- 在將裝置連線到電源之前，請先將隨機提供的天線安裝到裝置上；
- 確保您的網際網路服務提供商（ISP）允許硬體變更並自動分配 IP 地址；
- 將 ISP 線纜連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 以外的任意埠或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，使用網頁瀏覽器中的 WebFig，或使用位於 [https://mt.lv/winbox](https://mt.lv/winbox) 的 "WinBox" 配置工具。**提供多種配置方法以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，並且沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 "Check for updates" 按鈕，並將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性以及安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您的國家/地區，以應用該國家/地區的法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

要獲取**密碼**，請拉出產品資訊附近的卡片佔位符。

<p><Img src="/img/6e51537220ef1d68.webp" alt="" width={471} height={254} /></p>

## 供電 {#powering}

- DC 輸入數量 2（PoE-in、DC 插孔）
- PoE-in 輸入電壓 18-28 V
- DC 插孔輸入電壓 12-28 V
- PoE-out 被動 PoE Ether1，每埠最大輸出（輸入 &lt; 30 V）：0.625 A
- PoE-out 總輸出功率 15 W
- 電源介面卡標稱電壓 24 V
- 電源介面卡標稱電流 1.5 A
- 最大功耗（不含附件）15 W
- 最大功耗 38 W

## 配置 {#configuration}

我們建議點選 "Check for updates" 按鈕，並將您的 RouterOS 軟體更新到最新版本，以確保獲得最佳效能和穩定性。除了本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參見按鈕和跳線。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼 C53UiG+5HPaxD2HPaxD
- CPU 四核 IPQ-6010 1.8 GHz
- CPU 架構 ARM 64bit
- 記憶體大小 1 GB
- 儲存 128 MB，NAND
- 1G 乙太網埠數量 4
- 2.5G 乙太網埠數量 1（支援 PoE-in/out）
- USB 1 個 USB 3 type A
- 交換晶片型號 IPQ-6010
- 無線介面型號 QCN-5022（2.4 GHz）、QCN-5052（5 GHz）
- 無線 2.4 GHz 802.11b/g/n/ax 雙鏈，5 GHz 802.11a/n/ac/ax 雙鏈
- 無線天線最大增益 2.4 GHz（3.3 dBi）、5 GHz（5.5 dBi）
- 尺寸 251 x 130 x 39 mm
- 作業系統 RouterOS，許可級別 6
- 工作溫度 -40°C 至 +70°C

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三個功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 工具重新安裝 RouterOS，請使裝置進入 BOOTP 模式。有兩種載入程式選項可用：**Regular Booter** 和 **Backup Booter**。建議對這兩個選項都進行驗證，以防其中一個無法工作。

- **Regular Booter：** 要進入 etherboot 模式，請在給裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將引導進入 **BOOTP** 模式，準備好透過 **Netinstall** 重新安裝 RouterOS。根據型號的不同，這可能會透過 **USR、USER、System** 或 **ACT** LED，或透過 SFP 埠 LED 來指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 配件 {#accessories}

<p><Img src="/img/8bd7e2036792b537.webp" alt="" width={886} height={290} /></p>

## 注意事項 {#notice}

- 任何裝置的資料表均可在製造商官方網站上獲取。
- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 請確保裝置帶有鎖定軟體包（來自制造商的韌體版本），需要將其應用到終端使用者裝置上，以防止終端使用者重新配置。產品將標有國家程式碼 "-EG" - C53UiG+5HPaxD2HPaxD-EG。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 埃及法規韌體的無線頻率範圍限制為 2.400 – 2.4835 GHz，TX 功率限制為 20dBm（EIRP）。
- 埃及法規韌體的無線頻率範圍限制為 5.150 – 5.250 GHz，TX 功率限制為 23dBm（EIRP）。
- 埃及法規韌體的無線頻率範圍限制為 5.250 – 5.350 GHz，TX 功率限制為 20dBm（EIRP）。本裝置需要升級到最新版本，以確保符合當地主管部門的法規！終端使用者有責任遵守當地國家/地區法規，包括在法律允許的頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢棄物處置場所。請熟悉您所在地區將裝置正確運送到指定處置場所的相關程式。

### 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>C53UiG+5HPaxD2HPaxD-US</td><td>TV7C53-5AXD2AXD</td></tr></tbody></table>

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝中的有害干擾提供合理的防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來確定），則建議使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 請諮詢經銷商或有經驗的無線電/電視技術人員以獲取幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。其執行需滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。

注意：本機在測試時對外圍裝置使用了遮蔽電纜。為確保合規，必須使用遮蔽電纜連線本機。

批准的 2.4 GHz 天線：

-

3.36 dBi 全向（HGO-antenna-IN）批准的 5 GHz 天線：

-

6.01 dBi 全向（HGO-antenna-IN）**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC 針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 37 釐米。

### 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>C53UiG+5HPaxD2HPaxD-US</td><td>7442A-C53AX</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。其執行需滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。

本裝置內含的免許可證發射器/接收器符合加拿大創新、科學與經濟發展部（ISED）針對免許可證無線電裝置適用的 CNR 標準。允許在以下兩個條件下執行：1）裝置不得產生干擾；2）裝置必須接受任何接收到的無線電干擾，即使該干擾可能導致裝置執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

在 5150–5250 MHz 頻段內執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

批准的 2.4 GHz 天線：

-

3.36 dBi 全向（HGO-antenna-IN）批准的 5 GHz 天線：

-

6.01 dBi 全向（HGO-antenna-IN）**射頻輻射暴露：** 本 MikroTik 裝置符合 IC 針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 37 釐米。

本裝置符合 IC 針對非受控環境所規定的輻射暴露限值。本裝置安裝和使用時，輻射源與您身體之間應保持至少 37cm 的距離。

### UKCA 標誌 {#ukca-marking}

<p><Img src="/img/387853c20d5a4c82.gif" alt="" width={2115} height={2113} /></p>

### CE 符合性宣告 {#ce-declaration-of-conformity}

<table><thead><tr><th>*BG*</th><th>Mikrotīkls SIA 特此宣告，此型號無線電裝置 C53UiG+5HPaxD2HPaxD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</th></tr></thead><tbody><tr><td>CS</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型號 C53UiG+5HPaxD2HPaxD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DA</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DE</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EL</td><td>Mikrotīkls SIA 特此宣告，無線電裝置 C53UiG+5HPaxD2HPaxD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EN</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ES</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ET</td><td>Mikrotīkls SIA 特此宣告，此無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/EL 指令的要求。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FI</td><td>Mikrotīkls SIA 宣告，無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FR</td><td>簽署方 Mikrotīkls SIA 宣告，C53UiG+5HPaxD2HPaxD 型無線電裝置符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HR</td><td>Mikrotīkls SIA 特此宣告，C53UiG+5HPaxD2HPaxD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HU</td><td>Mikrotīkls SIA 證明，C53UiG+5HPaxD2HPaxD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IT</td><td>製造商 Mikrotīkls SIA 宣告，C53UiG+5HPaxD2HPaxD 型無線電裝置符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IS</td><td>Mikrotīkls SIA 特此宣告，C53UiG+5HPaxD2HPaxD 符合 2014/53/EU 指令中規定的基本要求和其他要求。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LT</td><td>本人 Mikrotīkls SIA 確認，無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/ES 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LV</td><td>Mikrotīkls SIA 特此宣告，無線電裝置 C53UiG+5HPaxD2HPaxD 符合 2014/53/ES 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>MT</td><td>Mikrotīkls SIA 特此宣告，此無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NL</td><td>本人 Mikrotīkls SIA 特此宣告，C53UiG+5HPaxD2HPaxD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址查閱：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NO</td><td>Mikrotīkls SIA 特此宣告，C53UiG+5HPaxD2HPaxD 裝置符合 2014/53/EU 指令中的基本要求和其他相關要求。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PL</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PT</td><td>簽署方 Mikrotīkls SIA 宣告，本無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/UE 指令。符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>RO</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SK</td><td>Mikrotīkls SIA 特此宣告，C53UiG+5HPaxD2HPaxD 型無線電裝置符合 2014/53/EÚ 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SL</td><td>Mikrotīkls SIA 確認，C53UiG+5HPaxD2HPaxD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SV</td><td>Mikrotīkls SIA 特此保證，此無線電裝置型別 C53UiG+5HPaxD2HPaxD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr></tbody></table>

***WLAN***

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>WLAN 2.4 GHz</th><th>2400-2483.5 MHz / 20 dBm</th></tr></thead><tbody><tr><td>WLAN 5 GHz</td><td>5150-5250 MHz / 23 dBm</td><td></td></tr><tr><td>WLAN 5 GHz</td><td>5250-5350 MHz / 20 dBm</td><td></td></tr><tr><td>WLAN 5 GHz</td><td>5470-5725 MHz / 27 dBm</td><td></td></tr><tr><td>WLAN 5 GHz</td><td>5725-5850 MHz / 14 dBm</td><td></td></tr><tr><td>WLAN 5 GHz</td><td>5850-5895 MHz / 14 dBm</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。更多詳細資訊請參見上文的符合性宣告。

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。

<p><Img src="/img/33ffcd4c629d94d3.webp" alt="" width={1600} height={435} /></p>

<table><thead><tr><th>**技術規格：**</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>產品電源輸入選項</td><td>DC 介面卡輸出規格</td><td>外殼的 IP 等級</td><td>工作溫度</td><td></td></tr><tr><td>電壓，V</td><td>電流，A</td><td></td><td></td><td></td></tr><tr><td>DC 插孔（12 - 28 V DC）PoE 輸入乙太網埠（18 - 28 V DC）</td><td>24</td><td>1.5</td><td>IP20</td><td>±0° .. +70°C</td></tr></tbody></table>
