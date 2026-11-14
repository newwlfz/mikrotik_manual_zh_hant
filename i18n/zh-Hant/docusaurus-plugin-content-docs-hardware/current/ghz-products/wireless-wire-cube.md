---
title: "無線 Wire Cube"
slug: /wireless-wire-cube
source: https://manual.mikrotik.com/hardware/wireless-wire-cube
captured_at: '2026-11-04T10:08:49+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/wireless-wire-cube-341547731816889727201641e27bbc3a.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/2a56acfbac220108.jpg)

## [Wireless Wire Cube](https://mikrotik.com/product/wireless_wire_cube) (CubeG-5ac60adpair) {#wireless-wire-cube-cubeg-5ac60adpair}

客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、布纜要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置擬安裝於機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會對人員造成危險情況並對系統造成損壞。
- 本產品僅供室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座上拔下電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、布纜要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 本裝置為 A 類裝置。在住宅環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置應與您的身體、職業使用者或普通公眾保持不少於 21 釐米的距離。

## 快速開始 {#quickstart}

- 用網線將裝置連線到隨附的 PoE 注入器；
- 將 PoE 注入器連線到 PC 或網路交換器；
- 將電源介面卡連線到 PoE 注入器；
- 下載 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)，開啟 WinBox 並連線到裝置；
- 預設 IP：192.168.88.2/192.168.88.3，使用者名稱：**admin**，密碼請見裝置標籤；
- 從 [https://mikrotik.com/download](https://mikrotik.com/download) 下載最新的 RouterOS 軟體；
- 選擇 ARM 軟體包，並將其儲存到您的 PC；
- 開啟 WinBox 並上傳已下載的軟體包，將其拖放到任意視窗中；
- 重啟裝置；
- 再次連線，並在 Wireless 選單的 W60G 標籤頁中選擇您的區域，在 **QuickSet** 選單中設定您的國家/地區，以應用國家法規設定。*如果裝置發生 RX 阻塞情況，裝置將在幾秒後恢復其訊號。*

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟應用。
- 預設情況下，IP 地址和使用者名稱將已自動填入。
- 點選 Connect 透過無線網路與您的裝置建立連線。
- 選擇 Quick setup，應用將通過幾個簡單步驟引導您完成所有基本配置設定。
- 還提供高階選單，可完整配置所有必要的設定。

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將您的 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將要使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置（參見 ）。如果裝置失去連線，請等待幾秒鐘，然後裝置將自動恢復連線。

## 組裝與安裝 {#assembly-and-mounting}

該裝置可以如圖片 A 和 B 所示安裝在垂直或水平抱杆上。請注意，裝置安裝時底部卡扣必須朝下。最大抱桿直徑為 51 mm。

本裝置的安裝和配置應由經過認證的人員完成。

選擇您想要的位置，裝置需要精確調整才能獲得最佳效能。

- 使用 ph0 螺絲刀，用隨附的螺絲將隨附的安裝支架固定到裝置背面。
- 使用 8 mm 棘輪，用 U 型螺栓支架安裝到抱杆上。
- 將螺栓放入三個位置之一，它們可以實現精細調節；放在中間位置時，您可以在 23 度範圍內調節，如果需要進一步調節，請將螺絲換到其他位置。

![](/img/acd1ca316e8c01cd.webp)

本裝置的 IP 防護等級為 IP54。在戶外安裝時，請確保所有線纜開口朝下。我們建議使用 POE 注入器並採用 Cat6 遮蔽線纜進行正確接地。使用和安裝本裝置時，請注意最大允許暴露（MPE）安全距離，輻射體與您的身體之間至少保持 20 cm。

此外，裝置也可以安裝在裝置背面的三個安裝槽之一上。

![](/img/c5e03fa807689f16.webp)

![](/img/be7006c56abe1792.webp)

- 例如，您可以使用金屬環。
- 使用十字螺絲刀鬆開金屬環。
- 將其一端穿過三個安裝槽中最方便的一個。
- 將裝置放置在其將要安裝的抱杆上。
- 將安裝環的松端滑回其閉合卡扣，並用螺絲刀擰緊。

建議使用紮帶將網線固定在抱杆上，與裝置的距離約為 30 cm。

作為附加選項，您可以使用 "quickMOUNT-X" —— 一種可單獨購買的、便於調節的安裝支架。產品網頁：[https://mikrotik.com/product/qm_x](https://mikrotik.com/product/qm_x)

![](/img/8f9318498c6d2b23.webp)

其特殊設計可在抱杆上實現垂直和水平調節。

## 接地 {#grounding}

裝置包含一個接地連線（標記為 ⏚），您應將其連線到裝置使用所在地的塔架或建築物的接地裝置上。這可大幅降低靜電放電和雷擊損壞的風險。

## 供電 {#powering}

Cube Lite60 接受來自無源 PoE 注入器的 DC ⎓ 電源（隨附一個電源和一個 PoE 注入器），支援 12-28 V DC ⎓，最大負載功耗為 4 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置上的網線連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的網線連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 10/100 乙太網埠。
- 整合 5 GHz 802.11a/n/ac 介面，帶內建天線。
- WiGig 晶片組 QCA6335。

## 復位按鈕 {#reset-button}

routerBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置和預設值。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路安全重灌 RouterOS 所需）。無論使用上述哪種選項，如果在裝置接通電源之前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內含以下隨裝置提供的附件：

- EU/US 開關電源 24V DC ⎓、0.8 A、9 W、Level VI、線纜：1.5 m。
- 帶遮蔽乙太網線纜/聯結器的 POE 注入器（RBPOE）。
- Cube 安裝支架。
- 用於 Cube 安裝支架的 K-70 緊固套件。

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS 軟體版本 *v6.47.2.*。具體的出廠預裝版本號顯示在 RouterOS 選單 /system resource 中。其他作業系統尚未經過測試。

## 說明 {#notes}

本裝置符合 ETSI 法規規定的最大發射功率限值。歐盟境內的頻率和最大發射功率列出如下：57-66GHz：34.92 dBm。60 GHz 頻段的工作模式：58.32 GHz、60.48 GHz、62.64 GHz。本裝置已透過認證，可用於戶外的點對多點應用。在以下國家/地區，本裝置不能用於固定點對點應用：

![](/img/01438e2d9209ce7d.webp)

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCCID</th></tr></thead><tbody><tr><td>CubeG-5ac60adpair</td><td>TV7CB5A60</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝環境中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能造成有害干擾，此時使用者需要自費糾正這種干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的權利。

本裝置符合 FCC 規則第 15 部分。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。

除 FCC CFR §15.255 (b) 中所列條件外，本裝置不得在飛機上執行。

**重要提示。FCC 輻射暴露宣告：** 本裝置符合 FCC 針對非受控環境所規定的輻射暴露限值。本裝置的安裝和執行應使輻射體與您的身體之間保持至少 21cm 的最小距離。用於連線外圍裝置的所有線纜必須遮蔽並接地。使用未遮蔽且未接地的線纜連線外圍裝置執行，可能會對無線電和電視接收造成干擾。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>CubeG-5ac60adpair</td><td>7442A-CB5A60</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 標準的免許可發射器/接收器。其執行須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

除 ISED RSS-210 附錄 J.1 中所列條件外，本裝置不得在飛機上執行。

本裝置不得在飛機上使用，除非符合 ISED RSS-210 附錄 J.1 中所列的條件。

**重要提示。IC 輻射暴露宣告：** 本裝置符合 IC RSS-102 針對非受控環境所規定的輻射暴露限值。本裝置的安裝和執行應使輻射體與您的身體之間保持至少 21cm 的最小距離。Cet équipement est conforme aux limites d'exposition aux rayonnements IC établies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé avec un minimum de 21cm de distance entre la source de rayonnement et votre corps.

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный каналы</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>5650-5850 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

有關裝置製造日期的資訊以斜槓分隔的形式標明在其標籤上的序列號末尾。第一位數字表示年份編號（年份的最後一位數字），其後兩位表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 (Norma Oficial Mexicana) {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5470-5725 МГц (27 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭境內使用，須按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議（2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）所批准的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Mikrotīkls SIA 特此宣告，無線電裝置型別 CubeG-5ac60adpair 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WiGig {#wigig}

<table><thead><tr><th>工作通道 / 最大輸出功率</th><th>58.32 GHz / &lt;40 dBm</th></tr></thead><tbody><tr><td>60.48 GHz / &lt;40 dBm</td><td></td></tr><tr><td>62.64 GHz / &lt;40 dBm</td><td></td></tr></tbody></table>

### WLAN {#wlan}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>5470-5725 MHz / 27 dBm</th></tr></thead></table>
