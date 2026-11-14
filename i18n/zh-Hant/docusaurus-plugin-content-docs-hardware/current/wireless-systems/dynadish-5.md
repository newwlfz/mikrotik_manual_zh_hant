---
title: "DynaDish 5"
slug: /dynadish-5
source: https://manual.mikrotik.com/hardware/dynadish-5
captured_at: '2026-11-04T09:48:10+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### DynaDish 5 (RBDynaDishG-5HacDr3) {#dynadish-5-rbdynadishg-5hacdr3}

![](/img/b28805dc6f440e18.webp)

## [DynaDish 5](https://mikrotik.com/product/RBDynaDishG-5HacDr3) (RBDynaDishG-5HacD) {#dynadish-5-rbdynadishg-5hacd}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關危險，並熟悉防止事故的標準做法。有關完整規格和宣傳冊，請參閱 [DynaDish 5 產品頁面](https://mikrotik.com/product/RBDynaDishG-5HacDr3)。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置安裝必須符合當地和國家電氣規範。
- 本產品設計用於戶外安裝在杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確程式，可能對人員造成危險並損壞系統。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和附件。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，應與您的身體、職業使用者或公眾保持不少於 20 釐米的距離。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 使用乙太網電纜將裝置連線到隨附 PoE 注入器的 data+power 端；
- 將 PoE 注入器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 透過 Web 瀏覽器使用 **WebFig** 或 **WinBox** 工具（[https://mt.lv/WinBox](https://mt.lv/WinBox)）配置裝置；提供多種配置方法以確保可訪問性；
- 開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後單擊 MAC 地址。使用者名稱為 "**admin**"，密碼為空（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，並重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## 供電 {#powering}

裝置透過乙太網埠接受供電 - PoE 802.3af/at 24-57 V DC ⎓。最大功耗 9 W。

## 配置 {#configuration}

我們建議單擊 "Check for updates" 按鈕，並將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。RouterOS 除本文件所述內容外還包含許多配置選項。我們建議訪問 RouterOS 文件頁面以熟悉這些可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問均被阻止）。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個 10/100/1000 千兆乙太網埠，支援自動交叉/直通電纜糾正（Auto MDI/X），因此您可以使用直通或交叉電纜連線到其他網路裝置。
- 一個整合無線 5 GHz 802.11a/n/ac，2x2 MIMO，帶內建拋物面天線，最大增益 24 dBi。

## 安裝 {#mounting}

本裝置設計用於戶外並安裝在杆上。

安裝時，請確保電纜饋線朝下。本裝置的 IP 等級為 IP54。我們建議使用 Cat6 遮蔽電纜。本裝置的安裝和配置應由合格人員完成。

- 用四顆螺釘將隨附的安裝支架固定到裝置上；

![](/img/a6f1b404988a0199.webp)

- 固定到杆或桅杆上；
- 用兩顆螺釘固定位置；
- 根據需要調整對齊，並擰緊第 3 步中的螺釘。

![](/img/8a21ada73667b37c.webp)

- 注意，乙太網電纜的位置必須朝下。請將所有鬆動的乙太網電纜和天線電纜固定在距裝置約 30cm 的杆或桅杆上，以免電纜重量拉扯埠和聯結器。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有以下功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（總計 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（總計 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總計 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 隨附部件 {#included-parts}

![](/img/c2c7336d67d4a0c0.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 `/system resource` 中。其他作業系統尚未測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請熟悉您所在地區將裝置正確運輸至指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID：TV7DYNADISHGAC

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能造成有害干擾，此時使用者需要自費糾正干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何收到的干擾，包括可能導致意外操作的干擾。

注意：本機在周邊裝置上使用遮蔽電纜進行了測試。必須使用遮蔽電纜搭配本機以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC：7442A-DYNADISHGAC

本裝置包含符合加拿大創新、科學與經濟發展部免許可證 RSS 的免許可證發射器/接收器。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

裝置製造日期資訊標示在其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後面兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

整合無線模組，工作於 5 GHz，協定 802.11a/n/ac，配有外部定向 PCB 天線，最大增益 24 dBi。

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5150-5250 МГц（23 дБм），5250-5350 МГц（20 дБм），5470-5725 МГц（27 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

要在烏克蘭使用，必須按照烏克蘭國家通訊和資訊領域國家監管委員會 2012 年 11 月 1 日第 559 號決議規定的程式獲得使用許可，該決議於 2013 年 1 月 3 日在烏克蘭司法部登記，編號為 57/22589。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, 拉脫維亞, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBDynaDishG-5HacDr3 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 TX 功率限制。有關更多詳細資訊，請參閱上方的符合性宣告。

![](/img/0561b3ba8c95a35c.webp)

在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。
