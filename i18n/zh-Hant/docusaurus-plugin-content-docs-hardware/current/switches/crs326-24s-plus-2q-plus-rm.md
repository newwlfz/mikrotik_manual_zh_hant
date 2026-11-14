---
title: "CRS326-24S+2Q+RM"
slug: /crs326-24s-plus-2q-plus-rm
source: https://manual.mikrotik.com/hardware/crs326-24s-plus-2q-plus-rm
captured_at: '2026-11-04T09:46:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/9ab3febba35a1f79.webp)

## [CRS326-24S+2Q+RM](https://mikrotik.com/product/crs326_24s_2q_rm) {#crs326-24s2qrm}

CRS326 是一款帶有 24 個 10G SFP+ 埠和兩個 QSFP+ 40G 埠的網路交換器。該裝置可直接作為交換器使用。完整規格和產品手冊請參見 [CRS326-24S+2Q+RM 產品頁面](https://mikrotik.com/product/crs326_24s_2q_rm)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於機架安裝。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或未遵循正確的步驟可能導致人員危險和系統損壞。
- 本產品適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 若裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將您的 PC 連線到乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 配置應使用 Web 瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方式以確保可訪問性；**
- 在 Web 瀏覽器中開啟 https://192.168.88.1 以開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後透過 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，然後在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保最佳的效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內使用。可使用隨附的機架支架將其安裝在機架機箱中，或放置在桌面上。桌面使用時，請將橡膠腳墊安裝到裝置底部；機架安裝時，請使用十字螺絲刀將機架耳片安裝到兩側：

- 將機架耳片安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如圖所示；
- 將裝置放入機架機箱並對齊螺孔，使其安裝順暢；
- 擰緊螺絲將其固定到位。

![](/img/837a6d2bb5f312fe.webp)

本裝置的 IP 防護等級為 IPX0。裝置沒有防水保護，請確保將裝置放置在乾燥通風的環境中。

本裝置的安裝和配置應由合格人員進行。我們建議為我們的裝置使用 Cat5/6 網線。

## 供電 {#powering}

本裝置由兩個 100-240 V AC 輸入供電。

本裝置在最大負載下的功耗最高為 42 W。帶附加裝置時最高為 69 W。

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件可在 [https://mt.lv/help](https://mt.lv/help) 獲取。裝置可使用 Web 瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方式以確保可訪問性。**

在 Web 瀏覽器中開啟 https://192.168.88.1 以開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後透過 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。

本裝置配備一個 RJ45 序列埠控制檯埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。為便於恢復，可以透過網路重新安裝裝置，請參閱復位按鈕。

Marvell Prestera 交換晶片的功能在 [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) 手冊中有描述。

裝置支援啟動 RouterOS 或 SwOS。預設情況下，裝置啟動進入 RouterOS。要切換到另一個作業系統：

- 從 SwOS 中：進入 **System** 選單，點選頁面底部的 "**Boot RouterOS**" 按鈕；
- 從 RouterOS 中：開啟 **System → RouterBOARD → Settings** 並選擇 **Boot OS**。

也可以使用序列埠控制檯選單選擇作業系統並配置其他啟動選項。

## 規格 {#specifications}

<table><thead><tr><th>**產品程式碼**</th><th>CRS326-24S+2Q+RM</th></tr></thead><tbody><tr><td>**CPU**</td><td>QCA9531, 650 MHz</td></tr><tr><td>**CPU 架構**</td><td>MIPSBE</td></tr><tr><td>**CPU 核心數**</td><td>1</td></tr><tr><td>**交換晶片型號**</td><td>98DX8332</td></tr><tr><td>**RAM**</td><td>128 MB（早期硬體版本為 64 MB）</td></tr><tr><td>**儲存**</td><td>16 MB Flash</td></tr><tr><td>**10/100 乙太網 (RJ45)**</td><td>1</td></tr><tr><td>**10G SFP+ 埠**</td><td>24</td></tr><tr><td>**40G QSFP+ 埠**</td><td>2</td></tr><tr><td>**USB Type-A 埠**</td><td>1</td></tr><tr><td>**序列埠控制檯 (RJ45)**</td><td>1</td></tr><tr><td>**作業系統**</td><td>RouterOS v7（許可證級別 5）/ SwOS（雙啟動）</td></tr><tr><td>**工作溫度**</td><td>-20 °C 至 +60 °C</td></tr><tr><td>**機殼尺寸**</td><td>443 × 200 × 44 mm</td></tr></tbody></table>

支援的 SFP 模組請參見 [MikroTik wired interface compatibility](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。

## 復位按鈕 {#reset-button}

- 要重設配置，請斷開裝置電源，按住復位按鈕，並在 USER (USR) LED 開始閃爍時鬆開；
- 要載入備份載入程式，請在接通電源之前按住復位按鈕，三秒後鬆開；
- 要啟動 Netinstall 流程（以 BOOTP 模式啟動裝置以重新安裝 RouterOS），請按住復位按鈕，給裝置上電，等待 USER (USR) LED 閃爍後變為常亮。當 USR LED 熄滅時，鬆開復位按鈕。

無論使用上述哪種方式，如果在裝置接通電源之前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下配件：

![](/img/10495ba102c10e83.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本以及 SwOS。具體的出廠預裝 RouterOS 版本列在 /system resource 中。其他作業系統尚未經過測試。
