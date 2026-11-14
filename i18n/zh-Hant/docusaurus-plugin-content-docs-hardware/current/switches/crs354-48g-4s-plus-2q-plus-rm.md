---
title: "CRS354-48G-4S+2Q+RM"
slug: /crs354-48g-4s-plus-2q-plus-rm
source: https://manual.mikrotik.com/hardware/crs354-48g-4s-plus-2q-plus-rm
captured_at: '2026-11-04T09:46:43+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/5575241f758f436d.jpg)

CRS354-48G-4S+2Q+RM 是一款網路交換器，具有 48 個千兆埠、四個 10G SFP+ 埠和兩個 40G QSFP+ 埠。該裝置可直接作為交換器使用。有關完整規格和宣傳冊，請參閱 [CRS354-48G-4S+2Q+RM 產品頁面](https://mikrotik.com/product/crs354_48g_4splus2qplusrm)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵守所有國家法律和法規。裝置的安裝必須符合當地和國家電氣規範。本機適用於安裝在機架中。開始安裝前，請仔細閱讀安裝說明。使用不正確的硬體或不遵循正確的操作步驟，可能會對人員造成危險並損壞系統。本產品適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。請僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。連線系統電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置出現故障，請斷開其電源。最快的方法是從電源插座中拔出電源插頭。客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 使用您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內，可使用隨附的機架安裝耳安裝在機架式機箱中，也可以放置在桌面上。使用十字螺絲刀將機架安裝耳固定在裝置兩側：

- 將機架安裝耳固定到右前側。
- 將機架安裝耳固定到左前側。
- 如有需要，安裝理線支架。

![](/img/b33c6771cd429919.webp)

本裝置沒有防水汙染保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 網線。本裝置的安裝和配置應由合格人員完成。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<table><thead><tr><th>**產品程式碼**</th><th>CRS354-48G-4S+2Q+RM</th></tr></thead><tbody><tr><td>**CPU**</td><td>QCA9531，650 MHz</td></tr><tr><td>**CPU 架構**</td><td>MIPSBE</td></tr><tr><td>**CPU 核心數**</td><td>1</td></tr><tr><td>**交換晶片型號**</td><td>98DX3257</td></tr><tr><td>**RAM**</td><td>128 MB</td></tr><tr><td>**儲存**</td><td>32 MB Flash</td></tr><tr><td>**1G 乙太網 (RJ45)**</td><td>48</td></tr><tr><td>**10G SFP+ 埠**</td><td>4</td></tr><tr><td>**40G QSFP+ 埠**</td><td>2</td></tr><tr><td>**序列控制檯 (RJ45)**</td><td>1</td></tr><tr><td>**作業系統**</td><td>RouterOS v7（許可證級別 5）/ SwitchOS（雙啟動）</td></tr><tr><td>**工作溫度**</td><td>-20 °C 至 +60 °C</td></tr><tr><td>**機箱尺寸**</td><td>297 × 443 × 44 mm</td></tr></tbody></table>

有關 MikroTik SFP 模組相容性和配置表，請訪問幫助頁面：MikroTik 有線介面相容性

## 供電 {#powering}

本裝置可透過兩路 100 – 240 V AC ⏦ 輸入供電。本裝置在最大負載下的功耗最高為 50 W。含附件時為 60 W。

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件可在以下地址獲取：[https://mt.lv/help](https://mt.lv/help) 您可以使用網頁瀏覽器中的 WebFig 或 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方式以確保可訪問性。** **要開始設定，請在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。該裝置配備一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。出於恢復目的，可以從網路重新安裝裝置，請參閱 Reset 按鈕。

Marvell Prestera 交換晶片功能使用者手冊

該裝置支援啟動 RouterOS（用於完整的路由和交換功能）或 SwOS（僅用於交換操作）。預設情況下，裝置啟動進入 RouterOS，但您可以按如下方式切換到另一個作業系統：

- 從 SwOS：轉到 System 選單，點選頁面底部的 Boot RouterOS 按鈕。
- 從 RouterOS：開啟 System → RouterBOARD → Settings 並選擇 Boot OS。也可以使用序列控制檯選單選擇作業系統並配置其他啟動選項。

## Reset 按鈕 {#reset-button}

- 在啟動期間按住此按鈕，直到 USR LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 按住 Reset 按鈕並給裝置上電（等待 "USR" LED 閃爍後穩定為 "On"，當 "USR" LED 變為 "Off" 時鬆開 Reset 按鈕）——裝置將以 bootp 模式啟動，以使用 Netinstall 重新安裝 RouterOS。**MGMT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。無論使用上述哪種方式，如果在裝置上電之前按下該按鈕，系統都將載入備份 RouterBOOT 載入程式。在 LED 開始閃爍之前鬆開按鈕，即可僅載入備份 RouterBOOT 而不進行重設。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

產品包裝內含以下隨裝置提供的配件：

![](/img/30cbe5f56587a6cf.webp)

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及更高版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。
