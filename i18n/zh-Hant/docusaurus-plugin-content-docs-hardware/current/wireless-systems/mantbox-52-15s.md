---
title: "MANTBox 52 15s"
slug: /mantbox-52-15s
source: https://manual.mikrotik.com/hardware/mantbox-52-15s
captured_at: '2026-11-04T09:56:02+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/21d1564b6a37c38a.webp)

## [mANTBox 52 15s](https://mikrotik.com/product/mantbox_52_15s) (RBD22UGS-5HPacD2HnD-15S) {#mantbox-52-15s-rbd22ugs-5hpacd2hnd-15s}

mANTBox 52 15s。有關完整規格和宣傳冊，請參閱 [MANTBox 52 15s 產品頁面](https://mikrotik.com/product/mantbox_52_15s)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責就安裝的結構完整性向當地主管部門/檢驗部門取得任何所需的當地或國家安全檢查。
- 將接入點安裝在任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計為安裝在戶外的立柱上。開始安裝前請仔細閱讀安裝說明。
- 未使用正確的硬體和配置，或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險。
- 本裝置需要升級到 RouterOS v6.46 或最新版本，以確保符合當地主管部門的規定。

**射頻輻射暴露：**本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境設定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或普通公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

- 開啟蓋子；
- 使用乙太網線將裝置連線到隨附 PoE 注入器的 data+power 端；
- 將 PoE 注入器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 透過 Web 瀏覽器使用 **WebFig** 或位於 [https://mt.lv/WinBox](https://mt.lv/WinBox) 的 **WinBox** 工具來配置您的裝置；**提供多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 即可訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為“**admin**”，密碼為空（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選“Check for updates”按鈕，將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡並具有活動的 Internet 連線；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在“Downloads”部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的“**Files**”選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

裝置可透過以下方式供電：

- 乙太網埠支援 802.3af/at PoE 12-57 V DC ⎓。
- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）支援 12-57 V DC⎓。最大負載下的功耗可達 21 W。

## 安裝 {#mounting}

mANTbox 隨附一個 QuickMount 介面卡，可使用隨附的螺絲將其固定到牆上，或使用隨附的金屬安裝環將其固定到立柱上。QuickMount 允許對裝置進行水平和垂直調節。

- 將快速安裝支架固定到裝置背面。

![](/img/6d8362fa9f81276e.webp)

- 將裝置固定到立柱上，並用隨附的鋼製卡箍將其固定。卡箍直徑 35 – 70 mm。

![](/img/006d6b97c4c91436.webp)

- 請避免將鬆動的乙太網線連線到乙太網埠，應將線纜固定在牆上或立柱上，以免線纜的重量拉扯埠。建議在距裝置 2m 以內固定乙太網線。這是為了確保線纜不會因其重量損壞埠，也不會脫落。我們建議使用 Cat6 遮蔽線纜。警告！本裝置的安裝和執行應保持裝置與人體之間的最小距離為 25 cm。在住宅環境中使用本裝置可能會造成無線電干擾。

## 配置 {#configuration}

我們建議點選“Check for updates”按鈕，並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議訪問 RouterOS 文件頁面以熟悉各種可能：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 internet 埠的所有訪問均被阻止）。

首次配置 [https://mt.lv/configuration](https://mt.lv/configuration)；

裝置升級 [https://mt.lv/upgrade](https://mt.lv/upgrade)；

## 接地 {#grounding}

安裝基礎設施（塔架和桅杆）以及路由器本身必須正確接地。裝置在機殼門後有一個接地線連線螺絲。將接地線連線到接地螺絲，然後將接地線的另一端連線到已接地的桅杆。這可大幅降低靜電放電和雷擊損壞的風險。

![](/img/9d368495fcc09e4b.webp)

裝置包含一個接地連線（標記為 ⏚）。

## 開啟蓋子 {#opening-cover}

要開啟蓋子，請用手逆時針轉動松不脫螺絲並將其提起。

![](/img/c9aa40a174a2b89d.webp)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 內建 5 GHz 和 2.4 GHz 無線介面。
- 一個 SFP 埠，用於 1.25GBit 模組，支援 DDMI。
- 千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通線或交叉線連線到其他網路裝置。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有以下功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置將開始尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，讓 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電前按住按鈕，系統將載入備份 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含以下隨裝置附帶的配件：

- 開關電源 DC ⎓ 24 V；
- 卡箍，35-70 mm；
- 緊固套件 K-41；
- 帶遮蔽接頭的千兆 POE 注入器線纜；
- 安裝支架。請參閱 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處理，例如送到指定的廢物處置場。請了解您所在地區將裝置正確運送到指定處置場的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBD22UGS-5HPacD2HnD-15S</td><td>TV7D2352AC</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域執行本裝置很可能會造成有害干擾，在這種情況下，使用者將需要自費糾正這種干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。其執行受以下兩個條件的約束：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。

注意：本裝置在測試時外圍裝置使用了遮蔽線纜。為確保合規，必須使用遮蔽線纜與本裝置配合。

**天線安裝警告**：安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用經授權的天線時，僅使用經本產品認證的天線。安裝人員應根據國家法規和天線型別配置天線的輸出功率水平。帶接頭的裝置需要由專業人員安裝，以確保符合健康和安全要求。

**經批准的 2.4 GHz 天線列表：**

3.6 dBi 偶極天線（型號：HGO-antenna-OUT）

5 dBi 偶極天線 HP（型號：DA-2450-05RP-SMA-01 (ACOMNIRPSMA)）

**經批准的 5 GHz 天線列表：**

6.68 dBi 偶極天線（型號：HGO-antenna-OUT）

19 dBi 扇區天線（型號：MTAS-5G-19D120）

30 dBi 拋物面天線（型號：MTAS-5G-30D3）

在符合認證的前提下，也可以使用與上述相同型別且增益更低的天線。

**重要：射頻輻射暴露。**本裝置符合 FCC 針對非受控環境設定的輻射暴露限值。本裝置的安裝和執行應保持輻射體與身體任何部位之間的最小距離為 20 cm。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBD22UGS-5HPacD2HnD-15S</td><td>7442A-D2352AC</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。其執行受以下兩個條件的約束：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

在 5150–5250 MHz 頻段執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

**天線安裝警告：**安裝人員有責任確保在加拿大（或適用 IC 規則的地區）使用經授權的天線時，僅使用經本產品認證的天線。安裝人員應根據國家法規和天線型別配置天線的輸出功率水平。帶接頭的裝置需要由專業人員安裝，以確保符合健康和安全要求。

**經批准的 2.4 GHz 天線列表：**

3.6 dBi 偶極天線（型號：HGO-antenna-OUT）

5 dBi 偶極天線 HP（型號：DA-2450-05RP-SMA-01(ACOMNIRPSMA)）

**經批准的 5 GHz 天線列表：**

6.68 dBi 偶極天線（型號：HGO-antenna-OUT）

19 dBi 扇區天線（型號：MTAS-5G-19D120）

30 dBi 拋物面天線（型號：MTAS-5G-30D3）

在符合認證的前提下，也可以使用與上述相同型別且增益更低的天線

**重要：射頻輻射暴露。**本裝置符合 IC 針對非受控環境設定的輻射暴露限值。本裝置的安裝和執行應保持輻射體與身體任何部位之間的最小距離為 20 cm。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный каналы</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## Norma Oficial Mexicana {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

Робоча частота (Максимальна вихідна потужність): 2400-2483.5 МГц (20 дБм), 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBD22UGS-5HPacD2HnD-15S 符合 2014/53/EU 指令。EU 符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均不受任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參閱上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen WLAN Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.

![](/img/0561b3ba8c95a35c.webp)

在 5150 至 5350 MHz 頻率範圍內執行時，本裝置的 WLAN 功能僅限室內使用。 / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.
