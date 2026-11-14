---
title: "CRS304-4XG-IN"
slug: /crs304-4xg-in
source: https://manual.mikrotik.com/hardware/crs304-4xg-in
captured_at: '2026-11-04T09:45:58+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/def6acc060d0060a.jpg)

## [CRS304-4XG-IN](https://mikrotik.com/product/crs304_4xg_in) {#crs304-4xg-in}

這是一款緊湊而強大的裝置，旨在簡化您的 10 千兆網路部署。它配備 4 個 10G 乙太網埠，開箱即可使用。完整規格與產品手冊請參見 [CRS304-4XG-IN 產品頁面](https://mikrotik.com/product/crs304_4xg_in)。

## 安全警告 {#safety-warnings}

- 在對任何 MikroTik 裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。
- 僅使用製造商認可的電源和附件，這些電源和附件可在本產品的原始包裝中找到。
- 本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責確保裝置的安裝符合當地和國家的電氣規範。
- 請勿嘗試拆卸、修理或改裝本裝置。如需維修，請聯絡 MikroTik 支援。
- 本產品適合在室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 我們無法保證因不當使用本裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 插座應安裝在裝置附近，並且應便於插拔。
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源介面卡。
- 為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如在指定區域處置。請熟悉將裝置妥善運送到您所在地區指定收集點的相關流程。

## 快速開始 {#quickstart}

- 將您的 PC 連線到任意乙太網埠；
- 將裝置連線到電源；
- 將網路卡的 IP 設定配置為 192.168.88.2/24；
- 使用網頁瀏覽器中的 WebFig 或 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁以查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 將 RouterOS 軟體升級到最新版本，可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

這款室內交換器提供多種安裝方式，包括側面的 DIN 導軌安裝和背面的標準螺絲孔位，便於輕鬆整合。DIN 導軌安裝支架還可以重新定位到背面。

![](/img/3ca16901a7457a74.webp)

![](/img/0a49dcd4680dbe4d.webp)

## 供電 {#powering}

本裝置可透過兩個 DC 電源插孔（用於冗餘故障切換）、一個 2 針端子或 MGMT/BOOT 乙太網 PoE-in 埠供電：

- 直接輸入電源插孔 DC1、DC2（外徑 5.5 mm、內徑 2 mm，母頭，中心正極）可接受 DC ⎓ 12-57 V DC。
- MGMT/BOOT 乙太網 PoE-in 埠可接受 DC ⎓ 36-57 V 範圍內的無源或 802.3af/at 乙太網供電。
- 2 針端子可接受 DC ⎓ 12-57 V DC。本裝置在最大負載下的功耗為 21 W，最小負載下為 15 W。使用 802.3af/at 為本裝置供電時，建議不要接地以獲得最佳相容性。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 使用乙太網線將裝置連線到隨附的 PoE 注入器，將其插入 data+power 或 PoE-out 埠；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器。

## 配置 {#configuration}

RouterOS 的完整文件可在 [https://mt.lv/help](https://mt.lv/help) 獲取。本裝置可使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方式以確保可訪問性。**

在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁以查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。

本裝置配備一個 RS-232 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無校驗。出於恢復目的，可以從網路重新安裝裝置，請參閱復位按鈕部分。

Marvell Prestera 交換晶片的特性在 [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) 手冊中有詳細說明。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 四個 1G/2.5G/5G/10G 乙太網埠。
- 一個千兆乙太網埠，建議用於管理（支援 Auto MDI/X，因此您可以使用直通線或交叉線連線到其他網路裝置）。MGMT/BOOT 乙太網埠還可用於透過網路啟動以及使用 Netinstall 進行恢復。

## 復位按鈕 {#reset-button}

- 要重設配置，請斷開裝置電源，按住復位按鈕，並在 USER (USR) LED 開始閃爍時鬆開。
- 要載入備份載入程式，請在通電前按住復位按鈕，三秒後鬆開。
- 要啟動 Netinstall 過程（以 BOOTP 模式啟動裝置以重新安裝 RouterOS），請按住復位按鈕，給裝置通電，等待 USER (USR) LED 閃爍，然後變為常亮。當 USR LED 熄滅時，鬆開復位按鈕。

無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>說明</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>CRS304-4XG-IN</td></tr><tr><td>**架構**</td><td>ARM 64 位</td></tr><tr><td>**CPU**</td><td>98DX2528，2 核，1200 MHz</td></tr><tr><td>**交換晶片型號**</td><td>98DX2528</td></tr><tr><td>**記憶體**</td><td>512 MB</td></tr><tr><td>**儲存**</td><td>32 MB，快閃記憶體</td></tr><tr><td>**乙太網埠**</td><td>4 × 1G/2.5G/5G/10G 乙太網</td></tr><tr><td>**管理埠**</td><td>1 × 10/100/1000 乙太網</td></tr><tr><td>**PoE-in**</td><td>802.3af/at，36-57 V</td></tr><tr><td>**DC 插孔輸入電壓**</td><td>12-57 V</td></tr><tr><td>**2 針端子輸入電壓**</td><td>12-57 V</td></tr><tr><td>**最大功耗**</td><td>21 W</td></tr><tr><td>**無附加裝置時的最大功耗**</td><td>15 W</td></tr><tr><td>**工作溫度**</td><td>-40 °C 至 +70 °C</td></tr><tr><td>**認證**</td><td>CE、EAC、ROHS</td></tr><tr><td>**IP 防護等級**</td><td>IP20</td></tr></tbody></table>

有關本產品、規格和圖片的更多資訊，請訪問我們的網頁：[https://mikrotik.com/product/crs304_4xg_in](https://mikrotik.com/product/crs304_4xg_in)

## 配件 {#accessories}

包裝中包含隨裝置提供的以下附件：

![](/img/d2b681a3d51228f9.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。
