---
title: "RB922UAGS-5HPacD"
slug: /rb922uags-5hpacd
source: https://manual.mikrotik.com/hardware/rb922uags-5hpacd
captured_at: '2026-11-04T10:00:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/480374f204f382a6.jpg)

720Mhz CPU、128MB RAM、1xGigabit Ethernet、1xSFP 插槽、1xminiPCI-e、1xSIM、板載 802.11ac 雙鏈 5Ghz 無線、RouterOS L4。有關完整規格和產品手冊，請參閱 [RB922UAGS-5HPacD 產品頁面](https://mikrotik.com/product/RB922UAGS-5HPacD)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應按照所有國家法律和法規進行。將接入點安裝在任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。裝置的安裝必須符合當地和國家的電氣規範。本產品設計用於在戶外立杆上安裝，但也可以安裝在室內。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。僅使用製造商認可且可在本產品原包裝中找到的電源和配件。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置發生故障，請將其斷電。最快的方法是將電源插頭從電源插座中拔出。客戶有責任遵守當地國家/地區的規定，包括在合法頻率通道內工作、輸出功率、布纜要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**暴露於射頻輻射：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行應使其與您的身體、職業使用者或公眾的距離不小於 20 釐米。

## 首次使用 {#first-use}

-

插入 miniPCIe 卡和 SIM 卡。

-

將天線線纜連線到 miniPCIe 卡。

-

（可選）將裝置安裝到外殼中。

-

將乙太網線纜連線到千兆乙太網埠。

-

插上電源線以開啟裝置。

-

透過 192.168.88.1 訪問；

-

使用者名稱為 admin，無密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）。

-

選擇您所在的國家/地區，以應用該國家/地區的法規設定。

-

設定密碼。

## 供電 {#powering}

裝置可從電源插孔或乙太網埠接受供電：

- 直接輸入電源插孔（外徑 5.5mm、內徑 2mm，母頭，中心針為正極）接受 8-30 V DC。
- 乙太網埠接受無源乙太網供電 8-30 V DC。最大負載下的功耗可達 17 W。

## 配置 {#configuration}

登入後，我們建議在 QuickSet 選單中點選 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將使用的國家/地區，以符合當地法規。RouterOS 除本文件所述內容外還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參閱相關章節。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個千兆乙太網埠可接受來自無源 PoE 注入器的 10-30 V DC 供電。
- 一個 SFP 插槽。
- 一個 miniPCIe 插槽，用於 3G/4G/LTE 調變解調器或其他無線網路卡。
- USB 埠。
- 2x MMCX 聯結器，用於內建的強勁 802.11ac 2x2 無線模組。
- SIM 插槽（需要 3g miniPCIe 卡）。

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在會尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## miniPCIe 插槽使用 {#minipcie-slot-usage}

本裝置配備一個支援 3G/4G/LTE 調變解調器或 WiFi 模組的 miniPCIe。SIM 插槽用於與 miniPCIe 調變解調器配合使用，不能單獨使用。

## 作業系統支援 {#operating-system-support}

本裝置支援版本號等於或高於 RouterOS 選單 /system resource 中所指示版本的 RouterOS 軟體。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢棄物處置場所。請了解將裝置正確運送到您所在地區指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID: TV7RB922-5HPACTM

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，證明符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝中的有害干擾提供合理防護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來判定），則建議使用者嘗試透過以下措施之一來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。 **FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期操作的干擾。本裝置及其天線不得與任何其他天線或發射器同址放置或聯合操作。

**重要：暴露於射頻輻射**。天線與使用者之間必須保持至少 20 釐米的距離。在此配置下，可滿足 FCC 針對一般人群/非受控環境規定的輻射暴露限值。天線安裝。

警告：安裝人員有責任確保在美國（或適用 FCC 規則的地方）使用授權天線時，僅使用隨產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用任何非隨產品認證的天線。安裝人員應根據國家/地區法規和每種天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC: 7442A-9225HPACT 本裝置符合加拿大工業部免許可 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。本裝置符合加拿大工業部針對免許可無線電裝置適用的 CNR 要求。允許在以下兩個條件下操作：(1) 裝置不得產生干擾，且 (2) 裝置使用者必須接受所受到的任何無線電干擾，即使該干擾可能影響其正常執行。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：暴露於射頻輻射。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和執行應使輻射體與您身體的任何部位之間保持至少 20 釐米的距離。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射功率</th></tr></thead><tbody><tr><td>5150-5350 МГц，5650-5850 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證而有所不同。

裝置生產日期資訊以斜槓分隔的形式標註在其標籤上的序列號末尾。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準（Norma Oficial Mexicana） {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5470-5725 МГц（27 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用須按照 NKРЗІ 2012 年 11 月 1 日第 559 號決議（2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 在此宣告，無線電裝置型別 RB922UAGS-5HPacD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家/地區的規定，包括在合法頻率通道內工作、輸出功率、布纜要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。如需更詳細的資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定所規定的 WLAN 最大發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。如需更多資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。如需更多資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限值。如需更多資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 最大發射功率限值。如需更多資訊，請參見上文的符合性宣告。
