---
title: "hEX 升級版"
slug: /hex-refresh
source: https://manual.mikrotik.com/hardware/hex-refresh
captured_at: '2026-11-04T05:58:40+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/8eba059757e4b7d0.jpg" alt="" width={799} height={523} /></p>

## [hEX refresh](https://mikrotik.com/product/hex_2024) (E50UG) {#hex-refresh-e50ug}

經典的 hEX refresh：同樣的價格，兩倍的效能！這款每個家庭都負擔得起的路由器迴歸了——憑藉現代 ARM CPU 和更大的記憶體，它比以往更強大。完整規格和宣傳冊請參見 [hEX refresh 產品頁面](https://mikrotik.com/product/hex_2024)。

## 安全警告 {#safety-warnings}

- 在對任何 MikroTik 裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。安裝人員應熟悉網路結構、術語和概念。
- 僅使用製造商認可的電源和配件，這些電源和配件可在本產品的原始包裝中找到。
- 本裝置應由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責確保裝置的安裝符合當地和國家的電氣規範。請勿嘗試拆卸、維修或改裝裝置。
- 本產品僅供室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 我們無法保證因裝置使用不當而不會發生事故或損壞。請小心使用本產品，風險自負！
- 電源插座應安裝在裝置附近，並應便於插拔。
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源介面卡與電源插座的連線。

## 快速開始 {#quickstart}

- 將 ISP 網線連線到 Ethernet1 埠，並將本地網路計算機連線到 2-5 埠；
- 將裝置連線到電源；
- 配置網路卡設定，使其透過 DHCP 自動獲取 IP 地址；
- 應使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具進行配置 [https://mt.lv/winbox](https://mt.lv/winbox)。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 以開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性以及安全更新；
- 設定您的路由器密碼。

## 配置 {#configuration}

除了本文件中描述的內容之外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help) 開始，以熟悉各種可能性。如果無法建立 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參閱復位按鈕。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個 10/100/1000 千兆乙太網埠。
- 一個 USB 2.0 type-A 埠。
- Ether1 上的 PoE 輸入。

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，即可將 RouterOS 配置恢復為預設值。
- 在 LED 熄滅後鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路安全重灌 RouterOS 時需要）。

無論使用上述哪種方式，如果在裝置接通電源之前按住按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 模式按鈕 {#mode-button}

可以透過 RouterOS 軟體配置模式按鈕的動作，以執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。模式按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## 配件 {#accessories}

包裝內含以下隨裝置提供的配件：

- DC ⎓ EU/US 開關電源 24 V，0.38 A，9 W，Level VI，線纜：1.5 m。

## 規格 {#specifications}

- CPU：EN7562CT 950 MHz。
- CPU 架構：ARM。
- CPU 核心數：2。
- 記憶體大小：512 MB。
- RAM 型別：DDR3L。
- 儲存：128 MB，NAND。
- 1G 乙太網埠數量：5。
- USB 埠：1 個（2.0 type A）。
- PoE 輸入：Ether1。
- 作業系統：RouterOS（許可證級別 4）。
- 交換晶片型號：EN7562CT。
- 工作溫度：-40°C 至 +70°C。
- 尺寸：113 x 89 x 28 mm。
- IP20。

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/hex_2024](https://mikrotik.com/product/hex_2024)

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。
