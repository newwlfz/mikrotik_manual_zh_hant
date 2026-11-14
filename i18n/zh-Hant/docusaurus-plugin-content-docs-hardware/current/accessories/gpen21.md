---
title: "GPEN21"
slug: /gpen21
source: https://manual.mikrotik.com/hardware/gpen21
captured_at: '2026-11-04T09:48:47+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/9c8119e8b8d823fd.jpg)

GPEN21 可以使用與 DC 輸入插孔相同的電壓，透過乙太網為支援 PoE 的裝置供電。完整規格和手冊請參見 [GPEN21 產品頁面](https://mikrotik.com/product/gpen21)。

## 供電 {#powering}

該裝置可透過直流輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，正極插頭）供電，12-57 V DC⎓。最大功耗 50 W。

## 電源輸出 {#power-output}

該裝置支援從蓋板下方的乙太網埠進行 PoE 輸出。您可以為支援被動式乙太網供電的 MikroTik 裝置供電。

GPEN21 具有乙太網埠和 SFP 埠，用於光纖連線。客戶可以選擇使用 GPEN21 為光模組供電，以便透過光纖上行至運營商，**或者提供 PoE** 為乙太網上行至運營商（使用我們的 GPeR 和/或 netPower 產品）供電，這兩者不能同時使用。

## Mode 按鈕 {#mode-button}

保留供將來使用。

## 安裝 {#mounting}

**步驟 1：**

-

使用 PH2 螺絲刀卸下蓋板螺絲；

-

取下蓋板以接觸安裝點。**步驟 2：**

-

使用鑽頭鑽孔；

-

如有需要，插入膨脹螺管；

-

將裝置安裝到牆上並用螺絲固定。步驟 1.步驟 2.

![](/img/c0ad2cbfa8e4ae4e.webp)

**步驟 3：**

- 插入連線到待供電裝置的乙太網線；
- 插入 GPEN 的電源。
- 輸出的乙太網線可以穿過位置 A 或 B 引入牆內。步驟 4：
- 重新裝回蓋板；
- 用螺絲固定蓋板；
- 使用貼紙遮蓋螺絲位置。

![](/img/72395d5cce047981.webp)

步驟 3.步驟 4. 在牆上安裝時，請確保線纜出口朝下。

## 重設與重新安裝 {#reset-and-reinstall}

GPEN21 內建備份 SwOS 韌體，可在標準韌體損壞或升級失敗時載入：

在裝置啟動時按住 Reset 按鈕幾秒鐘，將重設配置並載入備份韌體。Reset 按鈕位於前蓋板後面。載入備份韌體後，可以使用網頁瀏覽器連線到 192.168.88.1（或從 DHCP 伺服器獲取的地址）並安裝新的 SwOS 韌體。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的附件：

- K-62 螺絲套件包含四顆螺絲和用於牆面安裝的膨脹螺管。請參見 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 規格 {#specifications}

[https://i.mt.lv/cdn/product_files/GPEN_concept_200204.pdf](https://i.mt.lv/cdn/product_files/GPEN_concept_200204.pdf)

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供針對有害干擾的合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），建議使用者嘗試透過以下措施之一來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：未經合規責任方明確批准的任何更改或修改，可能會使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的規定。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。注意：本裝置在外圍裝置上使用遮蔽線纜進行了測試。必須使用遮蔽線纜連線本裝置以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
