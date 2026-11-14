---
title: "Chateau 5G ax"
slug: /chateau-5g-ax
source: https://manual.mikrotik.com/hardware/chateau-5g-ax
captured_at: '2026-11-04T09:45:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/3b205728dd9cd451.webp)

## [Chateau 5G ax](https://mikrotik.com/product/chateau_5g_ax) (S53UG+M-5HaxD2HaxD-TC&RG502Q-EA) {#chateau-5g-ax-s53ugm-5haxd2haxd-tcrg502q-ea}

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。有關完整規格和手冊，請參見 [Chateau 5G ax 產品頁面](https://mikrotik.com/product/chateau_5g_ax)。
- 本產品的最終處置應遵守所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品適用於室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，可在本產品的原始包裝中找到。
- 在將系統連線到電源之前，請閱讀安裝說明。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，風險自負！
- 如果裝置發生故障，請斷開其電源。最快的方法是拔下電源插座上的電源插頭。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和操作位置與您的身體、職業使用者或公眾的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

請按照以下快速步驟設定您的裝置：

![](/img/cbc5361d4144eab4.webp)

- 將外接天線連線到 SMA 介面（天線隨包裝提供，參見“(link)”）；
- 將 micro SIM 卡插入裝置下方的卡槽中；

![](/img/9619076cdc698366.webp)

- 將您的計算機連線到其中一個乙太網埠；
- 將電源介面卡連線到 DC 插孔；
- 裝置通電且 PC 已連線到裝置後，在 Web 瀏覽器中開啟 [https://192.168.88.1](https://192.168.88.1) 開始配置（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）；
- 使用者名稱：a*dmin，**密碼請檢視貼紙**；*
- 您應點選右側的 "Check for updates" 按鈕，將 RouterOS 軟體更新到最新版本，以確保最佳效能和穩定性；必須插入有效的 SIM 卡；
- 如需手動更新裝置，請訪問產品頁面 [https://mikrotik.com/products](https://mikrotik.com/products) 找到您的產品。所需軟體包可在 "Support&Downloads" 選單下獲取；
- 將下載的軟體包上傳到 (**WebFig**) (**Files**) 選單並重啟裝置；
- 將 RouterOS 軟體更新到最新版本可確保最佳效能、穩定性和安全更新；
- 要個性化您的無線網路，可在 "Network Name" 欄位中更改 SSID；
- 在螢幕左側的 "Country" 欄位中選擇您所在的國家/地區，以應用國家/地區法規設定；
- 在 "WiFi Password" 欄位中設定無線網路密碼，密碼長度至少為八個字元；
- 在右下方的 "Password" 欄位中設定路由器密碼，並在 "Confirm Password" 欄位中重複輸入，下次登入時將使用該密碼；
- 選擇 "Apply Configuration" 儲存更改。

## 使用移動應用連線 {#connecting-with-a-mobile-app}

使用智慧手機透過 WiFi 訪問路由器。

![](/img/9bcba09a7b6a0d53.webp)

- 插入 SIM 卡並給裝置通電。
- 掃描二維條碼並選擇您首選的作業系統。
- 安裝並開啟該應用程式。
- 選擇 Connect，透過無線網路建立與裝置的連線（請檢視貼紙上的無線密碼）。
- 使用者名稱為 "**admin**"，沒有密碼（或者，對於某些型號，請檢視貼紙上的使用者名稱和無線密碼）。
- 選擇 Quick Setup，應用程式將通過幾個簡單步驟引導您完成所有基本配置設定。
- 提供高階選單，可用於完整配置所有必要的設定。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/448fe884f3fe7820.webp)

- (link)DC 插孔 2.0 mm。
- 五個千兆埠，支援自動交叉/直通線纜糾正（Auto MDI/X）。直通線或交叉線均可用於連線其他網路裝置。
- USB type-A。
- (link) 用於 Micro sim 卡。
- 模式按鈕。
- 帶天線的型號不提供外接 (link) 的蓋板。
- WPS (link)
- 產品程式碼 S53UG+M-5HaxD2HaxD-TC&RG502Q-EA。
- CPU 四核 IPQ-6010 1.8 GHz。
- CPU 架構 ARM 64bit。
- RAM 大小 1 GB。
- RAM 型別 DDR3L。
- 儲存 128 MB，NAND。
- 1G 乙太網埠數量 4。
- 2.5G 乙太網埠數量 1。
- Micro SIM 卡槽 1。
- USB 1 個 USB 3.0 type A。
- M.2 插槽數量 1。
- 交換晶片型號 IPQ-6010。
- 無線介面型號 QCN-5022 (2.4 GHz)、QCN-5052 (5 GHz)。
- 無線 2.4 GHz 802.11ax 雙鏈、5 GHz 802.11ax 雙鏈。
- LTE 類別 20（下行 2.0 Gbps，上行 200 Mbps）。
- LTE 調變解調器 R11mL-RG502Q-EA。
- TAC 86073604。
- 5G SA 類別 下行 4.2 Gbps，上行 900 Mbps。
- 5G NSA 類別 下行 5.0 Gbps，上行 650 Mbps。
- 3G 類別 R8（下行 42.2Mbps，上行 5.76Mbps）。
- MIMO 下行 4x4 (5G SA FDD)、4x4 (5G NSA FDD)、4x4 (LTE FDD)。
- MIMO 上行 2x2 (5G SA FDD)、1x1 (5G NSA FDD)、1x1 (LTE FDD)。
- 5G SA FDD 頻段 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 7 (2600MHz) / 8 (900 MHz) / 20 (800 MHz) / 28 (700 MHz)。
- 5G SA TDD 頻段 38 (2600MHz) / 40 (2300MHz) / 41 (2500MHz) / 77 (3700 MHz) / 78 (3500 MHz) / 79 (4700 MHz)。
- 5G NSA FDD 頻段 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 7 (2600MHz) / 8 (900 MHz) / 20 (800 MHz) / 28 (700 MHz)。
- 5G NSA TDD 頻段 38 (2600MHz) / 40 (2300MHz) / 41 (2500MHz) / 77 (3700 MHz) / 78 (3500 MHz) / 79 (4700 MHz)。
- LTE FDD 頻段 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 7 (2600MHz) / 8 (900 MHz) / 18 (800 MHz) / 19 (800 MHz) / 20 (800 MHz) / 26 (850MHz) / 28 (700 MHz) / 32 (1500 MHz)。
- LTE TDD 頻段 34 (2000 MHz) / 38 (2600MHz) / 39 (1900MHz) / 40 (2300MHz) / 41 (2500MHz) / 42 (3500MHz) / 43 (3700MHz)。
- 3G 頻段 1 (2100MHz) / 3 (1800MHz) / 5 (850MHz) / 6 (850 MHz) / 8 (900MHz) / 19 (800 MHz)。
- 尺寸 240 x 156 x 44 mm。
- 作業系統 RouterOS v7，許可證級別 4。
- 工作溫度 -40°C 至 +70°C。

## 安裝 {#mounting}

本裝置設計用於室內，可放置在桌面上使用。

您應使用 CAT5 遮蔽網線。使用和安裝本裝置時，請注意最大允許暴露（MPE）安全距離，輻射體與您身體之間的距離至少為 20 cm。

## 供電 {#powering}

- DC 輸入數量 1。
- DC 插孔輸入電壓 12-28 V。
- 電源介面卡標稱電壓 24 V。
- 電源介面卡標稱電流 1.2 A。
- 無附件時的最大功耗為 16 W。
- 最大功耗 19 W。

## 配置 {#configuration}

您應經常檢查更新，以獲取 RouterOS 軟體的最新更新，從而確保最佳效能和穩定性。除了本文件所述內容之外，RouterOS 還包含許多配置選項。我們建議從這裡開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以引導裝置進行重灌，請參見 (link) 章節。

## 模式按鈕 {#mode-button}

模式按鈕位於裝置背面右側。模式按鈕的預設配置為深色模式——關閉所有 LED。可在 RouterOS 中配置該按鈕以執行任何使用者指定的指令碼。

## 同步按鈕 {#sync-button}

同步按鈕位於裝置頂部。如果在無線介面上配置了 WPS Sync 按鈕，可用於連線新用戶端。

![](/img/c76f6511aa4e14f0.webp)

- 按住 WPS 按鈕 1 – 5 秒，即可為無線介面啟用 WPS。

## 前面板 LED 狀態 {#front-led-status}

![](/img/9ba5b3e5c27a0830.webp)

- 無線網路活動。
- 乙太網埠活動。
- 系統 LED。
- 訊號強度。蜂窩連線技術依據系統 LED 顏色判斷：紅色：GSM 黃色：3G 藍色：LTE 綠色：5G NSA 紫色：5G SA

當 LTE 未連線到網路時，系統 LED 會閃爍紅色，表示 LTE 連線存在某些問題。如果 LTE 介面被有意停用（未使用），系統 LED 將發出藍光。

## SIM 卡槽使用 {#sim-slot-usage}

![](/img/a0db691ac4861274.webp)

SIM 卡槽設計用於 Micro SIM 卡。Nano SIM 卡厚度不同，不建議配合轉接卡使用。

## 復位按鈕 {#reset-button}

復位按鈕具有三種功能：

- 在啟動過程中按住此按鈕，直到綠色 LED 開始閃爍，鬆開按鈕即可重設 RouterOS 配置（共 5 秒）。
- 繼續按住 5 秒，LED 變為常亮，此時鬆開即可開啟 CAP 模式。裝置將開始尋找 CAPsMAN 伺服器（共 10 秒）。
- 要使用 Netinstall 實用程式重新安裝 RouterOS，請使裝置進入 BOOTP 模式。有兩種載入程式可用：常規載入程式和備用載入程式。常規載入程式 - 給裝置通電，等待 1-2 秒，然後按住復位按鈕。等待系統 LED 閃爍綠色，然後變為常亮 "On"。當綠色 LED 變為 "Off" 時，鬆開復位按鈕 - 裝置將進入 BOOTP 模式。
- 備用載入程式 – 關閉裝置電源，按住復位按鈕，然後通電。等待系統 LED 閃爍綠色，然後變為常亮 "On"。當綠色 LED 變為 "Off" 時，鬆開復位按鈕 - 裝置將使用備用載入程式進入 BOOTP 模式。無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統都將載入備用 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

Netinstall 執行 Netinstall 時，請確保 ROS 檔案和 Netinstall 軟體均使用最新的 v7 版本。

## 配件 {#accessories}

包裝中包含隨裝置提供的以下配件：

- ADAPT1_ EU/US 開關電源 24V，1.2A。
- CAB3_ CAT5E UTP 扁平網線，8P8C，AWG32，1.5m。

## 天線使用 {#antenna-usage}

SMA 介面用於隨附且已連線的 LTE 天線。

連線天線前請先關閉裝置，否則裝置可能會損壞！

外接天線插孔位於裝置背面。

- 將兩根天線擰到 SMA 插孔上（請遵循圖示中的說明）。

![](/img/7230db2d2f966b3d.webp)

## 拆卸後蓋以接觸 PCB {#removing-back-cover-to-access-pcb}

如果需要接觸 PCB，可以拆下後蓋。

- 拆下中心螺絲；

![](/img/3c40f644b6453592.webp)

- 使用小螺絲刀在標記處撬開背板；
- 繼續向上撬開；

![](/img/ef5c2817560d190a.webp)

- 最後將整塊背板取下。

## 作業系統支援 {#operating-system-support}

本裝置支援 RouterOS v7 及以上版本。具體的出廠安裝版本列於 /system resource 中。其他作業系統尚未經過測試。

為避免汙染環境，請將本裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請了解您所在地區將裝置妥善運送至指定處置場所的相關程式。

### UKCA 標誌 {#ukca-marking}

![](/img/387853c20d5a4c82.gif)

### CE 符合性宣告 {#ce-declaration-of-conformity}

<table><thead><tr><th>BG</th><th>С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение S53UG+M-5HaxD2HaxD-TC&RG502Q-EA е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: [https://mikrotik.com/products](https://mikrotik.com/products)</th></tr></thead><tbody><tr><td>CS</td><td>Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení S53UG+M-5HaxD2HaxD-TC&RG502Q-EA je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DA</td><td>Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen S53UG+M-5HaxD2HaxD-TC&RG502Q-EA er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DE</td><td>Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp S53UG+M-5HaxD2HaxD-TC&RG502Q-EA der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EL</td><td>Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός S53UG+M-5HaxD2HaxD-TC&RG502Q-EA πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EN</td><td>Hereby, Mikrotīkls SIA declares that the radio equipment type S53UG+M-5HaxD2HaxD-TC&RG502Q-EA is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ES</td><td>Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico S53UG+M-5HaxD2HaxD-TC&RG502Q-EA es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ET</td><td>Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp S53UG+M-5HaxD2HaxD-TC&RG502Q-EA vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FI</td><td>Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi S53UG+M-5HaxD2HaxD-TC&RG502Q-EA on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FR</td><td>Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type S53UG+M-5HaxD2HaxD-TC&RG502Q-EA est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HR</td><td>Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa S53UG+M-5HaxD2HaxD-TC&RG502Q-EA u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HU</td><td>Mikrotīkls SIA igazolja, hogy a S53UG+M-5HaxD2HaxD-TC&RG502Q-EA típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IT</td><td>Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio S53UG+M-5HaxD2HaxD-TC&RG502Q-EA è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IS</td><td>Hér með lýsir Mikrotīkls SIA því yfir að S53UG+M-5HaxD2HaxD-TC&RG502Q-EA er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LT</td><td>Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas S53UG+M-5HaxD2HaxD-TC&RG502Q-EA atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LV</td><td>Ar šo Mikrotīkls SIA deklarē, ka radioiekārta S53UG+M-5HaxD2HaxD-TC&RG502Q-EA atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>MT</td><td>B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju S53UG+M-5HaxD2HaxD-TC&RG502Q-EA huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NL</td><td>Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur S53UG+M-5HaxD2HaxD-TC&RG502Q-EA conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NO</td><td>Mikrotīkls SIA erklærer herved at utstyret S53UG+M-5HaxD2HaxD-TC&RG502Q-EA er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PL</td><td>Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego S53UG+M-5HaxD2HaxD-TC&RG502Q-EA jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PT</td><td>O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio S53UG+M-5HaxD2HaxD-TC&RG502Q-EA está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>RO</td><td>Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio S53UG+M-5HaxD2HaxD-TC&RG502Q-EA este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SK</td><td>Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu S53UG+M-5HaxD2HaxD-TC&RG502Q-EA je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SL</td><td>Mikrotīkls SIA potrjuje, da je tip radijske opreme S53UG+M-5HaxD2HaxD-TC&RG502Q-EA skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SV</td><td>Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning S53UG+M-5HaxD2HaxD-TC&RG502Q-EA överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr></tbody></table>

### WLAN/WCDMA/LTE {#wlanwcdmalte}

<table><thead><tr><th>工作頻率 / 最大輸出功率 Betriebsfrequenz / maximale Ausgangsleistung Fréquence de fonctionnement / puissance de sortie maximale Frequenza operativa / massima potenza di uscita Frecuencia de funcionamiento / potencia de salida máxima Рабочая частота / максимальная выходная мощность</th><th>WCDMA I</th><th>1922.4 MHz / 23dBm ± 2.7 dB</th></tr></thead><tbody><tr><td>WCDMA III</td><td>1712.4 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA V</td><td>826.4 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>WCDMA VIII</td><td>882.4 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>WLAN</td><td>2400-2483.5 MHz / 20dBm</td><td></td></tr><tr><td>WLAN</td><td>5150-5250 MHz / 23 dBm</td><td></td></tr><tr><td>WLAN</td><td>5250-5350 MHz / 20 dBm</td><td></td></tr><tr><td>WLAN</td><td>5470-5725 MHz / 27 dBm</td><td></td></tr><tr><td>WLAN</td><td>5725-5825 MHz / 30 dBm</td><td></td></tr><tr><td>LTE Band 1</td><td>2100 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 3</td><td>1800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 5</td><td>850 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 7</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 8</td><td>900 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 20</td><td>800 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 28</td><td>700 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 32</td><td>1500 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 34</td><td>2000 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 38</td><td>2600 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 40</td><td>2300 MHz / 23dBm ± 2.7 dB</td><td></td></tr><tr><td>LTE Band 42</td><td>3500 MHz / 23, 26dBm ± 3 dB</td><td></td></tr><tr><td>LTE Band 43</td><td>3700 MHz / 23dBm ± 3 dB</td><td></td></tr><tr><td>5G NR Band n1</td><td>2100 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n3</td><td>1800 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n7</td><td>2600 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n8</td><td>900 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n20</td><td>800 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n28</td><td>700 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n38</td><td>2600 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n40</td><td>2300 MHz / 23dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n41</td><td>2500 MHz / 26dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n77</td><td>3700 MHz / 26dBm ± 2 dB</td><td></td></tr><tr><td>5G NR Band n78</td><td>3500 MHz / 26dBm ± 2 dB</td><td></td></tr></tbody></table>

本 MikroTik 裝置符合 ETSI 法規規定的最大 TX 功率限制。有關更多詳細資訊，請參見上文的符合性宣告 / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

本裝置的 WLAN 功能在 5150 至 5350 MHz 頻率範圍內工作時僅限於室內使用。 / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.

![](/img/6250b391e18aff84.webp)

<table><thead><tr><th>**（EN）技術規格 / (DE) Technische Spezifikationen / (FR) Spécifications techniques /(IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики：**</th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td>（EN）產品電源輸入選項(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта</td><td>（EN）DC 介面卡輸出規格(DE) Ausgangsspezifikationen des Gleichstromadapters(FR) Spécifications de sortie de l'adaptateur de courant continu(IT) Specifiche di uscita dell'adattatore di corrente continua(ES) Especificaciones de salida del adaptador de corriente continua(RU) Выходные характеристики адаптера постоянного тока</td><td>（EN）外殼 IP 等級(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP</td><td>（EN）工作溫度(DE)Betriebstemperatur (FR) température de fonctionnement (IT) temperatura di esercizio (ES) Temperatura de funcionamiento (RU) Рабочая Температура</td><td></td></tr><tr><td>電壓，V</td><td>電流，A</td><td></td><td></td><td></td></tr><tr><td>DC 插孔（12 - 28 V DC）</td><td>24</td><td>1.5</td><td>IP20</td><td>±0°..+70°C</td></tr></tbody></table>
