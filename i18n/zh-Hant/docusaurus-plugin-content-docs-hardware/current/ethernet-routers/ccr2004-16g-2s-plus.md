---
title: "CCR2004-16G-2S+"
slug: /ccr2004-16g-2s-plus
source: https://manual.mikrotik.com/hardware/ccr2004-16g-2s-plus
captured_at: '2026-11-04T05:55:48+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/f7b1b7928d52fd10.jpg" alt="" width={800} height={228} /></p>

## [CCR2004-16G-2S+](https://mikrotik.com/product/ccr2004_16g_2splus) {#ccr2004-16g-2s}

這款強大且價格實惠的路由器在單核效能上全面超越了以往所有 CCR 型號。16 個千兆乙太網埠、USB、2 個 10G SFP+ 籠、主動散熱，並且在所有 CCR 裝置中擁有最佳的單核效能功耗比和最佳的整體效能功耗比。完整規格與產品手冊請參見 [CCR2004-16G-2S+ 產品頁面](https://mikrotik.com/product/ccr2004_16g_2splus)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準操作規範。
- 本產品的最終處置應按照所有國家和地區的法律法規執行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置預期安裝在機架中。開始安裝之前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的步驟，可能導致人員處於危險狀況並對系統造成損壞。
- 本產品預期在室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可且可在本產品原包裝中找到的電源和配件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 若裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家/地區的規定，包括在法律許可的頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將您的 PC 連線到標有 **MGMT/BOOT** 的埠或第一個乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

<p><Img src="/img/f8d0b2c8b9e368d0.webp" alt="" width={963} height={216} /></p>

本裝置配備雙路整合電源單元，交流電 **⏦** 100-240V，採用標準 IEC 相容插座，最大功耗為 48 W。

## 規格 {#specifications}

- 產品程式碼 CCR2004-16G-2S+
- CPU AL32400 1.7 GHz
- CPU 架構 ARM 64bit
- CPU 核心數 4
- 記憶體大小 4 GB
- 記憶體型別 DDR4
- 儲存 128 MB，NAND
- 1G 乙太網埠數量 16
- 10G SFP+ 埠數量 2
- 作業系統 RouterOS（許可級別 6）
- 交換晶片型號 88E6191X、88E619X
- 尺寸 443 x 210 x 44 mm
- 工作溫度 -20°C 至 +60°C

## 復位按鈕 {#reset-button}

**復位按鈕**：

- 在啟動期間按住此按鈕，直到 USER LED 燈開始閃爍，鬆開按鈕即可復位 RouterOS 配置。
- 按住復位按鈕併為裝置上電（等待 "USER" LED 閃爍後穩定為 "On"，當 "USER" LED 變為 "Off" 時鬆開復位按鈕）——裝置將以 BOOTP 模式啟動，從而使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 重新安裝 RouterOS。**MGMT/BOOT 乙太網埠用於 Netinstall 過程。** 有關使用 Netinstall 恢復工具的說明，請參閱 RouterOS 文件。

無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。若只想載入備份 RouterBOOT 而不復位，請在 LED 開始閃爍之前鬆開按鈕。這對於 RouterBOOT 偵錯和恢復很有用。

## 安裝 {#mounting}

本裝置設計用於室內，可使用隨附的機架安裝件安裝在機架式機箱中，也可放置在桌面上。如果指定用途為機架式機箱，請使用十字螺絲刀將機架安裝耳片安裝到裝置兩側：

<p><Img src="/img/27bf22aa32ecbced.webp" alt="" width={610} height={543} /></p>

- 將機架耳片安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如右圖所示；
- 將裝置放入機架式機箱並對準孔位，使裝置能夠順利裝入；
- 擰緊螺絲將其固定到位。本裝置不具備防水保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 網線。

## 隨附部件 {#included-parts}

<p><Img src="/img/7f015b1e7f1ade2d.webp" alt="" width={807} height={281} /></p>

- PLUG1-2_ EU/US 電源線，JL3-JL38C (D03+QT3) H05VV-F 3x0.75mm2 1.83m
- SET1_ 固定套件 K-57
- CASE3-4_ 1U 機架安裝支架（白色）

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。
