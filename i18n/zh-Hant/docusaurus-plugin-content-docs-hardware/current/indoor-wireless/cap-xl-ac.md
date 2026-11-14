---
title: "cAP XL ac"
slug: /cap-xl-ac
source: https://manual.mikrotik.com/hardware/cap-xl-ac
captured_at: '2026-11-04T05:55:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/21e1d856fbf13621.jpg" alt="" width={799} height={666} /></p>

## [cAP XL ac](https://mikrotik.com/product/cap_xl_ac)（RBcAPGi-5acD2nD-XL） {#cap-xl-ac-rbcapgi-5acd2nd-xl}

效能強悍的吸頂 AP！我們最暢銷的 cAP 回來了——更強勁、更出色。與之前的 cAP 型號相比，改進的高增益天線將覆蓋面積提升多達 100%！完整規格和宣傳冊請參見 [cAP XL ac 產品頁面](https://mikrotik.com/product/cap_xl_ac)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣線路相關危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置安裝必須符合當地和國家電氣規範。
- 本裝置適用於機架安裝。開始安裝前，請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確程式，可能對人員造成危險情況並對系統造成損壞。
- 本產品適用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和配件。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。

**射頻輻射暴露：**本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。安裝和操作本 MikroTik 裝置時，應與身體、職業使用者或普通公眾保持不少於 20 釐米的距離。

## 設定 {#setup}

- 確保你的網際網路服務提供商 (ISP) 允許硬體更換並自動分配 IP 地址；
- 將 ISP 線纜連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 以外的任意埠，或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用 [https://mt.lv/winbox](https://mt.lv/winbox) 上的 "WinBox" 配置工具。**提供多種配置方法以確保可連線性；**
- 使用預設 IP 地址 192.168.88.1 在所選的工具中開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）；
- 單擊 "Check for updates" 按鈕，並將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇你的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇你的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

產品程式碼 RBcAPGi-5acD2nD-XL

- CPU 四核 IPQ-4018 710 MHz
- RAM 大小 128 MB
- RAM 型別 DDR3L
- 儲存 16 MB，Flash
- 1G 乙太網埠數量 2
- 無線 2.4 GHz 5 GHz
- 支援的協定 802.11b/g/n 802.11a/n/ac
- 天線增益 6 dBi 5,5 dBi
- 鏈數量 2
- 作業系統 RouterOS（許可證級別 4）
- 交換晶片型號 IPQ-4018
- 尺寸 191 x 42 mm
- 工作溫度 -40°C 至 +70°C

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種啟動選項可用：**Regular Booter** 和 **Backup Booter**。建議在其中一個選項不可用時驗證兩個選項。

- **Regular Booter:** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter:** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。取決於型號，這可能由 **USR、USER、System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統都將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 模式按鈕 {#mode-button}

本裝置上有兩個模式按鈕，但它們執行相同的動作。可透過 RouterOS 軟體配置模式按鈕的動作，以執行任何使用者提供的 RouterOS 指令碼。你也可以停用此按鈕。預設情況下，這些按鈕會啟用 "dark mode"，從而停用蜂鳴聲和 LED 燈。可在 RouterOS 選單 /system routerboard mode-button 中配置模式按鈕。

## LED 指示燈 {#led-indicators}

<p><Img src="/img/ae0fc84c535b6e65.webp" alt="" width={587} height={649} /></p>

裝置上有七個 LED 燈，如有必要可將其全部停用。

- User – 可由使用者配置、用於任意所需指令碼的 LED。
- 5G – 5GHz 介面活動。
- 2G – 2.4 GHz 介面活動。
- E2 – Ethernet 2 已連線。
- E1 – Ethernet 1 已連線。
- PoE LED 表示 ETH2 埠當前正在透過 PoE 為另一臺裝置供電。
- 電源 LED 表示裝置正在透過 ETH1 埠接收供電。

## 配件 {#accessories}

包裝內包含隨裝置提供的以下配件：

- ADAPT1_ EU/US 開關電源 24V，1.2A。
- POE1_ 千兆 POE 注入器。
- BRAC1_ CAPGB 安裝支架。
- 螺絲套裝：2 顆螺絲和安裝用膨脹螺栓。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

- 掃描二維條碼並選擇你偏好的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將已填寫。
- 單擊 Connect 以透過無線網路建立到裝置的連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導你完成所有基本配置設定。
- 還提供高階選單，可完整配置所有必要設定。

## 注意事項 {#notice}

- 任何裝置的資料表均可在製造商官方網站上獲取。
- 對於某些型號，請檢視貼紙上的使用者密碼和無線密碼。
- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 請確保裝置具有鎖定軟體包（製造商提供的韌體版本），必須將其應用到終端使用者裝置上，以防止終端使用者重新配置。產品將標有國家/地區程式碼 “-EG” - RBcAPGi-5acD2nD-XL-EG。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 埃及法規韌體的無線頻率範圍限制為 2.400 – 2.4835 GHz，TX 功率限制為 20dBm (EIRP)。
- 埃及法規韌體的無線頻率範圍限制為 5.150 – 5.250 GHz，TX 功率限制為 23dBm (EIRP)。
- 埃及法規韌體的無線頻率範圍限制為 5.250 – 5.350 GHz，TX 功率限制為 20dBm (EIRP)。此裝置需要升級到最新版本，以確保符合當地主管部門法規！終端使用者有責任遵守當地國家法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝。

為避免環境汙染，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定廢物處置場所。請熟悉將裝置正確運送到你所在地區指定處置場所的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>*RBcAPGi-5acD2nD-XL*-US</td><td>TV7CPGI52XL</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理保護，防止有害干擾。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：未經合規負責方明確批准的任何更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。

注意：本裝置已使用外圍裝置的遮蔽電纜進行測試。必須使用遮蔽電纜連線本裝置以確保合規。

**重要：射頻輻射暴露。**本裝置符合 FCC 針對非受控環境規定的輻射暴露限值。安裝和操作本裝置時，輻射體與身體任何部位之間應保持至少 20 cm 的距離。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>*RBcAPGi-5acD2nD-XL*-US</td><td>7442A-CPGI52XL</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。操作須符合以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置內含的免許可證發射器/接收器符合加拿大創新、科學與經濟發展部（ISED）針對免許可證無線電裝置適用的 CNR 標準。允許在以下兩個條件下執行：1）裝置不得產生干擾；2）裝置必須接受任何接收到的無線電干擾，即使該干擾可能導致裝置執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

在 5150–5250 MHz 頻段中操作的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

**重要：射頻輻射暴露。**本裝置符合 IC 針對非受控環境規定的輻射暴露限值。安裝和操作本裝置時，輻射體與身體任何部位之間應保持至少 20 cm 的距離。

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 MHz, 5150-5350 MHz, 5650-5850 MHz</td><td>≤10 W</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊位於其貼紙上的序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 MHz（20 dBm），5150-5250 MHz（23 dBm），5250-5350 MHz（20 dBm），5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBcAPGi-5acD2nD-XL 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率 (EIRP)**</th><th>**限制**</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均不受任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均不受任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告。

<p><Img src="/img/0561b3ba8c95a35c.webp" alt="" width={146} height={135} /></p>

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。
