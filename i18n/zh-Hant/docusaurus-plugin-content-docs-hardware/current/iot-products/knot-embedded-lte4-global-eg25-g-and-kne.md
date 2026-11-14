---
title: "KNOT 嵌入式 LTE4 全球版 EG25-G&KNe"
slug: /knot-embedded-lte4-global-eg25-g-and-kne
source: https://manual.mikrotik.com/hardware/knot-embedded-lte4-global-eg25-g-and-kne
captured_at: '2026-11-04T09:51:54+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可以下載為 <a href="/assets/files/knot-embedded-lte4-global-eg25-g-and-kne-90ab457bdf749d4c1d6d36f3e9c20b44.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/10de52b491fffd8a.jpg)

### [KNOT Embedded LTE4 Global](https://mikrotik.com/product/knot_emb_lte4_global)（EG25-G&KNe） {#knot-embedded-lte4-global-eg25-gkne}

KNOT Embedded LTE4 現已推出 Global（EG25-G）版本，擴充套件了面向北美及其他國際市場的 LTE 頻段支援。工業級 LTE/BLE/GNSS 連線能力，隨處適用。最初為咖啡機和自動售貨機設計——同樣非常適合各類工業自動化應用。完整規格與宣傳冊請參見 [KNOT Embedded LTE4 Global EG25-G&KNe 產品頁面](https://mikrotik.com/product/knot_emb_lte4_global)。

## 快速開始 {#quickstart}

- 按照裝置上標示的位置將 SIM 卡插入卡槽；
- 將裝置連線到隨附的電源介面卡；
- 使用乙太網線將裝置連線到計算機；
- 透過 Web 瀏覽器使用 **WebFig** 或 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）配置裝置。**提供多種配置方式以確保可訪問性；**
- 開啟 192.168.188.1 即可訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 “**admin**”，無密碼（某些型號的使用者名稱和無線密碼請檢視裝置貼紙）；
- 如果您的行動網路運營商要求，請輸入 PIN 碼；
- 點選 “Check for updates” 按鈕，將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡並具備可用的 Internet 連線；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 “Downloads” 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 “Files” 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性與安全更新；
- 設定您的路由器密碼。

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>說明</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>EG25-G&KNe</td></tr><tr><td>**CPU**</td><td>ARM Cortex‑A7，1 核，800 MHz</td></tr><tr><td>**RAM / 儲存**</td><td>256 MB RAM / 256 MB NAND</td></tr><tr><td>**作業系統**</td><td>RouterOS v7，License Level 3</td></tr><tr><td>**行動網路：2G**</td><td>Class 12. 3 (1800MHz), 8 (900MHz) , 2 (1900MHz), 5 (850MHz</td></tr><tr><td>**行動網路：3G**</td><td>R8 (42.2 Mbps ↓ / 5.76 Mbps ↑). Bands, 1 (2100MHz), 5 (850MHz), 8 (900MHz), 1 (2100MHz), 5 (850MHz), 8 (900MHz), 2 (1900MHz), 4 (1700MHz), 6 (850 MHz), 19 (800 MHz), 2 (1900MHz), 4 (1700MHz), 6 (850 MHz), 19 (800 MHz</td></tr><tr><td>**行動網路：LTE**</td><td>Category 4（150 Mbps ↓ / 50 Mbps ↑）</td></tr><tr><td>**MIMO**</td><td>DL 2×2，UL 1×1</td></tr><tr><td>**LTE FDD 頻段**</td><td>1 (2100MHz), 3 (1800MHz), 5 (850MHz), 7 (2600MHz), 8 (900 MHz), 20 (800MHz), 2 (1900MHz), 4 (1700MHz), 12 (700MHz), 13 (700 MHz), 18 (800 MHz), 19 (800 MHz), 25 (1900MHz), 26 (850MHz), 28 (700MHz</td></tr><tr><td>**LTE TDD 頻段**</td><td>38 (2600MHz), 40 (2300MHz), 41 (2500MHz), 39 (1900MHz)</td></tr><tr><td>**TAC**</td><td>01673800</td></tr><tr><td>**GNSS**</td><td>GPS、GLONASS、北斗、Galileo（SMA 母頭）</td></tr><tr><td>**藍牙**</td><td>5.4（BLE）</td></tr><tr><td>**乙太網**</td><td>1 × 1 GbE RJ45（PoE‑in 802.3af/at，12‑57 V）</td></tr><tr><td>**SIM**</td><td>Nano‑SIM 與 eSIM</td></tr><tr><td>**GPIO**</td><td>6 針排針（耐壓 24 V，模擬與數字 I/O）</td></tr><tr><td>**供電**</td><td>PoE‑in（12‑57 V）或 USB‑C 5 V / 0.8 A，最大 6 W</td></tr><tr><td>**尺寸**</td><td>90 × 70 × 22 mm</td></tr><tr><td>**工作溫度**</td><td>–40 °C … +70 °C</td></tr><tr><td>**MTBF**</td><td>≈ 100 000 h @ 25 °C</td></tr></tbody></table>

## 安裝 {#mounting}

![](/img/6571d9174af6bfb6.webp)

![](/img/12860d4466370ab0.webp)

- 可使用隨附的 K-91 固定套件將裝置安裝在裝置的背面或側面，也可使用 DIN 導軌安裝套件。該套件適用於標準 35 mm × 7.5 mm 的 DIN 導軌。使用隨附的兩顆螺釘將安裝件固定到裝置上，然後將裝置固定到 DIN 導軌上。包裝中不包含 DIN 導軌。
- 或者，也可以使用裝置背面提供的螺釘孔將裝置安裝到牆上。裝置應以電纜開口朝下的方式安裝，如示意圖所示。*警告！本裝置安裝和操作時，裝置與人體之間應保持至少 20 cm 的距離。在居住環境中操作本裝置可能造成無線電干擾。* *本裝置的安裝與配置應由具備資質的人員完成。*

## 供電 {#powering}

- USB-C 輸入電壓：5 V，0.8 A。
- 乙太網埠支援 802.3af/at Power over Ethernet 12-57 V DC。最大功耗可達 6 W。

**連線到 PoE 介面卡：**

- 使用乙太網線將裝置連線到 PoE 介面卡的 **PoE + DATA** 埠。
- 使用乙太網線將本地網路（LAN）連線到 PoE 介面卡的 **DATA** 埠。
- 將電源線連線到介面卡，然後插入電源插座。

## 天線連線 {#antenna-connections}

<table><thead><tr><th>**埠**</th><th>**功能**</th><th>**在連線中的作用**</th><th>**備註**</th></tr></thead><tbody><tr><td>**MAIN**</td><td>主蜂窩發射與接收天線</td><td>所有資料收發所必需</td><td>必須連線，調變解調器才能工作</td></tr><tr><td>**DIV（分集）**</td><td>輔助蜂窩僅接收天線</td><td>透過從不同的空間路徑接收訊號，提升訊號質量與可靠性</td><td>可選，但在弱訊號或移動環境中建議使用</td></tr><tr><td>**GNSS**</td><td>GNSS（GPS）接收天線</td><td>啟用衛星定位（GPS/GNSS）功能</td><td>僅在使用 GNSS/定位服務時需要</td></tr></tbody></table>

### 它們如何協同工作 {#how-they-work-together}

**MAIN** 天線同時負責發射（TX）和接收（RX），是裝置執行所必需的。**DIV** 天線提供接收分集，使調變解調器能夠在兩路接收訊號中選擇更好的一路，從而提升穩定性與潛在吞吐量。

這一配置構成了裝置用於蜂窩連線的 2×2 MIMO 實現。

**GNSS** 天線獨立於蜂窩通訊，僅用於衛星定位。

### 實際注意事項 {#practical-considerations}

- 如果只使用一根蜂窩天線，它必須連線到 **MAIN** 埠。
- 在弱訊號環境中，強烈建議加裝 **DIV** 天線。
- 為獲得最佳效能，請讓 MAIN 和 DIV 天線之間保持一定的物理間距或採用不同的朝向。
- 安裝 **GNSS** 天線時應保證天空視野開闊，以獲得精確定位。

### 擴充套件插槽與埠 {#extension-slots--ports}

<table><thead><tr><th>埠</th><th>型別</th><th>功能</th></tr></thead><tbody><tr><td>1 × 1 GbE RJ45</td><td>PoE‑in / 資料</td><td>乙太網 + 供電</td></tr><tr><td>1 × USB‑C</td><td>僅供電</td><td>5 V 輸入</td></tr><tr><td>1 × SIM 插槽</td><td>Nano‑SIM / eSIM</td><td>蜂窩網路</td></tr><tr><td>3 × SMA</td><td>DIV / GNSS / MAIN</td><td>LTE 與 GNSS 天線</td></tr><tr><td>1 × 藍牙天線（內建）</td><td>2.4 GHz，2 dBi 增益</td><td>BLE</td></tr><tr><td>1 × GPIO 排針</td><td>6 針</td><td>數字 I/O，模擬輸入</td></tr><tr><td>1 × microUSB 2.0（適用於部分 KNOT 型號）</td><td>供電 / 外設</td><td>–</td></tr></tbody></table>

## 蜂窩調變解調器配置 {#cellular-modem-configuration}

子選單：`/interface lte`。有關頻段選擇、漫遊或高階選項，請參閱 LTE 指南。

## GNSS 配置 {#gnss-configuration}

更多詳細資訊請參閱此處的指南。

## 按鈕和跳線 {#buttons-and-jumpers}

### 復位按鈕 {#reset-button}

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置隨後將查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論採用上述哪種方式，如果在裝置上電之前按下該按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## GPIO 引腳排列 {#gpio-pinout}

GPIO 引腳位於外殼下方的電路板上，如下圖所示：

![](/img/a157bbe312aa3131.webp)

### ADC 輸入/模擬輸入（pin2） {#adc-inputanalog-input-pin2}

![](/img/a1a7751cf9c9c102.webp)

**注意：** *模擬輸入電壓為 0-24 V。理論解析度為 1.5 mV（14 位 ADC）。模擬輸入阻抗約為 72K Ohm。*

#### 連線的繼電器（pin4） {#connected-relays-pin4}

![](/img/1699bba96b105716.webp)

**注意：** 最大功耗（數字輸出開漏電晶體）為 0.48 W。建議在連續工作時不要超過 24V 或 0.5A。漏源絕對最大電壓為 30V，最大電流為 2.8A。*

![](/img/4c01507e5fd17337.webp)

#### 防拆開關（pin6） {#tamper-switch-pin6}

![](/img/07b8e8f51cc022fc.webp)

**注意：** *數字輸入電壓最大為 0-24 V。*

防拆開關：該輸入配有內部上拉電阻。要使引腳獲得邏輯 “0”，電壓應在 0-1.2 V 之間；

要使引腳獲得邏輯 “1”，電壓應在 1.2-24V 之間。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下配件：

![](/img/08c5b42d7bb22d3a.webp)

### 可單獨購買的天線 {#antennas-can-be-purchased-separately}

<table><thead><tr><th>**HGO-LTE-W**</th><th>**ACGPSA**</th></tr></thead><tbody><tr><td>![](/img/4b4ec2b339b71935.webp)</td><td>![](/img/d891612d324286e3.webp)</td></tr></tbody></table>

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 `/system resource` 中。其他作業系統未經測試。
