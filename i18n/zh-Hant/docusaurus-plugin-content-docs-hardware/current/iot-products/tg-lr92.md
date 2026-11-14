---
title: "TG-LR92"
slug: /tg-lr92
source: https://manual.mikrotik.com/hardware/tg-lr92
captured_at: '2026-11-04T10:06:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可下載為 <a href="/assets/files/tg-lr92-8a6d0117f62f9c262e34369cb2d654fe.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/e353c3e4f15fd23d.jpg)

雙頻（915MHz 和 2.4GHz），專為美國使用而設計。完整規格和產品手冊請參見 [TG-LR92 產品頁面](https://mikrotik.com/product/tg_lr92)。LoRa® 高精度、可溯源至 NIST 的溫度感測器節點

您可以在每個產品下的支援與下載部分找到軟體手冊 [https://mikrotik.com/products](https://mikrotik.com/products)

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 在任意牆面安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 未使用正確的硬體和配置，或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 我們無法保證因不當使用本裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 針對非受控環境制定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 概述 {#overview}

<table><thead><tr><th></th><th>TG-LR92</th></tr></thead><tbody><tr><td>溫度範圍</td><td>-20°C 至 +70°C</td></tr><tr><td>IP 等級</td><td>IP67</td></tr><tr><td>電池</td><td>1000mAh LiMn02</td></tr><tr><td>安裝方式</td><td>綁帶固定、M4 螺釘安裝</td></tr><tr><td>溫度感測器精度</td><td>在 -20°C 至 +70°C 範圍內為 +/-0.3°C（最大值），可溯源至 NIST</td></tr><tr><td>內建加速度計</td><td>否</td></tr><tr><td>磁鐵啟用</td><td>是</td></tr><tr><td>可選配 Crypto Authentication</td><td>是</td></tr><tr><td>尺寸</td><td>74 x 45 x 19mm</td></tr><tr><td>GNSS 掃描器</td><td>否</td></tr><tr><td>Wi-Fi 掃描器</td><td>否</td></tr><tr><td>LoRa® 915MHz</td><td>是</td></tr><tr><td>LoRa® 2.4GHz</td><td>是</td></tr></tbody></table>

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處理場所。請了解將裝置正確運送到您所在地區指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>TG-LR92</td><td>TV7-TGLR92</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝環境中的有害干擾提供合理防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝環境中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一項或多項措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或經驗豐富的無線電/電視技術人員以獲取幫助。**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分的要求。其操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受所接收到的任何干擾，包括可能導致意外操作的干擾。

*注：本機的外圍裝置使用遮蔽電纜進行了測試。必須使用遮蔽電纜與本機配合，以確保合規。*

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>TG-LR92</td><td>7442A-TGLR92</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 標準的免許可發射器/接收器。其操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置內含的免許可證發射器/接收器符合加拿大創新、科學與經濟發展部（ISED）針對免許可證無線電裝置適用的 CNR 標準。允許在以下兩個條件下執行：1）裝置不得產生干擾；2）裝置必須接受任何接收到的無線電干擾，即使該干擾可能導致裝置執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)
