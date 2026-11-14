---
title: "LHG XL 5 ac"
slug: /lhg-xl-5-ac
source: https://manual.mikrotik.com/hardware/lhg-xl-5-ac
captured_at: '2026-11-04T09:54:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/ec158eb4a218ea81.jpg)

## [LHG XL 5 ac](https://mikrotik.com/product/lhg_xl_5_ac) (RBLHGG-5acD-XL) {#lhg-xl-5-ac-rblhgg-5acd-xl}

雙鏈路長距離 27dBi 5GHz CPE/點對點一體化天線，支援 AC 和千兆乙太網。完整規格和產品手冊請參閱 [LHG XL 5 ac 產品頁面](https://mikrotik.com/product/lhg_xl_5_ac)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣線路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家和地方的法律法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於室外安裝在杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和配件，這些電源和配件可在本產品的原始包裝中找到。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座上拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 本裝置為 A 類裝置。在住宅環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行時，與您的身體、職業使用者或公眾的距離不應小於 20 釐米。

## 組裝 {#assembly}

將兩條支腿安裝到 LHG 外殼上，然後將組裝好的 LHG 單元卡入網格的適當位置。用兩顆自攻螺絲固定支腿（隨附，使用 PH2 十字螺絲刀）。使用隨附的螺絲將 L 形支架安裝到天線上。使用 U 型螺栓將單元固定到杆/桅杆上。

## 安裝 {#mounting}

為符合健康法規，請將本裝置安裝在距離身體至少 20 釐米的位置。

## 快速開始 {#quickstart}

- 開啟乙太網門，將乙太網線連線到乙太網埠，並將乙太網線的另一端連線到隨附的 PoE 供電器。
- 使用乙太網線將裝置連線到隨附 PoE 供電器的 data+power 端；
- 將 PoE 供電器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 供電器；
- 透過 **WebFig** 或 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)），使用 Web 瀏覽器配置您的裝置。**提供多種配置方法以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，導航到 **Neighbors** 標籤頁，然後單擊 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 要手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個乙太網埠，支援自動交叉/直通線纜校正 (Auto MDI/X)，因此您可以使用直通或交叉線纜連線到其他網路裝置。
- 一個內建網格天線的一體化無線裝置。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAPs 模式（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備用 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統未經測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場所。請了解您所在地區將裝置正確運輸到指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBLHGG-5acD-XL</td><td>TV7LHG5ACD</td></tr></tbody></table>

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝環境中的有害干擾提供合理保護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置可能會造成有害干擾，此時使用者將需要自費糾正干擾。

FCC 警告：未經合規負責方明確批准的任何更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的規定。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，以及 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或協同執行。**重要提示：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和執行時，輻射器與您身體任何部位之間的最小距離應為 20 釐米。本封閉式裝置符合 FCC 規則和法規 47CFR 第 15 段 C 的規定。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，以及 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBLHGG-5acD-XL</td><td>7442A-LHG5ACD</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，以及 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**重要提示：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和執行時，輻射器與您身體任何部位之間的最小距離應為 20 釐米。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный каналы</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>5650-5850 МГц</td><td>≤10 Вт</td></tr></tbody></table>

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

## 烏克蘭國家通訊和資訊國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

Робоча частота (Максимальна вихідна потужність): 5470-5725 МГц (27 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV-1039.

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBLHGG-5acD-XL 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>![](/img/706f99e51a4ac5b7.webp) 頻率範圍（**適用於相應型號**）</th><th>使用的通道</th><th>最大輸出功率 (EIRP)</th><th>限制</th></tr></thead><tbody><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線裝置必須由專業人員安裝！** *根據委員會決定 2000/299/EC（2000 年 4 月 6 日），本產品屬於第 2 類範圍。*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參閱上方的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.
