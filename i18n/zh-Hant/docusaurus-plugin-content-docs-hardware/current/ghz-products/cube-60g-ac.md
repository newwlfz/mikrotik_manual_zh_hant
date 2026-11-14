---
title: "Cube 60G ac"
slug: /cube-60g-ac
source: https://manual.mikrotik.com/hardware/cube-60g-ac
captured_at: '2026-11-04T09:48:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/cube-60g-ac-0575326476d89f7f1ddf08a17bccceb7.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/e1fbe52194fa5d7e.webp)

## [Cube 60G ac](https://mikrotik.com/product/cube_60g_ac)（CubeG-5ac60ad） {#cube-60g-ac-cubeg-5ac60ad}

客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

## 安全警告 {#safety-warnings}

- 在操作任何裝置之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 在任何牆面上安裝接入點的所有安裝方法均須獲得當地主管部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適合安裝在戶外的杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險情況並損壞系統。
- 僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 這是 A 類裝置。在居住環境中，本產品可能會造成無線電干擾，在這種情況下，使用者可能需要採取適當的措施。

## 快速開始 {#quickstart}

- 使用乙太網線將裝置連線到隨附的 PoE 注入器；
- 將 PoE 注入器連線到 PC 或網路交換器；
- 將電源介面卡連線到 PoE 注入器；
- 下載 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)，開啟 WinBox 並連線到裝置；
- 預設 IP：192.168.88.1，使用者名稱：**admin**，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 從 [https://mikrotik.com/download](https://mikrotik.com/download) 下載最新的 RouterOS 軟體；
- 選擇 ARM 軟體包，並將其儲存到您的 PC；
- 開啟 WinBox 並上傳已下載的軟體包，將其拖放到任意視窗中；
- 重啟裝置；
- 再次連線，在 Wireless 選單的 W60G 標籤頁中選擇您所在的地區，並在 **QuickSet** 選單中設定您所在的國家/地區，以應用國家/地區法規設定。*如果裝置發生了 RX 阻塞情況，裝置將在幾秒鐘後恢復其訊號。*

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描 QR 碼並選擇您偏好的作業系統。
- 安裝並開啟該應用。
- 預設情況下，IP 地址和使用者名稱將已自動填入。
- 單擊 Connect，透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 還提供高階選單，可完整配置所有必要的設定。

## 配置 {#configuration}

登入後，我們建議在 QuickSet 選單中單擊 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將要使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，熟悉各種可能的功能：[https://mt.lv/help](https://mt.lv/help)。如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置（參見 ）。如果裝置失去連線，請等待幾秒鐘，裝置將自動恢復連線。

## 組裝與安裝 {#assembly-and-mounting}

該裝置可以安裝在垂直或水平杆上，如圖 A 和 B 所示。請注意，安裝裝置時底部卡扣必須朝下。最大桿直徑是 51 mm。

本裝置的安裝和配置應由經過認證的人員完成。

選擇您想要的位置，裝置需要精確調整才能獲得最佳效能。

- 使用 ph0 螺絲刀，用隨附的螺絲將隨附的支架固定到裝置背面。
- 使用 8 mm 棘輪，用 U 型螺栓支架安裝到杆上。
- 將螺栓放在三個位置之一，它們可以實現微調；當放在中間位置時，您可以在 23 度範圍內進行調整，如果調整需要更大的範圍，請將螺絲更換到其他位置。

![](/img/acd1ca316e8c01cd.webp)

本裝置的 IP 防護等級為 IP54。在戶外安裝時，請確保所有線纜開口朝下。我們建議使用 POE 注入器，並使用 Cat6 遮蔽線纜進行正確接地。使用和安裝本裝置時，請注意最大允許暴露（MPE）安全距離，輻射體與您身體之間的最小距離為 20 cm。

此外，也可以將裝置安裝在裝置背面的三個安裝槽之一上。

![](/img/c5e03fa807689f16.webp)

![](/img/be7006c56abe1792.webp)

- 例如，您可以使用金屬環。
- 使用十字螺絲刀鬆開金屬環。
- 將金屬環的一端穿過三個安裝槽中最方便的一個。
- 將裝置放置在將要安裝的杆上。
- 將安裝環的活動端滑回其閉合卡扣處，並使用螺絲刀將其擰緊。

建議使用紮帶將乙太網線纜固定在杆上。與裝置的距離約為 30 cm。

作為額外選項，您可以使用 "quickMOUNT-X" —— 一個便於調節的安裝支架，可單獨購買。產品網頁：[https://mikrotik.com/product/qm_x](https://mikrotik.com/product/qm_x)

![](/img/8f9318498c6d2b23.webp)

經過專門設計，可在杆上進行垂直和水平調節。

## 接地 {#grounding}

本裝置包含一個接地連線（標記為 ⏚），您應將其連線到裝置使用所在塔架或建築物的接地裝置。這可大幅降低 ESD 和雷擊損壞的風險。

## 供電 {#powering}

該裝置由 Passive PoE 注入器（隨附一個電源和 PoE 注入器）提供 DC ⎓ 電源，支援 12-28 V DC ⎓，最大負載功耗為 4 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將來自裝置的乙太網線纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的乙太網線纜連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 10/100 乙太網埠。
- 整合 5 GHz 802.11a/n/ac 介面，帶內建天線。
- WiGig 晶片組 QCA6335。

## 復位按鈕 {#reset-button}

routerBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置復位為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置和預設值。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- 歐規/美規開關電源 24V DC ⎓，0.8 A，9 W，Level VI，線纜：1.5 m。
- 帶遮蔽乙太網線纜/聯結器的 POE 注入器（RBPOE）。
- Cube 支架。
- 用於 Cube 支架的 K-70 緊固套件。

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS 軟體版本 *v6.47.2*。具體的出廠安裝版本號顯示在 RouterOS 選單 /system resource 中。其他作業系統尚未經過測試。

本裝置符合 ETSI 法規規定的最大 TX 功率限值。在歐盟的頻率和最大發射功率如下：57-66GHz：34.92 dBm。60 GHz 頻段的工作模式：58.32 GHz、60.48 GHz、62.64 GHz、64.80 GHz。本裝置已透過認證，可在點對多點應用中用於戶外。在以下國家/地區，本裝置不能用於固定點對點應用：

![](/img/01438e2d9209ce7d.webp)

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCCID</th></tr></thead><tbody><tr><td>CubeG-5ac60ad</td><td>TV7CB5A60</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝環境中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在居住區操作本裝置可能會造成有害干擾，在這種情況下，使用者將被要求自費糾正干擾。

**FCC 注意：** 任何未經合規負責方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。其操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。

除 FCC CFR §15.255 (b) 中列出的條件外，本裝置不得在飛機上操作。

**重要：FCC 輻射暴露宣告：** 本裝置符合 FCC 針對不受控環境設定的輻射暴露限值。安裝和操作本裝置時，輻射體與您身體之間的最小距離應為 21cm。用於連線外圍裝置的所有線纜必須遮蔽並接地。使用未遮蔽且未接地的線纜連線外圍裝置進行操作，可能會對無線電和電視接收造成干擾。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>CubeG-5ac60ad</td><td>7442A-CB5A60</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 的免許可發射器/接收器。其操作須符合以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

除 ISED RSS-210 附錄 J.1 中列出的條件外，本裝置不得在飛機上操作。

本裝置不得在飛機上使用，除非符合 ISED RSS-210 附錄 J.1 中所列的條件。

在 5150–5250 MHz 頻段內工作的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

**重要：IC 輻射暴露宣告：** 本裝置符合 IC RSS-102 針對不受控環境設定的輻射暴露限值。安裝和操作本裝置時，輻射體與您身體之間的最小距離應為 21cm。本裝置符合 IC 針對不受控環境設定的輻射暴露限值。安裝和使用本裝置時，輻射源與您身體之間的最小距離應為 21cm。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射機功率</th></tr></thead><tbody><tr><td>5650-5850 MHz</td><td>≤10 W</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證情況而有所不同。

裝置製造日期資訊標註在其標籤上序列號的末尾，用斜線分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需要按照 NCCIR 2012 年 11 月 1 日第 559 號決定（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 CubeG-5ac60ad 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WiGig {#wigig}

<table><thead><tr><th>工作通道 / 最大輸出功率</th><th>58.32 GHz / &lt;40 dBm</th></tr></thead><tbody><tr><td>60.48 GHz / &lt;40 dBm</td><td></td></tr><tr><td>62.64 GHz / &lt;40 dBm</td><td></td></tr></tbody></table>

### WLAN {#wlan}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>5470-5725 MHz / 27 dBm</th></tr></thead></table>
