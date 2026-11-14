---
title: "hEX lite"
slug: /hex-lite
source: https://manual.mikrotik.com/hardware/hex-lite
captured_at: '2026-11-04T05:58:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/82be4fc253534ed3.jpg" alt="" width={799} height={799} /></p>

## [hEX lite](https://mikrotik.com/product/RB750r2) (RB750r2) {#hex-lite-rb750r2}

5 個乙太網口，小型塑膠外殼，850MHz CPU，64MB RAM，最經濟實惠的 MPLS 路由器，RouterOS L4。完整規格與宣傳冊請參閱 [hEX lite 產品頁面](https://mikrotik.com/product/RB750r2)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應依照所有國家法律和法規執行。
- 裝置的安裝必須符合當地及國家的電氣規範。
- 本裝置僅供室內使用，可放置在平坦表面上或安裝在牆上。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體或不遵循正確的操作步驟，可能對人員造成危險並損壞系統。
- 請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請先閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的做法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 快速開始 {#quickstart}

- 選擇您的供電方案，請參閱“供電”章節瞭解可能的方案；
- 將乙太網線連線到埠 1（標記為 "Internet"），並將本地網路計算機連線到埠 2-5；
- 如果不使用 PoE，請連線直流輸入電源插孔以啟動裝置；
- 裝置將啟動，在短暫的蜂鳴聲後，網路即可連線；
- 將計算機的 IP 配置設定為自動（DHCP）；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 進行。**提供多種配置方法以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，無密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單並重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 安裝 {#mounting}

本裝置設計用於室內使用，可放置在平坦表面上或安裝在牆上，安裝孔位如下圖所示，包裝中不包含螺絲。尺寸為 4x25 mm 的螺絲很合適，根據牆體結構，如有需要可使用 6x30 mm 的膨脹螺栓和 6 mm 鑽頭。

<p><Img src="/img/e8c99734ffbc0e6b.webp" alt="" width={592} height={504} /></p>

安裝在牆上時，請確保線纜進線口朝下。我們建議為我們的裝置使用 Cat5/6 線纜。本裝置的 IP 防護等級為 IPX0。

## 供電 {#powering}

主機板可透過電源插孔或第一個乙太網埠（被動 PoE）供電：

- 直流輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，正極插針）接受 6-30 V DC；
- 第一個乙太網埠接受被動乙太網供電，接受 6-30 V DC。通常本裝置的功耗為 2 W。

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將要使用的國家，以符合當地法規。

除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help) 開始，以熟悉各種可能。如果 IP 連線不可用，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參閱復位按鈕。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個獨立的乙太網埠，支援自動交叉/直通線纜校正（Auto MDI/X），因此您可以使用直通或交叉線纜連線其他網路裝置。乙太網埠接受來自被動 PoE 注入器的 6-30 V DC 電源，建議使用 12 V 或更高電壓以補償線纜損耗。

## 復位按鈕 {#reset-button}

RouterBOOT 復位按鈕具有以下功能。按住按鈕並接通電源，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並橋接所有介面。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 所需）。

無論使用上述哪種選項，如果在裝置接通電源之前按下按鈕，系統都將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/RB750r2](https://mikrotik.com/product/RB750r2)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列在 /system resource 中。其他作業系統未經測試。

## 安全提示 {#safety-notice}

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢物處置場所。請熟悉將裝置正確運送到您所在地區指定處置場所的程式。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝提供合理的有害干擾防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置可能會造成有害干擾，此時使用者需自費糾正干擾。

FCC 警告：任何未經合規責任方明確批准的更改或修改，都可能導致使用者失去操作本裝置的許可權。

本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得產生有害干擾，(2) 本裝置必須接受任何接收到的干擾，包括可能導致非預期執行的干擾。

注意：本裝置已使用外圍裝置上的遮蔽電纜進行測試。必須使用遮蔽電纜以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須滿足以下兩個條件：(1) 本裝置不得產生干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置非預期執行的干擾。

本裝置所含的免許可發射機/接收機符合加拿大創新、科學和經濟發展部針對免許可無線電裝置適用的 CNR 規定。允許在以下兩個條件下執行：1) 本裝置不得產生干擾；2) 本裝置必須承受所收到的任何無線電干擾，即使該干擾可能導致其執行異常。

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

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
