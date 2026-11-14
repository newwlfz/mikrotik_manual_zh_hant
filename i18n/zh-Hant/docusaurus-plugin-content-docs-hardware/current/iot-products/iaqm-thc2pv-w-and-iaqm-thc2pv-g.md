---
title: "IAQM-THC2PV-W 和 IAQM-THC2PV-G"
slug: /iaqm-thc2pv-w-and-iaqm-thc2pv-g
source: https://manual.mikrotik.com/hardware/iaqm-thc2pv-w-and-iaqm-thc2pv-g
captured_at: '2026-11-04T09:50:39+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本指南可下載為 <a href="/assets/files/iaqm-thc2pv-w-and-iaqm-thc2pv-g-ca07b49c7e0222e093e8d49c300e3b87.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/696eb4898c956f84.webp)

![](/img/f3e057ff78f46097.webp)

IAQM-THC2PV-W（白色）和 IAQM-THC2PV-G（灰色）、IAQM-THC2V-W（白色）和 IAQM-THC2V-G（灰色）、IAQM-THC2P-W（白色）和 IAQM-THC2P-G（灰色）是一款空氣質量感測器裝置，可測量溫度（°C/°F）、相對溼度（RH）、二氧化碳（CO₂），並可選配顆粒物（PM）或揮發性有機化合物（VOC）感測器。

有關完整規格和產品手冊，請參閱 [CLAIRE](https://mikrotik.com/product/claire) 和 [CLAIRE Lite](https://mikrotik.com/product/claire_lite) 產品頁面。

型號命名規則：IAQM-THC2PV-W/G

- IAQM - 室內空氣質量監測器
- T - 溫度 [°C/°F]
- H - 相對溼度 [%]
- C2 - 二氧化碳 [ppm]
- P - 顆粒物 [μg/m3]
- V - 揮發性有機化合物 [VOC 指數]
- W - 白色
- G - 灰色

## 安全警告 {#safety-warnings}

在對任何裝置進行操作之前，請了解與電路相關的危險，並熟悉防止事故的標準做法。本產品的最終處置應遵守所有國家法律和法規。在任何牆面上安裝接入點的所有安裝方式均須獲得當地主管部門的認可。裝置的安裝必須符合當地和國家的電氣規範。本產品僅供室內安裝。請將本產品遠離水、火、潮溼或高溫環境。僅使用製造商認可的電源和配件，它們可在本產品的原包裝中找到。我們建議使用符合 IEC 62368-1 的外部受限電源（LPS）為本裝置供電。僅使用額定為 LPS 的 AC/DC 介面卡，其輸出電壓和電流須與產品上標示的數值相符。我們無法保證因不當使用裝置而不會發生事故或損壞。請謹慎使用本產品，操作風險自負！如果裝置發生故障，請斷開其電源。最快捷的方法是拔下電源插座上的電源插頭。客戶有責任遵守當地國家法規，包括在合法頻段內工作、輸出功率和佈線要求。所有 MikroTik 無線裝置必須由專業人員安裝。為避免汙染環境，請將裝置與生活垃圾分開，並以安全的方式處置，例如送至指定的廢物處置場所。請了解將裝置妥善運送至您所在地區指定處置場所的相關流程。

**射頻輻射暴露：** 本 MikroTik 裝置符合歐盟針對非受控環境設定的輻射暴露限值。本 MikroTik 裝置的安裝和執行位置應與您的身體、職業使用者或公眾保持不小於 20 釐米的距離。

## 概述 {#overview}

符合 Matter 連線標準的空氣質量監測裝置，內建所有必備感測器——二氧化碳（CO₂）、顆粒物感測器（PM2.5 和 PM10）、溫度、相對溼度以及 VOC 感測器。

適用於家庭、辦公室、學校、酒店、養老院或其他公共場所。

## IAQM-THC2PV-W/G {#iaqm-thc2pv-wg}

- **溫度感測器**
範圍 0..+50°C
精度 ±0.5°C（典型值）
- **相對溼度感測器**
範圍 0..100 %RH
精度 ±4%（典型值）
- **CO₂ 感測器**
範圍 400..2000 ppm
精度 ±50.0 ppm ±5.0%
自動自校準（ASC），每週暴露於 400 ppm CO₂ 濃度的空氣中
- **顆粒物 PM2.5 感測器**
範圍 0..1000 μg/m3
精度 ±10%
- **顆粒物 PM10 感測器**
範圍 0..1000 μg/m3
精度 ±25%
- **VOC 感測器**
範圍 1..500 VOC 指數點
變化 ±15%
重複性 ±5%
- Matter 連線：支援，Matter over Thread
- 藍牙®：支援，僅用於簡單的 Matter 配網（裝置設定）
- 顯示屏：2” 全綵顯示屏，帶背光
- 顯示模式：使用者可調節多種預定義顯示模式
- 指示：針對惡化或不健康的空氣提供顏色編碼的視覺警告
- 供電：USB Type-C 插座或用於 LPS 介面卡的 5VDC 端子聯結器
- 整體尺寸：76x76x24mm
- 安裝方式：桌面或壁掛支架，可選安全螺絲
- 相容控制器：Google、Amazon、Apple 支援 Matter 的控制器，可與 Home Assistant App 整合

---

## 初始步驟 {#first-steps}

- 要給裝置開機，請使用隨附的 USB-C 介面卡連線。
- 開機後，請等待最多 10 分鐘讓系統穩定。
- 要更改顯示模式，請按住側邊按鈕 50 ms 至 3 秒。
- 要在 °C 和 °F 之間切換溫度顯示，請按住側邊按鈕 3 秒。選單出現後，短按按鈕一次（50 ms 至 1 s）導航到 Temperature unit 部分。要選擇該部分，請按住按鈕 1 秒。使用短按在攝氏度和華氏度之間切換，並按住按鈕 1 秒確認您的選擇。
- 所有感測器每 10 秒更新一次測量值，但 CO₂ 感測器每 30 秒更新一次，PM 感測器每 5 分鐘更新一次。

有關如何將裝置與相容 Matter over Thread 的智慧家居系統配對的說明，請參閱此處提供的手冊：

掃描二維條碼開啟手冊：[https://mt.lv/claire-help](https://mt.lv/claire-help)

![](/img/5db169fb86344481.png)

## 按鈕操作 {#button-controls}

本裝置透過位於側面的一顆多功能按鈕進行操作。所有選單導航和設定均透過該按鈕完成。

<table><thead><tr><th>操作</th><th>位置</th><th>結果</th></tr></thead><tbody><tr><td>輕按（50 ms – 3 s）</td><td>主螢幕</td><td>切換到下一個顯示佈局</td></tr><tr><td>長按（3 s）</td><td>主螢幕</td><td>開啟設定選單</td></tr><tr><td>輕按（50 ms – 1 s）</td><td>設定選單</td><td>切換到下一個選單選項</td></tr><tr><td>長按（1 s）</td><td>設定選單</td><td>確認高亮的選單項</td></tr><tr><td>無操作（30 s 無輸入）</td><td>設定選單</td><td>自動返回主螢幕</td></tr></tbody></table>

### 設定選單 {#settings-menu}

在主螢幕上長按（3 s）按鈕即可開啟設定選單。選單包含以下專案：

- Pairing code
- Temperature unit
- VOC unit for Matter
- Unpairing
- CO₂ sensor calibration
- Display settings
- Back（退出）

輕按（50 ms – 1 s）可在設定項之間迴圈切換；長按（1 s）可確認某一項。如果 30 秒內沒有輸入，螢幕會自動返回主佈局。

#### 配對碼 {#pairing-code}

導航到 **Pairing code** 並長按（1 s）。螢幕會顯示 Matter QR 配對碼。長按（1 s），或等待 30 秒超時，即可返回主螢幕。

#### 溫度單位 {#temperature-unit}

導航到 **Temperature unit** 並長按（1 s）。選擇 Celsius（°C）、Fahrenheit（°F）或 Back。長按（1 s）儲存單位並返回主螢幕。

#### Matter 的 VOC 單位 {#voc-unit-for-matter}

導航到 **VOC unit for Matter** 並長按（1 s）。選擇 ppm、µg/m³ 或 Back。長按（1 s）確認並返回主螢幕。

:::note note

VOC 單位會影響空氣質量資料在不同平臺上的顯示方式。使用 **Google Home** App 時，請使用 **ppm**。使用 **Apple HomePod** 和 **Amazon Alexa** App 時，請使用 **µg/m³**。

:::

#### 取消配對 {#unpairing}

導航到 **Unpairing** 並長按（1 s）；螢幕將顯示“Ready to unpair BLE/Matter”。

- 如果 30 秒超時，螢幕會在未取消配對的情況下返回。
- 輕按（50 ms – 3 s）即可取消配對；螢幕會確認成功。等待 5 秒超時或輕按返回。

:::note note

如果 **Claire** 已配對到其他家庭，請不要忘記執行 **Unpair**，因為它可能會妨礙新的配對。

:::

#### CO₂ 感測器校準 {#co-sensor-calibration}

導航到 **CO₂ sensor calibration** 並長按（1 s）。將裝置置於新鮮空氣中（約 400 ppm CO₂）並等待 60 秒。當提示開始校準時，輕按（50 ms – 3 s）確認（3 分鐘超時會返回）。等待校準完成；系統會自動重啟。

#### 顯示設定 {#display-settings}

導航到 **Display settings** 並長按（1 s）以訪問螢幕偏好設定：

-

**Display anti-burn in** – 選擇 **Display anti-burn in**（長按 1 s）。輕按（50 ms – 1 s）可在 **Enabled** 或 **Disabled**（預設 = **Disabled**）或（轉到）Back 之間切換。長按（1 s）儲存選擇。此功能適用於在強光下 24/7 執行的裝置：每 15 分鐘它會短暫重新整理螢幕（幾秒鐘）以減少燒屏。在正常使用中，亮度會自動調節，並在夜間變暗，因此燒屏不太可能發生，該功能預設關閉。

-

**Display brightness** – 選擇 **Display brightness**（長按 1 s）。輕按（50 ms – 1 s）可在 **Automatic**（透過環境光感測器調節）或 **Manual**（預設 = **Automatic**）或（轉到）Back 之間切換。長按（1 s）選擇該選項。在 **Manual** 下，您可以輕按（50 ms – 1 s）在 **Set brightness** 和 **Night mode**（或轉到 Back）之間切換。長按（1 s）選擇您的選項：

- **Set brightness** – 輕按（50 ms – 1 s）在 **2%, 10%, 25%, 50%, 75%, 100%**（或轉到 Back）之間切換。
- **Night mode** – 輕按（50 ms – 1 s）切換 **ON** 或 **OFF**（或轉到 Back）。**ON** 使用設定的亮度，但在黑暗環境中降至 2%；**OFF** 則無論黑暗與否都保持設定的亮度。長按（1 s）確認選擇。

-

**Back** – 選擇 **Back** 並長按（1 s）返回裝置設定列表。

#### 退出選單 {#exit-menu}

選擇 **Back** 並長按（1 s）返回主螢幕。

### 韌體升級 / 恢復出廠設定 / 重啟 {#firmware-upgrade--factory-reset--reboot}

要訪問此選單，請在按住按鈕的同時給裝置開機。請在接通電源**之前**按住按鈕，並在裝置開機過程中保持按住。

#### 韌體升級 {#firmware-upgrade}

透過 GUI 升級韌體：

**Claire**

- 在按住按鈕的同時透過 USB 將裝置連線到計算機——裝置會開機並開啟 Firmware upgrade / Factory reset / Reboot 選單。
- 輕按（50 ms – 1 s）到達 **Firmware Upgrade**，然後長按（1 s）選擇它。
- 螢幕允許您選擇 **Start Firmware Upgrade**（或轉到 Back）；在 **Start Firmware Upgrade** 上長按（1 s）。
- 裝置進入 DFU 模式，並在您的 PC 上顯示為名為“DFU in FS Mode”的新 USB 裝置。

**PC**

- 使用基於 Chromium 的瀏覽器（**Chrome** 或 **Edge**）。
- 在瀏覽器中開啟韌體升級 Web GUI：**[https://mikrotik.com/download/iot](https://mikrotik.com/download/iot)**。
- 在頁面上按步驟操作：**Connect** 並 **Select** USB 介面，然後 **Update device**。
- 等待更新完成——在此過程中請勿斷開裝置。

:::note note

**Ubuntu / Linux：** 在新增 MikroTik 的 **udev 規則**之前，瀏覽器無法訪問該裝置。當您嘗試連線時，Web GUI 會顯示帶有必需說明的錯誤——請按照說明操作，然後重新連線裝置並再次嘗試上傳。

:::

#### 恢復出廠設定 {#factory-reset}

輕按（50 ms – 1 s）到達 **Factory Reset** 並長按（1 s）選擇它。在 **Confirm Factory Reset** 上長按（1 s）；裝置會重設並重啟。

#### 重啟 {#reboot}

輕按（50 ms – 1 s）到達 **Reboot** 並長按（1 s）重啟裝置。

:::note note

當裝置按鈕被鎖定時，需要執行 Factory Reset。

:::

## Claire 與 Google Nest {#claire-and-google-nest}

如果您有帶 Thread 無線電的 Google Nest 音箱或顯示屏，並希望將 Claire 與該生態系統配對：

### Claire {#claire}

- 按住側邊按鈕 3 秒開啟選單。選擇 **Pairing code** 選項（您可以短按按鈕 50ms 至 1s 來迴圈切換其他選單設定）。選中 **Pairing code** 後，按住側邊按鈕 1 秒，它將顯示 **Matter QR code**。

### 手機 {#phone}

- 開啟 Google **Home** App 並點選 **(+)** **Add** → **(+)** **Device**：
- 用您的手機（攝像頭）掃描 **Claire** 顯示屏上顯示的 **Matter QR code**。
- 按照其餘提示完成配對過程。

## Claire 與 Apple HomePod {#claire-and-apple-homepod}

如果您有帶 Thread 無線電的 Apple HomePod 或 Apple TV，並希望將裝置與該生態系統配對：

### Claire {#claire-1}

- 按住側邊按鈕 3 秒開啟選單。選擇 **Pairing code** 選項（您可以短按按鈕 50ms 至 1s 來迴圈切換其他選單設定）。選中 **Pairing code** 後，按住側邊按鈕 1 秒，它將顯示 **Matter QR code**。

### iPhone {#iphone}

- 開啟 **Home** App 並點選 **Add Accessory**（+）。
- 用您的 iPhone（攝像頭）掃描 **Claire** 顯示屏上顯示的 **Matter QR code**。
- 按照其餘提示完成配對過程。

配對完成後，裝置將出現在您的 Apple **Home** App 中，您可以在那裡檢視空氣質量資料。

:::tip tip

如果您在配對裝置時遇到問題，有時先重啟 iPhone 會有幫助。

:::

## Claire 與 Amazon Alexa {#claire-and-amazon-alexa}

如果您有 Amazon Alexa 裝置（支援 Matter）並希望將 Claire 與該生態系統配對：

### Claire {#claire-2}

- 按住側邊按鈕 3 秒開啟選單。選擇 **Pairing code** 選項（您可以短按按鈕 50ms 至 1s 來迴圈切換其他選單設定）。選中 **Pairing code** 後，按住側邊按鈕 1 秒，它將顯示 **Matter QR code**。

### 手機 {#phone-1}

- 在 **Amazon Alexa app** 中，選擇 **Add device** → **Other** → **Matter**，然後繼續執行步驟，這些步驟會引導您掃描二維條碼。
- 用您的手機（攝像頭）掃描 **Claire** 顯示屏上顯示的 **Matter QR code**。
- 按照其餘提示完成配對過程。

配對完成後，系統會要求您設定多個裝置/感測器（您可以將它們放入同一組）。

## 安裝說明 {#mounting-instruction}

- 要將裝置安裝在牆上並透過 DC 端子供電，請使用一字螺絲刀或美工刀取下小蓋板。連線 DC 電源線時請確保極性正確。請勿反接極性。
- 使用隨附的安裝模板標記壁掛支架所需的鑽孔位置，如有需要，還需標記電纜入口孔的位置。

- 位置 1 – 使用安全螺絲安裝（推薦用於公共場所）。使用兩側的兩顆螺絲固定。
- 位置 2 – 不使用安全螺絲安裝。

- 對於混凝土或磚牆表面，請使用 5 mm 鑽頭鑽孔。
- 安裝壁掛支架：插入牆塞，對準支架，插入螺絲並擰緊。
- 將裝置安裝到壁掛支架上。
- 對於公共場所的安裝，請使用隨附的安全螺絲固定裝置。使用 T9 Torx 批頭擰緊螺絲。

![](/img/9244fbc09cc85cc0.webp)

## 歐亞符合性標誌 {#eurasian-conformity-mark}

裝置生產日期資訊標註在裝置標籤上序列號的末尾，以斜槓分隔。第一位數字表示年份（年份的最後一位），後面兩位數字表示週數。

製造商：Mikrotikls SIA, Unijas iela 2, Riga, LV-1039, Латвия, [support@mikrotik.com](mailto:support@mikrotik.com)。製造地請見包裝。

供應到歐亞關稅同盟的 MikroTik 產品，會根據相關要求進行評估，並按如下所示標有 EAC 標誌：

![](/img/984ad54320693690.webp)

## CE 符合性宣告 {#ce-declaration-of-conformity}

![](/img/6f53abac46c9e31f.jpg)

製造商：Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039。

Mikrotīkls SIA 特此宣告，無線電裝置 IAQM-THC2PV-W 和 IAQM-THC2PV-G 符合指令 2014/53/EU。歐盟符合性宣告的全文可在以下網址獲取：[https://mikrotik.com/products](https://mikrotik.com/products)

## 英國合規通知 {#uk-compliance-notice}

![](/img/5d0fc80f851cbbdf.webp)

本裝置上的 CE 標誌滿足適用的英國法規要求。

### 藍牙 / IEEE 802.15.4 (LR-WPAN) {#bluetooth--ieee-802154-lr-wpan}

<table><thead><tr><th>(EN) 工作頻率 / 輸出功率 (DE) 工作頻率 / 輸出功率 (FR) 工作頻率 / 輸出功率 (IT) 工作頻率 / 輸出功率 (ES) 工作頻率 / 輸出功率 (RU) 工作頻率 / 輸出功率</th><th>Bluetooth LE</th><th>2400-2483.5 MHz / 8 dBm (Max EIRP)</th></tr></thead><tbody><tr><td></td><td>IEEE 802.15.4 (LR-WPAN)</td><td>2400-2483.5 MHz / 8 dBm (Max EIRP)</td></tr></tbody></table>

**Bluetooth 合格產品**

![](/img/cf3c8d2919f980e2.webp)

本產品已成功完成 Bluetooth 認證流程。有關 Bluetooth 認證產品的更多資訊，請使用以下連結：[https://launchstudio.bluetooth.com/Listings/Search](https://launchstudio.bluetooth.com/Listings/Search)

Bluetooth® 文字商標和徽標是 Bluetooth SIG, Inc. 擁有的註冊商標，Mikrotikls SIA 對此類標誌的任何使用均已獲得許可。其他商標和商品名稱均為其各自所有者的財產。

:::note note

本裝置的法規標籤和製造商資訊印在貼上於裝置底部的標籤上。請參閱該標籤以瞭解型號、序列號和合規標誌。

:::

*注。此處包含的資訊可能會變更。請訪問 [www.mikrotik.com](https://www.mikrotik.com/) 上的產品頁面，獲取本文件的最新版本。*

#86426
