---
title: "LtAP LR8 LTE6 套件"
slug: /ltap-lr8-lte6-kit
source: https://manual.mikrotik.com/hardware/ltap-lr8-lte6-kit
captured_at: '2026-11-04T09:55:43+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可下載為 <a href="/assets/files/ltap-lr8-lte6-kit-71d41280de7103b44c39d02f829e279a.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/30e4f8523c74a8b6.jpg)

### [LtAP LR8 LTE6 kit](https://mikrotik.com/product/ltap_lr8g_lte6_kit)（LtAP-2HnD&FG621-EA&LR8） {#ltap-lr8-lte6-kit-ltap-2hndfg621-ealr8}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律法規進行處理。
- 在任何牆面安裝接入點的所有安裝方法均須獲得當地管轄部門的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於在室外立杆上安裝，但也可在室內安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險情況並損壞系統。
- 請僅使用製造商認可的電源和配件，這些均可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地的法規，包括在法律允許的頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。
- 這是 A 類裝置。在家庭環境中，本產品可能會造成無線電干擾，此時使用者可能需要採取適當的措施。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置應與您的身體、職業使用者或公眾保持不小於 30 釐米的距離。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

- 開啟底部蓋板；
- 將 Mini SIM 卡插入卡槽；
- 將裝置連線到電源；
- 在您計算機上進入網路連線部分，找到名為 "MikroTik-..." 的無線網路，然後連線到它（請檢視貼紙上的無線密碼）；
- 應透過移動應用程式經由無線網路進行配置，或者您可以使用 "WinBox" 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)。下載並開啟 "WinBox"，選擇 "Neighbors" 標籤頁以查詢裝置；
- 點選 MAC 地址。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 找到您的產品。所需的軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 "WinBox" 的 "Files" 選單並重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保獲得最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您的國家/地區，以應用國家/地區法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼；
- 在產品內的標籤上找到您的 LR Gateway ID，並在您的網路伺服器中註冊它。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/7b3321c1cbf665d8.webp)

- 內建 2 GHz 無線接入點模組，支援 AP/station/bridge/p2p 模式。板載內建 PIF 天線，以及用於外接天線的 MMCX 聯結器（可透過軟體選擇）。
- 兩個 miniPCIe 插槽和三個 SIM 卡槽。
- 內建 GPS 模組，配有外部 SMA 聯結器。
- 千兆乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。直通線或交叉線均可用於連線其他網路裝置。乙太網埠可透過無源 PoE 注入器接受 12-30 V DC 供電。
- 一個 DB9 RS232 序列埠，用於序列控制檯訪問。配置為 115200 bit/s、8 個數據位、1 個停止位、無校驗。
- 一個 USB 2.0 埠。
- R11e-LR8，帶有外部 SMA 聯結器的 miniPCIe 卡。

## 安裝 {#mounting}

- 可以使用隨附的四顆螺絲和機身上的四個孔將裝置固定在牆上。
- 埠由一個小門保護，該門由兩顆螺絲固定。取下它即可訪問乙太網埠、天線聯結器、SIM 卡槽等。
- 該門為所有可用埠留有開口，因此您可以引出所有必要的線纜，但請只打開始終要使用的開口。
- 機殼上提供了多個用於外接天線的位置，請使用合適尺寸的鑽頭將其開啟。請小心並測量所選天線，以確保安裝後不會碰到內部 PCB 板。

![](/img/dc0a3d4ff60b80cb.webp)

該裝置既可在室內也可在室外使用。IP 防護等級為 IP54。

如果您打算在室外安裝，請確保任何線纜開口都朝下。安裝方向由裝置上指向上的箭頭指示。請使用 PoE 注入器和正確的接地。建議使用 Cat6 遮蔽電纜。警告！本裝置的安裝和操作應與您的身體保持至少 30 釐米的距離。在住宅環境中操作本裝置可能會造成無線電干擾。裝置外殼上留有可鑽孔的位置，用於外接 LTE 和 GPS 天線。請使用鑽頭鑽出與所用天線線纜相匹配的孔。

## 配置 {#configuration}

我們建議點選 "Check for updates" 按鈕並將您的 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法進行 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下從網際網路埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參閱該章節（連結）第 4 部分；- 有關如何放置橡膠密封圈以實現最佳防水保護的參考，請參閱下圖；

- 重新裝配時請注意順序。PCB 螺絲的擰緊力矩為 0.3 Nm，機殼蓋/外殼螺絲為 0.5 Nm。

![](/img/03bc306812c7acce.webp)

在您將裝置重新裝入機殼並用先前拆下的螺絲固定之後，請將移動運營商的 SIM 卡滑入 SIM 卡槽，晶片朝向如埠標籤所示。該卡槽接受 miniSIM（2FF）。SIM 卡槽 2 和 3 適用於底部 miniPCIe 插槽，可在 RouterOS 的 "/system routerboard sim" 選單中切換。

## 復位按鈕 {#reset-button}

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可復位 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAP 模式。裝置現在將尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝內包含隨裝置提供的配件：

- K-67 緊韌體套裝。包含四顆 4x25 mm 螺絲、四個 6x30 mm 膨脹螺栓。
- DC ⎓ 電纜（H4130-04PDB000R 3 mm 2x2P Housing）轉（StripJacket 5 cm+WireEnd Strip/Tin 1 cm）24 AWG（黑/紅/藍/橙）0.35 m。
- EU/US 開關電源 24 V、1.2 A、28.8 W、86.8%、VI，DC ⎓ 電纜：220 cm RA DC plug mod Hor CMC 短插頭。

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您偏好的作業系統。
- 安裝並開啟應用程式。
- 預設情況下，IP 地址和使用者名稱將已填寫。
- 點選 Connect 以透過無線網路建立與裝置的連線。
- 選擇 Quick setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢物處置場所。請了解您所在地區將裝置正確運往指定處置場所的相關程式。
