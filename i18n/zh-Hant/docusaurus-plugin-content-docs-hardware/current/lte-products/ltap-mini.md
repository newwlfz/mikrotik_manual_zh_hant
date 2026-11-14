---
title: "LtAP mini"
slug: /ltap-mini
source: https://manual.mikrotik.com/hardware/ltap-mini
captured_at: '2026-11-04T09:55:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/ef26d7a069bd38f5.jpg)

## [LtAP mini](https://mikrotik.com/product/ltap_mini) (RB912R-2nD-LTm) {#ltap-mini-rb912r-2nd-ltm}

LtAP mini 是一款帶有兩個用於 3G/LTE 資料的 SIM 卡槽的無線接入點。LtAP mini 設計用於搭配您自己的調變解調器使用。

## 安全警告 {#safety-warnings}

-

在操作任何裝置之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。

-

本產品的最終處置應按照所有國家法律和法規進行。

-

將接入點安裝到任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。

-

裝置的安裝必須符合當地和國家電氣規範。

-

本產品擬安裝在室外杆上，但也可安裝在室內。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確步驟，可能會對人員造成危險並損壞系統。

-

僅使用製造商認可的電源和配件，這些物品可在本產品的原包裝中找到。

-

將系統連線到電源之前，請閱讀安裝說明。

-

我們無法保證因裝置使用不當而不會發生事故或損壞。請謹慎使用本產品，操作風險自負！

-

如果裝置發生故障，請斷開其電源。最快的做法是將電源插頭從電源插座中拔出。

-

客戶有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置都必須由專業人員安裝。

-

該裝置未經過 UL 的室外使用測試。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟為不受控環境設定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，應與您的身體、職業使用者或公眾保持不少於 20 釐米的距離。

## 連線 {#connecting}

- 安裝所需的調變解調器（參見 ""）。
- 如果打算使用 GPS，則需要外接天線（參見 ""）。
- 選擇您的供電方案（參見 ""）。
- 將您的 Internet 電纜連線到乙太網埠。
- 將計算機的 IP 配置設定為 *自動*（DHCP）。
- 如果不使用 PoE，請連線您的直接輸入電源插孔以啟動裝置。
- 裝置將啟動，無線網路將可供連線。
- 在您的 PC、手機或其他裝置上開啟網路連線，搜尋 MikroTik 無線網路並連線到它。
- 連線到無線網路後，在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始配置；由於預設沒有密碼，您將自動登入（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。也可以使用移動應用（參見 ""）和 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 完成配置。
- 您應選擇“檢查更新”按鈕，並將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。
- 選擇您的國家/地區，以應用國家/地區法規設定，並在載入的螢幕上設定密碼。
- *本產品的核心功能需要以下 RouterOS "npk" 軟體包：gps、system。

## 安裝 {#mounting}

![](/img/68d9301126412ebe.webp)

- 可以使用裝置側面提供的螺絲孔將裝置固定到牆上。裝置安裝時應使電纜開口朝下，如圖所示。
- 埠由一個小門保護，該門用一顆螺絲固定。使用 Philips PH2 螺絲刀開啟以接觸埠。
- 該門為所有可用埠留有開口位置，但只應破開您將使用的開口。該裝置可在室內和室外使用。該裝置的 IP 防護等級為 IP54。
- 裝置外殼上有可為外接 LTE 和 GPS 天線鑽孔的位置。使用鑽頭鑽出適合所用天線電纜的孔。或者，您可以購買 "DINrail Pro" 安裝支架，其設計適用於標準 35 mm x 7.5 mm DIN 導軌。[https://mikrotik.com/product/dinrail_pro](https://mikrotik.com/product/dinrail_pro)

在室外安裝時，確保任何電纜開口都朝下。使用 PoE 注入器和正確接地。建議使用 Cat6 電纜。

![](/img/9a7d512c8e08d773.webp)

*警告！本裝置安裝和操作時，裝置與您的身體之間應保持至少 20 釐米的距離。在住宅環境中操作本裝置可能會造成無線電干擾。* *本裝置的安裝和配置應由合格人員完成。*

## 供電 {#powering}

所有電壓均符合 ES1，並符合 EN IEC 62368-1 規定的最大 PS2/LPS。

<table><thead><tr><th>**輸入電壓**</th><th>DC 插頭：8-30 VDC ![](/img/f40c45a76b237ba5.webp) USB：5 VDC PoE：8-57 VDC</th></tr></thead><tbody><tr><td>**輸入功率**</td><td>9W</td></tr></tbody></table>

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 8-30 V DC。
- microUSB 埠接受 5 V 供電。
- 乙太網埠接受無源和 802.3af/at 乙太網供電（PoE）8-57 V DC（補償電纜上的損耗，因此建議高於 12 V）。帶附件時最大負載下的功耗可達 9 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網電纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的乙太網電纜連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

![](/img/8cb2973499cab5a9.webp)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 內建 2 GHz 無線接入點模組，支援 AP/station/bridge/p2p 模式。板載 PIF 天線為內建。天線增益 1.5 dBi。
- miniPCIe 插槽和兩個 SIM 卡槽（未安裝調變解調器時無法使用，且不能同時使用）用於搭配 3G/4G/LTE 調變解調器。提供板載天線，但機殼上提供了外接天線開口。
- 內建 GPS 模組 - 提供用於外接天線的 uFL 聯結器。要啟用，請將埠設定為 serial0（這會停用裝置上的 DB9 埠）。支援 - GPS、GLONASS、BeiDou、Galileo）。
- 一個 10/100 乙太網埠，支援自動交叉/直通電纜修正（Auto MDI/X）。可使用直通或交叉電纜連線到其他網路裝置。乙太網埠接受來自無源 PoE 注入器的 12-57 V DC 供電。
- 一個 DB9 RS232 序列埠，用於序列控制檯訪問。配置為 115200 bit/s、8 個數據位、1 個停止位、無校驗。如果在 serial0 上啟用了內建 GPS，則無法使用。
- 一個僅用於供電的 microUSB 2.0 埠。

## 配置 {#configuration}

RouterOS 除了本文件所述內容外，還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參見章節 。

## miniPCIe 插槽使用 {#minipcie-slot-usage}

該裝置配備一個 miniPCIe 插槽，用於搭配 3G/4G/LTE 調變解調器。提供兩個 SIM 卡槽，與 miniPCIe 調變解調器一起使用。SIM 卡槽不單獨使用。在這種情況下，內部天線不會連線（位於機殼內部）。安裝 miniPCIe 模組應由合格人員完成，處理電氣裝置時請遵循安全預防措施：

- 拆包和處理電氣元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞。
- 使用 Philips PH2 螺絲刀擰下一顆螺絲，開啟前蓋。
- 卸下機殼底部的四顆螺絲，並取下機殼頂部。您會看到連線在其上的天線。
- 找到 PCB 上的 mini PCIe 插槽，並卸下兩顆出廠時附帶的螺絲。
- 將隨附的厚導熱墊貼到卡上，並將卡安裝到 miniPCIe 插槽中，使導熱墊位於 PCB 和卡之間。
- 使用之前卸下的兩顆螺絲將卡固定到位。
- 將灰色 uFL 聯結器連線到調變解調器的 MAIN 天線聯結器，將黑色電纜連線到輔助（或 AUX）聯結器。
- 要使用外接天線，請連線天線聯結器，並使用 6.5 mm 鑽頭在裝置側面鑽孔。（參見 ""）說明 4。
- 請參見下圖，瞭解如何放置橡膠密封圈以獲得最佳防水保護。

![](/img/57f7ee8c33feb316.webp)

- 將天線聯結器連線到已安裝的卡以及 PCB 上的 GPS 聯結器，可使用額外的橡膠矽膠將聯結器固定在卡和 PCB 板上。

![](/img/45f214e7c671f1bf.webp)

- 將較薄的導熱墊貼到卡的頂部。
- 按相反順序重新組裝。將裝置重新裝入機殼並用之前卸下的螺絲固定後，將移動運營商的 SIM 卡滑入 SIM 卡槽，晶片朝向如埠標籤所示。卡槽接受 miniSIM（2FF）。合上 SIM 卡的黑色鎖釦，將其固定在卡槽中。

## GPS 使用 {#gps-usage}

為了使用 GPS，需要連線外接天線。使用 "ACGPSA" - 可單獨購買。ACGPSA 是一款獨立的有源 GPS 天線，工作在 1575.4 MHz 頻譜。天線尺寸為 46.5 mm x 26.5 mm x 12.5 mm，防護等級為 IP67，幷包含內部磁鐵和雙面膠，因此可以輕鬆附著到各種表面。它有一條帶 SMA 聯結器的 5m 長電纜，可透過 ACSMAUFL 尾纖（未包含，產品程式碼 ACSMAUFL）連線到 LtAP mini [https://mikrotik.com/product/acgpsa](https://mikrotik.com/product/acgpsa) [https://mikrotik.com/product/acsmaufl](https://mikrotik.com/product/acsmaufl) 要連線 GPS 天線，請參見“miniPCIe 插槽使用”步驟 10。

**支援 - GPS、GLONASS、BeiDou、Galileo）。**

配置資訊 - [GPS 手冊、基本示例](/docs/mobile-networking/gps#basic-examples)

GPS 使用有源天線，僅在電源關閉時連線。

## 按鈕和跳線 {#buttons-and-jumpers}

### 復位按鈕 {#reset-button}

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（總計 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開以開啟 CAP 模式。裝置現在將尋找 CAPsMAN 伺服器（總計 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（總計 15 秒）。無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

### 模式按鈕 {#mode-button}

模式按鈕的動作可以透過 RouterOS 軟體配置為執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。模式按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## 配件 {#accessories}

包裝內含以下隨裝置提供的配件：

- DC ⎓ 開關電源 24 V、1.2 A、28.8 W、86.8 %、VI，電纜：220 cm RA DC。
- 電纜 DC ⎓ 插頭 RA 5.5x2.1x10.5 轉 剝皮 2*24 AWG 鍍錫 8 mm，長度 0.35 m。
- 帶遮蔽乙太網電纜/聯結器的 PoE 注入器（RBPoE）。
- DC ⎓ 24 V 1.2 A 電源介面卡。
- 安裝套件 K-55 VMS。
- 彈性導熱墊，25x40x3.5 mm。

## 規格 {#specifications}

有關本產品、規格和圖片的更多資訊，請訪問我們的網頁：[https://mikrotik.com/product/ltap_mini](https://mikrotik.com/product/ltap_mini)

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描 QR 碼並選擇您首選的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將已輸入。
- 選擇“連線”以透過無線網路建立與裝置的連線。
- 選擇快速設定，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要設定。

為避免環境汙染，請將裝置與生活垃圾分開，並以安全方式處置，例如在指定的廢物處置場所處置。請熟悉您所在地區將裝置正確運輸到指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCCID</th></tr></thead><tbody><tr><td>RB912R-2nD-LTm</td><td>TV7RB912R-2NDLTM</td></tr></tbody></table>

本裝置已透過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的有害干擾防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 請諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。**FCC 警告：** 未經合規負責方明確批准的任何更改或修改，可能會使使用者操作本裝置的許可權失效。本裝置符合 FCC 規則第 15 部分。操作需滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共址或協同操作。

**重要：射頻輻射暴露。** 本裝置符合 FCC 為不受控環境設定的射頻輻射暴露限值。本裝置安裝和操作時，輻射體與您身體的任何部位之間應保持至少 20 cm 的距離。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RB912R-2nD-LTm</td><td>7442A-912R2NDLTM</td></tr></tbody></table>

本裝置符合加拿大工業部免許可證 RSS 標準。操作需滿足以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。本裝置符合加拿大工業部適用於免許可證無線電裝置的 CNR 標準。操作需滿足以下兩個條件：(1) 裝置不得產生干擾，且 (2) 裝置使用者必須接受所受到的任何無線電干擾，即使該干擾可能影響裝置的正常執行。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合 IC 為不受控環境設定的輻射暴露限值。本裝置安裝和操作時，輻射體與您身體的任何部位之間應保持至少 20 cm 的距離。本裝置符合 IC 為不受控環境設定的輻射暴露限值。本裝置安裝和使用時，輻射體與您身體的任何部位之間應保持至少 20 cm 的最小距離。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射器功率</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>≤100 mW</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊位於其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位表示週數。

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

## 烏克蘭國家通訊和資訊領域監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2480-2483.5 MHz（20 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置，需按照烏克蘭國家通訊和資訊領域監管委員會（НКРЗІ）2012 年 11 月 1 日第 559 號決議批准、並在烏克蘭司法部於 2013 年 1 月 3 日以第 57/22589 號登記的秩序取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RB912R-2nD-LTm 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相關型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置都必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告。/ 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。有關更多資訊，請參見上文的符合性宣告。/ 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。有關更多資訊，請參見上文的符合性宣告。/ 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。有關更多資訊，請參見上文的符合性宣告。/ 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 最大發射功率限值。有關更多資訊，請參見上文的符合性宣告。
