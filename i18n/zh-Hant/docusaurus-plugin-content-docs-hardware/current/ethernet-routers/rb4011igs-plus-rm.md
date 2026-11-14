---
title: "RB4011iGS+RM"
slug: /rb4011igs-plus-rm
source: https://manual.mikrotik.com/hardware/rb4011igs-plus-rm
captured_at: '2026-11-04T06:04:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/ed0c534e70eccc5f.jpg" alt="" width={799} height={497} /></p>

## [RB4011iGS+RM](https://mikrotik.com/product/rb4011igs_rm) {#rb4011igsrm}

裝置已預配置基本設定，您只需插入 ISP 線纜即可開始使用網際網路。我們建議您設定密碼以保護裝置。完整規格和宣傳冊請參見 [RB4011iGS+RM 產品頁面](https://mikrotik.com/product/rb4011igs_rm)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家和地區的法律法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於安裝於機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟可能會對人員造成危險並損壞系統。
- 本產品設計用於室內安裝。請將本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員進行安裝。

## 快速開始 {#quickstart}

- 將您的網際網路線纜連線到第一個埠，將區域網路計算機連線到其他埠；
- 選擇您的供電方案，請參見供電部分；
- 將裝置連線到電源；
- 配置您的網路卡設定，使用 DHCP 自動獲取 IP 地址；
- 應使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，且沒有密碼（對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，並重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

最大負載下的功耗可達 33 W。裝置可透過電源插孔或第一個乙太網埠供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2.1 mm，母頭，正極插針插頭）接受 12-57 V DC。
- 第一個乙太網埠接受 18-57 V DC 的 PoE 供電。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線纜連線到 PoE 介面卡的 PoE 埠；
- 將來自區域網路的乙太網線纜連線到 PoE 介面卡的 LAN 埠，注意資料和電力流向的箭頭；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help) 開始，以熟悉各種可能性。如果無法建立 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從區域網路側透過裝置的 MAC 地址進行連線（預設情況下，來自網際網路埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參見復位按鈕。

## 安裝 {#mounting}

本裝置設計用於室內使用，可使用隨附的機架安裝件安裝在機架機箱中，也可以放置在桌面上。如果希望放置在平面上，請在路由器底部貼上橡膠墊腳；如果指定用於機架機箱，請使用十字螺絲刀在裝置兩側安裝機架耳：

<p><Img src="/img/eb1f9b6b39ade041.webp" alt="" width={627} height={558} /></p>

- 將機架耳安裝到裝置兩側，並擰緊四顆螺絲將其固定到位；
- 將裝置放入機架機箱並對齊孔位，使裝置能夠方便地安裝到位；
- 擰緊螺絲將其固定到位。

本裝置沒有防水汙染保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 線纜。*本裝置的安裝和配置應由合格人員完成。*

工作溼度可為 5% 至 95%，無冷凝。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 乙太網埠分為兩組，每組五個，每組透過一個交換晶片連線。埠可單獨配置，並支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通線或交叉線連線到其他網路裝置。
- SFP+ 埠接受 SFP 和 SFP+ 模組。請參閱 [MikroTik 有線介面相容性](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。
- RJ45 控制檯埠用於序列控制檯訪問，預設設定為 115200 bit/s，8 個數據位，1 個停止位，無校驗。

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置恢復為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並橋接所有介面。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置尋找 Netinstall 伺服器（透過網路安全重灌 RouterOS 時需要）。

無論使用上述哪種選項，如果在裝置通電前按住按鈕，系統將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下附件：

- EU/US 開關電源 DC ⎓ 24 V 1.5 A 36 W 87.4% VI 150 cm RA DC 插頭。
- K-60 緊固套件。DIN965，M3x6。
- 安裝套件 4011 rm 支架。

支援的 SFP 模組請參見 [MikroTik 有線介面相容性](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/rb4011igs_rm](https://mikrotik.com/product/rb4011igs_rm)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 安全提示 {#safety-notice}

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝環境中的有害干擾提供合理保護。

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能會導致有害干擾，在這種情況下，使用者需要自費糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改都可能使使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致不良操作的干擾。

注意：本裝置在外圍裝置上使用遮蔽線纜進行了測試。必須使用遮蔽線纜與本裝置配合，以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置不良操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置不得造成有害干擾；且
- 本裝置必須接受任何干擾，包括可能導致其非預期操作的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
