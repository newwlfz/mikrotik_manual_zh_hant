---
title: "hAP ac²"
slug: /hap-ac-2
source: https://manual.mikrotik.com/hardware/hap-ac-2
captured_at: '2026-11-04T05:58:09+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/02e78c0981f20c86.jpg" alt="" width={637} height={799} /></p>

## [hAP ac²](https://mikrotik.com/product/hap_ac2) (RBd52G-5HacD2HnD-TC) {#hap-ac-rbd52g-5hacd2hnd-tc}

hAP ac² 是一款簡單的家庭無線接入點。它已完成預配置，您只需插入 ISP 網線即可開始使用無線上網。我們建議您設定密碼來保護裝置安全。完整規格和產品手冊請參見 [hAP ac² 產品頁面](https://mikrotik.com/product/hap_ac2)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於機架安裝。開始安裝前請仔細閱讀安裝說明。使用不正確的硬體或不遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，它們可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內工作、輸出功率、布纜要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 供電 {#powering}

裝置可從電源插孔或第一個乙太網埠（無源 PoE）獲取電源：

- 直接輸入電源插孔（外徑 5.5mm、內徑 2mm，母頭，中心正極插頭）接受 12-30 V DC
- 第一個乙太網埠接受無源 Power over Ethernet，接受 18-28 V DC（用於補償線纜上的損耗，因此建議高於 12V）最大負載下的功耗可達 15 W。

## 設定 {#setup}

- 將 ISP 網線連線到 Ethernet1 埠；如果您有有線裝置，請將它們連線到其他埠；
- 將計算機的 IP 配置設定為*自動*(DHCP)；
- 從您的 PC 或智慧手機連線到以 "MikroTik" 開頭的無線網路名稱；
- 連線到無線網路後，在 Web 瀏覽器中開啟 192.168.88.1 開始配置，由於預設沒有密碼，您將自動登入（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 在載入的介面中設定您的密碼。還請指定您所在的國家/地區，以確保遵守當地法規。

## 配置 {#configuration}

我們建議點選 "Check for updates" 按鈕，將 RouterOS 軟體更新到最新版本，以確保獲得最佳效能和穩定性。除本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始瞭解各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下來自 Internet 埠的所有訪問均被阻止）。為便於恢復，可以從網路引導裝置，請參見按鈕和跳線一節。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 乙太網埠透過交換晶片連線，可單獨配置，並支援自動交叉/直通線纜校正 (Auto MDI/X)，因此您可以使用直通線或交叉線連線到其他網路裝置。
- 整合的無線模組支援 AP/CPE/P2P/Repeater 模式。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開即可啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議對兩個選項都進行驗證，以防其中一個無法使用。

- **Regular Booter：**要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：**關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將引導進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。取決於型號，這可能會透過 **USR、USER、System** 或 **ACT** LED 指示，或透過 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列在 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢棄物處置場所。請了解您所在地區將裝置正確運輸至指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

FCC ID：TV7RBD52-5ACD2ND 本裝置經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限值旨在為住宅安裝環境提供合理的有害干擾防護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝環境中不會產生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），建議使用者嘗試透過以下措施之一來消除干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收機之間的距離。
- 將裝置連線到與接收機所連電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。 **FCC 警告：** 任何未經負責合規方明確批准的改變或修改，都可能導致使用者失去操作本裝置的權利。本裝置符合 FCC 規則第 15 部分的規定。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期操作的干擾。本裝置及其天線不得與任何其他天線或發射器同處一地或一起執行。**重要提示：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境所規定的射頻輻射暴露限值。本裝置在安裝和執行時，輻射體與您身體任何部位之間的最小距離應為 20 cm。

**天線安裝。警告：** 安裝人員有責任確保在美國（或適用 FCC 規則的地區）使用授權天線時，僅使用經本產品認證的天線。根據 FCC 規則 CFR47 第 15.204 節，明確禁止使用任何未經本產品認證的天線。安裝人員應根據國家法規並針對各天線型別配置天線的輸出功率等級。帶有聯結器的裝置需要由專業人員進行安裝，以確保符合健康與安全要求。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC：7442A-D52AC

本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，並且 (2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。本裝置符合適用於免許可無線電裝置的加拿大工業部 CNR 標準。使用須滿足以下兩個條件：(1) 裝置不得產生干擾，並且 (2) 裝置使用者必須接受所收到的任何無線電干擾，即使該干擾可能影響裝置的正常執行。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

在 5150–5250 MHz 頻段工作的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

**重要提示：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境所規定的輻射暴露限值。本裝置在安裝和執行時，輻射體與您身體任何部位之間的最小距離應為 20 cm。本裝置符合 IC 針對非受控環境所規定的輻射暴露限值。本裝置在安裝和執行時，輻射體與您身體任何部位之間的最小距離應為 20 cm。

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率通道</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц</td><td>≤10 Вт</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證情況而有所不同。

有關裝置製造日期的資訊標示在其標籤上的序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），隨後的兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)，5725-5850 MHz (30 dBm)。可用通道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

本裝置或裝置可能不會造成有害干擾。本裝置必須接受任何干擾，包括可能導致其非期望執行的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 МГц (20 дБм)、5150-5250 МГц (23 дБм)、5250-5350 МГц (20 дБм)、5470-5725 МГц (27 дБм)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用須按照 2012 年 11 月 1 日 NKРЗІ 第 559 號決議批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記（編號 57/22589）的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBD52G-5HacD2HnD-TC 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相應型號）**</th><th>**使用的通道**</th><th>**最大輸出功率 (EIRP)**</th><th>**限制**</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻率通道內工作、輸出功率、布纜要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線裝置必須由專業人員安裝！*

本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多詳細資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定中最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 法規規定的最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告 / 本 MikroTik 裝置符合 ETSI 規定中最大 WLAN 發射功率限值。更多資訊請參見上文的符合性宣告。

<p><Img src="/img/0561b3ba8c95a35c.webp" alt="" width={146} height={135} /></p>

在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。/ 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。/ 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。/ 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。/ 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。/ 在 5150 至 5350 MHz 頻率範圍內工作時，本裝置的 WLAN 功能僅限室內使用。
