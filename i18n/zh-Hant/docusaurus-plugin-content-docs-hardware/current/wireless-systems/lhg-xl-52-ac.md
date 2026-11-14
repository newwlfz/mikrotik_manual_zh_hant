---
title: "LHG XL 52 ac"
slug: /lhg-xl-52-ac
source: https://manual.mikrotik.com/hardware/lhg-xl-52-ac
captured_at: '2026-11-04T09:55:01+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/d0a3ba8554b1fc5b.webp)

## [LHG XL 52 ac](https://mikrotik.com/product/lhg_xl_52_ac) (RBLHGG-5HPacD2HPnD-XL) {#lhg-xl-52-ac-rblhgg-5hpacd2hpnd-xl}

極其強大的雙頻骨幹 / CPE，適用於無中斷的長距離連線。完整規格和宣傳冊請參閱 [LHG XL 52 ac 產品頁面](https://mikrotik.com/product/lhg_xl_52_ac)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣線路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 在任何牆面上安裝接入點的所有安裝方法均需獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計為安裝在室外的立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 僅使用製造商批准的電源和配件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的做法是從電源插座上拔出電源插頭。
- 客戶有責任遵守當地國家/地區的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 組裝裝置（參見“組裝”）。
- 開啟乙太網蓋板。
- 將裝置連線到 PoE（參見“連線到 PoE 介面卡”）。
- 安裝裝置（參見“安裝”）。
- 在您的 PC、手機或其他裝置上開啟網路連線，搜尋 MikroTik 無線網路並連線。
- 可以透過 Web 瀏覽器或移動應用經由無線網路完成配置 -（參見“配置”）。或者，您也可以使用 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。
- 連線到無線網路後，在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始配置，使用者名稱為 **admin**，預設沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）。
- 使用移動應用時請選擇 Quick setup，它將透過六個簡單步驟引導您完成所有必要的配置。
- 我們建議點選 "Check for updates" 按鈕，將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。
- 在加載出的螢幕上選擇您所在的國家/地區，以應用相應國家/地區的法規設定，並設定您的密碼。

## 供電 {#powering}

該裝置透過乙太網埠接受供電：

- PoE 802.3af/at 12-57 V DC ⎓。最大負載下的功耗可達 18 W。不含附件時為 16 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置上的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自您本地網路（LAN）的乙太網線連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

- 掃描二維條碼並選擇您喜歡的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱已自動填入。
- 點選 Connect，透過無線網路與您的裝置建立連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 還有一個高階選單，可用於完整配置所有必要的設定。

## 組裝 {#assembling}

該裝置需要由四個部件組裝而成：LHG 天線盤、兩條支腿和主體。

- 將兩條支腿安裝到主體上，兩條支腿不同，並標有 L 和 R。
- 將組裝好的部件安裝到天線盤上。
- 使用 PH2 螺絲刀以隨附的螺釘固定。

![](/img/bce1ac9b11d00ada.webp)

## 安裝 {#mounting}

LHG XL ac 設計用於室外，安裝在立杆或桅杆上。包裝內含一個可調節的安裝元件。

安裝時，請確保線纜出口朝下。該裝置的 IP 防護等級為 IP54。我們建議使用 Cat6 遮蔽網線。警告！本裝置的安裝和操作應保持裝置與人體之間至少 20 cm 的距離。在居住環境中操作本裝置可能會造成無線電干擾。本裝置的安裝和配置應由具備資質的人員完成。

包裝中隨附安裝元件。

![](/img/6099d00a8f5d161e.webp)

- 使用四顆螺釘將安裝元件固定到天線盤背面。
- 使用 U 型卡箍將裝置固定到立杆上，按圖示順序放置墊圈和螺母。
- 根據訊號調整裝置方向，並擰緊螺母。
- 裝置應始終以 UP 箭頭朝上的方式放置。

![](/img/646de475ba3c9d96.webp)

## 接地 {#grounding}

安裝基礎設施（塔和桅杆）以及路由器本身都必須正確接地。該裝置在乙太網蓋板後方設有一個接地線聯結器。將接地線連線到接地聯結器，然後將接地線的另一端連線到已接地的桅杆上。請將所有鬆散的乙太網線和天線線纜固定在距離裝置約 30cm 處的立杆或桅杆上，以免線纜重量拉扯埠和聯結器。

## 前面板狀態 LED 行為 {#front-status-led-behavior}

RouterOS 允許按使用者意願配置每個 LED 的活動。可以將 LED 配置為顯示無線訊號強度、在介面流量活動時閃爍以及許多其他選項。更多資訊請訪問 [LEDs](/docs/hardware/leds) 手冊頁面。此裝置的出廠預設配置：

![](/img/64256ab08972f54c.webp)

- 綠色 LED 第四個訊號強度等級。
- 綠色 LED 第三個訊號強度等級。
- 綠色 LED 第二個訊號強度等級。
- 綠色 LED 第一個訊號強度等級。
- 常亮綠色 – SFP 埠活動。
- 常亮綠色 – 乙太網埠活動。
- 常亮綠色 – 使用者自定義 LED。
- 常亮藍色 – 裝置已通電。

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 配置 {#configuration}

該裝置被配置為無線用戶端，您需要選擇要連線的 AP 並設定密碼。我們建議在 QuickSet 選單中點選 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。請確保您已選擇裝置將使用的國家/地區，以符合當地法規。除了本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始瞭解各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都被阻止）。出於恢復目的，可以讓裝置引導以進行重新安裝，請參見“Reset 按鈕”一節。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。可以使用直通線或交叉線連線到其他網路裝置。
- SFP 埠。
- 整合無線模組，工作在 2.4 GHz，802.11b/g/n 協定。
- 整合無線模組，工作在 5 GHz，802.11a/n/ac 協定。

## Reset 按鈕 {#reset-button}

Reset 按鈕有三個功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在將搜尋 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RBLHGG-5HPacD2HPnD-XL 搜尋 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電之前按住按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下配件：

- 歐盟開關電源 24 V ⎓ 1.2 A 28.8 W 86.8 % VI 220 cm RA DC 插頭，橫向短插頭型。
- 千兆 PoE 注入器。
- LHG 外殼
- LHG 支腿 L、R。
- LHG XL 550mm 天線盤
- 安裝元件
- LHG 2 緊韌體套裝。
- LHG 60 緊韌體套裝。請參閱 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/lhg_xl_52_ac](https://mikrotik.com/product/lhg_xl_52_ac)

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解您所在地區將裝置妥善運送至指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBLHGG-5HPacD2HPnD-XL</td><td>TV7LHG5HPACD2HPD</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝環境中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝環境中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來判斷），建議使用者嘗試透過以下措施之一來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 向經銷商或有經驗的無線電/電視技術人員尋求幫助。FCC 警告：任何未經負責合規的一方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受收到的任何干擾，包括可能導致非預期操作的干擾。本裝置及其天線不得與任何其他天線或發射器共址或協同工作。使用 CBRS 頻段時，最終主機裝置的 CBSD 類別將取決於所用的功率設定和天線增益。**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境所規定的射頻輻射暴露限值。本裝置的安裝和操作應保持輻射體與您身體任何部位之間的最小距離為 20 cm。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBLHGG-5HPacD2HPnD-XL</td><td>7442A-LHG5ACD2HPD</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。本裝置符合加拿大工業部針對免許可無線電裝置適用的 CNR 標準。允許在以下兩個條件下執行：(1) 裝置不得產生干擾；(2) 使用者必須接受裝置所受到的任何無線電干擾，即使該干擾可能影響其正常執行。

在 5150–5250 MHz 頻段工作的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境所規定的輻射暴露限值。本裝置的安裝和操作應保持輻射體與您身體任何部位之間的最小距離為 20 cm。本裝置符合 IC 針對非受控環境所定義的輻射暴露限值。本裝置的安裝和使用應保持輻射體與您身體任何部位之間的最小距離為 20 cm。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證而異。

裝置生產日期資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

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

工作頻率（最大輸出功率）：2400-2483.5 МГц (30 дБм)、5150-5250 МГц (23 дБм)、5250-5350 МГц (20 дБм)、5470-5725 МГц (27 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBLHGG-5HPacD2HPnD-XL 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相應型號）</th><th>使用的通道</th><th>最大輸出功率 (EIRP)</th><th>限制</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家/地區的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更詳細的資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置遵守 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限制。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告。

***BG. 說明***
