---
title: "wAP ac"
slug: /wap-ac
source: https://manual.mikrotik.com/hardware/wap-ac
captured_at: '2026-11-04T06:05:16+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/0f0957b07a6b9a42.webp" alt="" width={363} height={800} /></p>

<p><Img src="/img/12efca6087d36bfe.webp" alt="" width={144} height={160} /></p>

## [wAP ac](https://mikrotik.com/product/wap_ac) (RBwAPG-5HacD2HnD) {#wap-ac-rbwapg-5hacd2hnd}

wAP ac 是一款小型雙頻戶外防水無線接入點，可安裝在立杆、牆壁或天花板上。新版本配備 2 個千兆乙太網埠、更強的無線天線效能、更大的記憶體以及強勁的四核 CPU。完整規格與產品手冊請參見 [wAP ac 產品頁面](https://mikrotik.com/product/wap_ac)。

:::info 本文涵蓋

- **wAP ac** (RBwAPG-5HacD2HnD)
- **wAP ac BE** (RBwAPG-5HacD2HnD-BE)
:::

## 安全警告 {#safety-warnings}

- 本裝置設計用於安裝在立杆、牆壁或桅杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 遵循當地國家法規是客戶的責任，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝與執行位置與您的身體、職業使用者或普通公眾的距離不得小於 20 釐米。

## 設定 {#setup}

- 確保您的網際網路服務提供商（ISP）允許更換硬體並自動分配 IP 地址；
- 開啟底部蓋板；
- 將裝置連線到電源；
- 透過除 Ethernet1 以外的任意埠或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者使用網頁瀏覽器中的 WebFig，或使用位於 [https://mt.lv/winbox](https://mt.lv/winbox) 的 "WinBox" 配置工具。**提供多種配置方式以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新至最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，並重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中進行以下設定：選擇您的國家，以應用該國的法規設定；
- 根據使用型別，將 *Installation* 設定為室內或室外；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 安裝 {#mounting}

本裝置有多種安裝方式：牆面、天花板、立杆，也可以放置在包裝內附帶的 MikroTik 專用支架中。包裝內包含帶有說明的鑽孔模板，可幫助您完成乙太網線纜的安裝並將其固定到天花板或牆壁上。包裝內還包含一個用於安裝在天花板吊頂板另一側的鋼製支架、兩顆螺絲和牆錨。可使用紮帶或鋼卡箍將裝置固定到立杆上。為防止底部蓋板被開啟，可使用不同的螺絲。包裝內附帶一顆 Torx T20 安全螺絲供選用。配合附帶的 L 形扳手將其擰入底部蓋板。更換螺絲的詳細說明見包裝。

使用和安裝本裝置時，請注意最大允許暴露（MPE）安全距離，輻射體與您身體之間的距離至少為 31 釐米。

**安裝在桅杆或立杆上：**

<p><Img src="/img/b21639053eb61552.webp" alt="" width={455} height={595} /></p>

** 建議使用電工膠帶以增加材料之間的摩擦力。*

- 將塑膠紮帶穿過孔洞安裝到鋼製支架上。
- 將支架安裝到裝置上。
- 用螺絲將其固定。
- 將裝置安裝到立杆或桅杆上並對齊。
- 將乙太網線纜穿過開口並連線到乙太網埠。
- 關閉底部卡扣並用螺絲固定。建議使用紮帶將乙太網線纜固定到立杆上，與裝置的距離約為 30 釐米。

<p><Img src="/img/42ebcb18fdb0e686.webp" alt="" width={462} height={650} /></p>

**將裝置安裝在牆上：**

- 使用附帶的模板標記鑽孔位置，如有需要也標記乙太網線纜的位置。請相應地對齊，這取決於裝置最終將如何安裝。
- 如有需要，插入膨脹管，具體取決於牆體結構和材質。
- 將附帶的鋼製支架放置在牆上。
- 用螺絲將其固定到位。
- 將乙太網線纜穿過開口並連線到乙太網埠。
- 將裝置安裝到鋼製支架上
- 用螺絲將其固定到位。
- 關閉底部卡扣。

避免將裝置安裝在低窪地面上，否則您將無法安裝並關閉底部卡扣。**安裝在天花板上：**

<p><Img src="/img/35cd19164cabfd89.webp" alt="" width={459} height={532} /></p>

包裝內附帶一個專用支架，用於安裝在天花板吊頂上。它由兩部分組成，分別固定在天花板吊頂板的兩側。

-

使用模板標記鑽孔位置。

-

將兩個安裝支架放置在標記位置。

-

用螺絲將它們固定在一起。如果安裝在牆上，請以相同方式繼續組裝。

-

將乙太網線纜穿過開口並連線到乙太網埠。

-

將裝置安裝到鋼製支架上。

-

用螺絲將其固定到位。

-

關閉底部卡扣。

## 底部蓋板 {#bottom-lid}

- 底部蓋板由防脫螺絲固定到位。
- 使用 Philips PH2 螺絲刀將其擰鬆，但不要完全擰下螺絲。

<p><Img src="/img/b67c9df3c35b1165.webp" alt="" width={194} height={118} /></p>

- 朝遠離裝置的方向拉動蓋板即可將其取下。

<p><Img src="/img/23a475b4789e443e.webp" alt="" width={314} height={145} /></p>

- 重新組裝。

## 供電 {#powering}

裝置可從電源插孔或乙太網埠獲得供電，兩者均在包裝中提供：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 10-57 V ⎓ DC；
- 乙太網埠接受 802.3af/at PoE 18-57 V ⎓ DC。最大負載下的功耗可達 10 W。請將接地（地線）線連線到下部蓋板下方的螺絲上。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線纜連線到 PoE 介面卡的 PoE+DATA 埠；
- 將來自本地網路（LAN）的乙太網線纜連線到 PoE 介面卡；
- 將電源線連線到介面卡，然後將電源線插入電源插座。接地螺絲位於下部蓋板下方：

<p><Img src="/img/e459e23d5228cdb3.webp" alt="" width={174} height={213} /></p>

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<p><Img src="/img/315d6f9c6929731a.webp" alt="" width={613} height={462} /></p>

- 整合兩個無線模組，分別工作在 2.4 GHz 和 5 GHz，支援 AP/CPE/P2P/repeater 模式。
- 兩個 10/100/1000 乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X）。可使用直通線或交叉線連線到其他網路裝置。

## 配置 {#configuration}

我們建議點選 "Check for updates" 按鈕，並將您的 RouterOS 軟體更新到最新版本，以確保獲得最佳效能和穩定性。

- 網際網路連線配置 [https://mt.lv/configuration](https://mt.lv/configuration)；
- RouterOS 軟體的升級選項 [https://mt.lv/upgrade](https://mt.lv/upgrade)；除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議您訪問 RouterOS 文件頁面以熟悉這些功能：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問均被阻止）。可以從網路引導裝置，以便在恢復場景下重新安裝 RouterOS。這可以透過第一個乙太網埠完成，請參見按鈕與跳線。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 工具重新安裝 RouterOS，請將裝置進入 BOOTP 模式。有兩種載入程式選項可用：**Regular Booter** 和 **Backup Booter**。建議在其中一個無法工作時驗證另一個選項。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將引導進入 **BOOTP** 模式，準備好透過 **Netinstall** 重新安裝 RouterOS。根據型號不同，這可能由 **USR、USER、System** 或 **ACT** LED，或 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置上電之前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這適用於 RouterBOOT 偵錯和恢復。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統未經測試。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置的工作範圍與上述規定不同，則需要由製造商/供應商提供定製韌體版本並應用到終端使用者裝置，同時防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料手冊均可在製造商官方網站上獲取。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，發射功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，發射功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，發射功率限制為 20dBm（EIRP）。

請確保裝置帶有 lock 軟體包（來自制造商的韌體版本），該軟體包需要應用到終端使用者裝置，以防止終端使用者重新配置。產品將標註國家程式碼 "-EG"。本裝置需要升級到最新版本，以確保符合當地主管機構法規！遵循當地國家法規是終端使用者的責任，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。

## 配件 {#accessories}

<p><Img src="/img/6cfe871694361319.webp" alt="" width={713} height={154} /></p>

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢棄物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBwAPG-5HacD2HnD-US</td><td>TV7WAPGR5AC2D</td></tr><tr><td>RBwAPG-5HacD2HnD-BE-US</td><td>TV7WAPGR5AC2D</td></tr></tbody></table>

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝環境中的有害干擾提供合理保護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝環境中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來判斷），建議使用者嘗試透過以下一種或多種措施來消除干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。FCC 警告：任何未經負責合規一方明確批准的更改或修改，可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受收到的任何干擾，包括可能導致意外執行的干擾。

注意：本裝置在測試時對外圍裝置使用了遮蔽線纜。為確保合規，必須使用遮蔽線纜與本品配合。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境所規定的射頻輻射暴露限值。本裝置的安裝與執行位置與您身體任何部位之間的距離至少為 20 釐米。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBwAPG-5HacD2HnD-US</td><td>7442A-WAPGR5AC2D</td></tr><tr><td>RBwAPG-5HacD2HnD-BE-US</td><td>7442A-WAPGR5AC2D</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 規定的免許可發射器/接收器。其執行須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

在 5150–5250 MHz 頻段工作的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境所規定的輻射暴露限值。本裝置的安裝與執行位置與您身體任何部位之間的距離至少為 20 釐米。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射機功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證情況而異。

裝置製造日期資訊以斜槓形式標註在其標籤上的序列號末尾。第一位數字表示年份編號（年份的最後一位），其後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準（Norma Oficial Mexicana） {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 МГц (20 дБм), 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，登記號 57/22589）所批准的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相關型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

** 遵循當地國家法規是客戶的責任，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多詳細資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多詳細資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多詳細資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多詳細資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多詳細資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多詳細資訊請參見上方的符合性宣告。

<p><Img src="/img/0561b3ba8c95a35c.webp" alt="" width={146} height={135} /></p>

在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。/ 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。/ 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。/ 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。/ 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。/ 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。
