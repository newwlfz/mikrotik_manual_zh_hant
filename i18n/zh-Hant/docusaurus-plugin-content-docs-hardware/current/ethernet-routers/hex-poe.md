---
title: "hEX PoE"
slug: /hex-poe
source: https://manual.mikrotik.com/hardware/hex-poe
captured_at: '2026-11-04T05:58:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/5aab95e63cc4bcf0.jpg" alt="" width={800} height={509} /></p>

## [hEX PoE](https://mikrotik.com/product/RB960PGS) (RB960PGS) {#hex-poe-rb960pgs}

hEX PoE 是一款功能強大的五埠千兆乙太網路由器，配備 SFP 埠，可為其他裝置供電。完整規格和宣傳冊請參閱 [hEX PoE 產品頁面](https://mikrotik.com/product/RB960PGS)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置僅供室內使用，可放置在平坦表面上或安裝在牆上。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或未遵循正確的操作步驟，可能會給人員帶來危險並損壞系統。
- 請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可並可在本產品原包裝中找到的電源和配件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 選擇您的供電方案，請參閱“供電”部分了解如何連線；
- 裝置將啟動，在短促的蜂鳴聲之後，網路即可供連線；
- 將您的計算機 IP 配置設定為自動（DHCP）；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方法以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置專為室內使用而設計，可放置在平坦表面上或安裝在牆上，安裝孔位如下圖所示，包裝中不含螺釘。4x25 mm 的螺釘可以很好地適配，根據牆體結構，如有需要，您可以使用 6x30 mm 的脹塞和 6 mm 鑽頭。

<p><Img src="/img/fe1d555e6cb0e6db.webp" alt="" width={387} height={455} /></p>

安裝在牆上時，請確保線纜走向朝下。我們建議為我們的裝置使用 Cat6 線纜。本裝置的 IP 防護等級為 IPX0。

警告！本裝置安裝和操作時，裝置與人體之間應保持至少 20 cm 的距離。在居住環境中操作本裝置可能會造成無線電干擾。

## 供電 {#powering}

本裝置可透過電源插孔或第一個乙太網埠（Passive PoE）接受供電：

- 直流電源插孔直連（外徑 5.5mm、內徑 2mm，母頭，中心針為正極）可接受 12 - 57 V ⎓DC。
- 第一個乙太網埠可接受無源乙太網供電 12 - 57 V ⎓DC。
- 埠 2 - 5 支援 PoE 輸出。本裝置還支援無源 PoE 輸入以及無源或 802.3af/at PoE 輸出。乙太網埠 2-5 可以以與裝置所用相同的電壓為其他支援 PoE 的裝置供電。如果使用 48-57 V 輸入電壓，它可以為相容 802.3af/at mode B (4,5+)(7,8-) 的裝置供電。

本裝置在最大負載並連線外設時的功耗為 59 W。未連線外設時為 6 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線纜連線到 PoE 介面卡的 PoE 埠；
- 將來自您 LAN 的乙太網線纜連線到 PoE 介面卡的 LAN 埠，注意資料和電力流向的箭頭；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 電源輸出 {#power-output}

本裝置可透過其乙太網埠為外部裝置提供 PoE 供電。這很方便，因為您無需任何額外的 PoE 注入器即可為其他裝置供電。輸出電壓將與輸入電壓相同。在此模式下，每個乙太網埠的最大輸出功率為 1 A（所有埠的總最大值為 2 A）。一旦在 RouterOS 中啟用了電源輸出，乙太網 LED 會帶有紅色（綠色表示乙太網鏈路已建立，紅色表示有電但無鏈路，紅色和綠色同時亮起表示既有鏈路又有供電）。

## 配置 {#configuration}

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help)開始，以熟悉各種可能性。如果無法使用 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路啟動裝置，請參閱復位按鈕。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 本裝置有五個獨立的乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通或交叉線纜連線到其他網路裝置。
- 1G SFP 埠。
- USB Type-A 插槽。

請參閱 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按下按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並將所有介面橋接。
- 當 LED 熄滅（約 20 秒）後鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 所需）。

無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下配件：

<p><Img src="/img/55e089e53dfb2e7d.webp" alt="" width={274} height={153} /></p>

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/RB960PGS](https://mikrotik.com/product/RB960PGS)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 安全宣告 {#safety-notice}

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢物處置場所。請了解您所在地區將裝置妥善運輸至指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的保護，防止有害干擾。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉並重新開啟裝置來確定），則鼓勵使用者嘗試透過以下一項或多項措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。 FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致不良操作的干擾。

注意：本機在測試時外圍裝置使用了遮蔽電纜。必須使用遮蔽電纜與本機配合，以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須符合以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置不良操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置製造日期資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），隨後的兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
