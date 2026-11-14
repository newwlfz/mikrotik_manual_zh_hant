---
title: "Chateau 5G R16"
slug: /chateau-5g-r16
source: https://manual.mikrotik.com/hardware/chateau-5g-r16
captured_at: '2026-11-04T09:45:03+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/203403343d66ae6f.webp)

## [Chateau 5G R16](https://mikrotik.com/product/chateau5gr16)（D53G-5HacD2HnD-TC&RG520F-EU） {#chateau-5g-r16-d53g-5hacd2hnd-tcrg520f-eu}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請先了解與電路相關的危險，並熟悉防止事故的標準做法。完整的規格和手冊請參閱 [Chateau 5G R16 產品頁面](https://mikrotik.com/product/chateau5gr16)。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置都必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置距離您的身體、職業使用者或公眾不得小於 20 釐米。

## 快速開始 {#quickstart}

按照以下快速步驟設定您的裝置：

![](/img/cbc5361d4144eab4.webp)

- 將 micro SIM 卡插入裝置下方的卡槽；

![](/img/9619076cdc698366.webp)

- 將計算機連線到其中一個乙太網埠；
- 將電源介面卡連線到 DC 插孔；
- 裝置通電且 PC 已連線到裝置後，在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始配置（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 使用者名稱：a*dmin*，預設沒有密碼，您將自動登入到 Quick Set 介面；
- 您應點選右側的 "Check for updates" 按鈕，並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性，必須插入有效的 SIM 卡；
- 如需手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 查詢您的產品。所需的軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 **WinBox** 的 **Files** 選單並重啟裝置。透過將 RouterOS 軟體升級到最新版本，您可以確保最佳效能、穩定性和安全更新；
- 要個性化您的無線網路，可在 "Network Name" 欄位中更改 SSID；
- 在螢幕左側的 "Country" 欄位中選擇您所在的國家，以應用國家法規設定；
- 在 "WiFi Password" 欄位中設定無線網路密碼，密碼必須至少為八個字元；
- 在右側底部的 "Password" 欄位中設定路由器密碼，並在 "Confirm Password" 欄位中重複輸入，下次登入時將使用該密碼；
- 選擇 "Apply Configuration" 儲存更改。

## 使用移動應用連線 {#connecting-with-a-mobile-app}

使用您的智慧手機透過 WiFi 訪問路由器。

![](/img/9bcba09a7b6a0d53.webp)

- 插入 SIM 卡併為裝置通電。
- 用智慧手機掃描 QR 碼並選擇您首選的作業系統。
- 連線到無線網路。SSID 以 MikroTik 開頭，幷包含裝置 MAC 地址的最後幾位數字。
- 開啟應用程式。
- 預設情況下，IP 地址和使用者名稱將已自動填入。
- 選擇 Connect，透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 可使用高階選單來完整配置所有必要設定。

## 規格 {#specifications}

- 產品程式碼 D53G-5HacD2HnD-TC&RG520F-EU
- CPU 四核 IPQ-4019 716 MHz
- CPU 架構 ARM 32bit
- CPU 核心數 4
- 記憶體大小 256 MB
- 記憶體型別 DDR3L
- 儲存 128 MB，NAND
- 1G 乙太網埠數量 5
- USB 1 個 USB 2.0 A 型埠
- 交換晶片型號 IPQ-4019
- 無線 2.4 GHz 802.11a/b/g/n 雙鏈，5 GHz 802.11a/n/ac 雙鏈
- 無線天線最大增益 2.4 GHz - 3 dBi，5 GHz - 5,5 dBi
- 天線波束寬度 360°
- MIMO DL 2x2
- MIMO UL 1x1
- LTE 類別 20（下行 2.0 Gbps，上行 200 Mbps）
- LTE FDD 頻段：5 (850MHz) / 20 (800MHz) / 28 (700MHz) / 3 (1800MHz) / 1 (2100MHz) / 7 (2600MHz) / 8 (900 MHz) / 32 (1500 MHz)
- LTE TDD 頻段：40 (2300MHz) / 41 (2500MHz) / 42 (3500MHz) / 43 (3700MHz) / 38 (2600MHz)
- 3G 類別 R8（下行 42.2Mbps，上行 5.76Mbps）
- 3G 頻段 5 (850MHz) / 8 (900MHz) / 1 (2100MHz)
- TAC 86945405
- 尺寸 240 x 156 x 44 mm
- 作業系統 RouterOS v7，許可證級別 4
- IP 20
- 工作溫度 -40°C 至 +70°C

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/448fe884f3fe7820.webp)

- 復位按鈕。
- 供電 DC 插孔 2.0 mm。
- 五個千兆埠，支援自動交叉/直通線纜糾正（Auto MDI/X）。連線到其他網路裝置時，可使用直通線或交叉線。
- USB A 型。
- 用於 Micro SIM 卡的 SIM 卡槽。
- 模式按鈕。
- 帶天線的型號不提供外接 SMA 天線接頭的蓋板。
- WPS Sync 按鈕。
- 整合無線模組，工作在 2.4 GHz，802.11b/g/n 協定。天線增益 3 (dBi)。
- 整合無線模組，工作在 5 GHz，802.11a/n/ac 協定。天線增益 5.5 (dBi)。

## 安裝 {#mounting}

本裝置設計為室內使用，可放置在桌面上。

您應使用 Cat5 遮蔽線纜。使用和安裝本裝置時，請注意最大允許暴露（MPE）安全距離，輻射體與您的身體之間至少應保持 20 釐米。

## 供電 {#powering}

本裝置透過介面卡供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）12-28 V DC⎓。最大負載下的功耗可達 15 W，連線附件時為 25 W。

## 配置 {#configuration}

您應經常檢查更新，以獲取 RouterOS 軟體的最新更新，從而確保最佳效能和穩定性。除本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以讓裝置引導以進行重新安裝，請參閱“按鈕和跳線”章節。

## 模式按鈕 {#mode-button}

模式按鈕位於裝置背面右側。模式按鈕的預設配置為暗色模式 - 關閉所有 LED。該按鈕可在 RouterOS 中配置為執行任何使用者指定的指令碼。

## Sync 按鈕 {#sync-button}

Sync 按鈕位於裝置頂部。如果在無線介面上進行了配置，WPS Sync 按鈕可用於連線新用戶端。

![](/img/c76f6511aa4e14f0.webp)

- 按住 WPS 按鈕 1 – 5 秒可為無線介面啟用 WPS。

## 前面板 LED 狀態 {#front-led-status}

![](/img/9ba5b3e5c27a0830.webp)

- 無線網路活動。
- 乙太網埠活動。
- 系統 LED，具有交替模式用於指示蜂窩調變解調器狀態。
- 訊號強度。

### 系統 LED 交替調變解調器模式指示 {#system-led-alternate-modem-mode-indications}

當蜂窩調變解調器介面啟用時，系統 LED 具有交替指示：

紅色閃爍 - 未插入 SIM 卡

黃色 - 已在 3G 模式下建立連線

藍色 - 已在 LTE 模式下建立連線

綠色 - 已在 5G NSA 模式下建立連線

紫色 - 已在 5G SA 模式下建立連線

閃爍 - 正在建立連線，調變解調器已註冊到蜂窩網路，APN 尚未啟用

## SIM 卡槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議配合轉接卡使用。

## 復位按鈕 {#reset-button}

復位按鈕具有三種功能：

- 在引導期間按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置隨後將尋找 CAPsMAN 伺服器（共 10 秒）。
- 要使用 Netinstall 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種可用的載入程式：常規載入程式和備用載入程式。常規載入程式 - 給裝置通電，等待 1-2 秒，然後按住復位按鈕。等待系統 LED 呈綠色閃爍，然後變為常亮“On”。當綠色 LED 變為“Off”時，鬆開復位按鈕 - 裝置將進入 BOOTP 模式。
- 備用載入程式 - 關閉裝置電源，按住復位按鈕，然後給裝置通電。等待系統 LED 呈綠色閃爍，然後常亮“On”。當綠色 LED 變為“Off”時，鬆開復位按鈕 - 裝置將使用備用載入程式進入 BOOTP 模式。無論使用上述哪種選項，如果在給裝置通電之前按鈕已被按下，系統都將載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

Netinstall 執行 Netinstall 時，請確保 ROS 檔案和 Netinstall 軟體都使用最新的 v7 版本。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的附件：

- ADAPT1_ EU/US 開關電源 24V，1.2A。
- CAB3_ CAT5E UTP 扁平線纜，8P8C，AWG32，1.5m。本裝置沒有 SMA 接頭或天線。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式進行處置，例如送往指定的廢棄物處置場所。請了解您所在地區將裝置正確運輸至指定處置場所的相關程式。
