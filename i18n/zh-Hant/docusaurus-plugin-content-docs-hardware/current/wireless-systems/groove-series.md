---
title: "Groove 系列"
slug: /groove-series
source: https://manual.mikrotik.com/hardware/groove-series
captured_at: '2026-11-04T09:48:58+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **[Groove 52](https://mikrotik.com/product/RBGroove52HPnr2)**
- **[GrooveA 52](https://mikrotik.com/product/RBGrooveA-52HPnr2)** (RBGrooveA-52HPn)
- **[GrooveA 52 ac](https://mikrotik.com/product/RBGrooveGA-52HPacn)** (RBGrooveGA-52HPacn)
:::

![](/img/dd1382a945374619.jpg)

RouterBOARD Groove 預裝在室外機殼中，內建無線介面、一個 N-Male 天線接頭，以及一個支援 MDI-X 自動檢測的 10/100 乙太網介面。裝置包裝內附帶 24 V 電源介面卡、一個 PoE 注入器和兩個安裝環。有多種型號可供選擇（雙頻、單頻、AP 和 CPE 版本）。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計為安裝在室外的立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和配件，這些均可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行應與您的身體、職業使用者或公眾保持不少於 20 釐米的距離。

## 快速開始 {#quickstart}

Groove 接受來自 PoE 注入器的 8-30 V 無源 PoE。隨附的注入器應將 "Data" 端連線到交換器或其他路由器，"Data + Power" 埠則應透過所需長度（不隨附）的乙太網線纜連線到 Groove。

請按照以下快速步驟設定您的裝置：

- 在連線電源之前，將隨附的天線安裝到裝置上；
- 將 ISP 線纜連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 之外的任意埠或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；有多種配置方式可確保可訪問性；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 **WebFig**，或使用位於 [https://mt.lv/WinBox](https://mt.lv/WinBox) 的 "**WinBox**" 配置工具；
- 使用預設 IP 地址 192.168.88.1 在所選的工具中開始配置。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 單擊 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您所在的國家/地區，以應用該國家/地區的法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 供電 {#powering}

裝置可透過乙太網埠（無源 PoE）供電。在最大負載下，本裝置的功耗為 4 W。

## 安裝 {#mounting}

裝置應垂直安裝，使乙太網線纜朝下。如果您希望將 Groove 固定在立杆上，可以使用隨附的安裝環。Groove 隨附兩個安裝環——將安裝環穿過所提供的邊緣標記繞過 Groove，並繞過將要安裝的立杆。應避免將鬆弛的乙太網線纜連線到乙太網埠，並應將線纜固定在牆壁或立杆上，以免線纜的重量拉扯埠。建議在距 Groove 裝置小於 2m 的位置固定乙太網線纜。這是為了確保線纜不會因自身重量損壞埠，也不會脫落。

## 配置 {#configuration}

AP 型號的 Groove (A) 配置為無線接入點，乙太網埠配置為 DHCP 用戶端，用於連線到您的 ISP 路由器或交換器。無線介面上配置了 DHCP 伺服器。CPE 型號的 Groove 配置為用戶端，乙太網埠配置為 DHCP 伺服器。除本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問均被阻止）。

## 重設按鈕 {#reset-button}

重設按鈕有三項功能：• 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（總計 5 秒）。• 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAPs 模式，以便透過 CAPsMAN 伺服器管理該裝置（總計 10 秒）。• 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總計 15 秒）。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處理，例如送至指定的廢棄物處理場所。請了解您所在地區將裝置正確運送到指定處理場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>Groove 52</td><td>TV7GRV-A52HPN</td></tr><tr><td>GrooveA 52</td><td>TV7GRV-A52HPN</td></tr><tr><td>GrooveA 52 ac</td><td>TV7GRV-A52HPC</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝環境中的有害干擾提供合理的防護。

但是，並不保證在特定安裝環境中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來判斷），則建議使用者嘗試透過以下一種或多種措施來消除干擾：

- 調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助 **FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。其操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，(2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期操作的干擾。

注意：本裝置已使用外圍裝置的遮蔽線纜進行了測試。為確保合規，本裝置必須使用遮蔽線纜。

**天線安裝警告**：安裝者有責任確保在美國（或適用 FCC 規則的地區）使用經認可的天線時，僅使用經該產品認證的天線。安裝者應根據國家法規並按天線型別配置天線的輸出功率水平。帶有接頭的裝置需要由專業人員安裝，以確保符合健康與安全要求。

**認可的 2.4 GHz 天線清單：**

-

15 dBi 全向天線（型號：WLO-2450-15）

-

13 dBi 全向 HP 天線（型號：ODH 24-13）

-

20 dBi 平板天線（型號：WLP-2450-20）

-

17 dBi 扇區天線（型號：SA 24-90-17-WB）

-

24 dBi 碟形天線（型號：DC 24-HD-PFIP）**認可的 5 GHz 天線清單：**

-

8.5 dBi 全向天線（型號：MT-482016/N/A）

-

24 dBi 平板天線（型號：PA58-24-ANT）

-

32 dBi 碟形天線（型號：HDDA5W-32-DP2）在獲得認證的前提下，也可以使用與上述型號相同型別且增益更低的天線。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>Groove 52</td><td>7442A-GRVA52HPN</td></tr><tr><td>GrooveA 52</td><td>7442A-GRVA52HPN</td></tr><tr><td>GrooveA 52 ac</td><td>7442A-GRVA52HPC</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 標準的免許可發射器/接收器。其操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

工作在 5150–5250 MHz 頻段的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

天線安裝警告：安裝者有責任確保在加拿大（或適用 IC 規則的地區）使用經認可的天線時，僅使用經該產品認證的天線。安裝者應根據國家法規並按天線型別配置天線的輸出功率水平。帶有接頭的裝置需要由專業人員安裝，以確保符合健康與安全要求。

**認可的 2.4 GHz 天線清單：**

-

15 dBi 全向天線（型號：WLO-2450-15）

-

13 dBi 全向 HP 天線（型號：ODH 24-13）

-

20 dBi 平板天線（型號：WLP-2450-20）

-

17 dBi 扇區天線（型號：SA 24-90-17-WB）

-

24 dBi 碟形天線（型號：DC 24-HD-PFIP）**認可的 5 GHz 天線清單：**

-

8.5 dBi 全向天線（型號：MT-482016/N/A）

-

24 dBi 平板天線（型號：PA58-24-ANT）

-

32 dBi 碟形天線（型號：HDDA5W-32-DP2）在獲得認證的前提下，也可以使用與上述型號相同型別且增益更低的天線。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный диапазон</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

認證證書編號 (IFT)：請參閱產品標籤。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

Робоча частота (Максимальна вихідна потужність): 2400-2483.5 МГц (20 дБм), 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相應型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。如需更詳細的資訊，請參見上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

![](/img/0561b3ba8c95a35c.webp)

在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。 / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.
