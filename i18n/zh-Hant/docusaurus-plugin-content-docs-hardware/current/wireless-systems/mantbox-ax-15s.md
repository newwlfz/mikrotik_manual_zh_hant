---
title: "mANTBox ax 15s"
slug: /mantbox-ax-15s
source: https://manual.mikrotik.com/hardware/mantbox-ax-15s
captured_at: '2026-11-04T09:56:12+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/17a344f4f237e22e.jpg)

## [mANTBox ax 15s](https://mikrotik.com/product/mantbox_ax_15s)（L22UGS-5HaxD2HaxD-15S） {#mantbox-ax-15s-l22ugs-5haxd2haxd-15s}

這是對廣受歡迎的 mANTBox 雙頻扇區天線基站的一次 Wi-Fi 6 直接升級。一個功能強大的整包方案即可滿足你所有戶外網路需求，非常適合營地、體育場和公園使用。完整規格和宣傳手冊請參見 [mANTBox ax 15s 產品頁面](https://mikrotik.com/product/mantbox_ax_15s)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 本裝置須由經過培訓的合格人員按照這些安裝說明進行安裝。安裝人員負責取得當地主管部門/檢驗部門對安裝結構完整性所要求的任何地方性或國家性安全檢查。
- 在任何牆面上安裝接入點的所有安裝方法均需獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置設計用於在戶外立杆上安裝。開始安裝前請仔細閱讀安裝說明。
- 未使用正確的硬體和配置或未遵循正確的操作步驟，可能會給人員帶來危險狀況並損壞系統。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險。
- 本裝置需要升級到 RouterOS v7 或最新版本，以確保符合當地法規要求。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置安裝和執行時，與你的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

- 開啟蓋子；
- 用網線將裝置的資料+供電端連線到隨附的 PoE 注入器；
- 將 PoE 注入器的資料端連線到計算機；
- 將電源介面卡連線到 PoE 注入器；
- 透過 **WebFig** 或 **WinBox** 工具，使用網頁瀏覽器配置裝置，WinBox 下載地址：[https://mt.lv/WinBox](https://mt.lv/WinBox)；**提供多種配置方式以確保可訪問性；**
- 開啟 [https://192.168.88.1](https://192.168.88.1) 即可訪問 **WebFig**；對於 **WinBox**，請下載該工具，進入 **Neighbors** 標籤頁，然後點選 MAC 地址。使用者名稱為 "**admin**"，無密碼（某些型號的使用者名稱和無線密碼請檢視貼紙）；
- 點選 "Check for updates" 按鈕，將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡並擁有可用的網際網路連線；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇你的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，你可以確保獲得最佳效能、穩定性和安全更新；
- 設定路由器密碼。

## 供電 {#powering}

裝置隨附 24 V 1.2 A 電源介面卡。它可與隨附的 PoE 注入器或電源插孔配合使用。兩種方式下裝置均接受 12-28 V 電壓。裝置的最大功耗為 21 W 時的 11 W。

## 配置 {#configuration}

我們建議點選 "Check for updates" 按鈕，並將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議訪問 RouterOS 文件頁面來熟悉這些可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 internet 埠的所有訪問均被阻止）。

## 安裝 {#mounting}

mANTbox 12s 和 15s 配有 QuickMount 介面卡，可使用隨附的螺絲將其固定在牆上，或使用隨附的金屬安裝環固定在立杆上。QuickMount 允許對裝置進行水平和垂直調節。

- 將快速安裝座安裝到裝置背面。
-

![](/img/6d8362fa9f81276e.webp)

![](/img/f1b9c851a1837362.webp)

- 將裝置安裝到立杆上。
- 使用隨附的鋼製卡箍固定。卡箍直徑 35 – 70 mm。
-

![](/img/006d6b97c4c91436.webp)

- 請避免將鬆散的網線連線到乙太網埠，應將線纜固定在牆壁或立杆上，以免線纜的重量拉扯埠。建議將網線固定在距離裝置不到 2m 的位置。這是為了確保線纜不會因其重量而損壞埠，也不會脫落。我們建議使用 Cat6 遮蔽網線。警告！本裝置的安裝和執行時，裝置與你的身體之間應保持至少 25 cm 的距離。本裝置在住宅環境中執行可能會導致無線電干擾。

請避免將鬆散的網線連線到乙太網埠，應將線纜固定在牆壁或立杆上，以免線纜的重量拉扯埠。建議將網線固定在距離裝置不到 2m 的位置。這是為了確保線纜不會因其重量而損壞埠，也不會脫落。可以透過開啟蓋子連線接地線，那裡提供一個接地螺絲。

## 接地 {#grounding}

安裝基礎設施（塔架和桅杆）以及路由器本身都必須正確接地。裝置在機殼門後帶有接地線連線螺絲。將接地線連線到接地螺絲，然後將接地線的另一端連線到已接地的桅杆上。這可大幅降低 ESD 和雷擊損壞的風險。

![](/img/9d368495fcc09e4b.webp)

裝置帶有接地連線（標記為 ⏚）。

## 開啟蓋子 {#opening-cover}

要開啟蓋子，請用手逆時針擰鬆 captive screw 並將其提起。

![](/img/c9aa40a174a2b89d.webp)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼：L22UGS-5HaxD2HaxD-15S
- CPU：IPQ-5010 800 MHz
- CPU 架構：ARM
- CPU 核心數：2
- RAM 容量：256 MB
- RAM 型別：DDR3L
- 儲存：128 MB，NAND
- 作業系統：RouterOS（License level 4）
- 一個 10/100/1000 千兆乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X），因此你可以使用直通線或交叉線連線到其他網路裝置。該乙太網埠可透過無源 PoE 注入器接受 12-28V DC 供電。
- 一個適用於 2.5GBit 模組的 SFP 埠，支援 DDMI。
- 內建無線介面，2x2 MIMO，AP（RouterOS level 4 許可證）
- 無線介面型號：IPQ-5010（2.4 GHz）、QCN-6102（5 GHz）
- 無線：2.4 GHz 802.11b/g/n/ax 雙鏈；5 GHz 802.11a/n/ac/ax 雙鏈
- 天線增益 2.4 GHz：12 dBi
- 天線增益 5 GHz：15 dBi
- 無線 5 GHz 代際：Wi-Fi 6
- 尺寸 349 x 140 x 68 mm
- 工作溫度 -40°C 至 +70°C
- IP 55

## 按鈕和跳線 {#buttons-and-jumpers}

重設按鈕具有以下功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在將尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這在 RouterBOOT 偵錯和恢復時很有用。

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送往指定的廢棄物處置場所。請了解你所在地區將裝置妥善運送到指定處置場所的相關程式。
