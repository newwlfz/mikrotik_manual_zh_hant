---
title: "TG-BT5-IN"
slug: /tg-bt5-in
source: https://manual.mikrotik.com/hardware/tg-bt5-in
captured_at: '2026-11-04T10:05:47+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可作為 <a href="/assets/files/tg-bt5-in-c808773bd63bcc571c9cefe268e5bc79.pdf" target="_blank" rel="noopener">PDF 檔案</a> 下載。

![](/img/36aaff792f3485db.jpg)

TG-BT5-IN 是一款即用型藍牙標籤，預裝了電池。您可以在 [https://mikrotik.com/products](https://mikrotik.com/products) 的“支援”和“下載”部分中各產品頁面下找到軟體手冊。完整規格和宣傳冊請參見 [TG-BT5-IN 產品頁面](https://mikrotik.com/product/tg_bt5_in)。

## 軟體相關連結 {#software-related-links}

您可以透過以下連結找到使用 Android 應用程式配置該標籤的指南：

適用於 Android 裝置的 MikroTik Beacon Manager

您可以透過以下連結找到使用 iOS 應用程式配置該標籤的指南：

適用於 iOS 裝置的 MikroTik Beacon Manager

您可以透過以下連結找到有關該標籤廣播格式的更多資訊：

MikroTik 標籤廣播格式

## 室內細長矩形外形 - TG-BT5-IN {#indoor-slim-rectangular-shape---tg-bt5-in}

![](/img/e6632e6a533f4d0f.webp)

- 溫度範圍 -20..+60°C。
- 內建加速度計。
- 磁鐵啟用。
- 尺寸 35x22x7mm。
- BLE 5.2，採用 Silabs BG22。
- 防風雨（密封）版本，內建不可更換的 LiMnO2 CR2032（220mAh）電池。

## 安全警告 {#safety-warnings}

- 在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。
- 本產品的最終處置應遵循所有國家法律和法規。
- 裝置的安裝必須符合當地和國家的電氣規範。
- 本產品設計用於室內安裝。請使本產品遠離水、火、潮溼或高溫環境。
- 僅使用製造商認可的電源和附件，這些電源和附件可在本產品的原始包裝中找到。
- 我們無法保證因不當使用裝置而不會發生事故或損壞。請小心使用本產品，並自行承擔操作風險！
- 如果裝置發生故障，請斷開其電源。最快的方法是將電源插頭從電源插座中拔出。
- 客戶有責任遵守當地國家的法規，包括在合法頻率通道內執行、輸出功率、佈線要求以及動態頻率選擇（DFS）要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

**射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境所規定的輻射暴露限值。本 MikroTik 裝置安裝和執行時，應與您的身體、職業使用者或公眾保持不少於 20 釐米的距離。

## 概述 {#overview}

TG-BT5-IN 是我們 MikroTik 裝置系列的新成員。它是一款藍牙標籤（一個非常小的裝置），可以附著在其他裝置或其他物品上。藍牙標籤在 IoT 拓撲中發揮著重要作用，其中藍牙用於在短距離內廣播資料。安裝並配置完成後，標籤會以 iBeacon、Eddystone 或 MikroTik 遙測（預設封包格式）向閘道器（例如 KNOT）廣播 advertising 封包。而閘道器則利用 MQTT 或 HTTP 協定將 advertising 封包的有效載荷推送到遠端伺服器。

## 標籤模式 {#tag-modes}

產品出廠時處於工廠睡眠模式。在此模式下，所有元件儘可能關閉，MCU 進入最深度的睡眠狀態。電流消耗降至最低，因此這是在標籤存放和/或不使用時首選使用的模式。要退出此模式，請將磁鐵放在標籤邊緣（即“磁性開關”所在位置），並保持 3-10 秒，直到 LED 熄滅。之後，標籤退出睡眠模式並進入廣播模式。

在廣播模式下，標籤會廣播藍牙 advertising 封包。預設情況下，MikroTik 的 advertising 封包每 5 秒傳送一次。這可以在配置模式下更改。

配置模式只能從廣播模式進入，方法是像退出工廠睡眠流程那樣，將磁鐵施加到磁性開關上。施加磁鐵 5-10 秒後，LED 將熄滅，標籤進入配置模式。如果您施加磁鐵的時間超過 15 秒，或者未使用配置應用程式連線到標籤，它將返回廣播模式。

當裝置首次從工廠睡眠中喚醒時，具有以下預設配置：

<table><thead><tr><th>配置引數</th><th>設定/值</th></tr></thead><tbody><tr><td>Advertising 封包格式</td><td>MikroTik</td></tr><tr><td>Advertising 間隔</td><td>5.0 秒</td></tr><tr><td>角度閾值/傾斜觸發</td><td>60°</td></tr><tr><td>自由落體閾值/加速度計觸發</td><td>156.25 mg</td></tr><tr><td>喚醒閾值/喚醒觸發</td><td>1.0 mg</td></tr><tr><td>頻寬濾波器</td><td>0.8 Hz</td></tr><tr><td>低噪聲濾波器</td><td>disabled</td></tr><tr><td>Tx 功率</td><td>0 dBm</td></tr></tbody></table>

磁鐵用於幹簧管，以如上所述更改標籤的工作模式。一旦檢測到磁鐵（幹簧管被啟用），LED 將在接下來的 5 秒內（前 5 秒）開始閃爍，然後停止。這可以幫助您確認 5 秒已經過去，您可以移除磁鐵以進入配置模式。

![](/img/ce5411a28493da0a.webp)

## 初始步驟 {#initial-steps}

安裝“MikroTik Beacon Manager”應用程式並執行該應用。

對於 Android 裝置，您可以透過連結找到它。

- 首次登入時，您將看到附近裝置列表（處於廣播模式或配置模式的裝置）：

![](/img/75cd45d644b39f1a.webp)

要將標籤從工廠睡眠模式“喚醒”，應激活幹簧管 3-10 秒。

- 裝置一旦“喚醒”，就會顯示在“MikroTik Beacon Manager”列表中。選擇該標籤，然後按“CONFIG ONLY”按鈕即可開始配置：

![](/img/ced59977c5443fe5.webp)

![](/img/46257b517e9bdd48.webp)

- 緊接著，您需要將磁鐵放在裝置上方 10 秒（此步驟會將裝置設定為配置模式）：

![](/img/9e85d34e72af9de5.webp)

- 經過短暫準備時間後，裝置應已準備好進行配置：

![](/img/4c13d17f4a24770a.webp)

應用程式將在“Status”標籤頁中顯示有關該標籤的常規資訊，並允許您使用“Settings”標籤頁更改標籤的設定（如上圖所示）。

為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送往指定的廢物處置場所。請了解您所在地區將裝置正確運送到指定處置場所的程式。

## 美國聯邦通訊委員會干擾宣告 {#federal-communication-commission-interference-statement}

<table><thead><tr><th>型號</th><th>FCC ID</th></tr></thead><tbody><tr><td>TG-BT5-IN</td><td>TV7-TB5I</td></tr></tbody></table>

本裝置已經過測試，符合 FCC 規則第 15 部分對 B 類數字裝置的限制。這些限制旨在為住宅安裝提供合理的保護，防止有害干擾。

![](/img/ce6fc3eb10b9a1e6.webp)

本裝置會產生、使用並可能輻射射頻能量，如果未按照說明進行安裝和使用，可能會對無線電通訊造成有害干擾。但是，並不能保證在特定安裝中不會發生干擾。如果本裝置確實對無線電或電視接收造成有害干擾（可透過關閉和開啟裝置來確定），鼓勵使用者嘗試透過以下一種或多種措施來糾正干擾：

- 重新調整或重新放置接收天線。
- 增大裝置與接收器之間的距離。
- 將裝置連線到與接收器所連線電路不同的插座上。
- 諮詢經銷商或有經驗的無線電/電視技術人員以獲取幫助。 **FCC 警告：** 任何未經合規責任方明確批准的更改或修改，都可能導致使用者操作本裝置的許可權失效。

本裝置符合 FCC 規則第 15 部分。操作須符合以下兩個條件：(1) 本裝置不得造成有害干擾；(2) 本裝置必須接受任何接收到的干擾，包括可能導致意外操作的干擾。

注意：本裝置在測試時，外圍裝置使用了遮蔽電纜。必須使用遮蔽電纜連線本裝置以確保合規。

## 加拿大創新、科學與經濟發展部 {#innovation-science-and-economic-development-canada}

<table><thead><tr><th>型號</th><th>IC</th></tr></thead><tbody><tr><td>TG-BT5-IN</td><td>7442A-TB5I</td></tr></tbody></table>

本裝置包含符合加拿大創新、科學與經濟發展部免許可 RSS 的免許可發射器/接收器。操作須符合以下兩個條件：(1) 本裝置不得造成干擾。(2) 本裝置必須接受任何干擾，包括可能導致裝置意外操作的干擾。

本裝置內含的免許可證發射器/接收器符合加拿大創新、科學與經濟發展部（ISED）針對免許可證無線電裝置適用的 CNR 標準。允許在以下兩個條件下執行：1）裝置不得產生干擾；2）裝置必須接受任何接收到的無線電干擾，即使該干擾可能導致裝置執行異常。

本 B 類數字裝置符合加拿大 ICES-003 標準。

本 [B] 類數字裝置符合加拿大 NMB-003 標準。

CAN ICES-003 (B) / NMB-003 (B)

## UKCA 標誌 {#ukca-marking}

![](/img/5d0fc80f851cbbdf.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

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

## 烏克蘭國家通訊和資訊監管委員會 {#the-national-commission-for-the-state-regulation-of-communications-and-informatization-by-ukraine}

製造商：MikroTikls SIA，Brivibas gatve 214i 里加，拉脫維亞，LV1039。

MikroTikls SIA 特此宣告，該路由器符合 2014/53/EC 指令的基本要求及其他相關規定，並且符合烏克蘭內閣 2017 年 5 月 24 日第 355 號決議批准的無線電裝置技術法規的實質性要求。

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## CE 符合性宣告 {#ce-declaration-of-conformity}

製造商：MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

Mikrotīkls SIA 在此宣告，無線電裝置型別 TG-BT5-IN 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

### 藍牙 {#bluetooth}

<table><thead><tr><th>(EN) Operating Frequency / Maximum output power (DE) Betriebsfrequenz / maximale Ausgangsleistung (FR) Fréquence de fonctionnement / puissance de sortie maximale (IT) Frequenza operativa / massima potenza di uscita (ES) Frecuencia de funcionamiento / potencia de salida máxima (RU) Рабочая частота / максимальная выходная мощность</th><th>Bluetooth</th><th>2400-2483.5 MHz / 3.5 dBm</th></tr></thead></table>

**Bluetooth 認證產品

![](/img/cf3c8d2919f980e2.webp)

本產品已成功完成藍牙認證流程。有關藍牙認證產品的更多資訊，請使用以下連結：[https://launchstudio.bluetooth.com/Listings/Search](https://launchstudio.bluetooth.com/Listings/Search)
