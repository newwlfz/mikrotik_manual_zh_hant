---
title: "無線有線 Dish"
slug: /wireless-wire-dish
source: https://manual.mikrotik.com/hardware/wireless-wire-dish
captured_at: '2026-11-04T10:44:33+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可下載為 <a href="/assets/files/wireless-wire-dish-0b7f9054624012522cbc79e78af307a1.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/3d74a0afd5ea4ad8.jpg)

## [Wireless Wire Dish](https://mikrotik.com/product/wireless_wire_dish) (RBLHGG-60adkit) {#wireless-wire-dish-rblhgg-60adkit}

Wireless Wire Dish 是一套兩個 LHG 60G 裝置，工作在 60 GHz 無線頻譜中。出廠時已成對配置，便於首次輕鬆啟動。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作程式，可能導致人員處於危險情況並對系統造成損壞。
- 本產品設計用於室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商批准的電源和配件，這些可在本產品的原包裝中找到。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座中拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能造成無線電干擾，在這種情況下，使用者可能需要採取適當措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟為不受控環境設定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 51 釐米。

## 快速開始 {#quickstart}

- 組裝裝置；
- 開啟乙太網門，將乙太網線連線到乙太網埠，將乙太網線的另一端連線到隨附的 PoE 注入器；
- 將 PoE 注入器插入您的網路交換器；
- 將隨附的電源插入 PoE 注入器以啟動裝置；
- 將裝置安裝到桅杆或立柱上；
- 對準兩個單元；
- 下載 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。主裝置預設 IP：192.168.88.2，從裝置：192.168.88.3，使用者名稱：**admin**，密碼印在裝置蓋內側的標籤上；
- 如果無法透過 IP 連線，請使用 Neighbors 標籤頁並透過 MAC 地址連線；
- 對於 LHG 60G 型號，預設 IP 為 192.168.88.1，且沒有密碼；
- 連線後配置裝置，使其具有活動的 Internet 連線 [https://mt.lv/configuration](https://mt.lv/configuration)；
- 將 RouterOS 軟體升級到最新版本 [https://mt.lv/upgrade](https://mt.lv/upgrade)；
- 選擇您的國家/地區，以應用國家/地區法規設定。

## 組裝 {#assembly}

- 將兩條支腿安裝到 LHG 外殼上。
- 將組裝好的 LHG 單元卡入網格的適當位置。
- 用兩顆自攻螺釘固定支腿（使用 Phillips PH2 螺絲刀）。

![](/img/13ed4322cde89e25.webp)

## 安裝 {#mounting}

![](/img/2996df0a42666294.webp)

- 用四顆隨附螺釘將安裝元件固定到裝置背面。
- 使用隨附的 U 型螺栓卡箍將組裝好的單元安裝到立柱上。隨附鋼製卡箍的夾持直徑為 35 – 70 mm。

![](/img/c76fdbedc9f84ace.webp)

- 使用 Aim 工具調整您的裝置。有關安裝說明，請參見 [Wireless Wire Dish 產品頁面](https://mikrotik.com/product/wireless_wire_dish)。

![](/img/d81e925bdab602bf.webp)

裝置包含一個接地連線（標記為 ⏚），您應將其連線到裝置使用地點所在塔架或建築物的接地裝置。這是為了大幅降低 ESD 和雷擊損壞的風險。包裝中包含接地聯結器。

警告！本裝置的安裝和操作位置與您的身體之間應保持至少 95 cm 的距離。在住宅環境中操作本裝置可能會造成無線電干擾。本裝置的 IP 防護等級為 IP54。*本裝置的安裝和配置應由合格人員完成。*

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通或交叉線纜連線其他網路裝置。
- WiGig, 802.11ad.

## 供電 {#powering}

裝置透過乙太網埠供電。乙太網埠接受 12-57 V DC 的 PoE 輸入（無源和 802.3af/at）。包裝盒內包含一個電源介面卡和無源 PoE 注入器。使用 PoE 注入器時，請確保使用 "Power + Data" 聯結器連線裝置，使用 "Data" 聯結器連線您的 PC、路由器或交換器。**連線到 POE 介面卡：**

- 將來自裝置的乙太網線連線到 POE 介面卡的 POE+DATA 埠。
- 將來自本地網路（LAN）的乙太網線連線到 POE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。最大功耗 5 W。

## 配置 {#configuration}

完整的 RouterOS 文件位於此處：[https://mt.lv/help](https://mt.lv/help)。Wireless Wire dish 套件中包含的裝置已預配置為橋接模式下的 60GHz 和乙太網介面。必須根據上方連結的文件手冊應用其他配置。使用乙太網線將每臺 Wireless Wire dish 裝置連線到您的網路。為了使這些網路之間能夠通訊，裝置必須彼此對準並保持直接視距。連線後，裝置將自動橋接兩個網路。請熟悉有關 [W60G 介面](/docs/wireless/w60g) 的附加資訊。使用 MikroTik WinBox 工具透過乙太網線訪問裝置。應使用 WinBox 連線到主裝置的預設 IP 地址 192.168.88.2 和從裝置的預設 IP 地址 192.168.88.3。登入使用者名稱為 admin，密碼印在裝置蓋內側的標籤上。為便於恢復，可以啟動裝置以進行重新安裝，請參見相應章節。

## 按鈕和跳線 {#buttons-and-jumpers}

routerBOOT 復位按鈕具有以下功能。按下按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，復位到受密碼保護狀態（約 5 秒）
- 當 LED 變為常亮綠色時鬆開按鈕以清除所有配置（約 10 秒）
- 當 LED 不再點亮後鬆開按鈕（約 20 秒），使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。無論使用上述哪個選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## LED 狀態 {#led-status}

裝置包含使用 LED 的精確對準引導。如果從天線盤後方看向鏈路另一端，指示燈會用箭頭指示轉動天線盤的方向。當對準 LED 熄滅，僅保留 "link established" LED 時，表示對準完成。LED 指示燈包括：

![](/img/81b844d3fdf5b5cd.webp)

- 向上傾斜。
- 向下傾斜。
- 向右旋轉。
- 向左旋轉。
- 鏈路建立時 LED 點亮。
- 乙太網連線時 LED 點亮。
- 使用者可配置 LED。
- 電源狀態開啟。

## 配件 {#accessories}

包裝內包含以下隨裝置附帶的配件：

- K-LHG 螺絲套裝/固定套裝。
- 千兆 POE 注入器。
- LHG-5G-390 mm Dish（網孔尺寸 0.5 t x1.0 wx1.4 mm）。
- EU/US 開關電源 24 V ⎓，0.38 A，9 W，Level VI，線纜：1.5 m。
- 軟管卡箍 SUS304（Philips 型；夾持直徑範圍 35-70 mm）。
- BRAC1_ LHG 安裝元件。
- DynaDish U 型螺栓 M8（A2 不鏽鋼）。
- QuickMount AIM.

## 規格 {#specifications}

有關 LHG 產品、規格和圖片的更多資訊，請訪問我們的網頁：[https://mikrotik.com/product/wireless_wire_dish](https://mikrotik.com/product/wireless_wire_dish)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用在現場配置路由器，或為您的 MikroTik 家庭接入點應用最基本的初始設定。掃描二維條碼並選擇您首選的作業系統。

![](/img/9bcba09a7b6a0d53.webp)

![](/img/8d294e5cd375c591.webp)

本裝置符合 ETSI 法規規定的最大 TX 功率限制。60 GHz 頻段中的工作模式：58.32 GHz、60.48 GHz、62.64 GHz。本裝置已獲認證，可用於點對多點應用的室外使用。在以下國家/地區，固定業務僅允許在部分頻段內使用：

![](/img/01438e2d9209ce7d.webp)

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID: TV7LHGG60AD

本裝置已透過測試，符合 FCC Rules 第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝環境中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域操作本裝置可能會造成有害干擾，在這種情況下，使用者將需要自費糾正干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者喪失操作本裝置的許可權。

本裝置符合 FCC Rules 第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受收到的任何干擾，包括可能導致非預期操作的干擾。

注意：本單元已在連線外圍裝置時使用遮蔽線纜進行測試。必須使用遮蔽線纜與本單元配合，以確保合規。

除 FCC CFR §15.255 (b) 中列出的條件外，本裝置不得在飛機上操作。

**重要說明。FCC 輻射暴露宣告：** 本裝置符合 FCC 為不受控環境設定的輻射暴露限值。本裝置安裝和操作時，輻射器與您的身體之間應保持至少 51cm 的距離。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC: 7442A-LHGG60AD

本裝置包含免許可發射器/接收器，符合加拿大創新、科學與經濟發展部的免許可 RSS。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

除 ISED RSS-210 附錄 J.1 中列出的條件外，本裝置不得在飛機上操作。

本裝置不得在飛機上使用，除非符合 ISED RSS-210 附錄 J.1 中所列的條件。

**重要說明。IC 輻射暴露宣告：** 本裝置符合 IC 為不受控環境設定的 RSS-102 輻射暴露限值。本裝置安裝和操作時，輻射器與您的身體之間應保持至少 51cm 的距離。本裝置符合針對非受控環境制定的 IC 輻射暴露限值。本裝置安裝和使用時，輻射源與您的身體之間應保持至少 51cm 的距離。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期資訊以斜槓分隔標示在其標籤上的序列號末尾。第一位數字表示年份編號（年份的最後一位），後兩位數字表示週數。

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

在烏克蘭使用本裝置，必須按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBLHGG-60adkit 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### WiGig {#wigig}

<table><thead><tr><th>工作通道 / 最大輸出功率</th><th>58.32 GHz / 40 dBm</th></tr></thead><tbody><tr><td>60.48 GHz / 40 dBm</td><td></td></tr><tr><td>62.64 GHz / 40 dBm</td><td></td></tr></tbody></table>
