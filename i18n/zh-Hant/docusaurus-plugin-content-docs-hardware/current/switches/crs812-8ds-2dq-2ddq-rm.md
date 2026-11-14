---
title: "CRS812-8DS-2DQ-2DDQ-RM"
slug: /crs812-8ds-2dq-2ddq-rm
source: https://manual.mikrotik.com/hardware/crs812-8ds-2dq-2ddq-rm
captured_at: '2026-11-04T09:47:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/0336e04dd1dd22e2.jpg)

這款交換器是您的下一次飛躍——一種強大、高效且經濟的方式，可將 50G、200G 和 400G 引入您的機架。四核 2 GHz ARM CPU、雙冗餘電源和 4 個熱插拔散熱風扇、2 個 10G 乙太網口、8 個 50G SFP56、2 個 200G QSFP56 和 2 個 400G QSFP56-DD 埠。完整規格和宣傳冊請參見 [CRS812 DDQ 產品頁面](https://mikrotik.com/product/crs812_ddq)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵守所有國家法律法規。裝置的安裝必須符合當地和國家的電氣規範。本裝置旨在安裝於機架中。請在開始安裝前仔細閱讀安裝說明。使用錯誤的硬體或未遵循正確的操作流程可能導致人員危險和系統損壞。本產品僅供室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。插座應安裝在裝置附近且便於插拔。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。客戶有責任遵守當地國家的法規。所有 MikroTik 裝置必須由專業人員安裝。本產品為 A 類產品。在家庭環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施

## 快速開始 {#quickstart}

- 將您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig 或 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法以確保可訪問性；**
- 在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。使用 MAC 地址繼續連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置專為室內使用而設計，可使用隨附的機架安裝支架安裝在機櫃中，也可以直接放置在桌面上。如果希望放置在平坦表面上，請在路由器底部安裝橡膠腳墊；如果指定用途為機櫃安裝，請使用十字螺絲刀將機架安裝耳片安裝到裝置兩側：

- 將機架安裝耳片安裝到裝置的前側。

![](/img/2008a038f299bd3d.webp)

![](/img/665133e76c421621.webp)

![](/img/a48997ad98824cd2.webp)

![](/img/777e94adf9e9ec0f.webp)

- 將小型後部機架安裝支撐耳片安裝到裝置兩側。

![](/img/ca7257427d7f1f08.webp)

![](/img/0433ddb68eb49ec3.webp)

- 將長型後部機架安裝支撐耳片安裝到機架的後側。

![](/img/3a9329eb2e283df6.webp)

- 將裝置安裝到機架中，確保機箱支撐耳片牢固地固定在長型支撐耳片上。

本裝置沒有防水保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 網線。本裝置的安裝和配置應由合格人員完成。

## 供電 {#powering}

本裝置配備兩個熱插拔 IEC 型 AC 電源，功率 250 W，支援 100-240 V ⏦（約 50/60 Hz，最大 7 A）。未接附件時的最大功耗為 81 W，在最大負載下可達 134 W。

## 配置 {#configuration}

RouterOS 的完整文件可在以下地址獲取：[https://mt.lv/help](https://mt.lv/help) 您可以使用網頁瀏覽器中的 WebFig 或 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方法以確保可訪問性。** **要開始設定，請在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。使用 MAC 地址繼續連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。本裝置配備 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。出於恢復目的，可以從網路重新安裝裝置，請參見 Reset 按鈕。

Marvell Prestera 交換晶片功能使用者手冊

## 按鈕 {#buttons}

**Reset 按鈕**：

- 在啟動期間按住此按鈕，直到 USER LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 按住 Reset 按鈕並給裝置上電（等待 "USER" LED 閃爍後變為穩定 "On"，當 "USER" LED 變為 "Off" 時鬆開 Reset 按鈕）——裝置將以 BOOTP 模式啟動，使用 Netinstall 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復實用程式的資訊，請參見 RouterOS 文件。無論使用上述哪種方式，如果在裝置上電前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。請在 LED 開始閃爍前鬆開按鈕，以便僅載入備份 RouterBOOT 而不進行重設。這對於 RouterBOOT 偵錯和恢復非常有用。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼：**CRS812-8DS-2DQ-2DDQ-RM**。
- CPU：四核 AL52400 2000 MHz。
- CPU 架構：ARM 64bit。
- RAM 容量：4 GB。
- RAM 型別：DDR4。
- 儲存：512 MB，NAND。
- 1G/2.5G/5G/10G 乙太網埠數量：2（支援：10M/100M/1G/10G）。
- 50G SFP56 埠數量：8。
- 200G QSFP56 埠數量：2。
- 400G QSFP56-DD 埠數量：2。
- 1 個 RJ45 控制檯埠（設定為 115200bits/s、8 個數據位、1 個停止位、無奇偶校驗）。
- 交換晶片型號：98DX7335。
- 尺寸：443 x 156 x 44 mm。
- 作業系統 RouterOS：v7，許可證等級 6。
- 熱插拔散熱風扇：四個。
- 工作溫度：-10°C 至 +50°C。
- IP：20。支援的 SFP 模組請參見 [MikroTik 有線介面相容性](/docs/wired-connections/mikrotik-wired-interface-compatibility) 表。

## LED 指示燈 {#led-indicators}

- 當路由器使用合適的電源開啟時，POWER1 和 POWER2 LED 會亮起。
- USER LED 指示裝置在啟動進入不同模式時的狀態，例如重設配置或為 Netinstall 實用程式啟動裝置。
- FAULT LED 指示任何散熱風扇出現問題。
- 50G SFP56 籠外側 LED 箭頭指示鏈路活動，內側指示 50G 鏈路速度。
- 200G QSFP56 埠 LED 指示每個介面四個通道的活動。
- 400G QSFP56-DD 埠 LED 指示每個介面前四個通道的活動。

## 配件 {#accessories}

包裝內含以下隨裝置提供的附件：

![](/img/aaebbf84c9e794ac.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。
