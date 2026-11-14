---
title: "wAP ax LTE7 套件"
slug: /wap-ax-lte7-kit
source: https://manual.mikrotik.com/hardware/wap-ax-lte7-kit
captured_at: '2026-11-04T10:07:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/ab28db28cb8aebf8.webp)

![](/img/3f5b27411dbd2efd.webp)

## [wAP ax LTE7 kit](https://mikrotik.com/product/wap_ax_lte7) (wAPGR-5HaxD2HaxD&R11e-LTE7) {#wap-ax-lte7-kit-wapgr-5haxd2haxdr11e-lte7}

全新的 wAP LTE7 kit 是廣受歡迎的 wAP ac LTE6 的升級版本。現在——配備 Wi-Fi 6、CAT7 LTE、更強大的 ARM 平臺以及更高的天線增益。該裝置採用我們改進的新一代 IP66 防水外殼。

## 安全警告 {#safety-warnings}

- 在對任何 MikroTik 裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。
- 僅使用製造商認可的電源和附件，這些電源和附件可在本產品的原始包裝中找到。
- 本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責確保裝置的安裝符合當地和國家的電氣規範。
- 請勿嘗試拆卸、維修或改裝裝置。如需維修服務，請聯絡 MikroTik 支援。
- 本產品可在室內和室外使用。在開始安裝之前，請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，操作風險自負！
- 插座應安裝在裝置附近，並且應易於接近。
- 裝置發生故障時，請斷開其電源。最快的方法是將電源介面卡從電源插座上拔下。
- 這是 A 類產品。在居住環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。
- 為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定區域處置。請熟悉將裝置正確運送到您所在地區指定收集點的程式

## 快速開始 {#quickstart}

- 開啟底部蓋板；
- 按裝置上的指示將 SIM 卡插入插槽；
- 使用乙太網線將裝置連線到隨附 PoE 注入器的 *"data+power"* 端；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 在計算機上進入網路連線部分，找到名為 "*MikroTik-...*" 的無線網路。然後連線到它（請檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，使用網頁瀏覽器中的 WebFig，或位於 [https://mt.lv/winbox/](https://mt.lv/winbox/) 的 "WinBox" 配置工具 **提供多種配置方式以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 選擇 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## 安裝 {#mounting}

裝置可透過多種方式安裝：牆壁、天花板、抱杆，或者放置在包裝中隨附的專用 MikroTik 支架中。包裝中包含帶有說明的鑽孔模板，可幫助您安裝乙太網線並將其固定到天花板或牆壁上。包裝中還包含一個用於安裝到活動天花板吊頂板另一側的鋼製支架，以及兩顆螺絲和牆塞。裝置可使用紮帶或鋼製卡箍固定到抱杆上。可使用不同的螺絲防止底部蓋板被開啟。隨附一顆 Torx T20 安全螺絲供選配使用。請使用隨附的 L 形扳手將其固定到底部蓋板。更換螺絲的詳細說明在包裝中。

在使用和安裝本裝置時，請注意最大允許暴露量（MPE）安全距離，即輻射體與您身體之間至少保持 31 cm 的距離。

### 抱杆安裝 {#pole-mounting}

![](/img/6bf6bbf7b0406e6a.webp)

![](/img/fdfbab7b78baa4b2.webp)

** 建議使用電工膠帶以增加材料之間的摩擦力。*

- 將塑膠紮帶穿過孔洞，安裝到鋼製支架上。
- 將支架安裝到裝置上。
- 用螺絲固定。
- 將裝置安裝到抱杆或桅杆上並對齊。
- 將網線穿過開口並連線到乙太網埠。
- 關閉底部卡扣並用螺絲固定。建議使用紮帶將網線固定到抱杆上，與裝置的距離約為 30 cm。

### 牆壁/天花板安裝 {#wallceiling-mounting}

- 將安裝模板放在牆壁或天花板上，並標記鑽孔位置。

![](/img/35a51811319757d0.webp)

- 安裝孔之間的距離：**162.5 mm**
- 鑽安裝孔：為隨附的牆塞鑽 **Ø 6 mm** 孔，或
- 如果直接安裝到電纜導管中，則鑽 **Ø 5 mm** 孔。
- 如有需要，插入隨附的牆塞。
- 使用 K-95 套件中隨附的螺絲固定安裝支架。
- 從裝置上取下橡膠密封圈。
- 使用 PH2 螺絲刀鬆開外殼螺絲。

![](/img/8609dec5cac4198e.webp)

- 開啟外殼，將網線穿過電纜入口。

![](/img/8ac132d065ca3e3e.webp)

- 如果要安裝 ETH 插口，請使用 **13 mm** 鑽頭鑽孔。
- 如果只是走線，請使用 **8 mm** 鑽頭鑽孔。*（注意：此改裝會降低裝置的 IP 防護等級。）*

![](/img/f133af5d59e03f30.webp)

- 將裝置安裝到支架上：

![](/img/45f2457de4a5f3ce.webp)

將上部安裝點掛到支架上。

- 向下滑動裝置，直到其鎖定到位。
- 安裝 K-95 套件中的橡膠密封圈，以起到環境保護作用。

![](/img/a1668db5586e2165.webp)

- 連線網線並完成安裝。
- 擰緊外殼螺絲並重新裝上橡膠密封圈。
- 對於戶外安裝，請使用防護密封圈以確保環境保護。

:::warning 警告

- 鑽孔前，請確保牆內沒有隱藏的金屬物體或管線。
- 確認安裝表面能夠承受裝置的重量。
- 對於戶外安裝，請在適用的情況下使用隨附的天氣防護配件。

這種格式比逐張描述每張圖片更簡潔、更易遵循。

:::

### 線纜安裝 {#cable-installation}

#### 準備電纜入口 {#preparing-the-cable-entry}

- 開啟裝置外殼。
- 在橡膠密封圈上確定所需的電纜入口位置。
- 使用鋒利的刀或手術刀，沿標示的切割槽小心切開橡膠密封圈。
- 僅對要安裝的電纜進行必要的切割，以保持儘可能高的防護等級。

![](/img/8fe181a0b4aeb3b0.webp)

#### 安裝網線 {#installing-ethernet-cables}

- 將網線穿過橡膠密封圈上準備好的開口。

![](/img/2f48d1f9ed3ba351.webp)

- 網線穿過密封圈後，用合適的接頭進行壓接。

![](/img/69d804249a2be452.webp)

- 將網線連線到裝置內部所需的乙太網埠。

### 備選佈線方式 {#alternative-cable-routing}

#### 裸線安裝 {#bare-cable-installation}

- 如果裸線直接從牆壁引出，請在標示位置鑽一個 **Ø 8 mm** 的孔穿過外殼。

![](/img/ddd63d074a6b9255.webp)

- 將電纜穿過該孔，並在裝置內部進行端接。

![](/img/52353b9ff4063257.webp)

#### 預端接網線安裝 {#pre-terminated-ethernet-cable-installation}

- 如果使用帶有預裝 RJ45 接頭的電纜，請在標示位置鑽一個 **Ø 13 mm** 的孔穿過外殼。
- 將接頭穿過該孔，並連線到所需的乙太網埠。鑽額外的孔會降低防護（IP）等級。用合適的矽酮或密封膠密封所有開口。確保鑽孔後設備內部沒有殘留的金屬屑。

### 安裝 microSIM 卡（如適用） {#installing-a-microsim-card-if-applicable}

- 將 microSIM 卡插入 SIM 卡座。

![](/img/1e958da5a0b0e5d5.webp)

- 用 SIM 卡座的撥杆將卡推到位，直到聽到咔噠聲。

![](/img/1c6297692e476c24.webp)

- 確認撥杆已完全鎖定。

![](/img/e1c548d4aa737f81.webp)

#### 固定安裝 {#securing-the-installation}

- 使用紮帶整理並固定裝置內部的所有線纜。

![](/img/6ced9a6e29c10bed.webp)

- 合上外殼蓋。
- 使用 PH2 螺絲刀將外殼螺絲擰緊至 **0.8 Nm**。

![](/img/e413f73ee3e29b9e.webp)

- 重新裝上螺絲上的橡膠塞。

### 最終檢查 {#final-check}

- 確保所有電纜入口均已正確密封。
- 確認安裝時標有 **"This side faces the wall"** 的一面朝向正確。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<table><thead><tr><th>**引數**</th><th>值</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>wAPGR-5HaxD2HaxD&R11e-LTE7</td></tr><tr><td>**架構**</td><td>ARM 64bit</td></tr><tr><td>**CPU**</td><td>IPQ-5010</td></tr><tr><td>**CPU 核心數**</td><td>2</td></tr><tr><td>**CPU 執行緒數**</td><td>2</td></tr><tr><td>**CPU 頻率**</td><td>800 MHz</td></tr><tr><td>**RAM**</td><td>256 MB</td></tr><tr><td>**儲存**</td><td>128 MB NAND</td></tr><tr><td>**1G 乙太網埠**</td><td>2</td></tr><tr><td>**SIM 卡槽**</td><td>1 × Micro SIM 卡槽</td></tr><tr><td>**MiniPCIe 插槽**</td><td>1 × MiniPCIe 插槽，由 LTE 調變解調器佔用</td></tr><tr><td>**3G 類別**</td><td>R8 (DL 42.2 Mbps / UL 5.76 Mbps)</td></tr><tr><td>**3G 頻段**</td><td>1 (2100 MHz) / 3 (1800 MHz) / 5 (850 MHz) / 8 (900 MHz)</td></tr><tr><td>**LTE 類別**</td><td>7 (DL 300 Mbps / UL 100 Mbps)</td></tr><tr><td>**LTE 調變解調器**</td><td>R11e-LTE7</td></tr><tr><td>**TAC**</td><td>35312597</td></tr><tr><td>**MIMO DL**</td><td>2×2</td></tr><tr><td>**MIMO UL**</td><td>1×1</td></tr><tr><td>**LTE 頻段（FDD）**</td><td>1 (2100 MHz) / 3 (1800 MHz) / 5 (850 MHz) / 7 (2600 MHz) / 8 (900 MHz) / 20 (800 MHz) / 28 (700 MHz) / 32 (1500 MHz)</td></tr><tr><td>**LTE 頻段（TDD）**</td><td>38 (2600 MHz) / 40 (2300 MHz) / 41 (2500 MHz)</td></tr><tr><td>**無線 2.4 GHz**</td><td>574 Mbit/s，2 條鏈，802.11b/g/n/ax，6.9 dBi，IPQ-5010，Wi-Fi 6</td></tr><tr><td>**無線 5 GHz**</td><td>1200 Mbit/s，2 條鏈，802.11a/n/ac/ax，7 dBi，QCN-6102，Wi-Fi 6</td></tr><tr><td>**天線（2.4 GHz）**</td><td>內建天線，增益 6.9 dBi</td></tr><tr><td>**天線（5 GHz）**</td><td>內建天線，增益 7 dBi</td></tr><tr><td>**LTE 天線**</td><td>內建定向 LTE 天線</td></tr><tr><td>**復位按鈕**</td><td>多功能復位按鈕，用於重設配置、CAP 模式和 Netinstall</td></tr><tr><td>**模式按鈕**</td><td>可配置的軟體控制按鈕</td></tr><tr><td>**LED 指示燈**</td><td>使用者 LED 和介面狀態 LED</td></tr><tr><td>**PoE 輸入**</td><td>乙太網埠 1 支援 802.3af/at PoE 輸入</td></tr><tr><td>**直流電源輸入**</td><td>DC 插孔，輸入範圍 12–57 V</td></tr><tr><td>**防護等級**</td><td>IP66</td></tr></tbody></table>

![](/img/2f2676f1070e6fe5.webp)

## 配置 {#configuration}

完整的 RouterOS 文件位於此處：[https://mt.lv/help](https://mt.lv/help)。裝置已預配置為 LTE CPE 路由器：**LTE 介面** 作為受保護的 WAN 並啟用 DHCP，而 LAN 網橋 192.168.88.1/24 提供 DHCP 和 DNS 服務。雙頻戶外 Wi-Fi（2.4 GHz 和 5 GHz ax）已啟用，採用 WPA2/WPA3 安全機制。

要訪問裝置，請透過任意乙太網埠連線，或加入名為 "MikroTik‑…" 的預設 Wi‑Fi 網路。Wi‑Fi 密碼印在裝置附帶的貼紙上。

您可以透過移動應用程式、網頁瀏覽器中的 WebFig 或 WinBox 工具（可從 [https://mt.lv/winbox/](https://mt.lv/winbox/) 獲取）使用預設 IP 地址 **192.168.88.1** 來管理裝置。如果該地址不可達，請開啟 WinBox，進入 Neighbors 標籤頁，發現該裝置。

如需恢復，可使用復位按鈕透過網路重新安裝韌體。

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三個功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 持續按住復位按鈕，直到 LED 變為常亮，然後鬆開即可啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議在其中一個無法工作時對兩個選項都進行驗證。

- **Regular Booter:** 要進入 etherboot 模式，請在給裝置通電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter:** 關閉裝置。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，可透過 Netinstall 重新安裝 RouterOS。視型號而定，這可能由 **USR, USER, System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置上電之前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這可用於 RouterBOOT 偵錯和恢復。

## 隨附部件 {#included-parts}

![](/img/16ac040953ba53be.webp)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列在 **/system resource** 中。其他作業系統尚未經過測試。
