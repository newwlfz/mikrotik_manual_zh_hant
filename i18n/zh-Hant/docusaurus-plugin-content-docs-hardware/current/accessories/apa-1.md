---
title: "APA-1"
slug: /apa-1
source: https://manual.mikrotik.com/hardware/apa-1
captured_at: '2026-11-04T09:39:52+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/d8c6ffdcc1e351be.jpg)

APA-1 是一款帶過壓保護及其他安全功能的汽車電源介面卡。完整規格和宣傳手冊請參見 [APA-1 產品頁面](https://mikrotik.com/product/apa_1)。這些功能可保護您的 LtAP 及其他裝置免受惡劣車載環境的損害。

## 安全警告 {#safety-warnings}

- 在對任何 MikroTik 裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。
- 本裝置應由經過培訓的合格人員按照本安裝說明進行安裝。安裝人員負責確保裝置安裝符合當地和國家的電氣規範。請勿嘗試拆卸、維修或改裝裝置。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。

## 資訊 {#information}

技術規格、宣傳手冊及更多產品資訊請訪問，如果您需要配置或安裝方面的幫助，請諮詢顧問 [https://mikrotik.com/consultants](https://mikrotik.com/consultants)

250

## 供電 {#powering}

- DC 輸入數量 1（3 針端子）；
- 最小電壓 12 V；
- 最大電壓 48 V；
- 帶負載時的最大功耗 100 W。

## 安裝 {#installation}

輸入與輸出連線方案：

- GND - DC 負極端子。
- IN - DC 正極端子。
- EN - 使能降壓轉換器：高電平（9-60VDC）= 開啟，低電平（0-1.2VDC）= 關閉，可與車輛點火開關配合以使能電壓轉換器，預設情況下跳線使能 **降壓** 轉換器。

![](/img/9f6d9f00f651daba.webp)

- PASS - 直通模式 - 經過保護電路後的輸入電壓，EN 輸入不影響 PASS 輸出。OUT 和 PASS 輸出可同時使用，但 3A 輸入保險絲限制了電流，因此輸出功率預算取決於輸入電壓水平。電壓選擇跳線方案：

![](/img/bd28cf5cd22c2c38.webp)

*按照圖片放置跳線以選擇適當的電壓。

## 安裝 {#mounting}

- 使用隨附的鋼製支架並用螺絲將其固定到牆上，將裝置固定在支架中。

![](/img/a6722750b90f425f.webp)

- 尺寸 86 x 16 x 31 mm。
- 工作溫度 -40°C 至 +85°C。

## 配件 {#accessories}

包裝內含：

- 緊韌體套裝。

## 產品上的符號 {#symbols-on-the-product}

![](/img/34b0a3ea7ac8712d.webp)

產品上可能出現以下符號：

- 表面可能變熱。
- CE 標誌。
- 請勿將電子裝置作為未分類的城市垃圾處理。請使用單獨的回收設施或聯絡購買本儀器的供應商。

![](/img/b8ac70bab39acb56.webp)

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝環境中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能造成有害干擾，在這種情況下，使用者將被要求自行承擔費用來糾正干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的規定。其操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致非期望操作的干擾。本裝置及其天線不得與任何其他天線或發射器共址或聯合執行。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。其操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置非期望操作的干擾。

本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR。允許在以下兩個條件下操作：(1) 裝置不得產生干擾，且 (2) 裝置使用者必須接受所受到的任何無線電干擾，即使該干擾可能影響其執行。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其非預期執行的干擾。製造商：MikroTikls SIA, Unijas iela 2, Riga, LV-1039, 拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

![](/img/6296cd0d81e0e5d3.webp)

製造商：MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
