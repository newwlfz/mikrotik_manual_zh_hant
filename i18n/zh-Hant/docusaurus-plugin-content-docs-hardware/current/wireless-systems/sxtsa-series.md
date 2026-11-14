---
title: "SXTSA 系列"
slug: /sxtsa-series
source: https://manual.mikrotik.com/hardware/sxtsa-series
captured_at: '2026-11-04T10:04:58+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/c1df2084a462a484.webp)

## [SXTsq 5 ac](https://mikrotik.com/product/sxtsq_5_ac) (RBSXTsqG-5acD) {#sxtsq-5-ac-rbsxtsqg-5acd}

**SXT 系列：SXT SA5、SXT SA5 ac** SXT 是一款室外無線路由器，可在 PtM 部署中作為 CPE 使用，也可用於點對點鏈路。請確保裝置安裝正確，線纜應垂直朝下。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 在任意牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於安裝在室外的立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和配件，這些電源和配件可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請將其斷電。最快的斷電方式是從電源插座上拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻段內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。
- 本裝置為 A 類裝置。在居住環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。

## 組裝與安裝 {#assembly-and-mounting}

將卡扣朝前，把安裝支架滑入機殼底部的導軌中，直到卡扣咔噠一音效卡入到位。SXT 隨附喉箍，將喉箍穿過支架上的開口並環繞將安裝的立杆。對準完成後擰緊喉箍螺釘。另有兩個螺孔，用於額外防止支架意外移動。SXT 裝置有一個滑動門，乙太網埠和復位跳線位於門後。該門也可以用螺釘擰入預留的螺孔中固定關閉。

## 快速開始 {#quickstart}

- 開啟乙太網門，將乙太網線連線到乙太網埠，再將乙太網線的另一端連線到隨附的 PoE 供電器。
- 用乙太網線將裝置連線到隨附 PoE 供電器的資料+電源端；
- 將 PoE 供電器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 透過 **WebFig** 或 **WinBox** 工具使用網頁瀏覽器配置您的裝置，地址為 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 即可訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請在標籤上檢視使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 供電 {#powering}

本裝置僅接受來自無源 PoE 供電器的 8-32 V 電源（隨附一個電源和一個 PoE 供電器）。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個乙太網口（10/100 Mbit 或千兆，取決於型號），支援自動交叉/直通線纜糾正（Auto MDI/X），因此您可以使用直通線或交叉線連線其他網路裝置。
- 一個整合無線模組，配備內建定向天線，最大增益 16 dBi。

## 按鈕和跳線 {#buttons-and-jumpers}

routerBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並恢復預設值。
- 當 LED 熄滅（約 20 秒）後鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網重新安裝 RouterOS 時必需）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。裝置在乙太網埠門後有一個接地連線（根據型號不同，為螺釘或金屬環），您應將其連線到裝置使用所在塔架或建築的接地裝置。這可以大幅降低 ESD 和雷擊損壞的風險。

## 作業系統支援 {#operating-system-support}

本裝置僅支援版本號等於或高於 RouterOS 選單 /system resource 中所標示版本的 RouterOS 軟體。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢棄物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBSXTG-5HPnD-SAr2</td><td>TV7SXTG-5HPND</td></tr><tr><td>RBSXTG-5HPacD-SAr2</td><td>TV7SXTG-5HACD</td></tr></tbody></table>

***型號 RBSXTG-5HPnD-SAr2（SXT SA5）：***

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則建議使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。**重要：射頻輻射暴露。** 天線與使用者之間必須保持至少 75 cm 的距離。在此配置下，可滿足 FCC 針對人群/非受控環境規定的輻射暴露限值。

***型號 RBSXTG-5HPacD-SAr2（SXT SA5 ac）：***

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝中的有害干擾提供合理保護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在居住區操作本裝置很可能造成有害干擾，此時使用者將被要求自費糾正干擾。

**重要：射頻輻射暴露。** 天線與使用者之間必須保持至少 20 cm 的距離。在此配置下，可滿足 FCC 針對人群/非受控環境規定的輻射暴露限值。

**FCC 警告：** 任何未經合規負責方明確批准的更改或修改，都可能導致使用者操作本裝置的許可權失效。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受所接收到的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共址放置或協同工作。

**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地方）使用授權天線時，僅使用經本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用任何未隨本產品認證的天線。安裝人員應根據國家法規並按照天線型別配置天線的輸出功率級別。帶聯結器的裝置必須由專業人員安裝，以確保符合健康和安全要求。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBSXTG-5HPnD-SAr2</td><td>7442A-SXTG5HPND</td></tr><tr><td>RBSXTG-5HPacD-SAr2</td><td>7442A-SXTG5HACD</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，並且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

***型號 RBSXTG-5HPnD-SAr2（SXT SA5）：***

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露**。天線與使用者之間必須保持至少 33 cm 的距離。在此配置下，可滿足 FCC 針對人群/非受控環境規定的輻射暴露限值。

***型號 RBSXTG-5HPacD-SAr2（SXT SA5 ac）：***

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**重要：射頻輻射暴露。** 天線與使用者之間必須保持至少 22 cm 的距離。在此配置下，可滿足 FCC 針對人群/非受控環境規定的輻射暴露限值。

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

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

Робоча частота (Максимальна вихідна потужність): 5470-5725 МГц (27 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用無任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家法規，包括在合法頻段內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。如需更詳細的資訊，請參閱上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.
