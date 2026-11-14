---
title: "PowerBox Pro"
slug: /powerbox-pro
source: https://manual.mikrotik.com/hardware/powerbox-pro
captured_at: '2026-11-04T06:02:47+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/33cb1622c05d1793.jpg" alt="" width={799} height={617} /></p>

## [PowerBox Pro](https://mikrotik.com/product/RB960PGS-PB) (RB960PGS-PB) {#powerbox-pro-rb960pgs-pb}

PowerBox Pro 是一款室外裝置，具有五個千兆乙太網埠，並在埠 2-5 上提供 PoE 電源輸出（每埠最大 1 A，總計最大 2 A）。完整規格和宣傳冊請參見 [PowerBox Pro 產品頁面](https://mikrotik.com/product/RB960PGS-PB)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計為在戶外立杆上安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險情況並損壞系統。
- 請僅使用製造商認可的電源和附件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將 WAN 線纜連線到埠 1，並將其他裝置連線到埠 2-5；
- 將裝置連線到電源；
- 將網路卡設定為透過 DHCP 自動獲取 IP 地址；
- 應使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 設定路由器密碼。

## 供電 {#powering}

本裝置在不連線附件時的功耗為 6 W，最大功耗為 54 W。裝置可透過電源插孔或第一個乙太網埠（被動 PoE）供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 12-57 V DC。
- ether1 埠接受 12-57 V DC 的被動 PoE 輸入。

## 安裝 {#mounting}

可以使用隨附的 DIN 導軌支架和螺釘將裝置安裝到 DIN 導軌上。由於裝置具有防風雨的戶外外殼，您可以使用隨附的兩根紮帶或鋼製卡箍將其安裝在立杆上。接地線需要連線到裝置背面專門設計的螺釘上。

<p><Img src="/img/6e287d9e7e2efacf.webp" alt="" width={300} height={488} /></p>

請確保安裝裝置時乙太網埠朝下。

## 配置 {#configuration}

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議先閱讀 [RouterOS 文件](https://mt.lv/help) 以熟悉各項功能。如果無法建立 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參見復位按鈕。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個 10/100/1000 千兆乙太網埠。
- 一個 SFP 埠。

## 電源輸出 {#power-output}

裝置支援被動或標準 802.3at/af PoE 輸入/輸出。乙太網埠 2-5 可以使用與裝置相同的電壓為其他支援 PoE 的裝置供電。需要操心的電源介面卡和線纜更少！如果使用 48-57 V 輸入電壓，它可以為相容 af/at mode B (4,5+)(7,8-) 的裝置供電。每埠最大輸出為 1 A，使用 12-30 V 輸入電壓時總計 2 A。使用 31-57 V 輸入電壓時，每埠功率限制為 450 mA。在 RouterOS 中啟用電源輸出後，乙太網 LED 會額外顯示紅色（綠色表示乙太網鏈路已建立，紅色表示有電源但無鏈路，紅色和綠色同時亮表示既有鏈路又有電源）。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 或者繼續按住按鈕 5 秒以上，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器。

無論使用上述哪種方式，如果在裝置加電前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 規格 {#specifications}

- CPU 標稱頻率：800 MHz。
- RAM 容量：128 MB。
- 儲存：16 MB。
- 10/100/1000 乙太網埠：5。
- SFP 埠：1。
- 交換晶片型號：QCA8337。
- 尺寸：125 x 52 x 225 mm。
- 工作溫度：經測試為 -40°C 至 +70°C。

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/RB960PGS-PB](https://mikrotik.com/product/RB960PGS-PB)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

<p><Img src="/img/1891b912b88a23b9.webp" alt="" width={720} height={201} /></p>

## 安全提示 {#safety-notice}

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場所。請了解將裝置正確運送到您所在地區指定處置場所的相關程式。

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期的資訊以斜槓分隔的形式標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），後面兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## Norma Oficial Mexicana {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置不得造成有害干擾；且
- 本裝置必須接受任何干擾，包括可能導致其非預期操作的干擾。

製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039，拉脫維亞。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
