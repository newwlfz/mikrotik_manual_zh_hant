---
title: "CRS112-8G-4S-IN"
slug: /crs112-8g-4s-in
source: https://manual.mikrotik.com/hardware/crs112-8g-4s-in
captured_at: '2026-11-04T09:45:59+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/4a31c677eec08155.webp)

## [CRS112-8G-4S-IN](https://mikrotik.com/product/CRS112-8G-4S-IN) {#crs112-8g-4s-in}

本裝置是一臺帶有 8 個千兆乙太網埠和 4 個 SFP 埠的網路交換器。它已經完成配置，所有埠都已交換在一起。該機型相容 1.25G SFP 模組。完整規格和宣傳冊請參見 [CRS112-8G-4S-IN 產品頁面](https://mikrotik.com/product/CRS112-8G-4S-IN)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律和法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本機型用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用不正確的硬體或不遵循正確的操作步驟，可能會給人員帶來危險並損壞系統。
- 本產品適合在室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 請僅使用製造商認可的電源和附件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證不會因不當使用裝置而發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、線纜要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

預設情況下，所有介面都已交換在一起，並且網橋介面具有 IP 192.168.88.1/24。

- 將裝置放置在平整的表面上；
- 將您的 PC 連線到任意乙太網埠；
- 將電源介面卡連線到 DC 插孔；
- 將您的 PC IP 地址設定為 192.168.88.2/24；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 完成。**我們提供多種配置方法以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 若要手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單中，並重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

該板卡可從直流輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）取電，支援 10-57 V ⎓ DC。乙太網埠 1 也支援無源 PoE 電源輸入。本裝置在最大負載下的功耗最高為 11 W。可以同時連線兩路電源輸入，它們將以故障切換模式工作（電壓較高的輸入將作為主電源）。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線纜連線到 PoE 介面卡的 PoE+DATA 埠。
- 將來自本地網路（LAN）的乙太網線纜連線到 PoE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

該裝置被設定為交換器，以 192.168.88.1 作為網橋介面的管理 IP。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果 IP 連線不可用，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）透過裝置的 MAC 地址進行連線。該裝置配有一個 RJ45 序列埠，預設設定為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。可使用標準 RJ45 轉 COM 線纜，引腳定義可在文件中找到（參見上方連結）。出於恢復目的，可以引導裝置進行重灌，請參見下一節。

## 復位按鈕 {#reset-button}

復位按鈕具有以下功能：

- 在啟動期間按住此按鈕，直到使用者 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置。
- 繼續按住按鈕 5 秒鐘以上，或直到使用者 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器。第一個乙太網埠用於 Netinstall 過程。

無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統將載入備份 RouterBOOT 載入器。在 LED 開始閃爍之前鬆開按鈕，即可僅載入備份 RouterBOOT 而不進行重設。這對於 RouterBOOT 偵錯和恢復很有用。

## LED 指示燈 {#led-indicators}

- 當路由器透過 DC 插孔或 PoE 供電時，電源 LED 點亮。
- 使用者 LED 可以從 RouterOS 進行配置。
- 埠 LED 指示各個乙太網和 SFP 埠的活動狀態。

## 安裝 {#mounting}

本裝置設計用於室內使用，可使用隨附的機架掛耳安裝在機架機箱中，也可以放置在桌面上。如果指定用途為機架機箱，請使用十字螺絲刀將機架掛耳固定到裝置兩側：

- 將機架掛耳安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如照片所示。

![](/img/837a6d2bb5f312fe.webp)

- 將裝置放入機架機箱，並使其與孔位對齊，以便裝置順利安裝。
- 擰緊螺絲將其固定到位。

本裝置沒有防水汙染保護，請確保將裝置放置在乾燥且通風的環境中。我們建議為我們的裝置使用 Cat6 線纜。本裝置的安裝和配置應由合格人員完成。

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>說明</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>CRS112-8G-4S-IN</td></tr><tr><td>**架構**</td><td>MIPSBE</td></tr><tr><td>**CPU**</td><td>QCA8511，1 核，400 MHz</td></tr><tr><td>**交換晶片型號**</td><td>QCA8511-AL1C</td></tr><tr><td>**RAM**</td><td>128 MB</td></tr><tr><td>**儲存**</td><td>16 MB，Flash</td></tr><tr><td>**10/100/1000 乙太網埠**</td><td>8</td></tr><tr><td>**SFP 埠**</td><td>4</td></tr><tr><td>**PoE 輸入**</td><td>無源 PoE，10-57 V</td></tr><tr><td>**DC 插孔輸入電壓**</td><td>10-57 V</td></tr><tr><td>**最大功耗**</td><td>10 W</td></tr><tr><td>**尺寸**</td><td>200 × 143 × 44 mm</td></tr><tr><td>**工作溫度**</td><td>-40 °C 至 +70 °C</td></tr></tbody></table>

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/CRS112-8G-4S-IN](https://mikrotik.com/product/CRS112-8G-4S-IN)

## 配件 {#accessories}

![](/img/e06749365ce09789.webp)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS。具體的出廠預裝版本列在 /system resource 中。其他作業系統尚未經過測試。

## 安全提示 {#safety-notice}

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置點處置。請了解將裝置妥善運送到您所在地區指定處置點的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝環境提供合理的有害干擾防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區域操作本裝置很可能造成有害干擾，在此情況下，使用者需要自行承擔費用來糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能使使用者操作本裝置的許可權失效。本裝置符合 FCC 規則第 15 部分。操作須遵守以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。注意：本機型在測試時外圍裝置使用了遮蔽線纜。為確保合規，本裝置必須使用遮蔽線纜。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。操作須遵守以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。其執行須遵守以下兩個條件：(1) 裝置不得產生干擾；(2) 使用者必須接受裝置所承受的任何無線電干擾，即使該干擾可能影響其正常執行。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期的資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位），後面兩位表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## Norma Oficial Mexicana {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
