---
title: "cAP"
slug: /cap
source: https://manual.mikrotik.com/hardware/cap
captured_at: '2026-11-04T05:55:15+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/64fa735a50b61e30.jpg" alt="" width={800} height={776} /></p>

## [cAP](https://mikrotik.com/product/RBcAP2nD) (RBcAP2nD) {#cap-rbcap2nd}

cAP 是一款小型 AP 裝置，帶有一個乙太網埠，支援透過 PoE 供電，並且可選地由 CAPsMAN 管理伺服器進行管理。完整規格和宣傳冊請參見 [cAP 產品頁面](https://mikrotik.com/product/RBcAP2nD)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能給人員帶來危險並損壞系統。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境設定的輻射暴露限值。本 MikroTik 裝置的安裝和執行，與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 設定 {#setup}

- 確保您的網際網路服務提供商（ISP）允許更改硬體並自動分配 IP 地址；
- 將 ISP 網線連線到乙太網埠；
- 將裝置連線到電源；
- 透過無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具，地址為 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法以確保可訪問性；**
- 使用預設 IP 地址 192.168.88.1 在所選工具中開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可確保最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您的國家/地區，以應用國家法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 供電 {#powering}

裝置從乙太網埠接受供電：

- 乙太網埠接受 12-57 V DC **⎓**（802.3af/at 或被動 PoE）。最大負載下的功耗可達 4 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 POE 介面卡的 POE 埠。
- 將來自 WAN 的乙太網線連線到 POE 介面卡的 LAN 埠，請注意資料和電源流向的箭頭。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 安裝 {#mounting}

可以使用裝置背面的隨附安裝支架，將裝置固定到牆壁或天花板上。

<p><Img src="/img/4f5fb86cf27278d8.webp" alt="" width={451} height={365} /></p>

- 使用隨附的三顆螺絲將安裝支架固定到牆壁或天花板上。
- 如有必要，使用 5 mm 鑽頭配合隨附的膨脹螺栓。
- 將所需線纜連線到裝置。
- 如有需要，在薄天花板或牆壁上作業時，可使用第二個安裝支架提供額外支撐，隨附螺絲長度為 20 mm。
- 將第二個支架固定到天花板的另一側，並用螺絲穿過第一個支架固定。
- 將裝置安裝到安裝支架上，順時針旋轉直到裝置固定到位。我們建議為我們的裝置使用 Cat5/6 網線。本裝置的 IP 防護等級為 IPX0。*本裝置的安裝和配置應由具備資質的人員完成。* 警告！本裝置的安裝和執行，裝置與身體之間的最小距離應為 20 cm。在住宅環境中執行本裝置可能造成無線電干擾。

## 配置 {#configuration}

登入後，我們建議在 QuickSet 選單中點選 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置使用所在的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下所有來自 Internet 埠的訪問都被阻止）。出於恢復目的，可以從網路引導裝置，請參見 Reset 按鈕。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個 10/100 乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X）。直通線或交叉線均可用於連線其他網路裝置。
- 一個整合無線 2.4 GHz 802.11b/g/n。

## 復位按鈕 {#reset-button}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議同時驗證這兩個選項，以防其中一個無法使用。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。根據型號不同，這可能由 **USR、USER、System** 或 **ACT** LED，或 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置上電之前按下按鈕，系統將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 模式按鈕 {#mode-button}

模式按鈕的動作可以在 RouterOS 軟體中配置，以執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。模式按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下附件：

- K-46 安裝套件。
- DC ⎓ EU/US 開關電源 24 V，0.2 A，4.8 W，Level VI，線纜：1.5 m。
- 帶遮蔽乙太網線/聯結器的 POE 注入器（RBPOE）。
- cAP_2nD 天花板安裝附件。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/RBcAP2nD](https://mikrotik.com/product/RBcAP2nD)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許商業使用。
- 如果 WLAN 裝置的工作範圍與上述法規不同，則需要向終端使用者裝置應用來自制造商/供應商的定製韌體版本，並防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料表可在製造商官方網站上獲取。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制在 2.400 – 2.4835 GHz，TX 功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制在 5.150 – 5.250 GHz，TX 功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制在 5.250 – 5.350 GHz，TX 功率限制為 20dBm（EIRP）。

請確保裝置具有鎖定軟體包（來自制造商的韌體版本），該軟體包必須應用到終端使用者裝置以防止終端使用者重新配置。產品將標有國家程式碼 "-EG"。本裝置需要升級到最新版本以確保符合當地主管機構的法規！終端使用者有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如在指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID: TV7RBCM2ND 本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的有害干擾防護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。然而，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），建議使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。FCC 警告：未經合規責任方明確批准的任何更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或協同執行。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境設定的 RF 輻射暴露限值。本裝置的安裝和執行，輻射體與您身體任何部位之間的最小距離應為 20 cm。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC:7442A-CM2ND 本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。

本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR。允許在以下兩個條件下操作：(1) 裝置不得產生干擾，且 (2) 裝置使用者必須接受所受到的任何無線電干擾，即使該干擾可能影響其執行。

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境設定的輻射暴露限值。本裝置的安裝和執行，輻射體與您身體任何部位之間的最小距離應為 20 cm。本裝置符合針對非受控環境定義的 IC 輻射暴露限值。本裝置必須安裝和使用，輻射體與您身體任何部位之間的最小距離為 20 cm。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射器功率</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>≤100 mW</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證而有所不同。

有關裝置製造日期的資訊位於其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），隨後的兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

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

工作頻率（最大輸出功率）：2400-2483.5 MHz（20 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用，需按照烏克蘭國家通訊與資訊化監管委員會 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定中 WLAN 最大發射功率限值。更多資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。有關更多資訊，請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。更多資訊請參見上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 最大發射功率限值。更多資訊請參見上方的符合性宣告。
