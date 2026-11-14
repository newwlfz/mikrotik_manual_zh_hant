---
title: "ATLGM&EG18-EA"
slug: /atlgm-and-eg18-ea
source: https://manual.mikrotik.com/hardware/atlgm-and-eg18-ea
captured_at: '2026-11-04T09:40:32+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/f01d893fcf663533.jpg)

## [ATL LTE18 kit](https://mikrotik.com/product/atl18) (ATLGM&EG18-EA) {#atl-lte18-kit-atlgmeg18-ea}

先進技術水平（ATL）LTE 解決方案，配備寬範圍 MIMO 4x4 天線，可在農村和城市地區實現快速穩定的連線。充分利用您的移動覆蓋範圍！有關完整規格和宣傳冊，請參閱 [ATL LTE18 kit 產品頁面](https://mikrotik.com/product/atl18)。

## 安全警告 {#safety-warnings}

- 在操作任何裝置之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 將接入點安裝在任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本產品擬安裝在戶外立杆上。開始安裝前，請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確程式，可能會對人員造成危險並損壞系統。
- 請僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座中拔下電源插頭。
- 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能會造成無線電干擾，在這種情況下，使用者可能需要採取適當措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置應距離您的身體、職業使用者或公眾不少於 20 釐米。

## 快速開始 {#quickstart}

- 開啟乙太網埠蓋板；
- 將 SIM 卡插入卡槽，晶片朝上；
- 使用乙太網線將裝置連線到隨附 PoE 注入器的 data+power 端；
- 將 PoE 注入器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 使用 **WebFig** 或 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）透過 Web 瀏覽器配置裝置。開啟 [https://192.168.188.1](https://192.168.188.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，轉到 **Neighbors** 標籤頁，然後選擇 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如果行動網路運營商要求，請輸入 PIN 碼；
- 選擇 "Check for updates" 按鈕，並將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡並具有活動的 Internet 連線；
- 要手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 找到您的產品。所需軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 裝置將重啟；
- 再次連線，並在 **QuickSet** 選單中設定強密碼。

![](/img/4297e175c7b298d3.webp)

## 供電 {#powering}

- DC 輸入數量 1
- DC 輸入型別 PoE-in (12-57)
- 電源介面卡標稱電壓 24 V
- 電源介面卡標稱電流 0.8 A
- 無附件時的最大功耗 8 W
- 最大功耗 8 W

## 安裝 {#mounting}

- 將隨附的金屬安裝環滑入天線碟背面的兩個槽中。
- 將裝置固定到立杆上，使乙太網埠朝下。
- 使用 PH2 螺絲刀擰緊安裝環。
- 使用紮帶將乙太網線固定到立杆上，距裝置小於一米，以避免線纜從埠中被拉出。
- 檢查安裝角度和位置。在戶外安裝時，確保所有線纜開口朝下。使用 POE 注入器和正確接地，本裝置在埠蓋下方有專門設計的接地聯結器。建議使用遮蔽 Cat5/6 電纜。本裝置的 IP 防護等級為 IP54。

## 配置 {#configuration}

登入後，您應在 QuickSet 選單中選擇 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以啟動裝置進行重新安裝，請參閱相應章節。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的配件：

![](/img/f302bf1cf0939e79.webp)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼 ATLGM&EG18-EA
- CPU 雙核 88F3720 1.2 GHz
- CPU 架構 ARM 64bit
- RAM 大小 256 MB
- RAM 型別 DDR3L
- 儲存 16 MB，Flash
- 1G 乙太網埠數量 1
- LTE 調變解調器 R11mL-EG18-EA
- TAC 86981604
- LTE 類別 18（下行 1.2Gbps，上行 150Mbps）
- LTE 頻段 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 7 (2600MHz) / 8 (900 MHz) / 20 (800MHz) / 28 (700MHz) / 38 (2600MHz) / 40 (2300MHz) / 41 (2500MHz)
- 3G 類別 R8（下行 42.2Mbps，上行 11.2Mbps）
- 3G 頻段 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 8 (900MHz)
- 尺寸 直徑 315 mm x 深度 170 mm
- 作業系統 RouterOS，許可證級別 3
- 工作溫度 -40°C 至 +70°C

## SIM 卡槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議與介面卡一起使用。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（總計 5 秒）；
- 繼續按住 5 秒，LED 常亮，此時鬆開即可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（總計 10 秒）；
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總計 15 秒）；無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請熟悉將裝置正確運輸到您所在地區指定處置場所的程式。

### CE 符合性宣告 {#ce-declaration-of-conformity}

<table><thead><tr><th>*BG*</th><th>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</th></tr></thead><tbody><tr><td>CS</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DA</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DE</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EL</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EN</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ES</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ET</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FI</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FR</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HR</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HU</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IT</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IS</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LT</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LV</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>MT</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NL</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NO</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PL</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PT</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>RO</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SK</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SL</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SV</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 ATLGM&EG18-EA 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr></tbody></table>

### WLAN/LTE {#wlanlte}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>WCDMA Band I</th><th>2100 MHz / 24dBm ± 2.7 dB</th></tr></thead><tbody><tr><td>WCDMA Band III</td><td>1800 MHz / 24dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band V</td><td>850 MHz / 24dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>900 MHz / 24dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1700 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 5</td><td>850 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 28</td><td>700 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dBm ± 2.7 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大 TX 功率限值。有關更多詳細資訊，請參閱上文的符合性宣告。

<table><thead><tr><th>**(EN) 技術規格 / (DE) 技術規格 / (FR) 技術規格 / (IT) 技術規格 / (ES) 技術規格 / (RU) 技術規格：**</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>(EN) 產品電源輸入選項(DE) 產品電源輸入選項(FR) 產品電源輸入選項(IT) 產品電源輸入選項(ES) 產品電源輸入選項(RU) 產品輸入功率引數</td><td>(EN) DC 介面卡輸出規格(DE) 直流介面卡輸出規格(FR) 直流介面卡輸出規格(IT) 直流介面卡輸出規格(ES) 直流介面卡輸出規格(RU) 直流介面卡輸出特性</td><td>(EN) 外殼 IP 等級(DE) 外殼 IP 等級(FR) 機殼 IP 等級(IT) 外殼 IP 等級(ES) 外殼 IP 等級(RU) 外殼 IP 防護等級</td><td>(EN) 工作溫度(DE) 工作溫度(FR) 工作溫度(IT) 工作溫度(ES) 工作溫度(RU) 工作溫度</td><td></td></tr><tr><td>電壓，V</td><td>電流，A</td><td></td><td></td><td></td></tr><tr><td>PoE 輸入乙太網埠 (12 - 57 V DC)</td><td>24</td><td>0.8</td><td>IP54</td><td>-33°..+70°C</td></tr></tbody></table>
