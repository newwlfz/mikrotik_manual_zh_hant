---
title: "LDF 2"
slug: /ldf-2
source: https://manual.mikrotik.com/hardware/ldf-2
captured_at: '2026-11-04T09:53:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/6c7660fdb10c5220.webp)

## [LDF 2](https://mikrotik.com/product/ldf_2) (RBLDF-2nD) {#ldf-2-rbldf-2nd}

LDF（Lite dish feed）是一款帶有內建天線的室外無線系統，設計用於安裝在衛星偏饋天線上。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行處理。
- 在任意牆面上安裝接入點的所有安裝方式均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於在室外立杆上安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能對人員造成危險情況並損壞系統。
- 僅使用製造商認可並在本產品原包裝中提供的電源和配件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置出現故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 遵循當地國家法規是客戶的責任，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行距離，與您的身體、職業使用者或公眾不得小於 20 釐米。

## 組裝 {#assembly}

本裝置相容常用於衛星電視的標準偏饋天線。偏饋支架為通用的 40 mm 直徑，LDF 可以輕鬆放入其中。要將乙太網線連線到 LDF 裝置，請按以下步驟操作：

- 按圖示組裝所有元件。如果使用成品線纜，請在一側切開橡膠密封圈，將其套到線纜上。自行壓接的線纜應在密封圈套到線纜上之後再進行壓接；
- 將乙太網線連線到 LDF 上的乙太網介面；
- 順時針旋轉，將外殼螺母安裝到 LDF 主體上；
- 將橡膠密封圈滑入外殼螺母，然後順時針旋轉壓緊螺母，密封防水接頭。

![](/img/4697c94b5539fc15.webp)

## 在天線上組裝 {#assembling-on-dish}

請確保按右圖所示將 LDF 裝置安裝在偏饋支架上的正確位置。裝置應朝上對著天線。

![](/img/28d101453837d87d.webp)

![](/img/1a2a13170697f321.webp)

天線將作為反射器，放大訊號。元件的最終位置應按左圖所示放置並安裝到立杆或牆壁上。

## 安裝 {#mounting}

本裝置的 IP 防護等級為 IP54。本裝置設計用於室外使用，請確保所有線纜開口朝下。請使用帶 Cat6 線纜的 PoE 供電器。安裝基礎設施（塔架和桅杆）以及路由器本身都必須正確接地。

*本裝置的安裝和配置應由具備資質的人員完成。* *警告！本裝置的安裝和執行應保持裝置與身體之間的最小距離為 40 釐米。在住宅環境中執行本裝置可能造成無線電干擾。*

## 供電 {#powering}

本裝置接受來自無源 PoE 供電器的 10-28 V ⎓ DC 輸入。本裝置不能與符合 IEEE802.3af 的 48 V 供電器配合使用。包裝內含一個 PoE 供電器。最大功耗為 7 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠；
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 使用乙太網線將裝置連線到附帶的 PoE 供電器的 data+power 端；
- 將 PoE 供電器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 透過 **WebFig** 或 **WinBox** 工具（[https://mt.lv/WinBox](https://mt.lv/WinBox)）使用網頁瀏覽器配置您的裝置；提供多種配置方式以確保可訪問性；
- 開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 "**admin**"，密碼為空（某些型號請在貼紙上檢視使用者名稱和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保最佳的效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳的效能和穩定性。對於無線型號，請確保已選擇裝置將要使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始瞭解各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下所有來自 Internet 埠的訪問均被阻止）。出於恢復目的，可以啟動裝置進行重新安裝，請參閱相關章節。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 整合 2.4 GHz、802.11b/g/n 無線。
- 一個乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X），因此您可以使用直通線或交叉線連線到其他網路裝置。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）；
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置將開始查詢 CAPsMAN 伺服器（共 10 秒）；
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）；無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。這可用於 RouterBOOT 偵錯和恢復。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/ldf_2](https://mikrotik.com/product/ldf_2)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢物處置場所。請了解您所在地區將裝置正確運輸至指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBLDF-2nD</td><td>TV7LDF2ND</td></tr></tbody></table>

本裝置經測試，被認定符

![](/img/ce6fc3eb10b9a1e6.webp)

合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝中的有害干擾提供合理防護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來確定），則建議使用者嘗試透過以下一種或多種措施來消除干擾：

-

重新調整接收天線的方向或位置。

-

增大裝置與接收器之間的距離。

-

將裝置連線到與接收器所連線電路不同的插座上。

-

諮詢經銷商或有經驗的無線電/電視技術人員以獲得幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的要求。執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致不良執行的干擾。本裝置及其天線不得與其他任何天線或發射器位於同一位置或聯合執行。**重要：射頻輻射暴露。** 天線與職業使用者之間必須保持至少 20 釐米的距離。在此配置下，可滿足 FCC 針對人群/非受控環境規定的輻射暴露限值。**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用透過本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，嚴禁使用除本產品認證天線以外的任何天線。安裝人員應根據國家/地區法規和天線型別配置天線的輸出功率水平。帶聯結器的裝置必須由專業人員安裝，以確保符合健康與安全要求。認可的天線列表：

-

25 dBi 碟形天線，Winegard 型號：DS2076

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBLDF-2nD</td><td>7442A-LDF2ND</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。執行須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置不良執行的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement. Cet equipement est conforme aux limites d'exposition au rayonnement IC definies pour un environnement non controle. Cet equipement doit etre installe et utilise a une distance minimale de 40 cm entre le radiateur et toute partie de votre corps.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**本無線電發射器 7442A-LDF2ND 已獲加拿大創新、科學和經濟發展部批准，可與下列天線型別配合使用，並註明了最大允許增益。未列入此清單且增益大於所列任何型別最大增益的天線型別，嚴禁與本裝置配合使用。** 認可的天線列表：

- 25 dBi 碟形天線，Winegard 型號：DS2076 **重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和執行應保持輻射體與您身體任何部位之間的最小距離為 20 釐米。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный каналы</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>2400-2483.5 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

Робоча частота (Максимальна вихідна потужність): 2412-2472 МГц (20 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBLDF-2nD 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用型號）**</th><th>**使用的通道**</th><th>**最大輸出功率 (EIRP)**</th><th>**限制**</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

**遵循當地國家法規是客戶的責任，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參閱上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.
