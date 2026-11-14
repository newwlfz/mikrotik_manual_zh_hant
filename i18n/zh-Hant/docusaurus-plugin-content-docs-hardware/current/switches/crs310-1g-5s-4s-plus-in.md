---
title: "CRS310-1G-5S-4S+IN"
slug: /crs310-1g-5s-4s-plus-in
source: https://manual.mikrotik.com/hardware/crs310-1g-5s-4s-plus-in
captured_at: '2026-11-04T09:46:06+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/c2ccbbb17e2abdb5.jpg)

## [CRS310-1G-5S-4S+IN](https://mikrotik.com/product/crs310_1g_5s_4s_in) {#crs310-1g-5s-4sin}

10 千兆光纖連線距離遠超 100 米——適用於小型辦公室或 ISP。以經濟實惠的成本實現硬體解除安裝的 VLAN 過濾，甚至還能進行部分 L3 路由！有關完整規格和產品手冊，請參見 [CRS310-1G-5S-4S+IN 產品頁面](https://mikrotik.com/product/crs310_1g_5s_4s_in)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置應安裝在機架中。請在開始安裝前仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品適合在室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 請僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 在網頁瀏覽器中使用 WebFig，或使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，可確保最佳效能、穩定性和安全更新；
- 設定路由器密碼。

## 安裝 {#mounting}

![](/img/27bf22aa32ecbced.webp)

本裝置設計用於室內，可使用隨附的機架耳安裝在機架機箱中，也可以放置在桌面上。如果希望放置在平整表面上，請在路由器底部貼上橡膠腳墊；如果指定用於機架機箱，請使用十字螺絲刀將機架耳安裝在裝置兩側。

- 將機架耳安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如右圖所示。
- 將裝置放入機架機箱並對準孔位，使裝置能夠方便地安裝。
- 擰緊螺絲將其固定到位。本裝置的 IP 防護等級為 IPX0。本裝置沒有防水汙染保護，請確保將裝置放置在乾燥通風的環境中。我們建議為我們的裝置使用遮蔽 Cat5/6 線纜。*本裝置的安裝和配置應由有資質的人員完成。*

## 供電 {#powering}

本裝置可透過直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，正極針式插頭）接受 18-57 V DC ⎓ 輸入。管理埠支援 802.3af/at 和被動 PoE 電源輸入（18-57 V DC）。本裝置在最大負載下的功耗最高為 20 W。

## 規格 {#specifications}

<table><thead><tr><th>**產品程式碼**</th><th>CRS310‑1G‑5S‑4S+IN</th></tr></thead><tbody><tr><td>**CPU**</td><td>98DX226S, 800 MHz</td></tr><tr><td>**CPU 架構**</td><td>ARM 32bit</td></tr><tr><td>**CPU 核心數**</td><td>2</td></tr><tr><td>**交換晶片型號**</td><td>98DX226S</td></tr><tr><td>**RAM**</td><td>256 MB DDR3</td></tr><tr><td>**儲存**</td><td>16 MB Flash</td></tr><tr><td>**10/100/1000 Mbps 乙太網 (RJ45)**</td><td>1</td></tr><tr><td>**1G SFP 埠**</td><td>5</td></tr><tr><td>**10G SFP+ 埠**</td><td>4</td></tr><tr><td>**作業系統**</td><td>RouterOS v7 (License Level 5)</td></tr><tr><td>**工作溫度**</td><td>‑40 °C 至 +70 °C</td></tr><tr><td>**外殼尺寸**</td><td>200 × 166 × 44.5 mm</td></tr></tbody></table>

## 配置 {#configuration}

RouterOS 的完整文件可在 [https://mt.lv/help](https://mt.lv/help) 獲取。可以使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 來配置本裝置。**提供多種配置方式以確保可訪問性。**

在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。

本裝置配備一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。出於恢復目的，可以從網路重新安裝裝置，請參見復位按鈕。

Marvell Prestera 交換晶片的功能在 [Marvell Prestera 交換晶片功能](/docs/bridging-and-switching/marvell-prestera-switch-chip-features)手冊中有描述。

## 復位按鈕 {#reset-button}

- 要復位配置，請斷開裝置電源，按住復位按鈕，並在 USER (USR) LED 開始閃爍時鬆開。
- 要載入備份載入程式，請在通電前按住復位按鈕，三秒後鬆開。
- 要啟動 Netinstall 過程（以 BOOTP 模式引導裝置以重新安裝 RouterOS），請按住復位按鈕，給裝置通電，等待 USER (USR) LED 閃爍後變為常亮。當 USR LED 熄滅時，鬆開復位按鈕。

無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## LED 指示燈 {#led-indicators}

- 當路由器由 DC 插孔或 PoE 供電時，電源 LED 點亮。
- 使用者 LED 可以在 RouterOS 中配置。
- 埠 LED 指示各個乙太網和 SFP 埠的狀態。

## 配件 {#accessories}

包裝內含以下隨裝置附帶的配件：

![](/img/8c36c3fbb0b4f6fe.webp)

請訪問 wiki 頁面檢視 MikroTik SFP 模組相容性表：MikroTik 有線介面相容性。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。
