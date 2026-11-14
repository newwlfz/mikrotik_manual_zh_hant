---
title: "QRT 5"
slug: /qrt-5
source: https://manual.mikrotik.com/hardware/qrt-5
captured_at: '2026-11-04T09:58:41+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

5GHz AP/Backbone/CPE，雙鏈，千兆乙太網。完整規格和手冊請參見 [QRT 5 產品頁面](https://mikrotik.com/product/RB911G-5HPnD-QRT)。

型號：RB911G-5HPnD-QRT

![](/img/d1903c5423db6850.jpg)

## [QRT 5](https://mikrotik.com/product/RB911G-5HPnD-QRT) (RB911G-5HPnD-QRT) {#qrt-5-rb911g-5hpnd-qrt}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 在任何牆面安裝接入點的所有安裝方法均須獲得當地主管部門認可。
- 裝置安裝必須符合當地和國家電氣規範。
- 本產品 intended for outdoor pole mount. 請仔細閱讀安裝說明後再開始安裝。使用不正確的硬體和配置或未遵循正確程式，可能導致人員危險和系統損壞。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和附件。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 本裝置為 A 類裝置。在家庭環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和執行時，應與您的身體、職業使用者或公眾保持不少於 20 釐米的距離。

## 快速開始 {#quickstart}

- 使用乙太網線將裝置連線到隨附 PoE 注入器的資料+電源端；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 使用 Web 瀏覽器透過 **WebFig** 或 **WinBox** 工具配置您的裝置，地址為 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 即可訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，並單擊 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 要手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，並重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。
- 將本機安裝到您所需的位置，請參見（連結）

## 擴充套件插槽和埠 {#extension-slots-and-ports}

千兆乙太網埠，乙太網埠支援被動 PoE。

- 5 GHz 無線，支援的協定 802.11a/n，天線增益 24 (dBi)。

## 開啟卡扣 {#opening-latch}

要接觸乙太網埠和復位按鈕，請開啟卡扣：

![](/img/1cc7a712a6a341f7.webp)

- 將卡扣向下從裝置中拉出。
- 抬起卡扣，但不要將其完全拆下。

![](/img/bfaed7cbeee8d4a5.webp)

## 前面板狀態 LED 行為 {#front-status-led-behavior}

RouterOS 允許按使用者意願配置每個 LED 的活動。可以將 LED 配置為顯示無線訊號強度、在介面流量活動時閃爍以及許多其他選項。更多資訊請訪問 [LEDs](/docs/hardware/leds) 手冊頁。本裝置的默認出廠配置：

![](/img/3b568ebffbd94538.webp)

- 常亮藍色 – 裝置已通電。
- 常亮綠色 – 已連線乙太網埠。
- 常亮綠色 – 使用者自定義 LED。
- 常亮綠色 – 五個綠色 LED 組成的指示燈組，顯示訊號強度。

## 安裝 {#mounting}

本裝置設計用於戶外，安裝在桅杆上，所有所需線纜透過本機卡扣接入。

*本裝置的安裝和配置應由合格人員完成。*

安裝在桅杆上時，請確保線纜引入口朝下。本裝置的 IP 防護等級為 IP54。我們建議使用 Cat5/6 遮蔽線纜。警告！本裝置安裝和執行時，裝置與您的身體之間應保持至少 30 釐米的距離。在住宅環境中操作本裝置可能造成無線電干擾。QRT 包裝箱包含若干需要組裝的部件。請按以下步驟操作：

- 使用隨附的四顆螺釘（使用 PH1 螺絲刀）將兩個支架 (A) 安裝到旋轉調節器 (B) 上。

![](/img/f2a401efc69d5463.webp)

- 將兩個 U 型螺栓 (C) 套在桅杆或立柱上，並將它們穿過旋轉調節器 (D) 上的孔。然後，如右圖所示，每個 U 型螺栓各用一個平墊圈、一個彈簧墊圈和一個螺母擰緊。所有螺母都需要使用 10 號（3/8 in）扳手擰緊。立柱的最大直徑可達 70 mm。

![](/img/566b4a72f051a36b.webp)

- 使用安裝支架 (E)，將其放到天線背面。對每個內建螺栓，按此順序使用一個橡膠圈、一個墊圈和一個螺母進行安裝。

![](/img/2b7396442b92f286.webp)

- 將旋轉調節器安裝到安裝支架上。在位置 (F) 使用長螺栓。將一個平墊圈和一個彈簧墊圈裝到較短的螺釘上，然後將它們放入位置 (G)。不要擰得太緊，因為您現在需要調節天線。

![](/img/a6a3b8817862ac1b.webp)

- 根據軟體中的無線訊號調整好天線水平和角度後，擰緊所有螺母。記錄角度度數以供日後參考。風載荷 16 kg @ 40 m/s，9 kg @ 30 m/s；

## 接地 {#grounding}

安裝基礎設施（塔和桅杆）以及路由器本身必須正確接地。本裝置在本機背面包含一個接地線連線螺釘。將接地線連線到接地螺釘，然後將接地線的另一端連線到已接地的桅杆，請參見圖片：

![](/img/f54eca22e5502899.webp)

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（總計 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（總計 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總計 15 秒）。無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統將載入備份 RouterBOOT 載入器。這可用於 RouterBOOT 偵錯和恢復。

## 配件 {#accessories}

包裝內包含隨裝置附帶的附件：

- 安裝元件：QRT U 型螺栓，鋼 - 鍍鋅，直徑 6 mm，U 型桅杆夾，天線安裝座。
- EU/US 開關電源 24 V，0.8 A，19.2 W，DC ⎓，85.3 %，VI，線纜：150 cm Hor CMC。
- 用於 QRT 的 K-QRT_Fastening 緊固套件。
- ZCPOEC006-R2_Gigabit POE injector cable，帶遮蔽聯結器。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource。其他作業系統未經測試。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/RB911G-5HPnD-QRT](https://mikrotik.com/product/RB911G-5HPnD-QRT)

## MikroTik 移動應用 {#mikrotik-mobile-app}

![](/img/b0984aa3ad3c6d58.webp)

![](/img/25f50553ffd86eaf.webp)

![](/img/8d294e5cd375c591.webp)

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

為避免環境汙染，請將本裝置與生活垃圾分開，並以安全方式處置，例如送至指定廢物處置場所。請了解將裝置妥善運輸至您所在地區指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝環境提供合理的有害干擾防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域操作本裝置很可能造成有害干擾，在這種情況下，使用者將被要求自費糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者無權操作本裝置。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。

注意：本機已使用外圍裝置的遮蔽線纜進行測試。必須使用遮蔽線纜與本機配合，以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

在 5150–5250 MHz 頻段執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射器功率</th></tr></thead><tbody><tr><td>5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置生產日期資訊標在其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5470-5725 МГц (27 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用裝置，必須按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RB911G-5HPnD-QRT 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率 (EIRP)**</th><th>**限制**</th></tr></thead><tbody><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定中的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告。
