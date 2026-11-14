---
title: "Chateau 5G"
slug: /chateau-5g
source: https://manual.mikrotik.com/hardware/chateau-5g
captured_at: '2026-11-04T09:44:54+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/58927a682e31d536.jpg)

## [Chateau 5G](https://mikrotik.com/product/chateau_5g) (D53G-5HacD2HnD-TC&RG502Q-EA) {#chateau-5g-d53g-5hacd2hnd-tcrg502q-ea}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關危險，並熟悉防止事故的標準做法。有關完整規格和手冊，請參閱 [Chateau 5G 產品頁面](https://mikrotik.com/product/chateau_5g)。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適合室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和附件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，操作風險由您自行承擔！
- 如果裝置故障，請斷開電源。最快的方法是從電源插座中拔出電源插頭。
- 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，應與您的身體、職業使用者或公眾保持不小於 20 釐米的距離。

## 快速開始 {#quickstart}

按照以下快速步驟設定您的裝置：

![](/img/cbc5361d4144eab4.webp)

- 將外部天線連線到 SMA 介面（天線隨包裝提供，請參閱“(link)”）；
- 將 micro SIM 卡插入裝置下方的插槽；

![](/img/9619076cdc698366.webp)

- 將計算機連線到其中一個乙太網埠；
- 將電源介面卡連線到 DC 插孔；
- 裝置通電且 PC 已連線到裝置後，在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始配置（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）；
- 使用者名稱：a*dmin*，預設沒有密碼，您將自動登入到 Quick Set 介面；
- 您應選擇右側的“Check for updates”按鈕，並將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性；必須插入有效的 SIM 卡；
- 要手動更新裝置，請訪問 [https://mikrotik.com/download](https://mikrotik.com/download)
- 為此裝置選擇 ARM 軟體包，並將其下載到您的 PC。
- 將下載的軟體包上傳到 WebFig 的“Files”選單，然後重啟裝置。
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新。
- 要個性化您的無線網路，可以在“Network Name”欄位中更改 SSID；
- 在螢幕左側的“Country”欄位中選擇您的國家/地區，以應用國家/地區法規設定；
- 在“WiFi Password”欄位中設定無線網路密碼，密碼必須至少包含八個字元；
- 在右下方的“Password”欄位中設定路由器密碼，並在“Confirm Password”欄位中重複輸入，該密碼將用於下次登入；
- 選擇“Apply Configuration”以儲存更改。

## 使用移動應用連線 {#connecting-with-a-mobile-app}

使用智慧手機透過 WiFi 訪問路由器。

![](/img/9bcba09a7b6a0d53.webp)

- 插入 SIM 卡並開啟裝置。
- 用智慧手機掃描二維條碼並選擇您首選的作業系統。
- 連線到無線網路。SSID 以 MikroTik 開頭，幷包含裝置 MAC 地址的最後幾位數字。
- 開啟應用程式。
- 預設情況下，IP 地址和使用者名稱已預先填寫。
- 選擇 Connect 以透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 高階選單可用於完整配置所有必要設定。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/448fe884f3fe7820.webp)

- （link）。
- （link）DC 插孔 2.0 mm。
- 五個千兆埠，支援自動交叉/直通線纜校正（Auto MDI/X）。可使用直通或交叉線纜連線其他網路裝置。
- USB type-A。
- 用於 Micro SIM 卡的（link）。
- 模式按鈕。
- 帶天線的型號不提供外部（link）的蓋子。
- WPS（link）
- 整合無線模組工作在 2.4 GHz，802.11b/g/n 協定。天線增益 3 (dBi)。
- 整合無線模組工作在 5 GHz，802.11a/n/ac 協定。天線增益 4 (dBi)。

## 安裝 {#mounting}

本裝置設計用於室內，可放置在桌面上使用。

應使用 Cat5 遮蔽線纜。使用和安裝本裝置時，請注意最大允許暴露（MPE）安全距離，輻射器與身體之間至少保持 20 cm。

## 供電 {#powering}

裝置透過介面卡供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）12-28 V DC⎓。最大負載下的功耗可達 17 W，連線附件時為 23 W。

## 配置 {#configuration}

您應經常檢查更新，以獲取 RouterOS 軟體的最新更新，從而確保最佳效能和穩定性。除了本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能的功能：[https://mt.lv/help](https://mt.lv/help)。如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。為恢復目的，可以讓裝置進入重新安裝啟動模式，請參閱（link）部分。

## 模式按鈕 {#mode-button}

模式按鈕位於裝置背面右側。模式按鈕的預設配置為暗色模式 - 關閉所有 LED。可以在 RouterOS 中配置該按鈕以執行任何使用者指定的指令碼。

## 同步按鈕 {#sync-button}

同步按鈕位於裝置頂部。如果在無線介面上配置了 WPS Sync 按鈕，則可用於連線新用戶端。

![](/img/c76f6511aa4e14f0.webp)

- 按住 WPS 按鈕 1 – 5 秒，以為無線介面啟用 WPS。

## 前面板 LED 狀態 {#front-led-status}

![](/img/9ba5b3e5c27a0830.webp)

- 無線網路活動。
- 乙太網埠活動。
- 系統 LED 具有用於指示蜂窩調變解調器狀態的交替模式。
- 訊號強度。

### 系統 LED 交替調變解調器模式指示 {#system-led-alternate-modem-mode-indications}

啟用蜂窩調變解調器介面後，系統 LED 將具有交替指示：

紅色閃爍 - 未插入 SIM 卡

黃色 - 已建立 3G 模式連線

藍色 - 已建立 LTE 模式連線

綠色 - 已建立 5G NSA 模式連線

紫色 - 已建立 5G SA 模式連線

閃爍 - 正在建立連線，調變解調器已註冊到蜂窩網路，APN 尚未啟用

## SIM 插槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡插槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議配合轉接器使用。

## 復位按鈕 {#reset-button}

復位按鈕具有三項功能：

- 在啟動期間按住此按鈕，直到綠色 LED 開始閃爍，鬆開按鈕以重設 RouterOS 配置（總計 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開以開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（總計 10 秒）。
- 要使用 Netinstall 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種可用的載入程式：常規載入程式和備用載入程式。常規載入程式 - 開啟裝置，等待 1-2 秒，然後按住 Reset 按鈕。等待系統 LED 綠色閃爍，然後變為常亮“On”。當綠色 LED 變為“Off”時，鬆開 Reset 按鈕 - 裝置將進入 BOOTP 模式。
- 備用載入程式 – 關閉裝置，按住 Reset 按鈕，然後開啟裝置。等待系統 LED 綠色閃爍，然後變為常亮“On”。當綠色 LED 變為“Off”時，鬆開 Reset 按鈕 - 裝置將使用備用載入程式進入 BOOTP 模式。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統都將載入備用 RouterBOOT 載入程式。這可用於 RouterBOOT 偵錯和恢復。

執行 Netinstall 時，請確保 ROS 檔案和 Netinstall 軟體均使用最新的 v7 版本。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的附件：

- ADAPT1_ EU/US 開關電源 24V，1.2A。
- CAB3_ CAT5E UTP 扁平線纜，8P8C，AWG32，1.5m。
- ANT8-9_ 外部 LTE 天線。

## 天線使用 {#antenna-usage}

SMA 介面用於隨附的 LTE 天線。

連線或斷開外部天線時，裝置必須斷電，否則裝置可能損壞！

外部天線插孔位於裝置背面。

- 將兩根天線擰到 SMA 插孔上（請按照圖示中的說明操作）。

![](/img/b135503a374e2302.webp)

## 拆卸後蓋以接觸 PCB {#removing-back-cover-to-access-pcb}

如果需要接觸 PCB，可以拆下後蓋。

- 拆下中心螺絲；

![](/img/3c40f644b6453592.webp)

- 使用小螺絲刀在標記位置撬開後蓋板；
- 繼續向上撬開；

![](/img/ef5c2817560d190a.webp)

- 最後整個後蓋板取下。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未測試。

為避免環境汙染，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請熟悉您所在地區將裝置正確運輸至指定處置場所的程式。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。*

裝置製造日期資訊位於其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2480-2483.5 МГц (20 дБм)，5150-5250 МГц (23 дБм)，5250-5350 МГц (20 дБм)，5470-5725 МГц (27 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置，必須按照烏克蘭國家通訊和資訊監管委員會（НКРЗІ）2012 年 11 月 1 日第 559 號決定批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, 拉脫維亞, LV1039。

Mikrotīkls SIA 特此宣告，型號為 D53G-5HacD2HnD-TC&RG502Q-EA 的無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WLAN / WCDMA / LTE / 5G {#wlan--wcdma--lte--5g}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>WLAN 2.4 Ghz</th><th>2400-2483.5 MHz / 20 dBm</th></tr></thead><tbody><tr><td>WLAN 5Ghz</td><td>5150-5250 MHz / 23 dBm</td><td></td></tr><tr><td>WLAN 5Ghz</td><td>5250-5350 MHz / 20 dBm</td><td></td></tr><tr><td>WLAN 5Ghz</td><td>5470-5725 MHz / 27 dBm</td><td></td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band III</td><td>1712.4 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band V</td><td>826.4 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1700 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 5</td><td>850 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 28</td><td>700 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 32</td><td>1500 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 34</td><td>2000 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23, 26dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23, 26dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 41</td><td>2500 MHz / 23, 26dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 42</td><td>3500 MHz / 23, 26dBm ± 3 dB</td><td></td></tr><tr><td>LTE Band 43</td><td>3700 MHz / 23dBm ± 3 dB</td><td></td></tr><tr><td>5G NR Band n1</td><td>2100 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n3</td><td>1800 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n7</td><td>2600 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n8</td><td>900 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n20</td><td>800 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n28</td><td>700 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n38</td><td>2600 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n40</td><td>2300 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n41</td><td>2500 MHz / 26dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n77</td><td>3700 MHz / 26dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n78</td><td>3500 MHz / 26dBm ± 2 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大發射功率限值。有關更多詳細資訊，請參閱上方的符合性宣告。

![](/img/0561b3ba8c95a35c.webp)

在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限於室內使用。
