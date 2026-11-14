---
title: "CRS328-24P-4S+RM"
slug: /crs328-24p-4s-plus-rm
source: https://manual.mikrotik.com/hardware/crs328-24p-4s-plus-rm
captured_at: '2026-11-04T09:46:40+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/7e3f0e1ac8101182.jpg)

24 埠千兆乙太網路由器/交換器，配四個 10Gbps SFP+ 埠，1U 機架式機箱，雙啟動與 PoE 輸出，500W。完整規格與宣傳資料請參見 [CRS328-24P-4S+RM 產品頁面](https://mikrotik.com/product/crs328_24p_4s_rm)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵循所有國家法律和法規。裝置的安裝必須符合當地和國家電氣規範。本裝置用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟，可能導致人員處於危險境地並對系統造成損壞。本產品僅用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。僅使用製造商認可的電源和配件，它們可在本產品的原包裝中找到。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，操作風險自負！如果裝置發生故障，請斷開其電源。最快的做法是從電源插座上拔下電源插頭。客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 使用您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在 Web 瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 以開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後透過 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分中找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定路由器的密碼。

## 安裝 {#mounting}

本裝置設計用於室內，可使用隨附的機架安裝件安裝在機架式機箱中，也可以放置在桌面上。如果希望放置在平坦表面上，請在路由器底部貼上橡膠腳墊；如果指定用於機架式機箱，請使用十字螺絲刀將機架安裝耳片固定到裝置兩側：

- 將機架耳片安裝到裝置兩側，並擰緊四顆螺釘將其固定到位，如圖所示。

![](/img/837a6d2bb5f312fe.webp)

- 將裝置放入機架式機箱並對齊孔位，使裝置能夠方便地安裝到位。
- 擰緊螺釘將其固定到位。本裝置沒有防水汙染保護，請確保將裝置放置在乾燥通風的環境中。我們建議為我們的裝置使用 Cat6 網線。本裝置的安裝和配置應由具備資質的人員完成。

## 供電 {#powering}

本裝置配備一個 IEC 型交流電源輸入，支援 100-240 V **⏦** 供電（~ 50/60 Hz，最大 7 A）。本裝置自身在最大負載下的功耗最高為 44 W。

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件可在以下地址獲取：[https://mt.lv/help](https://mt.lv/help) 您可以在 Web 瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方式以確保可訪問性。** **要開始設定，請在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 以開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後透過 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。本裝置配備一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。出於恢復目的，可以從網路重新安裝裝置，請參閱 Reset 按鈕。

Marvell Prestera 交換晶片功能使用者手冊

本裝置支援引導 RouterOS（用於完整路由和交換功能）或 SwOS（僅用於交換執行）。預設情況下，裝置引導進入 RouterOS，但您可以按以下方式切換到另一個作業系統：

- 從 SwOS 中：轉到 System 選單，點選頁面底部的 Boot RouterOS 按鈕。
- 從 RouterOS 中：開啟 System → RouterBOARD → Settings 並選擇 Boot OS。也可以使用序列控制檯選單選擇作業系統並配置其他引導選項。

## 電源輸出 {#power-output}

本裝置可以透過其乙太網埠向外部裝置提供 PoE 供電。輸出電壓將根據所連線裝置所需的電壓型別自動選擇。本裝置既可為 802.3af/at 裝置供電，也可為接受被動 PoE 供電的裝置供電。如有必要，可以手動切換輸出電壓。預設情況下，PoE 模式設定為 auto，它不會損壞裝置，並會自動檢測支援 PoE 且需要相應電壓的裝置。一旦檢測到 PoE 裝置，就會為其供電，PoE LED 也會亮起。PoE 輸出埠分為三個 PoE 輸出組，每組 8 個埠（PSE8）。裝置 PoE 總限制 = 450w（每個 PSE8 組 150w）。每個埠在高電壓下可提供最高 30 W，在低電壓輸出下可提供 26,5 W。

## 按鈕和跳線 {#buttons-and-jumpers}

**Reset 按鈕**：

- 在引導期間按住此按鈕，直到 USR LED 指示燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住按鈕 5 秒以上，或直到使用者 LED 熄滅，然後鬆開，以讓 RouterBOARD 查詢 Netinstall 伺服器。**第一個乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。無論採用上述哪種方式，如果在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。請在 LED 開始閃爍之前鬆開按鈕，以僅載入備份 RouterBOOT 而不進行重設。這對 RouterBOOT 的偵錯和恢復很有用。**Mode 按鈕：** Mode 按鈕的動作可以透過 RouterOS 軟體配置，以執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。Mode 按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<table><thead><tr><th>**產品程式碼**</th><th>CRS328-24P-4S+RM</th></tr></thead><tbody><tr><td>**CPU**</td><td>98DX3236, 800 MHz</td></tr><tr><td>**CPU 架構**</td><td>ARM 32bit</td></tr><tr><td>**CPU 核心數**</td><td>1</td></tr><tr><td>**交換晶片型號**</td><td>98DX3236</td></tr><tr><td>**RAM**</td><td>512 MB</td></tr><tr><td>**儲存**</td><td>16 MB Flash</td></tr><tr><td>**1G 乙太網（RJ45）埠**</td><td>24</td></tr><tr><td>**10G SFP+ 埠**</td><td>4</td></tr><tr><td>**序列控制檯（RJ45）**</td><td>1</td></tr><tr><td>**作業系統**</td><td>RouterOS（license level 5）/ SwitchOS（雙啟動）</td></tr><tr><td>**工作溫度**</td><td>-20 °C 至 +60 °C（已測試）</td></tr><tr><td>**機箱尺寸**</td><td>443 × 300 × 44 mm</td></tr><tr><td>**PoE 輸出支援**</td><td>802.3af/at，全部 24 個乙太網埠支援被動 PoE</td></tr></tbody></table>

有關 MikroTik SFP 模組相容性表，請訪問幫助頁面：MikroTik 有線介面相容性

## LED 指示燈 {#led-indicators}

- 路由器通電時 PWR LED 亮起。
- LED 的使用可透過 RouterOS 配置。
- 三角形 LED（上排）指示 PoE 輸出狀態。綠色 LED 表示相應埠使用低電壓，紅色 LED 表示高電壓。單個綠色 LED 閃爍：啟動低電壓裝置時出現問題。單個紅色 LED 閃爍：高電壓裝置出現問題。
- 方形埠 LED（下排）指示各乙太網、SFP 埠的活動。
- FAN FAULT LED 表示任一散熱風扇出現問題。
- PoE FAULT LED 表示超出了整體最大 PoE 輸出限制。埠 PoE 輸出優先順序將在 3 個獨立區段（每段 8 個埠）中生效，任何區段超過 150W 消耗時都會發生過載

## 配件 {#accessories}

包裝中包含隨裝置提供的以下配件：

![](/img/185d3677850674bc.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。
