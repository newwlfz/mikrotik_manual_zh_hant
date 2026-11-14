---
title: "OmniTIK 系列"
slug: /omnitik-series
source: https://manual.mikrotik.com/hardware/omnitik-series
captured_at: '2026-11-04T09:57:49+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **[OmniTIK 5 ac](https://mikrotik.com/product/rbomnitikg_5hacd)** (RBOmniTikG-5HacD)
- **[OmniTIK 5 PoE ac](https://mikrotik.com/product/rbomnitikpg_5hacd)** (RBOmniTikPG-5HacD)
- **[OmniTIK 5 PoE](https://mikrotik.com/product/RBOmniTikUPA-5HnDr2)** (RBOmniTikUPA-5HnD)
- **[OmniTIK 5](https://mikrotik.com/product/RBOmniTikU-5HnDr2)** (RBOmniTikU-5HnD)
:::

本裝置需要升級到 RouterOS v7.11.2 或最新版本，以確保符合當地監管機構的規定。終端使用者有責任遵守所在國家/地區的規定，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。

*技術規格、宣傳冊以及有關產品的更多資訊，請訪問 [https://mikrotik.com/products](https://mikrotik.com/products)* *包含更多資訊的軟體配置手冊可在 [https://mt.lv/help](https://mt.lv/help) 找到*

*MikroTik 裝置僅供專業使用；如果您不具備相應資質，請諮詢顧問 [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 將接入點安裝在任何牆面上的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本產品旨在安裝於室外立杆上。開始安裝前，請仔細閱讀安裝說明。未能使用正確的硬體和配置或遵循正確的操作程式，可能會對人員造成危險並損壞系統。
- 僅使用製造商認可且可在本產品原包裝中找到的電源和附件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座中拔下電源插頭。
- 客戶有責任遵守所在國家/地區的規定，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。
- 這是 A 類裝置。在住宅環境中，本產品可能會造成無線電干擾，在這種情況下，使用者可能需要採取適當措施。

**重要：射頻輻射暴露。**

- 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和操作時，輻射體與人體任何部位之間的最小距離應為 30 釐米。

## 首次使用 {#first-use}

首個乙太網埠始終配置為 WAN 埠（受防火牆保護、啟用 DHCP 用戶端，並停用 MAC 連線/發現）。其他乙太網埠和無線介面會加入本地 LAN 網橋，並設定 192.168.88.1/24 地址和配置 DHCP 伺服器。

- 開啟底部蓋板。
- 將您的 PC 或 LAN 網線連線到乙太網埠。
- 按照“供電”部分所述連線電源。
- 將 LAN 計算機的 IP 配置設定為自動（DHCP）。
- 裝置的預設 IP 地址是 192.168.88.1，請在 Web 瀏覽器中開啟此地址以開始配置。使用者名稱為 admin，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。
- 我們建議點選“檢查更新”按鈕並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。
- 在載入的螢幕上選擇您的國家/地區，應用國家/地區法規設定並設定密碼。我們建議點選“檢查更新”按鈕並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。RouterOS 除了本文件所述內容外還包含許多配置選項。我們建議訪問 RouterOS 文件頁面以熟悉這些可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。

## 供電 {#powering}

裝置可透過以下方式接受供電：

- 乙太網埠接受無源 PoE 12-57 V DC ⎓。對於 Omnitik 5 型號，為 11-30 V。最大負載下的功耗可達 14 W。PoE 版本接受 12-57 V DC，最大功耗為 18W，帶附件時為 66 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置上的乙太網電纜連線到 PoE 介面卡的 PoE+DATA 埠；
- 將來自本地網路（LAN）的乙太網電纜連線到 PoE 介面卡；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 電源輸出 {#power-output}

*僅適用於 OmniTik 5 PoE ac：* 本裝置可以透過其乙太網埠向外部裝置提供 PoE 供電。這很方便，因為您不需要任何額外的 PoE 注入器來為其他裝置供電。輸出電壓將與輸入電壓相同。此模式下每個乙太網埠的最大輸出功率為 1A（所有埠的總最大值為 2A）。要達到最大輸出功率，建議使用高壓介面卡以及隨附的 PoE 注入器為 OmniTik 裝置供電（48/56V），因為 802.3af/at 輸入限制為 30W，而 OmniTik 自身將消耗高達 15W。在 RouterOS 中啟用 Power Output 後，乙太網 LED 會增加紅色（綠色表示已建立乙太網鏈路，紅色表示有電源但無鏈路，紅色和綠色均表示有鏈路且有電源）。

## 安裝 {#mounting}

在裝置背面，將隨附的立杆安裝介面卡滑動安裝，使卡扣朝前，直到卡扣咔嗒一聲到位。

![](/img/8d05977a197feefd.jpg)

## [OmniTIK 5 PoE ac](https://mikrotik.com/product/rbomnitikpg_5hacd) (RBOmniTikPG-5HacD) {#omnitik-5-poe-ac-rbomnitikpg-5hacd}

使用隨附的軟管卡箍將裝置固定到立杆或桅杆上。可調節的 QuickMount 介面卡可單獨購買。

![](/img/02ac439176662f7a.webp)

OmniTik 有一個用於固定埠門的鎖定螺釘，可使用 5mm 內六角螺絲刀將其關閉。

## 接地 {#grounding}

安裝基礎設施（塔和桅杆）必須正確接地。請將所有鬆散的乙太網電纜和天線電纜固定在距裝置約 30cm 的立杆或桅杆上，以免電纜重量拉扯埠和聯結器。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個千兆乙太網埠，支援自動交叉/直通電纜校正（Auto MDI/X），因此您可以使用直通或交叉電纜連線到其他網路裝置。
- 一個整合無線 5GHz 802.11a/n/ac，2x2 MIMO，內建柵格天線，最大增益 7.5dBi。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有以下功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置（總共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（總共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如在指定的廢物處置場所處置。請熟悉將裝置正確運輸到您所在地區指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>RBOmniTikG-5HacD</td><td>TV7OMNITIKPG5HACD</td></tr><tr><td>RBOmniTikPG-5HacD</td><td>TV7OMNITIKPG5HACD</td></tr><tr><td>RBOmniTikUPA-5HnD</td><td>TV7RBOMNITIK5HND</td></tr><tr><td>RBOmniTikU-5HnD</td><td>TV7RBOMNITIK5HND</td></tr></tbody></table>

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝中的有害干擾提供合理保護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域操作本裝置可能會造成有害干擾，在這種情況下，使用者將被要求自行承擔費用糾正干擾。

**FCC 警告：** 任何未經合規負責方明確批准的更改或修改都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作受以下兩個條件約束：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或協同操作。

**重要：射頻輻射暴露。**

本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和操作時，輻射體與人體任何部位之間的最小距離應為 20 釐米。

**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用已透過本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 部分，明確禁止使用任何未經本產品認證的天線。安裝人員應根據國家/地區法規和每種天線型別配置天線的輸出功率水平。帶聯結器的裝置需要專業安裝，以確保符合健康和安全要求。

**經批准的 5 GHz 天線列表：**

- 8.5 dBi 全向天線（型號：MT-482016/N/A）；
- 24 dBi 平板天線（型號：PA58-24-ANT）；
- 32 dBi 碟形天線（型號：HDDA5W-32-DP2）；根據認證，也可以使用與上述所列天線相同型別且增益更低的天線。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBOmniTikG-5HacD</td><td>7442A-OMNTKPG5AC</td></tr><tr><td>RBOmniTikPG-5HacD</td><td>7442A-OMNTKPG5AC</td></tr><tr><td>RBOmniTikUPA-5HnD</td><td>7442A-OMNTK5HND</td></tr><tr><td>RBOmniTikU-5HnD</td><td>7442A-OMNTK5HND</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。操作受以下兩個條件約束：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。其操作獲准滿足以下兩個條件：(1) 裝置不得產生干擾，且 (2) 裝置使用者必須接受所受到的任何無線電干擾，即使該干擾可能影響裝置的正常執行。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

在 5150–5250 MHz 頻段執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以減少對使用相同通道的移動衛星系統造成有害干擾的風險。

**重要：射頻輻射暴露。**

本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和操作時，輻射體與人體任何部位之間的最小距離應為 20 釐米。

**天線安裝警告：** 安裝人員有責任確保在加拿大（或適用 IC 規則的地區）使用授權天線時，僅使用已透過本產品認證的天線。安裝人員應根據國家/地區法規和每種天線型別配置天線的輸出功率水平。帶聯結器的裝置需要專業安裝，以確保符合健康和安全要求。

**經批准的 5 GHz 天線列表：**

- 8.5 dBi 全向天線（型號：MT-482016/N/A）
- 24 dBi 平板天線（型號：PA58-24-ANT）
- 32 dBi 碟形天線（型號：HDDA5W-32-DP2）根據認證，也可以使用與上述所列天線相同型別且增益更低的天線。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射器功率</th></tr></thead><tbody><tr><td>5150-5350 MHz, 5650-5850 MHz</td><td>≤100 mW</td></tr></tbody></table>

*可用頻率通道可能因產品型號和認證而異。

裝置製造日期資訊位於其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：5725-5850 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其非預期執行的干擾。製造商：MikroTikls SIA, Unijas iela 2, Riga, LV-1039, 拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊和資訊領域國家監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA, Unijas iela 2, 里加, 拉脫維亞, LV1039.

工作頻率（最大輸出功率）：5470-5725 MHz（27 dBm）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置，必須按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定批准並在烏克蘭司法部 2013 年 1 月 3 日第 57/22589 號登記的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Unijas iela 2. 里加，拉脫維亞，LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率（EIRP）**</th><th>**限制**</th></tr></thead><tbody><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

**客戶有責任遵守所在國家/地區的規定，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝！**

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定，滿足最大 WLAN 發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規，滿足最大 WLAN 發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規則，滿足最大 WLAN 發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告。
