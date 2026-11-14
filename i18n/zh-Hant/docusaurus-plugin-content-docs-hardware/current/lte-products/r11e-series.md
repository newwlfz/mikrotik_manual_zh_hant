---
title: "R11e 系列"
slug: /r11e-series
source: https://manual.mikrotik.com/hardware/r11e-series
captured_at: '2026-11-04T09:59:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/12c9810b3d1b4f4a.webp)

![](/img/87aa80d03beafd23.webp)

 R11e-LTE-US 是一款 Cat-4 調變解調器。它可以整合到任何帶有 miniPCI-e 插槽的 MikroTik 產品中。

:::info 本文涵蓋

- **R11e-LTE-US**
- **R11e-LTE**
- **R11e-4G**
- **R11e-LTE6**
:::

## 規格 {#specifications}

- 介面 – Mini-PCIe；
- 工作溫度 -30°C .. +70°C
- LTE 通道頻寬：1.4/3/5/10/15/20 MHz
- LTE 類別：4（150Mbps 下行，50Mbps 上行）
- 3G 類別：R7（Cat14 - 21.1Mbps 下行）
- LTE (FDD) 頻段：2/4/5/12 (1900/1700/850/700)
- 3G 頻段：2/5 (1900/850)

## 在裝置中安裝模組 {#installing-the-module-in-your-device}

R11e-TE-US 供專業使用。每張卡均採用 ESD 保護包裝。處理電氣裝置時，請遵守以下安全預防措施：

- 在拆包和處理電氣元件時使用腕部接地帶，以避免靜電放電（ESD）損壞；
- 拆包後，將卡放在防靜電墊上；
- 安裝時，確保沒有可能損壞或接觸 PCB 板的物體；
- 可以使用 PCB 板上出廠提供的螺絲孔將卡安裝到所需裝置中；
- 在裝置上找到 miniPCIe 插槽；
- 擰下兩個出廠附帶的螺絲；
- 可選地，您可以將導熱墊放在卡下方使用，包裝中不包含導熱墊；
- 將模組安裝到 miniPCIe 插槽，並用之前拆下的螺絲固定。擰緊扭矩 0,3 Nm；
- 將天線線纜連線到模組上的接頭：

![](/img/9130264c604e84bd.webp)

在戶外安裝時，請確保裝置外殼防水且專為戶外使用設計。*本裝置的安裝和配置應由合格人員完成。*

## 配置 {#configuration}

在由 MikroTik RouterOS 驅動的裝置中使用時，該裝置會被自動識別。配置可以在“Wireless”選單中設定。有關 LTE 配置的更多資訊，請參閱我們的文件：[LTE/5G 手冊](/docs/mobile-networking/lte-5g)

該裝置已使用 RouterOS v6 及以上版本進行測試。它可能與其他作業系統相容，但卡中不包含驅動程式。

## 作業系統支援 {#operating-system-support}

該模組支援 RouterOS。其他作業系統尚未測試。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>R11e-LTE-US</td><td>TV7R11ELTE</td></tr><tr><td>R11e-LTE</td><td>無</td></tr><tr><td>R11e-4G</td><td>TV7R11E4G</td></tr><tr><td>R11e-LTE6</td><td>TV7R11ELTE6</td></tr></tbody></table>

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝中的有害干擾提供合理保護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，不能保證特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種措施來糾正干擾：

- 重新調整或移動接收天線。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：未經合規責任方明確批准的任何更改或修改都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。本裝置及其天線不得與任何其他天線或發射器共置或協同執行。

**重要：射頻輻射暴露。**

天線與職業使用者之間必須保持至少 0,29m 的距離，與公眾之間必須保持 0,64m 的距離。在此配置下，可滿足 FCC 針對普通人群/非受控環境規定的輻射暴露限值。

**天線安裝警告**

安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用經產品認證的天線。根據 FCC 規則 CFR47 part 15.204，明確禁止使用任何未經產品認證的天線。安裝人員應根據國家法規和天線型別配置天線的輸出功率水平。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>R11e-LTE-US</td><td>7442A-R11ELTE</td></tr><tr><td>R11e-LTE</td><td>無</td></tr><tr><td>R11e-4G</td><td>7442A-R11E4G</td></tr><tr><td>R11e-LTE6</td><td>7442A-R11ELTE6</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。執行須滿足以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。其執行獲准須滿足以下兩個條件：(1) 裝置不得產生干擾，且 (2) 使用者必須接受裝置受到的任何無線電干擾，即使該干擾可能影響其正常執行。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## 致 OEM 整合商的重要通知 {#important-notice-to-oem-integrators}

-

本模組僅限 OEM 安裝。

-

根據 Part 2.1091(b)，本模組僅限安裝於移動或固定應用。

-

所有其他執行配置均需要單獨批准，包括就 Part 2.1093 而言的行動式配置以及不同的天線配置

## UKCA 標記 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>E-GSM-900</th><th>900 MHz / 33dB</th></tr></thead><tbody><tr><td>DCS-1800</td><td>1800 MHz / 30dB</td><td></td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 24dB ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 24dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1700 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dB ± 2.7 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大 LTE 發射功率限值。有關更詳細的資訊，請參閱上文的符合性宣告。
