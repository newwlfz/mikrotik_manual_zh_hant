---
title: "LHG XL HP5"
slug: /lhg-xl-hp5
source: https://manual.mikrotik.com/hardware/lhg-xl-hp5
captured_at: '2026-11-04T09:55:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/1907cf7e6bbe76a0.jpg)

## [LHG XL HP5](https://mikrotik.com/product/RBLHG-5HPnD-XL)（RBLHG-5HPnD-XL） {#lhg-xl-hp5-rblhg-5hpnd-xl}

雙鏈 eXtra Large 高功率 27dBi 5GHz CPE/點對點一體化天線。完整規格和宣傳冊請參見 [LHG XL HP5 產品頁面](https://mikrotik.com/product/RBLHG-5HPnD-XL)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家和地區的法律法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適合安裝在室外的立杆上。使用錯誤的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和配件，這些電源和配件可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境設定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 組裝 {#assembly}

將兩條支腿安裝到 LHG 外殼上，然後將組裝好的 LHG 單元卡入網格上的相應位置。用兩顆自攻螺釘（已隨附，使用 PH2 十字螺絲刀）將支腿固定到位。使用隨附的螺釘將 L 形支架安裝到碟形天線上。使用 U 型螺栓將裝置固定到立杆/桅杆上。

## 快速開始 {#quickstart}

- 開啟乙太網門，將您的 PC 或 LAN 網線連線到乙太網埠，將乙太網網線的另一端連線到 PoE 注入器；
- 使用乙太網網線將裝置連線到隨附 PoE 注入器的 data+power 端；
- 將 PoE 注入器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 透過 **WebFig** 或 **WinBox** 工具，使用 Web 瀏覽器配置您的裝置，工具地址為 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後單擊 MAC 地址。使用者名稱為 "**admin**"，密碼為空（某些型號的使用者名稱和無線密碼請檢視標籤）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中進行以下設定：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 供電 {#powering}

裝置僅支援透過 Passive PoE 注入器供電。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個乙太網埠，支援自動交叉/直通網線糾正（Auto MDI/X），因此您可以使用直通或交叉網線連線其他網路裝置。
- 一個整合無線裝置，內建網格天線。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：• 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。• 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAPs 模式（共 10 秒）。• 或者繼續按住按鈕 5 秒直到 LED 熄滅，然後鬆開，使 RBLHG-5HPnD-XL 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，只要在裝置通電之前按下按鈕，系統就會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復非常有用。

## 作業系統支援 {#operating-system-support}

裝置支援版本號等於或高於 RouterOS 選單 /system resource 中所指示版本的 RouterOS 軟體。

其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置正確運輸至指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBLHG-5HPnD-XL</td><td>TV7LHG5HPND</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的保護，防止有害干擾。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝環境中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），建議使用者嘗試透過以下一種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置插入與接收器所連線電路不同的插座。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：未經合規負責方明確批准的任何更改或修改，可能會使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的規定。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。本裝置及其天線不得與其他任何天線或發射器同址放置或聯合執行。

**重要：射頻輻射暴露。**

天線與使用者之間必須保持至少 20 釐米的距離。在此配置下，可滿足 FCC 針對人群/非受控環境設定的輻射暴露限值。

天線安裝。警告：安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用經授權的天線時，僅使用已透過本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用除本產品認證天線之外的任何天線。安裝人員應根據國家/地區法規和天線型別配置天線的輸出功率等級。帶有聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBLHG-5HPnD-XL</td><td>7442A-LHG5ACD2HPD</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。其執行須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置執行異常的干擾。

本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR。允許在以下兩個條件下操作：(1) 裝置不得產生干擾，且 (2) 裝置使用者必須接受所受到的任何無線電干擾，即使該干擾可能影響其執行。

在 5150–5250 MHz 頻段內工作的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射功率</th></tr></thead><tbody><tr><td>5150-5350 MHz, 5650-5850 MHz</td><td>≤10 W</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證而異。

裝置生產日期資訊以斜槓分隔的形式標註在標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

![](/img/984ad54320693690.webp)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA, Unijas 2, Рига, Латвія, LV1039。

工作頻率（最大輸出功率）：5150-5250 MHz（23 dBm）、5250-5350 MHz（20 dBm）、5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定（2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV-1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBLHG-5HPnD-XL 符合 2014/53/EU 指令。EU 符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（**適用於相應型號**）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用不受限制</td></tr></tbody></table>

**客戶有責任遵守當地國家的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！** *根據歐盟委員會 2000/299/EC 決定（2000 年 4 月 6 日），本產品屬於第 2 類。*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告。
