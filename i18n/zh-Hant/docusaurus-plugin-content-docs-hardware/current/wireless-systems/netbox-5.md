---
title: "NetBox 5"
slug: /netbox-5
source: https://manual.mikrotik.com/hardware/netbox-5
captured_at: '2026-11-04T09:56:39+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## [NetBox 5](https://mikrotik.com/product/RB911G-5HPacD-NB)（RB911G-5HPacD-NB） {#netbox-5-rb911g-5hpacd-nb}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 在任意牆面上安裝接入點的所有安裝方式均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計為安裝在戶外的立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 請僅使用製造商批准的電源和附件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用本裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 這是 A 類裝置。在居住環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 取下上蓋（參見取下上蓋）；
- 將外接天線連線到 SMA 聯結器（參見天線使用）；
- 開啟底蓋（參見開啟底蓋）；
- 使用乙太網線將裝置連線到附帶的 PoE 供電器（注入器）的資料+電源端；
- 將 PoE 供電器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 使用從 DHCP 伺服器獲得的 IP 地址連線到裝置。使用者名稱為 "**admin**"，無密碼（某些型號請檢視貼紙上的使用者和無線密碼），透過 **WebFig** 或 **WinBox** 工具連線；
- 配置裝置，使其具有可用的網際網路連線 [https://mt.lv/configuration](https://mt.lv/configuration)；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet, PTP Bridge AP" 選單中進行以下設定：選擇您的國家/地區，以應用國家法規設定；
- 根據所使用的天線設定天線增益；
- 在底部欄位中設定您的路由器密碼。

## 供電 {#powering}

本裝置可透過以下方式接受供電：

-

乙太網埠接受 Passive PoE 8-30 V DC ⎓。最大負載下的功耗可達 11.5 W。連線到 PoE 介面卡：

-

將乙太網線從裝置連線到 PoE 介面卡的 PoE+DATA 埠。

-

將乙太網線從您的本地網路（LAN）連線到 PoE 介面卡。

-

將電源線連線到介面卡，然後將電源線插入電源插座。

## 取下上蓋 {#removing-upper-cover}

![](/img/337855e5187dd025.webp)

- 要取下上蓋，請按下兩側的卡扣。
- 握住機身，將蓋子向側面拉開。組裝時請勿在上蓋上留下痕跡或參考標記。

## 開啟底蓋 {#opening-bottom-cover}

- 要開啟底蓋，請向上按壓卡扣以鬆開。
- 將蓋子從裝置機身稍微拉開。

![](/img/6d2916bd171187aa.webp)

- 將其抬起，但不要完全取下。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。可使用直通線或交叉線連線到其他網路裝置。
- 外部 SMA 天線聯結器。
- 整合無線模組，工作在 5 GHz，802.11a/n/ac 協定。

## 安裝 {#mounting}

Netbox 5 設計用於戶外，可安裝在立杆或 DIN 導軌上。安裝時，請確保線纜饋出方向朝下。本裝置的 IP 防護等級為 IP54。我們建議使用 Cat6 遮蔽線纜。警告！本裝置的安裝和執行位置與您的身體之間應保持至少 240 cm 的距離。在居住環境中操作本裝置可能造成無線電干擾。*本裝置的安裝和配置應由合格人員完成。*

### 安裝在立杆上 {#mounting-on-the-pole}

包裝中附帶安裝用軟管卡箍。

- 將軟管卡箍穿過裝置背面的開口，並將其固定在立柱上。
- 使用 PH2 螺絲刀，對齊並用軟管卡箍螺絲固定。
- 裝置應始終保持頂蓋朝上。
- 連線您的天線。

![](/img/906ecf02037cf996.webp)

- 天線不隨裝置提供，僅用於圖示說明。

## 接地 {#grounding}

安裝基礎設施（塔和立柱）必須正確接地。請將所有鬆散的乙太網線和天線線纜固定在距裝置約 30cm 處的立杆或立柱上，以免線纜重量拉扯埠和聯結器。

### 使用 DIN 導軌安裝 {#mounting-using-din-rail}

![](/img/fe5138b7c8bd03de.webp)

在 DIN 導軌上安裝時，請在包裝中找到專用支架，並用四顆螺絲將其固定到裝置背面。裝好安裝支架後，您就可以將裝置滑入 DIN 導軌。

## 前面板狀態 LED 行為 {#front-status-led-behavior}

RouterOS 允許按使用者意願配置每個 LED 的活動。可以配置 LED 顯示無線訊號強度、隨介面流量活動閃爍 LED 以及許多其他選項。更多資訊請訪問 [LEDs](/docs/hardware/leds) 手冊頁面。本裝置的出廠預設配置：

![](/img/7c85a8cc68fc9a22.webp)

- 常亮藍燈 – 裝置已通電。
- 常亮綠燈 – 使用者自定義 LED。
- 常亮綠燈 – 活動乙太網埠。
-

- 常亮綠燈 – 五個綠色 LED 的組合顯示訊號強度。

## 配置 {#configuration}

我們建議在 QuickSet 選單中點選 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。請確保您已選擇裝置將要使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包括許多配置選項。我們建議從這裡開始瞭解各種可能性：[https://mt.lv/help](https://mt.lv/help)。如果沒有可用的 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。請向您當地的培訓師尋求更多幫助，或自己成為培訓師。[https://mikrotik.com/training/about](https://mikrotik.com/training/about) 出於恢復目的，可以讓裝置引導以進行重新安裝，請參閱 部分。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（總計 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（總計 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總計 15 秒）。無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都將載入備份的 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下附件：

- 歐盟/美國開關電源 24 V DC ⎓，0.8 A，19.2 W。
- 軟管卡箍 40/60 w2 A2 9 mm。
- 2 個 - 塑膠紮帶緊韌體（300 mm（長）7.6 mm（寬））。
- 帶遮蔽聯結器的千兆 POE 供電器線纜（RBGPOE）。
- K-27 DIN 導軌支架安裝套件。

## 天線使用 {#antenna-usage}

![](/img/55046c863770027a.webp)

要連線到外接天線，請使用 "Flex-guide" —— 可單獨購買。這是一條超低損耗 50cm 長的 RPSMA 線纜，可實現卓越的連線質量，適用於室內和室外使用，該線纜提供出色的匹配和損耗值。[https://mikrotik.com/product/ACRPSMA](https://mikrotik.com/product/ACRPSMA) SMA 聯結器位於上蓋下方（參見取下上蓋），以便檢修。

請在裝置關閉時連線和斷開天線！

有關配置資訊，請參閱 [Wireless Interface](/docs/wireless/abgn/wireless-interface)。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/RB911G-5HPacD-NB](https://mikrotik.com/product/RB911G-5HPacD-NB)

[https://i.mt.lv/cdn/product_files/NetBox_190842.pdf](https://i.mt.lv/cdn/product_files/NetBox_190842.pdf)

- RB911G-5HPacD-NB-US（美國）出廠鎖定在 5170-5250MHz 和 5725-5835MHz 頻率。此鎖定無法解除。
- RB911G-5HPacD-NB（國際版）支援 5150MHz-5875MHz 範圍（具體頻率範圍可能受國家法規限制）。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統未經測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如送往指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBDisc-5nD</td><td>TV7RB922-5HPACTM</td></tr></tbody></table>

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制要求。這些限制旨在為商業安裝環境中的有害干擾提供合理防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在居住區操作本裝置很可能造成有害干擾，此時使用者需自費糾正干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的要求。其操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共址或聯合執行。

**重要提示：射頻輻射暴露。**

本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和執行位置與輻射體及您身體任何部位之間的距離應至少為 20 cm。

**天線安裝。警告：** 安裝者有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用經產品認證的天線。根據 FCC 規則 CRF47 第 15.204 部分，明確禁止使用任何未經產品認證的天線。安裝者應根據國家法規和天線型別，配置天線的輸出功率水平。*帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。*

**經批准的 5GHz 天線列表：**

- 8.5 dBi 全向天線（型號：MT-482016/N/A）
- 24 dBi 面板天線（型號：PA58-24-ANT）
- 32 dBi 碟形天線（型號：HDDA5W-32-DP2）根據認證，也可使用與上述型別相同且增益更低的天線。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBDisc-5nD</td><td>7442A-9225HPACT</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。其操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，並且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

工作在 5150–5250 MHz 頻段的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

天線安裝警告：安裝者有責任確保在加拿大（或適用 IC 規則的地區）使用授權天線時，僅使用經產品認證的天線。安裝者應根據國家法規和天線型別，配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

**重要提示：射頻輻射暴露。**

本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和執行位置與輻射體及您身體任何部位之間的距離應至少為 20 cm。

**經批准的 5GHz 天線列表：**

- 8.5 dBi 全向天線（型號：MT-482016/N/A）
- 24 dBi 面板天線（型號：PA58-24-ANT）
- 32 dBi 碟形天線（型號：HDDA5W-32-DP2）根據認證，也可使用與上述型別相同且增益更低的天線。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而有所不同。

有關裝置生產日期的資訊標註在其標籤上序列號的末尾部分，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

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

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5470-5725 МГц（27 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 NKРЗІ 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 在此宣告，無線電裝置型別 RB911G-5HPacD-NB 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相應型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 最大發射功率限值。更多詳細資訊請參見上文的符合性宣告。
