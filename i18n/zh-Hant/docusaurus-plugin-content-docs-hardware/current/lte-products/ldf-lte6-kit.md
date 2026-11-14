---
title: "LDF LTE6 套件"
slug: /ldf-lte6-kit
source: https://manual.mikrotik.com/hardware/ldf-lte6-kit
captured_at: '2026-11-04T09:53:34+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## [LDF LTE6 kit](https://mikrotik.com/product/ldf_lte6_kit)（RBLDFR&R11e-LTE6） {#ldf-lte6-kit-rbldfrr11e-lte6}

![](/img/9e37859fd85e768a.webp)

LDF（Lite dish feed）是一款室外 LTE 系統，設計用於安裝在偏置天線上。該裝置內建調變解調器，開箱即可使用。完整規格與宣傳冊請參閱 [LDF LTE6 kit 產品頁面](https://mikrotik.com/product/ldf_lte6_kit)。

## 安全警告 {#safety-warnings}

-

在進行任何裝置作業之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。

-

本產品的最終處置應依照所有國家法律法規進行。

-

在任何牆面上安裝接入點的所有安裝方法，均須獲得當地主管部門的認可。

-

裝置的安裝必須符合當地和國家的電氣規範。

-

本產品設計用於室外安裝在立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能對人員造成危險情況並損壞系統。

-

請僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。

-

在將系統連線到電源之前，請閱讀安裝說明。

-

我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！

-

如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。

-

客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

- 開啟乙太網埠蓋板；
- 將 SIM 卡插入卡槽，晶片朝上；
- 用乙太網線將裝置連線到隨附 PoE 注入器的 data+power 端；
- 將 PoE 注入器的 data 端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1)；
- 使用者名稱為 **admin**，沒有密碼（部分型號請在貼紙上檢視使用者名稱和無線密碼）；
- 使用 check for update 選項將裝置升級到最新版本。您必須有一張可用且有資料流量的 SIM 卡；
- 裝置將會重啟；
- 再次連線，並在 **QuickSet** 選單中設定您所在的國家/地區，以應用該國的法規設定；
- 保護您的裝置並設定強密碼。

## 供電 {#powering}

本裝置支援 PoE 802.3af/at 12-57 V DC ⎓。包裝內包含一個 PoE 注入器。最大功耗 6 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的乙太網線連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 組裝與安裝 {#assembly-and-mounting}

本裝置相容標準偏置天線。按圖示組裝帶蓋板的乙太網線：

- 橡膠密封圈側面已切開，以便將其套到乙太網線上。組裝時它必須位於外殼螺母內部，擰緊壓緊螺母會將其壓緊在乙太網線上。

![](/img/51f7d72bc1477a77.webp)

![](/img/01ee54020effb25c.webp)

- 將裝置安裝到天線上，LDF 的安裝直徑為 40 mm。請確保安裝時箭頭朝上。

![](/img/795edcfad2cc778d.webp)

- 插上乙太網線，並順時針旋緊蓋板。本裝置設計用於室外安裝在天線上，乙太網線連線到裝置背面。請確保將 LDF 單元以正確的位置安裝在偏置支架上——單元朝上正對天線。天線將充當反射器，放大訊號。組裝體的最終位置應放置在立杆上並固定。立杆安裝說明請參閱您的天線安裝說明。確保線纜引出口朝下。本裝置的 IPX 防護等級為 IP54。

警告！本裝置的安裝和操作應保持裝置與人體之間至少 20 cm 的距離。在住宅環境中操作本裝置可能造成無線電干擾。

*本裝置的安裝與配置應由具備資質的人員完成。*

## SIM 卡槽的使用 {#sim-slot-usage}

![](/img/135e991cc189ac69.webp)

SIM 卡槽位於蓋板下方，請按圖片所示方向插入 micro-SIM 卡。晶片朝上！

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通線或交叉線連線其他網路裝置。
- MiniPCIe 插槽，整合調變解調器。
- 模式按鈕。

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置將開始查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 包裝清單 {#included-parts}

![](/img/a5c4f3acae885ab5.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列在 /system resource 中。其他作業系統未經測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解您所在地區將裝置妥善運送到指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>包含的 FCCID</th></tr></thead><tbody><tr><td>RBLDFR&R11e-LTE6</td><td>TV7R11ELTE6</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝提供合理的有害干擾防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），建議使用者嘗試透過以下一種或多種措施來消除干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所接電路不同的插座上。
- 向經銷商或有經驗的無線電/電視技術人員尋求幫助。**FCC 警示：** 任何未經負責合規的一方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致執行異常的干擾。本裝置及其天線不得與任何其他天線或發射器共址或聯合執行。**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置的安裝和操作應保持輻射體與您身體任何部位之間至少 20 cm 的距離。*使用 CBRS 頻段時，最終主機裝置的 CBSD 類別將取決於所用的功率設定和天線增益。*

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>包含的 IC</th></tr></thead><tbody><tr><td>RBLDFR&R11e-LTE6</td><td>7442A-R11ELTE6</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 標準的免許可發射器/接收器。其操作須符合以下兩個條件：

-

本裝置不得造成干擾；

-

本裝置必須接受任何干擾，包括可能導致裝置執行異常的干擾。本裝置中包含的免許可發射器/接收器符合加拿大創新、科學與經濟發展部針對免許可無線電裝置適用的 CNR 標準。其操作須符合以下兩個條件：

-

本裝置不得產生干擾；

-

本裝置必須接受任何接收到的無線電干擾，即使該干擾可能影響其正常執行。此 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置的安裝和操作應保持輻射體與您身體任何部位之間至少 20 cm 的距離。Cet equipement est conforme aux limites d'exposition au rayonnement IC definies pour un environnement non controle. Cet equipement doit etre installe et utilise a une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置生產日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份（年份的最後一位數字），後兩位數字表示週數。

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

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置，須按照烏克蘭國家通訊與資訊化監管委員會（НКРЗІ）2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，登記號 57/22589）規定的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBLDFR&R11e-LTE6 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>E-GSM-900</th><th>900 MHz / 33 dBm</th></tr></thead><tbody><tr><td>DCS-1800</td><td>1800 MHz / 30 dBm</td><td></td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 24dB ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 24dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1700 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dB ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dB ± 2.7 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 和 LTE 最大發射功率限值。更多詳細資訊請參見上文的符合性宣告。

- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝！
