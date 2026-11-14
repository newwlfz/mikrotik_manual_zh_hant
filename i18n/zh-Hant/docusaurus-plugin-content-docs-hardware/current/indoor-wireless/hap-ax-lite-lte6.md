---
title: "hAP ax lite LTE6"
slug: /hap-ax-lite-lte6
source: https://manual.mikrotik.com/hardware/hap-ax-lite-lte6
captured_at: '2026-11-04T05:58:23+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/570befc167b9f654.jpg" alt="" width={503} height={799} /></p>

:::info 本文涵蓋

- hAP ax lite LTE6
- L41G-2axD&FG621-EA
:::

## 安全警告 {#safety-warnings}

- 在操作任何 MikroTik 裝置之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。完整規格和宣傳資料請參閱 [hAP ax lite LTE6 產品頁面](https://mikrotik.com/product/hap_ax_lite_lte6)。
- 僅使用製造商認可的電源和配件，這些均可在本產品的原包裝中找到。
- 本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責確保裝置的安裝符合當地和國家的電氣規範。請勿嘗試拆卸、修理或改裝本裝置。
- 本產品適合在室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源介面卡從電源插座中拔出。
- 介面卡應安裝在裝置附近，並應便於接觸。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置應與您的身體、職業使用者或公眾保持不小於 20 釐米的距離。

## 設定 {#setup}

- 確保您的網際網路服務提供商 (ISP) 允許硬體更改並自動分配 IP 地址；
- 將您的計算機連線到其中一個乙太網埠；
- 配置您的計算機透過 DHCP 自動獲取 IP 地址；
- 將 micro SIM 卡插入卡槽；

<p><Img src="/img/ff6ca66ab0388496.webp" alt="" width={1375} height={1383} /></p>

- IMEI 號可在機殼和包裝標籤上找到；
- 將電源介面卡連線到 DC 插孔；
- 透過任一埠或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具：[https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 使用預設 IP 地址 192.168.88.1，在所選工具中開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 "Check for updates" 並將您的 RouterOS 軟體更新到最新版本，以更新裝置。必須插入有效的 SIM 卡；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單並重啟裝置。透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您所在的國家/地區，以應用該國家/地區的法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

<p><Img src="/img/9bcba09a7b6a0d53.webp" alt="" width={249} height={246} /></p>

- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟該應用程式。
- 預設情況下，IP 地址和使用者名稱已預先填入。
- 單擊 Connect，透過無線網路與您的裝置建立連線。
- 選擇 Quick Setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可完整配置所有必要設定。

## 供電 {#powering}

裝置可透過以下方式接受供電：

- USB type C 接受 5 V DC⎓。最大負載下的功耗可達 12 W。

## 配置 {#configuration}

登入後，我們建議在 QuickSet 選單中點選 "Check for updates" 按鈕，因為將您的 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將要使用所在的國家/地區，以符合當地法規。除本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以讓裝置引導以進行重新安裝，請參閱按鈕與跳線部分。

## 按鈕和跳線 {#buttons-and-jumpers}

reset 按鈕具有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 持續按住 reset 按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請使裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議同時驗證這兩個選項，以防其中一個無法使用。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置通電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置通電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。視型號而定，這可能由 **USR、USER、System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統將載入備份的 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復非常有用。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。
