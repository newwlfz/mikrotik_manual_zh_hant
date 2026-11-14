---
title: "CRS418-8P-8G-2S+5axQ2axQ-RM"
slug: /crs418-8p-8g-2s-plus-5axq2axq-rm
source: https://manual.mikrotik.com/hardware/crs418-8p-8g-2s-plus-5axq2axq-rm
captured_at: '2026-11-04T09:46:51+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/965ab29068a47f6e.jpg)

CRS418 的 Wi-Fi 版本……搭載我們最強的 4x4 MIMO Wi-Fi 6！L3 硬體解除安裝、四核 2.2 GHz ARM CPU、16 個千兆乙太網埠 + 1 個帶直連 CPU 線路的千兆管理埠、2 個 10G SFP+ 埠、PoE-out。有關完整規格和宣傳冊，請參見 [CRS418-8P-8G-2S+5axQ2axQ-RM 產品頁面](https://mikrotik.com/product/crs418_8p_8g_2s_wifi)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應按照所有國家法律和法規進行處理。裝置的安裝必須符合當地和國家的電氣規範。本裝置擬安裝在機架中。開始安裝前，請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的程式，可能會對人員造成危險並損壞系統。本產品擬在室內安裝。請使本產品遠離水、火、潮溼或高溫環境。僅使用製造商批准且可在本產品原包裝中找到的電源和配件。插座應安裝在裝置附近，並且應易於觸及。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置發生故障，請斷開其電源。最快的方法是從電源插座上拔下電源插頭。客戶有責任遵守當地國家/地區的法規。所有 MikroTik 裝置必須由專業人員安裝。本產品為 A 類產品。在家庭環境中，本產品可能會造成無線電干擾，在這種情況下，使用者可能需要採取適當的措施。

## 快速開始 {#quickstart}

- 確保您的網際網路服務提供商（ISP）允許硬體更換並自動分配 IP 地址；
- 將 ISP 線纜連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 之外的任一埠，或無線網路 “MikroTik-...” 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在 Web 瀏覽器中使用 WebFig，或使用位於 [https://mt.lv/winbox](https://mt.lv/winbox) 的 “WinBox” 配置工具。**提供多種配置方法以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 “Neighbors” 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 “admin”，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 “Check for updates” 按鈕，並將 RouterOS 更新到最新版本；
- 要手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 “Downloads” 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 “Files” 選單，並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 “QuickSet” 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內，可使用隨附的機架安裝支架安裝在機架機箱中，或放置在桌面上。

如果將裝置安裝在機架中，請確保天線有足夠空間，並且可以不受阻礙地自由擺放。對於桌面放置，請將橡膠腳墊安裝到路由器底部。

進行機架安裝時，請使用十字螺絲刀將機架安裝耳安裝到裝置兩側：

- 如圖所示，將機架安裝耳和後部支撐耳安裝到裝置兩側，並擰緊四顆螺絲將其固定。

![](/img/837a6d2bb5f312fe.webp)

- 將裝置放入機架式機箱，並對齊安裝孔。
- 擰緊螺絲將裝置固定到位。本裝置沒有防水汙染保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 線纜。本裝置的安裝和配置應由合格人員完成。

## 供電 {#powering}

本裝置配備兩個 250 W 電源，支援 100-240 V ⏦（~ 50/60 Hz，最大 4.5 A）。未連線附件時最大功耗為 43 W，最大負載下可達 227 W。

## 配置 {#configuration}

RouterOS 的完整文件可在以下地址獲取：[https://mt.lv/help](https://mt.lv/help) 您可以使用 Web 瀏覽器中的 WebFig 或 “WinBox” 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方法以確保可訪問性。** **要開始設定，請在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果 IP 地址不可用，請使用 WinBox 並選擇 “Neighbors” 標籤頁來查詢裝置。繼續使用 MAC 地址進行連線。使用者名稱為 “admin”，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。本裝置配備一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。為恢復目的，可以從網路重新安裝裝置，請參見 Reset 按鈕。**

Marvell Prestera 交換晶片功能使用者手冊

## 按鈕 {#buttons}

**Reset 按鈕**：

- 在啟動期間按住此按鈕，直到 USER LED 燈開始閃爍，鬆開按鈕以重設 RouterOS 配置。
- 按住 Reset 按鈕並給裝置通電（等待 “USER” LED 閃爍，然後穩定為 “On”，當 “USER” LED 為 “Off” 時——鬆開 Reset 按鈕）——裝置將以 BOOTP 模式啟動，以使用 Netinstall 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠用於 Netinstall 過程。** 請參閱 RouterOS 文件中關於使用 Netinstall 恢復實用程式的內容。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備用 RouterBOOT 載入程式。在 LED 開始閃爍前鬆開按鈕，以僅載入備用 RouterBOOT 而不進行重設。這對於 RouterBOOT 偵錯和恢復很有用。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼：**CRS418-8P-8G-2S+RM**。
- RAM 大小：1 GB。
- RAM 型別：DDR3。
- 儲存：128 MB，NAND。
- 1G 乙太網埠數量：17。
- 10G SFP+ 乙太網埠數量：2。
- 帶 PoE-out 的 1G 乙太網埠數量：8。
- PoE-out 埠：Ether9-Ether16，802.3af/at，總輸出功率 150 W。
- 1x RJ45 控制檯埠（設定為 115200bits/s、8 個數據位、1 個停止位、無奇偶校驗）。
- USB：1 個 USB 3.0 type A。
- 交換晶片型號：98DX226S。
- 無線介面型號：QCN-5024（2.4 GHz）、QCN-5054（5 GHz）、Wi-Fi 6。
- 無線：2.4 GHz 802.11b/g/n/ax 四鏈，5 GHz 802.11a/n/ac/ax 四鏈。
- MIMO DL：4x4。
- MIMO UL：1x1（5G SA MIMO UL 2x2）。
- 尺寸：443 x 156 x 44 mm。
- 作業系統 RouterOS：v7，許可證級別 5。
- 工作溫度：-20°C 至 +70°C。請訪問幫助頁面以瞭解 MikroTik SFP 模組相容性和配置表：MikroTik 有線介面相容性

## LED 指示燈 {#led-indicators}

- 路由器通電時 PWR LED 點亮。
- USER LED 指示裝置在啟動進入不同模式時的狀態，例如重設配置或啟動裝置以使用 Netinstall 實用程式。
- FAULT LED 表示任一冷卻風扇出現問題。
- 三角形 LED（頂行）指示 PoE 輸出狀態。綠色 LED 表示相應埠使用低電壓，紅色 LED 表示高電壓。單個綠色 LED 閃爍：啟動低電壓裝置時出現問題。單個紅色 LED 閃爍：高電壓裝置出現問題。
- SFP+ 埠的綠色 LED 指示各個 SFP+ 埠活動。

## 配件 {#accessories}

包裝內含以下隨裝置提供的配件：

![](/img/9f561f728fa8bbfa.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。
