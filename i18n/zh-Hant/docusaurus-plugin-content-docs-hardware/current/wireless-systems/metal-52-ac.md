---
title: "Metal 52 ac"
slug: /metal-52-ac
source: https://manual.mikrotik.com/hardware/metal-52-ac
captured_at: '2026-11-04T09:56:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/fa3177f820e53e92.jpg)

## [Metal 52 ac](https://mikrotik.com/product/RBMetalG-52SHPacn) (RBMetalG-52SHPacn) {#metal-52-ac-rbmetalg-52shpacn}

RBMetalG-52SHPacn Metal 出廠時預裝在室外機殼中，內建無線介面、一個 N-Male 天線接頭，以及一個支援 MDI-X 自動檢測的 10/100/1000 乙太網介面。該裝置包裝內附帶 24 V 電源介面卡、PoE 注入器和兩個安裝環。提供多種型號（雙頻、單頻、AP 和 CPE 變體）。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本產品適合安裝在室外立杆上。開始安裝前，請仔細閱讀安裝說明。使用錯誤的硬體和配置或未遵循正確程式，可能導致人員處於危險境地並對系統造成損壞。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和附件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座拔下電源插頭。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，應與您的身體、職業使用者或公眾保持至少 20 釐米的距離。

## 快速開始 {#quickstart}

- 將天線連線到 N-Male 接頭（參見天線使用）；
- 開啟乙太網埠蓋（參見開啟乙太網蓋）；
- 將線纜穿過蓋子並連線到乙太網埠（參見開啟乙太網蓋）；
- 裝置接受來自 PoE 注入器的 10-30 V Passive PoE。隨附的注入器應將 "Data" 端連線到 PC，"Data + Power" 埠應使用所需長度的乙太網線纜（未附帶）連線到裝置；
- 使用隨附的橡膠絕緣件套在乙太網線纜上，並將其推入外殼開口，使開口緊密封閉；
- 使用乙太網線纜將裝置連線到隨附 PoE 注入器的 data+power 端；
- 將 PoE 注入器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 透過 **WebFig** 或 **WinBox** 工具在 [https://mt.lv/winbox](https://mt.lv/winbox) 使用 Web 瀏覽器配置裝置。**提供多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，導航到 **Neighbors** 標籤頁，然後單擊 MAC 地址。使用者名稱為 "**admin**"，密碼為空（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描 QR 碼並選擇您首選的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將已輸入。
- 單擊 Connect，透過無線網路與您的裝置建立連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要設定。

## 供電 {#powering}

裝置可透過乙太網埠（Passive PoE）供電。在最大負載下，本裝置的功耗為 11 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置上的乙太網線纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路 (LAN) 的乙太網線纜連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

RouterOS 除本文件所述內容外，還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help)。如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 internet 埠的所有訪問均被阻止）。

## 安裝 {#mounting}

裝置應垂直安裝，使乙太網線纜朝下。

*本裝置的安裝和配置應由合格人員完成。*

如果要將裝置緊固到立杆上，可以使用隨附的安裝環。裝置附帶兩個安裝環——將安裝環穿過提供的邊緣標記並繞過裝置，再繞過將要安裝的立杆。

可使用電工膠帶增加材料之間的摩擦力，將其用在卡箍與安裝表面之間。這有助於將裝置固定到位。包裝中提供安裝軟管卡箍。

![](/img/a6b1a7f28ce9b084.webp)

- 將軟管卡箍穿過裝置背面的開口。
- 固定到立杆或桅杆上。
- 使用 PH2 螺絲刀透過軟管卡箍螺絲對齊並固定。裝置放置時應使天線朝上。應避免將鬆散的乙太網線纜連線到乙太網埠，請將線纜固定到牆壁或立杆上，以免線纜重量拉扯埠。建議在距裝置小於 2m 處固定乙太網線纜。這是為了確保線纜不會因其重量損壞埠，也不會脫落。

安裝時，請確保電纜入口朝下。本裝置的 IP 防護等級為 IP54。我們建議使用 Cat6 遮蔽線纜。警告！本裝置安裝和操作時，裝置與身體之間應保持至少 20 cm 的距離。在住宅環境中操作本裝置可能會造成無線電干擾。

## 開啟乙太網蓋 {#opening-ethernet-cover}

![](/img/3e5c964590f9b4e3.webp)

- 要開啟蓋子，請鬆開兩個緊韌體的卡扣，蓋子即可開啟。
- 將乙太網線纜穿過蓋子開口中的橡膠密封件。
- 在電纜上壓接 RJ-45 接頭，並連線到乙太網埠。

## 天線使用 {#antenna-usage}

將天線擰到裝置上的接頭上以連線天線。

![](/img/27e497f2e7a39c3c.webp)

請在裝置關閉時連線和斷開天線！

## 復位按鈕 {#reset-button}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RBMetalG-52SHPacn 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 規格 {#specifications}

有關本產品、規格和圖片的更多資訊，請訪問我們的網頁：[https://mikrotik.com/product/RBMetalG-52SHPacn](https://mikrotik.com/product/RBMetalG-52SHPacn)。RBMetalG-52SHPacn-US（美國）在出廠時鎖定 2412-2462MHz、5170-5250MHz 和 5725-5835MHz 頻率。此鎖定無法移除。RBMetalG-52SHPacn（國際版）支援 2412-2484MHz 和 5150MHz-5875MHz 範圍（具體頻率範圍可能受國家/地區法規限制）。

## 配件 {#accessories}

包裝內包含以下隨裝置附帶的附件：

- 歐盟/美國開關電源 24 V ⎓ 0.8A，19.2 W。
- 用於 N FEMALE 的 2.4Ghz/5Ghz 雙頻全向天線，6 dBi，灰色，PVC 外殼，長度 285 mm。
- 千兆 POE 注入器。
- 塑膠紮帶緊韌體 2 件。
- 軟管卡箍 50 / 70 2 件。
- N-Male 轉 N-Female 直角轉接頭。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場。請熟悉您所在地區將裝置正確運輸至指定處置場的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBMetalG-52SHPacn</td><td>TV7MTLG52SHPN</td></tr></tbody></table>

本裝置已經過測試，符合

![](/img/ce6fc3eb10b9a1e6.webp)

Class B 數字裝置的限值，依據 FCC 規則第 15 部分。這些限值旨在為住宅安裝中的有害干擾提供合理保護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下措施之一來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的間隔。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。**FCC 警告：** 未經合規責任方明確批准的任何更改或修改，都可能導致使用者操作本裝置的許可權失效。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受接收到的任何干擾，包括可能導致不良操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或協同操作。

**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用經本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用任何未經本產品認證的天線。安裝人員應根據國家/地區法規和每種天線型別配置天線的輸出功率水平。帶有接頭的裝置需要由專業人員安裝，以確保符合健康與安全要求。**獲准的 2.4 GHz 天線列表：** • 24 dBi 碟形天線 DC 24-HD-PFIP • 20 dBi 平板天線 WLP-2450-20 • 17 dBi 扇區天線 SA 24-90-17-WB • 15 dBi 全向天線（立杆）WL0-2450-15 • 13 dBi 全向天線（水平極化）HP, 0DH 24-13 **獲准的 5GHz 天線列表：** • 8.5 dBi 全向天線 MTI Wireless MT-482016NA • 24 dBi 平板天線 Pacific Wireless PA58-24 • 32 dBi 碟形天線 Pacific Wireless HDDA5W-32-DP 在符合認證要求的情況下，可使用與上述型別相同且增益更低的天線。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBMetalG-52SHPacn</td><td>7442A-MG52SHPAC</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，並且 (2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。允許在以下兩個條件下操作：(1) 裝置不得產生干擾，並且 (2) 使用者必須接受裝置受到的任何無線電干擾，即使該干擾可能影響裝置的正常執行。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

在 5150–5250 MHz 頻段執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射器功率</th></tr></thead><tbody><tr><td>2400-2483.5 MHz、5150-5350 MHz、5650-5850 MHz</td><td>≤100 mW</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊以斜槓分隔的形式標註在其標籤上的序列號末尾。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 MHz（30 dBm）、5150-5250 MHz（23 dBm）、5250-5350 MHz（20 dBm）、5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用裝置，必須按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定批准、並在烏克蘭司法部 2013 年 1 月 3 日第 57/22589 號登記的秩序取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBMetalG-52SHPacn 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相應型號）</th><th>使用的通道</th><th>最大輸出功率 (EIRP)</th><th>限制</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、佈線要求和動態頻率選擇 (DFS) 要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更詳細資訊，請參見上文的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 規定所規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。有關更多資訊，請參見上文的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。有關更多資訊，請參見上文的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。有關更多資訊，請參見上文的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 最大發射功率限值。有關更多資訊，請參見上文的符合性宣告。

![](/img/0561b3ba8c95a35c.webp)

本裝置在 5150 至 5350 MHz 頻率範圍內工作時，其 WLAN 功能僅限室內使用。 / 本裝置在 5150 至 5350 MHz 頻率範圍內工作時，其 WLAN 功能僅限室內使用。 / 本裝置在 5150 至 5350 MHz 頻率範圍內工作時，其 WLAN 功能僅限室內使用。 / 本裝置在 5150 至 5350 MHz 頻率範圍內工作時，其 WLAN 功能僅限室內使用。 / 本裝置在 5150 至 5350 MHz 頻率範圍內工作時，其 WLAN 功能僅限室內使用。 / 本裝置在 5150 至 5350 MHz 頻率範圍內工作時，其 WLAN 功能僅限室內使用。
