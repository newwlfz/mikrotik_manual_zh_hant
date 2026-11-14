---
title: "LHGG LTE6 套件"
slug: /lhgg-lte6-kit
source: https://manual.mikrotik.com/hardware/lhgg-lte6-kit
captured_at: '2026-11-04T09:55:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/9214d5a2d4899217.jpg)

## [LHGG LTE6 kit](https://mikrotik.com/product/lhgg_lte6_kit) (RBLHGGR&R11e-LTE6) {#lhgg-lte6-kit-rblhggrr11e-lte6}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。完整規格和手冊請參閱 [LHGG LTE6 kit 產品頁面](https://mikrotik.com/product/lhgg_lte6_kit)。
- 本產品的最終處置應遵守所有國家法律和法規。
- 在任何牆面上安裝接入點的所有安裝方式均須獲得當地管轄部門的認可。
- 裝置安裝必須符合當地和國家電氣規範。
- 本產品設計用於在戶外立杆上安裝。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體和配置或未遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，操作風險自負！
- 若裝置發生故障，請斷開其電源。最快的方法是從電源插座上拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 這是 A 類裝置。在居住環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 130 釐米。

## 快速開始 {#quickstart}

- 開啟乙太網埠蓋板；
- 將 SIM 卡插入插槽，晶片朝上；
- 用乙太網線將裝置連線到隨附 PoE 注入器的 data+power 端；
- 將 PoE 注入器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 在網頁瀏覽器中開啟 [https://192.168.188.1](https://192.168.188.1)；
- 使用者名稱：**admin**，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如果您的行動網路運營商要求，請輸入 PIN 碼；
- 使用檢查更新選項將裝置升級到最新版本。您必須有一張已啟用且還有可用流量的 SIM 卡；
- 裝置將重啟；
- 再次連線，並在 **QuickSet** 選單中設定一個強密碼。

## 外殼組裝 {#case-assembly}

- 將兩條支腿分別滑入相應的一側，以安裝到 LHG 外殼上。兩條支腿不同且不可互換（面對產品時，使乙太網埠蓋板朝向您，標有 R 的支腿用於右側，標有 L 的支腿用於左側）。
- 將組裝好的 LHG 單元卡入網格的適當中心位置。
- 用隨附的兩顆自攻螺釘（十字螺絲刀 PH2）將兩條支腿固定到位。包裝中還包含一個接地線聯結器和一個 5 度角介面卡，便於向上或向下傾斜調節。

## 開啟外殼蓋 {#opening-the-case-cover}

可選 — 如需接觸 miniPCIe 插槽，需要開啟裝置頂蓋。作為開啟工具，可以使用大號一字螺絲刀或一枚小硬幣。開啟時務必格外小心，因為不正確地開啟卡扣可能會將其折斷！*本裝置的安裝和配置應由合格人員完成。* 請按以下步驟操作：

![](/img/82b7fa2a4a679f2f.webp)

抬起蓋子時的額外注意事項：不要用尖銳物體強行撬動。

## miniPCIe 插槽使用 {#minipcie-slot-usage}

本裝置配備一個 miniPCIe 插槽，並已安裝 LTE6 調變解調器。提供一個 SIM 插槽，用於與 miniPCIe 調變解調器配合使用。SIM 插槽不能單獨使用。更換 miniPCIe 模組應由合格人員完成，處理電氣裝置時請遵守安全注意事項：

- 在拆包和處理電子元件時使用腕部接地帶，以避免靜電放電（ESD）損壞；
- 按前面說明所示開啟上蓋；

![](/img/3ce4a8956b2c2a41.webp)

- 天線位於 PCB 下方；
- 找到 PCB 上的 miniPCIe 插槽，並卸下兩顆出廠時安裝的螺釘；
- 將隨附的厚導熱墊貼到卡上，然後將卡安裝到 miniPCIe 插槽中，使導熱墊位於 PCB 與卡之間；
- 插入您需要的卡；
- 用之前卸下的兩顆螺釘將卡固定到位；
- 將灰色 uFL 聯結器連線到調變解調器的 MAIN 天線聯結器，將黑色線纜連線到輔助（或 AUX）聯結器；
- 在卡的頂部貼上一塊較薄的導熱墊；
- 重新組裝。組裝完成後，將移動運營商的 SIM 卡滑入 SIM 插槽，晶片朝上，如埠標籤所示。該插槽支援 MicroSIM（3FF）。

## 供電 {#powering}

本裝置可由 12-57 V 的 802.3af/at 電源以及無源 PoE 注入器供電（隨附一個電源和一個 PoE 注入器）。最大功耗 6 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠；
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 安裝 {#mounting}

![](/img/819eccc51163cf32.webp)

- 將隨附的金屬安裝環滑入天線反射盤背面的兩個槽中。
- 將裝置固定到立杆上，乙太網埠朝下。
- 使用 PH2 螺絲刀擰緊安裝環。
- 使用紮帶將乙太網線固定在立杆上，距裝置不超過一米，以免線纜被拉出埠。
- 檢查安裝角度和位置。
- 可選：如有需要，在安裝裝置之前，可將隨附的 5 度調節介面卡插入安裝環所在的頂部或底部槽中。當裝置緊固到垂直立杆上時，這會產生額外的向上或向下角度。
- 將 5 度角介面卡插入其中一個槽中，然後重新安裝裝置。在戶外安裝時，請確保所有線纜開口朝下。使用 POE 注入器和正確的接地，本裝置在埠蓋下方設有專門設計的接地聯結器。建議使用遮蔽 Cat5/6 線纜。本裝置的 IP 防護等級為 IP54。*警告！本裝置的安裝和執行應與您的身體保持至少 120 釐米的距離。在居住環境中執行本裝置可能會造成無線電干擾。*

## 配置 {#configuration}

登入後，您應在 QuickSet 選單中選擇 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將使用的國家，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能的功能：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。

## 配件 {#accessories}

包裝包含以下隨裝置提供的配件和零件：

- ADAPT1_ EU/US 開關電源 24V, 0.8A；
- CLAMP1,2_ SUS304 軟管卡箍（philips 型；9mm；夾緊直徑範圍 25-70mm），帶 EPE 袋；
- POE1_ 千兆 POE 注入器；
- K-SET_K_Set 用於 LHGGR&R11e-LTE6；
- CASE1_ LHG-LTE-RHLEG-R0；
- CASE2_ LHG-LTE-LHLEG-R0；
- CASE10_ LHG-5G-390mm 碟形天線 3,0x2.5x0,5mm；
- 已組裝的 LHGGR 主支腿。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/67b78179c3a03815.webp)

- 一個千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。連線其他網路裝置時可以使用直通線或交叉線。該乙太網埠可接受來自無源 PoE 注入器的 9-30 V DC 供電。
- 帶 LTE6 調變解調器的 MiniPCIe 插槽。
- SIM 插槽（不能單獨使用）。

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）；
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在會搜尋 CAPsMAN 伺服器（共 10 秒）；
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 搜尋 Netinstall 伺服器（共 15 秒）；無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 模式按鈕 {#mode-button}

模式按鈕的動作可以透過 RouterOS 軟體進行配置，以執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。模式按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置妥善運送到指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>包含 FCC ID</th></tr></thead><tbody><tr><td>RBLHGGR&R11e-LTE6</td><td>TV7R11ELTE6</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝提供合理的有害干擾保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在居住區域執行本裝置很可能會造成有害干擾，此時使用者需要自行承擔費用來糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。

注意：本機在測試時外圍裝置使用了遮蔽線纜。為確保合規，必須使用遮蔽線纜與本機配合。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>包含 IC</th></tr></thead><tbody><tr><td>RBLHGGR&R11e-LTE6</td><td>7442A-R11ELTE6</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期資訊以斜槓分隔的形式標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## Norma Oficial Mexicana {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）批准的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBLHGGR&R11e-LTE6 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### GSM / WCDMA / LTE {#gsm--wcdma--lte}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>E-GSM-900</th><th>900 MHz / 33dBm</th></tr></thead><tbody><tr><td>DCS-1800</td><td>1800 MHz / 30dBm</td><td></td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 24dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 24dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1700 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dBm ± 2.7 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。有關更多詳細資訊，請參閱上文的符合性宣告。

![](/img/0561b3ba8c95a35c.webp)

當在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限於室內使用。
