---
title: "Chateau PRO ax"
slug: /chateau-pro-ax
source: https://manual.mikrotik.com/hardware/chateau-pro-ax
captured_at: '2026-11-04T05:56:13+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/138d6597d14f1806.jpg" alt="" width={603} height={799} /></p>

## [Chateau PRO ax](https://mikrotik.com/product/chateau_pro_ax) (H53UiG-5HaxQ2HaxQ) {#chateau-pro-ax-h53uig-5haxq2haxq}

一款面向高階使用者的 Wi-Fi 6 家庭接入點——它配備了效能卓越的無線系統以及與之匹配的 CPU。完整規格和宣傳冊請參見 [Chateau PRO ax 產品頁面](https://mikrotik.com/product/chateau_pro_ax)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適合在室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 插座應安裝在裝置附近，並且便於插拔。
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內工作、輸出功率、布綫要求以及動態頻率選擇 (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定區域處置。請熟悉將裝置正確運送到您所在地區指定收集點的程式。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 設定 {#setup}

- 確保您的網際網路服務提供商 (ISP) 允許更換硬體並自動分配 IP 地址；
- 將 ISP 網線連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 以外的任意埠或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，使用網頁瀏覽器中的 WebFig 或 "WinBox" 配置工具，地址為 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方法以確保可訪問性；**
- 使用預設 IP 地址 192.168.88.1，在所選工具中開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中進行以下設定：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 使用移動應用程式連線 {#connecting-with-a-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟該應用程式。
- 點選 Connect，透過無線網路建立與裝置的連線（請檢視貼紙上的無線密碼）。
- 使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。
- 選擇 Quick Setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要的設定。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼：H53UiG-5HaxQ2HaxQ
- CPU：四核 IPQ-8072A 2208 MHz
- CPU 架構：ARM 64bit
- RAM 容量：1 GB
- RAM 型別：DDR3
- 儲存：128 MB，NAND。
- 1G 乙太網埠數量：5
- 帶 Passive PoE 輸出（高達 57V，最大 0.6A）的 1G 乙太網埠數量：1 個，Ether5
- USB 埠數量：1 個，USB 3.0 type A
- 交換器晶片型號：IPQ-8072
- 無線介面型號：QCN-5024 (2.4 GHz)、QCN-5054 (5 GHz)
- 無線：2.4 GHz 802.11b/g/n/ax 4x4 MIMO，5 GHz 802.11a/n/ac/ax 4x4 MIMO
- WiFi 速率：AX3600
- 尺寸 240 x 156 x 44 mm
- 作業系統 RouterOS v7，許可證級別 6
- 工作溫度 -40°C 至 +70°C
- IP 20

## 安裝 {#mounting}

本裝置設計用於室內使用，可放置在桌面上。

我們建議使用 CAT5 遮蔽網線。使用和安裝本裝置時，請注意最大允許暴露 (MPE) 安全距離，輻射體與您的身體之間至少保持 20 釐米的距離。

## 供電 {#powering}

- DC 輸入數量 1。
- DC 插孔輸入電壓 18-57 V。
- 電源介面卡標稱電壓 48 V。
- 電源介面卡標稱電流 1.35 A。
- 無附加裝置時的最大功耗為 18 W。
- 最大功耗 55 W。
- 網路待機 (HiNA) ≤ 8 W。

## 配置 {#configuration}

我們建議經常檢查更新，以獲取 RouterOS 軟體的最新更新，從而確保最佳的效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具 ([https://mt.lv/winbox](https://mt.lv/winbox)) 從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以啟動裝置進行重新安裝，請參見 Reset 按鈕。

## Mode 按鈕 {#mode-button}

Mode 按鈕位於裝置背面右側。Mode 按鈕的預設配置為深色模式 - 關閉所有 LED。該按鈕可在 RouterOS 中配置為執行任何使用者指定的指令碼。

## Sync 按鈕 {#sync-button}

Sync 按鈕位於裝置頂部。如果已在無線介面上配置 WPS Sync 按鈕，則可用於連線新用戶端。

<p><Img src="/img/c76f6511aa4e14f0.webp" alt="" width={383} height={206} /></p>

- 按住 WPS 按鈕 1 – 5 秒，可為無線介面啟用 WPS。

## 正面 LED 狀態 {#front-led-status}

<p><Img src="/img/9ba5b3e5c27a0830.webp" alt="" width={1174} height={120} /></p>

- 無線網路活動。
- 乙太網埠活動。
- 系統 LED。
- 訊號強度。

## Reset 按鈕 {#reset-button}

Reset 按鈕有三項功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 持續按住 Reset 按鈕，直到 LED 變為常亮，然後鬆開即可啟用 CAP 模式。隨後裝置將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請使裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議對兩種選項都進行驗證，以防其中一種無法使用。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電後等待 1–2 秒，然後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。取決於型號，這可能由 **USR、USER、System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統將載入備份的 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- ADAPT1_ EU/US 開關電源 48 V，1.35 A。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。
