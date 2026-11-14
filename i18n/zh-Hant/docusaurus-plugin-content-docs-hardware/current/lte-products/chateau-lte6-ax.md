---
title: "Chateau LTE6 ax"
slug: /chateau-lte6-ax
source: https://manual.mikrotik.com/hardware/chateau-lte6-ax
captured_at: '2026-11-04T09:45:30+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/a5d7e76735358694.webp)

## [Chateau LTE6 ax](https://mikrotik.com/product/chateau_lte6_ax) (S53UG+5HaxD2HaxD-TC&FG621-EA) {#chateau-lte6-ax-s53ug5haxd2haxd-tcfg621-ea}

Chateau 是一款家用路由器，用於配合蜂窩網路運營商的 SIM 卡使用。完整規格和宣傳手冊請參見 [Chateau LTE6 ax 產品頁面](https://mikrotik.com/product/chateau_lte6_ax)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請先了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因裝置的不當使用而不會發生事故或損壞。請謹慎使用本產品，操作風險自負！
- 如果裝置發生故障，請將其斷電。最快的方法是拔下電源插頭，從電源插座中斷開。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

按照以下快速步驟設定您的裝置：

![](/img/cbc5361d4144eab4.webp)

- 將您的計算機連線到其中一個乙太網埠；
- 可選——將外接天線連線到 SMA 接頭（包裝中不提供天線，參見 ""）；
- 將 micro SIM 卡插入裝置底部的卡槽；

![](/img/9619076cdc698366.webp)

- 將電源介面卡連線到 DC 插孔；
- 裝置通電且 PC 已連線到裝置後，在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始配置；
- 使用者名稱：a*dmin*，預設沒有密碼，您將被自動登入到 Quick Set 介面（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 透過點選右側的 (*Check_for_updates*) 並將您的 RouterOS 軟體更新到最新版本來更新裝置。必須插入有效的 SIM 卡；
- 如需手動更新裝置，請訪問 [https://mikrotik.com/products](https://mikrotik.com/products) 產品頁面查詢您的產品。所需的軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 (**WebFig**) 的 (**Files**) 選單，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 要個性化您的無線網路，可在 "Network Name" 欄位中更改 SSID；
- 在 (**QuickSet**) 選單中進行以下設定：選擇您的國家/地區，以應用國家法規設定；
- 在 "WiFi Password" 欄位中設定您的無線網路密碼，密碼必須至少為八個字元；
- 在右下方的 "Password" 欄位中設定路由器密碼，並在 "Confirm Password" 欄位中重複輸入，該密碼將在下次登入時使用；
- 選擇 "Apply Configuration" 儲存更改。

## 使用移動應用連線 {#connecting-with-a-mobile-app}

使用您的智慧手機透過 WiFi 訪問路由器。

![](/img/9bcba09a7b6a0d53.webp)

- 插入 SIM 卡併為裝置通電。
- 用智慧手機掃描二維條碼，並選擇您偏好的作業系統。
- 連線到無線網路。SSID 以 MikroTik 開頭，幷包含裝置 MAC 地址的最後幾位數字。
- 開啟應用程式。
- 預設情況下，IP 地址和使用者名稱將已自動填寫。
- 選擇 Connect 以透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 還提供高階選單，可完整配置所有必要的設定。

## 規格 {#specifications}

- 產品程式碼 S53UG+5HaxD2HaxD-TC&FG621-EA
- CPU 四核 IPQ-6010 1.8 GHz
- CPU 架構 ARM 64bit
- CPU 核心數 4
- RAM 容量 1 GB
- RAM 型別 DDR3L
- 儲存 128 MB，NAND
- 1G 乙太網埠數量 4
- 2.5G 乙太網埠數量 1
- USB 1 個 USB 2.0 A 型埠
- 交換晶片型號 IPQ-6010
- 無線 2.4 GHz 802.11b/g/n/ax 雙鏈，5 GHz 802.11a/n/ac/ax 雙鏈
- 無線天線最大增益 2.4 GHz - 2 dBi，5 GHz - 4 dBi
- 天線波束寬度 360°
- LTE 類別 6（300Mbit/s 下行，50Mbit/s 上行）
- LTE 調變解調器 FG621-EA
- TAC 86335904
- MIMO DL 2x2
- MIMO UL 1x1
- LTE FDD 頻段 1（2100MHz）/ 3（1800MHz）/ 5（850MHz）/ 7（2600MHz）/ 8（900 MHz）/ 20（800MHz）/ 28（700MHz）
- 3G 類別 R8（42.2Mbps 下行，11.2Mbps 上行）
- 3G 頻段 1（2100MHz）/ 3（1800MHz）/ 5（850MHz）/ 8（900MHz）
- 尺寸 240 x 156 x 44 mm
- 作業系統 RouterOS v7，許可證級別 4
- 工作溫度 -40°C 至 +70°C

## 安裝 {#mounting}

本裝置設計用於室內使用，可放置在桌面上。

您應使用 CAT5 遮蔽網線。使用和安裝本裝置時，請注意最大允許暴露（MPE）安全距離，輻射體與您身體之間的最小距離為 20 釐米。

## 供電 {#powering}

本裝置透過介面卡供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）12-28 V DC⎓。最大負載下的功耗可達 13 W，帶附加裝置時為 17 W。

## 配置 {#configuration}

您應經常檢查更新，以獲取 RouterOS 軟體的最新更新，從而確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，熟悉各種可能的功能：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下，來自 Internet 埠的所有訪問都會被阻止）。出於恢復目的，可以讓裝置引導以進行重新安裝，請參閱該章節。

## Mode 按鈕 {#mode-button}

Mode 按鈕位於裝置背面右側（參見 ""）。Mode 按鈕的預設配置為深色模式——關閉所有 LED。該按鈕可在 RouterOS 中配置為執行任何使用者指定的指令碼。

## Sync 按鈕 {#sync-button}

Sync 按鈕位於裝置頂部。如果在無線介面上進行了配置，WPS Sync 按鈕可用於連線新用戶端。

![](/img/c76f6511aa4e14f0.webp)

- 按住 WPS 按鈕 1 – 5 秒，即可為無線介面啟用 WPS。

## 前面板 LED 狀態 {#front-led-status}

![](/img/9ba5b3e5c27a0830.webp)

- 無線網路活動。
- 乙太網埠活動。
- 系統 LED。
- 訊號強度。蜂窩連線技術取決於系統 LED 的顏色：紅色：GSM 黃色：3G 藍色：LTE 綠色：5G NSA 紫色：5G SA

當 LTE 未連線到網路時，系統 LED 將閃爍紅色，表示 LTE 連線存在問題。如果 LTE 介面被有意停用（未使用），系統 LED 將呈藍色常亮。

## SIM 卡槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議配合轉接卡使用。

## Reset 按鈕 {#reset-button}

Reset 按鈕有三種功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（總共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置隨後將查詢 CAPsMAN 伺服器（總共 10 秒）。
- 要使用 Netinstall 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種載入程式可用：常規載入程式和備份載入程式。常規載入程式——為裝置通電，等待 1-2 秒，然後按下並按住 Reset 按鈕。等待系統 LED 閃爍綠色，然後變為常亮 "On"。當綠色 LED 變為 "Off" 時，鬆開 Reset 按鈕——裝置將進入 BOOTP 模式。
- 備份載入程式——關閉裝置電源，按下並按住 Reset 按鈕，然後為裝置通電。等待系統 LED 閃爍綠色，然後變為常亮 "On"。當綠色 LED 變為 "Off" 時，鬆開 Reset 按鈕——裝置將使用備份載入程式進入 BOOTP 模式。無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

Netinstall執行 Netinstall 時，請確保 RouterOS 使用最新的 v7 版本。將您的 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

- 歐盟/美國開關電源 24 V ⎓，1.2 A。
- CAT5E UTP 扁平網線，8P8C，AWG32，1.5m，黑色

## 天線使用 {#antenna-usage}

SMA 接頭用於 LTE 天線。

外接天線插孔位於裝置背面。裝置附帶已連線的無線天線，包裝中不提供 LTE 天線。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置點。請了解您所在地區將裝置妥善運輸至指定處置點的相關程式。
