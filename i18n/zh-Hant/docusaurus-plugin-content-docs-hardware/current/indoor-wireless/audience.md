---
title: "受眾"
slug: /audience
source: https://manual.mikrotik.com/hardware/audience
captured_at: '2026-11-04T05:55:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/e6d36a61a309ffd5.jpg" alt="" width={416} height={799} /></p>

## [Audience](https://mikrotik.com/product/RBD25G-5HPacQD2HPnD) (RBD25G-5HPacQD2HPnD) {#audience-rbd25g-5hpacqd2hpnd}

Audience - 用於構建可靠網路的家庭接入點。透過向其中新增更多 Audience 裝置，可輕鬆擴充套件無線網路覆蓋範圍。您可以在網路範圍內攜帶無線裝置移動，Audience 裝置將與其繫結相同的 (SSID)。有關完整規格和宣傳冊，請參閱 [Audience 產品頁面](https://mikrotik.com/product/RBD25G-5HPacQD2HPnD)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家和地方法律法規。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本裝置旨在安裝於機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確程式可能會對人員造成危險情況，並損壞系統。
- 本產品適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和附件。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座上拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。
- 這是 A 類裝置。在居住環境中，本產品可能會造成無線電干擾，在這種情況下，使用者可能需要採取適當措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置應距離您的身體、職業使用者或公眾不少於 20 釐米。

## 設定 {#setup}

Audience 預設配置為 Home AP，以便在家庭或辦公室中簡單、可管理地使用。請按照以下步驟設定您的無線網路：

- 確保您的網際網路服務提供商 (ISP) 允許硬體更改並自動分配 IP 地址；
- 將 ISP 線纜連線到 ETH1 埠；
- 將裝置連線到電源；
- 透過任意乙太網埠或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在 Web 瀏覽器中使用 WebFig，或使用位於 https://mt.lv/winbox 的 "WinBox" 配置工具。**提供多種配置方法以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 單擊 "Check for updates" 按鈕，並將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

要將另一臺 Audience 裝置新增到網路，請參閱 WPS Sync 按鈕。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將已輸入。
- 單擊 Connect 建立透過無線網路與裝置的連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可全面配置所有必要設定。

## 供電 {#powering}

裝置可從電源插孔或乙太網埠接受供電：

-

所提供的直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）可接受 12-57 V DC ⎓。

-

乙太網 1 埠可接受 Passive PoE 24-57 V DC ⎓。最大負載下的功耗可達 30 W。**連線到 POE 介面卡。** POE 介面卡不包含在包裝中，如果您考慮使用它，請按照以下步驟操作：

-

將來自 Audience 的乙太網線纜連線到 POE 介面卡的 POE 埠。

-

將乙太網線纜從您的 LAN 連線到 POE 介面卡的 LAN 埠，請注意資料和電源流向箭頭。

-

將電源線連線到介面卡，然後將電源線插入電源插座。

## 安裝 {#mounting}

本裝置設計用於室內，放置在平坦表面上，所有所需線纜連線到裝置背面。IPX 防護等級為 IPX0。我們建議為 Audience 裝置使用 Cat6 遮蔽線纜。*警告！本裝置的安裝和操作應確保裝置與您的身體之間至少保持 20 cm 的距離。在居住環境中操作本裝置可能會造成無線電干擾。*

## 配置 {#configuration}

登入後，我們建議單擊 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將使用的國家/地區，以符合當地法規。RouterOS 除了本文件所述內容外，還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能性：https://mt.lv/help 如果 IP 連線不可用，可以使用 WinBox 工具（https://mt.lv/winbox）從 LAN 側連線到裝置的 MAC 地址（預設情況下，所有來自 Internet 埠的訪問都會被阻止）。出於恢復目的，可以啟動裝置進行重新安裝，請參閱按鈕和跳線。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 兩個千兆乙太網埠。
- 整合無線 2.4 GHz 802.11b/g/n，天線增益 3.5 dBi。
- 整合無線 5.0 GHz 802.11a/n/ac，天線增益 4.5 dBi。5180 – 5320 MHz。
- 整合無線 5.0 GHz 802.11a/n/ac，天線增益 4.5 dBi。5500 – 5825 MHz。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。隨後裝置將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請使裝置進入 BOOTP 模式。有兩個 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議驗證兩個選項，以防其中一個無法工作。

- **Regular Booter：** 要進入 etherboot 模式，請在給裝置通電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置通電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。取決於型號，這可能由 **USR, USER, System**，或由 **ACT** LED 指示，也可能由 SFP 埠 LED 指示。

無論使用上述哪個選項，如果在裝置通電前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

### WPS Sync 按鈕 {#wps-sync-button}

使用 WPS Sync 按鈕，透過向其中新增多臺 Audience 裝置來擴充套件無線中繼網路覆蓋範圍。

- 在選定的 Audience AP 上，按一次 "WPS-Sync" 按鈕，以開啟 WPS 模式兩分鐘，並使其等待 Audience 中繼器。狀態 LED 將閃爍綠色。
- 需要按住 "WPS-Sync" 按鈕啟動 Audience 中繼器，以便裝置根據 "WPS-Sync" 模式自行配置並連線到 Audience AP。當狀態 LED 閃爍琥珀色時，鬆開 "WPS-Sync" 按鈕。
- 如果 Audience 中繼器無法連線到 Audience AP，則可以透過 RouterOS 重複連線，或者按下 "WPS-Sync" 按鈕並在 5 秒後鬆開，裝置將開啟 "WPS-Sync" 模式兩分鐘並搜尋 Audience AP。狀態 LED 將閃爍琥珀色。
- 要將第三臺 Audience 中繼器新增到網路，請在網路中的第二臺 Audience 上按下 "WPS-Sync" 按鈕，然後在按住 "WPS-Sync" 按鈕的情況下啟動第三臺裝置。根據需要重複此操作，以向您的網路中新增更多裝置。

## 正面狀態 LED 行為 {#front-status-led-behavior}

- 常亮藍色 – 裝置已通電。
- 閃爍綠色 – 裝置處於 Access Point 模式，並等待另一臺 Audience 裝置連線。
- 閃爍琥珀色（紅色 + 綠色）– 裝置搜尋並嘗試連線到另一臺 Audience 裝置。
- 常亮綠色 – 裝置已在 Audience 網路中建立連線。
- 閃爍紅色 – 裝置執行 DFS 雷達檢測。

## 配件 {#accessories}

<p><Img src="/img/39548a32b05e93fa.webp" alt="" width={448} height={237} /></p>

## 規格 {#specifications}

有關本產品、規格和圖片的更多資訊，請訪問我們的網頁：https://mikrotik.com/product/audience

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 注意事項 {#notice}

- 頻段 5.470-5.725 GHz 不允許用於商業用途。
- 如果 WLAN 裝置的工作範圍與上述法規不同，則需要將來自制造商/供應商的定製韌體版本應用到終端使用者裝置，並且還要防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可證。
- 任何裝置的資料表可在製造商官方網站上獲取。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，TX 功率限制為 20dBm (EIRP)。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，TX 功率限制為 23dBm (EIRP)。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，TX 功率限制為 20dBm (EIRP)。

請確保裝置具有鎖定包（來自制造商的韌體版本），需要將其應用到終端使用者裝置，以防止終端使用者重新配置。產品將標有國家/地區程式碼 “-EG”。本裝置需要升級到最新版本，以確保符合當地主管機構法規！終端使用者有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及 DFS 要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如在指定的廢物處置場所處置。請了解您所在地區將裝置正確運輸到指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBD25G-5HPacQD2HPnD-US</td><td>TV7D25-5HPQ2HP</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝中的有害干擾提供合理保護。

本裝置會產生、使用並可能輻射無線電頻率能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者操作本裝置的許可權失效。

本裝置符合 FCC 規則第 15 部分。操作需滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。

注意：本裝置在周邊裝置上使用遮蔽線纜進行了測試。必須在本裝置上使用遮蔽線纜以確保合規。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBD25G-5HPacQD2HPnD-US</td><td>7442A-D255HPQ2HP</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。操作需滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置內含的免許可證發射器/接收器符合加拿大創新、科學與經濟發展部（ISED）針對免許可證無線電裝置適用的 CNR 標準。允許在以下兩個條件下執行：1）裝置不得產生干擾；2）裝置必須接受任何接收到的無線電干擾，即使該干擾可能導致裝置執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

在 5150–5250 MHz 頻段執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊位於其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示周編號。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 МГц (20 дБм), 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需要按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定（該決定已於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號）批准的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBD25GR-5HPacQD2HPnD 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網際網路地址獲取：https://mikrotik.com/products

### WLAN / WCDMA / LTE / 5G {#wlan--wcdma--lte--5g}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>WLAN</th><th>2400-2483.5 MHz / 20 dBm</th></tr></thead><tbody><tr><td>5150-5250 MHz / 23 dBm</td><td></td><td></td></tr><tr><td>5250-5350 MHz / 20 dBm</td><td></td><td></td></tr><tr><td>5470-5725 MHz / 27 dBm</td><td></td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更詳細資訊，請參閱上文的符合性宣告。

<p><Img src="/img/0561b3ba8c95a35c.webp" alt="" width={146} height={135} /></p>

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。
