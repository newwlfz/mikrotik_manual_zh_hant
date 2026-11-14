---
title: "Chateau LTE6"
slug: /chateau-lte6
source: https://manual.mikrotik.com/hardware/chateau-lte6
captured_at: '2026-11-04T09:45:29+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/da26ad150e7e6e72.jpg)

## [Chateau LTE6](https://mikrotik.com/product/chateau_lte6) (D53G-5HacD2HnD-TC&FG621-EA) {#chateau-lte6-d53g-5hacd2hnd-tcfg621-ea}

Chateau 是一款家用路由器，用於配合蜂窩網路運營商的 SIM 卡使用。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是從電源插座中拔出電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

![](/img/cbc5361d4144eab4.webp)

- 將您的計算機連線到其中一個乙太網埠；
- 可選 - 將外接天線連線到 SMA 聯結器（包裝中不提供天線，請參閱 "(連結) 瞭解 Micro SIM 卡。
- 模式按鈕。
- 外接（連結）的蓋板
- WPS（連結）
- 整合無線模組，工作在 2.4 GHz，802.11b/g/n 協定。
- 整合無線模組，工作在 5 GHz，802.11a/n/ac 協定。

## 安裝 {#mounting}

本裝置設計用於室內，可放置在桌面上使用。

應使用 CAT5 遮蔽網線。使用和安裝本裝置時，請注意最大允許暴露量（MPE）安全距離，輻射體與人體之間至少保持 20 cm 的距離。

## 供電 {#powering}

本裝置透過介面卡供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）12-28 V DC⎓。最大負載下的功耗可達 15 W，帶附件時 21 W。

## 配置 {#configuration}

您應經常檢查更新，以獲取 RouterOS 軟體的最新更新，從而確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉這些功能：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以讓裝置進入引導以進行重新安裝，請參閱相應章節。

## 模式按鈕 {#mode-button}

模式按鈕位於裝置背面右側（見 ""）。模式按鈕的預設配置為暗色模式 - 關閉所有 LED。該按鈕可在 RouterOS 中配置為執行任意使用者指定的指令碼。

## 同步按鈕 {#sync-button}

同步按鈕位於裝置頂部。如果在無線介面上配置了 WPS 同步按鈕，則可用於連線新用戶端。

![](/img/c76f6511aa4e14f0.webp)

- 按住 WPS 按鈕 1 – 5 秒，為無線介面啟用 WPS。

## 前面板 LED 狀態 {#front-led-status}

![](/img/9ba5b3e5c27a0830.webp)

- 無線網路活動。
- 乙太網埠活動。
- 系統 LED，具有用於指示蜂窩調變解調器狀態的替代模式。
- 訊號強度。

## 系統 LED 替代調變解調器模式指示 {#system-led-alternate-modem-mode-indications}

啟用蜂窩調變解調器介面後，系統 LED 具有替代指示：

紅色閃爍 - 未插入 SIM 卡

黃色 - 在 3G 模式下已建立連線

藍色 - 在 LTE 模式下已建立連線

閃爍 - 正在建立連線，調變解調器已註冊到蜂窩網路，APN 尚未啟用

## SIM 卡槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議配合轉接卡使用。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動期間按住此按鈕，直到綠色 LED 開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在會尋找 CAPsMAN 伺服器（共 10 秒）。
- 要使用 Netinstall 工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。可用的引導器有兩種：常規引導器和備用引導器。常規引導器 - 給裝置上電，等待 1-2 秒，然後按住復位按鈕。等待系統 LED 綠色閃爍，然後變為常亮 "On"。當綠色 LED 變為 "Off" 時，鬆開復位按鈕 - 裝置將進入 BOOTP 模式。
- 備用引導器 – 關閉裝置電源，按住復位按鈕，然後給裝置上電。等待系統 LED 綠色閃爍，然後常亮 "On"。當綠色 LED 變為 "Off" 時，鬆開復位按鈕 - 裝置將使用備用引導器進入 BOOTP 模式。無論使用上述哪種選項，如果在給裝置上電之前按下按鈕，系統都將載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復非常有用。

Netinstall執行 Netinstall 時，請確保 ROS 檔案和 Netinstall 軟體均使用最新的 v7 版本。

## 配件 {#accessories}

包裝中隨裝置附帶以下附件：

- 歐盟/美國開關電源 24 V ⎓，1.2 A，28.8 W，86.8 %，VI，線纜：150 cm。
- CAT5E UTP 扁平網線，8P8C，AWG32，1.5 m。

## LTE 天線使用 {#lte-antenna-usage}

SMA 聯結器用於 LTE 天線。

裝置背面門蓋後方有兩個外接天線聯結器。

- 向上拉動門蓋將其開啟。
- 將 LTE 天線擰到左側的 SMA 聯結器上。天線聯結器或所用其他轉接頭的最大直徑為 13 mm。

![](/img/b70ac6f60339b714.webp)

使用一根天線時，請連線到左側的 SMA 聯結器（ANT1）。僅在使用兩根天線時，才可以連線到右側的 SMA 聯結器（ANT4）。

![](/img/d3359d36ecb577c0.webp)

請在裝置關閉時連線和斷開天線！裝置上的 SMA 聯結器為母頭。

您應使用我們的天線 [https://mikrotik.com/product/mant_lte_5o](https://mikrotik.com/product/mant_lte_5o)

## 拆下前蓋以接觸 PCB {#removing-front-cover-to-access-pcb}

如果需要接觸 PCB，可以拆下前蓋。

- 取下中央螺絲；

![](/img/3c40f644b6453592.webp)

- 用小螺絲刀在標記位置撬開蓋子；
- 繼續向上撬開；

![](/img/ef5c2817560d190a.webp)

- 最後將整個蓋子取下。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢棄物處置場。請了解將裝置正確運送至您所在地區指定處置場的相關程式。
