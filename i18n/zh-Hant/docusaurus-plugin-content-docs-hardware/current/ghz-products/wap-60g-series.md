---
title: "wAP 60G 系列"
slug: /wap-60g-series
source: https://manual.mikrotik.com/hardware/wap-60g-series
captured_at: '2026-11-04T10:06:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/wap-60g-series-9b51ea18dc11beafdef583ebaff01300.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

:::info 本文涵蓋

- **[Wireless Wire](https://mikrotik.com/product/wireless_wire)** (RBwAPG-60adkit)
- **[wAP 60G](https://mikrotik.com/product/wap_60g)** (RBwAPG-60ad)
- **[wAP 60G AP](https://mikrotik.com/product/wap_60g_ap)** (RBwAPG-60ad-A)
- **wAP 60Gx3 AP** (RBwAPG-60ad-SA)
:::

wAP60G 裝置工作在 60GHz 無線頻段，這些裝置的工作溫度範圍為 -40°C 至 +70°C。裝置配有千兆乙太網埠，可透過電源插孔或乙太網供電。裝置可以安全地安裝在牆壁、天花板或立柱/桅杆上。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 在任意牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適合安裝在戶外立柱上，但也可以在室內安裝。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體和配置或未遵循正確的操作步驟，可能會導致人員危險和系統損壞。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因裝置使用不當而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座上拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能會造成無線電干擾，在這種情況下，使用者可能需要採取適當的措施。

## 快速開始 {#quickstart}

- 使用乙太網線將裝置連線到隨附的 PoE 注入器的資料+電源端；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 下載 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 預設 IP：192.168.88.1，使用者名稱：**admin**，沒有密碼，請在標籤上查詢密碼；
- 將您計算機的 IP 地址設定為 192.168.88.2；
- 如果 IP 連線不可用，請使用 Neighbors 標籤頁並透過 MAC 地址連線；
- 連線後配置裝置，使其具有有效的網際網路連線 [https://mt.lv/configuration](https://mt.lv/configuration)；
- 將 RouterOS 軟體升級到最新版本 [https://mt.lv/upgrade](https://mt.lv/upgrade)；
- 選擇您所在的國家，以應用國家法規設定；
- 根據使用型別將 *Installation* 設定為室內或室外；
- 保護您的裝置並設定強密碼；
- 有關更多配置資訊，請訪問 [W60G 介面手冊](/docs/wireless/w60g)；
- wAP60G AP 裝置預配置為 WISP Bridge 預設配置；
- Wireless Wire 和 wAP60G 裝置預配置為 PTP Bridge 預設配置；
- Wireless Wire 裝置已隨機生成匹配的 SSID 和無線密碼。

## 供電 {#powering}

這些裝置既可以透過電源介面卡供電，也可以透過乙太網埠供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，正極插針）接受 12-57 V DC。
- 乙太網埠接受 PoE 輸入 12-57 V DC（無源和 802.3af/at）。包裝盒內包含電源介面卡和無源 PoE 注入器。如果使用 PoE 注入器，請確保使用 "Power + Data" 聯結器連線 wAP60G 裝置，使用 "Data" 聯結器連線路由器或交換器。

## 配置與連線 {#configuration-and-connecting}

完整的 RouterOS 文件位於此處：[https://mt.lv/help](https://mt.lv/help) 具體的 wAP 60G 配置可在 [W60G 介面手冊](/docs/wireless/w60g) 中找到。透過連線乙太網埠訪問裝置，然後使用 MikroTik WinBox 實用程式進行連線。出於恢復目的，可以從網路引導裝置，請參閱相應章節。如果 IP 連線不可用，也可以使用 WinBox 實用程式連線到裝置的 MAC 地址。

## 安裝 {#mounting}

**安裝在桅杆或立柱上：**

![](/img/cbb89d9ff7c5f201.jpg)

**建議使用電工膠帶以增加材料之間的摩擦力。**

- 將塑膠紮帶穿過孔洞固定到鋼製支架上。
- 將支架安裝到裝置上。
- 用螺絲固定。
- 將裝置安裝並校準到立柱或桅杆上。
- 將乙太網線穿過開口並連線到乙太網埠。
- 關閉底部鎖釦並用螺絲固定。建議使用紮帶將乙太網線固定到立柱上。與裝置的距離約為 30 cm。

![](/img/42ebcb18fdb0e686.webp)

**將裝置安裝在牆上：**

- 使用隨附的模板標記鑽孔位置。如有需要，也標記乙太網線孔位。請相應校準，這將取決於裝置最終如何安裝。
- 如有需要，插入膨脹螺栓，這取決於牆體結構和材質。
- 將隨附的鋼製支架放置在牆上。
- 使用螺絲將其固定到位。
- 將您的乙太網線穿過開口並連線到乙太網埠。
- 將裝置安裝到鋼製支架上
- 用螺絲將其固定到位。
- 關閉底部鎖釦。

避免將裝置安裝在低窪處，因為您將無法安裝和關閉底部鎖釦。

**安裝在天花板上：**

![](/img/35cd19164cabfd89.webp)

包裝中包含一個專用支架，用於安裝在天花板上。由於它由兩部分組成，需要固定在天花板吊頂板的兩側。

-

使用模板標記孔位。

-

將兩個安裝支架放置在標記位置。

-

使用螺絲將它們固定在一起。如果安裝在牆上，請以相同方式繼續組裝。

-

將您的乙太網線穿過開口並連線到乙太網埠。

-

將裝置安裝到鋼製支架上。

-

用螺絲將其固定到位。

-

關閉底部鎖釦。

## 底蓋 {#bottom-lid}

- 底蓋由防脫落螺絲固定到位。
- 使用 Philips PH2 螺絲刀將其擰鬆，但不要完全擰下螺絲。

![](/img/b67c9df3c35b1165.webp)

- 朝遠離裝置的方向拉動蓋子以將其取下。

![](/img/0430222d528f3356.webp)

- 重新組裝。

## 按鈕和跳線 {#buttons-and-jumpers}

routerBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，以將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，以清除所有配置並恢復預設值。
- 當 LED 不再亮起（約 20 秒）後鬆開按鈕，使裝置查詢 Netinstall 伺服器（透過網路安全重灌 RouterOS 所需）。無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都會載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 隨附物品 {#included-items}

![](/img/fea8eac2c986b2cc.webp)

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列在 /system resource 中。其他作業系統尚未經過測試。

## 說明 {#notes}

本裝置符合 ETSI 法規規定的最大發射功率限制。60 GHz 頻段的工作模式：58.32 GHz、60.48 GHz、62.64 GHz。本裝置已透過認證，可用於戶外的點對多點應用。在以下國家/地區，本裝置不能用於固定點對點應用：

![](/img/01438e2d9209ce7d.webp)

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBwAPG-60adkit</td><td>TV7WAPG60AD</td></tr><tr><td>RBwAPG-60ad</td><td>TV7WAPG60AD</td></tr><tr><td>RBwAPG-60ad-A</td><td>TV7WAPG60AD</td></tr><tr><td>RBwAPG-60ad-SA</td><td>TV7WAPG60ADM</td></tr></tbody></table>

根據 FCC 規則第 15 部分，本裝置已經過測試，符合 A 類數字裝置的限制。這些限制旨在為商業安裝中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置可能會造成有害干擾，在這種情況下，使用者需要自費糾正干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不會造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。

注意：本裝置在外圍裝置上使用遮蔽電纜進行了測試。必須使用遮蔽電纜與本裝置配合以確保合規。

除 FCC CFR §15.255 (b) 中列出的情況外，本裝置不得在飛機上操作。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限制。本裝置安裝和操作時，輻射體與您身體的任何部位之間的最小距離應為 20 cm。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBwAPG-60adkit</td><td>7442A-WAPG60AD</td></tr><tr><td>RBwAPG-60ad</td><td>7442A-WAPG60AD</td></tr><tr><td>RBwAPG-60ad-A</td><td>7442A-WAPG60AD</td></tr><tr><td>RBwAPG-60ad-SA</td><td>7442A-WAPG60ADM</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限制。本裝置安裝和操作時，輻射體與您身體的任何部位之間的最小距離應為 20 cm。Cet equipement est conforme aux limites d'exposition au rayonnement IC definies pour un environnement non controle. Cet equipement doit etre installe et utilise a une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

除 ISED RSS-210 附錄 J.1 中列出的情況外，本裝置不得在飛機上操作。

本裝置不得在飛機上使用，除非符合 ISED RSS-210 附錄 J.1 中所列的條件。

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

## 烏克蘭國家通訊和資訊國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WiGig {#wigig}

<table><thead><tr><th>Operational channels / Maximum output power Betriebskanäle / maximale Ausgangsleistung Canaux opérationnels / puissance de sortie maximale Canali operativi / massima potenza di uscita Canales operacionales / potencia de salida máxima Операционные каналы / максимальная выходная мощность</th><th>58.32 GHz / 40 dBm</th></tr></thead><tbody><tr><td>60.48 GHz / 40 dBm</td><td></td></tr><tr><td>62.64 GHz / 40 dBm</td><td></td></tr></tbody></table>
