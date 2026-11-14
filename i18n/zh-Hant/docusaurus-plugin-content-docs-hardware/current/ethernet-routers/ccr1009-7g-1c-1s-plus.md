---
title: "CCR1009-7G-1C-1S+"
slug: /ccr1009-7g-1c-1s-plus
source: https://manual.mikrotik.com/hardware/ccr1009-7g-1c-1s-plus
captured_at: '2026-11-04T05:55:31+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/b1bedc61824dd47e.webp" alt="" width={798} height={508} /></p>

## [CCR1009-7G-1C-1S+](https://mikrotik.com/product/CCR1009-7G-1C-1Splus) {#ccr1009-7g-1c-1s}

1U 機架式，7x 千兆乙太網，1x Combo 埠（SFP 或千兆乙太網），1xSFP+ 插槽，9 核 x 1.2 GHz CPU，2GB RAM，LCD 面板，雙電源，SmartCard 插槽，RouterOS L6。完整規格和宣傳冊請見 [CCR1009-7G-1C-1S+ 產品頁面](https://mikrotik.com/product/CCR1009-7G-1C-1Splus)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置應安裝在機架中。開始安裝之前，請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作程式可能會對人員造成危險並損壞系統。
- 本產品僅供室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些電源和配件可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規。所有 MikroTik 裝置必須由專業人員安裝。
- 本產品為 A 類產品。在家庭環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。

## 快速開始 {#quickstart}

- 將您的 PC 連線到標有 **MGMT/BOOT** 的埠或第一個乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 配置應使用 Web 瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方法以確保可訪問性；**
- 在 Web 瀏覽器中開啟 192.168.88.1 開始設定。如果 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 復位按鈕 {#reset-button}

**復位按鈕**：

- 在啟動期間按住此按鈕，直到 USER LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 按住復位按鈕並開啟裝置電源（等待 "USER" LED 閃爍後變為穩定 "On"，當 "USER" LED 變為 "Off" 時鬆開復位按鈕）- 裝置將以 BOOTP 模式啟動，使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復實用程式的資訊，請參閱 RouterOS 文件。

無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入程式。在 LED 開始閃爍之前鬆開按鈕，則僅載入備份 RouterBOOT 而不進行重設。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下附件：

- 兩根 EU/US AC **⏦** 電源線，D03+QT3 H05VV-F 3x0.75 mm 2 1.83 m RoHS。
- 機架式機箱 K-10 的固定套件。
- 兩個機架式機箱側支架。
- USB A 母頭到 Micro B 線纜。請參閱 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/CCR1009-7G-1C-1Splus](https://mikrotik.com/product/CCR1009-7G-1C-1Splus)

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未經過測試。

<p><Img src="/img/9451b2eb2e7bf01c.webp" alt="" width={576} height={521} /></p>

安全提示：觸電危險。本裝置僅應由經過培訓的人員進行維修。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請熟悉將裝置正確運輸至您所在地區指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝提供合理的保護，防止有害干擾。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置可能會導致有害干擾，此時使用者需要自行承擔費用來糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾，(2) 本裝置必須接受收到的任何干擾，包括可能導致非預期操作的干擾。注意：本裝置已使用外圍裝置上的遮蔽電纜進行測試。必須使用遮蔽電纜與本裝置配合使用，以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得造成干擾，(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
