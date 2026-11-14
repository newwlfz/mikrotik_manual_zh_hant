---
title: "LHG LTE18 套件"
slug: /lhg-lte18-kit
source: https://manual.mikrotik.com/hardware/lhg-lte18-kit
captured_at: '2026-11-04T09:54:04+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/65fdb883a6f0b498.jpg)

## [LHG LTE18 套件](https://mikrotik.com/product/lhg_lte18)（LHGGM&EG18-EA） {#lhg-lte18-kit-lhggmeg18-ea}

超遠距離，更快速度——藉助超高速 LTE Category 18 調變解調器的強大效能。速度最高可達 1 Gbps！這是面向最偏遠地區的最後一公里網際網路解決方案。完整規格和宣傳冊請參閱 [LHG LTE18 kit 產品頁面](https://mikrotik.com/product/lhg_lte18)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 將接入點安裝在任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於安裝在室外的立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 僅使用製造商認可的電源和附件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證由於裝置的不當使用而不會發生事故或損壞。請謹慎使用本產品，並自行承擔風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。
- 本裝置為 A 類裝置。在住宅環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 56.5 釐米。

## 快速開始 {#quickstart}

- 握住裝置的中心立柱，向卡扣施加力，直到卡扣彈開。
- 將 SIM 卡插入卡槽，晶片朝上。
- 將支腳安裝到裝置底部以組裝外殼，參見（連結）段落。
- 將裝置安裝到所需位置，參見（連結）段落。
- 將 LAN 計算機的 IP 配置設定為*自動*（DHCP）。
- 在網頁瀏覽器中開啟 [https://192.168.188.1](https://192.168.188.1) 開始配置。
- 使用者名稱：admin，密碼見標籤（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）。
- 透過點選右側的 "Check for updates" 按鈕並更新您的 RouterOS 軟體至最新版本以更新裝置，從而確保最佳效能和穩定性。必須插入有效的 SIM 卡。
- 要手動更新裝置，請訪問 [https://mikrotik.com/download](https://mikrotik.com/download)
- 為此裝置選擇 ARM64 軟體包並下載到您的 PC。
- 將下載的軟體包上傳到 WebFig 的 "Files" 選單並重啟裝置。
- 將 RouterOS 軟體更新至最新版本可確保最佳效能、穩定性和安全更新。
- 在右側底部的 "Password" 欄位中設定路由器密碼，並在 "Confirm Password" 欄位中重複輸入，下次登入時將使用該密碼。
- 選擇 "Apply Configuration" 儲存更改。

![](/img/0f854fe8f1239bea.webp)

## 外殼組裝 {#case-assembly}

- 將兩個支腳分別滑入 LHG 外殼的相應兩側，兩個支腳不同且不可互換（觀察產品時，使乙太網埠蓋板朝向您，標記為 R 的支腳用於右側，標記為 L 的支腳用於左側）。
- 將組裝好的 LHG 裝置卡入網格中合適的中央位置。
- 使用隨附的兩顆自攻螺絲（十字螺絲刀 PH2）將兩個支腳固定到位。包裝中還包含接地線聯結器和 5 度角度介面卡，便於向上或向下調整傾斜角度。參見段落。

## 供電 {#powering}

裝置可透過以下方式供電：

PoE in 802.3af/at 支援的輸入電壓 12-57 V 電源介面卡標稱電壓 24 V 電源介面卡標稱電流 0.8 A 最大功耗 8 W

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠；
- 使用標有 DATA 的介面卡乙太網線將 PoE 介面卡連線到 PC 或其他網路裝置；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

![](/img/18a01bb861c1bf89.webp)

## 安裝 {#mounting}

![](/img/819eccc51163cf32.webp)

- 將隨附的金屬安裝環滑入天線碟背面的兩個槽中。
- 將裝置安裝到立杆上，使乙太網埠朝下。
- 使用 PH2 螺絲刀擰緊安裝環。
- 使用紮帶將乙太網線固定在立杆上，距裝置不超過一米，以免線纜被拉出埠。
- 檢查安裝角度和位置。
- 可選：如有需要，在安裝裝置之前，可將隨附的 5 度調節介面卡插入安裝環所在的頂部或底部槽中。這樣在將裝置擰緊到垂直立杆上時，就會額外形成向上或向下的角度。
- 將 5 度角度介面卡插入其中一個槽並重新安裝裝置。在戶外安裝時，請確保所有線纜開口朝下。請使用 POE 注入器和正確的接地，本裝置在埠蓋下方設有專門設計的接地聯結器。建議使用遮蔽 Cat5/6 線纜。本裝置的 IP 防護等級為 IP54。*警告！本裝置的安裝和操作位置與身體之間應保持至少 120 cm 的距離。在住宅環境中操作本裝置可能會造成無線電干擾。*

## 配置 {#configuration}

登入後，您應在 QuickSet 選單中選擇 "Check for updates" 按鈕，因為將 RouterOS 軟體更新至最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將使用的國家/地區，以符合當地法規。RouterOS 除本文件所述內容外還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果沒有可用的 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。為便於恢復，可以讓裝置引導以進行重新安裝，參見某章節。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

![](/img/2a7e7a38b3223b81.webp)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼 LHGGM&EG18-EA
- CPU 88F3720 800 MHz
- CPU 架構 ARM 64bit
- RAM 容量 256 MB
- 儲存 16 MB flash
- 1G 乙太網埠數量 1
- LTE 調變解調器 R11mL-EG18-EA
- TAC 86981604
- LTE 類別 18（下行 1.2Gbps，上行 150Mbps）
- LTE FDD 頻段 1 (2100MHz) / 3 (1800MHz) / 7 (2600MHz) / 8 (900 MHz) / 20 (800MHz) / 28 (700MHz) / 38 (2600MHz) / 40 (2300MHz)
- 3G 類別 R8（下行 42.2Mbps，上行 11.2Mbps）
- 3G 頻段 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 8 (900MHz)
- Micro SIM 插槽 1
- 尺寸 391 x 391 x 227 mm
- 作業系統 RouterOS v7，許可證級別 3
- 工作溫度 -40°C 至 +70°C

## SIM 插槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議配合介面卡使用。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）；
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置將開始尋找 CAPsMAN 伺服器（共 10 秒）；
- 或者繼續按住按鈕 5 秒直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）；無論使用上述哪種方式，如果在裝置通電前按住按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統未經測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送往指定的廢物處置場所。請熟悉您所在地區將裝置正確運送到指定處置場所的程式。

### UKCA 標誌 {#ukca-marking}

![](/img/387853c20d5a4c82.gif)

### 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

### 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

### 烏克蘭國家通訊與資訊化國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭境內使用須按照 NKРЗІ 2012 年 11 月 1 日第 559 號決議批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的決定所規定的程式取得使用許可。

### CE 符合性宣告 {#ce-declaration-of-conformity}

Mikrotīkls SIA 特此宣告，無線電裝置型別 LHGGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>WCDMA Band I</th><th>2100 MHz / 24dBm ± 2.7 dB</th></tr></thead><tbody><tr><td>WCDMA Band III</td><td>1800 MHz / 24dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>900 MHz / 24dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1700 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 28</td><td>700 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dBm ± 2.7 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。有關更詳細的資訊，請參閱上文的符合性宣告。本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。有關更多資訊，請參閱上文的符合性宣告。有關更多資訊，請參閱上文的符合性宣告。本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。有關更詳細的資訊，請參閱上文的符合性宣告。本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。有關更詳細的資訊，請參閱上文的符合性宣告。本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。有關更詳細的資訊，請參閱上文的符合性宣告。本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。有關更詳細的資訊，請參閱上文的符合性宣告。
