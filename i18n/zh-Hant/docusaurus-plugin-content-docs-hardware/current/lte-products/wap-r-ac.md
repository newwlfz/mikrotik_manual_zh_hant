---
title: "wAP R ac"
slug: /wap-r-ac
source: https://manual.mikrotik.com/hardware/wap-r-ac
captured_at: '2026-11-04T10:07:45+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/ba0590deb856bc57.webp)

## [wAP R ac](https://mikrotik.com/product/wap_r_ac) (RBwAPGR-5HacD2HnD) {#wap-r-ac-rbwapgr-5hacd2hnd}

wAP R ac 是一款小型防風雨裝置，配有整合天線和用於調變解調器的 miniPCIe 插槽。有關完整規格和宣傳冊，請參見 [wAP R ac 產品頁面](https://mikrotik.com/product/wap_r_ac)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 將接入點安裝在任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置安裝必須符合當地和國家電氣規範。
- 本產品設計為安裝在戶外立柱上，但也可在室內安裝。開始安裝前，請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確程式，可能導致人員危險和系統損壞。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和配件。
- 將系統連線到電源之前，請閱讀安裝說明。
- 我們不能保證因裝置使用不當而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座中拔下電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。安裝和操作本 MikroTik 裝置時，應與您的身體、職業使用者或公眾保持不少於 20 釐米的距離。

## 快速開始 {#quickstart}

- 使用十字螺絲刀擰鬆固定底蓋的螺釘（參見（連結）。
- SIM 卡槽。
- 指示裝置電源狀態的 LED。
- LED - 使用者自定義。
- 指示 LTE 網路活動的 LED。
- 用於 SMA 線纜的塑膠門。
- MiniPCIe 插槽。
- 整合無線模組，工作於 2.4 GHz、802.11b/g/n 和 5 GHz、802.11a/n/ac 協定。

## 配置 {#configuration}

裝置配置為 AP 路由器。Eth1 被防火牆阻止，您可以透過無線介面訪問路由器進行配置。您應在 QuickSet 選單中選擇 “Check for updates” 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能： [https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址。登入 WinBox 時，將顯示預設配置設定。為恢復目的，可以啟動裝置進行重新安裝，請參見相應章節。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三項功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（總計 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開以開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（總計 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總計 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內包含以下隨裝置附帶的配件：

![](/img/86132bf85da243d5.webp)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS 軟體版本 v6。具體的出廠安裝版本號顯示在 RouterOS 選單 /system resource 中。其他作業系統尚未經過測試。

為避免環境汙染，請將裝置與家庭垃圾分開，並以安全方式處置，例如送往指定的廢物處置場。請熟悉您所在地區將裝置正確運輸到指定處置場的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBwAPGR-5HacD2HnD</td><td>TV7WAPGR5AC2D</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 請諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。 **FCC 警告：** 任何未經合規負責方明確批准的更改或修改都可能使使用者操作本裝置的許可權失效。本裝置符合 FCC 規則第 15 部分。操作需滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共址或協同執行。 **重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的 RF 輻射暴露限值。安裝和操作本裝置時，輻射體與您身體任何部位之間的最小距離應為 20 cm。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBwAPGR-5HacD2HnD</td><td>7442A-WAPGR5AC2D</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作需滿足以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置非預期執行的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。操作需滿足以下兩個條件：(1) 裝置不得產生干擾，且 (2) 使用者必須接受所受到的任何無線電干擾，即使該干擾可能影響裝置的正常執行。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。安裝和操作本裝置時，輻射體與您身體任何部位之間的最小距離應為 20 cm。本裝置符合 IC 針對非受控環境規定的輻射暴露限值。安裝和使用本裝置時，輻射體與您身體任何部位之間的最小距離應為 20 cm。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射機功率</th></tr></thead><tbody><tr><td>2400-2483.5 MHz, 5150-5350 MHz, 5650-5850 MHz</td><td>≤10 W</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊位於其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2480-2483.5 MHz（20 dBm），5150-5250 MHz（23 dBm），5250-5350 MHz（20 dBm），5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議（2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA，Brivibas gatve 214i，Riga，Latvia，LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBwAPGR-5HacD2HnD 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相應型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用不受任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多詳細資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。有關更多資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的最大 WLAN 發射功率限值。有關更多資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的最大 WLAN 傳輸功率限值。有關更多資訊，請參見上文的符合性宣告。

![](/img/0561b3ba8c95a35c.webp)

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。 / 本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內執行時僅限室內使用。
