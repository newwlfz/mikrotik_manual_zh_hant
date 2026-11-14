---
title: "CRS125-24G-1S 系列"
slug: /crs125-24g-1s-series
source: https://manual.mikrotik.com/hardware/crs125-24g-1s-series
captured_at: '2026-11-04T09:46:06+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/16ae7547ab1e2421.webp)

![](/img/ede41f114aaf4c55.webp)

:::info 本文涵蓋

- **CRS125-24G-1S-IN**
- **CRS125-24G-1S-2HnD-IN**
:::

## 首次使用 {#first-use}

可以透過 IP 192.168.88.1 訪問裝置，使用者名稱為 admin，密碼為空（某些型號請檢視貼紙上的使用者名稱和無線密碼）。請使用 Web 瀏覽器連線此 IP 地址進行配置。有關連線和配置指南，請參閱本頁面：[RouterOS 文件](/docs/introduction) 裝置已預裝 RouterOS，可直接使用。裝置相容 RouterOS v6 及更高版本。對於無線型號 CRS125-24G-1S-2HnD-IN，埠已交換，無線介面和交換器已橋接，並且網橋中包含 DHCP 伺服器。Eth1 和 SFP1 已配置 DHCP 用戶端。連線後請選擇您所在的國家/地區，以應用該國家/地區的法規設定。

- 點選“檢查更新”按鈕將裝置更新到 v6.46 或最新 RouterOS 軟體，以確保最佳效能和穩定性。裝置需要具有可用的網際網路連線。
- 要手動更新裝置，請訪問我們的下載頁面 [https://mikrotik.com/download](https://mikrotik.com/download)
- 選擇您的架構（ARM），並從任意通道下載最新軟體包到您的 PC。
- 開啟 WinBox，在 Files 選單中上傳軟體包。
- 重啟裝置。
- 更新軟體可確保獲得最新的安全修復和當地法律規定的法規要求。
- 設定密碼以保護裝置。

## 供電 {#powering}

裝置接受直流輸入電源插孔：10-28 V（包裝內附 24 V0.8 A PSU）。最大負載下的功耗可達 20 W。

## 配置 {#configuration}

登入後，我們建議點選 QuickSet 選單中的“檢查更新”按鈕，因為將 RouterOS 軟體更新到最新版本可確保最佳效能和穩定性。對於無線型號，請確保已選擇裝置將使用所在的國家/地區，以符合當地法規。RouterOS 除了本文件所述內容外，還包含許多配置選項。我們建議從這裡開始，以熟悉各種可能性：[https://mt.lv/help](https://mt.lv/help) 如果無法使用 IP 連線，可以使用 WinBox 工具（[https://mt.lv/winbox](https://mt.lv/winbox)）從 LAN 側連線到裝置的 MAC 地址（預設情況下，來自 Internet 埠的所有訪問均被阻止）。出於恢復目的，可以從網路啟動裝置，請參閱相關章節。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 二十四個（24）10/100/1000（千兆）乙太網埠（Auto MDI/X）
- CRS125 有一個 SFP 插槽，相容 1.25G SFP 模組。
- CRS125-24G-1S-2HnD-IN 內建 802.11b/g/n 2GHz 無線接入點。

## 復位按鈕 {#reset-button}

routerBOOT 復位按鈕具有以下功能。按住按鈕並通電，然後：

- 當綠色 LED 開始閃爍時鬆開按鈕，可將 RouterOS 配置重設為預設值。
- 當 LED 變為常亮綠色時鬆開按鈕，可清除所有配置和預設值。
- 當 LED 不再亮起（約 20 秒）後鬆開按鈕，可使裝置查詢 Netinstall 伺服器（透過網路安全重灌 RouterOS 時需要）。無論使用上述哪種選項，如果在裝置通電前按下按鈕，系統都會載入備份 RouterBOOT 載入程式。這可用於 RouterBOOT 偵錯和恢復。

## 作業系統支援 {#operating-system-support}

裝置支援版本號等於或高於 RouterOS 選單 /system resource 中所指示版本的 RouterOS 軟體。其他作業系統尚未測試。

## 安全宣告 {#safety-notice}

![](/img/7ef0e65b341a324c.webp)

電擊危險。本裝置只能由經過培訓的人員進行維修。這是 A 類裝置，在住宅無線電裝置附近操作可能會造成無線電干擾。

![](/img/9f19426565d1f529.webp)

CRS125-24G-1S-IN：

![](/img/03ee8c1f12d35999.webp)

![](/img/1ed1d278d5e61c9c.webp)

聯邦通訊委員會干擾宣告 FCC ID:TV7CRS109-8G2HND 本裝置已透過測試，符合 FCC 規則第 15 部分對 A 類數字裝置的限制。這些限制旨在為住宅安裝提供合理保護，防止有害干擾。本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則建議使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增加裝置與接收器之間的間隔。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。FCC 警告：未經合規責任方明確批准的任何更改或修改，可能會使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。操作須滿足以下兩個條件：(1) 本裝置不得造成有害干擾，且 (2) 本裝置必須接受收到的任何干擾，包括可能導致意外操作的干擾。本裝置及其天線不得與其他任何天線或發射器共存或一起操作。重要：射頻輻射暴露。本裝置符合 FCC 針對不受控環境規定的射頻輻射暴露限制。安裝和操作本裝置時，輻射器與您身體任何部位之間的最小距離應為 20 cm。

### CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

<table><thead><tr><th>*BG*</th><th>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/ЕС 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</th></tr></thead><tbody><tr><td>CS</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DA</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>DE</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EL</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/ΕΕ 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>EN</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ES</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>ET</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EL 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FI</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>FR</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HR</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>HU</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IT</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>IS</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LT</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/ES 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>LV</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/ES 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>MT</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NL</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>NO</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PL</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>PT</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>RO</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/UE 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SK</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EÚ 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SL</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr><tr><td>SV</td><td>Mikrotīkls SIA 特此宣告，此型別無線電裝置 RouterBOARD 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)</td></tr></tbody></table>

### MPE 宣告 {#mpe-statement}

本裝置符合針對不受控環境規定的歐盟輻射暴露限制。除非本檔案第 1 頁另有明確說明，否則安裝和操作本裝置時，輻射器與您身體之間的最小距離應為 20 cm。在 RouterOS 中必須指定您所在的國家/地區，以確保遵守當地無線法規。

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相關型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2412-2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國均可無限制使用</td></tr><tr><td>5150-5250 MHz</td><td>26 - 48</td><td>23 dBm</td><td>僅限室內使用*</td></tr><tr><td>5250-5350 MHz</td><td>52 - 64</td><td>20 dBm</td><td>僅限室內使用*</td></tr><tr><td>5470-5725 MHz</td><td>100 - 140</td><td>27 dBm</td><td>在所有歐盟成員國均可無限制使用</td></tr></tbody></table>

** 客戶有責任遵守當地國家/地區法規，包括在合法頻率通道、輸出功率、布纜要求以及動態頻率選擇（DFS）要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝！*

![](/img/984ad54320693690.webp)

***BG. 說明書**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-bg](https://mt.lv/help-bg)* ***CS. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-cs](https://mt.lv/help-cs)* ***DA. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-da](https://mt.lv/help-da)* ***DE. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-de](https://mt.lv/help-de)* ***EL. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-el](https://mt.lv/help-el)* ***EN. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help](https://mt.lv/help)* ***ES. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-es](https://mt.lv/help-es)* ***ET. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-et](https://mt.lv/help-et)* ***FI. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-fi](https://mt.lv/help-fi)* ***FR. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-fr](https://mt.lv/help-fr)* ***HR. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-hr](https://mt.lv/help-hr)* ***HU. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-hu](https://mt.lv/help-hu)* ***IT. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-it](https://mt.lv/help-it)* ***IS. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-is](https://mt.lv/help-is)* ***NO. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-no](https://mt.lv/help-no)* ***LT. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-lt](https://mt.lv/help-lt)* ***LV. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-lv](https://mt.lv/help-lv)* ***MT. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-mt](https://mt.lv/help-mt)* ***NL. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-nl](https://mt.lv/help-nl)* ***PL. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-pl](https://mt.lv/help-pl)* ***PT. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-pt](https://mt.lv/help-pt)* ***RO. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-ro](https://mt.lv/help-ro)* ***SK. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-sk](https://mt.lv/help-sk)* ***SL. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-sl](https://mt.lv/help-sl)* ***SV. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-sv](https://mt.lv/help-sv)* ***NO. 使用說明**: 連線電源介面卡以開啟裝置。在網頁瀏覽器中開啟 192.168.88.1 以配置產品。更多資訊請見* \{*\}\{+\}[https://mt.lv/help-no](https://mt.lv/help-no)*

- **RU. 使用說明**: 連線電源介面卡以開啟裝置。在您的網頁瀏覽器中開啟 192.168.88.1 進行配置。更多資訊* \{*\}\{+\}[https://mt.lv/help-ru](https://mt.lv/help-ru)* ***CN. 說明書。*** *連線電源介面卡以開啟裝置。 在Web瀏覽器中開啟192.168.88.1進行配置。 有關*\{*\}\{+\}[https://mt.lv/help-zh](https://mt.lv/help-zh)* *的更多資訊*
