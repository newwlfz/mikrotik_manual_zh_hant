---
title: "CCR1016-12S-1S+"
slug: /ccr1016-12s-1s-plus
source: https://manual.mikrotik.com/hardware/ccr1016-12s-1s-plus
captured_at: '2026-11-04T05:55:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/25a9fbf9585b84ab.webp" alt="" width={800} height={320} /></p>

## [CCR1016-12S-1S+](https://mikrotik.com/product/CCR1016-12S-1Splus) {#ccr1016-12s-1s}

高效能 12 埠 SFP 雲核心路由器，帶一個 10G SFP+ 籠。完整規格和宣傳冊請參見 [CCR1016-12S-1S+ 產品頁面](https://mikrotik.com/product/CCR1016-12S-1Splus)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置 intended 安裝於機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能對人員造成危險情況並對系統造成損壞。
- 本產品僅供室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，操作風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將您的 PC 連線到標有 **MGMT/BOOT** 的埠或第一個乙太網埠；
- 將裝置連線到電源；
- 將您網路卡的 IP 設定配置為 192.168.88.2/24；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 192.168.88.1 以開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，然後在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

裝置支援由兩個冗餘電源供電，每個電源接受 100-240 V AC 電源。您可以只使用其中一個，也可以同時使用兩個。功耗最高可達 44 W。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 十二個 SFP 籠
- 一個 SFP+ 籠
- micro USB AB 型
- RS232 序列埠 Etherboot / Netinstall 可在埠 12 上使用。隨附一個 RJ45 SFP 轉乙太網模組用於管理連線。

## 安裝 {#mounting}

本裝置設計用於室內使用，可使用隨附的機架安裝件安裝在機架機箱中，也可以放置在桌面上。如果指定用於機架機箱，請使用十字螺絲刀將機架安裝耳固定到裝置兩側：

<p><Img src="/img/27bf22aa32ecbced.webp" alt="" width={610} height={543} /></p>

- 將機架耳固定到裝置兩側，並擰緊四顆螺絲將其固定到位，如圖所示。
- 將裝置放入機架機箱，對齊孔位，使裝置能夠方便地安裝。
- 擰緊螺絲將其固定到位。*本裝置沒有防水保護，請確保將裝置放置在乾燥通風的環境中。* *我們建議為我們的裝置使用遮蔽 Cat5/6 網線。* *本裝置的安裝和配置應由合格人員完成。*

## 按鈕和跳線 {#buttons-and-jumpers}

**Reset 按鈕**：

- 在啟動期間按住此按鈕，直到 USER LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置。
- 按住 Reset 按鈕並給裝置上電（等待 "USER" LED 閃爍後變為穩定 "On"，當 "USER" LED 為 "Off" 時鬆開 Reset 按鈕）——裝置將以 BOOTP 模式啟動，使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。

無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統將載入備份 RouterBOOT 載入程式。在 LED 開始閃爍之前鬆開按鈕，則僅載入備份 RouterBOOT 而不進行重設。這對於 RouterBOOT 偵錯和恢復非常有用。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 安全提示 {#safety-notice}

<p><Img src="/img/7ef0e65b341a324c.webp" alt="" width={574} height={494} /></p>

觸電危險。本裝置只能由經過培訓的人員進行維修。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已透過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的有害干擾防護。

本裝置會產生、使用並輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則建議使用者嘗試透過以下一種或多種措施來消除干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。FCC 警告：任何未經負責合規的一方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾，以及 (2) 本裝置必須接受所接收的任何干擾，包括可能導致非預期操作的干擾。注意：本裝置使用遮蔽電纜與外圍裝置一起進行了測試。必須使用遮蔽電纜與本裝置配合，以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得造成干擾，以及 (2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊，印在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的銷售商。

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其非預期執行的干擾。製造商：MikroTikls SIA, Unijas iela 2, Riga, LV-1039, 拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
