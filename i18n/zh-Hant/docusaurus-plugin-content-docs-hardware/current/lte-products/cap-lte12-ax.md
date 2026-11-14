---
title: "cAP LTE12 ax"
slug: /cap-lte12-ax
source: https://manual.mikrotik.com/hardware/cap-lte12-ax
captured_at: '2026-11-04T09:41:03+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/af6e9153d09f5342.jpg)

## [cAP LTE12 ax](https://mikrotik.com/product/cap_lte12_ax)（cAPGi-5HaxD2HaxD&EG12-EA） {#cap-lte12-ax-capgi-5haxd2haxdeg12-ea}

一款功能強大的吸頂式接入點，可為您的臨時業務提供真正的 Wi-Fi 6 移動性 —— 現在配備 CAT12 LTE 調變解調器！完整規格和宣傳冊請參見 [cAP LTE12 ax 產品頁面](https://mikrotik.com/product/cap_lte12_ax)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終廢棄處理應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品僅供室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和配件，它們可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行時應與您的身體、職業使用者或公眾保持不少於 30 釐米的距離。

## 快速開始 {#quickstart}

按照以下快速步驟設定您的裝置：

- 將 micro SIM 卡插入卡槽；
- IMEI 號可在機殼和包裝標籤上找到；
- 用乙太網線將裝置連線到隨附的 PoE 注入器的 *"data+power"* 端；
- 透過任一乙太網埠或無線網路 "MikroTik-..." 連線到裝置（請務必檢視貼紙上的無線密碼）；
- 使用移動應用程式建立連線。或者，在網頁瀏覽器中使用 WebFig，或使用位於 [https://mt.lv/winbox](https://mt.lv/winbox) 的 "WinBox" 配置工具。在所選工具中使用預設 IP 地址 192.168.88.1 開始配置。如果該 IP 地址不可用，請使用 WinBox 並選擇 "Neighbors" 標籤頁來查詢裝置；
- 繼續使用 MAC 地址進行連線。使用者名稱為 "admin"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 選擇 "Check for updates" 按鈕，將 RouterOS 更新到最新版本。必須插入有效的 SIM 卡並具有可用的 Internet 連線；
- 如需手動更新裝置，請訪問 [https://mikrotik.com/products](https://mikrotik.com/products) 的產品頁面找到您的產品。所需的軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 WebFig 或 WinBox 的 "Files" 選單，然後重啟裝置；
- 透過將 RouterOS 軟體升級到最新版本，您可以確保最佳效能、穩定性和安全更新；
- 在 "QuickSet" 選單中設定以下內容：選擇您所在的國家/地區，以應用該國家/地區的法規設定；
- 在左側欄位中設定您的無線網路密碼；
- 在底部欄位中設定您的路由器密碼。

## 供電 {#powering}

- DC 輸入數量：2（DC 插孔、PoE-IN）；
- 支援的輸入電壓 18-57 V（DC 插孔）18-57（PoE-In）
- PoE-in 802.3af/at：Ether1；
- PoE-Out 無源 PoE 最高 57V（&lt;30v DC 插孔必須使用，&gt;30V 可使用 PoE-In 和 DC 插孔）
- PoE-Out 埠：Ether2，每埠最大輸出（輸入 &lt; 30 V）：0.6 A，每埠最大輸出（輸入 &gt; 30 V）：0.4 A。電流超過 0.3 A 時，請使用 DC 插孔為裝置供電。
- 最大功耗（不含配件）13 W
- 最大功耗 34 W

## 安裝 {#mounting}

可以使用裝置背部的隨附安裝支架將裝置安裝到牆壁或天花板上：

- 用隨附的螺絲將安裝支架固定到牆壁或天花板上；
- 如有必要，使用隨附的膨脹螺柱配合鑽頭；
- 將所需的線纜連線到裝置；
- 透過滑動將裝置安裝到安裝支架上。

![](/img/26dbe3bbb765ae0b.webp)

*本裝置的安裝和配置應由合格人員完成。* 警告！本裝置的安裝和執行時應與您的身體保持至少 30 釐米的距離。在住宅環境中執行本裝置可能會造成無線電干擾。

## 配置 {#configuration}

預設情況下，裝置被配置為無線接入點，LTE 介面作為 WAN，Ether1、Ether2 介面與無線介面橋接在一起。橋接介面上配置了 DHCP 伺服器。登入後，您應在 QuickSet 選單中選擇 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將要使用的國家/地區，以符合當地法規。必須插入有效的 SIM 卡並具有可用的 Internet 連線。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下所有來自 Internet 埠的訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參閱相關章節。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 產品程式碼：cAPGi-5HaxD2HaxD&EG12-EA
- CPU：四核 IPQ-6010 1.8 GHz
- RAM 大小：1 GB
- RAM 型別：DDR3L
- 儲存：128 MB，NAND
- 1G 乙太網埠數量：2
- 交換晶片型號：IPQ-6010
- 無線介面型號：QCN-5022（2.4 GHz）、QCN-5052（5 GHz）
- 無線 2.4 GHz 802.11b/g/n/ax 雙鏈，5 GHz 802.11a/n/ac/ax 雙鏈
- 天線增益：5.5 dBi
- 3G 類別：R8（下行 42.2Mbps，上行 11.2Mbps）
- 3G 頻段：1（2100MHz）/ 3（1800MHz）/ 5（850MHz）/ 8（900MHz）
- LTE 類別：12（下行 600Mbps，上行 150Mbps）
- LTE 調變解調器：EG12-EA
- LTE FDD 頻段：1（2100MHz）/ 3（1800MHz）/ 5（850MHz）/ 7（2600MHz）/ 8（900 MHz）/ 20（800MHz）/ 28（700MHz）
- LTE TDD 頻段：38（2600MHz）/ 40（2300MHz）/ 41（2500MHz）
- TAC：86056104
- SIM 卡槽數量：1 個調變解調器（Micro SIM）
- 作業系統：RouterOS v7，License level 4
- 尺寸：228 x 48 mm
- IP：20
- 工作溫度：經過測試 -40°C 至 +70°C

## 按鈕和跳線 {#buttons-and-jumpers}

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置現在會尋找 CAPsMAN 伺服器（共 10 秒）。
- 或者繼續按住按鈕 5 秒直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（共 15 秒）。無論使用上述哪種方式，如果在裝置通電之前按住按鈕，系統都會載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 模式按鈕 {#mode-button}

![](/img/bd56fb1f06904d9a.webp)

模式按鈕的動作可以在 RouterOS 軟體中配置，以執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。預設情況下，該按鈕會啟用 "dark mode"，即關閉 LED 燈。模式按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列在 /system resource 中。其他作業系統尚未經過測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟該應用程式。
- 預設情況下，IP 地址和使用者名稱已經填好。
- 選擇 Connect，透過無線網路與您的裝置建立連線。
- 選擇 Quick Setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 還提供高階選單，可用於完整配置所有必需的設定。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的配件：

![](/img/5e8f40bb7700ca6e.webp)

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的相關程式。
