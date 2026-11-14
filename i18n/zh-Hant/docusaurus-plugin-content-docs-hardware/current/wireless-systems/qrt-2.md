---
title: "QRT 2"
slug: /qrt-2
source: https://manual.mikrotik.com/hardware/qrt-2
captured_at: '2026-11-04T09:58:33+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

QRT 是一款室外 CPE 裝置，具有以下硬體規格：

![](/img/aba055f98926df06.webp)

## [QRT 2](https://mikrotik.com/product/RBQRTG-2SHPnDr2)（RBQRTG-2SHPnD） {#qrt-2-rbqrtg-2shpnd}

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 使用乙太網線將裝置連線到隨附的 PoE 供電器上的資料+電源端；
- 將 PoE 供電器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 透過 **WebFig** 或 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）使用網頁瀏覽器配置您的裝置。**提供多種配置方式以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後單擊 MAC 地址。使用者名稱為 "**admin**"，密碼為空（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。
- 將裝置安裝到您想要的位置，請參見（連結）

## 擴充套件插槽和埠 {#extension-slots-and-ports}

千兆乙太網埠，乙太網埠上的被動 PoE。

- 2.4 GHz 無線，支援協定 802.11b/g/n，天線增益 17 (dBi)。

## 開啟卡扣 {#opening-latch}

要訪問乙太網埠和復位按鈕，請開啟卡扣：

![](/img/1cc7a712a6a341f7.webp)

- 將卡扣從裝置上向下拉出。
- 抬起卡扣，但不要將其完全取下。

![](/img/bfaed7cbeee8d4a5.webp)

## 前面板狀態 LED 行為 {#front-status-led-behavior}

RouterOS 允許按使用者意願配置每個 LED 的活動。可以將 LED 配置為顯示無線訊號強度、在介面流量活動時閃爍以及許多其他選項。更多資訊請訪問 [LEDs](/docs/hardware/leds) 手冊頁面。本裝置的出廠預設配置：

![](/img/3b568ebffbd94538.webp)

- 藍色常亮 – 裝置已通電。
- 綠色常亮 – 乙太網埠已連線。
- 綠色常亮 – 使用者自定義 LED。
- 綠色常亮 – 由五個綠色 LED 組成的指示燈組，顯示訊號強度。

## 安裝 {#mounting}

本裝置設計用於室外使用，安裝在桅杆上，所有所需線纜均透過裝置的卡扣連線。

*本裝置的安裝和配置應由合格人員完成。*

安裝在桅杆上時，請確保線纜進線口朝下。本裝置的 IP 防護等級為 IP54。我們建議使用 Cat5/6 遮蔽線纜。警告！本裝置的安裝和操作應保持裝置與您身體之間的最小距離為 30 cm。在居住環境中操作本裝置可能會造成無線電干擾。QRT 包裝盒中包含若干需要組裝的部件。請按以下流程操作：

- 使用隨附的四顆螺絲（使用 PH1 螺絲刀）將兩個支架 (A) 安裝到旋轉調節器 (B) 上。

![](/img/f2a401efc69d5463.webp)

- 將兩個 U 型螺栓 (C) 圍繞桅杆或立杆放置，並將它們穿過旋轉調節器 (D) 上的孔。然後擰緊 U 型螺栓，每個配一個平墊圈、一個彈簧墊圈和一個螺母，如右圖所示。所有螺母都需要使用 10 號（3/8 in）扳手擰緊。立杆的最大直徑可達 70 mm。

![](/img/566b4a72f051a36b.webp)

- 使用安裝支架 (E)，將其放到天線背面。對每個內建螺栓依次用一個橡膠圈、一個墊圈和一個螺母進行安裝（按此順序）。

![](/img/2b7396442b92f286.webp)

- 將旋轉調節器安裝到安裝支架上。在 (F) 位置使用長螺栓。在較短的螺絲上放一個平墊圈和一個彈簧墊圈，然後將它們放入 (G) 位置。不要擰得太緊，因為您現在需要調整天線。

![](/img/a6a3b8817862ac1b.webp)

- 一旦根據軟體中的無線訊號調整好天線的水平和角度，就擰緊所有螺母。請記錄下角度度數以備將來參考。風載荷16 kg @ 40m/s，9kg @ 30 m/s；

## 接地 {#grounding}

安裝基礎設施（塔和桅杆）以及路由器本身都必須正確接地。本裝置在裝置背面包含一個接地線連線螺絲。將您的接地線連線到接地螺絲，然後將接地線的另一端連線到已接地的桅杆，請參見圖片：

![](/img/f54eca22e5502899.webp)

## 復位按鈕 {#reset-button}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置將開始查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的附件：

- 安裝部件：QRT U 型螺栓，鋼 - 鍍鋅，直徑 6 mm，U 型桅杆夾，天線支架。
- 歐盟開關電源 24 V、0.8 A、19.2 W、DC ⎓、85.3 %、VI、電纜：150 cm Hor CMC。
- 用於 QRT 的 K-QRT_Fastening 緊固套裝。
- ZCPOEC006-R2_Gigabit POE 供電器電纜，帶遮蔽聯結器。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。具體的出廠預裝版本列於 /system resource。其他作業系統尚未測試。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片、下載內容和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/RBQRTG-2SHPnDr2](https://mikrotik.com/product/RBQRTG-2SHPnDr2)

## MikroTik 移動應用 {#mikrotik-mobile-app}

![](/img/b0984aa3ad3c6d58.webp)

![](/img/25f50553ffd86eaf.webp)

![](/img/8d294e5cd375c591.webp)

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID：TV7RBQRTG2SHPND

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的有害干擾防護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。然而，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的間距。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。FCC 警告：任何未經合規負責方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾，(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器位於同一位置或配合操作。重要：射頻輻射暴露。本裝置符合 FCC 針對不受控環境規定的射頻輻射暴露限制。本裝置的安裝和操作應保持輻射體與您身體任何部位之間的最小距離為 30 cm。**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用經授權的天線時，僅使用經本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用任何未經本產品認證的天線。安裝人員應根據國家/地區法規和每種天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC:7442A-QRTG2SHPND 本裝置符合加拿大工業部免許可 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得造成干擾，(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement. 重要：射頻輻射暴露。本裝置符合 IC 針對不受控環境規定的輻射暴露限制。本裝置的安裝和操作應保持輻射體與您身體任何部位之間的最小距離為 30 cm。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 30 cm entre le radiateur et toute partie de votre corps. CAN ICES-3 (B)/NMB-3(B)FCC

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>≤100 mW</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證而異。

裝置製造日期資訊以斜槓分隔的形式標示在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），後面兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2480-2483.5 MHz（20 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBQRTG-2SHPnD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率 (EIRP)**</th><th>**限制**</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用無任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝！**
