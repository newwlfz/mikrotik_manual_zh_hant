---
title: "SXTsq 系列"
slug: /sxtsq-series
source: https://manual.mikrotik.com/hardware/sxtsq-series
captured_at: '2026-11-04T10:06:02+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![SXTsq Lite5](/img/cc76e9d8f812a4f3.webp)

## [SXTsq 5 High Power](https://mikrotik.com/product/sxtsq_5_high_power) (RBSXTsq5HPnD) {#sxtsq-5-high-power-rbsxtsq5hpnd}

SXTsq 是一款內建定向天線的室外無線路由器。它可以用作 CPE，也可以用於點對點鏈路（在點對點場景下，使用 RouterOS 無線模式 "bridge" 即可作為單用戶端 AP 工作）。該系列產品列表：**SXTsq Lite2** **SXTsq Lite5** **SXTsq 5 ac** **SXTsq 5 High Power**

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行處理。
- 在任何牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計為安裝在室外的立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會給人員帶來危險並損壞系統。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置出現故障，請將其斷電。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所設定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置距離您的身體、職業使用者或公眾不得小於 20 釐米。

## 快速開始 {#quickstart}

- 開啟乙太網艙門。
- 用乙太網線將裝置連線到隨附 PoE 供電器的 data+power 端；
- 將 PoE 供電器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 使用 Web 瀏覽器透過 **WebFig** 或 **WinBox** 工具在 [https://mt.lv/winbox](https://mt.lv/winbox) 配置您的裝置。**提供多種配置方式以確保可訪問性；**
- 透過開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後單擊 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，然後在 "Downloads" 部分找到所需的安裝包；
- 將下載的安裝包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中進行以下設定：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![MikroTik mobile app](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱已自動填入。
- 單擊 Connect，透過無線網路與您的裝置建立連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 配置 {#configuration}

裝置已預配置為無線用戶端（CPE），您只需選擇要連線的 AP 並設定裝置密碼。您可以在預設載入的 quickSET 標籤頁中完成此操作。如果 IP 連線不可用，可以使用 WinBox 透過裝置的 MAC 地址進行連線。如果您希望從網路啟動裝置，例如使用 MikroTik Netinstall，請在啟動裝置時按住 RESET 按鈕，直到 LED 燈熄滅，然後裝置將開始查詢 Netinstall 伺服器。有關使用 RouterOS 以及連線此裝置的更多資訊，請參閱我們的文件：[https://mt.lv/help##](https://mt.lv/help##) 安裝

本裝置的 IP 防護等級為 IP54。在室外安裝時，請確保所有線纜開口朝下。我們建議使用 POE 供電器並做好正確接地。使用和安裝本裝置時，請注意最大允許暴露量（MPE）安全距離，輻射體與您身體之間至少保持 20 釐米。

裝置隨附一個金屬安裝環，可用於裝置背面的三個安裝槽之一。

- 使用十字螺絲刀鬆開金屬環。
- 將其一端穿過三個安裝槽中最方便的一個。
- 將裝置放置到將要安裝的立杆上。
- 將安裝環的鬆脫端滑回其閉合卡扣，並用螺絲刀擰緊。
- 隨附的環形支架可安裝於直徑 3-7 釐米的立杆上。

建議使用紮帶將乙太網線固定在立杆上。與裝置的距離約為 30 釐米。作為額外選項，您可以使用 "quickMOUNT-X"——便於調節的安裝支架，可單獨購買。產品網頁：[https://mikrotik.com/product/qm_x](https://mikrotik.com/product/qm_x)

![Mounting bracket](/img/8f9318498c6d2b23.webp)

![Mounting bracket adjustment](/img/ea498c8ab83d7423.webp)

專為 SQ 系列設計，可在立杆上進行垂直和水平調節。

## 供電 {#powering}

SQ 系列僅接受來自無源 PoE 供電器的 DC ⎓ 供電（隨附一個電源和一個 PoE 供電器）**SXTsq Lite2** 接受 10-30 V DC ⎓，最大負載功耗 5 W。**SXTsq Lite5** 接受 10-30 V DC ⎓，最大負載功耗 6 W。**SXTsq 5 ac** 接受 10-28 V DC ⎓，最大負載功耗 7 W。**SXTsq 5 High Power** 接受 10-28 V DC ⎓，最大負載功耗 7 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個乙太網 10/100 Mbit（**SXTsq 5 ac –** 千兆乙太網），支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通或交叉線纜連線到其他網路裝置。
- 一個整合無線介面：
- **SXTsq Lite22.4 GHz, 802.11b/g/n, antenna gain 10 dBi.**
- **SXTsq Lite55 GHz, 802.11a/n, antenna gain 16 dBi.**
- **SXTsq 5 ac5 GHz, 802.11a/n/ac, antenna gain 16 dBi.**
- **SXTsq 5 High Power5 GHz, 802.11a/n, antenna gain 16 dBi.**

## 按鈕和跳線 {#buttons-and-jumpers}

routerBOOT 復位按鈕具有以下功能。按住按鈕並通電，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並恢復預設值。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。無論使用上述哪種選項，如果在裝置通電前按住按鈕，系統都會載入備份 RouterBOOT 載入程式。這有助於 RouterBOOT 偵錯和恢復。

## 接地 {#grounding}

裝置包含一個接地連線（標記為 ⏚），您應將其連線到裝置使用地點所在塔架或建築物的接地裝置。這可以大幅降低靜電放電（ESD）和雷電損壞的風險。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下附件：

- 歐盟/美國開關電源 24V DC ⎓，0.38 A，9 W，線纜：1.5 m。
- 軟管卡箍 SUS304（十字型；夾緊直徑範圍 30-70 mm）。
- 帶遮蔽聯結器的 POE 供電器/千兆 POE 供電器。

## 規格 {#specifications}

有關 SQ 系列產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：**SXTsq Lite2** [https://mikrotik.com/product/sxtsq_lite2](https://mikrotik.com/product/sxtsq_lite2) **SXTsq Lite5** [https://mikrotik.com/product/RBSXTsq5nD](https://mikrotik.com/product/RBSXTsq5nD) **SXTsq 5 ac** [https://mikrotik.com/product/sxtsq_5_ac](https://mikrotik.com/product/sxtsq_5_ac) **SXTsq 5 High Power** [https://mikrotik.com/product/sxtsq_5_high_power](https://mikrotik.com/product/sxtsq_5_high_power)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>SXTsq Lite5</td><td>TV7LHG5NDM</td></tr><tr><td>SXTsq 5</td><td>TV7LHG5HPND</td></tr><tr><td>SXTsq 5 ac</td><td>TV7LHG5ACD</td></tr><tr><td>SXTsq Lite2</td><td>TV7SXTSQ-2ND</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制要求。這些限制旨在為住宅安裝環境提供合理的有害干擾防護。

![FCC compliance badge](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），建議使用者嘗試透過以下措施之一來糾正干擾：

- 重新調整或重新放置接收天線。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得產生有害干擾，且 (2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器同址放置或協同執行。**重要提示：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境所設定的射頻輻射暴露限值。本裝置的安裝和執行應使輻射體與您身體的任何部位之間保持至少 20 釐米的距離。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>SXTsq Lite5</td><td>7442A-LHG5NDM</td></tr><tr><td>SXTsq 5</td><td>7442A-LHG5HPND</td></tr><tr><td>SXTsq 5 ac</td><td>7442A-LHG5ACD</td></tr><tr><td>SXTsq Lite2</td><td>7442A-SXTSQ2ND</td></tr></tbody></table>

本裝置符合加拿大工業部免許可證 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得產生干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

**重要提示：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境所設定的輻射暴露限值。本裝置的安裝和執行應使輻射體與您身體的任何部位之間保持至少 20 釐米的距離。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![UKCA compliance badge](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный диапазон</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證情況而有所不同。

有關裝置製造日期的資訊，在其標籤上的序列號末尾以斜槓分隔的形式標明。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅聯盟的 MikroTik 產品均按照相關要求進行評估，並按如下所示標記 EAC 標誌：

![EAC compliance badge](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (20 dBm)、5725-5850 MHz (30 dBm)。可用頻率通道可能因產品型號和認證情況而有所不同。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置不得造成有害干擾；且
- 本裝置必須接受任何干擾，包括可能導致其非預期操作的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

Робоча частота (Максимальна вихідна потужність): 2400-2485.3 МГц (20 дБм), 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相關型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限於室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限於室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更詳細的資訊，請參見上方的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.
