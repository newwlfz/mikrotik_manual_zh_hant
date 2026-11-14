---
title: "CCR1009-7G-1C-1S+PC"
slug: /ccr1009-7g-1c-1s-plus-pc
source: https://manual.mikrotik.com/hardware/ccr1009-7g-1c-1s-plus-pc
captured_at: '2026-11-04T05:55:32+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/e9685d2eef55d87f.webp" alt="" width={799} height={377} /></p>

## [CCR1009-7G-1C-1S+PC](https://mikrotik.com/product/CCR1009-7G-1C-1SplusPC) {#ccr1009-7g-1c-1spc}

Cloud Core Router —— 每個完全獨立的乙太網埠都直接連線到 CPU。完整規格和宣傳冊請參見 [CCR1009-7G-1C-1S+PC 產品頁面](https://mikrotik.com/product/CCR1009-7G-1C-1SplusPC)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律法規進行處理。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計為安裝在機架中。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些均可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規。所有 MikroTik 裝置都必須由專業人員安裝。
- 本產品屬於 A 類產品。在居住環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。

## 快速開始 {#quickstart}

- 將您的 PC 連線到標有 **MGMT/BOOT** 的埠或第一個乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 應使用 Web 瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方式以確保可訪問性；**
- 在 Web 瀏覽器中開啟 192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 復位按鈕 {#reset-button}

**復位按鈕**：

- 在啟動期間按住此按鈕，直到 USER LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 按住復位按鈕併為裝置通電（等待 "USER" LED 閃爍後變為穩定的 "On"，當 "USER" LED 變為 "Off" 時鬆開復位按鈕）——裝置將以 BOOTP 模式啟動，以便使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。

無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。若只想載入備份 RouterBOOT 而不執行重設，請在 LED 開始閃爍之前鬆開按鈕。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內含以下隨裝置提供的配件：

- 歐盟/美國電源線，D03+QT3 H05VV-F 3x0.75 mm2 1.83 m RoHS。
- 電源介面卡 24VDC **⎓** 2.5 A 60 W 80% VI 121x54x33 線纜 1.2 m 插頭 2.1 mm。
- USB A 母頭轉 Micro B 線纜
- 用於 CRS110 機箱的機架安裝套件。請參閱 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

SFP 模組在使用時可能會變得非常熱，拔出時請格外小心，請參閱 SFP 模組通用使用指南：

[S+RJ10 通用指南](/docs/hardware/s-plus-rj10-general-guidance)

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/CCR1009-7G-1C-1SplusPC](https://mikrotik.com/product/CCR1009-7G-1C-1SplusPC)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未經過測試。

<p><Img src="/img/9451b2eb2e7bf01c.webp" alt="" width={576} height={521} /></p>

安全提示 觸電危險。本裝置只能由經過培訓的人員進行維修。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請熟悉在您所在地區將裝置正確運送到指定處置場所的相關流程。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制要求。這些限制旨在為商業安裝環境中的有害干擾提供合理防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在居住區執行本裝置很可能造成有害干擾，此時使用者需要自行承擔費用來糾正干擾。

FCC 警告：任何未經合規負責方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行須符合以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期執行的干擾。注意：本裝置已使用外圍裝置上的遮蔽電纜進行測試。為確保合規，必須在本裝置上使用遮蔽電纜。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。其執行須符合以下兩個條件：(1) 本裝置不得造成干擾，並且 (2) 本裝置必須接受任何干擾，包括可能導致本裝置非預期執行的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。允許在以下兩個條件下執行：(1) 裝置不得產生干擾，並且 (2) 使用者必須接受裝置所受到的任何無線電干擾，即使該干擾可能影響其正常執行。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置製造日期資訊以斜槓分隔的形式標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），後面兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

有關保修服務的詳細資訊，請聯絡您的經銷商。

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

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
