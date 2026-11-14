---
title: "RB2011iL-IN"
slug: /rb2011il-in
source: https://manual.mikrotik.com/hardware/rb2011il-in
captured_at: '2026-11-04T06:03:39+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/a43b53271bb00e1f.webp" alt="" width={798} height={259} /></p>

## [RB2011iL-IN](https://mikrotik.com/product/RB2011iL-IN) {#rb2011il-in}

RB2011iL-IN 是一款室內有線路由器，具有五個千兆埠和五個 Fast Ethernet 埠，並在 Ether10 上提供 PoE-out。完整規格和宣傳冊請參見 [RB2011iL-IN 產品頁面](https://mikrotik.com/product/RB2011iL-IN)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家電氣規範。
- 本裝置僅供室內使用，可放置在平坦表面上或安裝在牆上。開始安裝前，請仔細閱讀安裝說明。使用錯誤的硬體或未遵循正確的操作步驟，可能會對人員造成危險情況並對系統造成損壞。
- 本產品僅供室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商批准且可在本產品原包裝中找到的電源和附件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家/地區的法規，包括在合法頻率通道內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將您的網際網路網線連線到埠 1，將本地網路計算機連線到埠 2-10；
- 選擇您的供電方案，請參閱“供電”一節；
- 將裝置連線到電源；
- 將您的網路卡設定為使用 DHCP 自動獲取 IP 地址；
- 應使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行配置。**提供多種配置方法以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果 IP 地址不可用，請使用 **WinBox** 並選擇“**Neighbors**”標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為“**admin**”，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在“Downloads”部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的“**Files**”選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

本裝置可透過電源插孔或 LAN1 乙太網埠供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，正極針式插頭）接受 8-30 V DC（過壓保護從 30 V 開始）。
- Eth1 埠接受來自非標準（無源）乙太網供電注入器的 8-30 V DC 輸入（在板端；長線纜上需要更高電壓以補償功率損耗）。該板卡不適用於符合 IEEE802.3af 標準的 48 V 電源注入器。

最大功耗 6 W，帶附件時為 18 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 PoE 介面卡的 PoE 埠；
- 將來自您區域網路的乙太網線連線到 PoE 介面卡的 LAN 埠，注意資料和電流流向的箭頭；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 輸出功率 {#power-output}

Ether10 上的 PoE-out 輸出比輸入電壓低約 2 V，最高支援 0.58 A，因此隨附的 24 V 電源將在 Ether10 PoE 埠上提供 22 V、0.58 A 的輸出。

## 配置 {#configuration}

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help) 開始，以熟悉各種可能性。如果無法使用 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從區域網路側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都被阻止）。出於恢復目的，可以從網路引導裝置，請參閱復位按鈕。

## 安裝 {#mounting}

本裝置設計為室內使用，可放置在平坦表面上，所有需要的線纜連線到裝置前部。或者，也可以將裝置安裝在牆上，安裝套件可單獨購買，詳情請訪問我們的產品頁面：[https://mikrotik.com/product/RBWMK](https://mikrotik.com/product/RBWMK)。接地螺釘位於裝置外殼背面，請按照要求將其連線到有效接地。

<p><Img src="/img/89a51fc3d8a42270.webp" alt="" width={50} height={81} /></p>

安裝在牆上時，請確保線纜進出方向朝下。本裝置的 IPX 防護等級為 IPX0。我們建議使用 Cat6 遮蔽網線。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個 10/100/1000（千兆）乙太網埠（Auto MDI/X）
- 五個 10/100（快速）乙太網埠（Auto MDI/X）
- Ether10 支援 500 mA 輸出功率，比輸入電壓低約 2 V。Power-out 支援自動檢測，以保護非 PoE 裝置。

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並將所有介面橋接。
- 在 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時必需）。

無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入器。這對於 RouterBOOT 偵錯和恢復很有用。

## 規格 {#specifications}

如需瞭解有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/RB2011iL-IN](https://mikrotik.com/product/RB2011iL-IN)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

<p><Img src="/img/bed9fc8ab95db9f7.webp" alt="" width={181} height={195} /></p>

## 安全提示 {#safety-notice}

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝環境中的有害干擾提供合理防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能會造成有害干擾，此時使用者需自費糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。注意：本裝置已使用外圍裝置上的遮蔽線纜進行測試。必須使用遮蔽線纜與本裝置配合，以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置操作異常的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊標註在其標籤上序列號的末尾，由斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後續兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

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
