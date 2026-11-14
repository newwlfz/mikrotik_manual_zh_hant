---
title: "hEX PoE lite"
slug: /hex-poe-lite
source: https://manual.mikrotik.com/hardware/hex-poe-lite
captured_at: '2026-11-04T05:58:37+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/b88c127b18e5110e.jpg" alt="" width={799} height={505} /></p>

## [hEX PoE lite](https://mikrotik.com/product/RB750UPr2)（RB750UPr2） {#hex-poe-lite-rb750upr2}

hEX PoE lite 是一款配備五個乙太網埠的路由器。它有一個 USB 2.0 埠，並支援向埠 2-5 輸出 PoE 供電（每埠最大 500 mA）。完整規格和宣傳冊請參見 [hEX PoE lite 產品頁面](https://mikrotik.com/product/RB750UPr2)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適用於室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些電源和附件可在本產品的原包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將 WAN 線纜連線到埠 1，將 LAN 計算機連線到埠 2-5；
- 將裝置連線到電源；
- 將 LAN 計算機的 IP 配置設為自動（DHCP）；
- 配置應使用網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 完成。**提供多種配置方法以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保獲得最佳效能、穩定性和安全更新；
- 設定您的路由器密碼。

## 供電 {#powering}

該板卡可透過電源插孔或第一個乙太網埠（無源 PoE）接受供電：

- 直連輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母頭，中心正極插頭）接受 8-28 V DC；
- 第一個乙太網埠接受無源 Power over Ethernet 8-28 V DC。

正常情況下本裝置的功耗為 2.4 W，最大負載下為 3.6 W。

## 電源輸出 {#power-output}

本裝置可以透過其乙太網埠為外部裝置提供 PoE 供電。這很方便，因為您無需任何額外的 PoE 注入器即可為其他裝置供電。該功能由裝置型號名稱中的字母 "P" 表示。輸出電壓將與輸入電壓相同，並且需要在 RouterOS 軟體中在特定埠上啟用此功能。預設情況下它是停用的。在此模式下，每個乙太網埠的最大輸出功率為 500mA。在 RouterOS 中啟用 Power Output 後，乙太網 LED 燈會由綠色變為紅色。紅色 LED 表示該埠當前正在提供 PoE 供電。

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的 "Check for updates" 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保您已選擇裝置將要使用的國家/地區，以符合當地法規。

除了本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help) 開始，以熟悉各種可能性。如果無法建立 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都被阻止）。出於恢復目的，可以從網路引導裝置，請參見復位按鈕。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個獨立乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X），因此您可以使用直通或交叉線纜連線到其他網路裝置。乙太網埠接受來自無源 PoE 注入器的 8-28 V DC 供電，建議使用 12 V 或更高電壓以補償線纜損耗。
- 一個 USB type A。

## 復位按鈕 {#reset-button}

復位按鈕有三個功能：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置和預設值。
- 當 LED 熄滅後（約 20 秒）鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。

無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 規格 {#specifications}

如需瞭解有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/RB750UPr2](https://mikrotik.com/product/RB750UPr2)

## 作業系統支援 {#operating-system-support}

裝置支援 RouterOS v7 及以上版本。具體出廠安裝的版本列於 /system resource 中。其他作業系統尚未經過測試。

## 安全提示 {#safety-notice}

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<p><Img src="/img/ce6fc3eb10b9a1e6.webp" alt="" width={558} height={406} /></p>

本裝置已經過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為商業安裝提供合理的有害干擾防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明手冊安裝和使用，可能會對無線電通訊造成有害干擾。在住宅區操作本裝置很可能造成有害干擾，在這種情況下，使用者需要自費糾正干擾。

FCC 警告：未經合規責任方明確批准的任何更改或修改都可能使使用者喪失操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須遵守以下兩個條件：(1) 本裝置不得造成有害干擾，(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。注意：本裝置在測試時外圍裝置使用了遮蔽線纜。必須使用遮蔽線纜與本裝置配合，以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可證 RSS 標準。操作須遵守以下兩個條件：(1) 本裝置不得造成干擾，(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 A 類數字裝置符合加拿大 ICES-003。

此 [A] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (A) / NMB-003 (A)

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

有關裝置製造日期的資訊標示在其標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），接下來的兩位數字表示週數。

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

歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
