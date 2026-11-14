---
title: "mAP"
slug: /map
source: https://manual.mikrotik.com/hardware/map
captured_at: '2026-11-04T06:01:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/45438bca6a658278.jpg" alt="" width={800} height={800} /></p>

## [mAP](https://mikrotik.com/product/RBmAP2nD)（RBmAP2nD） {#map-rbmap2nd}

mAP 2nD 是一款小型無線 AP 裝置，帶有 2 個乙太網埠，Ether1 支援透過 PoE 受電，Ether2 支援 PoE 輸出，可為另一臺裝置供電。根據軟體配置的不同，它可以作為無線用戶端、接入點或中繼器使用。完整規格和宣傳冊請參閱 [mAP 產品頁面](https://mikrotik.com/product/RBmAP2nD)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置擬安裝於機架中。開始安裝前請仔細閱讀安裝說明。使用不正確的硬體或不遵循正確的操作步驟，可能會對人員造成危險情況並對系統造成損壞。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用本裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所制定的輻射暴露限值。本 MikroTik 裝置的安裝和使用位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 設定 {#setup}

- 確保您的網際網路服務提供商（ISP）允許更換硬體並自動分配 IP 地址；
- 將 ISP 網線連線到 Ether1 埠；
- 將裝置連線到電源；
- 透過 Ether2 埠或無線網路 "MikroTik-..."（請務必檢視貼紙上的無線密碼）連線到裝置；
- 使用移動應用程式建立連線。或者，使用網頁瀏覽器中的 WebFig，或使用 [https://mt.lv/winbox](https://mt.lv/winbox) 上的 "WinBox" 配置工具。**提供多種配置方法以確保可訪問性；**
- 使用預設 IP 地址 192.168.88.1 在所選工具中開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

Ether2 埠支援 PoE 輸出，具備自動檢測功能。這意味著您可以連線筆記型電腦和其他非 PoE 裝置而不會損壞它們。Ether2 上的 PoE 輸出約比輸入電壓低 2 V，最大支援 0.5 A（因此隨附的 24 V 電源將為 Ether2 PoE 埠提供 22 V / 0.5 A 的輸出）。

## 供電 {#powering}

本裝置可從電源插孔或第一個乙太網埠（無源 PoE）接受供電：

- DC 電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 8-57 V DC ⎓。
- 第一個乙太網埠接受無源乙太網供電 11-57 V DC ⎓。
- mAP 也可以透過內建的 micro USB 埠供電，使用 USB 5 V ⎓ 電源。在最大負載下，本裝置的功耗為 4W（不使用 PoE 輸出時）。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱已經填入。
- 點選 Connect，透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 可使用高階選單來完整配置所有必要的設定。

## 啟動過程 {#booting-process}

除本文件中所述內容外，RouterOS 還包含許多配置選項。我們建議您從這裡開始，熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問均被阻止）。出於恢復目的，可以讓裝置進入引導狀態以便重新安裝，請參閱按鈕和跳線部分。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 兩個 10/100 乙太網埠，支援自動交叉/直通線纜連線（Auto MDI/X），因此您可以使用直通線或交叉線連線到其他網路裝置。
- 一個整合無線 2.4GHz 802.11b/g/n 2x2 雙鏈路 MIMO，板載 PIF 天線，最大增益 1.2dBi。
- 一個 micro USB 2.0 埠。

## 安裝 {#mounting}

本裝置設計用於室內使用，可放置在平坦表面上，所有需要的線纜都連線到裝置的前部。我們建議使用 Cat6 遮蔽線纜。警告！本裝置的安裝和操作時，裝置與您身體之間應保持至少 20 cm 的距離。在住宅環境中操作本裝置可能會造成無線電干擾。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 常亮，然後鬆開即可啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種載入程式選項可用：**Regular Booter** 和 **Backup Booter**。建議對兩種選項都進行驗證，以防其中一個無法使用。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將引導進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。取決於型號，這可能由 **USR、USER、System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置上電之前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置的工作範圍與上述規定不同，則須向終端使用者裝置應用來自制造商/供應商的定製韌體版本，並防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料表均可在製造商官方網站上獲取。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，發射功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，發射功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，發射功率限制為 20dBm（EIRP）。

請確保裝置具有鎖定軟體包（來自制造商的韌體版本），該軟體包需要應用於終端使用者裝置，以防止終端使用者重新配置。產品將標有國家程式碼 "-EG"。本裝置需要升級到最新版本，以確保符合當地主管部門的法規！終端使用者有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID：TV7RBMAP2ND

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，證明符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的保護，防止有害干擾。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或經驗豐富的無線電/電視技術人員以獲取幫助。FCC 警告：未經合規負責方明確批准的任何更改或修改，都可能導致使用者無權操作本裝置。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不會造成有害干擾；(2) 本裝置必須接受任何收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射機處於同一位置或聯合執行。

**重要提示：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境所制定的射頻輻射暴露限值。本裝置的安裝和操作時，輻射體與您身體任何部位之間應保持至少 20 cm 的距離。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC: 7442A-MAP2ND 本裝置符合加拿大工業部免許可 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

**重要提示：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境所制定的輻射暴露限值。本裝置的安裝和操作時，輻射體與您身體任何部位之間應保持至少 20 cm 的距離。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>≤100 mW</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證而異。

有關裝置製造日期的資訊，標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## Norma Oficial Mexicana {#norma-oficial-mexicana}

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

在烏克蘭使用需按照 NKРЗІ 2012 年 11 月 1 日第 559 號決議批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記（編號 57/22589）的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBmAP2nD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 規定所設定的 WLAN 最大發射功率限值。更多詳細資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設定的 WLAN 最大發射功率限值。更多資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設定的 WLAN 最大發射功率限值。更多資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設定的 WLAN 最大發射功率限值。更多資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設定的 WLAN 最大發射功率限值。更多資訊請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所設定的 WLAN 最大發射功率限值。更多詳細資訊請參閱上文的符合性宣告。
