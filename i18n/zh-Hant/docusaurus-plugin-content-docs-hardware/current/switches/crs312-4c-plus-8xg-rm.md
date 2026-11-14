---
title: "CRS312-4C+8XG-RM"
slug: /crs312-4c-plus-8xg-rm
source: https://manual.mikrotik.com/hardware/crs312-4c-plus-8xg-rm
captured_at: '2026-11-04T09:46:13+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/10bf7e61d4f4f7e5.jpg)

## [CRS312-4C+8XG-RM](https://mikrotik.com/product/crs312_4c_8xg_rm) {#crs312-4c8xg-rm}

CRS312-4C+8XG 是一款 8 埠千兆乙太網交換器，帶有四個 10g Ethernet / SFP+ 組合埠。它具備受管交換器所需的全部基本功能以及更多特性。有關完整規格和手冊，請參閱 [CRS312-4C+8XG-RM 產品頁面](https://mikrotik.com/product/crs312_4c_8xg_rm)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家和地區的法律法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品僅適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些均可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請先閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置出現故障，請斷開其電源。最快的做法是將電源插頭從電源插座上拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 裝置都必須由專業人員進行安裝。

## 快速開始 {#quickstart}

- 用您的 PC 連線到任意 Ethernet 埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後透過 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（某些型號請檢視標籤上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內，可使用隨附的機架配件安裝在機架機箱中，也可以放置在桌面上。如果希望放置在平面上，請在路由器底部貼上橡膠腳墊；如果指定用於機架機箱，請使用十字螺絲刀將機架耳片安裝到裝置兩側：

- 如圖所示，將機架耳片安裝到裝置兩側，並擰緊四顆螺絲將其固定到位。
- 將裝置放入機架機箱，對準孔位，使裝置順利裝入。
- 擰緊螺絲將其固定到位。

![](/img/27bf22aa32ecbced.webp)

本裝置的 IP 防護等級為 IPX0。裝置不具備防水汙染保護，請確保將裝置放置在乾燥通風的環境中。我們建議為我們的裝置使用遮蔽 Cat5/6 網線。*本裝置的安裝和配置應由具備資質的人員完成。*

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件可在 [https://mt.lv/help](https://mt.lv/help) 獲取。裝置可透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方式以確保可訪問性。**

在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後透過 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（某些型號請檢視標籤上的使用者和無線密碼）。

裝置配備一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。為便於恢復，可以從網路重新安裝裝置，請參閱 Reset 按鈕。

Marvell Prestera 交換晶片的特性在 [Marvell Prestera 交換晶片特性](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) 手冊中進行了說明。

裝置支援啟動 RouterOS（獲得完整的路由和交換功能）或 SwOS（僅進行交換操作）。預設情況下，裝置啟動進入 RouterOS，但您可以按以下方式切換到另一個作業系統：

- 從 SwOS：轉到 **System** 選單，點選頁面底部的 "**Boot RouterOS**" 按鈕。
- 從 RouterOS：開啟 **System → RouterBOARD → Settings** 並選擇 **Boot OS**。

也可以使用序列埠控制檯選單選擇作業系統並配置其他啟動選項。

## 供電 {#powering}

裝置可透過兩個交流輸入供電，電壓範圍為 AC ⏦ 100-240 V。兩路電源為 IEC 電源介面，可實現冗餘。最大負載下的功耗可達 60 W。

## 規格 {#specifications}

<table><thead><tr><th>**產品程式碼**</th><th>CRS312‑4C+8XG‑RM</th></tr></thead><tbody><tr><td>**CPU**</td><td>QCA9531, 650 MHz</td></tr><tr><td>**CPU 架構**</td><td>MIPSBE</td></tr><tr><td>**CPU 核心數**</td><td>1</td></tr><tr><td>**交換晶片型號**</td><td>98DX8212</td></tr><tr><td>**RAM**</td><td>64 MB</td></tr><tr><td>**儲存**</td><td>16 MB Flash</td></tr><tr><td>**10/100 Ethernet (RJ45)**</td><td>1</td></tr><tr><td>**1G/2.5G/5G/10G Ethernet (RJ45)**</td><td>8</td></tr><tr><td>**10G Combo (RJ45/SFP+) 埠**</td><td>4</td></tr><tr><td>**USB Type‑A 埠**</td><td>1</td></tr><tr><td>**序列埠控制檯 (RJ45)**</td><td>1</td></tr><tr><td>**作業系統**</td><td>RouterOS v7 / SwOS (License 5)</td></tr><tr><td>**工作溫度**</td><td>‑30 °C 至 +70 °C</td></tr><tr><td>**外殼尺寸**</td><td>443 × 183 × 44 mm</td></tr></tbody></table>

## Combo 介面 {#combo-interface}

四個 combo 介面各自有兩個物理聯結器，同一時間只能使用其中一個。在 RouterOS 中，這些埠會自動錶示為 combo 1-4。可以在 RouterOS 軟體的 ethernet 選單中選擇使用哪個物理埠。如果保持預設的 "auto"，並且 F/T 兩端都插入了線纜，則 SFP 優先。例如，如果您將網線插入 1T 埠並在 1F 埠插入 SFP 模組，則必須在 RouterOS 中選擇要使用哪一個。在 RouterOS GUI 中雙擊相應的 combo 介面即可檢視使用的是哪個插口。

## Reset 按鈕 {#reset-button}

- 要重設配置，請斷開裝置電源，按住 Reset 按鈕，然後在 USER (USR) LED 開始閃爍時鬆開。
- 要載入備份載入程式，請在通電前按住 Reset 按鈕，三秒後鬆開。
- 要啟動 Netinstall 過程（讓裝置以 BOOTP 模式啟動以重新安裝 RouterOS），請按住 Reset 按鈕，給裝置通電，等待 USER (USR) LED 閃爍後變為常亮。當 USR LED 熄滅時，鬆開 Reset 按鈕。

無論使用上述哪種方式，如果在裝置通電前就已按下該按鈕，系統都會載入備份 RouterBOOT 載入程式。這適用於 RouterBOOT 偵錯和恢復。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下配件：

- 用於機架機箱的固定套件 K-57。
- AC ⏦ EU/US 電源線，D03+QT3 H05VV-F 3x0.75 mm2 1.83 m RoHS。
- 安裝套件 1U 機架支架（白色），2 個。請訪問 wiki 頁面檢視 MikroTik SFP 模組相容性表：MikroTik wired interface compatibility。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。
