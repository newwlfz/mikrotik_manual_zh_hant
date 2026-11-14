---
title: "LtAP LR8G LTE6 套件"
slug: /ltap-lr8g-lte6-kit
source: https://manual.mikrotik.com/hardware/ltap-lr8g-lte6-kit
captured_at: '2026-11-04T09:55:39+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可作為 <a href="/assets/files/ltap-lr8g-lte6-kit-23522edeb754bc391b59ac9013a88060.pdf" target="_blank" rel="noopener">PDF 檔案</a> 下載。

![](/img/30e4f8523c74a8b6.jpg)

### [LtAP LR8G LTE6 套件](https://mikrotik.com/product/ltap_lr8g_lte6_kit)（LtAP-2HnD&FG621-EA&LR8G） {#ltap-lr8g-lte6-kit-ltap-2hndfg621-ealr8g}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。完整規格和手冊請參見 [LtAP LR8G LTE6 kit 產品頁面](https://mikrotik.com/product/ltap_lr8g_lte6_kit)。
- 本產品的最終處置應遵循所有國家法律和法規。
- 在任何牆面上安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於戶外安裝在立杆上，但也可在室內安裝。開始安裝之前，請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險情況並對系統造成損壞。
- 僅使用製造商認可的電源和配件，這些均可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置出現故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。
- 這是 A 類裝置。在居住環境中，本產品可能造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和操作時，與您的身體、職業使用者或普通公眾的距離不得小於 30 釐米。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 開啟底部蓋板；
- 將 Mini SIM 卡插入卡槽；
- 將裝置連線到電源；
- 在計算機上進入網路連線部分，找到名為 "MikroTik-..." 的無線網路。繼續連線該網路（請檢視標籤上的無線密碼）；
- 配置應透過無線網路使用移動應用程式進行，或者您可以使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。下載並開啟 "WinBox"，選擇 "Neighbors" 標籤頁以查詢裝置；
- 單擊 MAC 地址。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視標籤上的使用者名稱和無線密碼）；
- 如需手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 找到您的產品。所需的軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 "WinBox" 的 "Files" 選單並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您的國家/地區，以應用國家法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼；
- 在產品內的標籤上找到您的 LR Gateway ID，並將其註冊到您的網路伺服器中。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/7b3321c1cbf665d8.webp)

- 內建 2 GHz 無線接入點模組，支援 AP/station/bridge/p2p 模式。板載內建 PIF 天線，以及用於外接天線的 MMCX 聯結器（可透過軟體選擇）。
- 兩個 miniPCIe 插槽和三個 SIM 插槽。第一個插槽（底部）由 LTE 調變解調器使用，其連線到內部 LTE 天線。第二個插槽（上部）由 R11e-LR8G 卡使用，其連線到外部 SMA 聯結器
- 內建 GPS 模組，帶外部 SMA 聯結器。
- 千兆乙太網埠，支援自動交叉/直通電纜校正（Auto MDI/X）。直通或交叉電纜均可用於連線其他網路裝置。乙太網埠接受來自無源 PoE 注入器的 12-30 V DC 供電。
- 一個 DB9 RS232 序列埠，用於序列控制檯訪問。配置為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。
- 一個 USB 2.0 埠。

## 安裝 {#mounting}

- 可以使用隨附的四顆螺絲和機組上設計的四個孔，將裝置固定到牆上。
- 埠由一個小門保護，該門用兩顆螺絲固定。取下它即可訪問乙太網埠、天線聯結器、SIM 插槽等。
- 該門上為所有可用埠預留了開口位置，因此您可以穿過所有必要的線纜，但請只敲開您將要使用的開口。
- 機殼上提供了若干外接天線位置，請使用合適尺寸的鑽頭將其開孔。注意測量所選天線，以免安裝時碰到內部 PCB 板。

![](/img/dc0a3d4ff60b80cb.webp)

該裝置可在室內和室外使用。IP 防護等級為 IP54。

如果您打算在戶外安裝，請確保所有線纜開口朝下。安裝方向由裝置上指向上的箭頭指示。請使用 POE 注入器和適當的接地。建議使用 Cat6 遮蔽電纜。警告！本裝置的安裝和操作應與裝置與您的身體之間保持至少 30 釐米的距離。在居住環境中操作本裝置可能造成無線電干擾。裝置外殼上留有可為外接 LTE 和 GPS 天線鑽孔的位置。請使用鑽頭鑽出適合所用天線電纜的孔。

## 配置 {#configuration}

我們建議單擊 "Check for updates" 按鈕並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問都被阻止）。出於恢復目的，可以從網路引導裝置，請參見（連結）部分的第 4 部分；- 如何放置橡膠密封圈以獲得最佳防水保護，請參考下圖；

- 重新組裝時請注意復原。PCB 螺絲的擰緊力矩為 0.3 Nm，機殼蓋/外殼螺絲為 0.5 Nm。

![](/img/03bc306812c7acce.webp)

在您將裝置重新裝入機殼並用先前拆下的螺絲固定後，請將從移動運營商處獲得的 SIM 卡滑入 SIM 插槽，晶片朝向如埠標籤所示。該插槽接受 miniSIM（2FF）。SIM 插槽 2 和 3 適用於底部 miniPCIe 插槽，可在 RouterOS 的 "/system routerboard sim" 選單中切換。

## 復位按鈕 {#reset-button}

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在將查詢 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器（共 15 秒）。無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的配件：

- K-67 緊固套件。包括四顆 4x25 mm 螺絲、四個 6x30 mm 膨脹螺栓。
- 直流 ⎓ 電纜（H4130-04PDB000R 3 mm 2x2P 外殼）至（StripJacket 5 cm+WireEnd Strip/Tin 1 cm）24 AWG（黑/紅/藍/橙）0.35 m。
- 歐盟/美國開關電源 24 V，1.2 A，28.8 W，86.8%，VI，直流 ⎓ 電纜：220 cm RA DC 插頭 mod Hor CMC 短插頭。

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱將已填寫。
- 單擊 Connect 透過無線網路建立與您裝置的連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢物處置場所。請熟悉將裝置正確運輸到您所在地區指定處置場所的程式。
