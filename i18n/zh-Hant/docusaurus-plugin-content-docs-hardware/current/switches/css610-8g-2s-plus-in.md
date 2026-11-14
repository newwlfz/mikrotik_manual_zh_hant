---
title: "CSS610-8G-2S+IN"
slug: /css610-8g-2s-plus-in
source: https://manual.mikrotik.com/hardware/css610-8g-2s-plus-in
captured_at: '2026-11-04T09:47:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/76ea017a3909dedc.jpg)

八個 1G 乙太網埠和兩個用於 10G 光纖連線的 SFP+ 埠。便攜、強大且極具價效比——這款交換器堪稱經典！完整規格和宣傳冊請參見 [CSS610-8G-2S+IN 產品頁面](https://mikrotik.com/product/css610_8g_2s_in)。

CSS610-8G-2S+IN

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵守所有國家法律和法規。裝置的安裝必須符合當地和國家的電氣規範。本裝置設計用於安裝在機架中。請在開始安裝前仔細閱讀安裝說明。使用不正確的硬體或不遵循正確的操作步驟可能會導致對人員造成危險的情況以及對系統造成損壞。本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。請僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員進行安裝。

## 快速開始 {#quickstart}

- 從 [https://mikrotik.com/download](https://mikrotik.com/download) 下載最新的 SwitchOS 軟體版本；
- 將您的計算機連線到任意一個乙太網埠；
- 將裝置連線到電源；
- 將您計算機的 IP 地址設定為 192.168.88.3；
- 開啟您的 Web 瀏覽器，預設管理 IP 地址為 192.168.88.1 / 192.168.88.2，使用者名稱為 **admin**，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 透過 Web 瀏覽器將檔案上傳到 Upgrade 標籤頁，升級後設備將重啟；
- 設定您的密碼以保護裝置。

## 供電 {#powering}

裝置可從電源插孔或從第一個乙太網埠（Passive PoE）接受供電。

- 直接輸入電源插孔（外徑 5.5mm、內徑 2mm，母頭，中心正極插頭）可接受 12-57V DC。
- 第一個乙太網埠可接受 12-57V DC 的 passive PoE 輸入。
- 功耗 5 W，帶附件時為 11 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網電纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自您本地網路（LAN）的乙太網電纜連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

除了本文件中所述的內容之外，SwOS 還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 出於恢復目的，可以引導裝置進行重新安裝，請參閱“按鈕和跳線”一節。

首次配置：[CSS610 系列 SwOS 手冊](/docs/bridging-and-switching/swos/css610)；

裝置升級 [https://mt.lv/upgrade](https://mt.lv/upgrade)；

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 八個獨立的千兆乙太網埠，支援自動交叉/直通線纜連線（Auto MDI/X），因此您可以使用直通或交叉線纜連線到其他網路裝置；
- 2 個 SFP+ 埠，用於使用 10G SFP+；

## 規格 {#specifications}

請參見 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 安裝 {#mounting}

本裝置設計用於室內使用，可使用隨附的機架安裝件安裝在機架機箱中，也可以放置在桌面上。如果指定用途為機架機箱，請使用十字螺絲刀將機架掛耳安裝在裝置兩側：

- 將機架掛耳安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如圖所示。

![](/img/837a6d2bb5f312fe.webp)

- 將裝置放入機架機箱，並對齊孔位，以便裝置方便地安裝到位。
- 擰緊螺絲將其固定到位。本裝置不具備防水汙染保護，請確保將裝置放置在乾燥且通風的環境中。*本裝置的安裝和配置應由合格人員完成。* *我們建議為我們的裝置使用 Cat6 線纜。*

## 按鈕和跳線 {#buttons-and-jumpers}

在啟動期間按住此按鈕，直到 LED 燈開始閃爍。鬆開按鈕以重設 SwOS 配置並載入用於重新安裝和升級的備份軟體。

## 作業系統支援 {#operating-system-support}

本裝置執行 SwOS，這是本裝置唯一支援的作業系統。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場所處置。請熟悉將裝置正確運輸到您所在地區指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝提供合理的保護，防止有害干擾。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能造成有害干擾，在這種情況下，使用者將被要求自行承擔費用來糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致不良操作的干擾。

注意：本機在測試時外圍裝置使用了遮蔽電纜。本機必須使用遮蔽電纜以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置不良操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

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

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

EU 符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
