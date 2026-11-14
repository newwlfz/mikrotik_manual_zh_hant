---
title: "hAP ax S"
slug: /hap-ax-s
source: https://manual.mikrotik.com/hardware/hap-ax-s
captured_at: '2026-11-04T05:58:24+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/15dd9306a8f3327b.jpg" alt="" width={799} height={370} /></p>

## [hAP ax S](https://mikrotik.com/product/hap_ax_s) (E62iUGS-2axD5axT) {#hap-ax-s-e62iugs-2axd5axt}

這是我們目前最具價效比的 Wi-Fi 6 接入點。三鏈 5 GHz 射頻（吞吐量最高 900 Mbit/s）、雙頻 Wi-Fi 6、5 個千兆乙太網埠以及一個 2.5G SFP。搭載雙核 ARM CPU，具備 PoE-in/PoE-out 靈活性、標準 DC 插孔、USB，以及可壁掛安裝的堅固高階外殼。完整規格和宣傳冊請參見 [hAP ax S 產品頁面](https://mikrotik.com/product/hap_ax_s)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置擬安裝於機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或未遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 本產品擬在室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，操作風險自負！
- 如果裝置出現故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：**本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和執行時，與身體、職業使用者或公眾的距離不得小於 20 釐米。

## 供電 {#powering}

- DC 輸入數量：2（DC 插孔、PoE-IN）。
- PoE-in 輸入電壓：18-28 V。
- DC 插孔輸入電壓：12-28 V。
- PoE-out 埠：Ether5。
- 最大總輸出：0.6 A。
- 總輸出功率：16.8 W。
- 電源介面卡標稱電壓 24 V。
- 電源介面卡標稱電流 1.5 A。
- 最大功耗（不含附件）11 W。
- 最大功耗 34 W。

## 設定 {#setup}

- 確保你的網際網路服務提供商（ISP）允許更換硬體並自動分配 IP 地址；
- 將 ISP 網線連線到 Ethernet1 埠；
- 將裝置連線到電源；
- 透過除 Ethernet1 之外的任意埠，或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者使用網頁瀏覽器中的 WebFig，或 "WinBox" 配置工具：[https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇你的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可確保最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇你的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定無線網路密碼；
- 在底部欄位中設定路由器密碼。

## 配置 {#configuration}

完整的 RouterOS 文件位於此處：[https://mt.lv/help](https://mt.lv/help) 裝置出廠時已預配置為路由器：WAN 埠（Ethernet1）受防火牆保護並執行 DHCP，而所有其他乙太網埠和無線介面都屬於 LAN 網橋。要設定裝置，請將 ISP 網線連線到 Ethernet1 埠，並將裝置接入電源。然後使用除 Ethernet1 之外的任意乙太網埠訪問裝置，或加入名為“MikroTik‑…”的預設 Wi‑Fi 網路。Wi‑Fi 密碼印在裝置附帶的貼紙上。你可以透過移動應用程式、網頁瀏覽器中的 WebFig 或 WinBox 工具（從 [https://mt.lv/winbox](https://mt.lv/winbox) 下載）進行連線。使用預設 IP 地址 192.168.88.1 進行配置；如果該地址無法訪問，請開啟 WinBox，轉到“Neighbors”標籤頁，發現裝置。如需恢復，可以使用 Reset 按鈕透過網路重新安裝韌體。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

<table><thead><tr><th>**引數**</th><th>**值**</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>E62iUGS-2axD5axT</td></tr><tr><td>**架構**</td><td>ARM 32bit</td></tr><tr><td>**CPU**</td><td>EN7562CT，雙核，950 MHz</td></tr><tr><td>**CPU 核心數**</td><td>2</td></tr><tr><td>**CPU 執行緒數**</td><td>2</td></tr><tr><td>**交換晶片型號**</td><td>EN7523</td></tr><tr><td>**RouterOS 許可證**</td><td>Level 4</td></tr><tr><td>**作業系統**</td><td>RouterOS v7</td></tr><tr><td>**RAM 容量**</td><td>512 MB</td></tr><tr><td>**儲存容量**</td><td>128 MB NAND</td></tr><tr><td>**測試環境溫度**</td><td>-40 °C 至 +70 °C</td></tr><tr><td>**無線 2.4 GHz 最大資料速率**</td><td>574 Mbit/s</td></tr><tr><td>**無線 2.4 GHz 鏈數**</td><td>2</td></tr><tr><td>**無線 2.4 GHz 標準**</td><td>802.11b/g/n/ax</td></tr><tr><td>**天線增益（2.4 GHz）**</td><td>5.5 dBi</td></tr><tr><td>**無線 2.4 GHz 晶片型號**</td><td>MT7916</td></tr><tr><td>**無線 2.4 GHz 代際**</td><td>Wi-Fi 6</td></tr><tr><td>**無線 5 GHz 最大資料速率**</td><td>2400 Mbit/s</td></tr><tr><td>**無線 5 GHz 鏈數**</td><td>3</td></tr><tr><td>**無線 5 GHz 標準**</td><td>802.11a/n/ac/ax</td></tr><tr><td>**天線增益（5 GHz）**</td><td>6.5 dBi</td></tr><tr><td>**無線 5 GHz 晶片型號**</td><td>MT7976</td></tr><tr><td>**無線 5 GHz 代際**</td><td>Wi-Fi 6</td></tr><tr><td>**Wi-Fi 速率**</td><td>AX3000</td></tr><tr><td>**10/100/1000 乙太網埠（RJ45）**</td><td>5</td></tr><tr><td>**帶 PoE-Out 的 1G 乙太網埠**</td><td>1（Ether5）</td></tr><tr><td>**光纖（SFP）**</td><td>1 × SFP（支援 2.5G）</td></tr><tr><td>**USB 埠**</td><td>1 × USB Type-A</td></tr><tr><td>**USB 電源重設**</td><td>是</td></tr><tr><td>**最大 USB 電流（A）**</td><td>1 A</td></tr><tr><td>**DC 輸入數量**</td><td>2（DC 插孔、PoE-IN）</td></tr><tr><td>**DC 插孔輸入電壓**</td><td>12–28 V</td></tr><tr><td>**PoE-IN 型別**</td><td>被動 PoE</td></tr><tr><td>**PoE-IN 電壓**</td><td>18–28 V</td></tr><tr><td>**PoE-Out 埠**</td><td>Ether5（被動 PoE）</td></tr><tr><td>**PoE-Out 最大電流**</td><td>0.6 A</td></tr><tr><td>**PoE-Out 總功率**</td><td>16.8 W</td></tr><tr><td>**最大功耗**</td><td>34 W</td></tr><tr><td>**最大功率（不含附件）**</td><td>11 W</td></tr><tr><td>**IP 防護等級**</td><td>IP20</td></tr><tr><td>**其他**</td><td>CPU 溫度監控</td></tr></tbody></table>

## 按鈕和跳線 {#buttons-and-jumpers}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 繼續按住復位按鈕，直到 LED 變為常亮，然後鬆開以啟用 CAP 模式。裝置隨後將開始搜尋 CAPsMAN 伺服器。
- 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議在其中一個無法工作時對兩個選項都進行驗證。

- **Regular Booter：**要進入 etherboot 模式，請在給裝置上電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter：**關閉裝置電源。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，準備好透過 **Netinstall** 重新安裝 RouterOS。根據型號的不同，這可能會由 **USR、USER、System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

無論使用上述哪種選項，只要在裝置通電之前按下按鈕，系統就會載入備份 RouterBOOT 載入器。這可用於 RouterBOOT 偵錯和恢復。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。
