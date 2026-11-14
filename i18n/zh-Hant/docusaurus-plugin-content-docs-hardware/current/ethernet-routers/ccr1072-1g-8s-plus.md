---
title: "CCR1072-1G-8S+"
slug: /ccr1072-1g-8s-plus
source: https://manual.mikrotik.com/hardware/ccr1072-1g-8s-plus
captured_at: '2026-11-04T05:55:42+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/ddd559ea1f682111.webp" alt="" width={799} height={450} /></p>

## [CCR1072-1G-8S+](https://mikrotik.com/product/CCR1072-1G-8Splus) {#ccr1072-1g-8s}

CCR1072-1G-8S+ 是一款配備八個 SFP+ 籠口的高效能多核路由器。埠直接連線到 Tilera 72 核 CPU，並由 16 GB 內建 ECC RAM 輔助。請參閱 [CCR1072-1G-8S+ 產品頁面](https://mikrotik.com/product/CCR1072-1G-8Splus) 獲取完整規格和宣傳冊。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置擬安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟可能會對人員造成危險情況並損壞系統。
- 本產品擬在室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規。所有 MikroTik 裝置必須由專業人員安裝。
- 這是 A 類產品。在家庭環境中，本產品可能會造成無線電干擾，在這種情況下，使用者可能需要採取適當的措施。

## 快速開始 {#quickstart}

- 將您的 PC 連線到標有 **MGMT/BOOT** 的埠或第一個乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 應使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 192.168.88.1 開始設定。如果 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可以確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內，可使用隨附的機架安裝件安裝在機架式機箱中，也可以放置在桌面上。如果指定用於機架式機箱，請使用十字螺絲刀將機架耳片安裝到裝置兩側：

- 將機架耳片安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如右圖所示；
- 將裝置放入機架式機箱並對齊孔位，使裝置能夠方便地安裝；
- 擰緊螺絲將其固定到位。

<p><Img src="/img/27bf22aa32ecbced.webp" alt="" width={610} height={543} /></p>

本裝置沒有防水汙染保護，請確保將裝置放置在乾燥通風的環境中。我們建議為我們的裝置使用 Cat6 網線。*本裝置的安裝和配置應由合格人員完成。*

## 供電 {#powering}

本裝置配備兩個可拆卸（支援熱插拔）的 AC **⏦** 110-240V (2.5 A) 電源單元，採用標準 IEC 相容插座，最大功耗為 125 W。

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，讓自己熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都被阻止）。出於恢復目的，可以啟動裝置進行重新安裝，請參閱 Reset 按鈕。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 2 個 M.2 插槽，可接受 80mm Key-M x4 PCIe 2.0 模組。M.2 插槽位於裝置內部的 PCB 板上。要接觸它們，請拆下路由器背面用於固定上蓋的螺絲，然後向上抬起並向蓋子方向拉動即可滑出。
- microSD 卡插槽。
- 用於儲存私鑰的 Smart Card 插槽。
- 1 個千兆乙太網埠。
- 8 個 SFP+ 埠，用於 10 Gb 連線。
- A 型 USB 插槽。
- AB 型 microUSB 插槽。
- 自動風扇轉速控制。CCR1072 具有連線到兩個 M.2 插槽的 PCIe Gen 2.0 x4 連線。建議使用容量最高 1TB 的 NVMe M.2 2280mm M key SSD 磁碟。

## Reset 按鈕 {#reset-button}

**Reset 按鈕**：

- 在啟動期間按住此按鈕，直到 USER LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 按住 Reset 按鈕並給裝置上電（等待 "USER" LED 閃爍後穩定為 "On"，當 "USER" LED 為 "Off" 時鬆開 Reset 按鈕）——裝置將以 BOOTP 模式啟動，使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。

無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。在 LED 開始閃爍前鬆開按鈕，即可僅載入備份 RouterBOOT 而不進行重設。這對 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的配件：

- EU/US AC **⏦** 電源線，D03+QT3 H05VV-F 3x0.75 mm 2 1.83 m RoHS。
- 用於機架式機箱 K-10 R2 的固定套件。
- Rackmount Case x72 側支架。請參閱 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/CCR1072-1G-8Splus](https://mikrotik.com/product/CCR1072-1G-8Splus)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未經過測試。

<p><Img src="/img/7ef0e65b341a324c.webp" alt="" width={574} height={494} /></p>

安全提示 電擊危險。本裝置只能由受過培訓的人員進行維修。這是 A 類裝置，在住宅無線電裝置附近操作可能會造成無線電干擾。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解將裝置正確運送到您所在地區指定處置場所的相關程式。

<p><Img src="/img/b412fabac7661e64.webp" alt="" width={591} height={196} /></p>

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期的資訊以斜槓分隔的形式標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），接下來的兩位數字表示週數。

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
