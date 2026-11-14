---
title: "CCR2004-16G-2S+PC"
slug: /ccr2004-16g-2s-plus-pc
source: https://manual.mikrotik.com/hardware/ccr2004-16g-2s-plus-pc
captured_at: '2026-11-04T05:55:46+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/ea609dae5237f4bc.jpg" alt="" width={800} height={667} /></p>

## [CCR2004-16G-2S+PC](https://mikrotik.com/product/ccr2004_16g_2s_pc) {#ccr2004-16g-2spc}

比之前的 CCR1009 路由器快最高 300%——在令人愉悅的靜默之中！以您負擔得起的價格，享受您應得的奢華。16 個千兆乙太網埠，2 個 10G SFP+ 籠。完整規格和宣傳冊請參見 [CCR2004-16G-2S+PC 產品頁面](https://mikrotik.com/product/ccr2004_16g_2s_pc)。

## 安全警告 {#safety-warnings}

- 在對任何 MikroTik 裝置進行操作之前，請了解與電氣電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 本裝置應由經過培訓的合格人員按照本安裝說明進行安裝。安裝人員負責確保裝置的安裝符合當地和國家的電氣規範。請勿嘗試拆卸、維修或改裝本裝置。
- 本產品適用於室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的做法是將電源插頭從電源插座上拔出。
- 本產品為 A 類產品。在居住環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施

<p><Img src="/img/ee40bff277b50ded.webp" alt="" width={574} height={494} /></p>

觸電危險。本裝置僅應由經過培訓的人員進行維修

## 快速開始 {#quickstart}

- 將您的 PC 連線到標有 **MGMT/BOOT** 的埠或第一個乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 應使用 Web 瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方法以確保可訪問性；**
- 在 Web 瀏覽器中開啟 192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，且沒有密碼（或者，對於某些型號，請在標籤上檢視使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 透過將您的 RouterOS 軟體升級到最新版本，可以確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

本裝置具有兩個整合電源單元，AC **⏦** 100-240V，配有標準 IEC 相容插座。支援的輸入電壓 36-57 V（DC 插孔）36-57（2 針端子）電源介面卡標稱電壓 48 V 電源介面卡標稱電流 0.9 A 最大功耗（不含附件）30 W 最大功耗 36 W

## 配置 {#configuration}

乙太網埠 15 具有用於連線的預設 IP 地址：192.168.88.1。使用者名稱為 admin，且沒有密碼。裝置預設未應用任何其他配置，請設定 WAN IP 地址、使用者密碼，並更新裝置。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址。出於恢復目的，可以啟動裝置進行重新安裝，請參見復位按鈕。

## 規格 {#specifications}

- 產品程式碼 CCR2004-16G-2S+PC
- CPU AL32400 1.2 GHz
- CPU 架構 ARM 64bit
- CPU 核心數 4
- RAM 容量 4 GB
- RAM 型別 DDR4
- 儲存 128 MB，NAND
- 1G 乙太網埠數量 16
- 10G SFP+ 埠數量 2
- 作業系統 RouterOS v7，許可證級別 6
- 交換晶片型號 88E6191X
- 交換器中的千兆埠數量 8
- 尺寸 272 x 195 x 44 mm
- 工作溫度 -20°C 至 +60°C

## 復位按鈕 {#reset-button}

**復位按鈕**：

- 在啟動過程中按住此按鈕，直到 USER LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置。
- 按住復位按鈕並給裝置通電（等待 "USER" LED 閃爍然後穩定為 "On"，當 "USER" LED 變為 "Off" 時——鬆開復位按鈕）——裝置將以 BOOTP 模式啟動，使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。

無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。在 LED 開始閃爍之前鬆開按鈕，則僅載入備份 RouterBOOT 而不進行重設。這對於 RouterBOOT 偵錯和恢復很有用。

## 安裝 {#mounting}

本裝置設計用於室內，可使用隨附的機架安裝件安裝在機架式機箱中，也可以放置在桌面上。如果指定用途為機架式機箱，請使用十字螺絲刀將機架安裝耳片固定到裝置兩側：

<p><Img src="/img/27bf22aa32ecbced.webp" alt="" width={610} height={543} /></p>

- 如右圖所示，將機架耳片安裝到裝置兩側，並擰緊四顆螺絲將其固定到位；
- 將裝置放入機架式機箱並對齊孔位，使裝置能夠方便地裝入；
- 擰緊螺絲將其固定到位。裝置不具備防水保護，請確保將裝置放置在乾燥通風的環境中。我們建議為我們的裝置使用 Cat6 線纜。

## 隨附部件 {#included-parts}

<p><Img src="/img/13c8554043c2e142.webp" alt="" width={642} height={280} /></p>

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

### 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/0097d5c5b96539f2.webp" alt="" width={198} height={166} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝中的有害干擾提供合理防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來確定），則鼓勵使用者嘗試透過以下一項或多項措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以獲取幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改都可能使使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分的要求。其執行受以下兩個條件約束：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受接收到的任何干擾，包括可能導致意外操作的干擾。

注意：本裝置已使用外設上的遮蔽電纜進行測試。必須在本裝置上使用遮蔽電纜以確保合規。

### 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。其執行受以下兩個條件約束：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置內含的免許可證發射器/接收器符合加拿大創新、科學與經濟發展部（ISED）針對免許可證無線電裝置適用的 CNR 標準。允許在以下兩個條件下執行：1）裝置不得產生干擾；2）裝置必須接受任何接收到的無線電干擾，即使該干擾可能導致裝置執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

### UKCA 標誌 {#ukca-marking}

<p><Img src="/img/387853c20d5a4c82.gif" alt="" width={2115} height={2113} /></p>

<table><thead><tr><th>**(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:**</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>(EN) Product Power Input Options (DE) Produkt Stromquellen Optionen (FR) Options d'entrée d'alimentation du produit (IT) Opzioni di ingresso alimentazione del prodotto (ES) Opciones de entrada de energía del producto (RU) Варианты входной мощности продукта</td><td>(EN) DC Adapter Output Specification, (V/A) (DE) Ausgangsspezifikationen des Gleichstromadapters, (V/A) (FR) Spécifications de sortie de l'adaptateur de courant continu, (V/A) (IT) Specifiche di uscita dell'adattatore di corrente continua, (V/A) (ES) Especificaciones de salida del adaptador de corriente continua, (V/A) (RU) Выходные характеристики адаптера постоянного тока, (В/А)</td><td>(EN) IP class of the enclosure (DE) IP-Klasse des Gehäuses (FR) Classe IP du boîtier (IT) Classe IP della custodia (ES) Clase de IP del recinto (RU) Класс защиты корпуса IP</td><td>(EN) Operating Temperature (DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура</td><td></td></tr><tr><td>Voltage, V</td><td>Current, A</td><td></td><td></td><td></td></tr><tr><td>DC Jack (36 - 57 V DC) 2-pin terminal (36 - 57 V DC)</td><td>48</td><td>0.9</td><td>IP20</td><td>±0°..+60°C</td></tr></tbody></table>
