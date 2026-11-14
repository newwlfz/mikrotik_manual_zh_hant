---
title: "wAP LR9 套件"
slug: /wap-lr9-kit
source: https://manual.mikrotik.com/hardware/wap-lr9-kit
captured_at: '2026-11-04T10:07:31+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可下載為 <a href="/assets/files/wap-lr9-kit-122ca84be22e5dcfa960c751ce766fdb.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/bb08cf678e80bbc2.webp)

### [wAP LR9 kit](https://mikrotik.com/product/wap_lr9_kit) (RBwAPR-2nD&R11e-LR9) {#wap-lr9-kit-rbwapr-2ndr11e-lr9}

wAP 是一款小型防風雨裝置，內建 LR9 卡，可將 UDP 封包轉發到所選伺服器。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 在任意牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品預期安裝在室外的立柱上，但也可在室內安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確步驟，可能導致人員處於危險境地並對系統造成損壞。
- 僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 這是 A 類裝置。在居住環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。安裝和操作本 MikroTik 裝置時，其與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

- 請確保您的 ISP 允許更換硬體，並會自動分配 IP 地址。
- 開啟底部蓋子。
- 將外部天線連線到 SMA 接頭。
- 將裝置連線到電源。
- 使用您的裝置連線到 MikroTik 無線網路
- 配置必須透過無線網路使用 Web 瀏覽器或移動應用完成。或者，您可以使用 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。預設情況下，乙太網埠訪問被防火牆阻止。
- 連線到無線網路後，在 Web 瀏覽器中開啟 192.168.88.1 以開始配置。
- 使用者名稱：a*dmin*，預設沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）。
- 使用移動應用時，請選擇 Quick setup，它將在六個簡單步驟中引導您完成所有必要的配置。
- 在產品內部的標籤上找到您的 LR 閘道器 ID，並將其註冊到您的 Network Server 中。
- 使裝置連線到 LR Network Server。
- 點選 "Check for updates" 按鈕並將您的 RouterOS 軟體更新到最新版本，裝置需要有可用的網際網路連線。
- 更新後設置您的國家/地區，以應用國家/地區法規設定。
- 設定您的 WiFi 密碼。
- 設定路由器密碼。
- 產品的核心功能需要以下 RouterOS "npk" 軟體包：lora、system。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/bb08cf678e80bbc2.webp)

- 10/100 乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X）。可使用直通線或交叉線連線到其他網路裝置。
- 外部 SMA 天線接頭，已連線到 LR 卡。
- 指示裝置電源狀態的 LED。
- 指示無線網路活動的 LED。
- 汽車聯結器。引腳定義：A - 保留供將來使用（橙色），B - 保留供將來使用（藍色），C - 接地（黑色），D – 電源輸入（紅色）。
- 帶整合 LR9 卡的 MiniPCIe 插槽。
- 整合無線模組，工作於 2.4 GHz，802.11b/g/n 協定。
- SIM 插槽。

## 供電 {#powering}

本裝置可透過以下方式供電：

- 乙太網埠接受被動 PoE 9-30 V DC ⎓。
- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心針為正極）接受 9-30 V DC⎓。
- 汽車聯結器 9-30 V DC⎓。最大負載下的功耗可達 7 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 安裝 {#mounting}

裝置可以透過多種方式安裝：立柱、牆面、天花板，也可以放置在包裝內附帶的專用 MikroTik 支架中。包裝內還包含帶有詳細安裝說明的鑽孔模板，幫助您安裝乙太網線並將其固定到天花板或牆面上。鋼製支架用於放在吊頂板另一側，另配有兩顆螺絲和牆錨。用於立柱安裝的紮帶或鋼卡箍。

本裝置的 IP 防護等級為 IP54。在室外安裝時，請確保所有線纜開口朝下。我們建議使用 POE 注入器和 Cat6 遮蔽線纜進行正確接地。使用和安裝本裝置時，請注意最大允許暴露量（MPE）安全距離，輻射體與您的身體之間至少保持 20 cm。

安裝在桅杆或立柱上：

建議使用電工膠帶以增加材料之間的摩擦力。

![](/img/b21639053eb61552.webp)

- 將塑膠紮帶穿過孔洞安裝到鋼製支架上。
- 將支架安裝到裝置上。
- 用螺絲固定。
- 將裝置安裝並調整到立柱或桅杆上。
- 將乙太網線穿過開口並連線到乙太網埠。
- 關閉底部卡扣並用螺絲固定。

建議使用紮帶將乙太網線固定到立柱上。與裝置的距離約為 30 cm。

將裝置安裝在牆面上：

![](/img/42ebcb18fdb0e686.webp)

- 使用隨附的模板標記鑽孔位置。如有需要，也標記乙太網線的位置。相應地進行對齊，這取決於裝置最終如何安裝。
- 如有需要，插入膨脹螺栓，這取決於牆體結構和材質。
- 將隨附的鋼製支架放置在牆面上。
- 用螺絲將其固定到位。
- 將乙太網線穿過開口並連線到乙太網埠。
- 將裝置安裝到鋼製支架上
- 用螺絲將其固定到位。
- 關閉底部卡扣。

避免將裝置安裝在低窪處，否則您將無法安裝並關閉底部卡扣。

安裝到天花板上：

![](/img/35cd19164cabfd89.webp)

包裝內附帶一個專用支架，用於安裝在吊頂上。由於它由兩部分組成，需要分別固定在天花板板的兩側。

-

使用模板標記孔位。

-

將兩個安裝支架放置在標記位置。

-

用螺絲將它們固定在一起。

-

如果安裝在牆面上，請按相同方式繼續組裝。

-

將乙太網線穿過開口並連線到乙太網埠。

-

將裝置安裝到鋼製支架上。

-

用螺絲將其固定到位。

-

關閉底部卡扣。

## 底蓋 {#bottom-lid}

- 底蓋由不脫出螺絲固定到位。

![](/img/0d1777eb306bd477.webp)

- 使用 Torx T20 螺絲刀將其擰鬆，但不要完全取下螺絲。

![](/img/fda7738b33a2c690.webp)

- 朝與裝置相反的方向拉動蓋板以將其取下。

![](/img/d57e2bacdcc55d28.webp)

- 重新組裝。

## 配置 {#configuration}

要設定 LR 的配置，請連線到裝置並透過 Web 瀏覽器登入，或使用移動應用。需遵循兩個簡單步驟：**第一步：**

-

登入後，將預設選中 Quick Set，請切換到螢幕右側的 WebFig。如果透過移動應用進行配置，請點選螢幕右側的齒輪圖示以開啟高階選單。

-

在左側選單中，找到並選擇 "Lora" 部分。

-

在新開啟的視窗中選擇 Servers 標籤頁。

-

點選 + 新增新的伺服器配置。

-

將出現一個新視窗，您需要輸入：Name：（伺服器名稱）Address：（伺服器地址）Up port：（通常為 1700）Down port：（通常為 1700）

-

點選 OK 儲存。**第二步：**

-

在之前的視窗中選擇 Device 標籤頁。

-

雙擊或點按該行進行配置。

-

在下拉選單中選擇之前輸入的網路。

-

點選 Enable 按鈕以啟用閘道器。

-

點選 OK 儲存。

-

配置完成。我們建議在 QuickSet 選單中點選 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以引導裝置進行重新安裝，請參閱相關章節。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描 QR 碼並選擇您偏好的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱已預先填入。
- 點選 Connect 透過無線網路建立到裝置的連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 天線使用 {#antenna-usage}

我們建議使用外部天線，即 "LoRa Antenna kit" —— 可單獨購買。天線套件帶有立柱安裝座和可直接與 LR 卡配合使用的線纜。[https://mikrotik.com/product/lora_antenna_kit](https://mikrotik.com/product/lora_antenna_kit) 位於底部艙門下的 SMA 接頭已連線到 LR 卡，可直接使用。請參閱有關如何取下艙門的章節。

請在裝置關閉時連線和斷開天線！

**內部天線** 2 dBi 可用於到閘道器距離小於 1 km 的部署場景。預設情況下，天線未連線到卡上！要使用內部天線：

- 開啟底部艙門（見 ""）。

![](/img/7202d8bf8949c9a8.webp)

- 使用 PH2 螺絲刀取下螺絲。
- 將上殼與底殼向相反方向滑動以將它們分離。

![](/img/a69174da52b6ff73.webp)

- 找到內部天線線纜，並將其替換為 LR 卡上的 SMA 線纜接頭。

![](/img/a9ac9728a5604913.webp)

- 重新組裝。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置隨後將查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內包含隨裝置提供的以下配件：

- EU/US 開關電源 24 V ⎓，0.8 A，19.2 W，85.3 %，VI，線纜：150 cm Hor CMC。
- WAP 桌面支架。
- WAP 室外機殼支架 AL，白色。
- POE 注入器線纜。
- 線纜（H4130-04PDB000R 3 mm 2x2P Housing）轉（StripJacket 5 cm+WireEnd Strip/Tin 1 cm）24 AWG。
- 軟管卡箍，35-70 mm，W4。
- K-52 緊固套件。
- WAP 鑽孔模板，紙質手冊。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。RouterOS 的 LR 支援僅限於 MikroTik LR 卡，不支援第三方 Lora 卡。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢棄物處置場所。請了解將裝置正確運送到您所在地區指定處置場所的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th><th>包含 FCC ID</th></tr></thead><tbody><tr><td>RBwAPR-2nD&R11e-LoRa9</td><td>TV7WAPR2ND</td><td>TV7LR9</td></tr></tbody></table>

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝環境中的有害干擾提供合理防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在居住區域操作本裝置很可能造成有害干擾，此時使用者需自費糾正干擾。

**FCC 警告：** 任何未經負責合規的一方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或協同工作。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。安裝和操作本裝置時，輻射體與您身體的任何部位之間應保持至少 20 cm 的距離。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th><th>包含 IC</th></tr></thead><tbody><tr><td>RBwAPR-2nD&R11e-LoRa9</td><td>7442A-WAPR2ND</td><td>7442A-LR9</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。其操作須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。其使用獲准須滿足以下兩個條件：(1) 裝置不得產生干擾；(2) 使用者必須接受裝置所受到的任何無線電干擾，即使該干擾可能影響其正常執行。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。安裝和操作本裝置時，輻射體與您身體的任何部位之間應保持至少 20 cm 的距離。本裝置符合 IC 針對非受控環境規定的輻射暴露限值。安裝和操作本裝置時，輻射體與您身體的任何部位之間應保持至少 20 cm 的距離。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊標註在其標籤上的序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2480-2483.5 МГц（20 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 NKРЗІ 2012 年 11 月 1 日第 559 號決議批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記（編號 57/22589）的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RB912R-2nD-LTm 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WLAN / LR {#wlan--lr}

<table><thead><tr><th>**WLAN**</th><th>工作頻率 / 最大輸出功率</th><th>2400-2483.5 MHz / 20 dBm</th></tr></thead><tbody><tr><td>**LR**</td><td>2403-2479 MHz / 20 dBm</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。更多詳細資訊請參閱上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistung Grenzwerte gemäß ETSI-Vorschriften. Weitere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance de transmission maximale conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti di potenza massima di trasmissione in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los valores límite de potencia máxima de transmisión de acuerdo con la normativa ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует предельным значениям максимальной мощности передачи в соответствии с правилами ETSI. Для получения более подробной информации см. Декларацию соответствия выше.
