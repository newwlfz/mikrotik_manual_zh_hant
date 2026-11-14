---
title: "RB911 系列"
slug: /rb911-series
source: https://manual.mikrotik.com/hardware/rb911-series
captured_at: '2026-11-04T10:00:14+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **911 Lite5**
- **911 Lite5 Dual**
- **911 Lite5 ac**
- **RB911G-2HPnD**
- **[RB911G-5HPnD](https://mikrotik.com/product/RB911G-5HPnD)**
- **RB911G-5HPacD**
:::

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的常規做法。本產品的最終處置應按照所有國家法律法規進行處理。裝置的安裝必須符合當地和國家的電氣規範。本產品可以安裝在室外的立柱上。未使用正確的硬體和配置，或未遵循正確的操作步驟，可能導致人員處於危險境地並對系統造成損壞。請僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用本裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

這是 A 類裝置。在居住環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

## 首次使用 {#first-use}

- （可選）將裝置安裝到外殼中。
- 將乙太網線連線到乙太網埠。
- 插上電源線以開啟裝置。
- 在您的 PC、手機或其他裝置上開啟網路連線，搜尋 MikroTik 無線網路並連線到它。
- 配置必須透過無線網路、使用網頁瀏覽器或移動應用程式完成 -（參見 ""）。或者，您也可以使用 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。
- 連線到無線網路後，在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始配置，使用者名稱為 a*dmin*，預設沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）。
- 我們建議點選 "Check for updates" 按鈕，並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。
- 選擇您的國家/地區，以應用國家法規設定，並在載入的介面上設定您的密碼。

## 組裝 {#assembly}

911 系列路由器供專業使用。每臺裝置均採用防靜電包裝。在處理電子裝置時，請遵守以下安全注意事項：

- 在拆包和處理電子元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞；
- 拆包後，請將路由器放置在防靜電墊上；
- 安裝裝置時，請確保沒有可能損壞或接觸 PCB 板的物體。可使用裝置兩側 PCB 板上的四個出廠預留孔，將裝置安裝到您想要的位置。

本裝置的 IPX 等級為 IPX0。在戶外應用中安裝時，請確保裝置具備防水保護。我們建議使用 Cat6 遮蔽網線。安裝基礎設施（塔架和桅杆）以及路由器本身必須正確接地。

## 供電 {#powering}

本裝置接受以下方式的供電：

- 透過乙太網埠進行無源 10-30 V DC ⎓ PoE 供電。電纜越長，為補償線路損耗所需的電壓就越高。建議至少使用 18 V。
- 直接輸入到電源插孔 10-30 V DC ⎓。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 啟動過程 {#booting-process}

RouterOS 是所有 RouterBOARD 路由器的作業系統。請在此處檢視文件：[https://mt.lv/help](https://mt.lv/help) 除乙太網埠上的 IP 地址外，本裝置未進行預配置。另一套配置必須根據上文連結的文件手冊進行應用。初始連線必須透過乙太網線完成，並使用 MikroTik WinBox 實用程式。應使用 WinBox 連線到預設 IP 地址 192.168.88.1，使用者名稱為 admin，密碼為空。如果您希望從網路啟動裝置，例如使用 MikroTik Netinstall，請在啟動裝置時按住復位按鈕，直到 LED 燈熄滅，裝置便會開始尋找 Netinstall 伺服器。如果 IP 連線不可用，也可以使用 WinBox 實用程式連線到裝置的 MAC 地址。更多資訊請參閱文件。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- RB911-5HnD – 5 GHz，802.11a/n，功耗 7 W。
- RB911-5Hn – 5 GHz，802.11a/n，功耗 5 W。
- RB911G-5HPacD – 5 GHz，802.11a/n/ac，功耗 12 W，千兆乙太網。
- RB911G-2HPnD – 2.4 GHz，802.11b/g/n，功耗 10 W，千兆乙太網。
- RB911-5HacD - 5 GHz，802.11a/n/ac，功耗 7 W。
- RB911G-5HPnD – 5 GHz，802.11a/n，功耗 11 W，千兆乙太網。

## 按鈕和跳線 {#buttons-and-jumpers}

RouterBOOT 復位按鈕具有以下功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAPs 模式（共 10 秒）。* 繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 去尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都將載入備份的 RouterBOOT 載入器。這適用於 RouterBOOT 偵錯和恢復。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/7e333f989e2f2ffe.jpg)

- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱已預先填入。
- 點選 Connect，透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用將通過幾個簡單的步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列在 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID：TV7RB911-5HNDM

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝提供合理的保護，防止有害干擾。

本裝置會產生、使用並可能輻射射頻能量，如果未按說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能會造成有害干擾，此時使用者需自費糾正該干擾。

FCC 警告：任何未經負責合規的一方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作受以下兩個條件約束：(1) 本裝置不得造成有害干擾，以及 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與其他任何天線或發射器共置或協同工作。重要：射頻輻射暴露。天線與使用者之間必須保持至少 20 釐米的距離。在此配置下，可滿足 FCC 針對人群/非受控環境規定的射頻暴露限值。天線安裝。警告：安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用經產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，嚴禁使用未經產品認證的任何其他天線。安裝人員應根據國家法規和每種天線型別配置天線的輸出功率水平。帶有聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC:7442A-9115HND 本裝置符合加拿大工業部免許可 RSS 標準。操作受以下兩個條件約束：(1) 本裝置不得造成干擾，以及 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的相關 CNR 標準。其執行須滿足以下兩個條件：(1) 裝置不得產生干擾，並且 (2) 裝置使用者必須接受任何接收到的無線電干擾，即使該干擾可能影響其正常執行。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

工作在 5150–5250 MHz 頻段的裝置僅供室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, , 5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊位於其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份（年份的最後一位數字），其後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## Norma Oficial Mexicana {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用頻率通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 МГц (20 дБм), 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用該裝置，必須按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）所批准的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相應型號）</th><th>使用通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限於室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限於室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更詳細的資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置遵守 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告。

![](/img/0561b3ba8c95a35c.webp)

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。

**BG. Инструкци**
