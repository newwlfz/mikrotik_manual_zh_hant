---
title: "NetMetal 系列"
slug: /netmetal-series
source: https://manual.mikrotik.com/hardware/netmetal-series
captured_at: '2026-11-04T09:57:21+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/3904c50029506789.jpg)

## [NetMetal 5](https://mikrotik.com/product/RB922UAGS-5HPacD-NM) (RB922UAGS-5HPacD-NM) {#netmetal-5-rb922uags-5hpacd-nm}

:::info 本文涵蓋

- **[NetMetal 5](https://mikrotik.com/product/RB922UAGS-5HPacD-NM)**
- **[NetMetal 5SHP](https://mikrotik.com/product/RB921UAGS-5SHPacD-NM)**
- **[NetMetal 5 triple](https://mikrotik.com/product/RB922UAGS-5HPacT-NM)**
- **[NetMetal 5SHP triple](https://mikrotik.com/product/RB921UAGS-5SHPacT-NM)**
:::

NetMetal 是一款堅固的防水戶外裝置。它配備高功率無線介面和一個千兆乙太網介面，支援 MDI-X 自動檢測。裝置具有兩個或三個 RP-SMA 接頭，用於連線外接天線（取決於型號）。裝置包裝內附有 24 V 電源介面卡、PoE 供電器和兩個安裝環。共有四種型號可供選擇——兩款三鏈裝置（帶 miniPCIe 插槽和不帶），以及兩款雙鏈型號（帶 miniPCIe 插槽和不帶）。在這種情況下，裝置上還留有額外的位置用於安裝更多 RP-SMA 接頭。

## 快速開始 {#quickstart}

- 使用乙太網線將裝置連線到隨附 PoE 供電器的 data+power 端；
- 將 PoE 供電器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 透過 Web 瀏覽器使用 **WebFig** 或 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）配置裝置。**提供多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 網橋上已啟用 DHCP Client；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet, CPE" 選單中設定以下內容：選擇您所在的國家/地區，以應用國家/地區法規設定；
- 根據所使用的天線設定天線增益；
- 在底部欄位中設定路由器密碼。

## 安裝 {#mounting}

NetMetal 設計用於戶外使用，可安裝在立柱或 DIN 導軌上。

安裝時，請確保線纜進線口朝下。本裝置的 IP 防護等級為 IP66。我們建議使用 Cat6 遮蔽網線。警告！本裝置安裝和執行時，裝置與身體之間應保持至少 20 cm 的距離。在住宅環境中執行本裝置可能導致無線電干擾。本裝置的安裝和配置應由合格人員完成。包裝內附有安裝軟管卡箍。

![](/img/888d0d7f203dd8db.webp)

- 將軟管卡箍穿過裝置背面的開口。
- 固定到立柱或桅杆上。
- 使用 HEX3 螺絲刀透過軟管卡箍螺絲對齊並固定。
- 裝置應始終以 TOP 蓋朝上的方式放置。

![](/img/f15a01cb176e5195.webp)

- 安裝在 DIN 導軌上時，請在包裝中找到專用支架，並用四顆螺絲將其固定到裝置背面。

![](/img/40aa019a9c63ef9b.webp)

- 裝上安裝支架後，即可將裝置滑入 DIN 導軌。

## 供電 {#powering}

乙太網埠接受 8-30 V DC 的無源 Power over Ethernet 供電。包裝內包含一個 24 V 介面卡和一臺 PoE 供電器。裝置在 24 V 下的最大功耗為 21 W。

## 配置 {#configuration}

裝置已配置為網橋模式，所有介面均已加入網橋並啟用了 DHCP Client。RouterOS 除本文件所述內容外還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問均被阻止）。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 內建 5GHz 802.11ac/a/n 無線，支援 AP/station/bridge 模式（用於 CPE、AP、PtP 模式）
- 一個 10/100/1000 千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通線或交叉線連線其他網路裝置。乙太網埠接受來自無源 PoE 供電器的 8-30 V DC 供電。
- 一個 USB 2.0 或 3.0 埠（取決於型號），用於額外儲存或 3G/4G 調變解調器

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAPs 模式，以便透過 CAPsMAN 伺服器管理該裝置（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列在 /system resource 中。其他作業系統尚未經過測試。我們建議點選 "Check for updates" 按鈕，將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處理，例如送至指定的廢棄物處理場所。請了解您所在地區將裝置正確運送至指定處理場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制要求。這些限制旨在為商業安裝環境提供合理的有害干擾防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域執行本裝置很可能造成有害干擾，此時使用者需要自行承擔費用來糾正干擾。

FCC 警告：未經負責合規方明確批准的任何更改或修改，可能會導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。其執行需滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。

注意：本裝置在外圍裝置上使用遮蔽線纜進行了測試。為確保合規，必須使用遮蔽線纜連線本裝置。

天線安裝警告：安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用經授權的天線時，僅使用經產品認證的天線。安裝人員應根據國家/地區法規和天線型別配置天線的輸出功率水平。帶接頭的裝置需要由專業人員安裝，以確保符合健康與安全要求。

認可天線表：

<table><thead><tr><th>天線型號</th><th>型別</th><th>天線增益，dBi</th></tr></thead><tbody><tr><td>**UNII-1 (5150-5250 MHz) 和 UNII-3 (5725-5850MHz)**</td><td></td><td></td></tr><tr><td>MT-482016/N/A</td><td>全向</td><td>8.5</td></tr><tr><td>PA58-24-ANT</td><td>面板</td><td>24</td></tr><tr><td>HDDA5W-32-DP2</td><td>碟形</td><td>32</td></tr><tr><td>**UNII-2A (5250-5350 MHz) 和 UNII-2C (5470-5725MHz)**</td><td></td><td></td></tr><tr><td>HGO-antenna-OUT</td><td>全向</td><td>7</td></tr><tr><td>MTAS-5G-19D120</td><td>扇形</td><td>19</td></tr></tbody></table>

**與上表所列天線相同型別且增益更低的天線也可根據認證使用。*

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學與經濟發展部豁免許可 RSS 的豁免許可發射器/接收器。其執行需滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

在 5150–5250 MHz 頻段執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

天線安裝警告：安裝人員有責任確保在加拿大（或適用 IC 規則的地區）使用經授權的天線時，僅使用經產品認證的天線。安裝人員應根據國家/地區法規和天線型別配置天線的輸出功率水平。帶接頭的裝置需要由專業人員安裝，以確保符合健康與安全要求。

認可天線表：

<table><thead><tr><th>天線型號</th><th>型別</th><th>天線增益，dBi</th></tr></thead><tbody><tr><td>**UNII-1 (5150-5250 MHz) 和 UNII-3 (5725-5850MHz)**</td><td></td><td></td></tr><tr><td>MT-482016/N/A</td><td>全向</td><td>8.5</td></tr><tr><td>PA58-24-ANT</td><td>面板</td><td>24</td></tr><tr><td>HDDA5W-32-DP2</td><td>碟形</td><td>32</td></tr><tr><td>**UNII-2 (5250-5350 MHz) 和 UNII-2-Extended (5490-5600 MHz, 5650-5730 MHz)**</td><td></td><td></td></tr><tr><td>HGO-antenna-OUT</td><td>全向</td><td>7</td></tr><tr><td>MTAS-5G-19D120</td><td>扇形</td><td>19</td></tr></tbody></table>

**與上表所列天線相同型別且增益更低的天線也可根據認證使用。*

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный диапазон</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

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

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

Робоча частота (Максимальна вихідна потужність): 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WLAN {#wlan}

<table><thead><tr><th>Operating Frequency / Maximum output power Betriebsfrequenz / maximale Ausgangsleistung Fréquence de fonctionnement / puissance de sortie maximale Frequenza operativa / massima potenza di uscita Frecuencia de funcionamiento / potencia de salida máxima Рабочая частота / максимальная выходная мощность</th><th>5470-5725 MHz / 27 dBm</th></tr></thead></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.
