---
title: "FiberBox"
slug: /fiberbox
source: https://manual.mikrotik.com/hardware/fiberbox
captured_at: '2026-11-04T09:48:13+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### FiberBox (CRS105-5S-FB) {#fiberbox-crs105-5s-fb}

![](/img/9bbf101a7bc9df03.jpg)

Fiberbox 是一款帶五個 SFP 埠的室外交換器，非常適合因距離限制而無法使用普通乙太網線的場所。該裝置具備防風雨能力，隨附不鏽鋼卡箍和紮帶，可直接安裝在高桅杆和塔上。完整規格和宣傳冊請參見 [FiberBox 產品頁面](https://mikrotik.com/product/fiberbox)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵循所有國家和地方的法律法規。裝置的安裝必須符合當地和國家的電氣規範。本產品設計為室外安裝在立杆上。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體和配置或未遵循正確的操作流程，可能對人員造成危險並損壞系統。僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！如果裝置出現故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

![](/img/0a5239f68824311b.webp)

預設配置利用交換晶片功能來配置非管理型交換器。所有乙太網埠都被加入交換器組，預設 IP 地址為 192.168.88.1/24。

- 初始連線必須透過乙太網線，使用 MikroTik WinBox 工具完成。
- 使用 WinBox 從任意埠連線到預設 IP 地址 192.168.88.1，使用者名稱為 admin，密碼為空，裝置已設定為交換器（或對於某些型號，請檢視貼紙上的使用者和無線密碼）。
- 我們建議點選 "Check for updates" 按鈕，並將系統軟體更新到最新版本，以確保最佳效能和穩定性。
- 設定您的密碼以保護裝置。

## 安裝 {#mounting}

我們建議為我們的裝置使用 Cat6 遮蔽網線。

使用鋼製卡箍從裝置背面穿過。

![](/img/034816fd335cc080.webp)

固定到立杆上，並擰緊使其牢固。

![](/img/9db87c984f147b03.webp)

## 供電 {#powering}

裝置支援以下供電方式：

- 直接輸入電源（外徑 5.5 mm、內徑 2 mm，母頭，中心針為正極）接受 DC ⎓ 9-30 V DC；該裝置在最大負載下的功耗最高為 11 W。

## 配置 {#configuration}

除了本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：CRS3xx 和 CSS3xx 系列手冊。初始連線必須透過乙太網線，使用 MikroTik WinBox 工具完成。應使用 WinBox 從任意埠連線到預設 IP 地址 192.168.88.1，使用者名稱為 admin，密碼為空。出於恢復目的，可以從網路重新安裝裝置，請參見 MikroTik 有線介面相容性。使用帶有分離式 SFP+ 籠的裝置時，仍不建議將 S+RJ10 收發器彼此相鄰部署。請每隔一個介面使用 S+RJ10，以避免收發器過熱而導致不可預測的行為。作業系統支援

裝置支援 RouterOS v6。出廠預裝的具體版本號顯示在 RouterOS 選單 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送往指定的廢棄物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的相關流程。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制要求。這些限制旨在為商業安裝環境中的有害干擾提供合理防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能造成有害干擾，此時使用者需自費糾正干擾

FCC 警告：任何未經負責合規的一方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受收到的任何干擾，包括可能導致非預期執行的干擾。

注意：本裝置已在周邊裝置使用遮蔽線纜的情況下進行測試。為確保合規，必須在本裝置上使用遮蔽線纜。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期執行的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），隨後的兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## Norma Oficial Mexicana {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
