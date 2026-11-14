---
title: "CCR2116-12G-4S+"
slug: /ccr2116-12g-4s-plus
source: https://manual.mikrotik.com/hardware/ccr2116-12g-4s-plus
captured_at: '2026-11-04T05:55:52+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/fd56a24a2221eb27.jpg" alt="" width={800} height={366} /></p>

## [CCR2116-12G-4S+](https://mikrotik.com/product/ccr2116_12g_4splus) {#ccr2116-12g-4s}

藉助這款基於 16 核 ARM CPU 的強大 CCR，在 10G 環境中無需再擔心 CPU 效能限制。效能是我們上一代 36 核 CCR 的兩倍，BGP 效能提升 6 倍。包含一個 M.2 PCIe 插槽。完整規格和宣傳冊請參閱 [CCR2116-12G-4S+ 產品頁面](https://mikrotik.com/product/ccr2116_12g_4splus)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律法規進行處理。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於機架安裝。開始安裝前請仔細閱讀安裝說明。使用不正確的硬體或不遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品設計用於室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家/地區法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

:::danger 開啟機箱前請先斷電

在開啟機箱或安裝/更換任何內部元件（例如 M.2 SSD）之前，請完全關閉系統並斷開 AC 電源的電源線。拔下電源後，請至少等待 10 秒，讓主機板中的殘餘電量完全釋放。

:::

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>值</th></tr></thead><tbody><tr><td>產品程式碼</td><td>CCR2116-12G-4S+</td></tr><tr><td>架構</td><td>ARM 64bit</td></tr><tr><td>CPU</td><td>AL73400</td></tr><tr><td>CPU 核心數</td><td>16</td></tr><tr><td>CPU 標稱頻率</td><td>2000 MHz</td></tr><tr><td>CPU 執行緒數</td><td>16</td></tr><tr><td>交換晶片型號</td><td>98DX3255</td></tr><tr><td>尺寸</td><td>443 x 199 x 44 mm</td></tr><tr><td>RouterOS 許可證</td><td>6</td></tr><tr><td>作業系統</td><td>RouterOS v7</td></tr><tr><td>RAM 容量</td><td>16 GB</td></tr><tr><td>儲存容量</td><td>128 MB</td></tr><tr><td>儲存型別</td><td>NAND</td></tr><tr><td>MTBF</td><td>25°C 下約 200'000 小時</td></tr><tr><td>測試環境溫度</td><td>-20°C 至 60°C</td></tr><tr><td>**供電**</td><td></td></tr><tr><td>AC 輸入數量</td><td>2</td></tr><tr><td>AC 輸入範圍</td><td>100-240</td></tr><tr><td>PSU 插槽數量</td><td>2</td></tr><tr><td>頻率 (Hz)</td><td>47-63</td></tr><tr><td>最大功耗</td><td>83 W</td></tr><tr><td>無附加元件時的最大功耗</td><td>60 W</td></tr><tr><td>散熱型別</td><td>4 個風扇</td></tr><tr><td>**乙太網**</td><td></td></tr><tr><td>10/100/1000 乙太網埠</td><td>13</td></tr><tr><td>**光纖**</td><td></td></tr><tr><td>SFP+ 埠</td><td>4</td></tr><tr><td>**外設**</td><td></td></tr><tr><td>序列埠控制檯埠</td><td>RJ45</td></tr><tr><td>M.2 插槽數量</td><td>1</td></tr><tr><td>**其他**</td><td></td></tr><tr><td>CPU 溫度監控</td><td>是</td></tr><tr><td>PCB 溫度監控</td><td>是</td></tr><tr><td>電壓監控</td><td>是</td></tr><tr><td>Mode 按鈕</td><td>是</td></tr><tr><td>**認證與批准**</td><td></td></tr><tr><td>認證</td><td>CE, EAC, ROHS</td></tr></tbody></table>

## 快速開始 {#quickstart}

- 將您的 PC 連線到標有 **ETH/BOOT** 的埠或第一個乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 應使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方法以確保可訪問性；**
- 在網頁瀏覽器中開啟 192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單並重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

該裝置可由兩個冗餘電源供電，每個電源均接受 100-240 V AC 電源。您可以單獨使用其中一個，或同時使用兩個。功耗最高 60 W。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 13x 10/100/1000 乙太網埠。
- 4x 10G SFP+ 埠。
- 一個 M.2 插槽，型別 PCIe x4。
- RJ45 控制檯埠。CCR2116-12G-4S+ 與 M.2 插槽之間為 PCIe Gen 3.0 x4 連線。推薦使用無容量限制的 NVMe M.2 2280mm M key SSD 硬碟。

## 安裝 {#mounting}

該裝置設計用於室內使用，可使用隨附的機架安裝件安裝在機架機箱中，也可以放置在桌面上。如果指定用於機架機箱，請使用十字螺絲刀將機架耳片安裝到裝置兩側：

<p><Img src="/img/27bf22aa32ecbced.webp" alt="" width={610} height={543} /></p>

- 如圖所示，將機架耳片安裝到裝置兩側，並擰緊四顆螺絲將其固定到位。
- 將裝置放入機架機箱中，對準孔位，使裝置安裝合適。
- 擰緊螺絲將其固定到位。*裝置無防水保護，請確保將裝置放置在乾燥且通風的環境中。* *我們建議為我們的裝置使用遮蔽 Cat5/6 線纜。* *本裝置的安裝和配置應由合格人員完成。*

## 配置 {#configuration}

RouterOS 的完整文件可在以下地址獲取：[https://mt.lv/help](https://mt.lv/help) 您可以使用網頁瀏覽器中的 **WebFig** 或 "**WinBox**" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 配置裝置。**提供多種配置方法以確保可訪問性。** 要開始設定，請在網頁瀏覽器中開啟 192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）。該裝置配有 RS-232 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。出於恢復目的，可以從網路重新安裝裝置，請參閱 Reset 按鈕。

## 按鈕和跳線 {#buttons-and-jumpers}

**Reset 按鈕**：

- 在啟動過程中按住此按鈕，直到 USER LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 按住 Reset 按鈕並給裝置上電（等待 "USER" LED 閃爍，然後穩定為 "On"，當 "USER" LED 變為 "Off" 時 - 鬆開 Reset 按鈕） - 裝置將以 BOOTP 模式啟動，以便使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 重新安裝 RouterOS。**Netinstall 過程使用 MGMT/BOOT 乙太網埠。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。

無論使用上述哪種方式，如果在裝置上電前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。在 LED 開始閃爍之前鬆開按鈕，即可僅載入備份 RouterBOOT 而不進行重設。這對 RouterBOOT 偵錯和恢復很有用。

Mode 按鈕預設不起作用，但可以在選單 /system routerboard mode-button 中為其分配任意指令碼

## LED 指示燈 {#leds}

該裝置有四個 LED 燈。PWR1/2 指示當前使用的是哪個電源。FAULT 指示散熱風扇出現問題。USER 可在軟體中配置。

## 配件 {#accessories}

- PLUG1, PLUG2_EU/US 電源線, D03+QT3 H05VV-F 3x0.75mm2 1.83m RoHS
- CASE3, CASE4_ 1U 機架安裝支架 白色
- SET1_Fastening set K-57r1v1

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。
