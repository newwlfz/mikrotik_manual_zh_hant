---
title: "mANT 系列"
slug: /mant-series
source: https://manual.mikrotik.com/hardware/mant-series
captured_at: '2026-11-04T06:01:36+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **mANT 19S** (MTAS-5G-19D120)
- **mANT 15s** (MTAS-5G-15D120)
:::

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。在將系統連線到電源之前，請閱讀安裝說明。本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責就安裝結構的完整性取得當地主管部門/檢驗部門要求的任何當地或國家安全檢查。在任何牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。裝置的安裝必須符合當地和國家的電氣規範。本裝置設計為安裝在室外的立杆上。開始安裝之前，請仔細閱讀安裝說明。**未使用正確的硬體和配置或未遵循正確的操作步驟，可能對人員造成危險情況並對系統造成損壞。** 我們無法保證因不當使用天線而不會發生事故或損壞。請小心使用本產品，風險自負。**當使用連線到 MikroTik 裝置的天線時，為確保符合當地法規，裝置需要升級到 RouterOS v6.48.3 或最新版本。**

客戶有責任遵守當地國家的法規，包括在合法的頻段內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電天線必須由專業人員安裝。

mANT 是一款帶有兩個 RP-SMA 聯結器的雙極化天線，有兩種尺寸：15dBi 型號和 19dBi 型號。兩款天線的波束寬度均為 120 度

## 首次使用 {#first-use}

- 用手擰下蓋板螺絲；
- 開啟蓋子；
- 將線纜連線到天線的 RP-SMA 聯結器；
- 確保裝置已斷電，然後將線纜連線到裝置；
- 安裝並固定元件。

## 安裝 {#mounting}

**mANT 15s** 配備 QuickMount 轉接件，可使用隨附的螺絲將其固定在牆上，或使用隨附的金屬安裝環將其固定在立杆上。透過 QuickMount 可以對天線進行水平和垂直調節。

- 將快裝支架安裝到天線背面。

<p><Img src="/img/45d623b2886f4717.webp" alt="" width={592} height={798} /></p>

<p><Img src="/img/f1b9c851a1837362.webp" alt="" width={560} height={786} /></p>

- 將天線安裝到立杆上。
- 使用隨附的鋼製卡箍將其固定。夾緊直徑 35 – 70 mm。

<p><Img src="/img/006d6b97c4c91436.webp" alt="" width={389} height={330} /></p>

- 請避免將鬆動的乙太網線纜連線到乙太網埠，請將線纜固定在牆壁或立杆上，以免線纜的重量拉扯埠。建議將乙太網線纜固定在天線 2m 以內的位置。這樣可以確保線纜不會因其重量而損壞埠，也不會脫落。我們建議使用 Cat6 遮蔽線纜。

**mANT 19s** 配備金屬立杆支架，可夾緊在金屬立杆上。

- 將安裝底座安裝到天線背面。
- 使用安裝支架將天線安裝到立杆上。
- 用支架和螺絲固定天線。

<p><Img src="/img/605f9373d3b55718.webp" alt="" width={610} height={828} /></p>

- 調整所需的方位。

請避免將鬆動的線纜連線到聯結器，請將線纜固定在牆壁或立杆上，以免線纜的重量拉扯埠。建議將線纜固定在天線 2m 以內的位置。這樣可以確保線纜不會因其重量而損壞聯結器，也不會脫落。

配件可單獨購買：

Flex-guide

<p><Img src="/img/beb93a76913dfa9e.webp" alt="" width={139} height={111} /></p>

## 接地 {#grounding}

安裝基礎設施（塔架和桅杆）以及路由器本身都必須妥善接地。天線在機殼門後設有一個接地線連線螺絲。將接地線連線到接地螺絲，然後將接地線的另一端連線到已接地的桅杆上。這可大幅降低靜電（ESD）和雷擊損壞的風險。

<p><Img src="/img/f5b76b224e6106fb.webp" alt="" width={414} height={320} /></p>

天線帶有一個接地連線點（標記為 ⏚）。

## 開啟蓋子 {#opening-cover}

要開啟蓋子，請用手逆時針旋轉松不脫螺絲並將其掀起。

<p><Img src="/img/c9aa40a174a2b89d.webp" alt="" width={310} height={220} /></p>

## 隨附部件 {#included-parts}

<p><Img src="/img/2da781ba7a16e5d7.webp" alt="" width={540} height={215} /></p>

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊，以斜槓分隔的形式標示在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），後面兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## Norma Oficial Mexicana {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：Mikrotīkls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
