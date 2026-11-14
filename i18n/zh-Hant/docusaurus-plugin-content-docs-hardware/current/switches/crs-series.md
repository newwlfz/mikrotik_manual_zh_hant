---
title: "CRS 系列"
slug: /crs-series
source: https://manual.mikrotik.com/hardware/crs-series
captured_at: '2026-11-04T09:45:44+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/7da2e3c29d053a0a.webp)

![](/img/ef6feece3b9368b4.webp)

:::info 本文涵蓋

- **CRS109-8G-1S-2HnD-IN**
- **CRS112-8G-4S-IN**
- **CRS210-8G-2S+IN**
- **CRS212-1G-10S-1S+IN**
:::

CRS 是一款高度可配置的交換器，由 RouterOS 驅動。

## 首次使用 {#first-use}

- 安裝裝置或將其放置在平坦表面上，具體說明請參見相關段落。
- 選擇您的供電方案，可選方式請參見相關章節。
- 首次連線必須使用乙太網線，透過 MikroTik WinBox 工具完成。
- 使用 WinBox 從任意埠連線到預設 IP 地址 192.168.88.1，使用者名稱為 admin，密碼為空，裝置已設定為交換器模式（對於某些型號，請檢視標籤上的使用者和無線密碼）。
- 點選 “Check for updates” 按鈕將裝置更新到 v6.46 或最新的 RouterOS 軟體，以確保最佳效能和穩定性。裝置需要具有可用的網際網路連線。
- 如需手動更新裝置，請訪問我們的下載頁面 [https://mikrotik.com/download](https://mikrotik.com/download)
- 選擇您的架構（MIPSBE），並從任意通道下載最新的軟體包到您的 PC。
- 開啟 WinBox，在 Files 選單中上傳軟體包。
- 重啟裝置。
- 更新軟體可確保獲得最新的安全修復，並符合當地法律規定的各項要求。
- 選擇您所在的國家/地區。
- 設定您的密碼以保護裝置安全。

## 供電 {#powering}

這些裝置可透過以下方式供電：

- 直接輸入電源插孔：8-56V（隨附 24V 0.8A 電源介面卡），
- 無源 PoE 輸入：8-56V（隨附註入器）。CRS212-1G-10S-1+IN 除外，該型號僅接受 8-30V 直接輸入，不支援 PoE 輸入

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 除 CRS212 外：八個（8）10/100/1000（千兆）乙太網埠（Auto MDI/X）。
- CRS109：一個 SFP 籠，相容 1.25G SFP 模組，內建 802.11b/g/n 2GHz 無線接入點。
- CRS112：四個 SFP 籠，相容 1.25G SFP 模組。
- CRS210：兩個 SFP+ 籠，SFP+1 相容 1.25G 和 10G，SFP+2 僅相容 10G SFP 模組。
- CRS212：十個 SFP 籠、一個 SFP+ 籠、一個千兆乙太網埠。該裝置配備一個 RJ45 序列埠，預設設定為 115200bit/s、8 個數據位、1 個停止位、無校驗。可使用標準 RJ45 轉 COM 線纜，引腳定義請參見 [Serial Console 手冊](/docs/management-tools/serial-console#rj45-type-serial-port)

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的 “Check for updates” 按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳的效能和穩定性。對於無線型號，請確保已選擇裝置將要使用的國家/地區，以符合當地法規。除本文件所述內容外，RouterOS 還包含許多配置選項。我們建議從此處開始熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法建立 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路引導裝置，請參見 “Reset button” 章節。

## 預設配置 {#default-configuration}

- CRS109-8G-1S-2HnD-IN：埠 2-8 處於交換狀態，無線介面與交換器已橋接，並且橋中包含 DHCP 伺服器。Eth1 和 SFP1 已配置 DHCP 用戶端。
- 所有其他型號的所有埠均處於交換狀態。這兩種型號均可透過 IP 192.168.88.1 訪問，使用者名稱為 admin，沒有密碼。請使用 Web 瀏覽器連線此 IP 地址進行配置。連線和配置指南請參見此頁面：[RouterOS 文件](/docs/introduction)

## Reset 按鈕 {#reset-button}

Reset 按鈕具有三項功能：

• 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置恢復為預設值。 • 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置並恢復預設值。 • 在 LED 熄滅（約 20 秒）後鬆開按鈕，可使裝置搜尋 Netinstall 伺服器（透過網路重新安裝 RouterOS 時需要）。

無論使用上述哪種方式，如果在裝置通電前按下按鈕，系統將載入備份的 RouterBOOT 載入程式。適用於 RouterBOOT 偵錯和恢復。

## 作業系統支援 {#operating-system-support}

裝置支援版本號等於或高於 RouterOS 選單 /system resource 中所指示版本的 RouterOS 軟體。其他作業系統尚未經過測試。

## 注意事項 {#notice}

- 5.470-5.725 GHz 頻段不允許用於商業用途。
- 如果 WLAN 裝置的工作範圍與上述規定不同，則需要將製造商/供應商提供的定製韌體版本應用於終端使用者裝置，並防止終端使用者重新配置。
- 戶外使用：終端使用者需要獲得 NTRA 的批准/許可。
- 任何裝置的資料手冊均可在製造商官方網站上獲取。
- 序列號末尾帶有 “EG” 字母的產品，其無線頻率範圍限制為 2.400 – 2.4835 GHz，發射功率限制為 20dBm（EIRP）。
- 序列號末尾帶有 “EG” 字母的產品，其無線頻率範圍限制為 5.150 – 5.250 GHz，發射功率限制為 23dBm（EIRP）。
- 序列號末尾帶有 “EG” 字母的產品，其無線頻率範圍限制為 5.250 – 5.350 GHz，發射功率限制為 20dBm（EIRP）。

請確保裝置具有鎖定軟體包（來自制造商的韌體版本），該軟體包必須應用於終端使用者裝置，以防止終端使用者重新配置。產品將標有國家程式碼 “-EG”。為確保符合當地主管機構的規定，此裝置需要升級到最新版本！終端使用者有責任遵守當地國家/地區的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線裝置必須由專業人員安裝。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

FCC ID：TV7CRS109-8G2HND 本裝置經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制要求。這些限制旨在為住宅安裝環境中的有害干擾提供合理保護。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則建議使用者嘗試透過以下一種或多種措施來糾正干擾： • 重新調整接收天線的方向或位置。 • 增加裝置與接收器之間的間距。 • 將裝置連線到與接收器所連線電路不同的插座上。 • 諮詢經銷商或有經驗的無線電/電視技術人員尋求幫助。FCC 警告：任何未經合規責任方明確批准的更改或修改都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分的規定。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。本裝置及其天線不得與任何其他天線或發射器位於同一位置或聯合執行。重要提示：射頻輻射暴露。本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。安裝和操作本裝置時，散熱器與您身體任何部位之間的最小距離應為 20 cm。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

<table><thead><tr><th>*BG*</th><th>С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение RouterBOARD е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: [https://mikrotik.com/products](https://mikrotik.com/products)</th></tr></thead><tbody><tr><td>CS</td><td>Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení RouterBOARD je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DA</td><td>Hermed erklærer Mikrotīkls SIA , at radioudstyrstypen RouterBOARD er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DE</td><td>Hiermit erklärt Mikrotīkls SIA , dass der Funkanlagentyp RouterBOARD der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EL</td><td>Με την παρούσα ο/η Mikrotīkls SIA , δηλώνει ότι ο ραδιοεξοπλισμός RouterBOARD πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EN</td><td>Mikrotīkls SIA 特此宣告，無線電裝置型別 RouterBOARD 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ES</td><td>Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico RouterBOARD es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ET</td><td>Käesolevaga deklareerib Mikrotīkls SIA , et käesolev raadioseadme tüüp RouterBOARD vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FI</td><td>Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi RouterBOARD on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FR</td><td>Le soussigné, Mikrotīkls SIA , déclare que l'équipement radioélectrique du type RouterBOARD est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HR</td><td>Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa RouterBOARD u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HU</td><td>Mikrotīkls SIA igazolja, hogy a RouterBOARD típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IT</td><td>Il fabbricante, Mikrotīkls SIA , dichiara che il tipo di apparecchiatura radio RouterBOARD è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IS</td><td>Hér með lýsir Mikrotīkls SIA því yfir að RouterBOARD er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU.Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LT</td><td>Aš, Mikrotīkls SIA , patvirtinu, kad radijo įrenginių tipas RouterBOARD atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LV</td><td>Ar šo Mikrotīkls SIA deklarē, ka radioiekārta RouterBOARD atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>MT</td><td>B'dan, Mikrotīkls SIA , niddikjara li dan it-tip ta' tagħmir tar-radju RouterBOARD huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NL</td><td>Hierbij verklaar ik, Mikrotīkls SIA , dat het type radioapparatuur RouterBOARD conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NO</td><td>Mikrotīkls SIA erklærer herved at utstyret RouterBOARD er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PL</td><td>Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego RouterBOARD jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PT</td><td>O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio RouterBOARD está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>RO</td><td>Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio RouterBOARD este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SK</td><td>Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu RouterBOARD je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SL</td><td>Mikrotīkls SIA potrjuje, da je tip radijske opreme RouterBOARD skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SV</td><td>Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning RouterBOARD överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: [https://mikrotik.com/products](https://mikrotik.com/products)</td></tr></tbody></table>

![](/img/984ad54320693690.webp)

**BG. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-bg](https://mt.lv/help-bg)

**CS. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-cs](https://mt.lv/help-cs)

**DA. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-da](https://mt.lv/help-da)

**DE. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-de](https://mt.lv/help-de)

**EL. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-el](https://mt.lv/help-el)

**EN. 說明書**：連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 進行配置。更多資訊請參見 \{+\}[https://mt.lv/help](https://mt.lv/help)

**ES. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-es](https://mt.lv/help-es)

**ET. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-et](https://mt.lv/help-et)

**FI. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-fi](https://mt.lv/help-fi)

**FR. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-fr](https://mt.lv/help-fr)

**HR. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-hr](https://mt.lv/help-hr)

**HU. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-hu](https://mt.lv/help-hu)

**IT. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-it](https://mt.lv/help-it)

**IS. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-is](https://mt.lv/help-is)

**NO. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-no](https://mt.lv/help-no)

**LT. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-lt](https://mt.lv/help-lt)

**LV. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-lv](https://mt.lv/help-lv)

**MT. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-mt](https://mt.lv/help-mt)

**NL. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-nl](https://mt.lv/help-nl)

**PL. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-pl](https://mt.lv/help-pl)

**PT. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-pt](https://mt.lv/help-pt)

**RO. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-ro](https://mt.lv/help-ro)

**SK. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-sk](https://mt.lv/help-sk)

**SL. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-sl](https://mt.lv/help-sl)

**SV. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-sv](https://mt.lv/help-sv)

**NO. 說明**: 連線電源介面卡以開啟裝置。在 Web 瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請參閱 \{+\}[https://mt.lv/help-no](https://mt.lv/help-no)

**RU. Руководство по эксплуатации**: подключите адаптер питания чтобы включить устройство. Откройте 192.168.88.1 в своем веб-браузере для конфигурации. Дополнительная информация [https://mt.lv/help-ru](https://mt.lv/help-ru) **CN. 說明書。** 連線電源介面卡以開啟裝置。 在Web瀏覽器中開啟192.168.88.1進行配置。 有關\{+\}[https://mt.lv/help-zh](https://mt.lv/help-zh)

的更多資訊
