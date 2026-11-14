---
title: "CRS804-4DDQ-hRM"
slug: /crs804-4ddq-hrm
source: https://manual.mikrotik.com/hardware/crs804-4ddq-hrm
captured_at: '2026-11-04T09:47:26+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![CRS804 DDQ](/img/061c0cdafc4d6be6.jpg)

這是一款緊湊的 1U 400G 交換器，專為 AI 叢集、儲存網路和高速匯聚而打造，配備四個 400G QSFP56-DD 埠、雙 10 Gigabit Ethernet 埠以及 RouterOS v7。完整規格和手冊請參見 [CRS804-4DDQ-hRM 產品頁面](https://mikrotik.com/product/crs804_ddq)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應按照所有國家和地區的法律法規執行。裝置的安裝必須符合當地和國家的電氣規範。本裝置設計用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟可能對人員造成危險並損壞系統。本產品設計用於室內安裝。請使本產品遠離水、火、潮溼或高溫環境。僅使用製造商認可的電源和配件，這些可在本產品的原始包裝中找到。電源插座應安裝在裝置附近且易於插拔。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置出現故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。客戶有責任遵守當地國家的法規。所有 MikroTik 裝置必須由專業人員安裝。本產品為 A 類產品。在家庭環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施

## 快速開始 {#quickstart}

- 將您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。接著使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼：**CRS804-4DDQ-hRM**。
- CPU：四核 AL52400 2000 MHz。
- CPU：架構 ARM 64bit。
- RAM 容量：4 GB。
- RAM 型別：DDR4。
- 儲存：512 MB，NAND。
- 10M/100M/1G/10G 乙太網埠數量：2 個。標記為 **MGMT/BOOT**。可以在 System → RouterBOARD → Settings → Etherboot Port 中將 **Ether1** 或 **Ether2** 設定為 **Etherboot port**。
- 400G QSFP56-DD 埠數量：4 個。
- PoE-out 埠：Ether9-Ether16，802.3af/at，總輸出功率 150 W。
- 1x RJ45 控制檯埠（設定為 115200bits/s，8 資料位，1 停止位，無奇偶校驗）。
- 交換晶片型號：98DX7335。
- 尺寸：387 x 218 x 44 mm。
- 作業系統 RouterOS：v7，許可證級別 6。
- 工作溫度：-10°C 至 +60°C。
- IP：20 支援的 SFP 模組請參見 [MikroTik 有線介面相容性](/docs/wired-connections/mikrotik-wired-interface-compatibility)表。

## LED 指示燈 {#led-indicators}

- 當路由器由使用中的 PSU 供電時，PWR1、PWR2 LED 會點亮。
- USER LED 指示裝置在以上電方式進入不同模式時的狀態，例如重設配置或為 Netinstall 工具啟動裝置。
- FAULT LED 指示任何散熱風扇出現問題。

## 安裝 {#mounting}

本裝置設計用於室內使用，可使用隨附的機架安裝配件安裝在 1U 機架式機箱中，或放置在平坦表面上。對於桌面安裝，請將隨附的橡膠腳墊安裝到裝置底部。對於機架安裝，請按下文所述，使用十字螺絲刀將機架安裝耳片安裝到裝置上。

### 在 1U 機架式機箱中安裝單臺裝置 {#single-device-installation-in-a-1u-rackmount-enclosure}

![](/img/b3a5c211837424ae.webp)

- 將前部機架安裝支架安裝到裝置的一側。
- 將長機架安裝支架安裝到相對的一側。
- 將後部支撐耳片安裝到裝置上。
- 如圖所示，使用四顆螺絲固定所有支架。
- 將裝置放入機架式機箱，並對齊安裝孔。
- 擰緊機架螺絲，將裝置固定到位。

![](/img/792dc366979acbe7.webp)

#### 使用 RMK-2x10/19 安裝兩臺 CRS804-4DDQ-hRM 裝置 {#installing-two-crs804-4ddq-hrm-devices-using-rmk-2x1019}

使用 RMK-2x10/19 套件（包裝內含），可以在單個 1U 機架單元內並排安裝兩臺 CRS804-4DDQ-hRM 裝置。

![](/img/dd4da1d5c0ab0cc9.webp)

- 將前部機架安裝支架和後部支撐耳片安裝到每臺裝置的同一（相對）側。
- 如圖所示，使用四顆螺絲固定每個支架。
- 將 RMK-2x10/19 安裝部件安裝到兩臺裝置的其餘兩側。
- 如圖所示，使用四顆螺絲固定 RMK-2x10/19 部件。
- 按照安裝指南將兩臺裝置對齊並卡合在一起。
- 將組裝好的單元放入機架式機箱，並對齊安裝孔。
- 擰緊機架螺絲，將元件固定到位。

![](/img/ed96d20dcf59d102.webp)

本裝置不具備防水保護；請將其安裝在乾燥、通風良好的位置。我們建議在我們的裝置上使用 Cat 6 網線。本裝置的安裝和配置應由專業人員完成。

## 供電 {#powering}

本裝置配備兩個支援熱插拔的 IEC 型別 AC 電源 G1394-0350WNA。AC 輸入 100-240 V ⏦（~ 50/60 Hz 8 A 最大）。DC 輸入 240V，27,5A MAX +5VSB，4A。不含附加元件時的最大功耗為 92 W，在最大負載下可達 123W。

## 配置 {#configuration}

RouterOS 的完整文件可在以下地址獲取：[https://mt.lv/help](https://mt.lv/help) 您可以使用網頁瀏覽器中的 WebFig 或 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方式以確保可訪問性。** **要開始設定，請在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。接著使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。裝置配備 RJ45 序列埠，預設設定為 115200 bit/s、8 資料位、1 停止位、無奇偶校驗。出於恢復目的，可以從網路重新安裝裝置，請參見 Reset 按鈕。

Marvell Prestera 交換晶片功能使用者手冊

## 散熱 {#cooling}

本裝置配備兩個 New MT-HotSwapFan-V2 單元。

## 按鈕 {#buttons}

**Reset 按鈕**：

- 在啟動期間按住此按鈕，直到 USR LED 開始閃爍，再鬆開按鈕即可重設 RouterOS 配置。
- 按住 Reset 按鈕並給裝置上電（等待 "USR" LED 閃爍後變為穩定的 "On"，當 "USR" LED 變為 "Off" 時鬆開 Reset 按鈕）——裝置將以 bootp 模式啟動，使用 Netinstall 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠（Ether1 或 Ether2）用於 Netinstall 過程。** 關於使用 Netinstall 恢復工具的說明，請參見 RouterOS 文件。無論使用上述哪種方式，如果在裝置上電之前按鈕已被按下，系統都會載入備份的 RouterBOOT 載入程式。在 LED 開始閃爍之前鬆開按鈕，則僅載入備份 RouterBOOT 而不進行重設。這對於 RouterBOOT 偵錯和恢復非常有用。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的配件：

![](/img/c863b0f847cac7c0.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列在 /system resource 中。其他作業系統尚未經過測試。
