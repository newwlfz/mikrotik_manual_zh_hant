---
title: "RB1100 系列"
slug: /rb1100-series
source: https://manual.mikrotik.com/hardware/rb1100-series
captured_at: '2026-11-04T06:03:36+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

:::info 本文涵蓋

- **[RB1100AHx4](https://mikrotik.com/product/rb1100ahx4)**
- **[RB1100AHx4 Dude Edition](https://mikrotik.com/product/RB1100Dx4)**
:::

<p><Img src="/img/4053195db135534a.jpg" alt="" width={799} height={551} /></p>

<p><Img src="/img/efb7383277cd62f2.webp" alt="" width={161} height={72} /></p>

RB1100 是一款可安裝於機架的乙太網路由器，具有 13 個千兆乙太網埠。其中兩個埠提供 bypass 功能。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品僅供室內安裝使用。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些電源和附件可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員進行安裝。

## 快速開始 {#quickstart}

- 將您的 ISP 線纜連線到 Ethernet1 埠，並將本地網路中的計算機連線到其他埠；
- 將裝置連線到電源；
- 將您的網路卡配置為 192.168.88.0/24 網段中的地址，因為裝置預設未啟用 DHCP 伺服器；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方法以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 以開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

裝置可透過機箱背面的雙路/故障切換 IEC 電源介面供電。您可以單獨使用其中任意一個介面，也可以同時使用兩個介面以實現故障切換。裝置還支援在乙太網埠 13 上使用 12-57V 無源 PoE 或 802.3af/at PoE。裝置還有一個接線端子，可用於 Telecom -48V DC 供電或 24-57 V 範圍內的任何其他 DC 供電。

## 配置 {#configuration}

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help) 開始，以熟悉各種可能性。如果無法建立 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都會被阻止）。為便於恢復，可以從網路引導裝置，請參閱復位按鈕。

## 啟動過程 {#booting-process}

首先啟動 RouterBOOT 載入程式。它會在板載 RS232C 非同步序列埠上顯示啟動資訊。序列埠預設設定為 115200 bit/s、8 個數據位、1 個停止位、無奇偶校驗。

隨後 RouterOS 系統會載入。這也會由兩聲蜂鳴聲指示。

您可以將計算機插入 Ether1 埠，並使用使用者名稱 "**admin**" 和無密碼（或者，對於某些型號，請檢視貼紙上的使用者密碼和無線密碼）連線到 192.168.88.1，從而透過 SSH、**WinBox** 或 Web 介面連線到裝置。裝置預設未啟用 DHCP 伺服器，您的 PC 應配置為該網段中的地址。

有關連線裝置的更多資訊：[https://mt.lv/help](https://mt.lv/help)

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 13 個千兆乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X），因此您可以使用直通線或交叉線連線其他網路裝置。ETH13 埠支援 PoE 供電，並可用於從網路引導裝置，以便透過 Netinstall 工具重新安裝（參見文件）
- DB9 RS232C 非同步序列埠
- microSD 插槽
- 2 個 M.2 插槽，可接受 2280 外形尺寸的 SATA 型別 M.2 SSD 磁碟（僅限 Dx4 型號）
- 2 個 2.5 英寸 SATA 介面，可接受標準 2.5" SATA HDD 磁碟（僅限 Dx4 型號）

推薦使用無容量限制的 SATA3 M.2 2242mm/2260mm/2280mm B+M key SSD 磁碟。

## 復位按鈕 {#reset-button}

復位按鈕具有以下功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，然後鬆開按鈕以重設 RouterOS 配置。
- 或者繼續按住按鈕 5 秒鐘，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器。

bypass 開關可將埠 11 和 12 以 bypass 模式繫結在一起，這意味著如果裝置斷電，這兩個埠將被連線在一起，資料可以從一個埠傳到另一個埠，就好像裝置不存在一樣。

無論使用上述哪種選項，如果在裝置上電之前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對 RouterBOOT 偵錯和恢復很有用。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/rb1100ahx4](https://mikrotik.com/product/rb1100ahx4)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體的出廠預裝版本列在 /system resource 中。其他作業系統尚未經過測試。

<p><Img src="/img/9451b2eb2e7bf01c.webp" alt="" width={576} height={521} /></p>

## 安全提示 {#safety-notice}

觸電危險。本裝置只能由經過培訓的人員進行維護。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢物處置場所。請了解將裝置正確運送到您所在地區指定處置場所的相關程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝環境提供合理的保護，防止有害干擾。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊進行安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置可能會導致有害干擾，在這種情況下，使用者將被要求自費糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不會造成有害干擾，且 (2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。注意：本裝置在測試時外圍裝置使用了遮蔽電纜。為確保合規，必須使用遮蔽電纜連線本裝置。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可證 RSS 標準。操作須符合以下兩個條件：(1) 本裝置不得產生干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。本裝置符合適用於免許可證無線電裝置的加拿大工業部 CNR 標準。其執行須滿足以下兩個條件：(1) 裝置不得產生干擾，且 (2) 使用者必須接受裝置所受到的任何無線電干擾，即使該干擾可能影響其正常執行。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置製造日期資訊標註在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後面兩位數字表示周編號。

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
