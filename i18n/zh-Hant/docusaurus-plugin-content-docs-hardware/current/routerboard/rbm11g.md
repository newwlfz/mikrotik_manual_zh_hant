---
title: "RBM11G"
slug: /rbm11g
source: https://manual.mikrotik.com/hardware/rbm11g
captured_at: '2026-11-04T10:05:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危害，並熟悉防止事故的標準做法。本產品的最終處置應按照所有國家和地方的法律法規進行。將接入點安裝到任何牆面上的所有安裝方法均需獲得當地管轄部門的認可。裝置的安裝必須符合當地和國家的電氣規範。本產品設計用於安裝在室外的立杆上，但也可以在室內安裝。開始安裝前請仔細閱讀安裝說明。未使用正確的硬體和配置，或未遵循正確的操作步驟，可能導致人員處於危險境地並對系統造成損壞。請僅使用製造商認可的電源和配件，這些均可在本產品的原始包裝中找到。在將系統連線到電源之前，請先閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，並自行承擔操作風險！如果裝置出現故障，請將其斷電。最快的方法是將電源插頭從電源插座中拔出。客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置都必須由專業人員安裝。

## 首次使用 {#first-use}

- 插入 miniPCIe 卡（未隨附），請參閱段落 。
- （可選）將裝置安裝到外殼中。
- 將天線線纜連線到 miniPCIe 卡，並將乙太網線纜連線到千兆乙太網埠。
- 插入電源線以開啟裝置。
- 我們建議使用 WinBox 連線到裝置，預設 IP 地址為 192.168.88.1，使用者名稱為 admin，無密碼（或者對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）。

## 安裝 {#mounting}

M11G 路由器供專業使用。每臺裝置均採用 ESD 防護包裝。處理電氣裝置時，請遵守以下安全注意事項：

- 在拆包和處理電氣元件時，請使用腕部接地帶，以避免靜電放電（ESD）損壞。
- 拆包後，請將路由器放置在防靜電墊上。
- 安裝裝置時，請確保沒有可能損壞或接觸 PCB 板的物體。
- 請注意，ETH 和 DC 插孔伸出 PCB 板的邊界。可使用 PCB 板上出廠提供的四個孔（位於裝置每側）將裝置安裝到您想要的位置。

## MiniPCIe 插槽 {#minipcie-slot}

安裝 miniPCIe 模組應由具備資質的人員完成，處理電氣裝置時請遵循安全注意事項：

- 將裝置放置在防靜電墊上。
- 找到 miniPCIe 插槽並拆下出廠時固定的兩顆螺釘。
- 將隨附的厚導熱墊貼到卡上，然後將卡安裝到 miniPCIe 插槽中，使導熱墊位於 PCB 和卡之間。
- 使用先前拆下的兩顆螺釘將卡固定到位。
- 將灰色 uFL 聯結器連線到調變解調器的 MAIN 天線聯結器，將黑色線纜連線到輔助（或 AUX）聯結器。
- 將較薄的導熱墊貼到卡的頂部。
- 將裝置安裝到您想要的位置。安裝好裝置後，請將移動運營商的 SIM 卡晶片朝下插入 SIM 插槽。該插槽支援 miniSIM（2FF）。

## 供電 {#powering}

裝置支援以下供電方式：

- 透過乙太網埠進行無源 10-30 V PoE 供電。長線纜上需要更高的電壓來補償功率損耗。建議至少使用 18 V。
- 透過電源插孔直接輸入 10-30 V。最大功耗 11 W。

## 啟動過程 {#booting-process}

RouterOS 是所有 RouterBOARD 路由器的作業系統。請參閱文件：[https://mt.lv/help](https://mt.lv/help) 除乙太網埠上的 IP 地址外，本裝置未進行任何預配置。必須按照上述連結的文件手冊應用其他配置。初始連線必須透過乙太網線纜，使用 MikroTik WinBox 工具完成。應使用 WinBox 連線到預設 IP 地址 192.168.88.1，使用者名稱為 admin，無密碼。如果您希望從網路啟動裝置，例如使用 MikroTik Netinstall，請在啟動時按住裝置的復位按鈕，直到 LED 燈熄滅，裝置將開始尋找 Netinstall 伺服器。如果無法使用 IP 連線，WinBox 工具也可用於連線到裝置的 MAC 地址。更多資訊請參閱文件。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 一個千兆乙太網埠（支援 Auto MDI/X，因此您可以使用直通線或交叉線連線到其他網路裝置）。該乙太網埠可透過無源 PoE 注入器接受 10-30V DC 供電。
- miniPCIe 插槽，可用於 802.11 無線網路卡或 3G/LTE 調變解調器。SIM 插槽適用於 miniPCIe 3G/LTE 調變解調器，未安裝調變解調器時不具備任何功能。

## 按鈕和跳線 {#buttons-and-jumpers}

RouterBOOT 復位按鈕具有以下功能：

- 在啟動期間按住此按鈕，直到 LED 燈開始閃爍，鬆開按鈕即可復位 RouterOS 配置（總共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開可開啟 CAPs 模式（總共 10 秒）。* 繼續按住按鈕 5 秒，直到 LED 熄滅，然後鬆開，使 RouterBOARD 尋找 Netinstall 伺服器（總共 15 秒）。無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## 規格 {#specifications}

有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/m11g](https://mikrotik.com/product/m11g)

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統未經測試。

## MikroTik 移動應用 {#mikrotik-mobile-app}

![](/img/90ba1c400fce0f3e.webp)

![](/img/25f50553ffd86eaf.webp)

![](/img/8d294e5cd375c591.webp)

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢棄物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的相關程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的保護，防止有害干擾。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉再開啟裝置來確定），建議使用者嘗試透過以下一種或多種措施來糾正干擾：

- 調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以獲得幫助。 **FCC 警告**：未經合規責任方明確批准的任何更改或改裝都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致不良執行的干擾。注：本裝置在測試時外圍裝置使用了遮蔽電纜。必須使用遮蔽電纜以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

本裝置符合加拿大工業部免許可 RSS 標準。其執行須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置執行不正常的干擾。Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置的生產日期資訊在其標籤上序列號的末尾以斜槓分隔表示。第一位數字表示年份編號（年份的最後一位數字），隨後的兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## Norma Oficial Mexicana {#norma-oficial-mexicana}

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV-1039。

歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)
