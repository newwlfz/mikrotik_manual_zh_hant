---
title: "LDF 5 系列"
slug: /ldf-5-series
source: https://manual.mikrotik.com/hardware/ldf-5-series
captured_at: '2026-11-04T09:53:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/83cf6b346ad1683b.webp)

## [LDF 5 ac](https://mikrotik.com/product/ldf_5_ac) (RBLDFG-5acD) {#ldf-5-ac-rbldfg-5acd}

LDF（Lite dish feed，輕量型天線饋源）是一種內建天線的室外無線系統，設計用於安裝在衛星偏饋天線上。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適用於安裝在室外的立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和附件，這些均可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。
- 本裝置為 A 類裝置。在居住環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取相應的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，與您的身體、職業使用者或普通公眾的距離不得小於 20 釐米。

## 組裝 {#assembly}

本裝置相容衛星電視常用的標準偏饋天線。偏饋安裝座為通用型，直徑 40 mm，LDF 可以輕鬆裝入其中。要將乙太網線連線到 LDF 單元，請按以下步驟操作：

- 按圖示組裝所有部件。如果使用成品網線，請在一側切開橡膠密封圈，以便將其套到網線上。自制壓接的網線應在密封圈套到網線上之後再壓接；
- 將乙太網線連線到 LDF 上的乙太網介面；
- 順時針旋轉，將外殼螺母安裝到 LDF 本體上；
- 將橡膠密封圈推入外殼螺母，然後順時針轉動壓緊螺母，密封防水接頭。

![](/img/4697c94b5539fc15.webp)

## 在天線上組裝 {#assembling-on-dish}

請確保將 LDF 單元按右圖所示的正確定位安裝到偏饋安裝座上。單元朝上對準天線。

![](/img/1a2a13170697f321.webp)

![](/img/28d101453837d87d.webp)

天線將作為反射器，放大訊號。組裝完成後，應如左圖所示放置並安裝到立杆或牆壁上。

## 安裝 {#mounting}

本裝置的 IP 防護等級為 IP54。本裝置設計用於室外，請確保所有線纜開口朝下。請使用 Cat6 網線配合 PoE 供電器。安裝基礎設施（塔架和桅杆）以及路由器本身都必須正確接地。

*本裝置的安裝和配置應由具備資質的人員完成。* *警告！本裝置的安裝和操作時，裝置與身體之間的最小距離應為 28 釐米。在居住環境中操作本裝置可能會造成無線電干擾。*

## 供電 {#powering}

本裝置接受來自無源 PoE 供電器（Passive PoE injector）的 10-28 V ⎓ 直流輸入。本裝置不能與符合 IEEE802.3af 的 48 V 供電裝置配合使用。包裝內附帶一個 PoE 供電器。最大功耗：

- LDF 5，6 W；
- LDF 5 ac，8 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠；
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 使用乙太網線將裝置連線到隨附的 PoE 供電器的 data+power 端；
- 將 PoE 供電器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 透過 **WebFig** 或 **WinBox** 工具，使用網頁瀏覽器在 [https://mt.lv/WinBox](https://mt.lv/WinBox) 配置您的裝置；提供多種配置方法以確保可訪問性；
- 開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 "**admin**"，沒有密碼（某些型號請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用國家法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳的效能和穩定性。對於無線型號，請確保您已選擇裝置將要使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，熟悉各種可能的功能：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以引導裝置進行重新安裝，請參見相關章節。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

-

整合無線：LDF 5，5 GHz，802.11a/n；LDF 5 ac，5 GHz，802.11a/n/ac。

-

一個乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X），因此您可以使用直通線或交叉線連線其他網路裝置。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）；
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置此時將尋找 CAPsMAN 伺服器（共 10 秒）；
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）；無論採用上述哪種方式，如果在裝置通電之前就按下按鈕，系統都將載入備份的 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復非常有用。

## 規格 {#specifications}

如需瞭解有關本產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：

- LDF 5 - [https://mikrotik.com/product/rbldf_5nd](https://mikrotik.com/product/rbldf_5nd)
- LDF 5 ac - [https://mikrotik.com/product/ldf_5_ac](https://mikrotik.com/product/ldf_5_ac)

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可以在現場配置您的路由器，或為您的 MikroTik 家庭接入點應用最基本的初始設定：

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟該應用。
- 點選 Connect，透過無線網路與您的裝置建立連線（請檢視貼紙上的無線密碼）。
- 使用者名稱為 "**admin**"，沒有密碼（某些型號請檢視貼紙上的使用者和無線密碼）。
- 選擇 Quick Setup，該應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置運送到指定處置場所的正確程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>LDF 5</td><td>TV7LHG5NDM</td></tr><tr><td>LDF 5 ac</td><td>TV7LHG5ACD</td></tr></tbody></table>

本裝置已經過測試，

![](/img/ce6fc3eb10b9a1e6.webp)

並認定符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝環境中的有害干擾提供合理防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在居民區操作本裝置很可能會造成有害干擾，此時使用者將需要自費糾正這種干擾。

FCC 警告：未經合規負責方明確批准的任何更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。本裝置及其天線不得與任何其他天線或發射器共置或聯合執行。**重要提示：射頻輻射暴露。** 天線與職業使用者之間必須保持至少 20 釐米的距離，與普通公眾之間必須保持 28 釐米的距離。在此配置下，可滿足 FCC 針對人群/非受控環境規定的輻射暴露限值。**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用經本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 條，明確禁止使用未經本產品認證的任何其他天線。安裝人員應根據國家法規和天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。經批准的天線：

- MikroTik 雙極化定向天線（9.0 dBi 和 16.0）；
- 短背射定向天線（21 dBi）；
- 拋物面天線（24.5 dBi 和 27.0 dBi）。

## OEM 宣告 {#oem-statement}

本模組僅供 OEM 安裝使用。因此，OEM 整合商有責任確保終端使用者沒有可自行拆卸、安裝或修改模組的手動說明。本模組僅限於在移動或固定應用場景中安裝。OEM 整合商可使用增益等於或低於本文件列表中所示增益的天線（更多資訊請參考 47 CFR 第 15.204(c)(4) 段。MikroTik OEM 射頻模組符合 FCC 規則和法規第 15 部分。OEM 模組已獲得 FCC 認證，可與其他產品配合使用而無需進一步認證（依據 FCC 第 2.1091 節）。其他工作配置（包括涉及 47CFR 第 2.1093 段的行動式配置）以及不同的天線配置需要另行審批。OEM 必須遵守針對成品的所有 47CFR 標籤說明和要求。未經 MikroTik 明確批准的更改或修改可能會使 OEM 安裝或操作裝置的許可權失效。OEM 必須對其最終產品進行測試，以符合非故意輻射體要求（FCC 第 15.107 和 15.109 節），然後才能宣告其最終產品符合 FCC 規則第 15 部分。**警告**：OEM 必須確保滿足 FCC 標籤要求。這包括在 OEM 外殼外部加貼可見標籤，標明本產品適用的 MikroTik OEM 射頻模組 FCC 識別符號，以及上文所述任何其他必需的 FCC 宣告。本內嵌裝置符合 FCC 規則和法規 47CFR 第 15 C 段。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。標籤和文字資訊的字號應足夠大，以便於清晰辨認，並與裝置和標籤的尺寸相稱。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>LDF 5</td><td>7442A-LHG5NDM</td></tr><tr><td>LDF 5 ac</td><td>7442A-LHG5ACD</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。其執行須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

在 5150–5250 MHz 頻段內執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。還應告知使用者，高功率雷達被指定為 5250-5350 MHz 和 5650-5850 MHz 頻段的主要使用者（即優先使用者），這些雷達可能會對 LE-LAN 裝置造成干擾和/或損壞。Les dispositifs fonctionnant dans la bande de 5 150 a 5 250 MHz sont reserves uniquement pour une utilisation a l'interieur afin de reduire les risques de brouillage prejudiciable aux systemes de satellites mobiles utilisant les memes canaux. Les utilisateurs devraient aussi etre avises, d'une part, que les utilisateurs de radars de haute puissance sont designes utilisateurs principaux (c.-a-d., qu'ils ont la priorite) des bandes de 5 250 a 5 350 MHz et de 5 650 a 5 850 MHz et, d'autre part, que ces radars pourraient causer du brouillage et/ou des dommages aux dispositifs de RL-EL.

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射機功率</th></tr></thead><tbody><tr><td>5150-5350 МГц，5650-5850 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證而有所不同。

有關裝置製造日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），其後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5150-5250 МГц（23 дБм）、5250-5350 МГц（20 дБм）、5470-5725 МГц（27 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭境內使用需要按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議（該決議於 2013 年 1 月 3 日在烏克蘭司法部登記，登記號為 № 57/22589）規定的程式獲得使用許可。

### CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相應型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。詳情請參見上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.
