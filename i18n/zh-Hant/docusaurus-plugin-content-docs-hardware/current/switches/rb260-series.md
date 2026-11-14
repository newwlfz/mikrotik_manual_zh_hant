---
title: "RB260 系列"
slug: /rb260-series
source: https://manual.mikrotik.com/hardware/rb260-series
captured_at: '2026-11-04T09:59:38+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/fe10609610848792.jpg)

![](/img/bef265ac73043df8.webp)

:::info 本文涵蓋

- **[RB260GS](https://mikrotik.com/product/RB260GS)**
- **[RB260GSP](https://mikrotik.com/product/RB260GSP)**
:::

CSS106 是一款帶有五個乙太網埠和一個 SFP 埠的網路交換器，由 SwOS 作業系統驅動。裝置已完成配置，所有埠均已相互交換連線。我們建議您設定密碼以保護您的裝置。CSS106-1G-4P-1S 的四個乙太網埠具備 PoE 輸出能力。

已測試並建議與以下 MikroTik SFP 模組搭配使用：S-85DLC05D、S-31DLC20D 和 S-35/53LC20D（不隨附）

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵循所有國家法律和法規。裝置的安裝必須符合當地和國家的電氣規範。本產品適合室內安裝。請讓本產品遠離水、火、潮溼或高溫環境。請僅使用製造商認可且可在本產品原始包裝中找到的電源和附件。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。客戶有責任遵守當地國家的法規，包括在法定頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 裝置必須由專業人員安裝。

## 供電 {#powering}

本裝置在最大負載下的功耗最高為 11 W。裝置可透過以下方式供電：

- 直流輸入電源插孔（外徑 5.5mm、內徑 2mm，母頭，中心正極插頭）接受 11-30 V DC。
- 組合乙太網埠接受無源 Power over Ethernet 11-30 V DC，不隨附 PoE 注入器。

## 首次使用 {#first-use}

請參閱 SwOS 手冊中的[連線到交換器](/docs/bridging-and-switching/swos/css106#connecting-to-the-switch)一節。

- 透過電源插孔（接受 11-30 V，裝置隨附電源介面卡）或透過第一個埠的無源 PoE（11-30 V）為裝置供電。
- 從 [https://mikrotik.com/download](https://mikrotik.com/download) 下載最新版本的 SwitchOS 軟體；
- 將您的計算機連線到其中一個乙太網埠；
- 將裝置連線到電源；
- 將您計算機的 IP 地址設定為 192.168.88.2；
- 開啟您的網頁瀏覽器，預設 IP 管理地址為 192.168.88.1，使用者名稱為 **admin** 且無密碼（部分型號請檢視貼紙上的使用者和無線密碼）；
- 在 Upgrade 標籤頁中透過網頁瀏覽器上傳檔案，升級完成後裝置將重啟；
- 設定您的密碼以保護裝置。

## 配置 {#configuration}

裝置已設定為交換器模式，以 192.168.88.1 作為主介面的管理 IP。

SwOS 是一款專為管理 MikroTik 交換器產品而設計的作業系統。

SwOS 可透過您的網頁瀏覽器進行配置。它為您提供受管交換器所需的所有基本功能以及更多功能：允許您管理埠到埠的轉發、廣播風暴控制、應用 MAC 過濾、配置 VLAN、映象流量、應用頻寬限制，甚至調整部分 MAC 和 IP 頭欄位。

配置詳情請參閱 [CSS106 (RB260) 系列 SwOS 手冊](/docs/bridging-and-switching/swos/css106)。

## 電源輸出 {#power-output}

CSS106-1G-4P-1S 型號可透過其乙太網埠為外部裝置提供 PoE 供電。這非常方便，因為您無需任何額外的 PoE 注入器即可為其他裝置供電。輸出電壓將與輸入電壓相同。預設情況下設定為 "auto"，因此將任何裝置插入供電埠都是安全的。在此模式下，每個乙太網埠的最大輸出功率為 1 A，所有埠總計 2 A。一旦在 RouterOS 中啟用 Power Output，乙太網 LED 燈會從綠色變為紅色。紅色 LED 表示該埠當前正在提供 PoE 供電。為獲得最佳的 PoE 輸出效能，請使用電源插孔為 CSS 裝置供電。

## 按鈕和跳線 {#buttons-and-jumpers}

在啟動期間按住此按鈕，並在 LED 燈停止閃爍後鬆開，即可重設 SwOS 配置並載入主備份韌體。訪問主韌體可重新安裝主韌體。

請參閱 SwOS 手冊中的[重設](/docs/bridging-and-switching/swos/css106#reset)一節。

## 作業系統支援 {#operating-system-support}

CSS 執行 SwOS，這是此裝置唯一支援的作業系統。更多資訊請參閱 [SwOS 手冊](/docs/bridging-and-switching/swos)。

![](/img/8d9ce79c77ac5eb2.webp)

### GSP 型號 {#gsp-models}

![](/img/8a35955d5856e1f3.webp)

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的有害干擾防護。

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新定向或重新安置接收天線。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 注意：未經合規責任方明確批准的任何更改或修改都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行須符合以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受所收到的任何干擾，包括可能導致執行異常的干擾。注意：本裝置已使用外圍裝置上的遮蔽電纜進行測試。必須使用遮蔽電纜與本裝置配合，以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。其執行須符合以下兩個條件：(1) 本裝置不得造成干擾，且 (2) 本裝置必須接受任何干擾，包括可能導致裝置執行異常的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期資訊以斜槓分隔的形式標示在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位數字），其後兩位數字表示週數。

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

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

歐盟符合性宣告的全文可在以下網際網路地址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
