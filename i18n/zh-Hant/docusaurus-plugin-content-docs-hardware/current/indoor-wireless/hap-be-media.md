---
title: "hAP be³ Media"
slug: /hap-be-media
source: https://manual.mikrotik.com/hardware/hap-be-media
captured_at: '2026-11-04T05:58:28+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/8d968a1e825ffb76.webp" alt="" width={1500} height={1200} /></p>

## [hAP be³ Media](https://mikrotik.com/product/hap_be3_media) (MA53UG+HbeH) {#hap-be-media-ma53ughbeh}

面向路由、服務、容器與現代網路工作負載的專業一體化平臺。這是一款功能強大的 Wi-Fi 7 混合路由器與媒體中心，集三頻無線、五個 2.5G 乙太網埠、內建 Matter/Thread 智慧自動化/IoT 支援，以及用於容器、儲存和高階網路的四核 ARM CPU 於一身。完整規格與宣傳手冊請參見 [hAP be³ Media 產品頁面](https://mikrotik.com/product/hap_be3_media)。

### 三頻 2x2 MIMO Wi-Fi 7 {#triple-band-2x2-mimo-wi-fi-7}

hAP be³ Media 在 2.4、5 和 6 GHz 頻段上提供真正的 Wi-Fi 7 效能。你將獲得更高的吞吐量、更低的延遲、更強的安全性以及更好的頻譜效率。寬廣的 6 GHz 頻段提供更多幹淨頻譜，有助於減少繁忙環境中的擁塞。

此外，hAP be³ Media 在 TR-MLMR（AP 模式）下支援 Wi-Fi 7 多鏈路操作（MLO）。

無論你是在執行多裝置環境、網路實驗室、工作站、VR 頭顯、NAS 備份、雲同步還是高解析度媒體流，一切都能同時執行，而無需爭搶空口時間。更多頻段意味著更大容量、更流暢的效能，以及終於能跟上現代工作負載的無線體驗。

- 2.4 GHz 天線增益：4 dBi
- 5 GHz 天線增益：7.5 dBi
- 6 GHz 天線增益：8 dBi

### 所有埠均為 2.5 Gigabit 乙太網 {#25-gigabit-ethernet-on-all-ports}

沒錯——不再有瓶頸！超高速 ISP 上行鏈路、NAS 伺服器、工作站——你全都可以擁有！

### 現代化的混合媒體中心 {#a-modern-hybrid-media-center}

憑藉 USB-C、兩個 USB-A 埠和一個 microSD 卡槽，hAP be³ Media 成為你本地媒體儲存的核心。使用快閃記憶體進行備份、存放照片、影片監控錄影或搭建私有家庭雲。

自託管的密碼管理器、文件和服務——如果你在意隱私與安全，這就是 2026 年的做法。無需依賴外部伺服器即可儲存自動化資料和容器工作負載。一切都保持快速、本地，並且**完全由你掌控**。此外，藉助 MikroTik BTH 應用和 WinBox 中改進的 File share 功能，你可以共享大檔案，而無需擔心連結過期、延遲或隱私問題。

### Matter 很重要：智慧物聯網整合從未如此簡單 {#matter-matters-smart-internet-of-things-integration-has-never-been-easier}

憑藉 Wi-Fi 7、Bluetooth 5.4 和 RouterOS v7，hAP be³ Media 為現代 IoT 部署提供了堅實的基礎。內建的 Thread 無線電和完整的容器支援讓使用者能夠部署 Thread IoT 自動化方案，這些方案保持本地化、私密且完全可自定義。

### 令人印象深刻的四核效能，勝任容器密集型與創意工作流 {#impressive-quad-core-performance-for-container-heavy-creative-workflows}

hAP be³ Media 搭載現代 1.5 GHz 四核 CPU，基於高效的 ARM64 架構，其能力遠超傳統網路用途。容器、本地儀表板、指令碼、複雜防火牆規則、加密、多個 VPN、BGP 和高階路由都能在一臺緊湊的裝置上流暢執行。這是你今天可以信賴的效能，也是在未來數年內始終領先於你日常需求的容量。

如果你認為容器很複雜——再想想！我們在 WinBox 中提供了一個簡單的一鍵設定頁面，你可以在其中啟用所需的容器應用。

從視覺化網路拓撲、託管輕量級網站，到執行自定義儀表板、安全工具，甚至實驗性的本地 AI 助手，容器為你打開了全新可能性的大門。

一如既往，hAP be³ Media 的全部功能都對你開放，沒有任何訂閱或付費牆。你買了它——你就擁有它，這是 MikroTik 的保證！

## 供電 {#powering}

- DC 輸入數量：2（DC 插孔、PoE-IN）。
- PoE-in 輸入電壓：24-57 V。
- DC 插孔輸入電壓：24-57 V。
- 電源介面卡標稱電壓 24 V。
- 電源介面卡標稱電流 1.5 A。
- 最大功耗（不含外接裝置）20 W。
- 最大功耗 29 W。

## 設定 {#setup}

- 確保你的網際網路服務提供商（ISP）允許更換硬體並自動分配 IP 地址；
- 將 ISP 網線連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 以外的任意埠或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用位於 [https://mt.lv/winbox](https://mt.lv/winbox) 的 "WinBox" 配置工具。**提供多種配置方式以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇你的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，你可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇你的國家/地區，以應用該國家/地區的法規設定；
- 在左側欄位中設定你的無線網路密碼；
- 在底部欄位中設定你的路由器密碼。

## 配置 {#configuration}

完整的 RouterOS 文件位於此處：[https://mt.lv/help](https://mt.lv/help) 裝置出廠時已預配置為路由器：WAN 埠（Ethernet1）受防火牆保護並執行 DHCP，而其他所有乙太網埠和無線介面都屬於 LAN 網橋。要設定裝置，請將 ISP 網線連線到 Ethernet1 埠，並將裝置插入電源。然後使用除 Ethernet1 以外的任意乙太網埠，或加入名為 "MikroTik‑…" 的預設 Wi‑Fi 網路來訪問裝置。Wi‑Fi 密碼印在裝置附帶的貼紙上。你可以透過移動應用、網頁瀏覽器中的 WebFig 或 WinBox 工具（從 [https://mt.lv/winbox](https://mt.lv/winbox) 下載）進行連線。使用預設 IP 地址 192.168.88.1 進行配置；如果該地址無法訪問，請開啟 WinBox，進入 "Neighbors" 標籤頁並發現裝置。如需恢復，可以透過網路使用 Reset 按鈕重新安裝韌體。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<table><thead><tr><th>**引數**</th><th>**值**</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>MA53UG+HbeH</td></tr><tr><td>**架構**</td><td>ARM 64bit</td></tr><tr><td>**CPU**</td><td>IPQ-5322</td></tr><tr><td>**CPU 核心數**</td><td>4</td></tr><tr><td>**CPU 執行緒數**</td><td>4</td></tr><tr><td>**CPU 頻率**</td><td>最高 1.5 GHz（自動）</td></tr><tr><td>**交換晶片型號**</td><td>QCA8386</td></tr><tr><td>**RAM**</td><td>2 GB</td></tr><tr><td>**儲存**</td><td>512 MB NAND</td></tr><tr><td>**2.5G 乙太網埠**</td><td>5</td></tr><tr><td>**USB 埠**</td><td>3 × USB 3.0 Type-A（最大 1.5 A）</td></tr><tr><td>**無線 2.4 GHz**</td><td>688 Mbit/s，2 條鏈，802.11b/g/n/ax/be，4 dBi，IPQ-5322，Wi-Fi 7</td></tr><tr><td>**無線 5 GHz**</td><td>2882 Mbit/s，2 條鏈，802.11a/n/ac/ax/be，7.5 dBi，QCM-8083，Wi-Fi 7</td></tr><tr><td>**無線 6 GHz**</td><td>5764 Mbit/s，2 條鏈，802.11ax/be，8 dBi，QXM-8086，Wi-Fi 7</td></tr><tr><td>**WiFi 速率**</td><td>BE9300</td></tr><tr><td>**作業系統**</td><td>RouterOS v7</td></tr><tr><td>**RouterOS 許可**</td><td>Level 6</td></tr><tr><td>**工作溫度**</td><td>-30 °C 至 +50 °C</td></tr><tr><td>**散熱**</td><td>被動散熱</td></tr><tr><td>**DC 輸入**</td><td>2（DC 插孔、PoE-in）</td></tr><tr><td>**DC 插孔電壓**</td><td>24–57 V</td></tr><tr><td>**PoE-in 標準**</td><td>802.3af/at</td></tr><tr><td>**PoE-in 電壓**</td><td>24–57 V</td></tr><tr><td>**最大功耗**</td><td>29 W</td></tr><tr><td>**最大功耗（不含外接裝置）**</td><td>20 W</td></tr><tr><td>**認證**</td><td>CE, FCC, IC, EAC, RoHS</td></tr><tr><td>**防護等級**</td><td>IP20</td></tr><tr><td>**CPU 溫度監控**</td><td>是</td></tr><tr><td>**藍牙**</td><td>5.4</td></tr></tbody></table>

## 按鈕和跳線 {#buttons-and-jumpers}

Reset 按鈕有三個功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住 Reset 按鈕，直到 LED 變為常亮，然後鬆開即可啟用 CAP 模式。裝置隨後會開始搜尋 CAPsMAN 伺服器。
- 如需使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議對兩種選項都進行驗證，以防其中一種無法使用。

- **Regular Booter：** 要進入 etherboot 模式，請在裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：** 關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備透過 **Netinstall** 重新安裝 RouterOS。取決於型號，這可能透過 **USR、USER、System** 或 **ACT** LED 指示，或透過 SFP 埠 LED 指示。

無論使用上述哪種選項，只要在裝置通電之前按下按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及更高版本。具體的出廠預裝版本列於 **/system resource** 中。其他作業系統尚未經過測試。
