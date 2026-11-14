---
title: "QRT 5 ac"
slug: /qrt-5-ac
source: https://manual.mikrotik.com/hardware/qrt-5-ac
captured_at: '2026-11-04T09:58:31+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律法規進行處理。
- 將接入點安裝在任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適用於安裝在戶外的立杆上。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的做法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 使用乙太網線將裝置連線到隨附的 PoE 供電器，接入資料+電源端；
- 將 PoE 供電器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 透過網頁瀏覽器使用 **WebFig** 或 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）配置裝置。**提供多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 即可訪問 **WebFig**；對於 **WinBox**，請下載該工具，轉到 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 "**admin**"，密碼為空（或者，對於某些型號，請在貼紙上檢視使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您所在的國家，以應用該國家的法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。
- 將裝置安裝到所需位置，請參閱（連結）

## 擴充套件插槽和埠 {#extension-slots-and-ports}

千兆乙太網埠，乙太網埠上支援被動 PoE。

- 5 GHz 無線，支援的協定 802.11a/n/ac，天線增益 24 (dBi)。

## 開啟卡扣 {#opening-latch}

要接觸乙太網埠和復位按鈕，請開啟卡扣：

![](/img/f3781190be56c137.webp)

## [QRT 5 ac](https://mikrotik.com/product/RB911G-5HPacD-QRT) (RB911G-5HPacD-QRT) {#qrt-5-ac-rb911g-5hpacd-qrt}

- 將卡扣從裝置上向下拉出。
- 抬起卡扣，但不要將它們完全取下。

![](/img/bfaed7cbeee8d4a5.webp)

## 前面板狀態 LED 行為 {#front-status-led-behavior}

RouterOS 允許按使用者意願配置每個 LED 的活動方式。可以配置 LED 顯示無線訊號強度、在介面有流量活動時閃爍以及許多其他選項。如需瞭解更多資訊，請訪問 [LEDs](/docs/hardware/leds) 手冊頁面。本裝置的默認出廠配置：

![](/img/3b568ebffbd94538.webp)

- 常亮藍色 – 裝置已通電。
- 常亮綠色 – 乙太網埠已連線。
- 常亮綠色 – 使用者自定義 LED。
- 常亮綠色 – 五個綠色 LED 的組合，顯示訊號強度。

## 安裝 {#mounting}

本裝置設計用於戶外，安裝在桅杆上，所有需要的線纜都透過裝置的卡扣穿入。

*本裝置的安裝和配置應由具備資質的人員完成。*

在桅杆上安裝時，請確保線纜入口朝下。本裝置的 IP 防護等級為 IP54。我們建議使用 Cat5/6 遮蔽線纜。警告！安裝和操作本裝置時，裝置與人體之間應保持至少 30 cm 的距離。在住宅環境中操作本裝置可能會造成無線電干擾。QRT 包裝箱內有多個部件需要組裝。請按以下步驟操作：

![](/img/f2a401efc69d5463.webp)

- 使用隨附的四顆螺釘將兩個支架 (A) 安裝到旋轉調節器 (B) 上（使用 PH1 螺絲刀）。
- 將兩個 U 型螺栓 (C) 環繞在桅杆或立杆上，並讓它們穿過旋轉調節器 (D) 上的孔。然後擰緊 U 型螺栓，每個配一個平墊圈、一個彈簧墊圈和一個螺母，如右圖所示。所有螺母需使用 10 號（3/8 in）扳手擰緊。立杆的最大直徑可達 70 mm。

![](/img/566b4a72f051a36b.webp)

- 使用安裝支架 (E)，將其裝到天線背面。對每個內建螺栓按此順序各安裝一個橡膠圈、一個墊圈和一個螺母。

![](/img/2b7396442b92f286.webp)

- 將旋轉調節器安裝到安裝支架上。在位置 (F) 使用長螺栓。在較短的螺釘上各放一個平墊圈和一個彈簧墊圈，然後將它們裝入位置 (G)。不要擰得太緊，因為此時需要調整天線。

![](/img/a6a3b8817862ac1b.webp)

- 根據軟體中的無線訊號調整好天線的水平和角度後，擰緊所有螺母。請記錄角度數值以備日後參考。風載荷 16 kg @ 40m/s，9kg @ 30 m/s；

## 接地 {#grounding}

安裝基礎設施（塔和桅杆）以及路由器本身必須正確接地。裝置背面有一個接地線固定螺釘。將接地線連線到接地螺釘上，然後將接地線的另一端連線到已接地的桅杆上，請參見圖片：

![](/img/f54eca22e5502899.webp)

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置將開始尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RB911G-5HPacD-QRT 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這可用於 RouterBOOT 偵錯和恢復。

## 配件 {#accessories}

包裝內含隨裝置提供的附件：

- 安裝部件：QRT U 型螺栓，鋼製 - 鍍鋅，直徑 6 mm，U 型桅杆卡箍，天線支架。
- 歐規/美規開關電源 24 V，1.2 A，30 W DC ⎓ 線纜：220 cm 直角 DC 插頭。
- K-QRT_Fastening set for QRT。
- ZCPOEC006-R2_Gigabit POE 供電器線纜，帶遮蔽接頭。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統未經測試。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片、下載內容和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/RB911G-5HPacD-QRT](https://mikrotik.com/product/RB911G-5HPacD-QRT)

## 國家列表 {#country-list}

<table><thead><tr><th></th><th>**AT**</th><th>**BE**</th><th>**BG**</th><th>**CY**</th><th>**CZ**</th><th>DE</th><th>DK</th><th>EE</th><th>EL</th><th>ES</th><th>FI</th><th>**FR**</th><th>**HR**</th><th>![](/img/bc5e2b50bec98c52.webp) HU</th></tr></thead><tbody><tr><td></td><td>**IE**</td><td>**IT**</td><td>LV</td><td>LT</td><td>**LU**</td><td>**MT**</td><td>**NL**</td><td>**PL**</td><td>PT</td><td>RO</td><td>**SE**</td><td>SI</td><td>**SK**</td><td>UK</td></tr></tbody></table>

加粗標註的為 BFWA（寬頻固定無線接入）成員。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解將裝置正確運送到您所在地區指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID:TV7RB922-5HPACTM

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制要求。這些限制旨在為住宅安裝環境中的有害干擾提供合理保護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝環境中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則建議使用者嘗試透過以下措施之一來消除干擾：

- 調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以獲取幫助。FCC 注意：任何未經合規責任方明確批准的更改或修改都可能導致使用者喪失操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的要求。其操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期操作的干擾。本裝置及其天線不得與任何其他天線或發射器共址或協同工作。**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。安裝和操作本裝置時，輻射體與身體任何部位之間應保持至少 20 cm 的距離。**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用經授權的天線時，僅使用經本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用任何未經本產品認證的天線。安裝人員應根據國家法規和天線型別配置天線的輸出功率水平。帶接頭的裝置需要由專業人員安裝，以確保符合健康與安全要求。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC:7442A-9225HPACT 本裝置符合加拿大工業部免許可證 RSS 標準。其操作須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。安裝和操作本裝置時，輻射體與身體任何部位之間應保持至少 20 cm 的距離。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證而異。

有關裝置生產日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），其後的兩位數字表示周編號。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準（Norma Oficial Mexicana） {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5150-5250 МГц (23 дБм)，5250-5350 МГц (20 дБм)，5470-5725 МГц (27 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置需按照 NKRZI 2012 年 11 月 1 日第 559 號決定（該決定於 2013 年 1 月 3 日在烏克蘭司法部登記，登記號為 57/22589）所規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Mikrotīkls SIA 特此宣告，無線電裝置型別 RB911G-5HPacD-QRT 符合 2014/53/EU 指令的要求。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！**
