---
title: "hEX S"
slug: /hex-s
source: https://manual.mikrotik.com/hardware/hex-s
captured_at: '2026-11-04T05:58:43+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/fb8d9c844c5d465f.jpg" alt="" width={799} height={497} /></p>

## [hEX S](https://mikrotik.com/product/hex_s) (RB760iGS) {#hex-s-rb760igs}

hEX S 是一款六口有線千兆路由器，帶有 SFP 埠和 PoE 輸出。完整規格和宣傳冊請參見 [hEX S 產品頁面](https://mikrotik.com/product/hex_s)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置僅供室內使用，可放置在平坦表面上或安裝到牆上。開始安裝之前，請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能會對人員造成危險並損壞系統。
- 請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家/地區的規定，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將您的網際網路網線連線到標有“Internet”的兩個埠之一，具體取決於您將使用 SFP 模組還是乙太網；
- 選擇您的供電方案，可選方式請參見“供電”章節；
- 如果不使用 PoE，請連線直流電源插孔以啟動裝置；
- 將您的本地網路計算機連線到埠 2-5；
- 將您的計算機 IP 配置設定為自動（DHCP）；
- 配置應使用 Web 瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 完成。**提供了多種配置方法以確保可訪問性；**
- 在 Web 瀏覽器中開啟 https://192.168.88.1 以開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇“**Neighbors**”標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為“**admin**”，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在“Downloads”部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的“**Files**”選單，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內，可放置在平坦表面上或安裝到牆上，安裝孔位位於裝置底部，包裝中不包含螺釘。尺寸為 4x25 mm 的螺釘可很好地適配，根據您的牆體結構，如有需要，可以使用 6x30 mm 的膨脹螺栓和 6 mm 鑽頭。

安裝到牆上時，請確保線纜饋線朝下。我們建議為我們的裝置使用 Cat6 遮蔽網線。本裝置的 IP 防護等級為 IPX0。

## 配置 {#configuration}

除本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help) 開始，以熟悉各種可能的功能。如果無法使用 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自網際網路埠的所有訪問均被阻止）。出於恢復目的，可以從網路啟動裝置，請參見復位按鈕。

## 供電 {#powering}

裝置可透過電源插孔或第一個乙太網埠供電：

- 直流電源插孔（外徑 5.5mm、內徑 2mm，母頭，針腳為正極）接受 DC ⎓ 12-57 V。
- 第一個乙太網埠接受 DC ⎓ 12-57 V 範圍內的無源或 802.3af/at 乙太網供電。

在無外接負載的最大負載下，本裝置的功耗最高為 6 W。使用 802.3af/at 為本裝置供電時，為了獲得最佳相容性，我們建議不要接地。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網網線連線到 PoE 介面卡的 PoE 埠；
- 將來自您 LAN 的乙太網網線連線到 PoE 介面卡的 LAN 埠，注意資料和電流流向的箭頭；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個獨立的 10/100/1000 千兆乙太網埠，支援自動交叉/直通網線糾正（Auto MDI/X），因此您可以使用直通或交叉網線連線到其他網路裝置。
- 一個 SFP 模組插槽，支援 1.25G 模組。
- MicroSD 插槽，用於擴充套件內建儲存。
- USB type-A。

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並通電，然後：

- 當綠色 SFP LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 SFP LED 變為常亮綠色時鬆開按鈕，可清除所有配置並橋接所有介面。
- 在 SFP LED 不再點亮（約 20 秒）後鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 所必需）。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 模式按鈕 {#mode-button}

模式按鈕的動作可以透過 RouterOS 軟體進行配置，以執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。模式按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的附件：

<p><Img src="/img/b2651c72328afb77.webp" alt="" width={139} height={148} /></p>

請參見 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/hex_s](https://mikrotik.com/product/hex_s)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及更高版本。出廠預裝的具體版本列在 /system resource 中。其他作業系統尚未經過測試。

## 安全提示 {#safety-notice}

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢物處置場所處置。請熟悉在您所在地區將裝置正確運送到指定處置場所的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的保護，防止有害干擾。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：未經合規負責方明確批准的任何更改或修改，可能會使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期操作的干擾。注意：本裝置已在外圍裝置上使用遮蔽網線進行測試。必須使用遮蔽網線連線本裝置以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置非預期操作的干擾。本裝置符合適用於免許可無線電裝置的加拿大工業部 CNR 標準。允許在以下兩個條件下操作：(1) 裝置不得產生干擾，且 (2) 使用者必須接受裝置所承受的任何無線電干擾，即使該干擾可能影響其正常執行。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊，在裝置標籤上的序列號末尾以斜槓分隔顯示。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

<p><Img src="/img/984ad54320693690.webp" alt="" width={240} height={240} /></p>

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
