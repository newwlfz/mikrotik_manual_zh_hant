---
title: "LtAP mini kit 系列"
slug: /ltap-mini-kit-series
source: https://manual.mikrotik.com/hardware/ltap-mini-kit-series
captured_at: '2026-11-04T09:55:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **[LtAP mini LTE kit](https://mikrotik.com/product/ltap_mini_lte_kit_2024)**（RB912R-2nD-LTm&R11e-LTE）
- **LtAP mini LTE kit-US**（RB912R-2nD-LTm&R11e-LTE-US）
- **LtAP mini 4G kit**（RB912R-2nD-LTm&R11e-4G）
:::

LtAP mini LTE kit 是一款帶兩個 SIM 卡槽的無線接入點。LtAP mini LTE、4G kit 出廠時已預裝一張卡。

## 安全警告 {#safety-warnings}

-

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。

-

本產品的最終處置應依照所有國家法律和法規進行。

-

將接入點安裝於任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。

-

裝置的安裝必須符合當地和國家的電氣規範。

-

本產品設計為安裝在戶外的抱杆上，但也可在室內安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確的操作步驟，可能導致人員處於危險境地並損壞系統。

-

請僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。

-

在將系統連線到電源之前，請閱讀安裝說明。

-

我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！

-

如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。

-

客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

-

本裝置未經 UL 的戶外使用測試。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟為不受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和執行時，與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 連線 {#connecting}

- 將乙太網線連線到乙太網埠（如果使用 LTE 作為主要連線，則此步驟可選）；
- 使用 miniPCIe 插槽安裝您的調變解調器（可選）；
- 將 SIM 卡插入 SIM 卡槽；
- 連線 GPS 天線（參見 ""，可選）；
- 選擇您的供電方案（參見 ""）；
- 在計算機上進入網路連線部分，找到名為 "*MikroTik-....*" 的無線網路。然後連線到它；
- 配置應透過無線網路使用 Web 瀏覽器或移動應用程式進行。或者，您可以使用 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1)；
- 使用者名稱：**admin**，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 選擇 "Check for updates" 按鈕，將 RouterOS 更新到最新版本。裝置需要有效的網際網路連線；
- 如需手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 查詢您的產品。所需的軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 **WinBox** 的 **Files** 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 在 **QuickSet** 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 安裝 {#mounting}

![](/img/ef26d7a069bd38f5.jpg)

- 可以使用裝置兩側提供的螺絲孔將裝置固定在牆上。裝置的安裝方式應使線纜開口朝下，如圖所示。
- 埠由一個小門保護，小門用一顆螺絲固定。請使用 Philips PH2 螺絲刀開啟以接觸埠。
- 小門上為所有可用埠預留了可掰開的開口，但請只掰開您要使用的開口。本裝置可在室內和室外使用。本裝置的 IP 防護等級為 IP54。
- 裝置外殼上有可為外接 LTE 和 GPS 天線鑽孔的位置。請使用鑽頭鑽出適合所用天線線纜的孔。或者，您可以選購 "DINrail Pro" 安裝支架，適用於標準 35 mm x 7.5 mm 的 DIN 導軌。[https://mikrotik.com/product/dinrail_pro](https://mikrotik.com/product/dinrail_pro)

在戶外安裝時，請確保所有線纜開口朝下。請使用 PoE 注入器和正確的接地。建議使用 Cat6 線纜。*警告！本裝置的安裝和執行時，裝置與您的身體之間應保持至少 20 釐米的距離。在住宅環境中使用本裝置可能會造成無線電干擾。* *本裝置的安裝和配置應由具備資質的人員完成。*

## 供電 {#powering}

- 直流輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）可接受 8-30 V DC。
- micro USB 埠可接受 5 V 供電。
- 乙太網埠支援無源和 802.3af/at 乙太網供電，8-57 V DC（需補償線纜損耗，因此建議高於 12 V）。在最大負載並連線外設時，功耗可達 9 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/8cb2973499cab5a9.webp)

- 內建 2 GHz 無線接入點模組，支援 AP/station/bridge/p2p 模式。板載內建 PIF 天線。天線增益 1.5 dBi。
- miniPCIe 插槽和兩個 SIM 卡槽（未安裝調變解調器時無法使用，且不能同時使用）可與 3G/4G/LTE 調變解調器配合使用。裝置提供板載天線，但外殼上提供了外接天線的開口。
- 內建 GPS 模組 - 提供 uFL 聯結器用於外接天線。要啟用，請將埠設定為 serial0（這將停用裝置上的 DB9 埠）。支援（GPS、GLONASS、BeiDou、Galileo）。
- 一個 10/100 乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。直通線或交叉線均可用於連線其他網路裝置。乙太網埠可接受來自無源 PoE 注入器的 12-57 V DC 供電。
- 一個 DB9 RS232 序列埠，用於序列控制檯訪問。配置為 115200 bit/s，8 個數據位，1 個停止位，無校驗。如果在 serial0 上啟用了內建 GPS，則無法使用。
- 一個僅用於供電的 micro USB 2.0 埠。

## 配置 {#configuration}

RouterOS 除了本文件所述內容外，還包含許多配置選項。建議從這裡開始熟悉各項功能：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下，來自網際網路埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，參見章節 。

## miniPCIe 插槽使用 {#minipcie-slot-usage}

本裝置配備一個 miniPCIe 插槽和出廠預裝的 LTE 調變解調器。提供兩個 SIM 卡槽，供與 miniPCIe 調變解調器配合使用。SIM 卡槽不能單獨使用。

在這種情況下，內建天線連線到調變解調器。更換 miniPCIe 模組應由具備資質的人員完成，處理電氣裝置時請遵循安全預防措施：- 在拆包和處理電氣元件時使用腕帶接地，以避免靜電放電（ESD）損壞。

- 用 Philips PH2 螺絲刀擰下一顆螺絲，開啟前蓋。
- 拆下機箱底部的四顆螺絲，取下圖中的機箱頂部。您會看到連線在其上的天線。
- 在 PCB 上找到 miniPCIe 卡，並拆下兩顆螺絲。
- 將隨附的厚導熱墊貼到卡上，然後將卡安裝到 miniPCIe 插槽中，使導熱墊位於 PCB 和卡之間。
- 使用之前拆下的兩顆螺絲將卡固定到位。
- 將灰色 uFL 聯結器連線到調變解調器的 MAIN 天線聯結器，將黑色線纜連線到次級（或 AUX）聯結器。
- 要使用外接天線（不包含），請安裝天線聯結器，並使用 6.5 mm 鑽頭在裝置側面鑽孔。（參見 ""）說明 4。
- 參見下圖瞭解如何放置橡膠密封圈以獲得最佳防水效果。

![](/img/57f7ee8c33feb316.webp)

- 將天線聯結器安裝到已安裝的卡上以及 PCB 上的 GPS 聯結器上，可額外使用橡膠矽膠將聯結器固定在卡和 PCB 板上。

![](/img/45f214e7c671f1bf.webp)

將較薄的導熱墊貼到卡的頂部。

- 重新組裝。將裝置重新裝入機箱並用之前拆下的螺絲固定後，將移動運營商的 SIM 卡滑入 SIM 卡槽，晶片朝向如埠標籤所示。卡槽接受 miniSIM（2FF）。合上 SIM 卡的黑色卡扣，將其固定在卡槽中。

## GPS 使用 {#gps-usage}

要使用 GPS，需要連線外接天線。使用 "ACGPSA" - 可單獨購買。ACGPSA 是一款獨立的有源 GPS 天線，工作在 1575.4 MHz 頻段。天線尺寸為 46.5 mm x 26.5 mm x 12.5 mm，防護等級為 IP67，內建磁鐵和雙面膠，因此可以輕鬆固定在各種表面上。它配有一根 5m 長的線纜，帶有 SMA 聯結器，可透過 ACSMAUFL 尾纖（不包含，產品程式碼 ACSMAUFL）連線到 LtAP mini [https://mikrotik.com/product/acgpsa](https://mikrotik.com/product/acgpsa) [https://mikrotik.com/product/acsmaufl](https://mikrotik.com/product/acsmaufl) 要連線 GPS 天線，請參見 "miniPCIe 插槽使用" 第 10 步。**支援 - GPS、GLONASS、BeiDou、Galileo）。**

配置資訊：[GPS 基本示例](/docs/mobile-networking/gps#basic-examples)。

GPS 使用有源天線，請僅在斷電時連線。

## 按鈕和跳線 {#buttons-and-jumpers}

### 復位按鈕 {#reset-button}

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 將常亮，此時鬆開可開啟 CAP 模式。裝置現在將尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統都會載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

### 模式按鈕 {#mode-button}

模式按鈕的動作可以透過 RouterOS 軟體配置為執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。模式按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## 配件 {#accessories}

包裝內含隨裝置提供的以下配件：

- DC ⎓ 開關電源 24 V，1.2 A，28.8 W，86.8 %，VI，線纜：220 cm RA DC。
- 線纜 DC ⎓ 插頭 RA 5.5x2.1x10.5 轉鍍錫 2*24 AWG 8 mm，長度 0.35 m。
- 帶遮蔽乙太網線纜/聯結器的 PoE 注入器（RBPoE）。
- DC ⎓ 24 V 1.2 A 電源介面卡。
- 安裝套件 K-55 VMS。
- 彈性導熱墊，25x40x3.5 mm。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：\{+\}[https://mikrotik.com/product/ltap_mini_lte_kit](https://mikrotik.com/product/ltap_mini_lte_kit)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱將已填寫。
- 選擇 Connect 以透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCCID</th><th>包含 FCCID</th></tr></thead><tbody><tr><td>RB912R-2nD-LTm&R11e-LTE</td><td>TV7RB912R-2NDLTM</td><td></td></tr><tr><td>RB912R-2nD-LTm&R11e-LTE-US</td><td>TV7RB912R-2NDLTM</td><td>TV7R11ELTE</td></tr><tr><td>RB912R-2nD-LTm&R11e-4G</td><td>TV7RB912R-2NDLTM</td><td>TV7R11E4G</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供針對有害干擾的合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。**FCC 警告：** 未經合規負責方明確批准的任何更改或修改，都可能使使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。

注意：本裝置在測試時外圍裝置使用了遮蔽線纜。為確保合規，必須使用遮蔽線纜連線本裝置。

**重要：射頻輻射暴露。**

本裝置符合 FCC 為不受控環境規定的輻射暴露限值。本裝置的安裝和執行時，輻射體與您身體的任何部位之間應保持至少 20 釐米的距離。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th><th>包含 IC</th></tr></thead><tbody><tr><td>RB912R-2nD-LTm&R11e-LTE</td><td>TV7RB912R-2NDLTM</td><td>無</td></tr><tr><td>RB912R-2nD-LTm&R11e-LTE-US</td><td>7442A-912R2NDLTM</td><td>7442A-R11ELTE</td></tr><tr><td>RB912R-2nD-LTm&R11e-4G</td><td>7442A-912R2NDLTM</td><td>7442A-R11E4G</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須符合以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合 IC 為不受控環境規定的輻射暴露限值。本裝置的安裝和執行時，輻射體與您身體的任何部位之間應保持至少 20 釐米的距離。Cet equipement est conforme aux limites d'exposition au rayonnement IC definies pour un environnement non controle. Cet equipement doit etre installe et utilise a une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный диапазон</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>2400-2483.5 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

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

Робоча частота (Максимальна вихідна потужність): 2480-2483.5 МГц (20 дБм).

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WLAN / 2G / 3G / LTE {#wlan--2g--3g--lte}

<table><thead><tr><th>工作頻率 / 最大輸出功率 Betriebsfrequenz / maximale Ausgangsleistung Fréquence de fonctionnement / puissance de sortie maximale Frequenza operativa / massima potenza di uscita Frecuencia de funcionamiento / potencia de salida máxima Рабочая частота / максимальная выходная мощность</th><th>WLAN</th><th>2400-2483.5 MHz / 20 dBm</th></tr></thead><tbody><tr><td>E-GSM-900</td><td>900 MHz / 33dB</td><td></td></tr><tr><td>DCS-1800</td><td>1800 MHz / 30dB</td><td></td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 24dB ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 24dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1700 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dB ± 2.7 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 規定的最大 WLAN 和 LTE 發射功率限值。有關更多詳細資訊，請參見上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- und LTE-Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN et LTE conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN e LTE in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN y LTE de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN и LTE в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.
