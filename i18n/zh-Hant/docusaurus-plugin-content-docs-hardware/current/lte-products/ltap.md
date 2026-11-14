---
title: "LtAP"
slug: /ltap
source: https://manual.mikrotik.com/hardware/ltap
captured_at: '2026-11-04T09:55:19+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## [LtAP](https://mikrotik.com/product/ltap)（RBLtAP-2HnD） {#ltap-rbltap-2hnd}

LtAP 是一款無線接入點，帶有三個用於蜂窩資料調變解調器的 SIM 卡槽。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責取得當地主管機構/檢驗部門對安裝結構完整性所需的任何地方或國家安全檢查。
- 在任何牆面上安裝接入點的所有安裝方法均需獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品 intended to be mounted outdoors on a pole but can also be installed indoors. 在開始安裝之前，請仔細閱讀安裝說明。使用錯誤的硬體和配置，或未遵循正確的操作步驟，可能導致人員危險和系統損壞。
- 我們無法保證因不當使用本裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行時，與您的身體、職業使用者或公眾的距離不得小於 120 釐米。

## 快速開始 {#quickstart}

按照以下快速步驟設定您的裝置：

- 擰下兩顆螺絲並取下艙門，以便接觸所有埠。參見（連結）插槽用法（可選）。
- 將 SIM 卡插入卡槽（可選）（參見（連結））。
- 連線 GPS 天線（可選）。
- 將裝置安裝到您想要的位置，參見相關段落。
- 選擇合適的供電方案，參見相關章節瞭解可能的方案。
- 下載 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。沒有設定預設 IP 地址，使用者名稱為 **admin**，且沒有密碼（或者，某些型號請在貼紙上檢視使用者名稱和無線密碼），使用 Neighbors 標籤頁並透過 MAC 地址連線；
- 您應當點選 "Check for updates" 按鈕，並將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。
- 選擇您的國家，以應用國家法規設定，並在載入的螢幕上設定您的密碼。
- 根據使用型別，將 *Installation* 設定為 indoors 或 outdoors。
- *產品的核心功能需要以下 RouterOS "npk" 軟體包：gps、system。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/30e4f8523c74a8b6.jpg)

- 內建 2 GHz 無線接入點模組，支援 AP/station/bridge/p2p 模式。板載內建 PIF 天線，以及用於外接天線的 MMCX 聯結器（可透過軟體選擇）。
- 兩個 miniPCIe 插槽和三個 SIM 插槽。
- 內建 GPS 模組，帶外部 SMA 聯結器。支援 - GPS、GLONASS、北斗、Galileo）。
- 千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。直通線或交叉線均可用於連線其他網路裝置。乙太網埠可透過無源 PoE 注入器接受 12-30 V DC 供電。
- 一個 DB9 RS232 序列埠，用於序列控制檯訪問。配置為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。
- 一個 USB 2.0 埠，用於儲存裝置或蜂窩調變解調器。

## 安裝 {#mounting}

- 可以使用提供的四顆螺絲和裝置上設計的四個孔，將裝置固定到牆上。
- 埠由一個小艙門保護，艙門由兩顆螺絲固定。取下後可接觸乙太網埠、天線聯結器、SIM 卡槽等。
- 艙門為所有可用埠留有開口位置，因此您可以穿過所有必要的線纜，但只需敲開您要使用的開口。
- 機殼上提供了多個用於外接天線的位置，請使用合適尺寸的鑽頭將其開出。請小心並測量所選天線，以免安裝時碰到內部 PCB 板。

![](/img/dc0a3d4ff60b80cb.webp)

裝置可在室內和室外使用。防護等級為 IP54。如果您打算在室外安裝，請確保所有線纜開口朝下。安裝方向由裝置上指向上的箭頭標示。使用 POE 注入器並做好正確接地。建議使用 Cat6 遮蔽線纜。警告！本裝置的安裝和執行時，裝置與身體之間的最小距離為 30 釐米。在住宅環境中操作本裝置可能造成無線電干擾。

## 配置 {#configuration}

您應當點選 "Check for updates" 按鈕，並將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下從網際網路埠的所有訪問均被阻止）。出於恢復目的，可以從網路啟動裝置，參見相關章節。

## GPS {#gps}

內建 GPS 模組需要使用外接天線（SMA 聯結器已安裝在裝置艙門後方）。請參見相關章節瞭解如何取下艙門。**注意** GPS 使用有源天線，請僅在裝置關閉時連線和斷開天線！

**支援 - GPS、GLONASS、北斗、Galileo）。** 請確保您的裝置上已安裝 GPS 軟體包。可透過以下命令檢查 /system package print。如果未安裝，請根據您的 RouterOS 版本從我們的下載頁面下載額外軟體包，並將 GPS 軟體包拖到 Files 選單中進行安裝。啟用 GPS 並開始工作：

- 啟用 - /system gps set enable=yes；
- 將天線設定為外接 - /system gps set gps-antenna-select=external；
- 檢查配置 - /system gps print。配置資訊 - [GPS 手冊，基本示例](/docs/mobile-networking/gps#basic-examples)

## 供電 {#powering}

- 直流輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）可透過隨附的 24 V、1.2 A 介面卡接受 12-30 V DC ⎓。
- 乙太網埠接受無源乙太網供電 12-30 V DC ⎓（補償線纜上的損耗，因此建議高於 12 V）。
- 汽車聯結器可用於從汽車和公交車中常見的 12/24 V ⎓ 連線為裝置供電。插頭有四個引腳：左下（黑色）為接地，右下為電源輸入（紅色）。上方兩個（AUX）保留供將來使用。無附件時最大負載下的功耗可達 12 W。將接地（地線）線連線到艙門下方的螺絲上。

### 連線到 PoE 介面卡：（不包含） {#connecting-to-a-poe-adapter-not-included}

- 將裝置上的乙太網線連線到 POE 介面卡的 POE out 埠。
- 將來自 LAN 的乙太網線連線到 POE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 前面板狀態 LED 行為 {#front-status-led-behavior}

- 常亮藍色 – 裝置已通電。
- 常亮綠色 – 使用者自定義 LED，可在系統設定中配置。
- 常亮綠色 – GPS 模組狀態。
- 常亮綠色– 五個綠色 LED 的組合，顯示蜂窩網路的訊號強度。

![](/img/1015646a55daf823.webp)

## miniPCIe 插槽 {#minipcie-slot}

### SIM 卡連線 {#sim-card-connectivity}

- MiniPCIe 1（上方插槽）支援 PCIe 和 USB 2.0 卡，但與 USB 2.0 type A 埠共用（不能同時使用 USB 埠和 miniPCIe 插槽）。它只能用於 SIM 插槽 #1。
- MiniPCIe 2（下方插槽）僅支援 USB（2.0 和 3.0）miniPCIe 調變解調器（不支援 PCIe）。使用 SIM 插槽 #2 和 SIM 插槽 #3。預設使用 SIM 插槽 #2。
- USB 2.0 type A 埠（僅在未使用 miniPCIe 1 時可用）。
- 要在上方 miniPCIe 插槽中使用 USB 型別的 miniPCIe 卡，請將 USB 連線切換到 miniPCIe 插槽：/system routerboard usb set type=mini-PCIe 這將停用裝置前面的 USB 2.0 埠。
- 將 SIM 卡插入上方插槽時，SIM 卡晶片朝下。下方插槽 – 晶片朝上。請檢查您使用的是正確的 SIM 插槽。對於插入下方 mini-pcie 插槽的調變解調器，您需要使用 SIM 插槽 2 或 SIM 插槽 3。並且需要在 RouterOS 中選擇所使用的 SIM 插槽。選擇 SIM 插槽的 CLI 命令：*/system routerboard modem set sim-slot=2*

### 調變解調器安裝 {#modem-installation}

本 LtAP 版本未安裝調變解調器。在這種情況下，內部天線未連線。安裝 miniPCIe 模組應由合格人員進行，處理電氣裝置時請遵循安全預防措施，本裝置支援兩張 LR 卡：

- 拆包和處理電子元件時，請使用腕帶接地，以避免靜電放電（ESD）損壞；
- 取下機殼底部的六顆螺絲，並掀起機殼頂部；
- 找到 miniPCIe 插槽並取下出廠時安裝的兩顆螺絲；
- 將隨附的厚導熱墊貼到卡上，並將卡安裝到 miniPCIe 插槽中，使導熱墊位於 PCB 和卡之間；
- 使用先前取下的兩顆螺絲將卡固定到位；
- 將內部天線線纜連線到您的調變解調器。或者將天線線纜穿過 GPS 聯結器附近的開口並連線到調變解調器。建議使用矽橡膠將聯結器固定到位。
- 在卡的頂部貼上較薄的導熱墊；
- 使用外接天線時，可將聯結器安裝在機殼側面，開孔請使用 6.5 mm 鑽頭，參見第 4 部分；
- 參見下圖，瞭解如何放置橡膠密封件以獲得最佳防水保護；

![](/img/03bc306812c7acce.webp)

- 按相反順序重新組裝。PCB 螺絲的擰緊力矩為 0.3 Nm，機殼蓋/外殼螺絲為 0.5 Nm。將裝置重新裝入機殼並用先前取下的螺絲固定後，將移動運營商的 SIM 卡滑入 SIM 卡槽，晶片朝向如埠標籤所示。該卡槽接受 miniSIM（2FF）。SIM 插槽 2 和 3 適用於下方 miniPCIe 插槽，可在 RouterOS 的 "/system routerboard sim" 選單中切換。

## 復位按鈕 {#reset-button}

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在將尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入程式。適用於 RouterBOOT 偵錯和恢復。

## 配件 {#accessories}

包裝中包括隨裝置提供的附件：

- K-67 緊固套件。包括四顆 4x25 mm 螺絲、四個 6x30 mm 膨脹螺栓。
- 線纜 DC ⎓（H4130-04PDB000R 3 mm 2x2P Housing）到（StripJacket 5 cm+WireEnd Strip/Tin 1 cm）24 AWG（黑/紅/藍/橙）0.35 m。
- 歐盟/美國開關電源 24 V、1.2 A、28.8 W、86.8%、VI，DC ⎓ 線纜：220 cm RA DC 插頭 mod Hor CMC 較短插頭。
- 彈性導熱墊 - 25x40x3.5mm +30x45x1mm，裝在自封袋中。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統未經測試。

## 規格 {#specifications}

有關本產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/ltap](https://mikrotik.com/product/ltap)

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描 QR 碼並選擇您偏好的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將被自動填入。
- 選擇 Connect，透過無線網路與您的裝置建立連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要設定。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許商業使用。
- 如果 WLAN 裝置的工作範圍與上述法規不同，則需要將製造商/供應商提供的定製韌體版本應用到終端使用者裝置上，並防止終端使用者重新配置。
- 室外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料手冊可在製造商官方網站上獲取。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，TX 功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，TX 功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，TX 功率限制為 20dBm（EIRP）。

請確保裝置具有 lock 軟體包（來自制造商的韌體版本），需要將其應用到終端使用者裝置上，以防止終端使用者重新配置。產品將標註國家程式碼 "-EG"。本裝置需要升級到最新版本，以確保符合當地主管機構的規定！終端使用者有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

為避免環境汙染，請將裝置與生活垃圾分開，並以安全方式處置，例如送往指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>Model</th><th>FCCID</th></tr></thead><tbody><tr><td>RBLtAP-2HnD</td><td>TV7LTAP2HND</td></tr></tbody></table>

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的有害干擾防護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。然而，不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），建議使用者嘗試透過以下措施之一來糾正干擾：

- 重新調整或放置接收天線。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。**FCC 警告：** 未經負責合規的一方明確批准的任何更改或修改，可能會使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作需滿足以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受所接收的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與其他任何天線或發射器共址或一起使用。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和執行時，輻射體與您身體任何部位之間的最小距離為 30 釐米。本封閉式裝置符合 FCC 規則和法規 47CFR 第 15 C 段。操作需滿足以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受所接收的任何干擾，包括可能導致意外操作的干擾。

*使用 CBRS 頻段時，最終主機裝置的 CBSD 類別將取決於所使用的功率設定和天線增益。*

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>Model</th><th>FCCID</th></tr></thead><tbody><tr><td>RBLtAP-2HnD</td><td>7442A-LTAP2HND</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作需滿足以下兩個條件：(1) 本裝置不得造成干擾，並且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。本裝置符合適用於免許可無線電裝置的加拿大工業部 CNR 標準。其執行須滿足以下兩個條件：(1) 裝置不得產生干擾，並且 (2) 裝置使用者必須接受任何無線電干擾，即使該干擾可能損害其執行。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和執行時，輻射體與您身體任何部位之間的最小距離為 20 釐米。

## UKCA 標識 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>≤100 mW</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊標註在其標籤上序列號末尾的小數點後。第一位數字表示年份編號（年份的最後一位數字），其後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2412-2472 MHz（30 dBm）。可用頻率通道可能因產品型號和認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2412-2472 MHz（20 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 NCCIR 2012 年 11 月 1 日第 559 號決定（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBLtAP-2HnD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相關型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在歐盟所有成員國使用無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！*
