---
title: "NetBox 5 ax"
slug: /netbox-5-ax
source: https://manual.mikrotik.com/hardware/netbox-5-ax
captured_at: '2026-11-04T09:57:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/e1dfd2faec31c861.jpg)

## [NetBox 5 ax](https://mikrotik.com/product/netbox_5_ax)（L11UG-5HaxD-NB） {#netbox-5-ax-l11ug-5haxd-nb}

廣受歡迎的 NetBox 5 的 Wi-Fi 6 升級版。AP/CPE/點對點——它樣樣都能勝任！PoE-in、DC 插孔、千兆乙太網、耐用的室外機殼、現代雙核 ARM CPU、Wi-Fi-6 5GHz 無線。完整規格和手冊請參見 [NetBox 5 ax 產品頁面](https://mikrotik.com/product/netbox_5_ax)。

## 安全警告 {#safety-warnings}

- 在對任何 MikroTik 裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。
- 請只使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 本裝置應由經過培訓的合格人員按照本安裝說明進行安裝。安裝人員負責確保裝置的安裝符合當地和國家的電氣規範。請勿嘗試拆卸、修理或改裝裝置。
- 本產品設計用於在室外安裝於立杆上。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體和配置或不遵循正確的步驟，可能對人員造成危險並損壞系統。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如裝置發生故障，請斷開其電源。最快的方法是將電源介面卡從電源插座上拔下。
- 為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定的區域。請熟悉將裝置正確運送到您所在地區指定收集點的程式。
- 本產品為 A 類產品。在住宅環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 取下上蓋（參見"取下上蓋"）；
- 在連線電源之前，請先將天線連線到 SMA 介面（參見"天線使用"）；
- 開啟底蓋（參見"開啟底蓋"）；
- 使用乙太網線將裝置連線到隨附的 PoE 注入器的 data+power 端；
- 將 PoE 注入器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 透過網頁瀏覽器使用 **WebFig** 或 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）配置您的裝置。**提供多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 即可訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 "**admin**"，無密碼（或對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用該國家/地區的法規設定；
- 在左側欄位設定您的無線網路密碼；
- 在底部欄位設定您的路由器密碼。

## 供電 {#powering}

裝置可透過以下方式供電：

- 乙太網埠支援 Passive PoE 18-28 V DC ⎓。無外接附件時，裝置最大功耗為 6W。在最大負載下，其功耗可達 15W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 使用乙太網線將裝置連線到隨附的 PoE 注入器，插入 data+power 或 PoE-out 埠；
- 將 PoE 注入器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 注入器。

## 取下上蓋 {#removing-upper-cover}

![](/img/2eda41655896d023.webp)

- 要取下上蓋，請按下兩側的卡扣。
- 握住機身，將蓋子向側面拉出。組裝時請勿在上蓋上留下痕跡或標記。

## 開啟底蓋 {#opening-bottom-cover}

- 要開啟底蓋，請擰下鎖定螺釘。
- 將蓋子稍微從裝置機身拉開。

![](/img/f16854c33d3acfab.webp)

![](/img/11ca542b5f33e0e8.webp)

- 將其提起，但不要完全取下。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。連線其他網路裝置時，可使用直通線或交叉線。
- USB Type-A 埠。
- 2 個外部 SMA 天線介面。
- 內建無線模組，工作於 5 GHz，採用 802.11a/n/ac/ax 協定。

## 安裝 {#mounting}

NetBox 5 ax 設計用於室外使用，可安裝在立杆或 DIN 導軌上。安裝時，請確保線纜入口朝下。本裝置的 IP 防護等級為 IP54。我們建議使用 Cat6 遮蔽網線。警告！本裝置的安裝和操作應確保裝置與人體之間的最小距離為 240 cm。本裝置在住宅環境中執行可能造成無線電干擾。*本裝置的安裝和配置應由合格人員完成。*

### 安裝在立杆上 {#mounting-on-the-pole}

包裝中隨附安裝用喉箍。

- 將喉箍穿過裝置背面的開口，並將其固定到立杆上。
- 使用 PH2 螺絲刀對齊並用喉箍螺釘固定。
- 裝置應始終保持 TOP 蓋朝上放置。

![](/img/165c32108e3b52e8.webp)

-

連線您的天線。

![](/img/906ecf02037cf996.webp)

-

天線不隨裝置提供，僅用於示意。

## 接地 {#grounding}

安裝基礎設施（塔和立杆）必須正確接地。請將所有鬆散的乙太網線和天線線纜固定在距裝置約 30cm 的立杆或桅杆上，以免線纜重量拉扯埠和接頭。

### 使用 DIN 導軌安裝 {#mounting-using-din-rail}

![](/img/9557df4fd23ac02e.webp)

在 DIN 導軌上安裝時，請在包裝中找到專用的支架，並用四顆螺釘將其固定到裝置的背面。裝上安裝支架後，您就可以將裝置滑入 DIN 導軌。

## 前面板狀態 LED 行為 {#front-status-led-behavior}

LED 位於底蓋下方。

![](/img/ecec391ed34e87dd.webp)

RouterOS 允許使用者按自己的意願配置每個 LED 的活動。可以將 LED 配置為顯示無線訊號強度、隨介面流量活動閃爍以及許多其他選項。更多資訊請參見 [LEDs](/docs/hardware/leds) 頁面。本裝置的出廠預設配置：

![](/img/7c85a8cc68fc9a22.webp)

- 常亮藍色 – 裝置已通電。
- 常亮綠色 – 表示裝置在啟動進入不同模式（例如重設配置或為 Netinstall 工具引導裝置）時的狀態。
- 常亮綠色 – 乙太網埠活動。
- 4-8 常亮綠色 – 這組五個綠色 LED 顯示訊號強度。

## 配置 {#configuration}

我們建議在 QuickSet 選單中點選 "Check for updates" 按鈕，因為將您的 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。請確保您已選擇裝置將要使用的國家/地區，以符合當地法規。除了本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始，讓您熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。請向您當地的培訓師尋求更多幫助，或自己成為培訓師。[https://mikrotik.com/training/about](https://mikrotik.com/training/about) 出於恢復目的，可以引導裝置以進行重新安裝，請參見章節 。

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- EU/US 開關電源 24 V DC ⎓，1.2 A，28.8 W。
- 喉箍 35/70 w4 A2 9 mm。
- 帶遮蔽接頭的千兆 POE 注入器線纜（RBGPOE）。
- K-27 DIN 導軌支架安裝套件。

## 天線使用 {#antenna-usage}

![](/img/55046c863770027a.webp)

要連線外部天線，請使用 "Flex-guide"——可單獨購買。這是一根超低損耗的 50cm 長 RPSMA 線纜，可實現卓越的連線質量，適用於室內和室外使用，該線纜具有出色的匹配和損耗值。[https://mikrotik.com/product/ACRPSMA](https://mikrotik.com/product/ACRPSMA) SMA 介面位於上蓋下方（參見"取下上蓋"）以便接入。

請在裝置關閉時連線和斷開天線！

配置資訊請參見 [無線介面](/docs/wireless/abgn/wireless-interface)。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/netbox_5_ax#fndtn-specifications](https://mikrotik.com/product/netbox_5_ax#fndtn-specifications)

[https://i.mt.lv/cdn/product_files/NetBox5ax_240425.pdf](https://i.mt.lv/cdn/product_files/NetBox5ax_240425.pdf)

L11UG-5HaxD-NB-US（美國）在出廠時鎖定為 5170-5330MHz、5490-5730MHz 和 5735-5835MHz 頻段。此鎖定無法解除。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統未經測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場。請熟悉將裝置正確運送到您所在地區指定處置場的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBDisc-5nD</td><td>TV7RB922-5HPACTM</td></tr></tbody></table>

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝中的有害干擾提供合理保護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能造成有害干擾，此時使用者將被要求自行承擔費用糾正干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，(2) 本裝置必須接受任何收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或聯合執行。

**重要：射頻輻射暴露。**

本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和操作應確保輻射體與您身體任何部位之間的最小距離為 20 cm。

**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地方）使用授權天線時，僅使用經本產品認證的天線。根據 FCC 規則 CRF47 第 15.204 部分，明確禁止使用任何未經本產品認證的天線。安裝人員應根據國家/地區法規並按照天線型別配置天線的輸出功率水平。*帶接頭的裝置需要專業安裝，以確保符合健康和安全要求。*

**認可的 5GHz 天線列表：**

- 8.5 dBi 全向天線（型號：MT-482016/N/A）
- 24 dBi 平板天線（型號：PA58-24-ANT）
- 32 dBi 碟形天線（型號：HDDA5W-32-DP2）根據認證，也可使用與上述型別相同且增益更低的天線。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBDisc-5nD</td><td>7442A-9225HPACT</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

工作在 5150–5250 MHz 頻段的裝置僅供室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

天線安裝警告：安裝人員有責任確保在加拿大（或適用 IC 規則的地方）使用授權天線時，僅使用經本產品認證的天線。安裝人員應根據國家/地區法規並按照天線型別配置天線的輸出功率水平。帶接頭的裝置需要專業安裝，以確保符合健康和安全要求。

**重要：射頻輻射暴露。**

本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和操作應確保輻射體與您身體任何部位之間的最小距離為 20 cm。

**認可的 5GHz 天線列表：**

- 8.5 dBi 全向天線（型號：MT-482016/N/A）
- 24 dBi 平板天線（型號：PA58-24-ANT）
- 32 dBi 碟形天線（型號：HDDA5W-32-DP2）根據認證，也可使用與上述型別相同且增益更低的天線。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>5650-5850 MHz</td><td>≤100 mW</td></tr></tbody></table>

*可用頻段可能因產品型號和認證而異。

裝置生產日期資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## Norma Oficial Mexicana {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置，須按 NKРЗІ 2012 年 11 月 1 日第 559 號決定（於 2013 年 1 月 3 日在烏克蘭司法部登記，登記號 № 57/22589）規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 在此宣告，無線電裝置型別 RB911G-5HPacD-NB 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相關型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家/地區法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限制。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告。
