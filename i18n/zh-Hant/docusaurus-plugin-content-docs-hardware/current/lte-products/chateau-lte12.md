---
title: "Chateau LTE12"
slug: /chateau-lte12
source: https://manual.mikrotik.com/hardware/chateau-lte12
captured_at: '2026-11-04T09:45:19+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/917e5b584a337097.jpg)

## [Chateau LTE12](https://mikrotik.com/product/chateau_lte12) (RBD53G-5HacD2HnD-TC&EG12-EA) {#chateau-lte12-rbd53g-5hacd2hnd-tceg12-ea}

Chateau 是一款家用路由器，需配合蜂窩網路運營商的 SIM 卡使用。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本產品適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因裝置使用不當而不會發生事故或損壞。請小心使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

按照以下快速步驟設定您的裝置：

![](/img/cbc5361d4144eab4.webp)

- 將計算機連線到其中一個乙太網埠；
- 可選——將外部天線連線到 SMA 聯結器（包裝中不提供天線，有關 Micro SIM 卡，請參見 "(link)。
- 模式按鈕。
- 外部 (link) 蓋板。
- WPS (link)
- 整合無線模組，工作於 2.4 GHz，802.11b/g/n 協定。
- 整合無線模組，工作於 5 GHz，802.11a/n/ac 協定。

## 安裝 {#mounting}

該裝置設計用於室內，可放置在桌面上使用。

應使用 CAT5 遮蔽電纜。使用和安裝此裝置時，請注意最大允許暴露量（MPE）安全距離，輻射體與身體之間至少保持 20 cm。

## 供電 {#powering}

裝置透過介面卡供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）12-28 V DC⎓。最大負載下的功耗可達 17 W，帶附件時為 23 W。

## 配置 {#configuration}

可以使用 Web 瀏覽器透過 WebFig、WinBox 工具 [https://mt.lv/winbox](https://mt.lv/winbox) 或 (link) 進行配置。提供多種方法以確保可訪問性。

- 要訪問 WebFig，請在瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1)。
- 對於 WinBox，請下載該工具，轉到 Neighbors 標籤頁，然後選擇 MAC 地址。預設使用者名稱是 "admin"，**在裝置貼紙上查詢密碼**。您應經常檢查更新，以確保 RouterOS 軟體保持最新，從而獲得最佳效能和穩定性。在 WinBox 或 WebFig 中選擇“Check for updates”按鈕以更新到最新版本。

必須插入有效的 SIM 卡或設定 eSIM，並且具有活動的 Internet 連線，更新才能正常工作。

本文件所述內容之外，RouterOS 還提供廣泛的配置選項。我們建議訪問 [https://mt.lv/help](https://mt.lv/help) 瞭解這些功能。

出於恢復目的，可以啟動裝置以重新安裝，參見 部分。

## 模式按鈕 {#mode-button}

模式按鈕位於裝置背面右側（見 ""）。模式按鈕的預設配置是暗色模式——關閉所有 LED。該按鈕可在 RouterOS 中配置為執行任何使用者指定的指令碼。

## 同步按鈕 {#sync-button}

同步按鈕位於裝置頂部。WPS 同步按鈕如果在無線介面上配置，可用於連線新用戶端。

![](/img/c76f6511aa4e14f0.webp)

- 按住 WPS 按鈕 1 – 5 秒，以啟用無線介面的 WPS。

## 前面板 LED 狀態 {#front-led-status}

![](/img/9ba5b3e5c27a0830.webp)

- 無線網路活動。
- 乙太網埠活動。
- 系統 LED，具有用於指示蜂窩調變解調器狀態的替代模式。
- 調變解調器訊號強度指示器。

### 系統 LED 替代調變解調器模式指示 {#system-led-alternate-modem-mode-indications}

紅色閃爍：未插入 SIM 卡

黃色：3G

藍色：LTE

閃爍：正在建立連線，調變解調器已註冊到蜂窩網路，APN 尚未啟用

當 LTE 未連線到網路時，系統 LED 將紅色閃爍，表示 LTE 連線存在一些問題。如果 LTE 介面被有意停用（未使用），系統 LED 將亮藍色。

## SIM 卡槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議與轉接器一起使用。

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 在啟動期間按住此按鈕，直到綠色 LED 開始閃爍，鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開以開啟 CAP 模式。裝置現在將尋找 CAPsMAN 伺服器（共 10 秒）。
- 要使用 Netinstall 實用程式重新安裝 RouterOS，請使裝置進入 BOOTP 模式。可用的載入程式有兩種：常規載入程式和備份載入程式。常規載入程式——開啟裝置電源，等待 1-2 秒，然後按住復位按鈕。等待系統 LED 呈綠色閃爍，然後變為常亮“On”。當綠色 LED 變為“Off”時，鬆開復位按鈕——裝置將進入 BOOTP 模式。
- 備份載入程式——關閉裝置電源，按住復位按鈕，然後開啟電源。等待系統 LED 呈綠色閃爍，然後變為常亮“On”。當綠色 LED 變為“Off”時，鬆開復位按鈕——裝置將使用備份載入程式進入 BOOTP 模式。無論使用上述哪種選項，如果在給裝置供電之前按下按鈕，系統將載入備份 RouterBOOT 載入程式。適用於 RouterBOOT 偵錯和恢復。

Netinstall 執行 Netinstall 時，請確保 ROS 檔案和 Netinstall 軟體均使用最新的 v7 版本。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- 歐盟/美國開關電源 24 V ⎓，1.2 A，28.8 W，86.8 %，VI，線纜：150 cm。
- CAT5E UTP 扁平線纜，8P8C，AWG32，1.5 m，白色。

## LTE 天線使用 {#lte-antenna-usage}

SMA 聯結器用於 LTE 天線。

裝置背面門後有兩個外部天線聯結器。

- 向上拉開門。
- 將 LTE 天線擰到左側的 SMA 聯結器上。所用天線聯結器或任何其他介面卡的最大直徑為 13 mm。

![](/img/b70ac6f60339b714.webp)

使用一根天線時，連線到左側的 SMA 聯結器（ANT1）。僅當使用兩根天線時，才可以連線到右側的 SMA 聯結器（ANT4）。

![](/img/d3359d36ecb577c0.webp)

在裝置關閉時連線和斷開天線！裝置上的 SMA 聯結器為母頭。

您應使用我們的天線 [https://mikrotik.com/product/mant_lte_5o](https://mikrotik.com/product/mant_lte_5o)

## 拆下前蓋以接觸 PCB {#removing-front-cover-to-access-pcb}

如果需要接觸 PCB，可以拆下前蓋。

- 拆下中心螺絲；

![](/img/3c40f644b6453592.webp)

- 使用小螺絲刀在標記位置撬開蓋子；
- 繼續向上撬開；

![](/img/ef5c2817560d190a.webp)

- 最後取下整個蓋子。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置正確運輸至指定處置場所的程式。

## UKCA 標識 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊在其標籤上的序列號末尾以斜槓分隔表示。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

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

## 烏克蘭國家通訊和資訊領域國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2480-2483.5 МГц（20 дБм），5150-5250 МГц（23 дБм），5250-5350 МГц（20 дБм），5470-5725 МГц（27 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式取得使用許可。

### CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i, 里加, 拉脫維亞, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBD53G-5HacD2HnD-TC&EG12-EA 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

#### WLAN / WCDMA / LTE {#wlan--wcdma--lte}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th></th></tr></thead><tbody><tr><td>WLAN 2.4 Ghz</td><td>2400-2483.5 MHz / 20 dBm</td></tr><tr><td>WLAN 5Ghz</td><td>5150-5250 MHz / 23 dBm</td></tr><tr><td>WLAN 5Ghz</td><td>5250-5350 MHz / 20 dBm</td></tr><tr><td>WLAN 5Ghz</td><td>5470-5725 MHz / 27 dBm</td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 24dB ± 2.7 dB</td></tr><tr><td>WCDMA Band III</td><td>1712.4 MHz / 24dB ± 2.7 dB</td></tr><tr><td>WCDMA Band V</td><td>826.4 MHz / 24dB ± 2.7 dB</td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 24dB ± 2.7 dB</td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dB ± 2.7 dB</td></tr><tr><td>LTE Band 3</td><td>1700 MHz / 23dB ± 2.7 dB</td></tr><tr><td>LTE Band 5</td><td>850 MHz / 23dB ± 2.7 dB</td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dB ± 2.7 dB</td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dB ± 2.7 dB</td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dB ± 2.7 dB</td></tr><tr><td>LTE Band 28</td><td>700 MHz / 23dB ± 2.7 dB</td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dB ± 2.7 dB</td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dB ± 2.7 dB</td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告。 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告。

![](/img/0561b3ba8c95a35c.webp)

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限於室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限於室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限於室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限於室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限於室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限於室內使用。
