---
title: "Woobm-USB"
slug: /woobm-usb
source: https://manual.mikrotik.com/hardware/woobm-usb
captured_at: '2026-11-04T10:08:39+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

![](/img/9d412487000cb428.webp)

Woobm 是一款 WiFi 轉序列埠橋接器。該裝置可為具備 USB 埠但沒有無線介面的 RouterBOARD 裝置提供無線訪問能力。該裝置工作在 2GHz 802.11b/g/n 無線模式，支援用戶端模式和接入點模式，並可使用 WPA 無線密碼進行保護（某些型號的賬號和無線密碼請檢視貼紙）。完整規格和宣傳冊請參見 [Woobm-USB 產品頁面](https://mikrotik.com/product/woobm)。

## 供電 {#powering}

該裝置透過 RouterBOARD 裝置的 USB 埠供電。

## 首次啟動 {#first-startup}

將 Woobm-USB 連線到 USB 埠，將會建立一個 SSID 為 WoobmAP 的無線網路。連線到該裝置，並在網頁瀏覽器中開啟裝置 IP 地址。

Woobm-USB 的預設 IP 是 **192.168.4.1**

執行 RouterOS 的裝置會自動掛載為序列 USB 裝置，並在成功登入後提供訪問。

## WEB 介面 {#web-interface}

WEB 介面允許配備了 802.11b/g/n 2.4GHz 無線模組的裝置訪問序列埠。

![](/img/1e9d33617debe666.webp)

Web 介面預設頁面為 "Home"。在主頁上，可以連線並配置 RouterOS 鄰居裝置（同一網路中的 MikroTik 裝置）。點選裝置 IP 地址即可建立連線：

![](/img/44a89aaf00392ae9.webp)

開啟 Terminal 標籤頁後，Woobm-USB 將嘗試模擬 USB 序列介面。若嘗試成功，終端視窗上方將顯示 "Connection successful! " 訊息。你可以透過鍵盤輸入命令，或使用按鍵按鈕透過 USB 序列介面傳送命令。

Show keyboard 會在移動裝置上調出鍵盤。額外按鈕為移動裝置提供缺失的鍵盤按鍵。

開啟 Terminal 標籤頁後，Woobm-USB 將嘗試模擬 USB 序列介面。若嘗試成功，終端視窗上方將顯示 "Connection successful! " 訊息。你可以透過鍵盤輸入命令，或使用按鍵按鈕透過 USB 序列介面傳送命令。

Show keyboard 會在移動裝置上調出鍵盤。額外按鈕為移動裝置提供缺失的鍵盤按鍵。

## 設定 {#settings}

Settings 標籤頁提供 Woobm-USB 裝置的基本配置。**basic settings** 部分提供序列埠、按鈕、LED 和無線常規設定

![](/img/348d8ba4b59b29df.webp)

### 屬性 {#properties}

<table><thead><tr><th>屬性</th><th>說明</th></tr></thead><tbody><tr><td>**Identity** (*string*; 預設：**MikroTik**)</td><td>裝置標識用作 DHCP 用戶端向 DHCP 伺服器上報時的 'hostname' 引數，同時也用於鄰居發現。</td></tr><tr><td>**Telnet port** (*integer*; 預設：**23**)</td><td>用於接收傳入 telnet 請求的埠</td></tr><tr><td>**Baud-rate** (*integer*; 預設：**115200**)</td><td>用於序列通訊的波特率。應與主機裝置匹配。</td></tr><tr><td>**Data bits** (; 預設：**8**)</td><td></td></tr><tr><td>**Parity** (; 預設：**None bits**)</td><td></td></tr><tr><td>**Stopbits** (*integer*; 預設：**1**)</td><td></td></tr><tr><td>**Web conn. timeout** (*integer*; 預設：**2400**)</td><td></td></tr><tr><td>**WPS enabled** (*On/off*; 預設：**On**)</td><td></td></tr><tr><td>**Set the default settings with a button** (*On/off*; 預設：**On**)</td><td></td></tr><tr><td>**Device greeting** (*On/off*; 預設：**On**)</td><td></td></tr><tr><td>**Force echo** (*On/off*; 預設：**On**)</td><td></td></tr><tr><td>**Ignore telnet commands** (*On/off*; 預設：**On**)</td><td></td></tr><tr><td>**Status LEDs enabled** (*On/off*; 預設：**On**)</td><td></td></tr><tr><td>**802.11 mode** (; 預設：**default**)</td><td></td></tr></tbody></table>

**WiFi Station** 設定部分提供 Woobm-USB 在用戶端模式下的無線設定。

![](/img/0ead108ed2f2a68b.webp)

<table><thead><tr><th>屬性</th><th>說明</th></tr></thead><tbody><tr><td>**SSID** (*string*; 預設：)</td><td>提供附近接入點的 SSID，或使用掃描功能。</td></tr><tr><td>**Password** (*string*; 預設：)</td><td>WPA-PSK 和 WPA2-PSK</td></tr><tr><td>**SSID MAC** (*MAC*; 預設：)</td><td></td></tr><tr><td>**Station MAC** (*MAC*; 預設：)</td><td></td></tr><tr><td>**IP address** (*IP*; 預設：)</td><td></td></tr><tr><td>**Gateway** (*IP*; 預設：)</td><td></td></tr><tr><td>**Netmask** (*IP*; 預設：)</td><td></td></tr></tbody></table>

**WiFi AP** 設定部分提供 Woobm-USB 在接入點模式下的無線設定。

![](/img/07ca22adb2460ee2.webp)

<table><thead><tr><th>屬性</th><th>說明</th></tr></thead><tbody><tr><td>**SSID** (*string*; 預設：)</td><td>Woobm-USB 接入點的 SSID</td></tr><tr><td>**Password** (*string*; 預設：)</td><td>WPA-PSK 和 WPA2-PSK</td></tr><tr><td>**Channel** (; 預設：**6**)</td><td>接入點使用的無線通道</td></tr><tr><td>**Auth. mode** (; 預設：)</td><td></td></tr><tr><td>**Hidden** (*On/Off*; 預設：**Off**)</td><td></td></tr><tr><td>**Max conn** (*1 to 4*; 預設：**4**)</td><td>接入點允許的最大用戶端數量。</td></tr><tr><td>**Beacon interval** (*100 to 60000*; 預設：**100**)</td><td>接入點廣播 AP 資訊的頻率。</td></tr><tr><td>**IP address** (*IP*; 預設：**192.168.4.1**)</td><td></td></tr><tr><td>**Gateway** (*IP*; 預設：)</td><td></td></tr><tr><td>**Netmask** (*IP*; 預設：)</td><td></td></tr><tr><td>**AP MAC** (*MAC*; 預設：)</td><td></td></tr><tr><td>**DHCP Enabled** (*On/Off*; 預設：**On**)</td><td>啟用/停用 DHCP 伺服器</td></tr><tr><td>**IP range start** (*IP*; 預設：**192.168.4.2**)</td><td></td></tr><tr><td>**IP range end** (*IP*; 預設：**192.168.4.5**)</td><td></td></tr><tr><td>**IP lease time** (; 預設：**120**)</td><td></td></tr></tbody></table>

## 升級韌體 {#upgrade-firmware}

使用 upgrade firmware 標籤頁進行手動韌體升級。韌體可在我們網頁的 Product Support & Download 部分獲取。

## Telnet 訪問 {#telnet-access}

可以使用 Telnet 用戶端訪問序列埠。要進行 Telnet 訪問，請在 telnet 用戶端中開啟 Woobm-USB 地址。Woobm-USB 會將序列埠轉發給 telnet 用戶端。

只能模擬一個序列埠橋例項。

## 按鈕功能 {#button-functionality}

按鈕提供啟用 WPS、重設配置和傳送鄰居訊息 (MNDP) 的功能。

### WPS 模式 {#wps-mode}

如果按鈕按下時間少於 5 秒，則會啟用 WPS 模式。如果與接入點建立了連線，則會儲存 Woobm 站點配置並覆蓋舊資料。

### 重設配置 {#reset-configuration}

要重設配置：

-

應當拔下 Woobm（從 USB 埠移除）；

-

按住按鈕；

-

在按住按鈕的同時將 Woobm 連線到 USB 埠；

-

等待紅色 LED 燈開始閃爍；

-

鬆開按鈕；

裝置將被重設為預設配置。

#### 鄰居訊息 {#neighbor-message}

鄰居訊息每分鐘自動傳送一次。要手動傳送訊息，請按住按鈕至少 5 秒，直到 LED 燈停止閃爍。

## 作業系統支援 {#operating-system-support}

該裝置僅支援 Woobm 軟體。可透過網頁配置頁面上傳更新的 .BIN 檔案來進行更新。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCCID</th></tr></thead><tbody><tr><td>Woobm-USB</td><td>TV7WBM</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝環境中的有害干擾提供合理保護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不能保證在特定安裝環境中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 向經銷商或有經驗的無線電/電視技術人員尋求幫助。**FCC 警告：** 任何未經合規責任方明確批准的更改或修改都可能導致使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行須滿足以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。本裝置及其天線不得與任何其他天線或發射器共置或聯合執行。本裝置作為從裝置/主裝置 (slave/MASTER) 執行，工作於 2.4 GHz（2412 ~2472 MHz）頻段。**射頻暴露資訊：** 該受測裝置 (EUT) 符合 IC RSS-102 中針對一般人群/非受控暴露限值的 SAR 要求，並已按照 IEEE 1528 規定的測量方法和程式進行測試。安裝和操作本裝置時，輻射體與人體之間的距離至少應保持 20 cm。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>Woobm-USB</td><td>7442A-WBM</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。其執行須滿足以下兩個條件：(1) 本裝置不得造成干擾；(2) 本裝置必須接受任何干擾，包括可能導致裝置執行異常的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。其使用須滿足以下兩個條件：(1) 裝置不得產生干擾；(2) 使用者必須接受裝置所受到的任何無線電干擾，即使該干擾可能影響裝置的正常執行。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合針對非受控環境規定的 IC 輻射暴露限值。安裝和操作本裝置時，輻射體與身體任何部位之間的距離至少應保持 20 cm。Cet équipement est conforme aux limites d'exposition au rayonnement IC définies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé à une distance minimale de 20 cm entre le radiateur et toute partie de votre corps.

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>Частотный диапазон</th><th>Мощность передатчика</th></tr></thead><tbody><tr><td>2412-2472 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用的頻率通道可能因產品型號和認證情況而有所不同。

有關裝置製造日期的資訊，標註在其貼紙上的序列號末尾，以斜槓分隔。第一位數字表示年份編號（年份的最後一位數字），後兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 (Norma Oficial Mexicana) {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2412-2472 MHz (30 dBm)。可用頻率通道可能因產品型號和認證情況而有所不同。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化管理委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2412-2472 MHz (20 dBm)。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置，須按照 NKRZI 2012 年 11 月 1 日第 559 號決議批准、並於 2013 年 1 月 3 日在烏克蘭司法部登記（編號 57/22589）的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

![](/img/9239d51861d9ff00.webp)

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，Woobm-USB 符合 2014/53/EU 指令。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>**頻率範圍（適用於相關型號）**</th><th>**使用的通道**</th><th>**最大輸出功率 (EIRP)**</th><th>**限制**</th></tr></thead><tbody><tr><td>2412 - 2472 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用均無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法的頻率通道、輸出功率、佈線要求以及動態頻率選擇 (DFS) 要求範圍內執行。所有 MikroTik 無線電裝置必須由專業人員安裝！*
