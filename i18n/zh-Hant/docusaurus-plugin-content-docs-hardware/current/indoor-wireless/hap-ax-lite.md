---
title: "hAP ax lite"
slug: /hap-ax-lite
source: https://manual.mikrotik.com/hardware/hap-ax-lite
captured_at: '2026-11-04T05:58:18+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/570befc167b9f654.jpg" alt="" width={503} height={799} /></p>

## [hAP ax lite](https://mikrotik.com/product/hap_ax_lite) (L41G-2axD) {#hap-ax-lite-l41g-2axd}

經濟實惠的 Gen6 無線 —— 小巧、快速，強大到足以發揮 RouterOS v7 的威力！完整規格和宣傳冊請參閱 [hAP ax lite 產品頁面](https://mikrotik.com/product/hap_ax_lite)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家和地區的法律法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於機架安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟，可能導致人員危險和系統損壞。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些電源和配件可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 設定 {#setup}

- 確保您的網際網路服務提供商（ISP）允許更換硬體並自動分配 IP 地址；
- 將 ISP 網線連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 之外的任意埠，或透過無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用位於 [https://mt.lv/winbox](https://mt.lv/winbox) 的 "WinBox" 配置工具。**提供多種配置方式以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中進行以下設定：選擇您的國家，以應用該國家的法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱已預先填入。
- 單擊 Connect，透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用程式將通過幾個簡單的步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要設定。

## 供電 {#powering}

裝置可透過以下方式供電：

- USB Type-C 接受 5 V DC⎓。最大負載下的功耗可達 8 W。

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將要使用的國家，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，以便熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。為便於恢復，可以引導裝置進行重灌，請參閱復位按鈕。

## 安裝 {#mounting}

本裝置設計用於室內，放置在平坦表面上，所有需要的線纜連線到裝置的前部。本裝置的 IP 防護等級為 IPX0。我們建議使用 Cat6 遮蔽網線。警告！本裝置的安裝和操作應與您的身體保持至少 20 釐米的距離。在住宅環境中操作本裝置可能會造成無線電干擾。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼：L41G-2axD。
- CPU：雙核 IPQ-5010 1 GHz。
- CPU 架構：ARM。
- 記憶體大小：256 MB。
- 儲存：128 MB，NAND。
- 1G 乙太網埠數量：4。
- 交換晶片型號：MT7531BE。
- 無線頻段：2.4 GHz。
- 無線介面型號：IPQ-5010。
- 無線 802.11b/g/n/ax：雙鏈。
- 無線天線最大增益：4.3 dBi。
- 尺寸：124 x 100 x 54 mm。
- 作業系統：RouterOS v7，許可證級別 4。
- 工作溫度：-40°C 至 +70°C。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開即可啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩個引導選項可用：**Regular Booter** 和 **Backup Booter**。建議對兩個選項都進行驗證，以防其中一個無法使用。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，可透過 **Netinstall** 重新安裝 RouterOS。視型號不同，這可能由 **USR、USER、System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復非常有用。

## 配件 {#accessories}

產品包裝中包含以下隨裝置提供的配件：

- 5V 2.4A 12W USB 電源介面卡

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢棄物處置場所處置。請了解您所在地區將裝置妥善運送到指定處置場所的相關程式。
