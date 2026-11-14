---
title: "Wireless Wire Cube Pro 和 Cube 60Pro ac"
slug: /wireless-wire-cube-pro-cube-60pro-ac
source: https://manual.mikrotik.com/hardware/wireless-wire-cube-pro-cube-60pro-ac
captured_at: '2026-11-04T10:08:19+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可下載為 <a href="/assets/files/tg-lr92-8a6d0117f62f9c262e34369cb2d654fe.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/2a56acfbac220108.jpg)

![](/img/854233100a314cf7.webp)

:::info 本文涵蓋

- **[Wireless Wire Cube Pro](https://mikrotik.com/product/wireless_wire_cube_pro)** (CubeG-5ac60aypair)
- **[Cube 60Pro ac](https://mikrotik.com/product/cube_60pro_ac)** (CubeG-5ac60ay)
:::

客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線裝置都必須由專業人員安裝。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 請僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線裝置都必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置與您的身體、職業使用者或公眾之間的距離不得小於 21 釐米。

## 快速開始 {#quickstart}

- 使用乙太網線將裝置連線到隨附的 PoE 注入器；
- 將 PoE 注入器連線到 PC 或網路交換器；
- 將電源介面卡連線到 PoE 注入器；
- 下載 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)，開啟 WinBox 並連線到裝置；
- 預設 IP：192.168.88.2/192.168.88.3，使用者名稱：**admin**，請在標籤上查詢密碼；
- 從 [https://mikrotik.com/download](https://mikrotik.com/download) 下載最新的 RouterOS 軟體；
- 選擇 ARM 軟體包，並將其儲存到您的 PC；
- 開啟 WinBox 並上傳下載的軟體包，拖放到任意視窗中；
- 重啟裝置；
- 再次連線，並在 Wireless 選單的 W60G 標籤頁中選擇您的區域，在 **QuickSet** 選單中設定您的國家/地區，以應用國家法規設定。*如果裝置發生了 RX 阻塞情況，裝置將在幾秒後恢復其訊號。*

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將要使用的國家/地區，以符合當地法規。除了本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具 ([https://mt.lv/winbox](https://mt.lv/winbox)) 從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置 (參見 )。如果裝置失去連線，請等待幾秒鐘，裝置將自動恢復連線。

## 組裝與安裝 {#assembly-and-mounting}

本裝置可以安裝在垂直或水平的立柱上。最大立柱直徑為 51 mm。

本裝置的安裝和配置應由經過認證的人員完成。

選擇您想要的位置，裝置需要進行精確調整以獲得最佳效能。

- 將隨附的支架固定到立柱上，並用螺絲刀擰緊。
- 將裝置裝到安裝支架上，並使用隨附的工具固定。

![](/img/d8bcf5eb7f7a756c.webp)

儘管本裝置的 IP 防護等級為 IP66，但在戶外安裝時，請確保任何線纜開口都朝下。我們建議使用 POE 注入器，並使用 Cat6 遮蔽線纜進行正確接地。使用和安裝本裝置時，請注意最大允許暴露 (MPE) 安全距離，輻射體與您的身體之間至少保持 20 cm 的距離。

## 供電 {#powering}

本裝置接受來自無源 PoE 注入器的 DC ⎓ 電源（隨附一個電源和一個 PoE 注入器），並接受 18-48 V DC ⎓，最大負載功耗為 13 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置上的乙太網線纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自您本地網路 (LAN) 的乙太網線纜連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼 CubeG-5ac60ay / CubeG-5ac60ay-SA
- CPU 4 核 IPQ-4019 716 MHz
- RAM 大小 256 MB
- 儲存 64 MB 快閃記憶體
- 1G 乙太網埠數量 1
- 無線 5 GHz 802.11a/n/ac
- 無線鏈路數 1
- 天線增益 (dBi) 11.5 5 GHz
- 天線波束寬度 35° 5 GHz
- 60 GHz 天線波束寬度 11° (CubeG-5ac60ay)；60° (CubeG-5ac60ay-SA)
- GPS MT3337V
- WiGig 晶片組 QCA6438
- WiGig 天線模組 SWL-QD46
- 支援的協定 MikroTik 802.11ad / 802.11ay
- 最大 EIRP (dBm) 40
- 尺寸 115 x 95 x 82 mm (CubeG-5ac60ay) 115 x 211 x 90 mm (Cube G-5ac60ay-SA)
- 工作溫度 -40°C 至 +70°C
- 作業系統 RouterOS，許可證級別 4

## 復位按鈕 {#reset-button}

![](/img/391fce45bfed655b.webp)

routerBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置和預設值。
- 在 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統都將載入備用 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含本裝置隨附的以下配件：

![](/img/5ba5d44e172ad3af.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS 軟體版本 *v6.49.5.*。具體的出廠安裝版本號顯示在 RouterOS 選單 /system resource 中。其他作業系統尚未經過測試。

### 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

![](/img/ce6fc3eb10b9a1e6.webp)

FCC ID：TV7CB5A60Y

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝環境提供合理的保護，防止有害干擾。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置可能會造成有害干擾，此時使用者將被要求自費糾正干擾。

FCC 警告：任何未經負責合規的一方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得產生有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。

除 FCC CFR §15.255 (b) 中列出的條件外，不得在飛機上操作本裝置。

重要提示：FCC 輻射暴露宣告：本裝置符合 FCC 針對非受控環境規定的輻射暴露限值。本裝置安裝和執行時，輻射體與您的身體之間的最小距離應為 20cm。用於連線外圍裝置的所有線纜都必須為遮蔽並接地。使用未遮蔽和未接地的線纜連線外圍裝置執行，可能會對無線電和電視接收造成干擾。

### 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

IC：7442A-CB5A60Y

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：(1) 本裝置不得產生干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

在 5150–5250 MHz 頻段內執行的裝置僅限室內使用，以減少對同通道移動衛星系統造成有害干擾的可能性。

在 5 150 至 5 250 MHz 頻段內工作的裝置僅限室內使用，以降低對使用相同通道的移動衛星系統造成有害干擾的風險。

除 ISED RSS-210 附錄 J.1 中列出的條件外，不得在飛機上操作本裝置。

本裝置不得在飛機上使用，除非符合 ISED RSS-210 附錄 J.1 中所列的條件。

重要提示：IC 輻射暴露宣告：本裝置符合 IC RSS-102 針對非受控環境規定的輻射暴露限值。本裝置安裝和執行時，輻射體與您的身體之間的最小距離應為 20cm。本裝置符合針對非受控環境制定的 IC 輻射暴露限值。本裝置安裝和執行時，輻射源與您的身體之間的最小距離應為 20cm。

### UKCA 標識 {#ukca-marking}

![](/img/387853c20d5a4c82.gif)

### CE 符合性宣告 {#ce-declaration-of-conformity}

<table><thead><tr><th>*BG*</th><th>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</th></tr></thead><tbody><tr><td>CS</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DA</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DE</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EL</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EN</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ES</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ET</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FI</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FR</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HR</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HU</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IT</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IS</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令的基本要求及其他相關規定。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LT</td><td>Mikrotīkls SIA 特此確認，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LV</td><td>Mikrotīkls SIA 特此宣告，該無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>MT</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NL</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NO</td><td>Mikrotīkls SIA 特此宣告，該裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令的基本要求及其他相關要求。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PL</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PT</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>RO</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SK</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SL</td><td>Mikrotīkls SIA 特此確認，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SV</td><td>Mikrotīkls SIA 特此宣告，該型別無線電裝置 CubeG-5ac60ay、CubeG-5ac60ay-SA 符合 2014/53/EU 指令。歐盟符合性宣告的完整文字可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr></tbody></table>

本裝置符合 ETSI 法規規定的最大發射功率限制。頻率為 5470-5725MHz，最大發射功率小於 27dBm。歐盟內的頻率和最大發射功率列舉如下：57 - 66 GHz：34.02 dBm。60 GHz 頻段的工作模式：58.32 GHz、60.48 GHz、62.64 GHz。本裝置已透過認證，可用於點到多點應用的室外使用。在以下國家，本裝置不能用於固定點到點應用：

![](/img/01438e2d9209ce7d.webp)

### WiGig {#wigig}

<table><thead><tr><th>工作通道 / 最大輸出功率</th><th>58.32 GHz / &lt;40 dBm</th></tr></thead><tbody><tr><td>60.48 GHz / &lt;40 dBm</td><td></td></tr><tr><td>62.64 GHz / &lt;40 dBm</td><td></td></tr></tbody></table>

### WLAN {#wlan}

<table><thead><tr><th>工作頻率 / 最大輸出功率</th><th>5470-5725 MHz / 27 dBm</th></tr></thead></table>

<table><thead><tr><th>**技術規格：**</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>產品電源輸入選項</td><td>DC 介面卡輸出規格</td><td>外殼防護等級 (IP 等級)</td><td>工作溫度</td><td></td></tr><tr><td>電壓，V</td><td>電流，A</td><td></td><td></td><td></td></tr><tr><td>PoE 輸入乙太網埠 (18 - 48 V DC)</td><td>24</td><td>0.8</td><td>IP54</td><td>-33°..+70°C</td></tr></tbody></table>
