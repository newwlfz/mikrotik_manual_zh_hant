---
title: "RB951 系列"
slug: /rb951-series
source: https://manual.mikrotik.com/hardware/rb951-series
captured_at: '2026-11-04T06:04:15+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **[RB951Ui-2HnD](https://mikrotik.com/product/RB951Ui-2HnD)**
- **RB951G-2HnD**
:::

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣線路相關危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本裝置擬安裝在機架中。開始安裝前，請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作程式，可能會對人員造成危險並損壞系統。
- 本產品擬在室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和附件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家/地區法規，包括在法律頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 設定 {#setup}

本裝置是一個簡單的家庭無線接入點。它已完成開箱配置，您只需插上網際網路線纜即可開始使用無線網際網路。我們建議您設定密碼來保護裝置。

- 確保您的網際網路服務提供商（ISP）允許硬體更換並自動分配 IP 地址；
- 將 ISP 線纜連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 之外的任意埠，或無線網路“MikroTik-...”連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用 “WinBox” 配置工具，網址為 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 “Neighbors” 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 “admin”，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 單擊 “Check for updates” 按鈕，並將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 “Downloads” 部分找到所需軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 “Files” 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 “QuickSet” 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## 供電 {#powering}

裝置可透過電源插孔或第一個乙太網埠（Passive PoE）接受供電。RB951G-2HnD 在最大負載下的功耗可達 7 W，RB951Ui-2HnD 可達 24 W。

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，正極插針）接受 8-30 V DC。
- 第一個乙太網埠支援 Passive PoE（無源乙太網供電），接受 8-30 V DC。在 RB951Ui 型號上，Ether5 埠支援 PoE 輸出，可為其他 RouterBOARD 裝置供電。該埠具有自動檢測功能，因此您可以連線筆記型電腦和其他非 PoE 裝置而不會損壞它們。Ether5 上的 PoE 輸出約比輸入電壓低 2V，最高支援 0.58A（因此，隨附的 24V PSU 將向 Ether5 PoE 埠提供 22V/0.58 A 輸出）。

## 配置 {#configuration}

RouterOS 除了本文件所述內容外，還包括許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help)。如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，從網際網路埠進行的所有訪問均被阻止）。出於恢復目的，可以從網路啟動裝置，請參見按鈕和跳線。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個獨立乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通或交叉線纜連線到其他網路裝置。
- 整合無線 2.4 GHz 射頻，配有板載 PIF 天線，最大增益 2.5 dBi

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議驗證這兩個選項，以防其中一個無法使用。

- **Regular Booter：** 要進入 etherboot 模式，請在給裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。取決於型號，這可能由 **USR、USER、System** 或 **ACT** LED 指示，也可能由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及更高版本。具體出廠安裝版本列於 /system resource。其他作業系統尚未測試。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置使用的範圍與上述法規不同，則必須向終端使用者裝置應用來自制造商/供應商的定製韌體版本，並防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可證。
- 任何裝置的資料表均可在製造商官方網站上獲取。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，TX 功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，TX 功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，TX 功率限制為 20dBm（EIRP）。

請確保裝置具有鎖定軟體包（製造商的韌體版本），必須將該軟體包應用到終端使用者裝置，以防止終端使用者重新配置。產品將標註國家/地區程式碼“-EG”。本裝置需要升級到最新版本，以確保符合當地主管部門法規！終端使用者有責任遵守當地國家/地區法規，包括在法律頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝。

為避免汙染環境，請將裝置與家庭垃圾分開，並以安全方式處置，例如送往指定的廢物處置場所。請熟悉您所在地區將裝置正確運送到指定處置場所的程式。

## 型號：RB951G-2HnD {#model-rb951g-2hnd}

### 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/b977cf7f64ea36aa.jpg" alt="" width={799} height={744} /></p>

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RB951G-2HnD</td><td>TV7RB951G-2HND</td></tr></tbody></table>

根據 FCC 規則第 15 部分，本裝置已經過測試，符合 B 類數字裝置的限值。這些限值旨在為住宅安裝提供合理保護，防止有害干擾。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致不期望執行的干擾。本裝置及其天線不得與任何其他天線或發射器共址或協同執行。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置安裝和執行時，輻射體與您身體任何部位之間的最小距離應為 20 cm。

### 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可證 RSS 標準。其執行須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置不期望執行的干擾。本裝置符合加拿大工業部適用於免許可證無線電裝置的 CNR 標準。其執行須滿足以下兩個條件：(1) 裝置不得產生干擾；(2) 裝置使用者必須接受所受到的任何無線電干擾，即使該干擾可能影響裝置正常執行。

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和執行時，輻射體與您身體任何部位之間的最小距離應為 20 cm。本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和執行時，輻射體與您身體任何部位之間的最小距離應為 20 cm。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## 型號：RB951Ui-2HnDr2 {#model-rb951ui-2hndr2}

### 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement-1}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RB951Ui-2HnD</td><td>TV7RB951U-2HND</td></tr></tbody></table>

根據 FCC 規則第 15 部分，本裝置已經過測試，符合 A 類數字裝置的限值。這些限值旨在為商業安裝提供合理保護，防止有害干擾。

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置可能會造成有害干擾，在這種情況下，使用者將需要自費糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致不期望執行的干擾。本裝置及其天線不得與任何其他天線或發射器共址或協同執行。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置安裝和執行時，輻射體與您身體任何部位之間的最小距離應為 20 cm。

### 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada-1}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RB951Ui-2HnD</td><td>7442A-951U2HND</td></tr></tbody></table>

本裝置符合加拿大工業部免許可證 RSS 標準。其執行須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置不期望執行的干擾。本裝置符合加拿大工業部適用於免許可證無線電裝置的 CNR 標準。其執行須滿足以下兩個條件：(1) 裝置不得產生干擾；(2) 裝置使用者必須接受所受到的任何無線電干擾，即使該干擾可能影響裝置正常執行。

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和執行時，輻射體與您身體任何部位之間的最小距離應為 20 cm。本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和執行時，輻射體與您身體任何部位之間的最小距離應為 20 cm。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射機功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而有所不同。

裝置製造日期資訊以斜槓分隔標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示周編號。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 МГц（20 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需要按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, 拉脫維亞, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RB951G-2HnD、RB951Ui-2HnD 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家/地區法規，包括在法律頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。有關更多詳細資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。如需更多資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。如需更多資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。如需更多資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 最大發射功率限值。如需更多資訊，請參見上文的符合性宣告。
