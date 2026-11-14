---
title: "CRS520-4XS-16XQ-RM"
slug: /crs520-4xs-16xq-rm
source: https://manual.mikrotik.com/hardware/crs520-4xs-16xq-rm
captured_at: '2026-11-04T09:47:02+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/3c0b35575e792c18.jpg)

這是一款超高速企業級交換器，藉助 CCR 系列 CPU 提供額外的處理能力，並擁有市場上每 100 Gigabit 埠的最佳價格！完整規格與產品手冊請參見 [CRS520-4XS-16XQ-RM 產品頁面](https://mikrotik.com/product/crs520_4xs_16xq_rm)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵守所有國家法律法規。裝置的安裝必須符合當地和國家的電氣規範。本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用不正確的硬體或不遵循正確的操作流程可能導致人員危險和系統損壞。本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。僅使用製造商認可且可在本產品原包裝中找到的電源和配件。插座應安裝在裝置附近並便於插拔。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。客戶有責任遵守當地國家法規。所有 MikroTik 裝置必須由專業人員安裝。本產品為 Class A 產品。在住宅環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施

## 快速開始 {#quickstart}

- 使用您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁查詢裝置。然後透過 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，某些型號請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內使用，可使用隨附的機架安裝耳件安裝在機架機箱中，也可以放置在桌面上。如果希望放置在平坦表面上，請在路由器底部貼上橡膠腳墊；如果指定用於機架機箱，請使用十字螺絲刀在裝置兩側安裝機架耳件：

- 將機架耳件和後部支撐耳件安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如圖所示。

![](/img/837a6d2bb5f312fe.webp)

- 將裝置放入機架機箱並對齊孔位，使裝置方便就位。
- 擰緊螺絲將其固定到位。本裝置不具備防水汙染保護，請確保將裝置放置在乾燥通風的環境中。我們建議為我們的裝置使用 Cat6 網線。本裝置的安裝和配置應由具備資質的人員完成。

## 供電 {#powering}

本裝置配備兩個熱插拔 IEC 型 AC 電源，150W，支援 100-240 V ⏦（~ 50/60 Hz，最大 12.5 A）。不帶附件時的最大功耗為 123 W，在最大負載下可達 150W。

## 配置 {#configuration}

RouterOS 和 SwOS 的完整文件可在以下地址獲取：[https://mt.lv/help](https://mt.lv/help) 您可以在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方式以確保可訪問性。** **要開始設定，請在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁查詢裝置。然後透過 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，某些型號請檢視貼紙上的使用者和無線密碼）。本裝置配備 RS-232 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。出於恢復目的，可以從網路重新安裝裝置，請參見 Reset 按鈕。

Marvell Prestera 交換晶片功能使用者手冊

本裝置支援啟動 RouterOS（以獲得完整的路由和交換功能）或 SwOS（僅用於交換操作）。預設情況下，裝置啟動進入 RouterOS，但您可以按如下方式切換到其他作業系統：

- 從 SwOS：進入 System 選單，點選頁面底部的 Boot RouterOS 按鈕。
- 從 RouterOS：開啟 System → RouterBOARD → Settings 並選擇 Boot OS。也可以透過序列埠控制檯選單選擇作業系統並配置其他啟動選項。

## 散熱 {#cooling}

本裝置配備四個 MT-HotSwapFan 單元。

## 按鈕 {#buttons}

**Reset 按鈕**：

- 在啟動過程中按住此按鈕，直到 USR LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 按住 Reset 按鈕並給裝置上電（等待 "USR" LED 閃爍後變為穩定 "On"，當 "USR" LED 變為 "Off" 時——鬆開 Reset 按鈕）——裝置將以 bootp 模式啟動，以便使用 Netinstall 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復工具的說明，請參見 RouterOS 文件。無論使用上述哪種方式，如果在裝置上電前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。請在 LED 開始閃爍之前鬆開按鈕，以便僅載入備份 RouterBOOT 而不進行重設。這對於 RouterBOOT 偵錯和恢復很有用。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 十六個 100G QSFP28 埠。
- 四個 25G SFP28 埠。
- 兩個用於管理訪問的 1G/10G 乙太網埠。
- 1x RJ45 控制檯埠（設定為 115200bits/s、8 個數據位、1 個停止位、無校驗）。有關 MikroTik SFP 模組相容性和配置表的說明，請訪問幫助頁面：MikroTik 有線介面相容性

## LED 指示燈 {#led-indicators}

- PWR1、PWR2 LED 在使用中的 PSU 為路由器供電時點亮。
- USER LED 指示裝置在啟動進入不同模式（例如重設配置或為 Netinstall 工具啟動裝置）時的狀態。
- FAULT LED 指示任一散熱風扇出現問題。

## 配件 {#accessories}

包裝中隨附以下配件：

![](/img/e3bdbf6673924349.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。
