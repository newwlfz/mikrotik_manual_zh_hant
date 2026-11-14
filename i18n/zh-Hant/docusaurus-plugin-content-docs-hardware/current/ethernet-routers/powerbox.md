---
title: "PowerBox"
slug: /powerbox
source: https://manual.mikrotik.com/hardware/powerbox
captured_at: '2026-11-04T06:02:41+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<p><Img src="/img/cb28f515f533d0a4.webp" alt="" width={800} height={729} /></p>

## [PowerBox](https://mikrotik.com/product/RB750P-PBr2) (RB750P-PBr2) {#powerbox-rb750p-pbr2}

PowerBox 是一款帶五個乙太網埠的室外裝置。包裝內包含 IEC 電源線、鋼製卡箍、PoE 注入器、24 V 電源介面卡和 DIN 安裝架。完整規格和宣傳冊請參見 [PowerBox 產品頁面](https://mikrotik.com/product/RB750P-PBr2)。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於在室外安裝在立柱上。開始安裝前請仔細閱讀安裝說明。使用錯誤的硬體和配置或未遵循正確的操作步驟，可能會對人員造成危險情況並對系統造成損壞。
- 僅使用製造商認可的電源和附件，這些可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置都必須由專業人員安裝。

## 快速開始 {#quickstart}

- 將 WAN 網線連線到埠 1，將其他裝置連線到埠 2-5；
- 將裝置連線到電源；
- 將網路卡設定為使用 DHCP 自動獲取 IP 地址；
- 配置應透過網頁瀏覽器中的 **WebFig** 或 **WinBox** 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) 完成。**提供多種配置方式以確保可訪問性；**
- 在網頁瀏覽器中開啟 https://192.168.88.1 開始設定。如果該 IP 地址不可用，請使用 **WinBox** 並選擇 "**Neighbors**" 標籤頁來查詢裝置。然後使用 MAC 地址進行連線。使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）；
- 如需手動更新裝置，請訪問 mikrotik.com，選擇您的型號，並在 "Downloads" 部分找到所需的軟體包；
- 將下載的軟體包上傳到 **WebFig** 或 **WinBox** 的 "**Files**" 選單，然後重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保最佳效能、穩定性和安全更新；
- 設定路由器密碼。

## 安裝 {#mounting}

可以使用隨附的 DIN 導軌支架和螺絲將裝置安裝到 DIN 導軌上。由於裝置具有防風雨的室外外殼，您也可以使用隨附的鋼製卡箍將其安裝在立柱上。

<p><Img src="/img/acc7dbfd27d05576.webp" alt="" width={274} height={312} /></p>

請確保安裝時乙太網埠朝下。

## 供電 {#powering}

該板可透過電源插孔或第一個乙太網埠（被動 PoE）供電：

- 直接輸入電源插孔（外徑 5.5 mm、內徑 2 mm，母座，中心正極插頭）接受 8-30 V DC，
- 第一個乙太網埠接受被動 Power over Ethernet，接受 8-30 V DC。

該裝置的功耗為 2 W。

## 電源輸出 {#power-output}

該裝置可以透過其乙太網埠為外部裝置提供 PoE 供電。這很方便，因為您無需任何額外的 PoE 注入器就能為其他裝置供電。此功能由裝置型號名稱中的字母 "P" 表示。輸出電壓將與輸入電壓相同，並且需要在 RouterOS 軟體中為特定埠啟用此功能。預設情況下它是停用的。此模式下每個乙太網埠的最大輸出功率為 1 A（所有埠總計 2 A）。在 RouterOS 中啟用 Power Output 後，乙太網 LED 燈也會以紅色亮起。紅色 LED 表示該埠當前正在提供 PoE 供電，綠色表示乙太網已建立鏈路，兩者同時亮起表示乙太網已建立鏈路且正在輸出電源。

## 配置 {#configuration}

除了本文件中描述的內容之外，RouterOS 還包含許多配置選項。我們建議從 [RouterOS 文件](https://mt.lv/help) 開始，以熟悉各種可能性。如果無法建立 IP 連線，可以使用 **WinBox** 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問都會被阻止）。為便於恢復，可以從網路引導裝置，請參見復位按鈕。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 五個獨立的乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X），因此您可以使用直通線或交叉線連線到其他網路裝置。

## 復位按鈕 {#reset-button}

復位按鈕有三種功能：

- 在啟動過程中按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可重設 RouterOS 配置。
- 或者繼續按住按鈕 5 秒鐘，直到 LED 熄滅，然後鬆開，使 RouterBOARD 查詢 Netinstall 伺服器。

無論使用上述哪種方式，如果在裝置通電之前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復非常有用。

## 配件 {#accessories}

包裝內包含以下隨裝置提供的附件：

- IEC 電源線。
- 鋼製卡箍。
- PoE 注入器。
- 24 V 電源介面卡。
- DIN 安裝架。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/RB750P-PBr2](https://mikrotik.com/product/RB750P-PBr2)

## 作業系統支援 {#operating-system-support}

該裝置支援 RouterOS v7 及以上版本。出廠預裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

<p><Img src="/img/c7c684760aa47212.webp" alt="" width={723} height={212} /></p>

## 安全須知 {#safety-notice}

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如在指定的廢棄物處置場。請熟悉您所在地區將裝置正確運送到指定處置場的相關程式。

## UKCA 標誌 {#ukca-marking}

<p><Img src="/img/5d0fc80f851cbbdf.webp" alt="" width={1600} height={1598} /></p>

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期的資訊以斜槓分隔的形式標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），隨後的兩位數字表示週數。

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
