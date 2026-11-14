---
title: "CRS326-4C+20G+2Q+RM"
slug: /crs326-4c-plus-20g-plus-2q-plus-rm
source: https://manual.mikrotik.com/hardware/crs326-4c-plus-20g-plus-2q-plus-rm
captured_at: '2026-11-04T09:46:35+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/5bbe728d7bb856ed.jpg)

CRS326-4C+20G+2Q+RM 是一款網路交換器，具有二十個 2.5G 乙太網埠、四個 2.5/10G SFP+ 埠以及一個 100M 埠和兩個 40G QSFP+ 埠。該裝置可直接作為交換器使用。完整規格和宣傳冊請參見 [CRS326-4C+20G+2Q+RM 產品頁面](https://mikrotik.com/product/crs326_4c_20g_2q_rm)。

## 安全警告 {#safety-warnings}

在操作任何 MikroTik 裝置之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。請僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。本裝置須由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責確保裝置的安裝符合當地和國家電氣規範。請勿嘗試拆卸、修理或改裝該裝置。本裝置適合安裝在機架中。開始安裝前，請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟，可能會給人員帶來危險並損壞系統。本產品適合在室內安裝。請將本產品遠離水、火、潮溼或高溫環境。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！插座應安裝在裝置附近且便於觸及的位置。若裝置發生故障，請斷開其電源。最快的做法是將電源介面卡從電源插座中拔出。為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如置於指定區域。請熟悉將裝置妥善運送至您所在地區指定收集點的相關流程。

![](/img/ee40bff277b50ded.webp)

觸電危險。本裝置僅可由經過培訓的人員進行維修

## 快速開始 {#quickstart}

- 將您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可以確保最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

該裝置專為室內使用而設計，可使用隨附的機架安裝件安裝在機架機箱中，也可以放置在桌面上。如果希望放置在平坦表面上，請在路由器底部貼上橡膠墊腳；如果指定用途是機架機箱，請使用十字螺絲刀將機架掛耳安裝到裝置兩側：

- 如圖所示，將機架掛耳安裝到裝置兩側，並擰緊四顆螺絲將其固定到位。
- 將裝置放入機架機箱，並對齊孔位，使裝置能夠順利安裝。
- 擰緊螺絲將其固定到位。

![](/img/837a6d2bb5f312fe.webp)

本裝置的 IP 防護等級為 IP20。該裝置沒有防水保護，請確保將裝置放置在乾燥通風的環境中。本裝置的安裝和配置應由合格人員完成。

## 供電 {#powering}

該裝置可由兩個 100 – 240 V AC ⏦ 輸入供電。無外接附件時功耗為 51 W。接有附件時最高可達 70 W。

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件請見：[https://mt.lv/help](https://mt.lv/help) 您可以在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 配置裝置。**提供多種配置方式以確保可訪問性。** **要開始設定，請在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1)。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）。該裝置配備一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。為便於恢復，可以從網路重新安裝裝置，請參見復位按鈕。****

Marvell Prestera 交換晶片功能使用者手冊

該裝置支援啟動 RouterOS（用於完整的路由和交換功能）或 SwOS（僅用於交換操作）。預設情況下，裝置啟動進入 RouterOS，但您可以按以下方式切換到另一個作業系統：

- 從 SwOS 中：進入 System 選單，點選頁面底部的 Boot RouterOS 按鈕。
- 從 RouterOS 中：開啟 System → RouterBOARD → Settings 並選擇 Boot OS。也可以透過序列埠控制檯選單選擇作業系統並配置其他啟動選項。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<table><thead><tr><th>**產品程式碼**</th><th>CRS326‑4C+20G+2Q+RM</th></tr></thead><tbody><tr><td>**CPU**</td><td>QCA9531, 650 MHz</td></tr><tr><td>**CPU 架構**</td><td>MIPSBE</td></tr><tr><td>**CPU 核心數**</td><td>1</td></tr><tr><td>**交換晶片型號**</td><td>98DX8332</td></tr><tr><td>**RAM**</td><td>128 MB</td></tr><tr><td>**儲存**</td><td>32 MB Flash</td></tr><tr><td>**100 Mbps 乙太網 (RJ45)**</td><td>1</td></tr><tr><td>**2.5G 乙太網 (RJ45)**</td><td>20</td></tr><tr><td>**組合 10G (2.5G ETH / SFP+) 埠**</td><td>4</td></tr><tr><td>**40G QSFP+ 埠**</td><td>2</td></tr><tr><td>**序列埠控制檯 (RJ45)**</td><td>1</td></tr><tr><td>**作業系統**</td><td>RouterOS v7 (License 6)</td></tr><tr><td>**工作溫度**</td><td>‑20 °C 至 +60 °C</td></tr><tr><td>**外殼尺寸**</td><td>443 × 258 × 44 mm</td></tr></tbody></table>

請訪問幫助頁面檢視 MikroTik SFP 模組相容性表：MikroTik 有線介面相容性

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，即可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，以清除所有配置並恢復預設值。
- 按住復位按鈕並給裝置上電（等待 "USR" 指示燈閃爍後變為穩定的 "On"，當 "USR" 指示燈變為 "Off" 時鬆開復位按鈕）——裝置將以 bootp 模式啟動，從而使用 Netinstall 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。這適用於 RouterBOOT 偵錯和恢復。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的配件：

![](/img/a00204c74fd80c9c.webp)

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。
