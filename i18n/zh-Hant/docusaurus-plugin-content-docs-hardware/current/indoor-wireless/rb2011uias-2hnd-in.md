---
title: "RB2011UiAS-2HnD-IN"
slug: /rb2011uias-2hnd-in
source: https://manual.mikrotik.com/hardware/rb2011uias-2hnd-in
captured_at: '2026-11-04T06:03:47+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/82343a7161286309.webp" alt="" width={800} height={519} /></p>

## [RB2011UiAS-2HnD-IN](https://mikrotik.com/product/RB2011UiAS-2HnD-IN)（RB2011UiAS-2HnD-IN） {#rb2011uias-2hnd-in-rb2011uias-2hnd-in}

RouterBOARD 2011UiAS-2HnD 具備我們所有無線路由器的大部分功能和介面。它由新的 Atheros 600MHz 74K MIPS 網路處理器驅動，具有 128MB RAM、五個 Gigabit LAN 埠、五個 Fast Ethernet LAN 埠和 SFP 籠（不含 SFP 模組！）。此外，它還配備強大的（最高 1W！）雙鏈 2.4Ghz 802.11bgn 無線、RJ45 序列埠、全尺寸 USB 埠和 RouterOS L5 許可證。有關完整規格和宣傳冊，請參見 [RB2011UiAS-2HnD-IN 產品頁面](https://mikrotik.com/product/RB2011UiAS-2HnD-IN)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本裝置設計用於機架安裝。開始安裝前，請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的程式，可能會對人員造成危險情況並損壞系統。
- 本產品適合室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和附件。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座上拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能造成無線電干擾，在這種情況下，使用者可能需要採取適當措施。

**射頻輻射暴露：** 此 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。此 MikroTik 裝置的安裝和執行應距離您的身體、職業使用者或公眾不少於 20 centimeters。

## 設定 {#setup}

請按照以下快速步驟設定您的裝置：

- 確保您的網際網路服務提供商 (ISP) 允許硬體更改並自動分配 IP 地址；
- 將 ISP 電纜連線到 ETH1 埠；
- 將您的其他本地計算機連線到其他乙太網埠；
- 透過隨附的電源或 PoE 將裝置連線到電源；
- 透過任意乙太網埠或無線網路 “MikroTik-...” 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用位於 [https://mt.lv/winbox](https://mt.lv/winbox) 的 “WinBox” 配置工具。**提供多種配置方法以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 “Neighbors” 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 “admin”，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）；
- 單擊 “Check for updates” 按鈕，並將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 “Downloads” 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 “Files” 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 “QuickSet” 選單中設定以下內容：選擇您所在的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## 供電 {#powering}

該裝置可透過電源插孔或 LAN1 乙太網埠供電：

-

直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 8-30 V DC（過壓保護從 30 V 開始）。

-

Eth1 埠接受來自非標準（無源）Power over Ethernet 注入器的 8-30 V DC 輸入（在板端；長電纜上需更高電壓以補償功率損耗）。該板卡不能與符合 IEEE802.3af 的 48 V 電源注入器配合工作。最大功耗 11 W。**連線到 POE 介面卡：**

-

將裝置上的乙太網線連線到 POE 介面卡的 POE 埠。

-

將來自區域網路的乙太網線連線到 POE 介面卡的 LAN 埠，請注意資料和電源流向箭頭。

-

將電源線連線到介面卡，然後將電源線插入電源插座。

## 電源輸出 {#power-output}

該裝置支援從 Ethernet 10 埠輸出 PoE，您可以為支援透過乙太網供電的 MikroTik 裝置供電。Ether10 上的 PoE 輸出電壓約比輸入電壓低 2 V，並支援最高 0.58 A（因此，所提供的 24 V PSU 將在 Ether10 PoE 埠以 0.58 A 輸出時提供 22 V）。

## 安裝 {#mounting}

該裝置設計用於室內，並可放置在平坦表面上，所有所需電纜均連線到裝置前部。或者，本裝置也可以安裝在牆上，安裝點位於裝置底部，包裝中不含螺絲。4x25 mm 的螺絲可很好地適配，根據牆體結構，如有需要，您可以使用 6x30 mm 的膨脹管和 6 mm 鑽頭。接地螺絲位於裝置外殼背面，請將其相應地連線到有效接地。安裝在牆上時，請確保電纜引入方向朝下。我們建議使用 Cat5/6 遮蔽電纜。*警告！本裝置應在裝置與您的身體之間保持至少 20 cm 的最小距離進行安裝和操作。在住宅環境中操作本裝置可能造成無線電干擾。*

## 配置 {#configuration}

登入後，我們建議單擊 QuickSet 選單中的 “Check for updates” 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法進行 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。為進行恢復，可以將裝置引導以重新安裝，請參見“按鈕和跳線”。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個 10/100/1000 (Gigabit) 乙太網埠（Auto MDI/X）。
- 五個 10/100 (Fast) 乙太網埠（Auto MDI/X）。
- Ether10 支援 500 mA 輸出功率，約比輸入電壓低 2 V。電源輸出支援自動檢測以保護裝置。
- 一個 8-30 V DC 電源插孔。
- 用於 SFP 模組的 SFP 埠（不含模組，僅可與 Gigabit 模組配合使用）。
- 內建無線 AP（2GHz，802.11b/g/n），帶外接天線。
- 一個 USB 2.0 A 型埠。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕位於裝置背面，您需要至少 6mm 長的工具才能正確觸及。復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請使裝置進入 BOOTP 模式。有兩個引導器選項可用：**Regular Booter** 和 **Backup Booter**。建議驗證這兩個選項，以防其中一個無法工作。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 seconds 後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將引導進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。取決於型號，這可能會由 **USR、USER、System** 或 **ACT** LED，或由 SFP 埠 LED 指示。

無論使用上述哪個選項，如果在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內含用於為裝置供電的電源：

- EU/US 開關電源 24 V，DC ⎓，1.2 A，28.8 W，86.8%，VI，線纜：220 cm RA。
- 裝置出廠時已安裝兩根天線。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/RB2011UiAS-2HnD-IN](https://mikrotik.com/product/RB2011UiAS-2HnD-IN)

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

<p><Img src="/img/b0984aa3ad3c6d58.webp" alt="" width={239} height={81} /></p>

<p><Img src="/img/25f50553ffd86eaf.webp" alt="" width={241} height={80} /></p>

<p><Img src="/img/8d294e5cd375c591.webp" alt="" width={247} height={244} /></p>

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

## 注意 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置使用的工作範圍與上述法規不同，則需要由製造商/供應商向終端使用者裝置應用定製韌體版本，並防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可證。
- 任何裝置的資料表可在製造商官方網站上獲取。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，TX 功率限制為 20dBm (EIRP)。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，TX 功率限制為 23dBm (EIRP)。
- 序列號末尾帶有字母 “EG” 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，TX 功率限制為 20dBm (EIRP)。

請確保裝置具有 lock package（來自制造商的韌體版本），該 lock package 必須應用到終端使用者裝置，以防止終端使用者重新配置。產品將標有國家程式碼 “-EG”。為確保符合當地主管部門法規，需要將此裝置升級到最新版本！終端使用者有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置妥善運輸至指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID: TV7RB2011-2HND

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝環境中的有害干擾提供合理防護。

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域操作本裝置很可能造成有害干擾，在這種情況下，使用者將被要求自行承擔費用糾正干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者無權操作本裝置。本裝置符合 FCC 規則第 15 部分。執行需滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期執行的干擾。本裝置及其天線不得與任何其他天線或發射器共址或聯合執行。**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的 RF 輻射暴露限值。本裝置的安裝和執行應使輻射體與您身體的任何部位之間保持至少 20 cm 的最小距離。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

IC: 7442A-RB20112HND

本裝置符合加拿大工業部免許可證 RSS 標準。執行需滿足以下兩個條件：(1) 本裝置不得產生干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期執行的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和執行應使輻射體與您身體的任何部位之間保持至少 20 cm 的最小距離。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊位於其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 МГц (20 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定（該決定於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）所規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RB2011UiAS-2HnD-IN 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用通道**</th><th>**最大輸出功率 (EIRP)**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝！*

此 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參閱上文的符合性宣告 / 此 MikroTik 裝置符合 ETSI 規定所設定的最大 WLAN 發射功率限值。更多資訊請參閱上文的符合性宣告 / 此 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參閱上文的符合性宣告 / 此 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參閱上文的符合性宣告 / 此 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參閱上文的符合性宣告 / 此 MikroTik 裝置符合 ETSI 規則規定的最大 WLAN 發射功率限值。有關更多資訊，請參閱上文的符合性宣告。
