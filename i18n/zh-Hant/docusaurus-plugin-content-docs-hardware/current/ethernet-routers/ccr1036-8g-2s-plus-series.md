---
title: "CCR1036-8G-2S+ 系列"
slug: /ccr1036-8g-2s-plus-series
source: https://manual.mikrotik.com/hardware/ccr1036-8g-2s-plus-series
captured_at: '2026-11-04T05:55:41+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/44eeac550f5f7853.webp" alt="" width={799} height={506} /></p>

<p><Img src="/img/c0a2a206816d5024.webp" alt="" width={169} height={82} /></p>

:::info 本文涵蓋

- **[CCR1036-8G-2S+](https://mikrotik.com/product/CCR1036-8G-2Splus)**
- **[CCR1036-8G-2S+EM](https://mikrotik.com/product/CCR1036-8G-2SplusEM)**
:::

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。若未使用正確的硬體或未遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 本產品僅限室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 只能使用製造商認可的電源和附件，它們可在本產品的原包裝中找到。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 若裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座上拔下。
- 遵守當地國家法規是客戶的責任。所有 MikroTik 裝置必須由專業人員安裝。
- 本產品為 Class A 產品。在住宅環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

## 快速開始 {#quickstart}

- 將您的 PC 連線到標有 **MGMT/BOOT** 的埠或第一個乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定為 192.168.88.2/24；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保最佳效能、穩定性和安全更新；
- 設定路由器密碼。

## 供電 {#powering}

本裝置配有兩個可拆卸（支援熱插拔）的 AC **⏦** 110-240V 電源單元，採用標準 IEC 相容插座。最大功耗為 73 W。

## 復位按鈕 {#reset-button}

**復位按鈕**：

- 在啟動過程中按住此按鈕，直到 USER LED 燈開始閃爍，鬆開按鈕即可復位 RouterOS 配置。
- 按住復位按鈕並給裝置上電（等待 "USER" LED 閃爍後變為穩定的 "On"，當 "USER" LED 變為 "Off" 時 — 鬆開復位按鈕）— 裝置將以 BOOTP 模式啟動，使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。

無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。若只想載入備份 RouterBOOT 而不進行復位，請在 LED 開始閃爍前鬆開按鈕。這對於 RouterBOOT 偵錯和恢復非常有用。

## 安裝 {#mounting}

本裝置設計用於室內使用，可使用隨附的機架安裝件安裝在機架機箱中，也可放置在桌面上。如果指定用途為機架機箱，請使用十字螺絲刀將機架耳固定在裝置兩側：

<p><Img src="/img/27bf22aa32ecbced.webp" alt="" width={610} height={543} /></p>

- 如右圖所示，將機架耳固定到裝置兩側並用四顆螺釘擰緊；
- 將裝置放入機架機箱，對準孔位，使裝置方便安裝；
- 擰緊螺釘將其固定到位。

本裝置無防水保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 網線。

## LED 指示燈 {#leds}

本裝置有四個 LED 指示燈。PWR1/2 指示當前正在使用的電源。FAULT 指示散熱風扇出現問題。USER 可在軟體中進行配置。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體出廠預裝版本列於 /system resource 中。其他作業系統未經測試。

## PCIe 使用 {#pcie-usage}

M.2 插槽 PCIe 4x，安裝 SSD 請遵循以下說明：

- 關閉裝置（拔下電源線）；2. 擰下固定 CCR 上蓋的 6 顆螺釘；
- 開啟上蓋；
- 擰下固定 SSD 的螺釘；
- 將 SSD 插入 m.2 插槽；
- 接上電源線並檢查 SSD 是否正確初始化；
- 擰回 6 顆上蓋螺釘。另外請注意，預設情況下您應使用 m.2 2280 規格的 SSD。

CCR1036 型號的 M.2 插槽採用 PCIe Gen 2.0 x4 連線。推薦使用容量最高 1TB 的 NVMe M.2 2280mm M key SSD 硬碟。

<p><Img src="/img/9451b2eb2e7bf01c.webp" alt="" width={576} height={521} /></p>

安全提示 觸電危險。本裝置只能由受過培訓的人員維護。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置經測試，符合 FCC 規則第 15 部分對 Class A 數字裝置的限制要求。這些限制旨在為商業安裝環境中的有害干擾提供合理防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域操作本裝置很可能造成有害干擾，此時使用者將需要自費糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。注意：本裝置在測試時對周邊裝置使用了遮蔽電纜。為確保合規，必須在本裝置上使用遮蔽電纜。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。其操作須滿足以下兩個條件：(1) 本裝置不得產生干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置執行異常的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。其操作須滿足以下兩個條件：(1) 本裝置不得產生干擾；(2) 本裝置必須接受任何無線電干擾，即使該干擾可能導致裝置執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置製造日期資訊以斜槓分隔的形式標示在其標籤上序列號的末尾。第一位數字表示年份（年份的最後一位數字），隨後的兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的銷售商。

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## Norma Oficial Mexicana（墨西哥官方標準） {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其非預期執行的干擾。製造商：MikroTikls SIA, Unijas iela 2, Riga, LV-1039, 拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
