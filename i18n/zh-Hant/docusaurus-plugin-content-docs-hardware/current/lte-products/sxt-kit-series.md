---
title: "SXT kit 系列"
slug: /sxt-kit-series
source: https://manual.mikrotik.com/hardware/sxt-kit-series
captured_at: '2026-11-04T10:04:42+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/7b4d436fcd14582c.webp)

:::info 本文涵蓋

- **SXT 4G kit**
- **SXT LTE6 kit**
- **SXT LTE kit-US**
- **SXT LTE kit**
- **SXT LTE6 kit**（2023）
:::

SXT kit 作為完整套件提供，包含內建調變解調器，並連線到內建天線。它具有兩個支援 MDI-X 自動檢測的 10/100 乙太網介面。有兩個 micro SIM 卡槽可用，以便在蜂窩網路運營商之間切換。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家和地方法律法規。
- 在任意牆面安裝接入點的所有安裝方法均需獲得當地管轄部門的認可。
- 裝置安裝必須符合當地和國家電氣規範。
- 本產品設計為安裝在戶外立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確程式，可能導致人員危險和系統損壞。
- 僅使用製造商批准的電源和配件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，應與您的身體、職業使用者或公眾保持至少 45 釐米的距離。

## 首次使用 {#first-use}

- 開啟底部蓋板。
- IMEI 號碼可在外殼和包裝標籤上找到。
- 將 SIM 卡插入 micro-SIM 卡槽（預設使用 SIM A 卡槽）。如果使用另一個卡槽，可以在 RouterOS 中透過 CLI 命令更改配置：/system routerboard modem set sim-slot=down。更改 SIM 卡槽後，LTE 調變解調器將重新啟動。它可能需要一些時間（取決於調變解調器和板卡，大約 30 秒）才能完全初始化，因此請務必測試調變解調器。有關配置詳細資訊，請參閱 [雙 SIM 卡應用](/docs/mobile-networking/dual-sim-application)。
- 將裝置連線到電源（參見“”）。
- 透過 Web 瀏覽器使用 **WebFig** 或 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）配置裝置。開啟 [https://192.168.188.1](https://192.168.188.1) 可訪問 **WebFig**；對於 **WinBox**，請下載該工具，導航到 **Neighbors** 標籤頁，然後選擇 MAC 地址。使用者名稱為“**admin**”，無密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 選擇“Check for updates”按鈕，並將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡並具有活動的 Internet 連線；
- 如需手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 查詢您的產品。所需軟體包可在“Support&Downloads”選單下獲取；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的“Files”選單，並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可以確保最佳效能、穩定性和安全更新；
- 設定路由器密碼。所有 7.1.4 之前的 ROS 版本預設 IP 都設定為 192.168.88.1，升級到 7.1.4 後預設 IP 設定為 192.168.188.1。

## 安裝 {#mounting}

SXT 設計為安裝在立杆上，包裝內包含安裝支架和鋼製卡箍。

- 將卡扣朝前，把安裝支架滑入外殼底部的導軌，直到卡扣咔嗒一聲到位。
- 將卡箍穿過支架上的開口。
- 將裝置固定到立杆上，使乙太網埠朝下。

![](/img/cb77d7c81af721ab.webp)

- 對齊完成後，使用 PH2 螺絲刀擰緊卡環。
- 使用紮帶將乙太網線纜固定到立杆上，距離裝置小於一米，以避免線纜從埠被拉出。
- 檢查安裝角度和位置。使用兩個乙太網埠時，請務必在塑膠門板上切出更寬的線纜開口。您可以使用鉗子撕掉保護線纜開口的塑膠件。關閉塑膠門時，請務必施加壓力，直到其“咔嗒”一聲到位。*本裝置的安裝和配置應由合格人員完成。*

安裝在牆上時，請確保線纜引出方向朝下。本裝置的 IPX 防護等級為 IP54。應使用 Cat6 遮蔽線纜。警告！本裝置安裝和操作時，裝置與身體之間應保持至少 20 釐米的距離。

## 接地 {#grounding}

安裝基礎設施（塔架和桅杆）以及路由器本身必須正確接地。裝置在外殼門後包含一個接地線連線螺絲。將接地線連線到接地螺絲，然後將接地線的另一端連線到已接地的桅杆。這可以顯著降低 ESD 和雷擊損壞的風險。

## 供電 {#powering}

裝置透過乙太網埠供電：

- 12 - 57 V DC ⎓ 無源供電以及 802.3af/at PoE 供電至 ETH1 埠。最大負載下的功耗可達 5 W，帶附件時為 22 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 使用乙太網線纜將裝置連線到 PoE 介面卡的 PoE 輸出（PoE+DATA 或 Data+Power）埠。
- 將 PoE 介面卡的 RJ45 聯結器插入本地路由器、交換器或計算機的乙太網埠。
- 將 PSU 直流插頭連線到 PoE 介面卡，然後將 PSU 連線到交流電源。

## 配置 {#configuration}

登入後，您應選擇 QuickSet 選單中的“Check for updates”按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將使用的國家/地區，以符合當地法規。RouterOS 除了本文件所述內容外還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法進行 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以將裝置啟動以進行重新安裝，請參閱相關章節。

預設配置為 CPE RouterMode：

*LTE 介面連線到運營商網路（WAN 埠）；

*WAN 埠受防火牆保護，並啟用了 DHCP 用戶端。

LAN 配置：

IP 地址 192.168.88.1/24 設定在網橋（LAN 埠）上

所有 7.1.4 之前的 ROS 版本預設 IP 都設定為 192.168.88.1，升級到 7.1.4 後預設 IP 設定為 192.168.188.1。

DHCP 伺服器已啟用；

DNS：已啟用。

WAN（閘道器）配置：

gateway：lte1；

ip4 firewall：已啟用；

NAT：已啟用。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 兩個乙太網埠支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通或交叉線纜連線到其他網路裝置。
- ETH2 埠能夠透過無源 PoE 為另一個 RouterBOARD 裝置供電（最高 57 V）。使用低於 30 V 為本裝置供電時，最大輸出電流為 600 mA；使用高於 30 V 時，最大輸出電流為 400 mA。
- MiniPSIe 插槽。
- 兩個 micro SIM 卡槽。
- 整合 LTE 模組，支援的頻段取決於地區（請檢視宣傳冊）。

## SIM 卡槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議與轉接器一起使用。

## 復位按鈕 {#reset-button}

復位按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（總計 5 秒）；
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（總計 10 秒）；
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（總計 15 秒）；無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 模式按鈕 {#mode-button}

可以從 RouterOS 軟體配置模式按鈕的動作，以執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。模式按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的配件：

- ADAPT1_EU/US 開關電源 24 V、0.8 A、19.2 W、85.3%、VI、線纜：150 cm Hor CMC；
- CLAMP1_Hose Clapmp SUS304（十字型；夾持直徑範圍 35-70 mm）；
- POE1_POE 注入器，帶遮蔽聯結器；
- BRAC1_SXT5D 安裝支架；

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未測試。

**要排查任何問題，請訪問提供的頁面，並導航到專門的故障排除部分以獲取詳細指導和解決方案：故障排除文章**

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>包含 FCCID</th></tr></thead><tbody><tr><td>RBSXTR&R11e-4G</td><td>TV7R11E4G</td></tr><tr><td>RBSXTR&R11e-LTE6</td><td>TV7R11ELTE6</td></tr><tr><td>RBSXTR&R11e-LTE-US</td><td>TV7R11ELTE</td></tr><tr><td>RBSXTR&R11e-LTE</td><td>-</td></tr></tbody></table>

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限值。這些限值旨在為商業安裝中的有害干擾提供合理保護。

本裝置產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置可能會造成有害干擾，此時使用者將被要求自行承擔費用糾正干擾。

**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受收到的任何干擾，包括可能導致非預期操作的干擾。本裝置及其天線不得與任何其他天線或發射器共置或一起操作。**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。本裝置安裝和操作時，輻射器與身體任何部位之間應保持至少 45 釐米的距離。使用 CBRS 頻段時，最終主機裝置的 CBSD 類別將取決於所使用的功率設定和天線增益。

## 加拿大創新、科學和經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>包含 IC</th></tr></thead><tbody><tr><td>RBSXTR&R11e-4G</td><td>7442A-R11E4G</td></tr><tr><td>RBSXTR&R11e-LTE6</td><td>7442A-R11ELTE6</td></tr><tr><td>RBSXTR&R11e-LTE-US</td><td>7442A-R11ELTE</td></tr><tr><td>RBSXTR&R11e-LTE</td><td>-</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學和經濟發展部免許可 RSS 標準的免許可發射器/接收器。操作須滿足以下兩個條件：

-

本裝置不得造成干擾；

-

本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。本裝置內含的免許可發射器/接收器符合加拿大創新、科學和經濟發展部適用於免許可無線電裝置的 CNR 標準。允許在以下兩個條件下執行：

-

本裝置不得產生干擾；

-

本裝置必須接受所受到的任何無線電干擾，即使該干擾可能導致非預期操作。此 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和操作時，輻射器與身體任何部位之間應保持至少 45 釐米的距離。本裝置符合 IC 針對非受控環境規定的輻射暴露限值。本裝置安裝和操作時，輻射器與身體任何部位之間應保持至少 45 釐米的距離。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊顯示在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

如需保修服務的詳細資訊，請聯絡賣家。

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其非預期執行的干擾。製造商：MikroTikls SIA, Unijas iela 2, Riga, LV-1039, 拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA, Unijas iela 2, 里加, 拉脫維亞, LV1039.

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用需要按照 НКРЗІ 2012 年 11 月 1 日第 559 號決定（該決定於 2013 年 1 月 3 日在烏克蘭司法部登記，編號 57/22589）規定的程式獲得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Unijas iela 2, Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RouterBOARD 型無線電裝置符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### GSM / WCDMA / LTE / {#gsm--wcdma--lte-}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>E-GSM-900</th><th>900 MHz / 33 dBm</th></tr></thead><tbody><tr><td>DCS-1800</td><td>1800 MHz 30 dBm</td><td></td></tr><tr><td>WCDMA Band I</td><td>1922.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA Band VIII</td><td>882.4 MHz / 24 dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 1（SXT 4G kit 除外）</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8（SXT 4G kit 除外）</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 31（僅 SXT 4G kit）</td><td>450 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38（SXT 4G kit 除外）</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 42（僅 SXT 4G kit）</td><td>3500 MHz / 23 dBm ± 3 dB</td><td></td></tr><tr><td>LTE Band 43（僅 SXT 4G kit）</td><td>3700 MHz / 23 dBm ± 3 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大 LTE 發射功率限制。有關更多詳細資訊，請參閱上文的符合性宣告。

-

-
