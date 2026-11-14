---
title: "wAP ac kit 系列"
slug: /wap-ac-kit-series
source: https://manual.mikrotik.com/hardware/wap-ac-kit-series
captured_at: '2026-11-04T10:06:45+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **wAP ac LTE kit**
- **wAP ac 4G kit**
- **wAP ac LTE6 kit**
:::

本裝置需要升級到 RouterOS v6.46 或最新版本，以確保符合當地主管部門的規定。

客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

![](/img/6ee4c755ff10151e.webp)

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 在任意牆面安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本產品設計用於室外立杆安裝，但也可以室內安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的程式，可能會給人員帶來危險並損壞系統。
- 僅使用製造商認可的電源和附件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用本裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或普通公眾的距離不得小於 45 釐米。

## 快速開始 {#quickstart}

- 使用十字螺絲刀擰鬆固定底蓋的螺絲（參見 ）。
- 將 micro SIM 卡插入卡槽；
- 選擇合適的供電方式，有關可能性請參閱相關章節。
- 在您的 PC 上開啟網路連線，搜尋以 "MikroTik" 開頭的 SSID。
- 在計算機上進入網路連線部分，找到名為 "*MikroTik-...*" 的無線網路。繼續連線它（請檢視貼紙上的無線密碼）；
- 配置應透過無線網路使用移動應用程式完成，或者您也可以使用 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 下載並開啟 **WinBox**，選擇 **Neighbors** 標籤頁以查詢裝置；
- 選擇 MAC 地址。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 查詢您的產品。所需的軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 **WinBox** 的 **Files** 選單，然後重啟裝置。透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 **QuickSet** 選單中設定以下內容：選擇您的國家，以應用國家法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟該應用程式。
- 預設情況下，IP 地址和使用者名稱已預先填入。
- 選擇 Connect 以透過無線網路與您的裝置建立連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 還提供高階選單，可完整配置所有必要設定。

## 供電 {#powering}

本裝置可透過電源插孔或乙太網埠供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）支援 12-57 V ⎓ DC；
- 乙太網埠支援 802.3af/at PoE 18-57 V ⎓ DC。最大負載下的功耗可達 16 W。將接地線連線到固定底蓋的螺絲上。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將乙太網線從裝置連線到 PoE 介面卡的 PoE+DATA 埠；
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 安裝 {#mounting}

本裝置可透過多種方式安裝：立杆、牆壁、天花板，或者可以放置在包裝內附帶的設計專用 MikroTik 支架中。包裝中還包含帶有詳細安裝說明的鑽孔模板，幫助您完成乙太網線安裝以及固定到天花板或牆壁上。用於放置在天花板吊頂板另一側的鋼製支架，以及兩顆螺絲和牆塞。用於立杆安裝的紮帶或鋼製卡箍。本裝置的 IP 等級為 IP54。在室外安裝時，請確保所有線纜開口朝下。您應使用 POE 注入器和帶有 Cat6 遮蔽線纜的適當接地。使用和安裝本裝置時，請注意最大允許暴露量（MPE）安全距離，輻射體與身體之間至少保持 35 cm。**安裝在桅杆或立杆上：**

![](/img/b21639053eb61552.webp)

** 建議使用電工膠帶以增加材料之間的摩擦力。*

- 將塑膠紮帶穿過孔洞固定到鋼製支架上。
- 將支架安裝到裝置上。
- 用螺絲將其固定。
- 將裝置安裝並對準到立杆或桅杆上。
- 將乙太網線穿過開口並連線到乙太網埠。
- 合上底部卡扣並用螺絲固定。建議使用紮帶將乙太網線固定到立杆上，與裝置的距離約為 30 cm。

![](/img/42ebcb18fdb0e686.webp)

**將裝置安裝到牆壁上：**

- 使用隨附的模板標記鑽孔位置。如需要，也可標記乙太網線的位置。請相應地對齊，這取決於裝置最終將如何安裝。
- 如有需要，插入膨脹螺栓，這取決於牆體結構和材質。
- 將隨附的鋼製支架放置在牆上。
- 用螺絲將其固定到位。
- 將您的乙太網線穿過開口並連線到乙太網埠。
- 將裝置安裝到鋼製支架上
- 用螺絲將其固定到位。
- 合上底部卡扣。

避免將裝置安裝在低窪位置，否則您將無法安裝併合上底部卡扣。**安裝到天花板上：**

![](/img/35cd19164cabfd89.webp)

包裝中附帶一個專用支架，用於安裝在吊頂上。由於它由兩部分組成，需要固定在天花板吊頂板的兩側。

-

使用模板標記孔洞位置。

-

將兩個安裝支架放置到位。

-

用螺絲將它們固定在一起。如果安裝到牆壁上，請以相同方式繼續組裝。

-

將您的乙太網線穿過開口並連線到乙太網埠。

-

將裝置安裝到鋼製支架上。

-

用螺絲將其固定到位。

-

合上底部卡扣。

## 底蓋 {#bottom-lid}

- 底蓋透過防脫螺絲固定到位。
- 使用 Philips PH2 螺絲刀將其擰鬆，但不要完全卸下螺絲。

![](/img/b67c9df3c35b1165.webp)

- 將蓋板朝背離裝置的方向拉動以將其拆下。

![](/img/0430222d528f3356.webp)

- 重新組裝。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 整合兩個無線模組，分別工作在 2.4 GHz 和 5 GHz，支援 AP/CPE/P2P/中繼模式。
- 兩個千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。直通線或交叉線均可用於連線到其他網路裝置。
- miniPCIe 插槽和 SIM 插槽（不能單獨使用），用於配合調變解調器使用。

## MiniPCIe 插槽使用 {#minipcie-slot-usage}

本裝置配備 miniPCIe 插槽，出廠已預裝 LTE6、LTE 或 4G 卡。還提供 SIM 插槽，用於配合 miniPCIe 調變解調器使用。SIM 插槽不能單獨使用。此外，您可以安裝自己選擇的外接天線，這應由具備資質的人員完成，操作電氣裝置時請遵循安全預防措施，拆封和處理電氣部件時請佩戴腕部接地帶，以避免靜電放電（ESD）損壞。安裝外接天線：

-

使用 Philips PH2 螺絲刀卸下螺絲，並向下滑動底蓋將其拆下；

-

卸下電源插孔下方的兩顆螺絲，並滑出 wAP PCB 板；

![](/img/84e975dda87c27e6.webp)

-

從調變解調器的 MAIN 天線介面上斷開灰色 uFL 接頭，從另一個（或 AUX）介面上斷開黑色線纜；

-

使用一字螺絲刀或類似工具拆下兩個塑膠蓋，將天線線纜穿過孔洞並連線到已安裝的 LTE6 卡上；

-

之後將 wAP 板重新插回外殼，並用之前卸下的螺絲固定；

-

將移動運營商的 SIM 卡插入 SIM 插槽，晶片朝上。

-

SIM 插槽透過塑膠卡扣防止 SIM 卡掉出。您可以將卡扣按向左側以解鎖，然後插入或更換 SIM 卡，可使用鑷子或類似工具。使用外接天線時，將接頭安裝到外殼上：

-

開孔並使用 6.5 mm 鑽頭，在四個預設位置中的任意一個鑽孔；

![](/img/87aafcea8aa9d40e.webp)

-

引導您的 ACSMAUFL 接頭並將其固定到位，有關如何放置橡膠密封圈以獲得最佳防水保護的參考，請見下圖：

![](/img/03bc306812c7acce.webp)

## SIM 插槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議配合轉接卡使用。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置隨後將查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備用的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復非常有用。

## 配置 {#configuration}

您應點選 "Check for updates" 按鈕，並將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議您訪問 RouterOS 文件頁面，熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下，來自網際網路埠的所有訪問均被阻止）。可以從網路引導裝置，以便為恢復目的重新安裝 RouterOS。這可以透過第一個乙太網埠完成。具體方法請見上文。

## 配件 {#accessories}

包裝中包括以下隨裝置附帶的附件：

![](/img/3ce6215e631f2406.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS 6 和 7 版本。具體的出廠預裝版本號顯示在 RouterOS 的 `/system resource` 選單中。其他作業系統未經測試。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置工作的頻段與上述規定不同，則需要對終端使用者裝置應用來自制造商/供應商的定製韌體版本，並且還要防止終端使用者重新配置。
- 室外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料手冊均可在製造商官方網站上獲取。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，發射功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，發射功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，發射功率限制為 20dBm（EIRP）。

確保裝置具有鎖定軟體包（來自制造商的韌體版本），需要將其應用到終端使用者裝置上，以防止終端使用者重新配置。產品將標有國家程式碼 "-EG"。本裝置需要升級到最新版本，以確保符合當地主管部門的規定！終端使用者有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>**型號**</th><th>**FCC ID**</th><th>**包含 FCC ID**</th></tr></thead><tbody><tr><td>wAP ac LTE6 kit</td><td>TV7WAPGR5AC2D</td><td>TV7R11ELTE6</td></tr><tr><td>wAP ac LTE kit</td><td>TV7WAPGR5AC2D</td><td>TV7R11ELTE</td></tr><tr><td>wAP ac 4G kit</td><td>TV7WAPGR5AC2D</td><td>TV7R11E4G</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝提供合理的保護，防止有害干擾。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），建議使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。**FCC 警告：** 未經合規負責方明確批准的任何更改或修改，都可能導致使用者無權操作本裝置。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共址或協同執行。**重要：** 射頻輻射暴露。本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和執行位置與您身體任何部位之間的距離應至少為 45 cm。

*使用 CBRS 頻段時，最終主裝置的 CBSD 類別將取決於所使用的功率設定和天線增益。*

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>**型號**</th><th>**IC**</th><th>**包含 IC**</th></tr></thead><tbody><tr><td>wAP ac LTE6 kit</td><td>7442A-WAPGR5AC2D</td><td>7442A-R11ELTE6</td></tr><tr><td>wAP ac LTE kit</td><td>7442A-WAPGR5AC2D</td><td>7442A-R11ELTE</td></tr><tr><td>wAP ac 4G kit</td><td>TV7WAPGR5AC2D</td><td>TV7R11E4G</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 標準的免許可發射器/接收器。操作須符合以下兩個條件：

-

本裝置不得造成干擾；

-

本裝置必須接受任何干擾，包括可能導致裝置執行異常的干擾。L'émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d'Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes:

-

本裝置不得產生干擾；

-

L'appareil doit accepter tout brouillage radioélectrique subi, mźme si le brouillage est. 本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和執行位置與您身體任何部位之間的距離應至少為 45 cm。Cet equipement est conforme aux limites d'exposition au rayonnement IC definies pour un environnement non controle. Cet equipement doit etre installe et utilise a une distance minimale de 45 cm entre le radiateur et toute partie de votre corps.

在 5150–5250 MHz 頻段內執行的裝置僅限室內使用，以減少對同頻道移動衛星系統造成有害干擾的可能性。les dispositifs fonctionnant dans la bande de 5150 ą 5250 MHz sont réservés uniquement pour une utilisation ą l'intérieur afin de réduire les risques de brouillage préjudiciable aux systčmes de satellites mobiles utilisant les mźmes canaux.

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證而異。

有關裝置製造日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 МГц (20 дБм)、5150-5250 МГц (23 дБм)、5250-5350 МГц (20 дБм)、5470-5725 МГц (27 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用須按照 NKРЗІ 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Mikrotīkls SIA 特此宣告，無線電裝置型別 RouterBOARD 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/product/wap_ac_lte_kit](https://mikrotik.com/product/wap_ac_lte_kit)

### WLAN / WCDMA / LTE / 5G {#wlan--wcdma--lte--5g}

<table><thead><tr><th>工作頻率 / 最大輸出功率 Betriebsfrequenz / maximale Ausgangsleistung Fréquence de fonctionnement / puissance de sortie maximale Frequenza operativa / massima potenza di uscita Frecuencia de funcionamiento / potencia de salida máxima Рабочая частота / максимальная выходная мощность</th><th>WLAN</th><th>2400-2483.5 MHz / 20 dBm</th></tr></thead><tbody><tr><td>5150-5250 MHz / 23 dBm</td><td></td><td></td></tr><tr><td>5250-5350 MHz / 20 dBm</td><td></td><td></td></tr><tr><td>5470-5725 MHz / 27 dBm</td><td></td><td></td></tr><tr><td>E-GSM-900（4G kit 除外）</td><td>900 MHz / 33 dBm ± 3 dB</td><td></td></tr><tr><td>DCS-1800（4G kit 除外）</td><td>1800 MHz 30 dBm ± 3 dB</td><td></td></tr><tr><td>WCDMA Band I（4G kit 除外）</td><td>1922.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII（4G kit 除外）</td><td>882.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1（4G kit 除外）</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8（4G kit 除外）</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 31（僅 4G kit）</td><td>450 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38（4G kit 除外）</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40（4G kit 除外）</td><td>2300 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 41（僅 4G kit）</td><td>2500 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 42（僅 4G kit）</td><td>3500 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 43（僅 4G kit）</td><td>3700 MHz / 23dBm ± 2.7 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。更多詳細資訊請參見上方的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- und LTE-Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN et LTE conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN e LTE in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN y LTE de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN и LTE в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.

![](/img/0561b3ba8c95a35c.webp)

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。/ Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.
