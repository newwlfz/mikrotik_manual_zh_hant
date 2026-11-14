---
title: "cAP ac"
slug: /cap-ac
source: https://manual.mikrotik.com/hardware/cap-ac
captured_at: '2026-11-04T05:55:20+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/66e65ebbae205af4.jpg" alt="" width={799} height={792} /></p>

## [cAP ac](https://mikrotik.com/product/cap_ac)（RBcAPGi-5acD2nD） {#cap-ac-rbcapgi-5acd2nd}

cAP ac 是一款可吸頂安裝的無線接入點。它已完成配置，您只需插入 ISP 網線即可開始使用無線網際網路。有關完整規格和宣傳冊，請參見 [cAP ac 產品頁面](https://mikrotik.com/product/cap_ac)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應依照所有國家法律和法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於機架安裝。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟可能會對人員造成危險並損壞系統。
- 本產品設計用於室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，它們可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 設定 {#setup}

- 確保您的網際網路服務提供商 (ISP) 允許更換硬體並自動分配 IP 地址；
- 將 ISP 網線連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 以外的任意埠，或透過無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在 Web 瀏覽器中使用 WebFig，或使用 [https://mt.lv/winbox](https://mt.lv/winbox) 上的 "WinBox" 配置工具。**提供多種配置方式以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可以確保最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您所在的國家/地區，以應用該國家/地區的法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 拆卸安裝環 {#removing-mounting-ring}

安裝環出廠時已安裝在裝置上，為了使用乙太網埠，請逆時針旋轉將其拆下，安裝環即可鬆開。

<p><Img src="/img/d33fa6faeea2ff7d.webp" alt="" width={679} height={455} /></p>

## 供電 {#powering}

裝置透過乙太網埠接受供電，因此您必須使用隨附的被動 PoE 注入器，或確保您的交換器支援被動 PoE 或 802.3af/at PoE 輸出。

- 乙太網埠接受 12-57 V DC **⎓**（802.3af/at 或被動 PoE）。最大負載下的功耗可達 13 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網線連線到 POE 介面卡的 POE 埠。
- 將來自您的區域網路的乙太網線連線到 POE 介面卡的 LAN 埠，請注意資料和電源流向的箭頭指示。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 安裝 {#mounting}

可以使用裝置背面的隨附安裝支架將裝置固定到牆壁或天花板上：

- 使用隨附的三顆螺釘將安裝支架固定到牆壁或天花板上；
- 如有必要，使用 5 mm 鑽頭並配合隨附的牆塞；

<p><Img src="/img/4f5fb86cf27278d8.webp" alt="" width={451} height={365} /></p>

- 將所需的線纜連線到裝置；
- 如有需要，在薄天花板或牆壁上施工時，可使用第二個安裝支架作為額外支撐，所用螺釘長度為 20 mm；
- 將第二個安裝座固定在天花板的另一側，並透過第一個安裝座用螺釘固定；
- 將裝置安裝到安裝支架上並順時針旋轉，直到裝置固定到位；*本裝置的安裝和配置應由合格人員完成。* 警告！本裝置的安裝和操作應保持裝置與您的身體之間至少 20 釐米的距離。在住宅環境中操作本裝置可能會造成無線電干擾。

工作溼度可為 5% 至 95%，無凝露。

## 配置 {#configuration}

預設情況下，裝置配置為無線接入點，第一個乙太網埠 (Eth1) 配置為 DHCP 用戶端，第二個介面與無線介面橋接在一起。橋接介面上配置了 DHCP 伺服器。登入後，我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請務必選擇裝置將使用所在的國家/地區，以符合當地法規。RouterOS 除本文件所述內容外還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可使用 WinBox 工具 ([https://mt.lv/winbox](https://mt.lv/winbox)) 從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。為便於恢復，可以從網路引導裝置，請參見 Reset 按鈕。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 兩個 10/100/1000 乙太網埠，支援自動交叉/直通線纜修正 (Auto MDI/X)。直通線或交叉線均可用於連線其他網路裝置。Eth2 埠能夠以被動 PoE 為另一臺 RouterBOARD 裝置供電（最高 57 V）。使用低於 30 V 為本裝置供電時，最大輸出電流為 500mA；使用高於 30 V 時，最大輸出電流為 400mA。
- 整合無線 2.4 GHz 802.11b/g/n，支援 AP/CPE/P2P/repeater 模式。
- 整合無線 5 GHz 802.11a/n/ac。

## Reset 按鈕 {#reset-button}

Reset 按鈕有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住 Reset 按鈕，直到 LED 變為常亮，然後鬆開即可啟用 CAP 模式。隨後裝置將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種引導器選項可用：**Regular Booter** 和 **Backup Booter**。建議兩種選項都驗證一下，以防其中一種無法工作。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置通電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置通電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。取決於型號，這可能透過 **USR、USER、System** 或 **ACT** LED，或透過 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## Mode 按鈕 {#mode-button}

本裝置上有兩個 mode 按鈕，但它們執行相同的操作。可以透過 RouterOS 軟體配置 mode 按鈕的動作，以執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。預設情況下，這些按鈕會啟用"深色模式"，即關閉蜂鳴聲和 LED 燈。Mode 按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## LED 指示燈 {#led-indicators}

本裝置上有七個 LED 燈，如有必要可以全部停用。

- User – 可由使用者配置的 LED，用於執行任意所需指令碼。
- 5G – 5GHz 介面活動。
- 2G – 2.4 GHz 介面活動。
- E2 – Ethernet 2 已連線。
- E1 – Ethernet 1 已連線。
- PoE LED 表示 ETH2 埠當前正透過 PoE 為另一臺裝置供電。
- 電源 LED 表示裝置正透過 ETH1 埠接收供電。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- K-46 安裝套件。
- DC ⎓ EU/US 開關電源 24 V, 1.2 A, 28.8 W, Level VI，線纜：1.5 m。
- 帶遮蔽乙太網線/聯結器的 POE 注入器 (RBPOE)。
- cAP 吸頂安裝附件。
- 外殼蓋。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/cap_ac](https://mikrotik.com/product/cap_ac)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將已預先填入。
- 點選 Connect，透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要設定。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置的工作範圍與上述法規不同，則必須對終端使用者裝置應用來自制造商/供應商的定製韌體版本，並防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料表均可在製造商官方網站上獲取。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，TX 功率限制為 20dBm (EIRP)。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，TX 功率限制為 23dBm (EIRP)。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，TX 功率限制為 20dBm (EIRP)。

請確保裝置具有鎖定軟體包（來自制造商的韌體版本），該軟體包必須應用於終端使用者裝置，以防止終端使用者重新配置。產品將標有國家程式碼 "-EG"。本裝置需要升級到最新版本，以確保符合當地主管部門的法規！終端使用者有責任遵守當地國家法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢棄物處置場所。請熟悉您所在地區將裝置正確運送至指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID: TV7CPGI5ACD2ND 本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝提供合理的保護，防止有害干擾。

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則建議使用者嘗試透過以下措施之一來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以獲得幫助。FCC 警告：未經負責合規的一方明確批准的任何更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期操作的干擾。本裝置及其天線不得與任何其他天線或發射器放在一起或協同工作。**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和操作應保持輻射體與您身體任何部位之間至少 20 cm 的距離。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC:7442A-CPGI5ACD2ND 本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 標準的免許可發射器/接收器。操作須滿足以下兩個條件：

-

本裝置不得造成干擾；

-

本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。本裝置中包含的免許可發射器/接收器符合加拿大創新、科學與經濟發展部針對免許可無線電裝置的適用 CNR 標準。允許在以下兩個條件下操作：

-

本裝置不得產生干擾；

-

裝置必須接受所收到的任何無線電干擾，即使該干擾可能影響正常使用。**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和操作應保持輻射體與您身體任何部位之間至少 20 cm 的距離。本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和操作應保持輻射體與您身體任何部位之間至少 20 cm 的距離。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B) 在 5150–5250 MHz 頻段內工作的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。在 5150 至 5250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而有所不同。

裝置生產日期資訊以斜槓分隔的形式標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），接下來的兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 (Norma Oficial Mexicana) {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2412-2472 MHz (20 dBm)、5150-5250 MHz (23 dBm)、5250-5350 MHz (20 dBm)、5470-5725 MHz (27 dBm)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需要按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部註冊，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBcAPGi-5acD2nD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：

[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用型號）**</th><th>**使用的通道**</th><th>**最大輸出功率 (EIRP)**</th><th>**限制**</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告。

<p><Img src="/img/0561b3ba8c95a35c.webp" alt="" width={146} height={135} /></p>

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限室內使用。
