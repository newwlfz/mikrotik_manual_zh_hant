---
title: "MTP250 系列"
slug: /mtp250-series
source: https://manual.mikrotik.com/hardware/mtp250-series
captured_at: '2026-11-04T09:56:36+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **[MTP250-53V47-OD](https://mikrotik.com/product/mtp250_53v47_od)**
- **[MTP250-26V94-OD](https://mikrotik.com/product/mtp250_26v94_od)**
:::

![](/img/2b4511965afb07cb.jpg)

## 安全警告 {#safety-warnings}

- 在操作任何 MikroTik 裝置之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。
- 本裝置應由經過培訓的合格人員按照本安裝說明進行安裝。安裝人員負責確保裝置的安裝符合當地和國家的電氣規範。請勿嘗試拆卸、修理或改裝本裝置。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源介面卡從電源插座上拔下。
- 接觸 PSU 的時間為（&gt; 1 s 且 &lt; 10 s）。

## 資訊 {#information}

有關產品的技術規格、宣傳冊和更多資訊，如需配置或安裝方面的幫助，請諮詢顧問 [https://mikrotik.com/consultants](https://mikrotik.com/consultants)

## 供電 {#powering}

![](/img/8edf2db501c0252c.webp)

本裝置由交流電源供電：

輸入：100-240V ~ 50/60Hz。

![](/img/eac93f8f752cbbf0.webp)

輸出：

<table><thead><tr><th></th><th>MTP250-26V94-OD</th><th>MTP250-53V47-OD</th></tr></thead><tbody><tr><td>直流輸出電壓（V）</td><td>26</td><td>53</td></tr><tr><td>直流輸出電流（A）</td><td>9.4</td><td>4.7</td></tr><tr><td>直流輸出功率（W）</td><td>244</td><td>249</td></tr></tbody></table>

## 安裝 {#installation}

安裝時，直流輸出端請使用截面積至少為 1.2 平方毫米的銅線。在輸入端（100-240V ~ 50/60Hz），將 MTP250 系列 PSU 連線到 RCD。

![](/img/deb8f3ee0fe10f8b.webp)

## 安裝 {#mounting}

- 使用隨機提供的鋼製卡箍穿過孔洞，然後將裝置固定到桅杆上。

![](/img/ba5899411a242e56.webp)

- 或者使用隨機提供的螺絲將裝置固定到牆上，並根據牆體材質使用膨脹螺栓。

## 配件 {#accessories}

包裝內含：

CLAMP1-2_Hose Clamp SUS304（Philips 型；9mm；夾緊直徑範圍 25-70mm）配 EPE 袋。SET1_ K-77 緊固套裝。

## 執行環境 {#operation-environment}

工作溫度：-40°C 至 70°C

防護等級 - IP 67

![](/img/03de8c5343a96761.webp)

警告。警告宣告用於指出可能導致人身傷害或死亡的情況或操作。

## 產品上的符號 {#symbols-on-the-product}

產品上可能出現以下符號：

- 高壓：此符號表示高壓。它提醒您注意可能對您和其他操作本裝置的人員造成危險的專案或操作。請閱讀相關提示並仔細遵照說明操作。

![](/img/eba5b3f64c552590.webp)

- 不要將電子裝置作為未分類的城市垃圾處理。請使用單獨的回收設施，或聯絡購買本儀器的供應商。

![](/img/b8ac70bab39acb56.webp)

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制要求。這些限制旨在為商業安裝環境中的有害干擾提供合理防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能造成有害干擾，此時使用者需自費糾正干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的規定。其操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受所接收到的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與其他任何天線或發射器處於同一位置或協同工作。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。其操作須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR。允許在以下兩個條件下操作：(1) 裝置不得產生干擾，且 (2) 裝置使用者必須接受所受到的任何無線電干擾，即使該干擾可能影響其執行。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## Інформація для користувачів в Україні {#інформація-для-користувачів-в-україні}

Цей пристрій відповідає вимогам Технічного регламенту електромагнітної сумісності обладнання та Технічного регламенту низьковольтного електричного обладнання.

![](/img/7182f05dc1a2f3bc.webp)

Виробник гарантує, що даний пристрій безпечний при правильному використанні згідно з інструкцією.

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

86929
