---
title: "RB4011iGS+5HacQ2HnD-IN"
slug: /rb4011igs-plus-5hacq2hnd-in
source: https://manual.mikrotik.com/hardware/rb4011igs-plus-5hacq2hnd-in
captured_at: '2026-11-04T06:03:57+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/de2251b3df2b7d46.jpg" alt="" width={799} height={497} /></p>

## [RB4011iGS+5HacQ2HnD-IN](https://mikrotik.com/product/rb4011igs_5hacq2hnd_in) (RB4011iGS+5HacQ2HnD-IN) {#rb4011igs5hacq2hnd-in-rb4011igs5hacq2hnd-in}

裝置已預配置基本設定，您只需插入 ISP 網線即可開始使用網際網路。我們建議您設定密碼以保護裝置安全。完整規格和宣傳冊請參見 [RB4011iGS+5HacQ2HnD-IN 產品頁面](https://mikrotik.com/product/rb4011igs_5hacq2hnd_in)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於機架安裝。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的步驟可能會導致人員危險和系統損壞。
- 本產品僅適合室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境設定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，應與您的身體、職業使用者或公眾保持不少於 20 釐米的距離。

## 設定 {#setup}

- 確保您的網際網路服務提供商（ISP）允許硬體更換並自動分配 IP 地址；
- 將 ISP 網線連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 以外的任意埠或無線網路“MikroTik-...”（請務必檢視貼紙上的無線密碼）連線到裝置；
- 使用移動應用程式建立連線。或者使用網頁瀏覽器中的 WebFig 或 [https://mt.lv/winbox](https://mt.lv/winbox) 上的“WinBox”配置工具。**提供多種配置方式以確保可訪問性；**
- 使用預設 IP 地址 192.168.88.1 在所選的工具中開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇“Neighbors”標籤頁以查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為“admin”，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選“Check for updates”按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在“Downloads”部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的“Files”選單，並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保最佳效能、穩定性和安全更新；
- 在“QuickSet”選單中進行以下設定：選擇您的國家，以應用國家法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 供電 {#powering}

最大負載下的功耗可達 44 W。裝置可透過電源插孔或第一個乙太網埠供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 12-57 V DC。
- 第一個乙太網埠接受 18-57 V DC 的 Power over Ethernet 供電。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置上的乙太網線連線到 POE 介面卡的 POE 埠。
- 將來自您區域網路的乙太網線連線到 POE 介面卡的 LAN 埠，請注意資料和電力流向的箭頭。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的“Check for updates”按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將要使用的國家，以符合當地法規。RouterOS 除本文件所述內容外，還包含許多配置選項。我們建議從此處開始瞭解各種可能性：[https://mt.lv/help](https://mt.lv/help)。如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從區域網路側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以啟動裝置進行重新安裝，請參見按鈕和跳線。

## 安裝 {#mounting}

可以使用裝置背面的螺釘孔將裝置固定到牆上。裝置應以線纜開口朝下的方式安裝。裝置沒有防水保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat5/6 遮蔽電纜。本裝置的安裝和配置應由合格人員完成。*外殼包含一個 M4 螺紋的接地螺釘孔（不含螺釘）。在存在 ESD 放電風險的場所，建議您將接地螺釘連線到經過驗證的接地設施。* 本裝置安裝和操作時，裝置與您身體之間的最小距離應為 20 釐米。在住宅環境中操作本裝置可能會導致無線電干擾。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 乙太網埠分為兩組，每組五個，每組透過一個交換晶片連線。這些埠可以單獨配置，並支援自動交叉/直通電纜校正（Auto MDI/X），因此您可以使用直通或交叉電纜連線到其他網路裝置。
- SFP+ 埠接受 SFP 和 SFP+ 模組。請參閱 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。
- RJ45 控制檯埠用於序列控制檯訪問，預設為 115200 bit/s、8 個數據位、1 個停止位、無校驗。
- 整合 QCA9984 雙頻 4x4，支援 4 個 SS MIMO，5 GHz 802.11a/n/ac。
- 一個 MiniPCIe 插槽，已安裝 MiniPCIe 卡 R11e-2HnD，2.4 GHz 802.11b/g/n。僅支援 Mini PCIe 卡。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請使裝置進入 BOOTP 模式。有兩種引導選項可用：**常規載入程式**和**備份載入程式**。建議在其中一個無法工作時驗證這兩個選項。

- **常規載入程式：** 要進入 etherboot 模式，請在裝置通電並等待 1–2 秒後按下 **Reset** 按鈕。
- **備份載入程式：** 關閉裝置電源。按下並按住 **Reset** 按鈕，然後給裝置通電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。根據型號不同，這可能會透過 **USR、USER、System** 或 **ACT** LED 或 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統未經測試。

## 配件 {#accessories}

包裝包含以下隨附配件：

- 電源介面卡 24 V DC ⎓ 2.5 A 60 W 80 % VI 121x54x33 線纜 2 m 插頭 RA 2.1 mm。
- EU/US 電源線，D03+QT3 H05VV-F 3x0.75mm2 1.83m RoHS。
- 安裝套件 K-59 緊固套裝。請參閱 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## MikroTik 移動應用 {#mikrotik-mobile-app}

<p><Img src="/img/8d294e5cd375c591.webp" alt="" width={247} height={244} /></p>

<p><Img src="/img/25f50553ffd86eaf.webp" alt="" width={241} height={80} /></p>

<p><Img src="/img/b0984aa3ad3c6d58.webp" alt="" width={239} height={81} /></p>

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

## 注意 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置的工作範圍與上述規定不同，則需要將製造商/供應商提供的定製韌體版本應用到終端使用者裝置上，並防止終端使用者重新配置。
- 室外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料表均可在製造商官方網站上獲取。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，發射功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，發射功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，發射功率限制為 20dBm（EIRP）。

請確保裝置具有鎖定軟體包（來自制造商的韌體版本），該軟體包需要應用到終端使用者裝置上，以防止終端使用者重新配置。產品將標有國家程式碼“-EG”。本裝置需要升級到最新版本，以確保符合當地主管部門的法規！終端使用者有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如在指定的廢物處置場所處置。請了解將裝置妥善運輸到您所在地區指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th><th>包含 FCCID</th></tr></thead><tbody><tr><td>RB4011iGS+5HacQ2HnD-IN</td><td>TV74011GS-5HQ2HD</td><td>TV7R11E2HPND</td></tr></tbody></table>

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的有害干擾防護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整或重新放置接收天線。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。**FCC 警告：** 任何未經合規責任方明確批准的更改或修改都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾，(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或協同操作。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境設定的射頻輻射暴露限值。本裝置安裝和操作時，輻射體與您身體任何部位之間的最小距離應為 20 釐米。

**天線安裝。警告：** 安裝者有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用與本產品一起認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用未經本產品認證的任何其他天線。安裝者應根據國家法規和天線型別配置天線的輸出功率水平。帶有聯結器的裝置需要專業安裝，以確保符合健康和安全要求。包含 FCC ID TV7R11E2HPND。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th><th>包含 IC</th></tr></thead><tbody><tr><td>RB4011iGS+5HacQ2HnD-IN</td><td>7442A-4011G5Q2</td><td>7442A-R11E2HPND</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得造成干擾，(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境設定的輻射暴露限值。本裝置安裝和操作時，輻射體與您身體任何部位之間的最小距離應為 20 釐米。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный диапазон</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, , 5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用頻率通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

Робоча частота (Максимальна вихідна потужність): 2400-2483.5 МГц (20 дБм), 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RB4011iGS+5HacQ2HnD-IN 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.

<p><Img src="/img/0561b3ba8c95a35c.webp" alt="" width={146} height={135} /></p>

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.
