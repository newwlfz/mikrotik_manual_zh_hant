---
title: "hAP be 精簡版"
slug: /hap-be-lite
source: https://manual.mikrotik.com/hardware/hap-be-lite
captured_at: '2026-11-04T05:58:24+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/3da852f0ffb505c8.jpg" alt="" width={458} height={800} /></p>

## [hAP be lite](https://mikrotik.com/product/hap_be_lite) (A42G-HbeP) {#hap-be-lite-a42g-hbep}

對於需要 RouterOS 的靈活性與強大功能的網路來說，這是最經濟實惠的 Wi-Fi 7 路由器與接入點。USB-C 供電、2.5 千兆與千兆乙太網、Wi-Fi 7 多鏈路操作、BE3600。完整規格與宣傳資料請參見 [hAP be lite 產品頁面](https://mikrotik.com/product/hap_be_lite)。

hAP be lite 將現代 Wi-Fi 7 效能與 RouterOS 靈活性融入一個緊湊、實惠的平臺，專為空間、外觀、速度和預算同樣重要的場景而打造。緊湊的設計、低功耗（最高 12 W）以及 USB-C 供電，讓幾乎任何位置都能輕鬆部署。

### 效能更強、成本更低的 Wi-Fi 7 {#wi-fi-7-built-to-deliver-more--cost-less}

強大的雙頻 Wi-Fi 7 天線與 Wi-Fi 7 多鏈路操作（MLO）為筆記型電腦、手機、平板電腦及其他日常裝置帶來 BE3600 級別的無線效能。

我們的 Wi-Fi 7 產品專為當今極度擁擠的無線環境而設計，在此環境中，比以往更多的裝置在爭奪同一片空域。即使在繁忙區域，Wi-Fi 7 也有助於保持連線順暢、響應迅速。hAP be lite 結合了雙鏈 2.4 GHz 與三鏈 5 GHz 射頻，在現代裝置最需要的地方提供額外的無線容量。

在有線方面，我們提供三個千兆乙太網埠和一個 2.5 千兆乙太網埠，可用於高速上行鏈路、工作站、NAS 裝置或其他高要求場景。

在內部，hAP be lite 採用主頻 950 MHz 的現代雙核 ARM CPU 和 512 MB RAM，為高階網路任務和繁重流量提供可靠效能。

但硬體只是故事的一部分。藉助 RouterOS，你獲得的遠不止基本的無線連線。你可以構建 VLAN、配置 VPN、進行流量整形、應用高階防火牆規則、透過指令碼實現任務自動化，並完全自定義你的設定以滿足確切需求。

沒有人為限制。沒有訂閱、付費牆或鎖定功能。無論你管理的是單個緊湊部署還是大得多的網路，RouterOS 都能讓你完全掌控。

你還可以使用更新後的 CAPsMAN，透過單一介面集中管理多個 MikroTik 接入點。

## 供電 {#powering}

- DC 輸入數量：1（USB-C）。
- USB-C 輸入電壓：5 V。
- 最大功耗 12 W。

## 設定 {#setup}

- 確保你的網際網路服務提供商（ISP）允許更換硬體並自動分配 IP 地址；
- 將 ISP 線纜連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 以外的任意埠，或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者使用網頁瀏覽器中的 WebFig，或 [https://mt.lv/winbox](https://mt.lv/winbox) 上的 "WinBox" 配置工具。**提供多種配置方式以確保可訪問性；**
- 在所選工具中開始配置，使用預設 IP 地址 192.168.88.1。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，並且沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇你的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，你可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇你的國家/地區，以應用該國家/地區的法規設定；
- 在左側欄位中設定你的無線網路密碼；
- 在底部欄位中設定你的路由器密碼。

## 配置 {#configuration}

完整的 RouterOS 文件位於此處：[https://mt.lv/help](https://mt.lv/help) 裝置出廠時已預配置為路由器：WAN 埠（Ethernet1）受防火牆保護並執行 DHCP，而所有其他乙太網埠和無線介面都是 LAN 網橋的一部分。要設定裝置，請將 ISP 線纜連線到 Ethernet1 埠，並將裝置插入電源。然後使用除 Ethernet1 以外的任意乙太網埠訪問裝置，或加入名為 “MikroTik‑…” 的預設 Wi‑Fi 網路。Wi‑Fi 密碼印在裝置所貼的標籤上。你可以透過移動應用、網頁瀏覽器中的 WebFig 或 WinBox 工具（從 [https://mt.lv/winbox](https://mt.lv/winbox) 下載）進行連線。使用預設 IP 地址 192.168.88.1 進行配置；如果該地址無法訪問，請開啟 WinBox，轉到 “Neighbors” 標籤頁，發現該裝置。如需恢復，可使用 Reset 按鈕透過網路重新安裝韌體。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<table><thead><tr><th>**引數**</th><th>**值**</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>A42G-HbeP</td></tr><tr><td>**架構**</td><td>ARM 32bit</td></tr><tr><td>**CPU**</td><td>AN7563PT</td></tr><tr><td>**CPU 核心數**</td><td>2</td></tr><tr><td>**CPU 執行緒數**</td><td>2</td></tr><tr><td>**CPU 頻率**</td><td>950 MHz</td></tr><tr><td>**交換晶片型號**</td><td>AN7563PT</td></tr><tr><td>**RAM**</td><td>512 MB</td></tr><tr><td>**儲存**</td><td>128 MB NAND</td></tr><tr><td>**2.5G 乙太網埠**</td><td>1</td></tr><tr><td>**1G 乙太網埠**</td><td>3</td></tr><tr><td>**無線 2.4 GHz**</td><td>688 Mbit/s，2 條鏈，802.11b/g/n/ax/be，4.4 dBi，MT7991，Wi-Fi 7</td></tr><tr><td>**無線 5 GHz**</td><td>2882 Mbit/s，3 條鏈，802.11a/n/ac/ax/be，7 dBi，MT7991，Wi-Fi 7</td></tr><tr><td>**WiFi 速率**</td><td>BE3600</td></tr><tr><td>**作業系統**</td><td>RouterOS v7</td></tr><tr><td>**RouterOS 許可證**</td><td>Level 4</td></tr><tr><td>**工作溫度**</td><td>-40 °C 至 +50 °C</td></tr><tr><td>**散熱**</td><td>被動</td></tr><tr><td>**DC 輸入**</td><td>1（USB-C）</td></tr><tr><td>**DC 插孔電壓**</td><td>5 V</td></tr><tr><td>**最大功耗**</td><td>12 W</td></tr><tr><td>**認證**</td><td>CE, FCC, IC, EAC, RoHS</td></tr><tr><td>**防護等級**</td><td>IP20</td></tr><tr><td>**CPU 溫度監控**</td><td>是</td></tr></tbody></table>

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕具有三種功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用程式重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種載入程式選項可用：**Regular Booter** 和 **Backup Booter**。建議兩種選項都驗證一下，以防其中一種無法使用。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備好透過 **Netinstall** 重新安裝 RouterOS。根據型號不同，這可能會由 **USR、USER、System** 或 **ACT** LED 指示，也可能由 SFP 埠 LED 指示。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 **/system resource** 中。其他作業系統尚未測試。
