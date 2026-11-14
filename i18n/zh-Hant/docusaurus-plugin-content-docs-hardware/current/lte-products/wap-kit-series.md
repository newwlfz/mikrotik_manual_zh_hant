---
title: "wAP kit 系列"
slug: /wap-kit-series
source: https://manual.mikrotik.com/hardware/wap-kit-series
captured_at: '2026-11-04T10:06:54+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **[wAP LTE kit](https://mikrotik.com/product/wap_lte_kit_2024)**
- **wAP LTE kit US**
- **wAP 4G kit**
:::

本裝置需要升級至 RouterOS v6.44.6 或最新版本，以確保符合當地主管部門的法規要求。

客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員進行安裝。

![](/img/5e39899dfd23337d.webp)

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣線路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 將接入點安裝在任何牆面上的所有安裝方式均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於室外安裝在立杆上，但也可在室內安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的步驟，可能會對人員造成危險情況並對系統造成損壞。
- 請僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員進行安裝。
- 這是 A 類裝置。在住宅環境中，本產品可能會造成無線電干擾，在這種情況下，使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 38 釐米。

## 快速開始 {#quickstart}

- 使用十字螺絲刀擰鬆固定底部蓋板的螺絲（見 ）。
- 插入 SIM 卡。
- 選擇您的供電方案，可用的方案請參見相關章節。
- 將乙太網電纜連線到 PoE，並將乙太網電纜的另一端連線到本 MikroTik 路由器。將隨附的電源連線到 PoE 供電器。
- 無線 AP 模式預設已啟用，您可以從計算機連線到以 "MikroTik" 開頭的 SSID。可透過 Web 瀏覽器訪問配置介面。地址為 [https://192.168.88.1](https://192.168.88.1)。
- 連線到無線網路，在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 以開始配置。
- 使用者名稱：a*dmin*，預設沒有密碼，您將自動登入到 Quick Set 介面（或者，對於某些型號，請在貼紙上檢視使用者名稱和無線密碼）。
- 選擇右側的 "Check for updates" 按鈕，並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。必須插入有效的 SIM 卡。
- 要個性化您的無線網路，可在 "Network Name" 欄位中更改 SSID；
- 在螢幕左側的 "Country" 欄位中選擇您所在的國家/地區，以應用國家/地區法規設定。
- 在 "WiFi Password" 欄位中設定您的無線網路密碼，密碼長度必須至少為八個字元。
- 在右側底部的 "Password" 欄位中設定您的路由器密碼，並在 "Confirm Password" 欄位中重複輸入，該密碼將在下次登入時使用。
- 選擇 "Apply Configuration" 以儲存更改。
- 如果沒有可用的網際網路連線，可手動更新裝置。
- 從 [https://mikrotik.com/download](https://mikrotik.com/download) 下載最新的 RouterOS 軟體。
- 選擇 MIPSBE 軟體包，並將其儲存到您的 PC。
- 再次連線，並在 **Files** 選單中上傳已下載的軟體包。
- 重啟裝置。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描 QR 碼並選擇您首選的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱將已填寫。
- 選擇 Connect，透過無線網路與您的裝置建立連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 供電 {#powering}

**PoE 輸入**

乙太網埠接受 9-30 V 無源 PoE 供電。包裝盒內包含一個 24 V 介面卡和一個 PoE 供電器。將隨附的 PoE 供電器插入您將在 LAN 中使用的路由器的第一個埠或 internet 埠（或直接插入您的筆記型電腦），並將乙太網電纜連線到 PoE 供電器。將此乙太網電纜的另一端連線到 wAP LTE 裝置。將電源連線到 PoE 供電器

**電源插孔**

DC 插孔（外徑 5.5 mm，內徑 2 mm，母頭，中心正極插頭）支援 9-30 V 供電，裝置隨附一個 24 V 1.2 A 電源介面卡

**汽車聯結器**

汽車聯結器可用於從汽車和公交車中常見的 12/24 V 連線為裝置供電。該插頭有四個引腳：左下（黑色）為接地，右下為電源輸入（紅色）。上面兩個引腳保留供將來使用。24 V 時的最大功耗在無 miniPCIe 時為 6 W，在 miniPCIe 卡滿載時為 8 W。

## 安裝 {#mounting}

本裝置可以透過多種方式安裝：立杆、牆壁、天花板，或者可以放置在包裝內隨附的專門設計的 MikroTik 支架中。包裝內還包含一個鑽孔模板和詳細的安裝說明，以幫助您安裝乙太網電纜並將其固定到天花板或牆壁上。用於放置在吊頂板另一側的鋼製支架以及兩顆螺絲和牆錨。用於安裝在立杆上的紮帶或鋼製卡箍。本裝置的 IP 防護等級為 IP54。在室外安裝時，請確保任何電纜開口朝下。您應使用 POE 供電器和帶有 Cat6 遮蔽電纜的正確接地。使用和安裝本裝置時，請注意最大允許暴露量（MPE）安全距離，輻射體與您身體之間的距離至少為 35 cm。**安裝在立柱或立杆上：**

![](/img/b21639053eb61552.webp)

**建議使用電工膠帶以增加材料之間的摩擦力。*

- 將塑膠紮帶穿過孔洞安裝到鋼製支架上。
- 將支架安裝到裝置上。
- 用螺絲固定。
- 將裝置安裝到立杆或立柱上並對齊。
- 將乙太網電纜穿過開口並連線到乙太網埠。
- 關閉底部鎖釦並用螺絲固定。

建議使用紮帶將乙太網電纜固定到立杆上。與裝置的距離約為 38 cm。

![](/img/42ebcb18fdb0e686.webp)

**將裝置安裝在牆上：**

- 使用隨附的模板標記鑽孔位置。如有需要，也標記乙太網電纜的位置。請相應地對齊，這將取決於裝置最終安裝的方式。
- 如有需要，插入膨脹管，這取決於牆體結構和材料。
- 將隨附的鋼製支架放在牆上。
- 使用螺絲將其固定在相應位置。
- 將您的乙太網電纜從開口處伸出並連線到乙太網埠。
- 將裝置安裝到鋼製支架上
- 用螺絲將其固定到位。
- 關閉底部鎖釦。

避免將裝置安裝在低窪位置，否則您將無法安裝並關閉底部鎖釦。**安裝在天花板上：**

![](/img/35cd19164cabfd89.webp)

包裝內隨附一個專用支架，用於安裝在吊頂上。由於它由兩部分組成，需要固定在天花板板的兩側。

-

使用模板標記孔的位置。

-

將兩個安裝支架放在相應位置。

-

使用螺絲將它們固定在一起。如果安裝在牆上，請以相同方式繼續組裝。

-

將您的乙太網電纜從開口處伸出並連線到乙太網埠。

-

將裝置安裝到鋼製支架上。

-

用螺絲將其固定到位。

-

關閉底部鎖釦。150

## 底部蓋板 {#bottom-lid}

- 底部蓋板通過鬆不脫螺絲固定到位。
- 使用 Philips PH2 螺絲刀將其擰鬆，但不要完全拆下螺絲。

![](/img/b67c9df3c35b1165.webp)

- 朝與裝置相反的方向拉動蓋板以將其取下。

![](/img/0430222d528f3356.webp)

- 重新組裝。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 內建 2 GHz 無線接入點模組，支援 AP/station/bridge/p2p 模式。
- 一個 10/100 乙太網埠，支援自動交叉/直通電纜糾正（Auto MDI/X）。直通或交叉電纜均可用於連線其他網路裝置。乙太網埠接受來自無源 PoE 供電器的 9-30 VDC 供電。
- miniPCIe 插槽和 SIM 插槽（不能單獨使用），用於配合 3G/4G/LTE 調變解調器使用（某些套件已包含）。

## miniPCIe 插槽的使用 {#minipcie-slot-usage}

本裝置配備一個 miniPCIe 插槽（也提供預裝調變解調器的套件），用於配合 3G/4G/LTE 調變解調器使用。提供一個 SIM 插槽，與 miniPCIe 調變解調器配合使用。SIM 插槽不能單獨使用。要安裝 miniPCIe 模組，請拆下電源插孔下方的兩顆螺絲，並將 wAP PCB 板滑出。插入 miniPCIe 調變解調器，並用已就位的兩顆 Philips 螺絲固定。將灰色 uFL 聯結器連線到調變解調器的 MAIN 天線聯結器，將黑色電纜連線到另一個（或 AUX）聯結器。可以為調變解調器使用外接天線，復位按鈕旁邊提供了兩個 SMA 安裝孔；或者如果您希望將天線直接安裝到外殼上，可先拆下兩個塑膠孔蓋，然後將 SMA 天線安裝在外殼底部。在將 wAP 板重新插入外殼並用之前拆下的螺絲固定後，將移動運營商的 SIM 卡晶片朝上滑入 SIM 插槽。該插槽接受 miniSIM（2FF）。SIM 插槽透過塑膠卡扣防止 SIM 卡掉落。您可以按下卡扣，然後使用鑷子或類似工具將 SIM 卡拔出。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配置 {#configuration}

您應選擇 "Check for updates" 按鈕並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議您訪問 RouterOS 文件頁面以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下，來自 internet 埠的所有訪問均被阻止）。可以從網路引導裝置，以便出於恢復目的重新安裝 RouterOS。這可以透過第一個乙太網埠完成。請參閱上文了解如何操作。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。具體的出廠預裝版本列在 /system resource 中。其他作業系統尚未經過測試。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置工作在高於上述法規的頻率範圍，則需要將製造商/供應商提供的定製韌體版本應用於終端使用者裝置，並防止終端使用者重新配置。
- 室外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料表均可在製造商官方網站上獲取。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，發射功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，發射功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，發射功率限制為 20dBm（EIRP）。

請確保裝置具有鎖定包（來自制造商的韌體版本），需要將其應用於終端使用者裝置以防止終端使用者重新配置。產品將標有國家/地區程式碼 "-EG"。本裝置需要升級到最新版本，以確保符合當地主管部門的法規要求！終端使用者有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員進行安裝。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置點處置。請熟悉您所在地區將裝置正確運輸到指定處置點的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝環境中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置可能會造成有害干擾，在這種情況下，使用者將需要自費糾正干擾

FCC 警告：任何未經負責合規的一方明確批准的更改或修改，都可能導致使用者操作本裝置的許可權失效。本裝置符合 FCC 規則第 15 部分。其操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受所接收的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或協同操作。

**重要提示：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和執行位置與輻射體到您身體任何部位的距離至少為 38 cm。

<table><thead><tr><th>**型號**</th><th>**FCC ID**</th><th>**包含 FCC ID**</th></tr></thead><tbody><tr><td>wAP LTE kit</td><td>TV7WAPR2ND</td><td>TV7R11ELTE</td></tr><tr><td>wAP 4G kit</td><td>TV7WAPR2ND</td><td>TV7R11E4G</td></tr></tbody></table>

*使用 CBRS 頻段時，最終主機裝置的 CBSD 類別將取決於所使用的功率設定和天線增益。*

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。其操作須滿足以下兩個條件：

-

本裝置不得造成干擾；

-

本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。L'émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d'Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes:

-

本裝置不得產生干擾；

-

L'appareil doit accepter tout brouillage radioélectrique subi, mźme si le brouillage est. 本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**重要提示：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和執行位置與輻射體到您身體任何部位的距離至少為 38 cm。Cet equipement est conforme aux limites d'exposition au rayonnement IC definies pour un environnement non controle. Cet equipement doit etre installe et utilise a une distance minimale de 38 cm entre le radiateur et toute partie de votre corps.

<table><thead><tr><th>**型號**</th><th>**IC**</th><th>**包含 IC**</th></tr></thead><tbody><tr><td>wAP LTE kit</td><td>7442A-WAPR2ND</td><td>TV7R11ELTE</td></tr><tr><td>wAP 4G kit</td><td>7442A-WAPR2ND</td><td>7442A-R11E4G</td></tr></tbody></table>

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный каналы</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>2400-2483.5 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置生產日期資訊標註在其標籤上的序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後面兩位數字表示週數。

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

工作頻率（最大輸出功率）：2400-2483.5 МГц（20 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需要按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WLAN/ GSM / WCDMA / LTE / {#wlan-gsm--wcdma--lte-}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>WLAN</th><th>2400-2483.5 MHz / / 20 dBm</th></tr></thead><tbody><tr><td>E-GSM-900</td><td>900 MHz / 33 dBm</td><td></td></tr><tr><td>DCS-1800</td><td>1800 MHz / 30 dBm</td><td></td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1（4G kit 除外）</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8（4G kit 除外）</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 31（僅 4G kit）</td><td>450 MHz / 23 dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 42（僅 4G kit）</td><td>3500 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 43（僅 4G kit）</td><td>3700 MHz / 23dBm ± 2.7 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。更多詳細資訊請參閱上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。更多詳細資訊請參閱上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。更多詳細資訊請參閱上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。更多詳細資訊請參閱上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。更多詳細資訊請參閱上方的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。更多詳細資訊請參閱上方的符合性宣告。
