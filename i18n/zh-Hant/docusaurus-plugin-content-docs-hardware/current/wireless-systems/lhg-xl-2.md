---
title: "LHG XL 2"
slug: /lhg-xl-2
source: https://manual.mikrotik.com/hardware/lhg-xl-2
captured_at: '2026-11-04T09:54:41+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/6a907bf16ba327f1.webp)

## [LHG XL 2](https://mikrotik.com/product/lhg_xl_2) (RBLHG-2nD-XL) {#lhg-xl-2-rblhg-2nd-xl}

雙鏈 21dBi 2.4GHz CPE/點對點一體化天線，適用於更遠距離。完整規格和宣傳冊請參見 [LHG XL 2 產品頁面](https://mikrotik.com/product/lhg_xl_2)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應依照所有國家法律和法規進行處理。
- 在任何牆面上安裝接入點的所有安裝方式均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於在室外安裝在立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和附件，這些均可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請先閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座上拔下。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行時，與您的身體、職業使用者或公眾的距離不得小於 40 釐米。

## 組裝 {#assembly}

將兩條支腳安裝到 LHG 外殼上，然後將組裝好的 LHG 單元在相應位置卡入網格。用兩顆自攻螺釘固定支腳（隨附，請使用 PH2 十字螺絲刀）。使用隨附的螺釘將 L 形支架安裝到碟形天線上。使用 U 型螺栓將單元固定到立杆/桅杆上。

## 安裝 {#mounting}

為符合健康法規，請將本裝置安裝在距離您的身體至少 20 cm 的位置。

## 快速開始 {#quickstart}

- 開啟乙太網艙門，將乙太網線纜連線到乙太網埠，並將乙太網線纜的另一端連線到隨附的 PoE 注入器。
- 使用乙太網線纜將裝置連線到隨附 PoE 注入器的資料+電源端；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 透過 **WebFig** 或 **WinBox** 工具使用網頁瀏覽器配置您的裝置，地址為 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中進行以下設定：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通線或交叉線連線到其他網路裝置。
- 一個 SFP 埠。
- 一個帶有內建柵格天線的一體化無線裝置。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置（總共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAPs 模式（總共 10 秒）。
- 或者繼續按住按鈕 5 秒直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總共 15 秒）。無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

本裝置支援版本號等於或高於 RouterOS 選單 /system resource 中所指示版本的 RouterOS 軟體。其他作業系統尚未經過測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢棄物處置場。請了解您所在地區將裝置正確運送到指定處置場的相關流程。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>LHG XL 2</td><td>TV7LHG2ND</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝環境中的有害干擾提供合理保護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝環境中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所在電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以獲取幫助。FCC 警告：任何未經負責合規的一方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的要求。其執行受以下兩個條件的約束：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。本裝置及其天線不得與任何其他天線或發射器同址放置或聯合執行。**重要提示：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置安裝和執行時，輻射體與您身體的任何部位之間的最小距離應為 40 cm。本封閉式裝置符合 FCC 規則與法規 47CFR 第 15 C 段的要求。其執行受以下兩個條件的約束：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>LHG XL 2</td><td>7442A-LHG2ND</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。其執行受以下兩個條件的約束：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置執行異常的干擾。本裝置符合加拿大工業部對免許可無線電裝置適用的 CNR 標準。其使用須滿足以下兩個條件：(1) 裝置不得產生干擾；(2) 使用者必須接受裝置受到的任何無線電干擾，即使該干擾可能影響裝置的正常執行。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要提示：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和執行時，輻射體與您身體的任何部位之間的最小距離應為 40 cm。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻段通道</th><th>發射機功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*可用頻段通道可能因產品型號和認證而異。

有關裝置生產日期的資訊標示在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後面兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

![](/img/984ad54320693690.webp)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

## Norma Oficial Mexicana {#norma-oficial-mexicana}

整合無線模組，工作在 2,4 GHz，採用 802.11 b/g/n 協定並配備內建天線，最大增益為 +21 dBi。

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊學監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2412-2472 MHz（20dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置必須按照 NCRSI 2012 年 11 月 1 日第 559 號決定（該決定於 2013 年 1 月 3 日在烏克蘭司法部登記，編號為 57/22589）所批准的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV-1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（**適用於相關型號**）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！** *根據歐盟委員會 2000/299/EC 決定（2000 年 4 月 6 日），本產品屬於第 2 類範圍。*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。如需更多詳細資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。如需瞭解更多資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規所規定的 WLAN 最大發射功率限值。如需更多資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則所規定的 WLAN 最大發射功率限值。如需瞭解更多資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所規定的 WLAN 最大發射功率限值。如需更多資訊，請參見上文的符合性宣告。
