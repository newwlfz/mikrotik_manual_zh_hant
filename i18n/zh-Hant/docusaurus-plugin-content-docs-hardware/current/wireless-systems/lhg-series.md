---
title: "LHG 系列"
slug: /lhg-series
source: https://manual.mikrotik.com/hardware/lhg-series
captured_at: '2026-11-04T09:54:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **[LHG 2](https://mikrotik.com/product/lhg_2)** (RBLHG-2nD)
- **[LHG 5](https://mikrotik.com/product/RBLHG-5nD)** (RBLHG-5nD)
- **[LHG HP5](https://mikrotik.com/product/RBLHG-5HPnD)** (RBLHG-5HPnD)
- **[LHG 5 ac](https://mikrotik.com/product/lhg_5_ac)** (RBLHGG-5acD)
:::

## 安全警告 {#safety-warnings}

-

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。

-

本產品的最終處置應遵守所有國家法律和法規。

-

在任何牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。

-

裝置的安裝必須符合當地和國家的電氣規範。

-

本產品設計用於在室外安裝在立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險情況並對系統造成損壞。

-

請僅使用製造商批准並可在本產品原包裝中找到的電源和附件。

-

在將系統連線到電源之前，請閱讀安裝說明。

-

我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！

-

如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。

-

客戶有責任遵守當地國家/地區的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

-

LHG 是一款內建定向天線的室外無線路由器。它可用作 CPE，或用於點對點鏈路（使用 RouterOS 無線模式 "bridge" 作為單用戶端 AP 用於點對點場景）。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或普通公眾的距離不得小於 40 釐米。

## 快速開始 {#quickstart}

- 開啟乙太網艙門，將乙太網線纜連線到乙太網埠，並將乙太網線纜的另一端連線到隨附的 PoE 供電模組。
- 使用乙太網線纜將裝置連線到隨附 PoE 供電模組的資料+電源端；
- 將 PoE 供電模組的資料端連線到計算機；
- 將電源介面卡連線到 PoE 供電模組；
- 使用網頁瀏覽器透過 **WebFig** 或 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）配置您的裝置。**提供多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後單擊 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單中，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中進行以下設定：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 組裝與安裝 {#assembly-and-mounting}

- 將兩條支腿安裝到 LHG 外殼上。

![](/img/4b843b31ec032a91.jpg)

## [LHG 5](https://mikrotik.com/product/RBLHG-5nD) (RBLHG-5nD) {#lhg-5-rblhg-5nd}

- 將組裝好的 LHG 單元在相應位置卡入網格。
- 用兩顆自攻螺釘將支腿固定到位（使用 PH2 十字螺絲刀）。

![](/img/4333f6bb76f982d7.webp)

本裝置設計為使用紮帶或鋼製卡箍安裝在立杆上，如圖所示。隨附鋼製卡箍的夾緊直徑為 35 – 70 mm。

![](/img/e29801f908debc24.webp)

- 將隨附的鋼製卡箍穿過裝置。
- 將裝置固定到立杆上。
- 對齊並擰緊卡箍以固定裝置。可選：如有需要，在安裝裝置之前，您可以將隨附的 5 度調節介面卡插入安裝環所插入的頂部或底部槽口中。當裝置擰緊到垂直立杆上時，這將產生額外的向上或向下角度。

![](/img/0aaffeda7585ef66.webp)

本裝置包含一個接地連線（標記為 ⏚），您應將其連線到裝置使用所在塔架或建築物的接地裝置。這可大幅降低靜電放電和雷擊損壞的風險。警告！本裝置的安裝和操作位置與您的身體之間應保持至少 40 cm 的距離。在住宅環境中操作本裝置可能會導致無線電干擾。

將乙太網線纜連線到艙門下方的乙太網埠，並如圖所示從支腿中穿過：

![](/img/6a72f386ce5fdaa5.webp)

可另行購買額外的安裝支架：

LHG 安裝支架

![](/img/bb1a08169dd25567.webp)

solidMOUNT

![](/img/bb890f595de6c700.webp)

## 供電 {#powering}

本裝置僅接受來自無源 PoE 供電模組的供電。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線纜連線到 POE 介面卡的 POE 埠。
- 將來自您區域網路的乙太網線纜連線到 POE 介面卡的 LAN 埠，請注意資料與電源流向的箭頭。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

登入後，我們建議單擊 QuickSet 選單中的 "Check for updates" 按鈕，因為將您的 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置使用所在的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，讓您熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參閱相關章節。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通或交叉線纜連線到其他網路裝置。
- 一個整合的 2x2 MIMO 無線裝置，內建柵格天線。LHG 2 雙鏈 18 dBi，2.4GHz，802.11b/g/n。最大功耗 5 W。LHG 5 雙鏈 24.5 dBi，5GHz，802.11 a/n。最大功耗 6 W。LHG HP5 雙鏈 24dBi，5GHz，802.11 a/n。最大功耗 7 W。LHG 5 ac 雙鏈 24.5dBi，5GHz，802.11 a/n/ac。最大功耗 8 W。

## Reset 按鈕 {#reset-button}

Reset 按鈕有三個功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAPs 模式（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論採用上述哪種方式，如果在裝置通電前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的附件：

- LHG-5 安裝套件。
- POE 供電模組/千兆 POE 供電模組（適用於 LHGG-5acD）。
- LHG-5G-390 mm 碟形天線 3,0x2.5x0,5 mm。
- DC ⎓ EU/US 開關電源 24 V，0.38 A，9 W，Level VI，線纜：1.5 m）。
- 軟管卡箍 SUS304（philips 型；夾緊直徑範圍 35-70 mm）。

## 規格 {#specifications}

有關 LHG 產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/lhg_2](https://mikrotik.com/product/lhg_2) [https://mikrotik.com/product/RBLHG-5nD](https://mikrotik.com/product/RBLHG-5nD) [https://mikrotik.com/product/RBLHG-5HPnD](https://mikrotik.com/product/RBLHG-5HPnD) [https://mikrotik.com/product/lhg_5_ac](https://mikrotik.com/product/lhg_5_ac)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

![](/img/8d294e5cd375c591.webp)

![](/img/25f50553ffd86eaf.webp)

![](/img/b0984aa3ad3c6d58.webp)

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置正確運輸至指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>LHG 2</td><td>TV7LHG2ND</td></tr><tr><td>LHG 5</td><td>TV7LHG5NDM</td></tr><tr><td>LHG 5 ac</td><td>TV7LHG5ACD</td></tr><tr><td>LHG HP5</td><td>TV7LHG5HPND</td></tr></tbody></table>

![](/img/ce6fc3eb10b9a1e6.webp)

**LHG 5** 和 **LHG 5 ac** 已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝中的有害干擾提供合理保護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域操作本裝置很可能會造成有害干擾，此時使用者需要自費糾正干擾。

**LHG 2** 和 **LHG HP5** 已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝中的有害干擾提供合理保護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。然而，無法保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來判斷），建議使用者嘗試透過以下措施之一來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以獲得幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與其他任何天線或發射器共址或聯合執行。**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和操作位置與輻射體及您身體任何部位之間的距離應至少為 40 cm。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>LHG 2</td><td>7442A-LHG2ND</td></tr><tr><td>LHG 5</td><td>7442A-LHG5NDM</td></tr><tr><td>LHG 5 ac</td><td>7442A-LHG5ACD</td></tr><tr><td>LHG HP5</td><td>7442A-LHG5HPND</td></tr></tbody></table>

本裝置符合加拿大工業部免許可證 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement. **重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和操作位置與輻射體及您身體任何部位之間的距離應至少為 40 cm。**IMPORTANTE:** Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 40 cm entre le radiateur et toute partie de votre corps.

**LHG 5** 和 **LHG 5 ac**。此 A 類數字裝置符合加拿大 ICES-003 標準。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**LHG 2** 和 **LHG HP5**。此 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

在 5150–5250 MHz 頻段執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。Les dispositifs fonctionnant dans la bande de 5 150 a 5 250 MHz sont reserves uniquement pour une utilisation a l'interieur afin de reduire les risques de brouillage prejudiciable aux systemes de satellites mobiles utilisant les memes canaux.

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный каналы</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

有關裝置製造日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

如需瞭解保修服務的詳細資訊，請聯絡您的銷售商。

![](/img/984ad54320693690.webp)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化管理委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA, Unijas iela 2, 里加, 拉脫維亞, LV1039.

Робоча частота (Максимальна вихідна потужність): 2400-2483.5 МГц (30 дБм), 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz（僅 LHG 2）</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用無任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用無任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家/地區的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 TX 功率限值。有關更多詳細資訊，請參閱上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

![](/img/0561b3ba8c95a35c.webp)

在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。/ Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.
