---
title: "RB3011UiAS-RM"
slug: /rb3011uias-rm
source: https://manual.mikrotik.com/hardware/rb3011uias-rm
captured_at: '2026-11-04T06:03:53+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/47e62aa56e12a2f1.webp" alt="" width={798} height={232} /></p>

## [RB3011UiAS-RM](https://mikrotik.com/product/RB3011UiAS-RM) {#rb3011uias-rm}

RB3011UiAS-RM 是一款機架式有線路由器，配備十個千兆乙太網埠、一個 SFP 籠、USB 3.0、一個 LCD 面板以及在 Ether10 上的 PoE-out。完整規格和宣傳手冊請參閱 [RB3011UiAS-RM 產品頁面](https://mikrotik.com/product/RB3011UiAS-RM)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應按照所有國家法律法規進行處理。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本裝置適用於安裝在機架中。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟可能會給人員帶來危險並損壞系統。
- 本產品適用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證不會因不當使用裝置而發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請將其與電源斷開。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將您的網際網路網線連線到埠 1，將區域網路計算機連線到埠 2-10；
- 選擇您的供電方案，請參閱供電部分；
- 將裝置連線到電源；
- 配置您的網路卡設定，以使用 DHCP 自動獲取 IP 地址；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 完成。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將您的 RouterOS 軟體更新到最新版本，以確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

本裝置可從電源插孔或 LAN1 乙太網埠獲取供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）可接受 10-30 V DC ⎓（過壓保護從 30 V 開始）。
- Eth1 埠可接受來自非標準（無源）Power over Ethernet 注入器的 10-30 V DC ⎓ 輸入（在板上；長電纜上需要更高電壓以補償功率損耗）。本板不支援符合 IEEE802.3af 的 48 V 電源注入器。

最大負載下的功耗可達 30 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網電纜連線到 PoE 介面卡的 PoE 埠；
- 將來自您區域網路的乙太網電纜連線到 PoE 介面卡的 LAN 埠，注意資料與功率流向的箭頭；
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 十個 10/100/1000（千兆）乙太網埠（Auto MDI/X）。
- USB 3.0 type A。
- LCD 面板。
- 用於 SFP 模組的 SFP 埠。
- Ether10 埠支援帶自動檢測的 PoE 輸出，因此可以連線非 PoE 裝置而不會造成損壞。Ether10 上的 PoE-out 輸出比輸入電壓低約 2 V，最高支援 0.7 A，因此隨附的 24 V 電源將在 Ether10 PoE 埠上提供 22 V、0.7 A 的輸出。

## 安裝 {#mounting}

<p><Img src="/img/27bf22aa32ecbced.webp" alt="" width={610} height={543} /></p>

本裝置專為室內使用而設計，可使用隨附的機架安裝件安裝在機架式機箱中，也可以放置在桌面上。如果希望放置在平面上，請在路由器底部貼上橡膠腳墊；如果指定用於機架式機箱，請使用十字螺絲刀將機架耳固定在裝置兩側：

- 將機架耳安裝到裝置兩側，並擰緊四顆螺絲將其固定到位，如右圖所示；
- 將裝置放入機架式機箱並對準孔位，使裝置方便地安裝到位；
- 擰緊螺絲將其固定到位。

本裝置的 IP 防護等級為 IPX0。該裝置沒有防水汙染保護，請確保將裝置放置在乾燥通風的環境中。我們建議為我們的裝置使用 Cat5/6 網線。*本裝置的安裝和配置應由具備資質的人員完成。*

工作溼度可為 5% 到 95%，無冷凝。

## 配置 {#configuration}

RouterOS 除本文件所述內容外還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help) 開始，以熟悉各種可能性。如果無法建立 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側透過裝置的 MAC 地址進行連線（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參閱復位按鈕。

## 復位按鈕 {#reset-button}

要使用復位按鈕，請按住它，然後在不鬆開按鈕的情況下開啟裝置。

- 當綠色 LED 開始閃爍時鬆開按鈕，即可復位 RouterOS 配置。為了不載入備用載入程式，您可以在已通電後再開始按住按鈕。
- 在 LED 不再閃爍後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 所必需）。您也可以在裝置出現在 Netinstall 實用程式的裝置列表中時鬆開按鈕。

無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都會載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下配件：

- EU/US 開關電源 DC ⎓ 24 V, 1.2 A, 28.8 W, 86.8%, VI, 線纜：220 cm。
- 1U 機架安裝支架，黑色。
- 用於 RB2011 機架式機箱的固定套件 K-19 v3。

<p><Img src="/img/2ca97fab837580cb.webp" alt="" width={176} height={196} /></p>

請參閱 [MikroTik SFP 模組相容性表](/docs/wired-connections/mikrotik-wired-interface-compatibility)。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/RB3011UiAS-RM](https://mikrotik.com/product/RB3011UiAS-RM)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

## 安全提示 {#safety-notice}

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢棄物處置場所。請熟悉您所在地區將裝置正確運送到指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的保護，防止有害干擾。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），建議使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整或重新放置接收天線。
- 增加裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 向經銷商或有經驗的無線電/電視技術人員諮詢以獲得幫助。

FCC 警告：任何未經合規負責方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行須符合以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受接收到的任何干擾，包括可能導致意外執行的干擾。注：本裝置在測試時對外圍裝置使用了遮蔽電纜。必須使用遮蔽電纜與本裝置配合，以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。其執行須符合以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊標註在其標籤上序列號的末尾，以斜線分隔。第一位數字表示年份編號（年份的最後一位數字），隨後的兩位數字表示周編號。

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

歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
