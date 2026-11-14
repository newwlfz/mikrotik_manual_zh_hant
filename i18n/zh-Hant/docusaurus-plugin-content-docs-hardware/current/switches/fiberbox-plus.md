---
title: "FiberBox Plus"
slug: /fiberbox-plus
source: https://manual.mikrotik.com/hardware/fiberbox-plus
captured_at: '2026-11-04T09:48:15+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/9bbf101a7bc9df03.jpg)

萬兆室外網路的極致價效比之選。高杆、立杆或鐵塔——您的連線安全無虞！netFiber 9 的高效能經濟版本。請參閱 [FiberBox Plus 產品頁面](https://mikrotik.com/product/fiberboxplus) 瞭解完整規格和宣傳冊。

### FiberBox Plus (CRS305-1G-4S+OUT) {#fiberbox-plus-crs305-1g-4sout}

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵守所有國家法律法規。裝置的安裝必須符合當地和國家的電氣規範。本裝置設計為安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟可能導致人身危險和系統損壞。本產品適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。請僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 用您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（某些型號請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

250

## 供電 {#powering}

- DC 輸入數量 3（PoE-in、DC 插孔、2 針端子）
- PoE-in 輸入電壓 42-57 V 802.3af/at
- DC 插孔輸入電壓 24-57 V
- 2 針端子輸入電壓 24-57 V
- 電源介面卡額定電壓 48 V
- 電源介面卡額定電流 1.2 A
- 最大功耗（不含附加模組）7 W
- 最大功耗 17 W
- -48V 供電與 PoE-in 和 +24V（或任何其他負極接地的 PSU）不相容！我們強烈建議使用隨附的電源。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 POE 介面卡的 POE 埠。
- 將來自您區域網路的乙太網線連線到 POE 介面卡的 LAN 埠，請注意資料和電力流向的箭頭。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

RouterOS 的完整文件可在以下地址獲取：[https://mt.lv/help](https://mt.lv/help) 您可以使用網頁瀏覽器中的 WebFig 或 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方式以確保可訪問性。** **要開始設定，請在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（某些型號請檢視貼紙上的使用者和無線密碼）。該裝置配備一個 RJ45 序列埠，預設為 115200 bit/s，8 個數據位，1 個停止位，無奇偶校驗。出於恢復目的，可以從網路重新安裝裝置，請參見復位按鈕。

Marvell Prestera 交換晶片功能使用者手冊

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<table><thead><tr><th>**產品程式碼**</th><th>CRS305‑1G‑4S+OUT (FiberBox Plus)</th></tr></thead><tbody><tr><td>**CPU**</td><td>98DX226S, 800 MHz</td></tr><tr><td>**CPU 架構**</td><td>ARM 32bit</td></tr><tr><td>**CPU 核心數量**</td><td>2</td></tr><tr><td>**交換晶片型號**</td><td>98DX226S</td></tr><tr><td>**RAM**</td><td>256 MB</td></tr><tr><td>**儲存**</td><td>16 MB Flash</td></tr><tr><td>**1G 乙太網 (RJ45)**</td><td>1</td></tr><tr><td>**10G SFP+ 埠**</td><td>4</td></tr><tr><td>**序列控制檯 (RJ45)**</td><td>1</td></tr><tr><td>**作業系統**</td><td>RouterOS v7（license level 5）/ SwOS（雙啟動）</td></tr><tr><td>**工作溫度**</td><td>‑40 °C 至 +70 °C</td></tr><tr><td>**外殼尺寸**</td><td>330 × 200 × 70 mm</td></tr><tr><td>**防護等級**</td><td>IP66</td></tr></tbody></table>

## 復位按鈕 {#reset-button}

要使用復位按鈕，請按住它，然後在仍按住按鈕的情況下開啟裝置。

- 當綠色 LED 開始閃爍時鬆開按鈕，以重設 RouterOS 配置。如果不想載入備份載入程式，可以在已通電後再開始按住按鈕。
- 在 LED 不再閃爍（約 20 秒）後鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。您也可以在裝置出現在 Netinstall 實用程式裝置列表時鬆開按鈕。無論採用上述哪種方式，如果在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

![](/img/24bdf7855d251582.webp)

有關 MikroTik SFP 模組相容性和配置表，請訪問幫助頁面：MikroTik 有線介面相容性

## 作業系統支援 {#operating-system-support}

該裝置支援與 SwOS 2.9 及更高版本以及 RouterOS 7 或更高版本的雙啟動。出廠安裝的具體 RouterOS 版本可在 RouterOS 的 /system resource 選單中檢視。其他作業系統未經測試，也不受官方支援。
