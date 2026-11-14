---
title: "TG-LR82"
slug: /tg-lr82
source: https://manual.mikrotik.com/hardware/tg-lr82
captured_at: '2026-11-04T10:05:59+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可下載為 <a href="/assets/files/tg-lr82-69720aecca1b4446c1872862e03183cb.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/644b30fc44ce8252.jpg)

雙頻（868MHz 和 2.4GHz）。完整規格和宣傳冊請參見 [TG-LR82 產品頁面](https://mikrotik.com/product/tg_lr82)。LoRa® 高精度、可溯源至 NIST 的溫度感測器節點

軟體手冊可在各產品頁面的“支援”與“下載”部分找到 [https://mikrotik.com/products](https://mikrotik.com/products)

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的常規做法。
- 本產品的最終處置應依照所有國家法律和法規進行。
- 在任何牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 未使用正確的硬體和配置，或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 我們無法保證因不當使用本裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 客戶有責任遵守當地國家/地區的法規，包括在合法的頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 概述 {#overview}

<table><thead><tr><th></th><th>TG-LR82</th></tr></thead><tbody><tr><td>溫度範圍</td><td>-10°C 至 +70°C</td></tr><tr><td>IP 等級</td><td>IP65</td></tr><tr><td>電池</td><td>1100mAh LiMn02</td></tr><tr><td>安裝方式</td><td>綁帶固定、M4 螺釘固定</td></tr><tr><td>溫度感測器精度</td><td>-20°C 至 +70°C 範圍內為 +/-0.3°C（最大），可溯源至 NIST</td></tr><tr><td>內建加速度計</td><td>是</td></tr><tr><td>磁鐵啟用</td><td>是</td></tr><tr><td>尺寸</td><td>74 x 45 x 19mm</td></tr><tr><td>LoRa® 868MHz/915MHz</td><td>是</td></tr><tr><td>LoRa® 2.4GHz</td><td>是</td></tr></tbody></table>

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢棄物處置場。請了解將裝置正確運送到您所在地區指定處置場的相關程式。

## UKCA 標識 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊，以斜槓分隔的形式標註在裝置標籤序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），其後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

如需瞭解保修服務的詳細資訊，請聯絡您的經銷商。

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，且。
- 本裝置必須接受任何干擾，包括可能導致其非預期執行的干擾。製造商：MikroTikls SIA, Unijas 2, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

![](/img/7182f05dc1a2f3bc.webp)

烏克蘭國家通訊和資訊國家監管委員會 製造商：MikroTikls SIA，Unijas 2, Рига, Латвія, LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭境內使用須按照 2012 年 11 月 1 日第 559 號 NKРЗІ 決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）所規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA，Unijas 2, Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 TG-LR82 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

<table><thead><tr><th>（EN）工作頻率 / 最大輸出功率（DE）工作頻率 / 最大輸出功率（FR）工作頻率 / 最大輸出功率（IT）工作頻率 / 最大輸出功率（ES）工作頻率 / 最大輸出功率（RU）工作頻率 / 最大輸出功率</th><th>LoRa</th><th>2400-2483.5 MHz / 14 dBm</th></tr></thead><tbody><tr><td>LoRa</td><td>863-870 MHz / 14 dBm</td><td></td></tr></tbody></table>
