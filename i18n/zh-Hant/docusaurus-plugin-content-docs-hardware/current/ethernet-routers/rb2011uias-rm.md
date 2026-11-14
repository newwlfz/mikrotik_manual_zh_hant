---
title: "RB2011UiAS-RM"
slug: /rb2011uias-rm
source: https://manual.mikrotik.com/hardware/rb2011uias-rm
captured_at: '2026-11-04T06:03:51+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/218439e4a8e82980.webp" alt="" width={799} height={230} /></p>

## [RB2011UiAS-RM](https://mikrotik.com/product/RB2011UiAS-RM) {#rb2011uias-rm}

RB2011UiAS-RM 是一款機架式有線路由器，配備五個千兆乙太網埠和五個快速乙太網埠、一個 SFP 籠、USB、LCD 面板，並在 Ether10 上提供 PoE-out。完整規格和宣傳冊請參見 [RB2011UiAS-RM 產品頁面](https://mikrotik.com/product/RB2011UiAS-RM)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家和地區的法律法規進行。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置適合安裝在機架中。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 本產品適合室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將您的網際網路網線連線到埠 1，將本地網路計算機連線到埠 2-10；
- 選擇合適的供電方案，請參見“供電”部分；
- 將裝置連線到電源；
- 配置您的網路卡設定，使用 DHCP 自動獲取 IP 地址；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方法以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

裝置可透過電源插孔或 LAN1 乙太網埠供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，正極插針）接受 8-30 V DC（過壓保護從 30 V 開始）。
- Eth1 埠可從非標準（被動式）乙太網供電注入器接受 8-30 V DC 輸入（在板端；長線纜上需要更高電壓以補償功率損耗）。該板卡不能與符合 IEEE802.3af 的 48 V 電源注入器配合使用。

最大功耗 6 W，帶附件時 18 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網網線連線到 PoE 介面卡的 PoE 埠；
- 將來自您區域網路的乙太網網線連線到 PoE 介面卡的 LAN 埠，注意資料和功率流向的箭頭；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 電源輸出 {#power-output}

Ether10 上的 PoE-out 輸出約比輸入電壓低 2 V，最高支援 0.58 A，因此隨附的 24 V 電源將在 Ether10 PoE 埠上提供 22 V、0.58 A 的輸出。

## 配置 {#configuration}

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help)開始，以熟悉各種可能性。如果無法建立 IP 連線，可使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下，來自 Internet 埠的所有訪問都被阻止）。出於恢復目的，可以從網路引導裝置，請參見復位按鈕。

## 安裝 {#mounting}

本裝置設計用於室內使用，可放置在桌面上，也可以使用十字螺絲刀將機架耳固定在裝置兩側，將其安裝到機架中：

- 將機架耳安裝到裝置兩側，並擰緊四顆螺絲將其固定到位；
- 將裝置放入機架外殼並對齊孔位，使裝置能夠方便地裝入；
- 擰緊螺絲將其固定到位。

本裝置沒有防水汙染保護，請確保將裝置放置在乾燥且通風的環境中。*本裝置的安裝和配置應由具備資質的人員完成。* 接地螺絲位於裝置外殼背面，請相應地將其連線到有效接地。

<p><Img src="/img/89a51fc3d8a42270.webp" alt="" width={50} height={81} /></p>

在牆面安裝時，請確保線纜進線方向朝下。本裝置的 IPX 防護等級為 IPX0。我們建議使用 Cat6 遮蔽網線。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個 10/100/1000（千兆）乙太網埠（Auto MDI/X）
- 五個 10/100（快速）乙太網埠（Auto MDI/X）
- Ether10 支援 500 mA 輸出功率，約比輸入電壓低 2 V。Power-out 支援自動檢測以保護非 PoE 裝置。
- 1G SFP 埠。
- A 型 USB 插槽。
- 序列埠。
- 用於配置的 LCD。

請參見 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並橋接所有介面。
- 當 LED 熄滅（約 20 秒）後鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。

無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 規格 {#specifications}

如需瞭解有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/RB2011UiAS-RM](https://mikrotik.com/product/RB2011UiAS-RM)

<p><Img src="/img/55cedc0575138e32.webp" alt="" width={181} height={192} /></p>

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## 安全提示 {#safety-notice}

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處理場所。請了解將裝置正確運送到您所在地區指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝提供合理的有害干擾防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區執行本裝置可能會造成有害干擾，此時使用者將被要求自行承擔費用來糾正干擾。

FCC 警告：任何未經合規負責方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何收到的干擾，包括可能導致意外執行的干擾。注意：本裝置已在外圍裝置上使用遮蔽線纜進行測試。必須使用遮蔽線纜與本裝置配合，以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。其執行須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期的資訊以斜槓分隔標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

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

EU 符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
