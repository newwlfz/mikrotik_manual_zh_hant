---
title: "LAMP 5G R16"
slug: /lamp-5g-r16
source: https://manual.mikrotik.com/hardware/lamp-5g-r16
captured_at: '2026-11-04T09:53:09+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/861b3d16ec018683.webp)

## [LAMP 5G R16](https://mikrotik.com/product/lamp_5g_r16)（LAMPGM&RG520F-EU） {#lamp-5g-r16-lampgmrg520f-eu}

這是一款堅固的戶外 5G 裝置，使用全向天線和內建 eSIM 支援，可自動連線到可用的最佳基站——無需調整天線方向，也無需更換物理 SIM 卡。IP67 防護等級、海洋級耐用性、GNSS、PoE 輸入。完整規格和產品手冊請參見 [LAMP 5G R16 產品頁面](https://mikrotik.com/product/lamp_5g_r16)。

## 安全警告 {#safety-warnings}

- 在對任何 MikroTik 裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。
- 僅使用製造商批准的電源和配件，這些可在本產品的原包裝中找到。
- 本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責確保裝置安裝符合當地和國家的電氣規範。
- 請勿嘗試拆卸、修理或改裝裝置。如需服務，請聯絡 MikroTik 支援。
- 本產品設計為安裝在戶外的立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險情況並對系統造成損壞。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 插座應安裝在裝置附近且易於觸及的位置。
- 如果裝置出現故障，請斷開其電源。最快的方法是將電源介面卡從電源插座上拔下。
- 本產品為 A 類產品。在居住環境中，本產品可能引起無線電干擾，此時使用者可能需要採取適當的措施。
- 為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如在指定區域處置。請熟悉將裝置正確運送到您所在地區指定收集點的流程

## 快速開始 {#quickstart}

- 開啟乙太網埠蓋；
- 按照裝置上的指示將 SIM 卡插入卡槽；
- 使用乙太網線將裝置連線到隨附 PoE 注入器的資料+電源端；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 使用 Web 瀏覽器透過 WebFig 或 WinBox 工具 [https://mt.lv/WinBox](https://mt.lv/WinBox) 配置您的裝置；提供多種配置方法以確保可訪問性；
- 開啟 [https://192.168.188.1](https://192.168.188.1) 訪問 WebFig，對於 WinBox，請下載該工具，導航到 Neighbors 標籤頁，然後選擇 MAC 地址。使用者名稱為 "admin"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 選擇"Check for updates"按鈕，將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡並具有活動的 Internet 連線；
- 要手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在"Downloads"部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的"Files"選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

- 直流輸入數量：1（PoE-IN）。
- PoE 輸入：802.3 af/at。
- PoE 輸入電壓：12-56 V。
- 電源介面卡額定電流：0.5 A。
- 無配件時最大功耗：10 W。
- 最大功耗：10 W。

## 安裝 {#mounting}

![](/img/f97edacf013f52ed.png)

### 立杆安裝 {#pole-mounting}

- 使用隨附的螺釘將安裝支架固定到裝置上。

![](/img/034bfc999d870964.png)

- 使用 U 型螺栓以及隨附的墊圈和螺母將支架固定到立杆上。

![](/img/f170f1179619f879.png)

- 將裝置安裝到立杆上，使乙太網埠朝下。
- 使用 PH2 螺絲刀擰緊環扣。
- 支援的立杆直徑為 Ø 25–60 mm。

### 壁掛安裝 {#wall-mounting}

- 使用隨附的螺釘將安裝支架固定到裝置上。

![](/img/034bfc999d870964.png)

- 鑽 Ø 6 mm 的孔用於安裝牆塞。

![](/img/f910583dba897c50.png)

- 插入牆塞，並使用隨附的螺釘將安裝支架固定到牆上。

![](/img/86704f48d278dcd5.png)

:::warning 警告

請按照圖示垂直安裝本產品。

:::

- 使用紮帶將乙太網線固定到立杆上，距裝置不超過一米，以免線纜被從埠中拉出。若要使用預製的乙太網線，必須先切開橡膠密封件。或者，在連線 RJ45 接頭之前先將線纜穿過橡膠密封件。
- 請勿使用不帶橡膠密封件的線纜，否則將影響 IP67 防護等級。
- 檢查安裝角度和位置。
- 在戶外安裝時，確保所有線纜開口朝下。使用 PoE 注入器並正確接地，本裝置在埠蓋下方設有專門設計的接地聯結器。建議使用遮蔽 Cat5/6 線纜。本裝置的 IP 防護等級為 IP67。

## 配置 {#configuration}

可以透過 Web 瀏覽器使用 WebFig 進行配置，也可使用 WinBox 工具 [https://mt.lv/winbox](https://mt.lv/winbox)，多種方法可確保可訪問性。

- 要訪問 WebFig，請在瀏覽器中開啟 [https://192.168.188.1](https://192.168.188.1)。
- 對於 WinBox，請下載該工具，轉到 Neighbors 標籤頁，然後選擇 MAC 地址。預設使用者名稱為 "admin"，**請在裝置貼紙上查詢密碼**。
- 您應經常檢查更新，以確保您的 RouterOS 軟體保持最新，從而獲得最佳效能和穩定性。在 WinBox 或 WebFig 中選擇"Check for updates"按鈕以更新到最新版本。

必須插入有效的 SIM 卡或設定 eSIM，並具有活動的 Internet 連線，更新才能正常工作。

RouterOS 提供的配置選項遠不止本文件所述。我們建議訪問 [https://mt.lv/help](https://mt.lv/help) 瞭解這些功能。

出於恢復目的，可以引導裝置進行重新安裝，請參見相應章節。

## eSIM 設定 {#esim-settings}

預設情況下，裝置配置為使用 SIM 卡槽。要使用板載 eSIM，請使用以下命令切換卡槽：**/interface/lte/settings/set sim-slot=esim**

單個 eSIM 晶片可以儲存多個 eSIM 配置檔案，最大配置檔案數量取決於所使用的 eSIM 晶片。

詳情請參見 [LTE eSIM](/docs/mobile-networking/lte-5g#lte-esim) 頁面。

## Reset 按鈕 {#reset-button}

Reset 按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置將開始查詢 CAPsMAN 伺服器（共 10 秒）。
- 使用 Netinstall 重新安裝 RouterOS。要使用 Netinstall 實用程式重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種可用的載入程式：常規載入程式和備用載入程式。常規載入程式——給裝置上電，等待 1-2 秒，然後按住 Reset 按鈕。等待直到 "USR" LED 閃爍，然後變為常亮"On"。當 "USR" LED 變為"Off"時，鬆開 Reset 按鈕——裝置將進入 BOOTP 模式。
- 備用載入程式——關閉裝置電源，按住 Reset 按鈕，然後給裝置上電。等待直到 "USR" LED 閃爍，然後變為常亮"On"。當 "USR" LED 變為"Off"時，鬆開 Reset 按鈕——裝置將使用備用載入程式進入 BOOTP 模式。

無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

Netinstall：執行 Netinstall 時，請確保 ROS 檔案和 Netinstall 軟體均使用最新的 v7 版本。

## 接地 {#grounding}

本裝置包含一個接地連線（標記為 ⏚），您應將其連線到裝置使用所在地的塔架或建築物的接地裝置。這可大幅降低靜電放電和雷擊損壞的風險。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- 24 V 0.5 A 電源介面卡
- LAMP 安裝支架
- 千兆 PoE 注入器

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼：**LAMPGM&RG520F-EU.**
- CPU 雙核：88F3720 800 MHz
- CPU 架構：ARM 64bit
- RAM 容量：512 MB
- RAM 型別：DDR3L
- 儲存：32 MB，Flash
- 1G 乙太網埠數量：1
- LTE 類別：20（下行 2.0 Gbps，上行 200 Mbps）
- LTE 調變解調器：RG520F-EU
- TAC：86945405
- 5G SA 類別：下行 4.2 Gbps，上行 900 Mbps。
- 5G NSA 類別：下行 5.0 Gbps，上行 650 Mbps。
- 3G 類別：R8（下行 42.2Mbps，上行 5.76Mbps）。
- MIMO 下行：4x4。
- 5G SA FDD 頻段：1 (2100 MHz) / 3 (1800 MHz) / 5 (850 MHz) / 7 (2600 MHz) / 8 (900 MHz) / 20 (800 MHz) / 28 (700 MHz)。
- 5G SA TDD 頻段：38 (2600 MHz) / 40 (2300 MHz) / 41 (2500 MHz) / 75 (1500 MHz) / 76 (1500 MHz) / 77 (3700 MHz) / 78 (3500 MHz)。
- 5G NSA FDD 頻段：1 (2100 MHz) / 3 (1800 MHz) / 5 (850 MHz) / 7 (2600 MHz) / 8 (900 MHz) / 20 (800 MHz) / 28 (700 MHz)。
- 5G NSA TDD 頻段：38 (2600 MHz) / 40 (2300 MHz) / 41 (2500 MHz) / 75 (1500 MHz) / 76 (1500 MHz) / 77 (3700 MHz) / 78 (3500 MHz)。
- LTE FDD 頻段：1 (2100 MHz) / 3 (1800 MHz) / 5 (850 MHz) / 7 (2600 MHz) / 8 (900 MHz) / 20 (800 MHz) / 28 (700 MHz) / 32 (1500 MHz)。
- LTE TDD 頻段：38 (2600 MHz) / 40 (2300 MHz) / 41 (2500 MHz) / 42 (3500 MHz) / 43 (3700 MHz)。
- 3G 頻段：1 (2100 MHz) / 5 (850 MHz) / 8 (900 MHz)。
- 尺寸：311 x 311 x 179 mm。
- 作業系統：RouterOS 版本 7，許可證級別 3
- 工作溫度 -40°C 至 +70°C

## SIM 卡槽使用 {#sim-slot-usage}

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡的厚度不同，不建議配合轉接器使用。

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>說明</th></tr></thead><tbody><tr><td>產品程式碼</td><td>LAMPGM&RG520F-EU</td></tr><tr><td>**架構**</td><td>ARM 64bit</td></tr><tr><td>**CPU**</td><td>88F3720</td></tr><tr><td>**CPU 核心數**</td><td>2</td></tr><tr><td>**CPU 標稱頻率**</td><td>800 MHz</td></tr><tr><td>**CPU 執行緒數**</td><td>2</td></tr><tr><td>**RouterOS 許可證**</td><td>Level 3</td></tr><tr><td>**作業系統**</td><td>RouterOS v7</td></tr><tr><td>**RAM**</td><td>512 MB</td></tr><tr><td>**儲存**</td><td>32 MB FLASH</td></tr><tr><td>**MTBF**</td><td>25°C 下約 200'000 小時</td></tr><tr><td>**工作溫度**</td><td>-40°C 至 +70°C</td></tr><tr><td>**最大功耗**</td><td>10 W</td></tr><tr><td>**無附件時最大功耗**</td><td>10 W</td></tr><tr><td>**電源**</td><td>PoE-IN，12–56 V</td></tr><tr><td>**PoE 輸入**</td><td>802.3af/at</td></tr><tr><td>**散熱**</td><td>被動散熱</td></tr><tr><td>**乙太網**</td><td>1 × 10/100/1000 Mbps</td></tr><tr><td>**帶反向 PoE (PoE-in) 的 1G 乙太網埠數量**</td><td>1</td></tr><tr><td>**SIM**</td><td>1 個調變解調器（Micro SIM）</td></tr><tr><td>**eSIM**</td><td>是</td></tr><tr><td>**M.2 插槽**</td><td>1</td></tr><tr><td>**行動網路：3G**</td><td>Category R8（下行：42.2 Mbps；上行：5.76 Mbps）</td></tr><tr><td>**3G 頻段**</td><td>1 (2100 MHz)、5 (850 MHz)、8 (900 MHz)</td></tr><tr><td>**行動網路：LTE**</td><td>Category 20（下行：2.0 Gbps；上行：200 Mbps）</td></tr><tr><td>**MIMO**</td><td>下行 4×4，上行 2×2</td></tr><tr><td>**LTE FDD 頻段**</td><td>1 (2100 MHz)、3 (1800 MHz)、5 (850 MHz)、7 (2600 MHz)、8 (900 MHz)、20 (800 MHz)、28 (700 MHz)、32 (1500 MHz)</td></tr><tr><td>**LTE TDD 頻段**</td><td>38 (2600 MHz)、40 (2300 MHz)、41 (2500 MHz)、42 (3500 MHz)、43 (3700 MHz)</td></tr><tr><td>**5G NSA FDD 頻段**</td><td>1 (2100 MHz)、3 (1800 MHz)、5 (850 MHz)、7 (2600 MHz)、8 (900 MHz)、20 (800 MHz)、28 (700 MHz)</td></tr><tr><td>**5G NSA TDD 頻段**</td><td>38 (2600 MHz)、40 (2300 MHz)、41 (2500 MHz)、75 (1500 MHz)、76 (1500 MHz)、77 (3700 MHz)、78 (3500 MHz)</td></tr><tr><td>**5G SA FDD 頻段**</td><td>1 (2100 MHz)、3 (1800 MHz)、5 (850 MHz)、7 (2600 MHz)、8 (900 MHz)、20 (800 MHz)、28 (700 MHz)</td></tr><tr><td>**5G SA TDD 頻段**</td><td>38 (2600 MHz)、40 (2300 MHz)、41 (2500 MHz)、75 (1500 MHz)、76 (1500 MHz)、77 (3700 MHz)、78 (3500 MHz)</td></tr><tr><td>**TAC**</td><td>86945405</td></tr><tr><td>**IP 防護等級**</td><td>IP67</td></tr><tr><td>**認證**</td><td>CE、EAC、ROHS</td></tr></tbody></table>

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

有關重要的安全說明和法規認證，請參閱 [https://mikrotik.com/products](https://mikrotik.com/products) 上提供的 Safety and Regulatory Information 文件。導航至：Support & Downloads → Safety and Regulatory Information
