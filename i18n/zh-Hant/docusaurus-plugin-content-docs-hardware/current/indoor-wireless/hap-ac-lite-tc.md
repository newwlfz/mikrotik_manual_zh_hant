---
title: "hAP ac lite TC"
slug: /hap-ac-lite-tc
source: https://manual.mikrotik.com/hardware/hap-ac-lite-tc
captured_at: '2026-11-04T05:58:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/ae778f17923632db.jpg" alt="" width={800} height={800} /></p>

## [hAP ac lite TC](https://mikrotik.com/product/RB952Ui-5ac2nD-TC) (RB952Ui-5ac2nD-TC) {#hap-ac-lite-tc-rb952ui-5ac2nd-tc}

hAP ac lite TC 是一款簡單的家庭無線接入點。它開箱即已配置好，您只需插入網際網路線纜即可開始使用無線網際網路。我們建議您設定密碼以保護裝置，請按照以下步驟操作。有關完整規格和宣傳冊，請參閱 [hAP ac lite TC 產品頁面](https://mikrotik.com/product/RB952Ui-5ac2nD-TC)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家和地方法律法規處理。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本裝置用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的程式，可能導致人員危險和系統損壞。
- 本產品適合室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和配件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座上拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對不受控環境規定的射頻輻射暴露限值。本 MikroTik 裝置安裝和操作時，與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 設定 {#setup}

確保您的 ISP 允許硬體更改，請按照以下快速步驟設定裝置：

- 確保您的網際網路服務提供商（ISP）允許硬體更改並自動分配 IP 地址；
- 將 ISP 線纜連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 之外的任一埠，或無線網路“MikroTik-...”連線到裝置（請務必檢視標籤上的無線密碼）；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用 [https://mt.lv/winbox](https://mt.lv/winbox) 上的“WinBox”配置工具。**提供多種配置方法以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇“Neighbors”標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為“admin”，沒有密碼（或者，對於某些型號，請檢視標籤上的使用者和無線密碼）；
- 點選“Check for updates”按鈕，並將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在“Downloads”部分找到所需軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的“Files”選單，並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在“QuickSet”選單中設定以下內容：選擇您所在的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用在現場配置路由器，或為您的 MikroTik 家庭接入點應用最基本的初始設定。

- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱將已填寫。
- 點選 Connect 以透過無線網路建立到裝置的連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 高階選單可用於完整配置所有必要設定。

## 供電 {#powering}

裝置可透過電源插孔或第一個乙太網埠（Passive PoE）供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 10-30 V DC。
- 第一個乙太網埠接受被動 Power over Ethernet，接受 12-30 V DC。最大負載下的功耗可達 5 W。Ether5 埠支援 PoE 輸出，可為其他 RouterBOARD 裝置供電。該埠具有自動檢測功能，因此您可以連線筆記型電腦和其他非 PoE 裝置而不會損壞它們。Ether5 上的 PoE 輸出約比輸入電壓低 2 V，並支援最高 0.58A（因此，隨附的 24 V PSU 將為 Ether5 PoE 埠提供 22 V/0.58 A 輸出）。

## 配置 {#configuration}

登入後，我們建議您點選 QuickSet 選單中的“Check for updates”按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將使用的國家/地區，以符合當地法規。RouterOS 除了本文件所述內容外，還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以將裝置啟動以重新安裝，請參閱“按鈕和跳線”。

## 安裝 {#mounting}

本裝置設計用於室內，可放置在平坦表面上，所有所需線纜連線到裝置前部。或者，也可將裝置安裝在牆上，安裝點位於裝置底部，包裝中不包含螺釘。4x25 mm 規格的螺釘非常合適；根據牆體結構，如有需要，可使用 6x30 mm 的膨脹螺栓和 6 mm 鑽頭。安裝在牆上時，請確保線纜走向朝下。我們建議使用 Cat6 遮蔽線纜。警告！本裝置安裝和操作時，裝置與身體之間應保持至少 20 cm 的距離。在住宅環境中操作本裝置可能會造成無線電干擾。

## 擴充套件槽和埠 {#extension-slots-and-ports}

- 五個獨立的 10/100 乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通或交叉線纜連線到其他網路裝置。
- 整合 2.4 GHz 和 5 GHz 802.11 a/b/g/n/ac 無線，雙頻同時工作的射頻模組，配有板載 PIF 天線，最大增益 1.5 dBi。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三個功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。隨後裝置將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/tags/netinstall) 實用程式重新安裝 RouterOS，請將裝置進入 BOOTP 模式。有兩個引導器選項可用：**Regular Booter** 和 **Backup Booter**。建議驗證這兩個選項，以防其中一個無法工作。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置通電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置通電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備好透過 **Netinstall** 重新安裝 RouterOS。根據型號不同，這可能由 **USR、USER、System** 或 **ACT** LED，或 SFP 埠 LED 指示。

無論使用上述哪個選項，如果在裝置通電前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的配件：

- 歐盟開關電源 24 V。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/RB952Ui-5ac2nD](https://mikrotik.com/product/RB952Ui-5ac2nD)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未測試。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置的工作範圍與上述法規不同，則終端使用者裝置需要應用來自制造商/供應商的定製韌體版本，並且還要防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可證。
- 任何裝置的資料表均可在製造商官方網站上獲取。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，發射功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，發射功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母“EG”的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，發射功率限制為 20dBm（EIRP）。

請確保裝置具有鎖定軟體包（來自制造商的韌體版本），該軟體包需要應用到終端使用者裝置，以防止終端使用者重新配置。產品將標有國家/地區程式碼“-EG”。本裝置需要升級到最新版本，以確保符合當地主管部門法規！終端使用者有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC 識別符號：TV7RB952-5AC2ND 本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理保護，防止有害干擾。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：（1）本裝置不得造成有害干擾；（2）本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與其他任何天線或發射器共置或協同操作。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對不受控環境規定的射頻輻射暴露限值。本裝置安裝和操作時，輻射器與身體任何部位之間應保持至少 20 cm 的距離。

**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用經產品認證的天線。根據 FCC 規則 CFR47 part 15.204，明確禁止使用除經產品認證的天線以外的任何天線。安裝人員應根據國家/地區法規和天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康和安全要求。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

IC：7442A-9525AC

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

-

本裝置不得產生干擾；

-

本裝置必須接受任何干擾，包括可能導致裝置執行不正常的干擾。本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：

-

本裝置不得產生干擾；

-

本裝置必須接受所接收到的任何無線電干擾，即使該干擾可能導致裝置執行不正常。此 B 類數字裝置符合加拿大 ICES-003。

此 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)
<p><Img src="/img/0561b3ba8c95a35c.webp" alt="" width={146} height={135} /></p>

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

工作在 5150–5250 MHz 頻段的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。工作在 5150–5250 MHz 頻段的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

**重要：射頻輻射暴露。** 本裝置符合 IC 針對不受控環境規定的射頻輻射暴露限值。本裝置安裝和操作時，輻射器與身體任何部位之間應保持至少 20 cm 的距離。本裝置符合 IC 針對不受控環境規定的暴露限值。本裝置安裝和操作時，輻射器與身體任何部位之間應保持至少 20 cm 的距離。

## UKCA 標誌 {#ukca-marking}

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 MHz、5150-5350 MHz、5650-5850 MHz</td><td>≤10 W</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊位於其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位），後面兩位表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23，Riga，LV-1006，拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

如需瞭解保修服務的詳細資訊，請聯絡銷售商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品已根據相關要求進行評估，並帶有如下所示的 EAC 標誌：

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz（30 dBm）、5725-5850 MHz（30 dBm）。可用頻率通道可能因產品型號和認證而異。

能效符合 NOM-029-ENER-2017。

本裝置的操作須滿足以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非預期操作的干擾。

製造商：MikroTikls SIA，Brivibas gatve 214i，Riga，LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區問題，請聯絡當地經銷商。進口商名單可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊基礎設施監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i，里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 MHz（20 dBm）、5150-5250 MHz（23 dBm）、5250-5350 MHz（20 dBm）、5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求和其他相關規定，也符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA，Brivibas gatve 214i，Riga，拉脫維亞，LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RB952Ui-5ac2nD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相關型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定中的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的最大 WLAN 傳輸功率限值。有關更多資訊，請參閱上文的符合性宣告。

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。
