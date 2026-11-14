---
title: "nRAY 系列"
slug: /nray-series
source: https://manual.mikrotik.com/hardware/nray-series
captured_at: '2026-11-04T09:58:06+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可作為 <a href="/assets/files/nray-series-8b1c8f47fdd8ce1e1b232581c0108acf.pdf" target="_blank" rel="noopener">PDF 檔案</a> 下載。

## [Wireless Wire nRAY](https://mikrotik.com/product/wireless_wire_nray) (nRAYG-60adpair) {#wireless-wire-nray-nrayg-60adpair}

![](/img/13fadc3ec23f304e.jpg)

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關危險，並熟悉防止事故的標準做法。完整規格和宣傳冊請參見 [nRAY 系列產品頁面](https://mikrotik.com/product/wireless_wire_nray)。
- 本產品的最終處置應按照所有國家法律和法規處理。
- 在任何牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置安裝必須符合當地和國家電氣規範。
- 本產品設計用於室外立杆安裝，但也可在室內安裝。開始安裝前，請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確的操作程式，可能導致人員危險和系統損壞。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和附件。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證不會因不當使用裝置而發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能會造成無線電干擾，在這種情況下，使用者可能需要採取適當措施。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 擰下蓋子以接觸乙太網埠；
- 將乙太網電纜穿過開口；
- 插入乙太網埠並順時針擰緊，以確保防水；
- 將 PoE 注入器連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 下載 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)，或使用 Web 瀏覽器；
- 預設 IP：192.168.88.2 和 192.168.88.3，使用者名稱：**admin**，密碼請見裝置標籤；
- 預設情況下，裝置配置為 W60G Bridge；
- 連線後，配置裝置使其具有可用的 Internet 連線 [https://mt.lv/configuration](https://mt.lv/configuration)，或繼續下一步手動升級軟體；
- 將 RouterOS 軟體升級到最新版本 [https://mt.lv/upgrade](https://mt.lv/upgrade)；
- 再次連線並選擇您的區域，可在 Wireless 選單的 W60G 標籤頁中完成；
- 雙擊 W60G 介面，轉到 Wireless 標籤頁並選擇您的區域；

## 供電 {#powering}

裝置支援 802.3af/at PoE 供電，12 – 57 V DC ⎓。最大負載下的功耗可達 6 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網電纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路 (LAN) 的乙太網電纜連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 安裝 {#mounting}

本裝置設計用於室外並安裝在立杆上。安裝時，請確保排水孔朝下。本裝置的 IP 防護等級為 IP54。我們建議使用 Cat6 遮蔽電纜。警告！本裝置安裝和操作時，裝置與人體之間應保持至少 60 cm 的距離。本裝置在住宅環境中使用可能會造成無線電干擾。*本裝置的安裝和配置應由具備資質的人員完成。*

- 使用安裝支架組裝裝置。

![](/img/4d07761fb35c6ef7.webp)

- 使用 M5 螺釘固定安裝支架，並用 HEX3 工具擰緊——該工具不隨包裝提供。
- 插入 U 型螺栓。按照圖片所示的順序進行。

![](/img/ad91bad55da92d23.webp)

- 將元件固定到立杆上。

![](/img/11b701c0c3d9bdda.webp)

- 安裝安裝支架，並使用兩個 13 mm 螺母固定裝置。

![](/img/64d3710a74ea5103.webp)

## 對準工具使用 {#aim-tool-usage}

![](/img/733707fa84b1658d.webp)

裝置背面帶有 LED 箭頭。使用這些箭頭可實現精確對準。

![](/img/b9d380f70a9cb9a7.webp)

箭頭會亮起並指示應轉動裝置的方向。目標是達到 0.4 - 0.8 度範圍，此時訊號最強。

## 接地 {#grounding}

安裝基礎設施（塔架和桅杆）必須正確接地。請將所有鬆散的乙太網電纜和天線電纜固定在距裝置約 30cm 的立杆或桅杆上，以免電纜重量拉扯埠和聯結器。

## 配置 {#configuration}

我們建議在 QuickSet 選單中點選 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。請確保已選擇裝置將使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。請向當地培訓師尋求更多幫助，或自己成為培訓師。[https://mikrotik.com/training/about](https://mikrotik.com/training/about) 為恢復目的，可以啟動裝置進行重新安裝，請參閱 節。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（總計 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開以開啟 CAP 模式。裝置現在將尋找 CAPsMAN 伺服器（總計 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（總計 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體出廠安裝版本列在 /system resource 中。其他作業系統尚未經過測試。

## 說明 {#notes}

本裝置符合 ETSI 法規規定的最大 TX 功率限制。60 GHz 頻段的工作模式：58.32 GHz、60.48 GHz、62.64 GHz、64.80 GHz。本裝置已獲認證，可用於點對多點應用的室外使用。在以下國家/地區，本裝置不能用於固定點對點應用：

![](/img/01438e2d9209ce7d.webp)

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID: TV7RAY60

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝提供合理保護，防止有害干擾。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域操作本裝置很可能造成有害干擾，在這種情況下，使用者需要自費糾正干擾。

**FCC 警告：** 未經合規負責方明確批准的任何更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或協同操作。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的 RF 輻射暴露限值。本裝置安裝和操作時，輻射體與身體任何部位之間應保持至少 60 cm 的距離。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

IC: 7442A-RAY60

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：

-

本裝置不得造成干擾；

-

本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。本裝置中包含的免許可發射器/接收器符合加拿大創新、科學和經濟發展部適用於免許可無線電裝置的 CNR。允許在以下兩個條件下執行：

-

本裝置不得產生干擾；

-

本裝置必須接受其受到的任何無線電干擾，即使該干擾存在。**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和操作時，輻射體與身體任何部位之間應保持至少 60 cm 的距離。本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和操作時，輻射體與身體任何部位之間應保持至少 60 cm 的距離。

除 ISED RSS-210 附錄 J.1 中列出的條件外，本裝置不得在飛機上操作。除 ISED RSS-210 附錄 J.1 中列出的條件外，本裝置不得在飛機上使用。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置製造日期資訊位於其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位表示週數。

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

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置，必須按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議批准並在烏克蘭司法部於 2013 年 1 月 3 日以第 57/22589 號登記的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 nRAYG-60adpair 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WiGig {#wigig}

<table><thead><tr><th>工作通道 / 最大輸出功率</th><th>58.32 GHz / &lt;40 dBm</th></tr></thead><tbody><tr><td>60.48 GHz / &lt;40 dBm</td><td></td></tr><tr><td>62.64 GHz / &lt;40 dBm</td><td></td></tr></tbody></table>
