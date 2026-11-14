---
title: "MQS"
slug: /mqs
source: https://manual.mikrotik.com/hardware/mqs
captured_at: '2026-11-04T09:56:27+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

The MQS – Mobile Quick Setup 是一款微型無線裝置，旨在簡化現場的 MikroTik 裝置配置。

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵循所有國家法律法規。裝置的安裝必須符合當地和國家的電氣規範。本裝置設計用於安裝在機架中。開始安裝前，請仔細閱讀安裝說明。未使用正確的硬體或未遵循正確的操作步驟，可能會對人員造成危險並損壞系統。本產品僅供室內安裝。請使本產品遠離水、火、潮溼或高溫環境。僅使用製造商認可的電源和附件，它們可在本產品的原包裝中找到。在將系統連線到電源之前，請閱讀安裝說明。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，風險自負！如果裝置發生故障，請斷開其電源。最快的方法是拔出電源插座上的電源插頭。客戶有責任遵守當地國家法規，包括在合法頻段內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置應與您的身體、職業使用者或公眾保持不小於 20 釐米的距離。

## 快速開始 {#quickstart}

- 透過 USB 為裝置供電，例如使用筆記型電腦或移動電源。
- 在筆記型電腦或智慧手機上，連線到以 "RBMQS" 開頭的 MQS 無線網路。
- 預設情況下，MQS 已在無線介面上啟用 DHCP 伺服器。
- 管理介面的 IP 地址為 192.168.88.3。以避免與其他 MikroTik 裝置衝突。
- 在網頁瀏覽器中開啟 [https://192.168.88.3](https://192.168.88.3) 開始配置，沒有密碼，使用者名稱為：admin（或者，對於某些型號，請檢視貼紙上的使用者和無線密碼）。
- MQS 沒有 RouterOS 軟體，其配置功能有限。

## LED 指示燈 {#led-indicators}

![](/img/bd620b29224a6a8f.webp)

- 該 LED 顯示 POE 處於活動狀態。
- 顯示乙太網埠的連線處於活動狀態。
- 顯示接入點模式。
- 顯示 station 模式。
- 使用者 LED 表示裝置當前處於出廠韌體，更新後將不再點亮；若要使裝置回到出廠韌體，請在啟動時按住 reset 按鈕，LED 會再次亮起。
- 電源 LED 表示裝置正在接收供電。

## 安裝 {#mounting}

如有需要，可以使用紮帶穿過裝置背面的開口進行固定，或使用隨附的綁帶，或使用壁掛支架。本裝置的 IP 防護等級為 IPX0。為符合健康法規，安裝和使用本裝置時應與身體保持至少 20cm 的距離。

## 供電 {#powering}

- MicroUSB 埠接受 5 V 供電。
- 乙太網埠接受無源 PoE 12-28 V DC 供電（需補償線纜損耗，因此建議高於 12 V）。最大負載下的功耗可達 7 W，無連線附件時為 1 W。

### 連線到 PoE 介面卡 {#connecting-to-a-poe-adapter}

- 將裝置的乙太網線連線到 POE 介面卡的 POE+DATA 埠。
- 將來自本地網路（LAN）的乙太網線連線到 POE 介面卡。
- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 配置 {#configuration}

我們建議從這裡開始熟悉各項功能：[https://mt.lv/help](https://mt.lv/help) WinBox 和 MikroTik 移動應用可透過 MQS 配置其他裝置。MQS 本身只能在網頁介面中配置。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

- 內建 2 GHz 無線接入點模組，支援 AP/station/bridge/p2p 模式。板載內建 PIF 天線。
- 一個 10/100 乙太網埠，支援自動交叉/直通線纜糾正（Auto MDI/X）。連線其他網路裝置時可以使用直通線或交叉線。乙太網埠接受 12-28 V DC 供電，並且能夠輸出 POE。
- 一個 micro-USB 2.0 埠，僅用於供電。

## 按鈕和跳線 {#buttons-and-jumpers}

### 復位按鈕 {#reset-button}

在啟動期間按住此按鈕，可將軟體和韌體恢復為出廠設定。

### 模式按鈕 {#mode-button}

預設情況下，MQS 會以 AP 模式啟動；如果在啟動期間按住此按鈕，MQS 將以 station 模式啟動。這些模式可透過 quick-set 選單進行調整。

## 配件 {#accessories}

包裝中包含以下隨裝置提供的附件：

- USB A 公頭直頭轉 Micro USB 公頭扁平線纜，L=100 mm，無資料引腳。
- 魔術貼綁帶 16x300 mm（帶橡膠背襯）。
- 塑膠紮帶 4.8 mm（寬），157 mm（長），尼龍，黑色。
- K-33 緊固套件。
- MQS 安裝支架。

## 規格 {#specifications}

如需瞭解有關本產品的更多資訊、規格和圖片，請訪問我們的網頁：[https://mikrotik.com/product/mqs](https://mikrotik.com/product/mqs)

## 升級 {#upgrading}

為使裝置保持最新狀態，請訪問我們 MQS 產品的支援與下載部分，並檢查最新的軟體版本：

- 訪問 [https://mikrotik.com/product/mqs#fndtn-downloads](https://mikrotik.com/product/mqs#fndtn-downloads)
- 下載韌體 "MQS current release"；
- 使用網頁瀏覽器連線到 MQS；
- 選擇 Upgrade 標籤頁；
- 點選 "Choose File" 按鈕並瀏覽到已下載的檔案；
- 點選 Upgrade 按鈕並等待設定完成。

## 聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCCID</th></tr></thead><tbody><tr><td>RBMQS</td><td>TV7MQS</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限值要求。這些限值旨在為住宅安裝中的有害干擾提供合理防護。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），則建議使用者嘗試透過以下一種或多種措施來消除干擾：

- 重新調整接收天線的方向或位置。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以尋求幫助。**FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能使使用者失去操作本裝置的許可權。本裝置符合 FCC 規則第 15 部分。其執行需滿足以下兩個條件：（1）本裝置不得造成有害干擾，且（2）本裝置必須接受任何接收到的干擾，包括可能導致意外執行的干擾。本裝置及其天線不得與任何其他天線或發射器共址或聯合執行。

**重要：射頻輻射暴露。** 本裝置符合 FCC 針對非受控環境規定的射頻輻射暴露限值。安裝和操作本裝置時，輻射體與身體任何部位之間應保持至少 20 cm 的距離。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>RBMQS</td><td>7442A-MQS</td></tr></tbody></table>

本裝置符合加拿大工業部免許可 RSS 標準。其執行須滿足以下兩個條件：（1）本裝置不得造成干擾，且（2）本裝置必須接受任何干擾，包括可能導致裝置意外執行的干擾。本裝置符合加拿大工業部適用於免許可無線電裝置的 CNR 標準。其使用須滿足以下兩個條件：（1）裝置不得產生干擾，且（2）使用者必須接受裝置受到的任何無線電干擾，即使該干擾可能影響其正常執行。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

**重要：射頻輻射暴露。** 本裝置符合 IC 針對非受控環境規定的輻射暴露限值。安裝和操作本裝置時，輻射體與身體任何部位之間應保持至少 20 cm 的距離。本裝置符合 IC 針對非受控環境規定的輻射暴露限值。安裝和操作本裝置時，輻射體與身體任何部位之間應保持至少 20 cm 的距離。

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

<table><thead><tr><th>頻率範圍</th><th>發射功率</th></tr></thead><tbody><tr><td>2400-2483.5 МГц</td><td>≤100 мВт</td></tr></tbody></table>

*可用頻段可能因產品型號和認證而異。

裝置生產日期資訊以斜槓分隔的形式標註在其標籤上序列號的末尾。第一位數字表示年份編號（年份的最後一位），隨後的兩位數字表示週數。

製造商：MikroTikls SIA，Aizkraukles iela 23, Riga, LV-1006, 拉脫維亞，[support@mikrotik.com](mailto:support@mikrotik.com)。中國、拉脫維亞或立陶宛製造。請見包裝。

有關保修服務的詳細資訊，請聯絡您的經銷商。MikroTik 產品在俄羅斯聯邦的進口商資訊：[https://mikrotik.com/buy/europe/russia](https://mikrotik.com/buy/europe/russia)

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## 墨西哥官方標準 {#norma-oficial-mexicana}

頻率範圍（最大輸出功率）：2400-2483.5 MHz (30 dBm)。可用頻道可能因型號和產品認證而異。

能源效率符合 NOM-029-ENER-2017。

本裝置的執行須符合以下兩個條件：

- 本裝置或裝置可能不會造成有害干擾，並且。
- 本裝置必須接受任何干擾，包括可能導致其執行不正常的干擾。製造商：MikroTikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia。

原產國：拉脫維亞；立陶宛；中國（人民共和國）；美國；墨西哥。

如有特定地區的問題，請聯絡當地經銷商。進口商列表可在我們的主頁上找到 – [https://mikrotik.com/buy/latinamerica/mexico](https://mikrotik.com/buy/latinamerica/mexico)。

## 烏克蘭國家通訊與資訊化監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

工作頻率（最大輸出功率）：2400-2483.5 МГц（20 дБм）。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

在烏克蘭使用本裝置，須按照 НКРЗІ 2012 年 11 月 1 日第 559 號決議（於 2013 年 1 月 3 日在烏克蘭司法部登記，登記號 57/22589）批准的程式取得使用許可。

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，RBMQS 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 頻段使用條款 {#frequency-bands-terms-of-use}

<table><thead><tr><th>頻率範圍（適用於相關型號）</th><th>使用的通道</th><th>最大輸出功率（EIRP）</th><th>限制</th></tr></thead><tbody><tr><td>2400-2483.5 MHz</td><td>1 - 13</td><td>20 dBm</td><td>在所有歐盟成員國使用無任何限制</td></tr></tbody></table>

** 客戶有責任遵守當地國家法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝！*
