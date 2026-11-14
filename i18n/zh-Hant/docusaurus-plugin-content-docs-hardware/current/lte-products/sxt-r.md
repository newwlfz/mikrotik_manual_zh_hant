---
title: "SXT R"
slug: /sxt-r
source: https://manual.mikrotik.com/hardware/sxt-r
captured_at: '2026-11-04T10:05:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/c940bb43baa154ad.webp)

## [SXT R](https://mikrotik.com/product/sxt_r) (RBSXTR) {#sxt-r-rbsxtr}

SXT R 出廠時不帶模組，內建 LTE 天線，具有兩個支援 MDI-X 自動檢測的 10/100 乙太網介面。裝置提供兩個 micro SIM 卡槽，用於在不同運營商之間切換。完整規格和宣傳冊請參見 [SXT R 產品頁面](https://mikrotik.com/product/sxt_r)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解電氣電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 在任何牆面安裝接入點的所有安裝方式均須獲得當地主管機構的認可。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於戶外安裝在立杆上。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置或未遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 僅使用製造商認可且可在本產品原包裝中找到的電源和配件。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 若裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座上拔下。
- 客戶有責任遵守當地國家法規，包括在合法頻段內工作、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置安裝和執行時，與您的身體、職業使用者或公眾的距離不得小於 45 釐米。

## 首次使用 {#first-use}

- 開啟底部蓋板。
- 將所需的卡安裝到 miniPCIe 插槽中，請參閱相關段落（連結）。
- 將 micro-SIM 卡插入 micro-SIM 卡槽（預設使用 SIM A 卡槽）。
- 將裝置連線到電源（參見 "SXT kit-series#Powering"）。
- 裝置上電且 PC 連線到裝置後，請在 Web 瀏覽器或 WinBox 中開啟 [https://192.168.88.1](https://192.168.88.1)

以開始配置（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）。

- 使用者名稱為 a*dmin*，預設沒有密碼，您將自動登入到 Quick Set 介面。
- 您應點選右側的 "Check for updates" 按鈕，並將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性。必須具有網際網路連線和有效的 SIM 卡。
- 如需手動更新裝置，請訪問我們的網頁，並將最新的（MIPSBE）軟體包下載到您的 PC。
- 開啟 Web 瀏覽器或 WinBox，將軟體包上傳到 Files 選單，然後重啟裝置。
- 在右側底部的 "Password" 欄位中設定路由器密碼，並在 "Confirm Password" 欄位中重複輸入，該密碼將在下次登入時使用。
- 選擇 "Apply Configuration" 儲存更改。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 兩個 10/100 乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X）。連線其他網路裝置時，可使用直通線或交叉線。
- MiniPCIe 插槽和兩個 SIM 卡槽（不能單獨使用），用於 3G/4G/LTE 模組。
- 按下 Mode 按鈕時，可執行任意指令碼。

## 供電 {#powering}

裝置可透過乙太網埠 ETH1 接受 18-57 V DC 無源供電和 802.3af/at PoE 供電。包裝內包含一個 24 V 介面卡和一個無源 PoE 注入器。無外接附件時功耗最高為 6 W。

### 連線 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將乙太網線纜從裝置連線到 POE 介面卡的 POE 埠。
- 將來自您區域網路的乙太網線纜連線到 POE 介面卡的 LAN 埠，注意資料和電力流向的箭頭。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

登入後，您應在 Quick Set 選單中選擇 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將要使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參見相關章節。

## MiniPCIe 插槽的使用 {#minipcie-slot-usage}

此 SXT 版本未預裝出廠模組。要安裝模組，您需要取下塑膠頂蓋，並將 PCB 板從底殼中取出。安裝 miniPCIe 模組應由具備資質的人員完成，處理電氣裝置時請遵循安全預防措施：

![](/img/c8f7fd233b164227.webp)

- 在拆包和處理電氣元件時請使用腕部接地帶，以避免靜電放電（ESD）損壞。
- 取下頂蓋時，將塑膠工具插入六個孔中的一個，稍微向側面轉動並輕輕扭動，使蓋子略微脫離其固定位置。
- 繼續沿周邊操作，直到所有卡扣都鬆開。
- 向上提起以取下頂蓋。
- 您將接觸到 PCB 的上表面和天線，取下兩個黑色軟墊以接觸 PCB 固定件。
- 將兩個塑膠固定件向相反方向推，使 PCB 板脫離其位置。
- 取出 PCB 板，小心地向上提起並放置在防靜電墊上。
- 在 PCB 底部找到 mini PCIe 插槽，並取下兩顆出廠固定的螺絲。
- 在卡上貼上隨附的厚導熱墊。
- 將卡安裝到 miniPCIe 插槽中，使導熱墊位於 PCB 和卡之間。
- 使用之前取下的兩顆螺絲將卡固定到位。
- 將灰色 uFL 接頭連線到模組的 MAIN 天線接頭，將黑色線纜連線到輔助（或 AUX）接頭。使用矽膠型橡膠將線纜固定到位。
- 在卡的頂部貼上較薄的導熱墊。
- 按相反順序重新組裝。將裝置重新裝入外殼後，將移動運營商的 SIM 卡晶片朝下插入 SIM 卡槽。

## 安裝 {#mounting}

SXT 設計用於安裝在立杆上，包裝內包含安裝支架和鋼製卡箍。

![](/img/6a16db5b9e901d59.webp)

- 使卡扣朝前，將安裝支架滑入外殼底部的導軌，直到卡扣咔嗒一音效卡入到位。
- 將卡箍穿過支架上的開口。
- 將裝置安裝到立杆上，使乙太網埠朝下。
- 對齊完成後，使用 PH2 螺絲刀擰緊卡箍。
- 使用紮帶將乙太網線纜固定在立杆上，距離裝置不超過一米，以免線纜被從埠中拉出。
- 檢查安裝角度和位置。在戶外安裝時，確保所有線纜開口朝下。使用 POE 注入器和適當的接地，本裝置在埠蓋下方設有專門設計的接地聯結器。建議使用 Cat5/6 線纜。本裝置的 IP 防護等級為 IP54。SXT 裝置有一個滑動門，乙太網埠和復位按鈕位於其後。也可以用螺絲將門鎖緊在所提供的螺絲孔中。使用兩個乙太網埠時，請務必在塑膠門上切出更寬的線纜開口。您可以使用鉗子撕掉保護線纜開口的塑膠片。關閉塑膠門時，請務必施加壓力，直到它"咔嗒"一音效卡入到位。*本裝置的安裝和配置應由具備資質的人員完成。*

## 接地 {#grounding}

安裝基礎設施（塔架和桅杆）以及路由器本身必須正確接地。裝置在機殼門後方設有接地線連線螺絲。將接地線連線到接地螺絲上，然後將接地線的另一端連線到已接地的桅杆上。這可以大幅降低 ESD 和雷擊損壞的風險。

## LED 指示燈 {#led-indicators}

- 電源 LED 表示裝置正透過 ETH1 埠接收電力。
- LTE LED 表示裝置當前已連線到蜂窩基站。
- LTE 訊號 LED 顯示蜂窩訊號的強度。
- PoE LED 表示 ETH2 埠當前正在透過 PoE 為另一臺裝置供電。

## 復位按鈕 {#reset-button}

routerBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置復位為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並恢復預設值。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。無論使用上述哪種方式，如果在裝置接通電源之前就按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 模式按鈕 {#mode-button}

可透過 RouterOS 軟體配置模式按鈕的動作，以執行任何使用者提供的 RouterOS 指令碼。您也可以停用此按鈕。模式按鈕可在 RouterOS 選單 /system routerboard mode-button 中配置。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的配件：

![](/img/cf6d48ddc802bec5.webp)

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/sxt_r](https://mikrotik.com/product/sxt_r)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及更高版本。具體的出廠預裝版本列於 /system resource 中。其他作業系統尚未經過測試。

## SIM 卡槽的使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。

Nano SIM 卡的厚度不同，不建議配合轉接卡使用。

250

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全方式處置，例如送至指定的廢棄物處置場。請了解您所在地區將裝置妥善運送至指定處置場的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝提供合理的有害干擾防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所接電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。**FCC 警告：** 未經合規責任方明確批准的任何更改或修改，都可能導致使用者操作本裝置的許可權失效。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，並且 (2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與任何其他天線或發射機共置或協同工作。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。操作須滿足以下兩個條件：(1) 本裝置不得造成干擾，並且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes : (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊，以斜槓分隔標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

要在烏克蘭使用，必須按照 NCCIR 2012 年 11 月 1 日第 559 號決議批准並在烏克蘭司法部 2013 年 1 月 3 日以第 57/22589 號登記的程式取得使用許可。

### CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Mikrotīkls SIA 特此宣告，無線電裝置型別 RBSXTR 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
