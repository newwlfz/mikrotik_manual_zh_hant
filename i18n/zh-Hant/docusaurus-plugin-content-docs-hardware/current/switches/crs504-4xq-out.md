---
title: "CRS504-4XQ-OUT"
slug: /crs504-4xq-out
source: https://manual.mikrotik.com/hardware/crs504-4xq-out
captured_at: '2026-11-04T09:47:01+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/88498ad0f5a4d896.jpg)

價格實惠、結構緊湊、節能高效的 100 Gbps 網路，隨時隨地（ANYWHERE）！IP66 防護外殼，4 個 100 Gigabit 埠，多種供電方式。完整規格和宣傳冊請參見 [CRS504-4XQ-OUT 產品頁面](https://mikrotik.com/product/crs504_4xq_out)。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵循所有國家法律和法規。裝置的安裝必須符合當地和國家電氣規範。本裝置適用於機架安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟，可能對人員造成危險並損壞系統。本產品適用於室內安裝。請使本產品遠離水、火、潮溼或高溫環境。僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！如果裝置發生故障，請斷開其電源。最快的做法是將電源插頭從電源插座上拔下。客戶有責任遵守所在國家/地區的規定，包括在合法頻段內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 用您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在 Web 瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可確保最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。該裝置應用於光纖場景，線纜可穿過電纜密封接頭後連線到 QSFP 模組。它還支援帶不可分離聯結器的 DAC、AOC 和 Breakout 線纜，但在某些埠上使用時，必須拆下電纜密封接頭。請注意，在不使用電纜密封接頭的情況下使用本裝置，其 IP 等級將從 IP66 降至 IP54。

## 安裝 {#mounting}

## 250 {#250}

## 供電 {#powering}

- DC 輸入數量 3（PoE-in、DC 插孔、2 針端子）
- PoE-in 輸入電壓 43-57 V 802.3bt
- DC 插孔輸入電壓 36-57 V
- 2 針端子輸入電壓 36-57 V
- 電源介面卡標稱電壓 48 V
- 電源介面卡標稱電流 0.95 A
- 最大功耗（不含附件）25 W
- 最大功耗 38 W

## 配置 {#configuration}

RouterOS 的完整文件參見：[https://mt.lv/help](https://mt.lv/help) 您可以在 Web 瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置裝置。**提供多種配置方式以確保可訪問性。** **要開始設定，請在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始設定。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。裝置配有 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。出於恢復目的，可以從網路重新安裝裝置，請參閱 Reset 按鈕。

Marvell Prestera 交換晶片功能使用者手冊

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 4CRS504-4XQ-OUT
- 產品程式碼 CRS504-4XQ-OUT
- CPU QCA9531 650 MHz
- CPU 架構 MIPSBE
- CPU 核心數 1
- RAM 容量 128 MB
- 儲存 32 MB，Flash
- 100M 乙太網埠數量 1
- 100G QSFP28 埠數量 4
- 交換晶片型號 98DX4310
- IP 等級 IP66
- 尺寸 330 x 200 x 70 mm
- 作業系統 RouterOS v7，許可級別 5
- 工作溫度 -40°C 至 +70°C

## Reset 按鈕 {#reset-button}

- 要重設配置，請斷開裝置電源，按住 Reset 按鈕，當 USER（USR）LED 開始閃爍時鬆開。
- 要載入備份載入程式，請在通電前按住 Reset 按鈕，然後三秒後鬆開。
- 要啟動 Netinstall 過程（以 BOOTP 模式啟動裝置以重新安裝 RouterOS），請按住 Reset 按鈕，給裝置通電，等待 USER（USR）LED 閃爍後變為常亮。當 USR LED 熄滅時，鬆開 Reset 按鈕。無論使用上述哪種方式，只要在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內含以下隨裝置提供的附件：

![](/img/da4a2e2f6fc0b0d2.webp)

有關 MikroTik SFP 模組相容性和配置表，請訪問幫助頁面：MikroTik wired interface compatibility

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。
