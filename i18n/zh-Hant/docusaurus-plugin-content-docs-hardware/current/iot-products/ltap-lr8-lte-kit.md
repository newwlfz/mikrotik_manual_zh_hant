---
title: "LtAP LR8 LTE 套件"
slug: /ltap-lr8-lte-kit
source: https://manual.mikrotik.com/hardware/ltap-lr8-lte-kit
captured_at: '2026-11-04T09:55:47+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/ltap-lr8-lte-kit-eeb73bd200953b5a8ca3fc070627ae4b.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/30e4f8523c74a8b6.jpg)

### [LtAP LR8 LTE kit](https://mikrotik.com/product/ltap_lr8_lte_kit) (RBLtAP-2HnD&R11e-LTE&LR8) {#ltap-lr8-lte-kit-rbltap-2hndr11e-ltelr8}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 在任何牆面上安裝接入點的所有安裝方法均須獲得當地主管部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於在室外抱杆安裝，但也可以安裝在室內。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體和配置或未遵循正確的步驟，可能會對人員造成危險情況並損壞系統。
- 請僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 這是 A 類裝置。在居住環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 30 釐米。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 開啟底部蓋板；
- 將 SIM 卡插入 SIM 2 插槽（中間）；
- 將裝置連線到電源；
- 用您的電腦連線到 MikroTik 無線網路；
- 在網頁瀏覽器中開啟 https://192.168.88.1 以開始配置；
- 使用者名稱：**admin**，預設未設定密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 連線後，在 QuickSet LTE AP 選單中輸入您的 PIN 碼 [https://mt.lv/configuration](https://mt.lv/configuration)；
- 將 RouterOS 軟體升級到最新版本 [https://mt.lv/upgrade](https://mt.lv/upgrade)；
- 再次連線，並在 *QuickSet LTE AP* 選單中設定您的無線網路密碼；
- 在螢幕左側選擇您所在的國家，以應用國家法規設定；
- 保護您的裝置並設定強密碼。
- 在產品標籤上找到您的 *LR Gateway ID*，並將其註冊到您的網路伺服器中。
- *本產品的核心功能需要以下 RouterOS "npk" 軟體包：gps、lora、system。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/7b3321c1cbf665d8.webp)

- 內建 2 GHz 無線接入點模組，支援 AP/station/bridge/p2p 模式。板載 PIF 內建天線，以及用於外接天線的 MMCX 聯結器（可透過軟體選擇）。
- 兩個 miniPCIe 插槽和三個 SIM 插槽。
- 內建 GPS 模組，配有外部 SMA 聯結器。
- 千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。直通線或交叉線均可用於連線其他網路裝置。乙太網埠接受來自無源 PoE 注入器的 12-30 V DC 供電。
- 一個 DB9 RS232 序列埠，用於序列埠控制檯訪問。配置為 115200 bit/s、8 個數據位、1 個停止位、無校驗。
- 一個 USB 2.0 埠。
- R11e-LR8，帶外部 SMA 聯結器的 miniPCIe 卡。

## 安裝 {#mounting}

- 可以使用隨附的四顆螺釘和機身上的四個預留孔將裝置固定到牆上。
- 埠由一個小門保護，該門用兩顆螺釘固定。取下後可訪問乙太網埠、天線聯結器、SIM 插槽等。
- 該門為所有可用埠預留了開口位置，因此您可以引導所有必要的線纜穿過，但請只打開您將要使用的開口。
- 機殼上提供了多處用於外接天線的位置，請使用合適尺寸的鑽頭將其開啟。請小心並測量所選天線，以確保安裝後不會觸碰內部 PCB 板。

![](/img/dc0a3d4ff60b80cb.webp)

該裝置可在室內和室外使用。防護等級為 IP54。

如果您打算在室外安裝，請確保任何線纜開口都朝下。安裝方向由裝置上的向上箭頭指示。請使用 POE 注入器並正確接地。建議使用 Cat6 遮蔽線纜。警告！本裝置的安裝和操作應保持裝置與您的身體之間至少 30 釐米的距離。在居住環境中操作本裝置可能會造成無線電干擾。裝置外殼上設有可鑽孔的位置，用於安裝外部 LTE 和 GPS 天線。請使用鑽頭鑽出適合所用天線線纜的孔。

## 配置 {#configuration}

我們建議點選 "Check for updates" 按鈕並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法進行 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下，來自網際網路埠的所有訪問都被阻止）。出於恢復目的，可以從網路引導裝置，請參閱（連結）部分。

## GPS {#gps}

內建 GPS 模組需要使用外部天線（SMA 聯結器已安裝在裝置艙門後方）。有關如何取下艙門，請參閱（連結）部分。**注意** GPS 使用有源天線，請僅在裝置關機時連線和斷開天線！

**支援 - GPS、GLONASS、BeiDou、Galileo）。** 請確保您的裝置上已安裝 GPS 軟體包。可透過以下命令檢查 /system package print。如果未安裝，請根據您的 RouterOS 版本從我們的下載頁面下載額外軟體包，並將 GPS 軟體包拖到 Files 選單中進行安裝。啟用 GPS 並開始工作：

- 啟用 - /system gps set enable=yes;
- 將天線設定為外部 - /system gps set gps-antenna-select=external;
- 檢查配置 - /system gps print。有關更多詳細資訊，請參閱 [GPS 手冊](/docs/mobile-networking/gps)。

## LR 使用 {#lr-usage}

有關介面配置，請訪問 [LoRa 手冊](/docs/internet-of-things/lora)。

我們建議使用我們的天線套件，[https://mikrotik.com/product/lora_antenna_kit](https://mikrotik.com/product/lora_antenna_kit)

## USB 使用 {#usb-usage}

使用 LR 卡時，USB 埠的電源將由 CPU 關閉。因此它不能與 LR 卡一起使用。

## 汽車聯結器使用 {#automotive-connector-usage}

![](/img/b82bafca5c454664.webp)

## 供電 {#powering}

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，正極針式插頭）接受 12-30 V DC ⎓，隨附 24 V、1.2 A 介面卡。
- 乙太網埠接受無源 PoE 12-30 V DC ⎓（需補償線纜上的損耗，因此建議高於 12 V）。
- 汽車聯結器可用於從汽車和公交車上的常規 12/24 V ⎓ 連線為裝置供電。該插頭有四個引腳：左下方（黑色）為接地，右下方為電源輸入（紅色）。上方兩個（AUX）保留供將來使用。無附加裝置時，最大負載下的功耗可達 12 W。請將接地（地線）線連線到艙門下方的螺釘上。

### 連線到 PoE 介面卡：（不包含） {#connecting-to-a-poe-adapter-not-included}

- 將裝置上的乙太網線連線到 POE 介面卡的 POE out 埠。
- 將來自您 LAN 的乙太網線連線到 POE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 前面板狀態 LED 行為 {#front-status-led-behavior}

- 常亮藍色 – 裝置已通電。
- 常亮綠色 – 使用者自定義 LED，可在系統設定中配置。
- 常亮綠色 – GPS 模組狀態。
- 常亮綠色– 五個綠色 LED 組成的指示燈組，顯示蜂窩網路的訊號強度。

![](/img/1015646a55daf823.webp)

## miniPCIe 插槽 {#minipcie-slot}

### SIM 卡連線 {#sim-card-connectivity}

- MiniPCIe 1 **LR**（頂部插槽）支援 PCIe 和 USB 2.0 卡，但與 USB 2.0 type A 埠共用（USB 埠或 miniPCIe 插槽只能同時使用其中一個）。它只能用於 SIM 插槽 #1。
- MiniPCIe 2 **LTE**（底部插槽）僅支援 USB（2.0 和 3.0）miniPCIe 調變解調器（不支援 PCIe）。使用 SIM 插槽 #2 和 SIM 插槽 #3。預設使用 SIM 插槽 #2。SIM 卡可在 ROS 中切換。
- USB 2.0 type A 埠（僅在未使用 miniPCIe 1 時可用）。如果使用 LR，USB 將被關閉。
- 要在頂部 miniPCIe 插槽中使用 USB 型別的 miniPCIe 卡，請將 USB 連線切換到 miniPCIe 插槽：/system routerboard usb set type=mini-PCIe 這將停用裝置前面的 USB 2.0 埠。**將 SIM 卡插入頂部插槽時，SIM 卡晶片朝下。底部插槽 – 晶片朝上。**

**預設情況下，LR 卡連線至 SIM 插槽 #1，該插槽不能用於其他用途。**

請檢查您是否使用了正確的 SIM 插槽。對於插入底部 mini-pcie 插槽的調變解調器，您需要使用 SIM 插槽 2 或 SIM 插槽 3。並且需要在 RouterOS 中選擇所使用的 SIM 插槽。用於選擇 SIM 插槽的 CLI 命令：*/system routerboard modem set sim-slot=2*

### 調變解調器安裝 {#modem-installation}

此 LtAP 版本的調變解調器已安裝在底部插槽中。安裝額外的調變解調器時，請使用上方插槽。在這種情況下，內部天線連線到底部調變解調器。安裝 miniPCIe 模組應由合格人員完成，處理電氣裝置時請遵循安全預防措施：

- 拆包和處理電氣元件時請使用腕部接地帶，以避免靜電放電（ESD）損壞；
- 拆下機殼底部的六顆螺釘，然後取下機殼頂部。請注意天線線纜連線到底部調變解調器；
- 找到 miniPCIe 插槽並拆下兩顆出廠固定的螺釘；
- 在卡上貼上隨附的厚導熱墊，然後將卡安裝到 miniPCIe 插槽中，使導熱墊位於 PCB 和卡之間；
- 使用之前拆下的兩顆螺釘將卡固定到位；
- 將天線線纜穿過 GPS 聯結器附近的開口，並連線到您的調變解調器。建議使用矽橡膠固定聯結器。
- 在卡的上方貼上較薄的導熱墊；
- 使用外部天線時，可將聯結器安裝在機殼側面，使用 6.5 mm 鑽頭鑽孔，請參閱（連結）部分第 4 點；
- 有關如何放置橡膠密封圈以獲得最佳防水效果，請參閱下圖；
- 按相反順序重新組裝。PCB 螺釘的擰緊力矩為 0.3 Nm，機殼蓋/外殼螺釘的擰緊力矩為 0.5 Nm。

![](/img/03bc306812c7acce.webp)

在您將裝置重新裝回機殼並用之前拆下的螺釘固定後，請將移動運營商的 SIM 卡滑入 SIM 插槽，晶片朝向如埠標籤所示。該插槽接受 miniSIM（2FF）。SIM 插槽 2 和 3 適用於底部 miniPCIe 插槽，可在 RouterOS 的 "/system routerboard sim" 選單中切換。

## 復位按鈕 {#reset-button}

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的附件：

- K-67 緊固套件。包括四顆 4x25 mm 螺釘、四個 6x30 mm 膨脹螺栓。
- 直流 ⎓ 線纜（H4130-04PDB000R 3 mm 2x2P 外殼）至（StripJacket 5 cm+WireEnd Strip/Tin 1 cm）24 AWG（黑/紅/藍/橙）0.35 m。
- 歐盟/美國開關電源 24 V、1.2 A、28.8 W、86.8%、VI 級，DC ⎓ 線纜：220 cm RA DC 插頭 mod Hor CMC 短插頭。

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將已自動填入。
- 點選 Connect，透過無線網路建立與您裝置的連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置使用的頻段與上述規定不同，則需向終端使用者裝置應用來自制造商/供應商的定製韌體版本，並防止終端使用者重新配置。
- 室外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料手冊均可在製造商官方網站上獲取。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，TX 功率限制為 20dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，TX 功率限制為 23dBm（EIRP）。
- 序列號末尾帶有字母 "EG" 的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，TX 功率限制為 20dBm（EIRP）。

請確保裝置具有鎖定軟體包（來自制造商的韌體版本），需要將其應用到終端使用者裝置以防止終端使用者重新配置。該產品將標有國家程式碼 "-EG"。本裝置需要升級到最新版本，以確保符合當地主管部門的法規！終端使用者有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置妥善運輸至指定處置場所的程式。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>≤100 mW</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而有所不同。

有關裝置製造日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

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

## 烏克蘭國家通訊和資訊領域國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2480-2483.5 MHz（20 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用須按照 NKRZI 2012 年 11 月 1 日第 559 號決定批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 在此宣告，無線電裝置型別 RBLtAP-2HnD&R11e-LTE&LR8 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### GSM / WCDMA / LTE / WLAN / LR {#gsm--wcdma--lte--wlan--lr}

<table><thead><tr><th>E-GSM-900</th><th>工作頻率 / 最大輸出功率 Betriebsfrequenz / maximale Ausgangsleistung Fréquence de fonctionnement / puissance de sortie maximale Frequenza operativa / massima potenza di uscita Frecuencia de funcionamiento / potencia de salida máxima Рабочая частота / максимальная выходная мощность</th><th>900 MHz /33 dBm</th></tr></thead><tbody><tr><td>DCS-1800</td><td>1800 MHz / 300 dBm</td><td></td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 2.4 dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 2.4 dBm ± 2.7 dB</td><td></td></tr><tr><td>WLAN</td><td>2400-2483.5 MHz / 20 dBm</td><td></td></tr><tr><td>LTE BAND 1</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE BAND 3</td><td>1800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE BAND 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE BAND 8</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE BAND 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE BAND 38</td><td>3600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE BAND 40</td><td>2300 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LR (SRD)</td><td>863-870 MHz / 14 dBm</td><td></td></tr></tbody></table>

*客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 和 LTE 發射功率限值。有關更多詳細資訊，請參閱上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- und LTE-Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN et LTE conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN e LTE in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN y LTE de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN и LTE в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.
