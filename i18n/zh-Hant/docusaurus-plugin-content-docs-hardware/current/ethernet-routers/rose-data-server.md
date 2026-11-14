---
title: "ROSE 資料伺服器"
slug: /rose-data-server
source: https://manual.mikrotik.com/hardware/rose-data-server
captured_at: '2026-11-04T06:05:18+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### RDS2216-2XG-4S+4XS-2XQ {#rds2216-2xg-4s4xs-2xq}

<p><Img src="/img/4a48a7823e0bdec2.jpg" alt="" width={799} height={559} /></p>

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。完整規格和產品手冊請參閱 [ROSE Data Server 產品頁面](https://mikrotik.com/product/rds2216)。本產品的最終處置應遵守所有國家和地區的法律法規。裝置的安裝必須符合當地和國家的電氣規範。本裝置設計為安裝在機架中。開始安裝前，請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的步驟，可能會對人員造成危險並損壞系統。在將系統連線到電源之前，請閱讀安裝說明。客戶有責任遵守當地國家的法規，包括在合法的頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 產品規格 {#product-specifications}

- 產品型號：RDS2216-2XG-4S+4XS-2XQ。
- CPU 架構：ARM 64bit。
- CPU 核心數：16。
- CPU：AL73400 2000 MHz。
- RAM 容量：32 GB。
- RAM 型別：DDR4。
- 儲存（FLASH）：32 MB。
- 儲存（NAND）：128 MB。
- 1G 乙太網埠數量：1。
- 1G/2.5G/5G/10G 乙太網埠數量：2。
- 10G SFP+ 埠數量：4。
- 25G SFP28 埠數量：4。
- 100G QSFP28 埠數量：2。
- 交換晶片型號：98DX4310。
- 交換晶片與 CPU 的連線：4x25 Gbps。
- 作業系統：僅 RouterOS v7，License level 6。
- 尺寸：476 x 443 x 29 mm。
- 工作溫度：-20°C 至 +50°C。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- M.2 SATA 插槽數量：2
- 2.5" 硬碟托架數量：20（僅限最大高度為 7mm 的 U.2 格式 SSD 硬碟）
- USB 插槽：2（USB 3.0 Type A 和 USB 2.0 Type A）
- 序列控制檯埠：RJ45 RDS2216-2XG-4S+4XS-2XQ 具有連線到兩個 M.2 插槽的 SATA3 連線。推薦使用無容量限制的 SATA3 M.2 2280mm B+M key SSD 硬碟。

## 供電 {#powering}

本裝置配備兩個熱插拔 IEC 型交流電源，功率 550W，支援 100-240 V ⏦（~ 50/60 Hz，最大 7 A）。

不安裝任何附加元件時的最大功耗為 105 W，在最大負載下可達到 286W。

- 100G QSFP28 支援的速度：1x 100G；1x 40G；4x 25G；4x 10G；4x 1G。不支援：2x 50G；1x 50G；2x 40G
- 25G SFP28 支援的速度：1x 25G；1x 10G；1x 2.5G；1x 1G。不支援：1x 5G

## 首次使用 - 連線磁碟前先設定 RouterOS {#first-use---routeros-set-up-before-connecting-disks}

- 將您的 PC 連線到標有 MGMT/BOOT 的埠或第一個乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 配置應透過網頁瀏覽器中的 WebFig 或 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 完成。在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝磁碟 {#install-disks}

安裝磁碟的步驟：

- 按下右側的按鈕並拉出，即可開啟托架。

<p><Img src="/img/5942c386e0f114fa.webp" alt="" width={1600} height={907} /></p>

<p><Img src="/img/c24aa95e89381370.webp" alt="" width={1600} height={860} /></p>

<p><Img src="/img/5788fbf93491c39c.webp" alt="" width={1600} height={859} /></p>

<p><Img src="/img/177647d5a315990c.webp" alt="" width={1600} height={859} /></p>

- 將硬碟安裝到支架內（可選擇用螺絲固定）。

<p><Img src="/img/cec144967554097a.webp" alt="" width={1600} height={858} /></p>

<p><Img src="/img/45259a11722d915a.webp" alt="" width={1600} height={858} /></p>

- 將托架插回其插槽，向前推直至鎖定。

<p><Img src="/img/d5be365114c14410.webp" alt="" width={1600} height={860} /></p>

<p><Img src="/img/70f1a7994236ffbd.webp" alt="" width={1600} height={860} /></p>

<p><Img src="/img/06c0b59247132436.webp" alt="" width={1600} height={860} /></p>

<p><Img src="/img/7ce7288d39e29b15.webp" alt="" width={1600} height={860} /></p>

- 硬碟托架從左上角開始編號（從 1 開始），直到右下角的最後一個托架。

<p><Img src="/img/9e9966bf4ad57dbe.webp" alt="" width={1600} height={318} /></p>

(連結)

**在從 RouterOS 裝置上物理移除任何硬碟之前，請務必使用 /disk eject-drive。**

**不支援強制移除，可能導致資料丟失。**

## 安裝 {#mounting}

本裝置設計為室內使用，既可使用隨附的機架安裝耳將其安裝在機架中，也可放置在桌面上。隨附的機架安裝耳套件推薦用於深度不超過 600 mm 的機架。進行機架安裝時，請使用十字螺絲刀按以下步驟操作：

- 將機架安裝耳安裝到裝置的前部兩側。

<p><Img src="/img/01b95e385da33957.webp" alt="" width={1600} height={912} /></p>

<p><Img src="/img/0c98569ecf489ff4.webp" alt="" width={1600} height={912} /></p>

<p><Img src="/img/f19297cc6ede514e.webp" alt="" width={1600} height={912} /></p>

<p><Img src="/img/571df449ab14d41d.webp" alt="" width={1600} height={912} /></p>

- 將後部的小型機架支撐耳安裝到裝置的兩側。

<p><Img src="/img/ca7257427d7f1f08.webp" alt="" width={1600} height={912} /></p>

<p><Img src="/img/0433ddb68eb49ec3.webp" alt="" width={1600} height={912} /></p>

<p><Img src="/img/88d7f2f1a14254a8.webp" alt="" width={1600} height={912} /></p>

<p><Img src="/img/6c1ec1a2a2359b7c.webp" alt="" width={1600} height={912} /></p>

- 將後部的長型機架支撐耳安裝到機架後側。

<p><Img src="/img/3a9329eb2e283df6.webp" alt="" width={1600} height={888} /></p>

- 將裝置安裝到機架中，確保機箱支撐耳牢固地固定在長型支撐耳上。

<p><Img src="/img/a82d115e33a103d9.webp" alt="" width={1600} height={912} /></p>

<p><Img src="/img/f1cd28713f6c7c0e.webp" alt="" width={1600} height={912} /></p>

<p><Img src="/img/c375f0a6b473b9b6.webp" alt="" width={1600} height={912} /></p>

<p><Img src="/img/1aa585e79fd5ec17.webp" alt="" width={1600} height={912} /></p>

<p><Img src="/img/044508c5715427b5.webp" alt="" width={1600} height={888} /></p>

<p><Img src="/img/ad6d89e48e090b66.webp" alt="" width={1600} height={888} /></p>

## 按鈕 {#buttons}

**Reset 按鈕**：

- 在啟動過程中按住此按鈕，直到 USR LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 按住 Reset 按鈕並給裝置上電（等待 "USR" 燈閃爍後變為穩定 "On"，當 "USR" 燈變為 "Off" 時鬆開 Reset 按鈕）——裝置將以 bootp 模式啟動，以便使用 Netinstall 重新安裝 RouterOS。**Netinstall 過程使用 MANAGEMENT/BOOT 乙太網埠。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。無論採用上述哪種方式，如果在裝置上電之前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。若只想載入備份 RouterBOOT 而不進行重設，請在 LED 開始閃爍之前鬆開按鈕。這對於 RouterBOOT 偵錯和恢復很有用。

## LED 指示燈 {#led-indicators}

### 背面板 {#back-panel}

-

當路由器已通電並連線到合適的電源時，PWR1/2 LED 會亮起。

-

USER LED 指示裝置在不同啟動模式下的狀態，例如重設配置或為 Netinstall 工具啟動裝置時。

-

如果任何散熱風扇出現問題，FAULT LED 會亮起。

-

方形的橙色和綠色乙太網埠 LED 指示各個 10G 乙太網埠的活動狀態。

-

三角形的 25G SFP28 和 SFP+ 埠綠色 LED 指示各個 25G SFP28 和 SFP+ 埠的活動狀態。

-

圓形的 100G QSFP28 埠綠色 LED 指示 100G QSFP28 埠各個通道的活動狀態。前面板：

-

USER LED 指示裝置在不同啟動模式下的狀態，例如重設配置或為 Netinstall 工具啟動裝置時。

-

如果任何散熱風扇出現問題，FAULT LED 會亮起。

-

路由器通電時 POWER LED 會亮起。

-

2.5" 硬碟托架 LED（綠色和藍色）指示相應托架中是否安裝了硬碟。

## 配件 {#accessories}

- IEC 電源線 2 條；
- 機架安裝耳（ROSE）；
- 後部小型支撐耳（ROSE）；
- 後部長型機架支撐耳（ROSE）；
- K-90 緊固套件。隨附的機架安裝耳套件推薦用於深度不超過 600 mm 的機架。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。出廠預裝的具體版本可在 /system resource 中檢視。其他作業系統尚未經過測試。
