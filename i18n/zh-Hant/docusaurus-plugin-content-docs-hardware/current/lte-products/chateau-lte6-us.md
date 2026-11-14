---
title: "Chateau LTE6-US"
slug: /chateau-lte6-us
source: https://manual.mikrotik.com/hardware/chateau-lte6-us
captured_at: '2026-11-04T09:45:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/da26ad150e7e6e72.jpg)

## [Chateau LTE6-US](https://mikrotik.com/product/chateau_lte6_us) (D53G-5HacD2HnD-TC&EG06-A) {#chateau-lte6-us-d53g-5hacd2hnd-tceg06-a}

經美國運營商認證（AT&T、T-Mobile）的家庭接入點，支援 LTE6，速度最高可達 300 Mbps。它配備 5 個千兆乙太網埠、強勁的四核 CPU 以及令人耳目一新的雅緻設計，是大多數家庭的正確選擇。完整規格與手冊請參閱 [Chateau LTE6-US 產品頁面](https://mikrotik.com/product/chateau_lte6_us)。

Chateau 是一款配合蜂窩網路運營商 SIM 卡使用的家用路由器。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終廢棄處理應遵守所有國家法律法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品僅供室內安裝使用。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

按照以下快速步驟設定您的裝置：

![](/img/cbc5361d4144eab4.webp)

- 將計算機連線到其中一個乙太網埠；
- 可選 — 將外接天線連線到 SMA 接頭（包裝中不提供天線，請參見“（連結）”）；
- 將 micro SIM 卡插入裝置底部的卡槽；

![](/img/9619076cdc698366.webp)

- 將電源介面卡連線到 DC 插孔；
- 裝置通電且 PC 已連線到裝置後，在網頁瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始配置；
- 使用者名稱：a*dmin*，預設沒有密碼，您將自動登入到 Quick Set 介面（對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 您應點選右側的“Check for updates”按鈕，將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性，必須插入有效的 SIM 卡；
- 要手動更新裝置，請訪問 [https://mikrotik.com/download](https://mikrotik.com/download)
- 為此裝置選擇 ARM 軟體包並將其下載到您的 PC。
- 將下載的軟體包上傳到 WebFig 的“Files”選單，然後重啟裝置。
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新。
- 要個性化您的無線網路，可在“Network Name”欄位中更改 SSID；
- 在螢幕左側的“Country”欄位中選擇您所在的國家/地區，以應用該國法規設定；
- 在“WiFi Password”欄位中設定無線網路密碼，密碼至少需要八個字元；
- 在底部右側的“Password”欄位中設定路由器密碼，並在“Confirm Password”欄位中重複輸入，該密碼將在下次登入時使用；
- 選擇“Apply Configuration”儲存更改。

## 使用移動應用連線 {#connecting-with-a-mobile-app}

使用智慧手機透過 WiFi 訪問路由器。

![](/img/9bcba09a7b6a0d53.webp)

- 插入 SIM 卡併為裝置通電。
- 用智慧手機掃描二維條碼，並選擇您偏好的作業系統。
- 連線到無線網路。SSID 以 MikroTik 開頭，幷包含裝置 MAC 地址的最後幾位數字。
- 開啟應用程式。
- 預設情況下，IP 地址和使用者名稱已經填好。
- 選擇 Connect，透過無線網路與裝置建立連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 還提供高階選單，可完整配置所有必要設定。

## 規格 {#specifications}

- 產品程式碼 D53G-5HacD2HnD-TC&EG06-A
- CPU IPQ-4019 488-896 MHz 自動
- CPU 架構 ARM 32bit
- CPU 核心數 4
- RAM 大小 256 MB
- RAM 型別 DDR3L
- 儲存 16 MB，Flash
- 1G 乙太網埠數量 5
- USB 1 個 USB 2.0 A 型埠
- 交換晶片型號 IPQ-4019
- 無線 2.4 GHz 802.11b/g/n 雙鏈，5 GHz 802.11a/n/ac 雙鏈
- 無線天線最大增益 2.4 GHz（3 dBi），5 GHz（5.5 dBi）
- 天線波束寬度 360°
- LTE 類別 6（下行 300Mbit/s，上行 50Mbit/s）
- LTE 調變解調器 EG06-A
- TAC 01619900
- LTE FDD 頻段 2 (1900MHz) / 4 (1700MHz) / 5 (850MHz) / 7 (2600MHz) / 12 (700MHz) / 13 (700 MHz) / 25 (1900MHz) / 26 (850MHz) / 29 (700 MHz) / 30 (2300 MHz) / 66 (1700MHz)
- 3G 類別 R8（下行 42.2Mbps，上行 5.76Mbps）
- 3G 頻段 2 (1900MHz) / 5 (850MHz)
- 尺寸 240 x 156 x 44 mm
- 作業系統 RouterOS，許可證級別 4
- 工作溫度 -40°C 至 +70°C

## 安裝 {#mounting}

本裝置為室內使用而設計，放置在桌面上即可。

您應使用 CAT5 遮蔽線纜。使用和安裝本裝置時，請注意最大允許暴露量（MPE）安全距離，即輻射體與您身體之間至少保持 20 釐米。

## 供電 {#powering}

裝置透過介面卡供電：

- 直流輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）12-28 V DC⎓。最大負載下的功耗可達 14.3 W，連線附件時為 19 W。

## 配置 {#configuration}

您應頻繁檢查更新，以獲取 RouterOS 軟體的最新更新，確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以引導裝置進行重灌，請參見相應章節。

## Mode 按鈕 {#mode-button}

Mode 按鈕位於裝置背面右側（參見“”）。Mode 按鈕的預設配置為暗色模式 - 關閉所有 LED。可以在 RouterOS 中配置該按鈕以執行任何使用者指定的指令碼。

## Sync 按鈕 {#sync-button}

Sync 按鈕位於裝置頂部。如果已在無線介面上配置 WPS Sync 按鈕，它可用於連線新用戶端。

![](/img/c76f6511aa4e14f0.webp)

- 按住 WPS 按鈕 1 – 5 秒，可為無線介面啟用 WPS。

## 前面板 LED 狀態 {#front-led-status}

![](/img/9ba5b3e5c27a0830.webp)

- 無線網路活動。
- 乙太網埠活動。
- 系統 LED。
- 訊號強度。蜂窩連線技術由系統 LED 的顏色表示：紅色：GSM 黃色：3G 藍色：LTE 綠色：5G NSA 紫羅蘭色：5G SA

當 LTE 未連線到網路時，系統 LED 將閃爍紅色，表示 LTE 連線存在問題。如果 LTE 介面被有意停用（未使用），系統 LED 將亮藍色。

## SIM 卡槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡的厚度不同，不建議配合轉接卡使用。

## Reset 按鈕 {#reset-button}

Reset 按鈕有三個功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置將開始查詢 CAPsMAN 伺服器（共 10 秒）。
- 要使用 Netinstall 工具重灌 RouterOS，請讓裝置進入 BOOTP 模式。有兩種引導器可用：常規引導器和備份引導器。常規引導器 - 給裝置上電，等待 1-2 秒，然後按住 Reset 按鈕。等到系統 LED 閃爍綠色，然後變為常亮“On”。當綠色 LED 變為“Off”時，鬆開 Reset 按鈕 - 裝置將進入 BOOTP 模式。
- 備份引導器 – 關閉裝置電源，按住 Reset 按鈕，然後給裝置上電。等到系統 LED 閃爍綠色，然後變為常亮“On”。當綠色 LED 變為“Off”時，鬆開 Reset 按鈕 - 裝置將使用備份引導器進入 BOOTP 模式。無論使用上述哪種方式，如果在裝置上電之前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這適用於 RouterBOOT 偵錯和恢復。

Netinstall執行 Netinstall 時，請確保 ROS 檔案和 Netinstall 軟體均使用最新的 v7 版本。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的附件：

- EU/US 開關電源 24 V ⎓，1.2 A，28.8 W，86.8 %，VI，線纜：150 cm。
- CAT5E UTP 扁平線纜，8P8C，AWG32，1.5 m，白色。

## LTE 天線使用 {#lte-antenna-usage}

裝置背面蓋板後有兩個外接天線接頭。

- 向上拉動蓋板將其開啟。
- 將 LTE 天線擰到左側的 SMA 接頭上。天線接頭或所用任何其他轉接頭的最大直徑為 13 mm。

![](/img/b70ac6f60339b714.webp)

使用一根天線時，請連線到左側的 SMA 接頭（ANT1）。只有使用兩根天線時，才可以連線到右側的 SMA 接頭（ANT4）。

![](/img/d3359d36ecb577c0.webp)

請在裝置關閉時連線和斷開天線！裝置上的 SMA 接頭為母頭。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統未經測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢棄物處置場所。請熟悉您所在地區將裝置正確運輸至指定處置場所的相關程式。

### 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th><th>包含的 FCC ID</th></tr></thead><tbody><tr><td>D53G-5HacD2HnD-TC&EG06-A</td><td>TV7D53G-5ACD2ND</td><td>XMR201807EG06A</td></tr></tbody></table>

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝環境中的有害干擾提供合理防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），建議使用者嘗試透過以下一項或多項措施來消除干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以獲取幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者操作本裝置的許可權失效。

本裝置符合 FCC 規則第 15 部分。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受所接收到的任何干擾，包括可能導致意外執行的干擾。

注意：本裝置已在周邊裝置使用遮蔽線纜的情況下進行測試。必須使用遮蔽線纜連線本裝置以確保合規。

<table><thead><tr><th>**技術規格**</th><th></th><th></th><th></th></tr></thead><tbody><tr><td>產品電源輸入選項</td><td>DC 介面卡輸出規格，(V/A)</td><td>外殼 IP 等級</td><td>工作溫度</td></tr><tr><td>DC 插孔 12-28 V</td><td>24 V / 1.2</td><td>IP20</td><td>0°..+70°C</td></tr></tbody></table>
