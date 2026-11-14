---
title: "NetMetal ac²"
slug: /netmetal-ac
source: https://manual.mikrotik.com/hardware/netmetal-ac
captured_at: '2026-11-04T09:57:16+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/0d9b97cbb07a1832.webp)

## [NetMetal ac²](https://mikrotik.com/product/netmetal_ac2)（RBD23UGS-5HPacD2HnD-NM） {#netmetal-ac-rbd23ugs-5hpacd2hnd-nm}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行處理。
- 將接入點安裝在任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置安裝必須符合當地和國家電氣規範。
- 本產品用於安裝在室外立柱上。開始安裝前，請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確程式，可能會對人員造成危險並損壞系統。
- 僅使用製造商批准且可在本產品原始包裝中找到的電源和附件。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能會造成無線電干擾，在此情況下，使用者可能需要採取適當措施。

**射頻輻射暴露：** 此 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。此 MikroTik 裝置安裝和操作時，應與您的身體、職業使用者或公眾保持不小於 20 釐米的距離。

## 快速開始 {#quickstart}

該配置與 AP 模式下的 PTP Bridge 相同，不同之處在於 PTMP 設定中無線模式設定為 ap_bridge。可透過該地址直接訪問路由器。如果裝置連線到啟用了 DHCP 伺服器的網路，網橋介面上配置的 DHCP 用戶端將獲取 IP 地址，該地址可用於訪問路由器。

請按照以下快速步驟設定裝置：

- 開啟上蓋；
- 使用乙太網線將裝置連線到隨附 PoE 注入器的資料+電源端；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 透過 Web 瀏覽器使用 **WebFig** 或 [https://mt.lv/winbox](https://mt.lv/winbox) 上的 **WinBox** 工具配置裝置。**提供多種配置方法以確保可訪問性；**
- 透過開啟 [https://192.168.88.1](https://192.168.88.1) 訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，並單擊 MAC 地址。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 要手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，並重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 在 "Quick Set" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。直通線或交叉線均可用於連線其他網路裝置。

- SFP 埠。
- 外部 SMA 天線聯結器。
- MiniPCIe 插槽。
- 工作在 2.4 GHz、802.11b/g/n 協定的整合無線模組。
- 工作在 5 GHz、802.11a/n/ac 協定的整合無線模組。
- USB Type-A。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以復位 RouterOS 配置（總共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開以開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（總共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內含以下隨裝置附帶的附件：

- EU 開關電源 48 V ⎓ 0.95 A 45.6 W。
- 千兆 POE 注入器。
- K-27 DIN 導軌支架安裝套件。
- 軟管卡箍 40/60 w2 A2 9 mm。有關支援的 SFP 模組，請參閱 [MikroTik 有線介面相容性](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。

## MiniPCIe 插槽使用 {#minipcie-slot-usage}

此 NetMetal 版本未安裝調變解調器。要安裝模組，需要拆下上蓋並開啟底蓋。安裝 miniPCIe 模組應由合格人員完成，處理電氣裝置時請遵循安全預防措施：

- 拆包和處理電氣元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞。
- 使用 HEX3 螺絲刀拆下四顆螺絲。

![](/img/3d63a4287bb06b8b.webp)

- 提起並拆下頂蓋。
- 找到 PCB 上的 miniPCIe 插槽，並拆下兩顆出廠預裝螺絲。

![](/img/d6c2929801f06cb6.webp)

- 將隨附的厚導熱墊貼到卡上，然後將卡安裝到 miniPCIe 插槽中，使導熱墊位於 PCB 和卡之間。
- 使用之前拆下的兩顆螺絲將卡固定到位。
- 將灰色 uFL 聯結器連線到調變解調器的 MAIN 天線聯結器，將黑色線纜連線到輔助（或 AUX）聯結器。
- 將較薄的導熱墊貼到卡的頂部。

![](/img/5c2c2beff2ec1921.webp)

- 為 SMA 聯結器鑽孔。
- 引導卡線纜穿過。
- 重新組裝。

組裝時，請確保橡膠密封圈牢固地環繞外殼放置並均勻展開，以防止進水汙染。外殼螺絲扭矩為 2,5 Nm。安裝所裝插卡的天線時，請確保將它們與無線天線保持適當距離並分開。

## 天線使用 {#antenna-usage}

天線安裝。警告：安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用經產品認證的天線。根據 FCC 規則 CFR47 part 15.204，明確禁止使用任何未經產品認證的天線。安裝人員應根據國家/地區法規並按天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。已批准的 2GHz 天線列表：

-

5 dBi 偶極天線 ACOMNIRPSMA 已批准的 5GHz 天線列表：

-

30 dBi 拋物面天線 MTAD-5G-30D3

-

19 dBi 扇區天線 MTAS-5G-19D120 與上述所列天線型別相同且增益更低的天線可在符合認證的情況下使用。有關無線介面的更多資訊：[無線介面](/docs/wireless/abgn/wireless-interface)

## 規格 {#specifications}

有關此產品的更多資訊、規格、圖片、下載和測試結果，請訪問我們的網頁：[https://mikrotik.com/product/netmetal_ax](https://mikrotik.com/product/netmetal_ax)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置妥善運輸至指定處置場所的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID：TV7RB922-5HPACT、TV7RB921-5SHPACT、TV7A21GS-5HPACD。

本裝置已經過測試，發現符合 FCC 規則第 15 部分對 A 類數字裝置的限值要求。這些限值旨在為商業安裝環境中的有害干擾提供合理保護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置可能會造成有害干擾，在此情況下，使用者將需要自費糾正干擾。

FCC 警告：未經合規責任方明確批准的任何更改或修改，可能會使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受收到的任何干擾，包括可能導致非預期執行的干擾。本裝置及其天線不得與任何其他天線或發射器共址或聯合執行。

**重要：射頻輻射暴露。**

本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置安裝和操作時，應與輻射器和您身體的任何部位保持至少 20cm 的距離。

**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用經產品認證的天線。根據 FCC 規則 CFR47 part 15.204，明確禁止使用任何未經產品認證的天線。安裝人員應根據國家/地區法規並按天線型別配置天線的輸出功率水平。帶聯結器的裝置需要由專業人員安裝，以確保符合健康與安全要求。

已批准的 2GHz 天線列表：• 24 dBi 拋物面天線 DC 24-HD-PFIP • 20 dBi 平板天線 WLP-2450-20 • 17 dBi 扇區天線 SA 24-90-17-WB • 15 dBi 全向天線（杆裝）WL0-2450-15 • 13 dBi 全向天線（水平極化）HP, 0DH 24-13 已批准的 5GHz 天線列表：• 8.5 dBi 全向天線 MTI Wireless MT-482016NA • 24 dBi 平板天線 Pacific Wireless PA58-24 • 32 dBi 拋物面天線 Pacific Wireless HDDA5W-32-DP 與上述所列天線型別相同且增益更低的天線可在符合認證的情況下使用。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC：7442A-D2352AC

本裝置符合加拿大工業部適用於免許可無線電裝置的 RSS 標準。其執行須滿足以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置執行異常的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。其執行須滿足以下兩個條件：(1) 本裝置不得產生干擾，且 (2) 本裝置必須接受所收到的任何無線電干擾，即使該干擾可能導致裝置執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

在 5150–5250 MHz 頻段執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

**重要：射頻輻射暴露。**

本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置安裝和操作時，應與輻射器和您身體的任何部位保持至少 20 cm 的距離。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>5150-5350 МГц, 5650-5850 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置生產日期資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：5150-5250 МГц（23 дБм），5250-5350 МГц（20 дБм），5470-5725 МГц（27 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需要按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記為第 57/22589 號的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i 里加，拉脫維亞，LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

**客戶有責任遵守當地國家法規，包括在合法頻率通道、輸出功率、佈線要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝！**

此 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限制。有關更詳細的資訊，請參閱上方的符合性宣告 / 此 MikroTik 裝置符合 ETSI 規定所設定的最大 WLAN 發射功率限值。更多資訊請參閱上方的符合性宣告 / 此 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限制。有關更多資訊，請參閱上方的符合性宣告 / 此 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限制。有關更多資訊，請參閱上方的符合性宣告 / 此 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限制。有關更多資訊，請參閱上方的符合性宣告 / 此 MikroTik 裝置符合 ETSI 規定規定的最大 WLAN 發射功率限制。有關更多資訊，請參閱上方的符合性宣告。

![](/img/0561b3ba8c95a35c.webp)

此裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 此裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 此裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 此裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 此裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 此裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。
