---
title: "hAP ac3"
slug: /hap-ac3
source: https://manual.mikrotik.com/hardware/hap-ac3
captured_at: '2026-11-04T05:58:20+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/a1300d1f5847a368.jpg" alt="" width={799} height={571} /></p>

## [hAP ac³](https://mikrotik.com/product/hap_ac3) (RBd53iG-5HacD2HnD) {#hap-ac-rbd53ig-5hacd2hnd}

一款無線雙頻路由器，具有 5 個千兆乙太網埠和外部高增益天線，可提供更廣覆蓋。請參閱 [hAP ac³ 產品頁面](https://mikrotik.com/product/hap_ac3) 以獲取完整規格和宣傳冊。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本裝置擬安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確程式可能會對人員造成危險情況，並損壞系統。
- 本產品擬在室內安裝。請將本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商批准的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證不會因裝置使用不當而發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- **未連線天線時請勿通電！**
- 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝。

## 設定 {#setup}

- 確保您的網際網路服務提供商（ISP）允許硬體更改並自動分配 IP 地址；
- 將 ISP 線纜連線到 Ethernet1 埠；
- 將裝置連線到電源，並在通電前將隨附天線連線到裝置；
- 透過除 Ethernet1 以外的任意埠或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在 Web 瀏覽器中使用 WebFig，或使用位於 [https://mt.lv/winbox](https://mt.lv/winbox) 的 "WinBox" 配置工具。**提供多種配置方法以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 單擊 "Check for updates" 按鈕並將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱將已輸入。
- 單擊 Connect 透過無線網路與您的裝置建立連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完全配置所有必要設定。

## 供電 {#powering}

裝置可透過介面卡和 PoE 供電：

- 直流輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）12-28 V DC⎓。
- **Ethernet 1 上的 PoE 輸入 18-28 V DC⎓**。最大負載下的功耗可達 12 W，帶附件時為 30 W。

## 底板安裝說明 {#base-plate-mounting-instruction}

- 底板隨包裝附帶，如需組裝，請遵循以下說明。
- 將底板的小尖端插入裝置底部的殼體中，然後向下摺疊。

<p><Img src="/img/b08358f3fffd9cc3.webp" alt="" width={900} height={286} /></p>

- 雙手握住時，用手指輕輕按壓並向下推，直到鎖定，按照圖示順序操作。

<p><Img src="/img/59f1995ab09b5790.webp" alt="" width={900} height={295} /></p>

## 配置 {#configuration}

登入後，我們建議單擊 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。請確保您已選擇裝置將使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以將裝置引導以進行重新安裝，請參閱按鈕和跳線。

首次配置 [https://mt.lv/configuration](https://mt.lv/configuration)；

裝置升級 [https://mt.lv/upgrade](https://mt.lv/upgrade)；

## 安裝 {#mounting}

本裝置設計用於室內，放置在平坦表面上，所有所需線纜連線到裝置背面。

可使用隨附螺釘將安裝底座固定到牆上：

- 使用隨附螺釘將底座固定到牆上；

<p><Img src="/img/e50527a302675fcd.webp" alt="" width={170} height={200} /></p>

- 按照底板部分的前述說明，將裝置安裝到安裝底座上。*為確保最佳效能，請確保良好的空氣流通，並將裝置放置在開闊空間的支架上。* 警告！本裝置應在裝置與身體之間至少保持 20 cm 距離的情況下安裝和操作。在住宅環境中操作本裝置可能會造成無線電干擾。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通或交叉線纜連線到其他網路裝置。
- 整合無線 5GHz、802.11a/n/ac 和 2.4 GHz b/g/n。
- USB 埠。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三項功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。提供兩種啟動器選項：**Regular Booter** 和 **Backup Booter**。建議驗證兩個選項，以防其中一個無法工作。

- **Regular Booter：** 要進入 etherboot 模式，請在給裝置通電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置通電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。根據型號不同，這可能會由 **USR, USER, System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

無論使用上述哪個選項，如果在裝置通電前按下按鈕，系統都將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

**模式按鈕** 可執行使用者新增的自定義指令碼。

**前部藍色 LED 按鈕** 可啟用 WPS 模式。

## 配件 {#accessories}

包裝內包含以下隨裝置附帶的配件：

<p><Img src="/img/577b29c31902f682.webp" alt="" width={917} height={230} /></p>

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列在 /system resource 中。其他作業系統尚未測試。

## 注意 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置使用的範圍與上述法規不同，則需要向終端使用者裝置應用來自制造商/供應商的自定義韌體版本，並防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料表可在製造商官方網站上獲取。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，TX 功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，TX 功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，TX 功率限制為 20dBm（EIRP）。

請確保裝置具有鎖定軟體包（來自制造商的韌體版本），需要將其應用到終端使用者裝置，以防止終端使用者重新配置。產品將標有國家/地區程式碼 “-EG”。本裝置需要升級到最新版本，以確保符合當地主管部門法規！終端使用者有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBD53iG-5HacD2HnD-US</td><td>TV7D53I-5ACD2ND</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理保護，防止有害干擾。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一項或多項措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所在電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改都可能使使用者操作本裝置的許可權失效。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：（1）本裝置不得造成有害干擾，並且（2）本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。

注意：本裝置在測試時使用了遮蔽電纜連線外圍裝置。為確保合規，必須使用遮蔽電纜連線本裝置。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的輻射暴露限制。安裝和操作本裝置時，輻射體與身體任何部位之間應至少保持 20 cm 的距離。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBD53iG-5HacD2HnD-US</td><td>7442A-D53IAC</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：（1）本裝置不得造成干擾。（2）本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

在 5150–5250 MHz 頻段執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限制。安裝和操作本裝置時，輻射體與身體任何部位之間應至少保持 20 cm 的距離。

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射器功率</th></tr></thead><tbody><tr><td>2400-2483.5 MHz，5150-5350 MHz，5650-5850 MHz</td><td>≤10 W</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊位於其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

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

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 MHz（20 dBm），5150-5250 MHz（23 dBm），5250-5350 MHz（20 dBm），5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBD53iG-5HacD2HnD 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均不受任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均不受任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更詳細的資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參閱上文的符合性宣告。

<p><Img src="/img/0561b3ba8c95a35c.webp" alt="" width={146} height={135} /></p>

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。
