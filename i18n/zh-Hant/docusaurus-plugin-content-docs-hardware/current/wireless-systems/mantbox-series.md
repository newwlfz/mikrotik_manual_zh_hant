---
title: "mANTBox 系列"
slug: /mantbox-series
source: https://manual.mikrotik.com/hardware/mantbox-series
captured_at: '2026-11-04T09:56:12+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **[mANTBox 15s](https://mikrotik.com/product/RB921GS-5HPacD-15S)** (RB921GS-5HPacD-15S)
- **[mANTBox 2 12s](https://mikrotik.com/product/mantbox_2_12s)** (RB911G-2HPnD-12S)
- **[mANTBox 19s](https://mikrotik.com/product/RB921GS-5HPacD-19S)** (RB921GS-5HPacD-19S)
:::

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責取得當地主管部門/檢驗部門對安裝結構完整性要求的任何當地或國家安全檢查。
- 將接入點安裝在任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本裝置設計用於安裝在戶外立杆上。開始安裝前請仔細閱讀安裝說明。
- 未使用正確的硬體和配置或未遵循正確的操作程式，可能會對人員造成危險情況並損壞系統。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負。
- 本裝置需要升級到 RouterOS v6.48.3 或最新版本，以確保符合當地主管部門法規。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。安裝和操作本 MikroTik 裝置時，應與您的身體、職業使用者或公眾保持不少於 20 釐米的距離。

## 快速開始 {#quickstart}

- 開啟蓋子；
- 用乙太網電纜將裝置連線到隨附 PoE 注入器的 data+power 端；
- 將 PoE 注入器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 使用 Web 瀏覽器透過 **WebFig** 或 [https://mt.lv/WinBox](https://mt.lv/WinBox) 中的 **WinBox** 工具配置裝置；**提供多種配置方法以確保可訪問性；**
- 透過開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，導航到 **Neighbors** 標籤頁，然後單擊 MAC 地址。使用者名稱為“**admin**”，無密碼（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）；
- 點選“Check for updates”按鈕，並將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡並具有活動的網際網路連線；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在“Downloads”部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的“**Files**”選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定路由器密碼。

## 供電 {#powering}

裝置附帶 24 V 0.8 A 電源介面卡。它可與隨附的 PoE 注入器或電源插孔配合使用。裝置在兩種方式下均接受 8-30 V。裝置在 24 V 時的最大功耗為 11 W，具體型號的功耗如下所示。

mANTBox 15s (RB921GS-5HPacD-15S)- 13 W

mANTBox 2 12s (RB911G-2HPnD-12S)- 11 W

mANTBox 19s (RB921GS-5HPacD-19S)- 13 W

## 配置 {#configuration}

我們建議點選“Check for updates”按鈕，並將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。RouterOS 除了本文件所述內容外還包含許多配置選項。我們建議訪問 RouterOS 文件頁面以熟悉這些功能：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的訪問全部被阻止）。

## 安裝 {#mounting}

mANTbox 12s 和 15s 配備 QuickMount 介面卡，可使用隨附的螺絲將其固定到牆上，或使用隨附的金屬安裝環將其固定到立杆上。QuickMount 允許在水平和垂直方向調整裝置。

- 將快裝支架安裝到裝置背面。

![](/img/c2aeb3d4527b034d.jpg)

## [mANTBox 2 12s](https://mikrotik.com/product/mantbox_2_12s) (RB911G-2HPnD-12S) {#mantbox-2-12s-rb911g-2hpnd-12s}

![](/img/f1b9c851a1837362.webp)

- 將裝置固定到立杆上。
- 使用隨附的鋼製卡箍將其固定。夾緊直徑 35 – 70 mm。

![](/img/006d6b97c4c91436.webp)

- 請避免將鬆動的乙太網電纜連線到乙太網埠，應將電纜固定到牆面或立杆上，以免電纜重量拉扯埠。建議在距裝置小於 2m 處固定乙太網電纜。這是為了確保電纜不會因其重量損壞埠，也不會脫落。我們建議使用 Cat6 遮蔽電纜。警告！安裝和操作本裝置時，裝置與身體之間應保持至少 25 cm 的距離。在住宅環境中操作本裝置可能會造成無線電干擾。

mANTbox 19s 配備金屬立杆支架，可夾緊在金屬立杆上。

- 將安裝底座固定到裝置背面。
- 使用安裝支架將裝置固定到立杆上。
- 用支架和螺絲固定裝置。

![](/img/605f9373d3b55718.webp)

- 調整所需的對準方向。

請避免將鬆動的乙太網電纜連線到乙太網埠，應將電纜固定到牆面或立杆上，以免電纜重量拉扯埠。建議在距裝置小於 2m 處固定乙太網電纜。這是為了確保電纜不會因其重量損壞埠，也不會脫落。開啟蓋子後，可在其中找到接地螺絲，因此可以將接地線連線到裝置。

## 接地 {#grounding}

安裝基礎設施（塔架和桅杆）以及路由器本身必須正確接地。裝置在機殼門後配有接地線連線螺絲。將接地線連線到接地螺絲，然後將接地線的另一端連線到已接地的桅杆。這可大幅降低 ESD 和雷擊損壞的風險。

![](/img/9d368495fcc09e4b.webp)

裝置包含接地連線（標記為 ⏚）。

## 開啟蓋子 {#opening-cover}

要開啟蓋子，請用手逆時針旋轉松不脫螺絲，然後將其抬起。

![](/img/c9aa40a174a2b89d.webp)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 內建無線介面，2x2 MIMO，支援 AP/station/bridge 模式。
- 一個 10/100/1000 千兆乙太網埠，支援自動交叉/直通電纜校正（Auto MDI/X），因此您可以使用直通或交叉電纜連線到其他網路裝置。乙太網埠接受來自無源 PoE 注入器的 8-30V DC 供電。
- 一個用於 1.25GBit 模組的 SFP 埠，支援 DDMI。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有以下功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在會尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復非常有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送到指定的廢物處置場所。請熟悉您所在地區將裝置正確運輸到指定處置場所的程式。

## 型號：RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s) {#models-rb921gs-5hpacd-15s-mantbox-15s-rb921gs-5hpacd-19s-mantbox-19s}

### 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RB921GS-5HPacD-15S</td><td>TV7RB921G-5HPACD</td></tr><tr><td>RB921GS-5HPacD-19S</td><td>TV7RB921G-5HPACD</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝環境中的有害干擾提供合理保護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在居民區操作本裝置很可能造成有害干擾，在這種情況下，使用者需要自費糾正干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受收到的任何干擾，包括可能導致非預期操作的干擾。

注意：本裝置已使用外圍裝置上的遮蔽電纜進行測試。必須使用遮蔽電纜與本裝置配合，以確保合規。

**天線安裝警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，只能使用已透過本產品認證的天線。安裝人員應根據國家/地區法規和天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

**重要：射頻輻射暴露。** 天線與職業使用者之間必須保持至少 20 cm 的距離。在此配置下，可滿足 FCC 針對一般人群/非受控環境規定的輻射暴露限值。

### 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RB921GS-5HPacD-15S</td><td>7442A-921G5HPACD</td></tr><tr><td>RB921GS-5HPacD-19S</td><td>7442A-921G5HPACD</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。操作須符合以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

在 5150–5250 MHz 頻段工作的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

**天線安裝警告：** 安裝人員有責任確保在加拿大（或適用 IC 規則的地區）使用授權天線時，只能使用已透過本產品認證的天線。安裝人員應根據國家/地區法規和天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

**重要：射頻輻射暴露。** 天線與職業使用者之間必須保持至少 20 cm 的距離。在此配置下，可滿足 FCC 針對一般人群/非受控環境規定的輻射暴露限值。

### UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

### 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射功率</th></tr></thead><tbody><tr><td>5150-5350 MHz, 5650-5850 MHz</td><td>≤10 W</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊以斜槓分隔標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

### 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

### 烏克蘭國家通訊和資訊學監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5150-5250 MHz（23 dBm），5250-5350 MHz（20 dBm），5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定（該決定於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式取得使用許可。

### CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i，里加，拉脫維亞，LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

#### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相應型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定規定的最大 WLAN 發射功率限值。更多資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的最大 WLAN 發射功率限值。有關更多資訊，請參閱上文的符合性宣告。

## 型號：RB911G-2HPnD-12S (mANTBox 2 12s) {#models-rb911g-2hpnd-12s-mantbox-2-12s}

### 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement-1}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RB911G-2HPnD-12S</td><td>TV7RB911G2HPND</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝環境中的有害干擾提供合理保護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在居民區操作本裝置很可能造成有害干擾，在這種情況下，使用者需要自費糾正干擾

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受收到的任何干擾，包括可能導致非預期操作的干擾。

注意：本裝置已使用外圍裝置上的遮蔽電纜進行測試。必須使用遮蔽電纜與本裝置配合，以確保合規。

**天線安裝警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，只能使用已透過本產品認證的天線。安裝人員應根據國家/地區法規和天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。安裝和操作本裝置時，輻射器與身體任何部位之間應保持至少 20 cm 的距離。

### 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada-1}

IC: 7442A-911G2HPND

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。操作須符合以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**天線安裝警告：** 安裝人員有責任確保在加拿大（或適用 IC 規則的地區）使用授權天線時，只能使用已透過本產品認證的天線。安裝人員應根據國家/地區法規和天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。安裝和操作本裝置時，輻射器與身體任何部位之間應保持至少 20 cm 的距離。

### UKCA 標誌 {#ukca-marking-1}

![](/img/5d0fc80f851cbbdf.webp)

### 歐亞符合性標誌 {#eurasian-conformity-mark-1}

<table><thead><tr><th>頻率通道</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>≤10 W</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊以斜槓分隔標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

### 墨西哥官方標準 {#norma-oficial-mexicana-1}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

### 烏克蘭國家通訊和資訊學監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine-1}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 MHz（30 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定（該決定於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式取得使用許可。

### CE 符合性宣告 {#ce-declaration-of-conformity-1}

製造商：MikroTikls SIA, Brivibas gatve 214i，里加，拉脫維亞，LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RB911G-2HPnD-12S 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

#### 頻段使用條款 {#frequency-bands-terms-of-use-1}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 TX 功率限值。有關更詳細的資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定規定的最大發射功率限值。更多資訊請參閱上文的符合性宣告。更多資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 TX 功率限值。有關更多資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 TX 功率限值。有關更多詳細資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 TX 功率限值。有關更多詳細資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的最大 TX 功率限制。有關更多詳細資訊，請參閱上文的符合性宣告。
