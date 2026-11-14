---
title: "LHG R"
slug: /lhg-r
source: https://manual.mikrotik.com/hardware/lhg-r
captured_at: '2026-11-04T09:54:23+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## [LHG R](https://mikrotik.com/product/rblhgr) (RBLHGR) {#lhg-r-rblhgr}

![](/img/7c2295886e9fa394.webp)

LHG R 不帶工廠安裝的調變解調器，您可以選擇自己的解決方案。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 將接入點安裝到任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本產品 intended to be mounted outdoors on a pole. 開始安裝前請仔細閱讀安裝說明。未能使用正確的硬體和配置，或未遵循正確程式，可能對人員造成危險情況並損壞系統。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和配件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境設定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，應與您的身體、職業使用者或公眾保持不少於 120 釐米的距離。

## 快速開始 {#quickstart}

- 握住裝置的中央立柱，同時用力按壓使卡扣保持閉合的卡舌，直到卡扣彈開。
- 將 SIM 卡插入卡槽，晶片朝上。
- 安裝您所需的調變解調器。
- 將支腳安裝到裝置底部以組裝外殼，參見外殼組裝段落。
- 將裝置安裝到您所需的位置，參見“安裝”段落。
- 將乙太網線連線到乙太網埠，將乙太網線的另一端連線到隨附的 PoE 注入器。
- 將 PoE 注入器插入您的 PC。
- 將隨附的電源插入 PoE 注入器以啟動裝置。參見“供電”段落。
- 將 LAN 計算機的 IP 配置設定為*自動*（DHCP）。
- 在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 以開始配置。
- 使用者名稱：a*dmin*，預設無密碼，您將自動登入到 Quick Set 螢幕（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。
- 透過選擇右側的“Check for updates”按鈕並更新您的 RouterOS 軟體到最新版本，以更新裝置，確保最佳效能和穩定性。必須插入有效的 SIM 卡。
- 要手動更新裝置，請訪問 [https://mikrotik.com/download](https://mikrotik.com/download)
- 為此裝置選擇 MIPSBE 軟體包並下載到您的 PC。
- 將下載的軟體包上傳到 WebFig 的“Files”選單並重啟裝置。將 RouterOS 軟體更新到最新版本可確保最佳效能、穩定性和安全更新。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個 10/100 乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。可使用直通或交叉線纜連線其他網路裝置。該乙太網埠接受來自無源 PoE 注入器的 9-30 V DC 供電。
- MiniPCIe 插槽和 SIM 插槽（不能單獨使用），用於 3G/4G/LTE 調變解調器。

## 供電 {#powering}

該裝置可由 12-57 V 802.3af/at 電源和無源 PoE 注入器供電（隨附一個電源和 PoE 注入器）。最大功耗 6 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網線連線到 POE 介面卡的 POE 埠。
- 將來自 LAN 的乙太網線連線到 POE 介面卡的 LAN 埠，注意資料和電源流向箭頭。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 開啟外殼蓋 {#opening-the-case-cover}

要訪問 MiniPCIe 插槽，需要開啟裝置的頂蓋。作為開啟工具，您可以使用大號一字螺絲刀或小硬幣。開啟時務必極其小心，因為不正確地開啟卡扣可能會將其折斷！*本裝置的安裝和配置應由合格人員完成。* 請按照以下步驟操作：

![](/img/82b7fa2a4a679f2f.webp)

額外注意：掀起蓋子時，不要用尖銳物體強行撬開。

## miniPCIe 插槽使用 {#minipcie-slot-usage}

該裝置配備一個 miniPCIe 插槽，用於 3G/4G/LTE 調變解調器。提供一個 SIM 插槽，與 miniPCIe 調變解調器一起使用。SIM 插槽不能單獨使用。在這種情況下，內部天線未連線（位於外殼內部）。安裝 miniPCIe 模組應由合格人員完成，處理電氣裝置時請遵循安全預防措施：

- 拆包和處理電氣元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞。
- 按照前面的說明開啟上蓋。
- 天線位於 PCB 下方。
- 找到 PCB 上的 miniPCIe 插槽，並拆下兩個出廠安裝的螺絲。
- 將隨附的厚導熱墊貼到卡上，然後將卡安裝到 miniPCIe 插槽中，使導熱墊位於 PCB 和卡之間。

![](/img/3ce4a8956b2c2a41.webp)

- 插入您所需的卡。
- 使用之前拆下的兩個螺絲將卡固定到位。
- 將黑色 uFL 聯結器連線到調變解調器的 MAIN 天線聯結器，將灰色線纜連線到 DIV 聯結器。
- 將較薄的導熱墊貼到卡的頂部。
- 按相反順序重新組裝。重新組裝後，將移動運營商的 SIM 卡滑入 SIM 插槽，晶片朝上，如埠標籤所示。該插槽接受 MicroSIM（3FF）。

## 組裝 {#assembly}

- 將兩個支腳滑入各自一側，以安裝到 LHG 外殼上，支腳有所不同且不能互換（檢視產品時，使乙太網埠蓋位於您前方，標有 R 的支腳用於右側，標有 L 的支腳用於左側）。
- 將組裝好的 LHG 裝置卡入網格的適當中央位置。
- 使用隨附的兩個自攻螺絲（PH2 十字螺絲刀）將兩個支腳固定到位。包裝中還包含一個接地線聯結器和一個 5 度角介面卡，便於向上或向下傾斜調整。

## 安裝 {#mounting}

![](/img/819eccc51163cf32.webp)

- 將隨附的金屬安裝環滑入天線碟背面的兩個槽中。
- 將裝置安裝到立杆上，使乙太網埠朝下。
- 使用 PH2 螺絲刀擰緊安裝環。
- 使用紮帶將乙太網線固定到立杆上，距離裝置小於一米，以避免線纜從埠被拉出。
- 檢查安裝角度和位置。
- 可選：如有需要，在安裝裝置之前，您可以將隨附的 5 度調整介面卡插入安裝環所插入的頂部或底部槽中。當裝置緊固到垂直立杆上時，這將產生額外的向上或向下角度。
- 將 5 度角介面卡插入其中一個槽並重新安裝裝置。戶外安裝時，確保所有線纜開口朝下。使用 POE 注入器和正確接地，本裝置在埠蓋下方有專門設計的接地聯結器。建議使用遮蔽 Cat5/6 線纜。本裝置的 IP 防護等級為 IP54。

## 配置 {#configuration}

登入後，您應選擇 QuickSet 選單中的“Check for updates”按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將使用的國家/地區，以符合當地法規。RouterOS 除本文件所述內容外，還包含許多配置選項。我們建議從這裡開始瞭解各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路啟動裝置，參見相關章節。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 當綠色 LED 開始閃爍時鬆開按鈕，以將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，以清除所有配置和預設值。
- 當 LED 不再點亮（約 20 秒）後鬆開按鈕，使裝置尋找 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。無論使用上述哪種選項，如果在給裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。該裝置在乙太網埠門後包含一個接地連線，您應將其連線到裝置使用地點所在塔架或建築的接地裝置。這可以大幅降低 ESD 和雷擊損壞的風險。

## 模式按鈕 {#mode-button}

可以從 RouterOS 軟體配置模式按鈕的操作，以執行使用者提供的任意 RouterOS 指令碼。您也可以停用此按鈕。模式按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## 規格 {#specifications}

有關本產品、規格和圖片的更多資訊，請訪問我們的網頁：[https://mikrotik.com/product/rblhgr](https://mikrotik.com/product/rblhgr)

## 配件 {#accessories}

![](/img/a62040f544ef34ab.webp)

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

![](/img/8d294e5cd375c591.webp)

![](/img/25f50553ffd86eaf.webp)

![](/img/b0984aa3ad3c6d58.webp)

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

為避免環境汙染，請將裝置與生活垃圾分開，並以安全方式處置，例如在指定的廢物處置場所處置。請熟悉您所在地區將裝置正確運輸到指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝中的有害干擾提供合理保護。

本裝置產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域操作本裝置可能會造成有害干擾，在這種情況下，使用者需要自行承擔費用來糾正干擾

**FCC 警告：** 未經合規負責方明確批准的任何更改或修改，都可能導致使用者失去操作本裝置的權利。本裝置符合 FCC 規則第 15 部分。操作受以下兩個條件約束：(1) 本裝置不得造成有害干擾，以及 (2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或聯合操作。注意：本單元在外圍裝置上使用遮蔽線纜進行了測試。為確保合規，必須在本單元上使用遮蔽線纜。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。操作受以下兩個條件約束：

-

本裝置不得造成干擾；

-

本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。本裝置包含的免許可發射器/接收器符合加拿大創新、科學和經濟發展部適用於免許可無線電裝置的免許可 RSS。操作須滿足以下兩個條件：

-

本裝置不得產生干擾；

-

本裝置必須接受任何無線電干擾，即使該干擾可能影響其正常操作。此 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境設定的輻射暴露限值。本裝置安裝和操作時，輻射體與您身體任何部位之間的最小距離應為 120 釐米。本裝置符合 IC 針對非受控環境定義的輻射暴露限值。本裝置安裝和使用時，輻射體與您身體任何部位之間的最小距離應為 120 釐米。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置製造日期資訊位於其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後續兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBLHGR 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WCDMA / LTE / 5G {#wcdma--lte--5g}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>E-GSM-900</th><th>900 MHz / 33 dBm</th></tr></thead><tbody><tr><td>DCS-1800</td><td>1800 MHz / 30 dBm</td><td></td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dBm ± 2.7 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。有關更詳細的資訊，請參閱上方的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 規定中的 WLAN 和 LTE 最大發射功率限值。更多資訊請參閱上方的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大傳輸功率限值。有關更多資訊，請參閱上方的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。有關更多資訊，請參閱上方的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。有關更多資訊，請參閱上方的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 規則規定的 WLAN 和 LTE 最大發射功率限值。有關更多資訊，請參閱上方的符合性宣告。
