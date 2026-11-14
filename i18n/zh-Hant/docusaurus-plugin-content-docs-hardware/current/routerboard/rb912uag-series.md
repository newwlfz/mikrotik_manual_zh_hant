---
title: "RB912UAG 系列"
slug: /rb912uag-series
source: https://manual.mikrotik.com/hardware/rb912uag-series
captured_at: '2026-11-04T10:00:18+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **[RB912UAG-5HPnD](https://mikrotik.com/product/RB912UAG-5HPnD)**
- **[RB912UAG-2HPnD](https://mikrotik.com/product/RB912UAG-2HPnD)**
:::

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。在將系統連線到電源之前，請閱讀安裝說明。本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責就安裝的結構完整性取得當地主管部門/檢查部門要求的任何地方或國家安全檢查。將接入點安裝到任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。裝置安裝必須符合當地和國家電氣規範。請在開始安裝前仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的程式，可能會對人員造成危險情況並損壞系統。我們無法保證因裝置使用不當而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險。

這是 A 類裝置。在家庭環境中，本產品可能造成無線電干擾，在這種情況下，使用者可能需要採取適當的措施。

## 安裝 {#mounting}

912UAG 系列路由器供專業使用。每臺裝置均採用 ESD 防護包裝。處理電氣裝置時，請遵守以下安全預防措施：

- 在拆包和處理電氣元件時使用腕部接地帶，以避免靜電放電（ESD）損壞，
- 拆包後，請將路由器放在防靜電墊上，
- 安裝裝置時，請確保沒有可能損壞或接觸 PCB 板的物體，
- 請注意，ETH、USB 埠和 DC 插孔伸出 PCB 板的邊緣。可使用 PCB 板上出廠提供的四個孔（位於裝置每側）將裝置安裝到您想要的位置。*警告！本裝置安裝和操作時，裝置與人體之間應保持至少 380 cm 的距離。在住宅環境中操作本裝置可能造成無線電干擾。*

## 連線 {#connecting}

- 選擇您的供電方案，請參閱“供電”部分了解可能的方案。
- 如有需要，將配件連線到 miniPCIe 插槽，將天線線纜連線到 miniPCIe 卡，並插入 SIM 卡。
- 將乙太網線纜連線到千兆乙太網埠。
- 如果不使用 POE，請連線直接輸入電源插孔以啟動裝置。
- 裝置將啟動，短鳴一聲後，無線網路將可供連線。
- 在您的 PC、手機或其他裝置上開啟網路連線，搜尋 MikroTik 無線網路並連線到它。
- 連線到無線網路後，在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始配置；由於預設沒有密碼，您將自動登入（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。
- 我們建議單擊“Check for updates”按鈕並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。
- 在載入的螢幕中選擇您的國家/地區，以應用國家/地區法規設定並設定您的密碼。

## 供電 {#powering}

本裝置支援以下供電模式：

- 透過乙太網埠提供無源 10-30 V PoE。長線纜上需要更高電壓來補償功率損耗。建議至少 18 V。
- 電源插孔直接輸入 10-30 V。最大功耗 14 W。

## 配置 {#configuration}

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路啟動裝置，參見相關章節。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個千兆乙太網埠（支援 Auto MDI/X，因此您可以使用直通或交叉線纜連線到其他網路裝置）。該乙太網埠可接受來自無源 PoE 注入器的 10-30 V DC 供電。
- 一個 miniPCIe 插槽。*本裝置可能與 R11e-LTE 國際調變解調器不相容。*
- A 型 USB 插槽。
- SIM 卡插槽。
- RB912UAG-5HPnD 支援 5 GHz、802.11a/n。
- RB912UAG-2HPnD 支援 2.4 GHz、802.11b/g/n。

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（總共 5 秒）。
- 再按住 5 秒，LED 變為常亮，此時鬆開以開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（總共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總共 15 秒）。無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統將載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢物處置場所。請熟悉您所在地區將裝置正確運輸至指定處置場所的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RB912UAG-5HPnD</td><td>TV7RB912G-5HPNDM</td></tr><tr><td>RB912UAG-2HPnD</td><td>TV7RB912G-2HPND</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝中的有害干擾提供合理保護。

![](/img/0a33cf47745dd39e.jpg)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能造成有害干擾，在這種情況下，使用者將被要求自費糾正干擾。

**FCC 警告：** 未經合規負責方明確批准的任何更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作需滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或協同操作。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限制。本裝置安裝和操作時，輻射體與您身體任何部位之間應保持至少 167 cm 的距離。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

IC:7442A-912G2HPND, 7442A-912G5HPNDM 本裝置符合加拿大工業部免許可證 RSS 標準。操作需滿足以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。本裝置符合加拿大工業部適用於免許可證無線電裝置的 CNR 要求。允許在以下兩個條件下操作：(1) 裝置不得產生干擾，且 (2) 使用者必須接受裝置受到的任何無線電干擾，即使該干擾可能影響裝置執行。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

在 5150–5250 MHz 頻段內執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限制。本裝置安裝和操作時，輻射體與您身體任何部位之間應保持至少 168 cm 的距離。本裝置符合 IC 針對非受控環境規定的輻射暴露限制。本裝置安裝和使用時，輻射體與您身體任何部位之間應保持至少 168 cm 的距離。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5650-5850 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊標在其標籤上序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 МГц（20 дБм），5470-5725 МГц（27 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定（該決定已於 2013 年 1 月 3 日在烏克蘭司法部登記，登記號為 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限制。本 MikroTik 裝置安裝和操作時，與您的身體、職業使用者或公眾的距離不得小於 20 釐米。本裝置符合歐盟針對非受控環境規定的輻射暴露限制。除非本文件第 1 頁另有明確說明，本裝置安裝和操作時，輻射體與您身體之間應保持至少 20 cm 的距離。在 RouterOS 中，您必須指定您的國家/地區，以確保遵守當地無線法規。

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相應型號）</th><th>使用通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限制。有關更多詳細資訊，請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的 WLAN 最大發射功率限制。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限制。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限制。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告。
