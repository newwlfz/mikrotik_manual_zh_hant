---
title: "GPeR"
slug: /gper
source: https://manual.mikrotik.com/hardware/gper
captured_at: '2026-11-04T09:49:32+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/e8f113e9ffa4a9cf.jpg)

千兆無源乙太網中繼器。完整規格和宣傳冊請參見 [GPeR 產品頁面](https://mikrotik.com/product/gper)。

## 連線 {#connecting}

- 將帶有供電的所需網線連線到 PoE in 乙太網埠，並透過 PoE out 延伸出去。
- 將網線連線到下一臺 GPeR 裝置或其他裝置。
- 檢查線路上的最終裝置，確認 PoE 相容性；如不需要，可使用跳線手動停用 PoE out，參見章節（連結）

## 供電 {#powering}

裝置需要透過乙太網埠供電：

- 乙太網埠接受無源 PoE 或 802.3af/at DC 24 - 57 V**⎓**。最大負載下的功耗可達 2 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網電纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的乙太網電纜連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

### 跳線用法 {#jumper-usage}

如果目標裝置不支援 PoE 供電，可以透過拔掉 "PoE out" 一側的兩個跳線來手動停用功率直通。只有當 "PoE in" 由無源 PoE 電源供電時，此方法才有效，因為 802.3af/at 交換器無法為 GPeR 本身供電。

![](/img/40a38cccc4464fb0.webp)

- 重新安裝跳線時，請注意如下圖所示的水平位置：當四個跳線全部連線時，GPeR 可在兩個方向上工作。

## 安裝 {#mounting}

本裝置設計為室內使用，本裝置的 IP 防護等級為 IPX0。可以使用裝置安裝支架上提供的螺絲孔將裝置固定在牆上。

在戶外使用時請使用防水外殼。[https://mikrotik.com/product/gper_ip67_case](https://mikrotik.com/product/gper_ip67_case)

![](/img/b5d6e1d2bbe79b6f.webp)

建議使用 Cat5/6 電纜。*本裝置的安裝和配置應由具備資質的人員完成。*

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 兩個千兆乙太網埠。

## LED 狀態 {#led-status}

裝置具有兩個 LED，用於指示每個已連線乙太網埠的工作狀態。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下附件：

- 帶螺絲和膨脹螺栓的安裝支架。

## 規格 {#specifications}

尺寸單位為毫米。

![](/img/8cd493f0b55ddbba.webp)

IP68 外殼可單獨購買，[https://mikrotik.com/product/gper_ip67_case](https://mikrotik.com/product/gper_ip67_case)

![](/img/5bef20a42d5210de.webp)

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/gper](https://mikrotik.com/product/gper)

## MikroTik 移動應用 {#mikrotik-mobile-app}

![](/img/8d294e5cd375c591.webp)

![](/img/9bcba09a7b6a0d53.webp)

使用 MikroTik 智慧手機應用，可透過 GPeR 在現場配置您的路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。掃描二維條碼並選擇您首選的作業系統。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供針對有害干擾的合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：未經合規負責方明確批准的任何更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得產生有害干擾，且 (2) 本裝置必須接受接收到的任何干擾，包括可能導致意外操作的干擾。注意：本裝置使用遮蔽電纜與外圍裝置進行了測試。必須使用遮蔽電纜與本裝置配合使用以確保合規。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可證 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得產生干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊以斜槓分隔的形式標在其標籤序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），其後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。

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

製造商：MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
