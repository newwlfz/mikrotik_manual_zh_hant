---
title: "CRS328-4C-20S-4S+RM"
slug: /crs328-4c-20s-4s-plus-rm
source: https://manual.mikrotik.com/hardware/crs328-4c-20s-4s-plus-rm
captured_at: '2026-11-04T09:46:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/9b881b49523c4a97.jpg)

智慧交換器，20 個 SFP 籠、4 個 SFP+ 籠、4 個 Combo 埠（千兆乙太網或 SFP）、800MHz CPU、512MB RAM、1U 機架式機箱、雙電源、RouterOS L5 或 SwitchOS（雙啟動）。完整規格和產品手冊請參見 [CRS328-4C-20S-4S+RM 產品頁面](https://mikrotik.com/product/crs328_4c_20s_4s_rm)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵守所有國家法律和法規。裝置的安裝必須符合當地和國家的電氣規範。本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會給人員帶來危險情況並損壞系統。本產品適合在室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。請僅使用製造商認可的電源和附件，這些可在本產品的原始包裝中找到。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！如果裝置發生故障，請斷開其電源。最快的做法是將電源插頭從電源插座中拔出。客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 用您的 PC 連線到任意一個乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，即可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

- 裝置可透過兩個 IEC 介面供電。交流輸入範圍 100-240 V ⏦。最大負載下的功耗可達 43 W。

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件請參見：[https://mt.lv/help](https://mt.lv/help) 您可以使用網頁瀏覽器中的 WebFig 或 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方式以確保可訪問性。** **要開始設定，請在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）。裝置配備 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。出於恢復目的，可以從網路重新安裝裝置，請參見 Reset 按鈕。

Marvell Prestera 交換晶片功能使用者手冊

裝置支援啟動 RouterOS（用於完整的路由和交換功能）或 SwOS（僅用於交換執行）。預設情況下，裝置啟動進入 RouterOS，但您也可以按以下方式切換到另一個作業系統：

- 從 SwOS：進入 System 選單，點選頁面底部的 Boot RouterOS 按鈕。
- 從 RouterOS：開啟 System → RouterBOARD → Settings 並選擇 Boot OS。也可以透過序列埠控制檯選單選擇作業系統並配置其他啟動選項。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<table><thead><tr><th>**產品程式碼**</th><th>CRS328-4C-20S-4S+RM</th></tr></thead><tbody><tr><td>**CPU**</td><td>98DX3236, 800 MHz</td></tr><tr><td>**CPU 架構**</td><td>ARM 32bit</td></tr><tr><td>**CPU 核心數**</td><td>2</td></tr><tr><td>**交換晶片型號**</td><td>98DX3236</td></tr><tr><td>**RAM**</td><td>512 MB</td></tr><tr><td>**儲存**</td><td>16 MB Flash</td></tr><tr><td>**Combo 乙太網/SFP 埠**</td><td>4</td></tr><tr><td>**SFP 埠**</td><td>20</td></tr><tr><td>**SFP+ 埠**</td><td>4</td></tr><tr><td>**序列埠控制檯 (RJ45)**</td><td>1</td></tr><tr><td>**作業系統**</td><td>RouterOS（許可證等級 5）/ SwitchOS（雙啟動）</td></tr><tr><td>**工作溫度**</td><td>-20 °C 至 +60 °C</td></tr><tr><td>**機箱尺寸**</td><td>443 × 194 × 44 mm</td></tr></tbody></table>

請訪問幫助頁面檢視 MikroTik SFP 模組相容性表：MikroTik 有線介面相容性

## Combo 埠 {#combo-ports}

四個 combo 介面各有兩個物理聯結器，同一時間只能使用其中一個。在 RouterOS 中，這些埠會自動錶示為 combo1-4。可以在 RouterOS 軟體的 Ethernet 選單中選擇使用哪個物理埠。如果保持預設的 "auto"，並且 F/T 兩端都插了線纜，則 SFP 優先。例如，如果您在 1T 埠插入了乙太網線，並在 1F 埠插入了 SFP 模組，則必須在 RouterOS 中選擇使用哪一個。在 RouterOS GUI 中雙擊相應的 combo 介面即可檢視使用的是哪個插槽。

## 安裝 {#mounting}

本裝置設計用於室內使用，可以使用隨附的機架安裝件安裝在機架式機箱中，也可以放置在桌面上。如果希望放置在平面上，請在路由器底部貼上橡膠腳墊；如果指定用於機架式機箱，請使用十字螺絲刀將機架耳安裝在裝置兩側：

- 將機架耳安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如圖所示。
- 將裝置放入機架式機箱，並對齊孔位，使裝置能夠方便地裝入。

![](/img/837a6d2bb5f312fe.webp)

- 擰緊螺絲將其固定到位。本裝置的 IP 防護等級為 IPX0。裝置沒有防水汙染保護，請確保將裝置放置在乾燥通風的環境中。*本裝置的安裝和配置應由合格人員完成。* *我們建議為我們的裝置使用 Cat6 網線。*

## 按鈕和跳線 {#buttons-and-jumpers}

### Reset 按鈕 {#reset-button}

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 搜尋 Netinstall 伺服器（共 15 秒）。**Netinstall 過程使用第一個乙太網埠（combo-ether1）。** 關於使用 Netinstall 恢復工具的說明，請參見 RouterOS 文件。無論使用上述哪種方式，如果在裝置通電前按下該按鈕，系統都會載入備份的 RouterBOOT 載入程式。用於 RouterBOOT 偵錯和恢復。

### Mode 按鈕 {#mode-button}

可以透過 RouterOS 軟體配置 mode 按鈕的動作，以執行任何使用者提供的 RouterOS 指令碼。配置時請使用選單 /system routerboard mode-button

![](/img/ea2449a97b0b8831.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。
