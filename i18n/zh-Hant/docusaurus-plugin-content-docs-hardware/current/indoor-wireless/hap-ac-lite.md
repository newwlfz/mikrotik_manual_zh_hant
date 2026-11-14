---
title: "hAP ac lite"
slug: /hap-ac-lite
source: https://manual.mikrotik.com/hardware/hap-ac-lite
captured_at: '2026-11-04T05:58:08+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/757b607ba8569550.jpg" alt="" width={800} height={635} /></p>

## [hAP ac lite](https://mikrotik.com/product/RB952Ui-5ac2nD)（RB952Ui-5ac2nD） {#hap-ac-lite-rb952ui-5ac2nd}

hAP ac lite 是一款簡單的家用無線接入點。它出廠即已完成配置，您只需插上網線即可開始使用無線網路。我們建議您設定密碼以保護裝置安全，請按以下步驟操作。有關完整規格和宣傳手冊，請參閱 [hAP ac lite 產品頁面](https://mikrotik.com/product/RB952Ui-5ac2nD)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家和地方的法律法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置用於機架安裝。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 本產品適用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，它們可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座上拔下。
- 客戶有責任遵守當地國家的法規，包括在合法的頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境制定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不應小於 20 釐米。

## 設定 {#setup}

請確保您的網際網路服務提供商（ISP）允許更換硬體，請按照以下快速步驟設定您的裝置：

- 確保您的網際網路服務提供商（ISP）允許更換硬體並自動分配 IP 地址；
- 將 ISP 網線連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 以外的任意埠，或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具，地址為 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您所在的國家，以應用該國家的法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

- 掃描二維條碼，選擇您首選的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱已自動填入。
- 點選 Connect 透過無線網路建立到裝置的連線。
- 選擇 Quick setup，應用程式將通過幾個簡單的步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 供電 {#powering}

裝置可透過電源插孔或第一個乙太網埠（Passive PoE）接受供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 10-28 V DC。
- 第一個乙太網埠接受被動式 Power over Ethernet，接受 12-28 V DC。最大負載下的功耗可達 5 W。Ether5 埠支援 PoE 輸出，可為其他 RouterBOARD 裝置供電。該埠具有自動檢測功能，因此您可以連線筆記型電腦和其他非 PoE 裝置而不會損壞它們。Ether5 上的 PoE 輸出比輸入電壓低約 2 V，最高支援 0.58A（因此，如果提供 24 V 電源，Ether5 PoE 埠將輸出 22V/0.58 A）。

## 配置 {#configuration}

登入後，我們建議您在 QuickSet 選單中點選 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將要使用的國家，以符合當地法規。除了本文件中描述的內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法進行 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。為便於恢復，可以讓裝置引導以進行重新安裝，請參閱“按鈕和跳線”。

## 安裝 {#mounting}

本裝置設計用於室內，可放置在平坦表面上，所有需要的線纜連線到裝置前方。此外，裝置也可以安裝在牆上，安裝點位於裝置底部，包裝中不包含螺絲。4x25 mm 的螺絲可以很好地適配，根據您的牆體結構，如有需要可以使用 6x30 mm 的膨脹螺栓和 6 mm 鑽頭。安裝在牆上時，請確保線纜進線方向朝下。警告！本裝置的安裝和操作應與您的身體保持至少 20 釐米的距離。在居住環境中操作本裝置可能會造成無線電干擾。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個獨立的 10/100 乙太網埠，支援線纜自動交叉/直通校正（Auto MDI/X），因此您可以使用直通線或交叉線連線其他網路裝置。
- 整合無線 2.4 GHz 和 5 GHz 802.11 a/b/g/n/ac，配備板載 PIF 天線的同步雙頻無線電，最大增益 1.5 dBi。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 常亮，然後鬆手以啟用 CAP 模式。隨後裝置將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請使裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議對兩種選項都進行驗證，以防其中一種無法使用。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，可透過 **Netinstall** 重新安裝 RouterOS。根據型號不同，這可能會透過 **USR、USER、System** 或 **ACT** LED，或 SFP 埠 LED 來指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統將載入備份的 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下配件：

- 歐盟標準 24 V 開關電源。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/RB952Ui-5ac2nD](https://mikrotik.com/product/RB952Ui-5ac2nD)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如在指定的廢物處置場。請熟悉您所在地區將裝置妥善運輸至指定處置場的程式。

## 美國聯邦通訊委員會（FCC）干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID：TV7RB952-5AC2ND

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝環境提供合理的保護，防止有害干擾。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則建議使用者嘗試透過以下措施之一來消除干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以獲得幫助。**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的要求。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期執行的干擾。本裝置及其天線不得與任何其他天線或發射器共置或協同執行。**重要提示：射頻輻射暴露。**

本裝置符合 FCC 針對非受控環境制定的輻射暴露限值。本裝置的安裝和操作應使輻射體與您身體的任何部位之間保持至少 20 釐米的距離。

**天線安裝。警告：** 安裝者有責任確保在美國（或適用 FCC 規則的地區）使用經授權的天線時，僅使用與產品一同認證的天線。根據 FCC 規則 CFR47 第 15.204 部分的規定，嚴禁使用任何未經產品認證的天線。安裝者應根據國家法規和天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

IC：7442A-9525AC

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。其執行須滿足以下兩個條件：

-

本裝置不得造成干擾；

-

本裝置必須接受任何干擾，包括可能導致裝置非預期執行的干擾。本裝置中包含的免許可發射器/接收器符合加拿大創新、科學和經濟發展部適用於免許可無線電裝置的 CNR 標準。其執行獲准須滿足以下兩個條件：

-

本裝置不得產生干擾；

-

本裝置必須接受任何無線電干擾，即使該干擾可能影響其執行。本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要提示：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境制定的輻射暴露限值。本裝置的安裝和操作應使輻射體與您身體的任何部位之間保持至少 20 釐米的距離。本裝置符合 IC 針對非受控環境制定的輻射暴露限值。本裝置的安裝和操作應使輻射體與您身體的任何部位之間保持至少 20 釐米的距離。

工作在 5150–5250 MHz 頻段的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。工作在 5150 至 5250 MHz 頻段的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

有關裝置製造日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），其後兩位數字表示週數。

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

工作頻率（最大輸出功率）：2480-2483.5 МГц (20 дБм)、5150-5250 МГц (23 дБм)、5250-5350 МГц (20 дБм)、5470-5725 МГц (27 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議（2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RB952Ui-5ac2nD 符合 2014/53/EU 指令的要求。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相應型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用無任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家的法規，包括在合法的頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參閱上文的符合性宣告。

<p><Img src="/img/0561b3ba8c95a35c.webp" alt="" width={146} height={135} /></p>

在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。 / 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。 / 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。 / 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。 / 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。 / 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。
