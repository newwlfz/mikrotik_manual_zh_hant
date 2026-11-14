---
title: "wAP LR2 套件"
slug: /wap-lr2-kit
source: https://manual.mikrotik.com/hardware/wap-lr2-kit
captured_at: '2026-11-04T10:07:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/wap-lr2-kit-0ff0e8046d9b3541dfdd77380b8cc0f3.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/579445f9629a4c7e.jpg)

### [wAP LR2 kit](https://mikrotik.com/product/wap_lr2)（RBwAPR-2nD&R11e-LR2） {#wap-lr2-kit-rbwapr-2ndr11e-lr2}

wAP 是一款小型防風雨裝置，內建 LR2 卡。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律法規進行處理。
- 在任意牆面安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於戶外立杆安裝，但也可以安裝在室內。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險並導致系統損壞。
- 請僅使用製造商批准的電源和配件，它們可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置出現故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 這是 A 類裝置。在住宅環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

- 請確保您的 ISP 允許更換硬體，並且會自動分配 IP 地址。
- 開啟底部蓋板（參見 ""）。
- 將外接天線連線到 SMA 聯結器（參見 ""）。
- 將裝置連線到電源（參見 ""）。
- 使用您的裝置連線到 MikroTik 無線網路
- 配置必須透過無線網路使用網頁瀏覽器或移動應用完成 -（參見 ""）。或者，您可以使用 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。預設情況下，乙太網埠訪問被防火牆阻止。
- 連線到無線網路後，請在網頁瀏覽器中開啟 192.168.88.1 以開始配置。
- 使用者名稱：a*dmin*，預設沒有密碼（或者，對於某些型號，請在貼紙上檢視使用者名稱和無線密碼）。
- 使用移動應用時，請選擇 Quick setup，它會以六個簡單步驟引導您完成所有必要的配置。
- 在產品內的標籤上找到您的 LR Gateway ID，並將其註冊到您的網路伺服器中。
- 要使裝置連線到 LR 網路伺服器，請參見 ""。
- 點選 "Check for updates" 按鈕並將您的 RouterOS 軟體更新到最新版本，裝置需要有可用的網際網路連線。
- 更新後請設定您的國家/地區，以應用國家法規設定。
- 設定您的 WiFi 密碼。
- 設定路由器密碼。
- 產品的核心功能需要以下 RouterOS "npk" 軟體包：lora、system。

![](/img/8a33ad1fe4c43635.webp)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 10/100 乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。連線其他網路裝置時可以使用直通線或交叉線。
- 外部 SMA 天線聯結器已連線到 LR 卡。
- 汽車聯結器。引腳定義：A - 保留供將來使用（橙色），B - 保留供將來使用（藍色），C - 接地（黑色），D – 電源輸入（紅色）。
- MiniPCIe 插槽，內建 LR2 卡。
- 內建無線模組，工作於 2.4 GHz，802.11b/g/n 協定。
- Mini-SIM 插槽。

## 供電 {#powering}

裝置可透過以下方式供電：

- 乙太網埠支援被動 PoE 9-30 V DC ⎓。
- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）支援 9-30 V DC⎓。
- 汽車聯結器 9-30 V DC⎓。最大負載下的功耗可達 8 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的乙太網線纜連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 安裝 {#mounting}

裝置可以透過多種方式安裝：立杆、牆面、天花板，也可以放置在隨包裝附帶的專用 MikroTik 支架中。包裝中還包含帶詳細安裝說明的鑽孔模板，可幫助您完成乙太網線纜的安裝以及在天花板或牆面上的固定。鋼板支架用於放在吊頂天花板板的另一側，另有兩顆螺絲和牆塞。紮帶或鋼卡箍用於安裝在立杆上。

本裝置的 IP 防護等級為 IP54。在戶外安裝時，請確保所有線纜開口朝下。我們建議使用 POE 注入器和 Cat6 遮蔽線纜進行正確接地。使用和安裝本裝置時，請注意最大允許暴露（MPE）安全距離，輻射器與您的身體之間至少保持 20 釐米。

安裝在桅杆或立杆上：

建議使用電工膠帶以增加材料之間的摩擦力。

![](/img/b21639053eb61552.webp)

- 將塑膠紮帶穿過孔洞固定到鋼板支架上。
- 將支架安裝到裝置上。
- 用螺絲固定。
- 將裝置安裝到立杆或桅杆上並對齊。
- 將乙太網線纜穿過開口並連線到乙太網埠。
- 關閉底部卡扣並用螺絲固定。建議使用紮帶將乙太網線纜固定在立杆上，與裝置的距離約為 30 cm。

將裝置安裝在牆上：

![](/img/42ebcb18fdb0e686.webp)

- 使用隨附的模板標記鑽孔位置。如有需要，也標記乙太網線纜的位置。請相應地對齊，這取決於裝置最終將如何安裝。
- 如有需要，插入牆塞，這取決於牆體結構和材料。
- 將隨附的鋼板支架放在牆上。
- 用螺絲將其固定到位。
- 將您的乙太網線纜穿出開口並連線到乙太網埠。
- 將裝置安裝到鋼板支架上
- 用螺絲將其固定到位。
- 關閉底部卡扣。

避免將裝置安裝在低窪地面處，否則您將無法安裝和關閉底部卡扣。

安裝在天花板上：

![](/img/35cd19164cabfd89.webp)

包裝中包含一個專用支架，用於安裝在吊頂上。它由兩部分組成，分別安裝在天花板板的兩側。

-

使用模板標記鑽孔位置。

-

將兩個安裝支架放在標記處。

-

使用螺絲將它們固定在一起。

-

如果安裝在牆上，請以相同方式繼續組裝。

-

將您的乙太網線纜穿出開口並連線到乙太網埠。

-

將裝置安裝到鋼板支架上。

-

用螺絲將其固定到位。

-

關閉底部卡扣。

## 底部蓋板 {#bottom-lid}

- 底部蓋板由防脫落螺絲固定到位。

![](/img/0d1777eb306bd477.webp)

- 使用 Torx T20 螺絲刀將其擰鬆，但不要完全取下螺絲。

![](/img/fda7738b33a2c690.webp)

- 朝與裝置相反的方向拉動蓋板以將其取下。

![](/img/be3a042d3ac48e4c.webp)

- 重新裝配。

## 配置 {#configuration}

要設定 LR 的配置，請連線到裝置並使用網頁瀏覽器登入，或使用移動應用。只需兩個簡單步驟：**第一步：**

-

登入後，Quick Set 將被選中，請切換到螢幕右側的 WebFig。如果配置是透過移動應用完成的，請點選螢幕右側的齒輪圖示以開啟高階選單。

-

在左側選單中找到並選擇 "Lora" 部分。

-

在 newly opened window 中選擇 Servers 標籤頁。

-

點選 + 新增新的伺服器配置。

-

將出現一個新視窗，您需要輸入：Name:（伺服器名稱）Address:（伺服器地址）Up port:（通常為 1700）Down port:（通常為 1700）

-

點選 OK 儲存。**第二步：**

-

在上一個視窗中選擇 Device 標籤頁。

-

雙擊或點按該行進行配置。

-

在下拉選單中選擇先前輸入的網路。

-

點選 Enable 按鈕以啟用閘道器。

-

點選 OK 儲存。

-

配置完成。我們建議在 QuickSet 選單中點選 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都被阻止）。出於恢復目的，可以引導裝置進行重新安裝，請參見相關章節。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將已填寫。
- 點選 Connect 透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要設定。

## 天線使用 {#antenna-usage}

我們建議使用外接天線 "TOF-2400-8V-4"，可另行購買。該天線帶有立杆安裝件和可直接用於 LR 卡的線纜。[https://mikrotik.com/product/tof_2400_8v_4](https://mikrotik.com/product/tof_2400_8v_4) 位於底部艙門下方的 SMA 聯結器已連線到 LR 卡，隨時可用。請參閱有關如何取下艙門的章節。

**無需拆解裝置**。已安裝的 LR2 mini PCIe 卡有兩個可用聯結器 - uFL 和 MMCX。內建天線透過 uFL 聯結器連線，開箱即可使用。MMCX 聯結器已連線到 SMA，如果您希望使用外接天線，只需將其連線到 SMA 即可。裝置將根據稍後展示的設定選擇使用哪個天線。

**請在裝置關閉時連線和斷開天線！**

**內建天線** 4.7dBi 可用於節點與裝置之間距離不超過 200 米的部署（實際距離需在環境中進行核實）。該天線已連線並隨時可用。

要確認天線的連線方式：

- 開啟底部艙門（參見 ""）。

![](/img/8c722210ffb66bd7.webp)

- 使用 PH2 螺絲刀取下螺絲。
- 將上蓋與底部沿相反方向滑動，從而將其拆開。

![](/img/ce6936f2b0764db6.webp)

- 內建天線將使用 uFL 聯結器，而 SMA（用於外接天線）將按下圖所示透過 MMCX 聯結器連線。

![](/img/66c82c15bafd80f8.webp)

![](/img/ba146620d35704a2.webp)

- 重新裝配。**軟體負責選擇裝置所使用的天線。**

請確保在軟體設定中模組使用了正確的聯結器。

為此，請進入裝置的 GUI，檢視 **LoRa* → *Devices* → 在閘道器上"雙擊" → 在 "**Antenna**" 部分下使用的是哪個聯結器：

![](/img/4f432620cfebced0.webp)

如果您希望使用內建天線，請保持選擇 uFL。如果您希望使用連線到 SMA 插槽的外接天線，請選擇 MMCX。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三個功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置現在將尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪個選項，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含以下隨裝置附帶的配件：

- EU/US 開關電源 24 V ⎓，0.8 A，19.2 W，85.3 %，VI，線纜：150 cm Hor CMC。
- WAP 桌面支架。
- WAP 戶外外殼支架 AL，白色。
- POE 注入器線纜。
- 線纜 (H4130-04PDB000R 3 mm 2x2P Housing) 至 (StripJacket 5 cm+WireEnd Strip/Tin 1 cm) 24 AWG。
- 軟管卡箍，35-70 mm，W4。
- K-52 緊固套裝。
- WAP-drill-template，紙質手冊。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統未經測試。RouterOS 的 LR 支援僅限於 MikroTik LR 卡，不支援第三方 Lora 卡。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解您所在地區將裝置正確運輸至指定處置場所的相關程式。

## UKCA 標誌 {#ukca-marking}

![](/img/387853c20d5a4c82.gif)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2412 - 2472 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻段通道可能因產品型號和認證而異。

有關裝置製造日期的資訊以斜槓分隔標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），隨後的兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## Norma Oficial Mexicana {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2412 - 2472 MHz (30 dBm)。可用頻道可能因產品型號和認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2412 - 2472 МГц (20 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用須按照 2012 年 11 月 1 日第 559 號國家通訊與資訊化監管委員會決議（於 2013 年 1 月 3 日在烏克蘭司法部註冊，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBwAPR-2nD&R11e-LR2 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WLAN / LR {#wlan--lr}

<table><thead><tr><th>***WLAN***</th><th>工作頻率 / 最大輸出功率</th><th>2412-2472 MHz / 20 dBm</th></tr></thead><tbody><tr><td>**LR**</td><td>2403-2479 MHz / 20 dBm</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。有關更多詳細資訊，請參見上文的符合性宣告。
