---
sidebar_key: "internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-android-devices"
sidebar_position: 1
title: "適用於 Android 裝置的 MikroTik Beacon Manager"
sidebar_label: "適用於 Android 裝置的 MikroTik Beacon Manager"
source: https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-android-devices
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

##

## 概述 {#overview}

MikroTik Beacon Manager 應用用於 Bluetooth 標籤（TG-BT5-XX）配置。由於這些標籤是基於 Bluetooth 的裝置，在繼續配置之前，你必須在手機上啟用 Bluetooth。

對於 Android 裝置，你可以透過[連結](https://play.google.com/store/apps/details?id=com.mikrotik.android.bt5&hl=en_US&gl=US&pli=1)找到該應用。

![](/img/6f29fdbe1437d3b0.png)

## Beacon Manager 介面 {#beacon-manager-screen}

啟動應用後看到的第一個介面是 "MikroTik Beacon Manager" 介面，其中會顯示所有附近的 Bluetooth 標籤。

![](/img/f58035e23befaa90.webp)

如果列表為空，表示所有附近的標籤都處於出廠睡眠模式。一旦標籤進入廣播模式或配置模式，它就會顯示在列表中。要將標籤從出廠睡眠模式喚醒，請將磁鐵放在標籤上（啟用簧片開關）3-10 秒。

:::info
如果你確定標籤就在手機範圍內，但列表仍未捕獲任何標籤 → 請嘗試在手機的 GPS 設定中開啟 "Location=ON"。
:::
在介面的右上角有 3 個按鈕：

![](/img/b392db8146318769.webp)

### 二維條碼讀取器 {#or-code-reader}

"QR Code reader" 按鈕，可讓你透過二維條碼新增標籤（MAC 地址用作標籤 ID）：

![](/img/e466c601df2ce7fa.webp)

#### NFC 支援 {#nfc-support}

:::info
本節僅適用於 TG-BT5-OUT 型號
:::

你也可以使用 NFC（類似二維條碼讀取器功能）查詢標籤（MAC 地址用作標籤 ID）。

你只需在手機設定中啟用 NFC，並開啟 MikroTik Beacon Manager 應用。

當你看到初始介面（標籤列表）後，將標籤靠近手機的 NFC 天線，系統會提供開啟裝置設定的選項：

![](/img/4f2a44b0e3b0399f.webp)

如果你按下 "YES"，你將跳轉到下方所示的頁面。在選單中，你可以選擇從列表中刪除裝置，或透過 "Configure" 按鈕進入配置模式。

![](/img/9588ae77a34e8d75.webp)

### 排序方式 {#order-by}

"Order by" 按鈕，可讓你更改裝置列表的順序，或透過勾選 "Show only MikroTik beacons" 複選框來篩選列表，僅顯示 MikroTik 信標：

![](/img/85e3eca466822a0e.webp)

### 設定與批次配置 {#settings-and-batch-configuration}

"⋮" 標籤頁分為 2 個子標籤頁 - "Settings" 和 "Batch Configuration"。

#### 設定 {#settings}

此標籤頁中的第一個選項是設定 "Discovery refresh interval"，即掃描附近標籤的間隔。

![](/img/d014ba1eb333003e.webp)

第二個選項是啟用或停用 "Save triggers" 設定。啟用後，應用會將檢測到的觸發器儲存到資料庫中。你可以在 "Sensor Triggers" 選單中檢視觸發器（"Sensor Triggers" 選單在本指南的 "**標籤管理**" 部分中展示）。如果停用此選項，應用一關閉，"Sensor Triggers" 資料就會被清除。

最後，"App version" 欄位顯示當前應用版本/構建。

#### 批次配置 {#batch-configuration}

此選項允許你使用相同設定批次配置多個標籤。

為此，你需要從其中一個標籤匯出配置檔案。標籤配置的匯出和匯入在本指南的 "**標籤配置**" 部分中展示。

儲存配置檔案後，只需按下 "Batch Configuration" 按鈕，它會帶你進入檔案選單，你需要在其中選擇檔案。選擇（你希望應用到多個裝置的）配置檔案，應用將顯示一個包含所有附近檢測到的標籤的介面：

![](/img/76fec7b838576b5b.webp)

最後一步是將這些標籤置於配置模式（將磁鐵放在標籤上 5-10 秒）。裝置進入配置模式後，你將看到 "Uploading configuration" 訊息。配置成功應用後，訊息將變為 "Configuration updated"。

![](/img/d8b8d8832e0eb2d0.webp)

## 標籤管理 {#tag-management}

當標籤出現在列表中時，你可以點選其 MAC 地址，然後會看到以下選項：

![](/img/3bdcf336e67b4308.webp)

可以 "SAVE" 標籤，或透過 "CONFIG ONLY" 按鈕立即進入標籤的配置選單。

首先，我們將更詳細地說明 "SAVE" 選項。標籤的配置選單將在後面的 "**標籤配置**" 部分中說明。

當你點選先前儲存的標籤時，你將看到以下選單：

![](/img/4a21fd05985dd1e2.webp)

你首先會注意到的是訊號強度指示（標籤的 RSSI 訊號 - 即標籤距離多遠）。當所有圓圈都為綠色時，表示訊號強度約為 -60 RSSI。當只有 2 個圓圈為綠色時，表示訊號強度約為 -70 RSSI。當只有 1 個圓圈為綠色時，表示訊號強度為 -80 RSSI。當沒有圓圈為綠色時，表示訊號強度為 -90 RSSI 或更弱。

在訊號強度指示器下方，你有 2 個選項 - 進入標籤的配置選單（"Configure" 按鈕）或刪除裝置（"Delete" 按鈕）。

在 "Name/Display Name" 欄位中，你可以更改標籤名稱：

![](/img/3cc42b102dc2b60d.webp)

在 "Sensors" 欄位中，你可以檢視標籤的電池電量或溫度。

:::info
TG-BT5-IN 型號沒有溫度感測器
:::

在 "Sensor Triggers" 欄位中，你可以檢視標籤上報的觸發器：

![](/img/5e1aecb3bba33a48.webp)

## 標籤配置 {#tag-configuration}

要訪問標籤的配置選單，你需要按下 "CONFIG ONLY" 按鈕或 "Configure" 按鈕，如下所示：

![](/img/d4ba1819e5f99163.webp)

![](/img/a1fcdbe850a16ab4.webp)

緊接著，你需要將磁鐵放在簧片開關上 5-10 秒：

![](/img/7ed4d27347a1a08e.webp)

經過短暫的啟動時間後，裝置應進入配置模式：

![](/img/9a63e10fcf7d8ca4.webp)

應用將在 "Status" 標籤頁中顯示標籤的常規資訊（如上方截圖所示）。

可以在 "Settings" 標籤頁中更改配置：

![](/img/55935bfe7099a80f.webp)

![](/img/b8dae72f15a18872.webp)

![](/img/23344769cc22ccd2.webp)

### 防寫 {#write-protection}

此選單允許你使用 6 個字元長的密碼鎖定標籤的設定：

![](/img/15657717c80f4f1f.webp)

設定密碼後，無法移除密碼保護（只能編輯密碼）。

下次你嘗試配置標籤時，系統會通知你標籤處於 "write protected" 狀態，你可以選擇停留在 "READ-ONLY" 模式（該模式允許你瀏覽/讀取設定，並限制進行配置更改），或透過輸入已配置的密碼來 "UNLOCK" 設定：

![](/img/6b272eaa0494ef13.webp)

### Beacon 設定 {#beacon-settings}

在廣播模式下，標籤透過 Bluetooth 廣播封包廣播自身資訊。資訊取決於廣播封包型別（該型別可在設定中更改）。

目前，支援的型別如下：

DeviceName、MikroTik、[Eddystone-TLM](https://play.google.com/store/apps/details?id=com.mikrotik.android.bt5&hl=en_US&gl=US&pli=1)、[Eddystone-UID](https://github.com/google/eddystone/tree/master/eddystone-uid) 和 [iBeacon](https://developer.apple.com/ibeacon/)。

![](/img/8a4ae96eb079e028.webp)

![](/img/30ae17907a6d9e72.webp)

![](/img/9bcaf537ad2f7fcd.webp)

![](/img/52d8f01aa1ffdb6e.webp)

| 屬性 | 描述 |
| --- | --- |
| **Advertisement interval** (20ms...24h or disable) | 以毫秒為單位的間隔，經過該間隔後標籤將廣播一個廣播封包。當你僅配置了 advertisement interval 而未啟用任何觸發器時 → 廣播封包將根據設定的間隔時間廣播（每 **x** 秒）。 |
| **Freefall detect** (on/off) | 當標籤檢測到自由落體觸發器時是否傳送廣播封包。當啟用自由落體觸發器並檢測到自由落體狀態時 → 將傳送封包。 |
| **Tilt detect** (on/off) | 當標籤檢測到傾斜觸發器時是否傳送廣播。當啟用傾斜觸發器且裝置發生傾斜時 → 將立即廣播廣播封包。 |
| **Impact detec**t (on/off) | 當標籤檢測到撞擊/喚醒觸發器時是否傳送廣播。當啟用撞擊觸發器且裝置被推動/移動時 → 將傳送廣播封包。 |
| **Encrypt** (on/off) - 僅適用於 MikroTik 格式  | 是否使用 "AES" 金鑰加密廣播的十六進位制有效載荷。啟用 "Encrypt" 引數後，十六進位制有效載荷資料（加速度、溫度、執行時間、觸發動作和電池百分比）將使用私鑰加密。此金鑰只有標籤所有者知道（隨購買獲得）。 |
| **Namespace** - 僅適用於 Eddystone-UID 格式  | 設定一個唯一的 10 位元組長信標 Namespace ID。 |
| **Instance** - 僅適用於 Eddystone-UID 格式  | 設定一個唯一的 6 位元組長信標 Instance ID。 |
| **UUID** - 僅適用於 iBeacon 格式  | 按以下格式設定通用唯一識別符號（UUID）：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx |
| **Major** - 僅適用於 iBeacon 格式  | 設定一個 16 位整數次級識別符號，使用十六進位制格式或十進位制數字（從 0 到 65 535）。 |
| **Minor** - 僅適用於 iBeacon 格式  | 設定一個 16 位整數次級識別符號，使用十六進位制格式或十進位制數字（從 0 到 65 535）。 |

### 廣播屬性 {#advertisment-properties}

| 屬性 | 描述 |
| --- | --- |
| **Connectable advertisements** (on/off) | 啟用可連線廣播。 |
| **Channel 37** (on/off) | 用於啟用在特定通道上的廣播。 |
| **Channel 38**(on/off) | 用於啟用在特定通道上的廣播。 |
| **Channel 39** (on/off) | 用於啟用在特定通道上的廣播。 |

### 預計電池壽命 {#estimated-battery-life}

本節顯示預計電池壽命：

![](/img/05ff3932b3c4fbe8.webp)

預計電池壽命在很大程度上取決於傳送（配置為傳送）的廣播封包數量。應用會計算預計每天廣播多少個數據包、標籤將活躍多長時間，以及平均每日功耗的估計值。

### 加速度計設定 {#accelerometer-settings}

加速度計可以完全關閉，並可透過 "Use Accelerometer" 切換按鈕重新開啟。

本節允許你更改下方截圖中顯示的引數：

![](/img/fa46dd072ad19a43.webp)

#### 模式與資料速率 {#mode-and-data-rate}

![](/img/7117984b7a85b0cd.webp)

此選單允許你在 2 種模式之間選擇："Low power" 和 "High power"。在 "Low power" 模式下，你將獲得較低精度，但功耗也更低。在 "High power" 模式下，你將獲得較高精度，但功耗也更高。

"Data Rate" 設定表示 1 秒視窗內的加速度測量次數（測量頻率）。每秒傳送的封包越少 → 功耗越低。

#### 滿量程 {#full-scale}

![](/img/8a82bf78367c9341.webp)

可在 (2g...16g) 之間變化。它是用於計算喚醒閾值的測量範圍。滿量程定義加速度計能夠測量的加速度範圍（範圍越大，測得加速度的精度越低）。

#### 頻寬濾波器 {#bandwith-filter}

![](/img/5d4bc1fdc9a6be12.webp)

是數字濾波截止值（高通濾波器頻寬）。

如果頻寬 = "x" Hz，則標籤會過濾掉每秒發生次數少於 "x" 次的加速度變化。

例如，如果裝置平放在桌面上，即使存在地球重力，加速度也會顯示為 0g（而不是 1g）→（因為地球重力是恆定的 - 其變化頻率為 0 Hz，即 &lt; "x" Hz）它會被過濾掉。

#### 喚醒閾值與持續時間 {#wakeup-threshold-and-duration}

![](/img/1f8377968b5b1f1d.webp)

"Wakeup Threshold" 定義喚醒區域/加速度範圍。"Wakeup Duration" 定義加速度超過所配置喚醒閾值的時間。當任一軸（X、Y 或 Z）上的加速度在配置的喚醒持續時間內超過閾值時，將生成喚醒事件（觸發喚醒條件）。要更好地理解“任一軸（X、Y 或 Z）上的加速度”的含義，請想象一個三維笛卡爾座標系，並在原點（公共點）放置標籤的加速度計或標籤本身：

![](/img/13cf2251bb92b747.png) ![](/img/03b6ed29411f1e34.png)

例如，喚醒閾值設定為 1.0g（表示 -1.0g 到 +1.0g 之間的任何加速度都屬於配置的閾值/加速度範圍），喚醒持續時間設定為 0.12s。因此，一旦裝置被推動/拋向任一軸方向（裝置開始向任意方向移動），且加速度超過配置閾值（acceleration> +1.0g 或 acceleration&lt; -1.0g）的時間長於 0.12s → 就會觸發喚醒條件。

#### 自由落體閾值與持續時間 {#free-fall-threshold-and-duration}

![](/img/1b4f6496b95e6782.webp)

"Free Fall Threshold" 定義自由落體區域/加速度範圍。"Free Fall Duration" 定義加速度處於所配置自由落體閾值內的時間。當所有 3 個軸（X、Y 和 Z）上的加速度在配置的自由落體持續時間內都處於自由落體區域/閾值內時，將生成自由落體事件（觸發自由落體條件）。要更好地理解“所有軸（X、Y 和 Z）上的加速度”的含義，請檢視上方“喚醒閾值與持續時間”部分中的裝置照片。

例如，自由落體閾值設定為 156.25g（表示 -156.25g 到 +156.25g 之間的任何加速度都屬於配置的閾值/加速度範圍），自由落體持續時間設定為 0.2s。因此，一旦裝置處於自由落體狀態，且所有軸上的加速度在配置閾值內（-156.25g&lt;acceleration&lt;+156.25g）的時間長於 0.2s → 就會觸發自由落體條件。

#### 角度閾值 {#angle-threshold}

![](/img/24b22a76d2d2e7e8.webp)

可在 50°...80° 之間變化。它是傾斜功能的閾值。例如，當閾值設定為 60° 且裝置傾斜到該角度時 - 將觸發傾斜動作併發送廣播封包。

#### 低噪聲濾波器 {#low-noise-filter}

![](/img/a00ac2855c2db0e7.webp)

用於啟用或停用低噪聲濾波器的選項。低噪聲濾波器用於降低測量中的噪聲密度。啟用此功能會略微增加功耗。

#### 溫度偏移 {#temperature-offset}

:::info
TG-BT5-IN 型號沒有溫度感測器！
:::

![](/img/1cc4ecf08cb17427.webp)

可在 -10°C...+10°C 之間變化。以百分之一攝氏度為單位，應用於原始溫度測量的偏移量。

#### 發射功率 {#tx-power}

![](/img/f41c183a7fd2b7d4.webp)

以分貝毫瓦為單位的發射功率級別。可在 -28dBm...6dBm 之間變化。Tx Power 僅用於增大/減小標籤的發射功率。

### 資料日誌 {#data-logs}

:::info
本節僅適用於 TG-BT5-OUT 型號。
:::

本節允許你配置/檢視日誌（這些日誌只能透過應用訪問）：

![](/img/6ce97a2795400a43.webp)

#### 配置日誌記錄 {#configure-logging}

在 "Configure logging" 選單中，你可以設定日誌記錄設定：

![](/img/fa4784b5151a54cd.webp)

你可以設定 "Periodic logging interval (s)"（也可以停用它）。啟用後，資料日誌將每隔 "x" 秒自動儲存：

![](/img/5b7488c3eb97c510.webp)

另一個選項是啟用 "Log Triggers"（週期性日誌記錄和觸發器日誌記錄可以一起使用）。使用日誌觸發器時 - 每當檢測到傾斜、自由落體和/或撞擊動作時，都會儲存日誌。

例如，當啟用傾斜觸發器且標籤檢測到該觸發器時 - 將記錄訊息。

你可以在 "Field config" 部分設定要記錄哪些引數：

![](/img/254acf4fa68bf455.webp)

![](/img/366c81f7cd5d818a.webp)

![](/img/7452cf1b74ee0cd9.webp)

你可以記錄 3 個引數：1) 電池電量；2) 溫度；3) 加速度。

如果你對某個引數不感興趣，可以停用該引數，也可以為它們設定閾值。

如果你只希望在電池電量低於 40% 時記錄電池電量，可以設定從 minimum=0% 到 maximum=40% 的閾值，這樣一來，只有當電池電量（電池電量百分比）處於所配置範圍內時，才會顯示在日誌中。同樣的原則適用於其他 2 個引數。

#### 資料日誌 {#data-logs-1}

已記錄的訊息將顯示在 "Data Logs" 標籤頁中：

![](/img/236d8ff71c774a82.webp)

你可以透過 "Export as .csv" 按鈕將日誌匯出為 .csv 檔案：

![](/img/0fbcd98eaa207fb4.webp)

### 系統 {#system}

在 "System" 標籤頁中，你可以同步時間、檢視系統日誌、將標籤置於出廠睡眠模式，並升級韌體：

![](/img/868402679294ec95.webp)

#### Unix 時間 {#unix-time}

使用此設定，你可以為標籤同步當前時間和日期：

![](/img/049ff4f3464d32b7.webp)

#### 日誌 {#logs}

可檢視系統日誌的選單：

![](/img/8c9c6e6aba6f4ac5.webp)

#### 出廠睡眠 {#factory-sleep}

此選項可以為標籤啟動出廠睡眠模式：

![](/img/09bb3ed977d0102d.webp)

#### 升級韌體 {#upgrade-firmware}

此選單允許你升級標籤的韌體版本：

![](/img/df88c003a9455902.webp)

##### 自動升級 {#automatic-upgrade}

點選 "Download and install" 並等待裝置重啟。

##### 手動升級 {#manual-upgrade}

要手動下載標籤的韌體檔案，請訪問 https://download.mikrotik.com/firmware/bt-tag/latest。你將能夠下載 "latest" 檔案，該檔案可在記事本或任何其他文字編輯器中開啟。檔案內容將指示最新的可用 TG-BT5-XX 版本：

```
2.3.1 1638358509
1326c554c18340a41e79fd88abbea193dc53b99931eddecd018e33cff577f6d3 bt-tag_HT_app_2.3.1-0rr.gbl
9dc21eb980e8bd36732ec4db8e4b03a8177885fccdbbd87122f7d9bf76410b8b bt-tag_HT_apploader_3.2.3-0rr.gbl
9e4f30d9006f24063ac96d0fb1181d135929d86d0e243d3b3985cc5e43d6b448 bt-tag_IN_app_2.3.1-0rr.gbl
e03fa2987b874463e9a5c686303f4d75fef0c0f8d89dde14f8c4b04be4838a93 bt-tag_IN_apploader_3.2.3-0rr.gbl
54e959dd9cc1da3a5408b5dc7c797c52ae1a1685122e14d966cbe433ec1d1b3c bt-tag_OUT_app_2.3.1-0rr.gbl
e0bc2e8a1a9de6a1974c201a48cfea2276465414e07efc07816400abca91aa14 bt-tag_OUT_apploader_3.2.3-0rr.gbl
5257a1b06cb8d57d06ae10ef2c87abf0df0a3ab8a9ac7f9229a9a421b8a0c0fc bt-tag_HT_app_2.3.1-000.gbl
caf3e333721852077945c8a766db32ee5e478f1e7844dcb3e0e3d700dbab009f bt-tag_HT_apploader_3.2.3-000.gbl
0f6603d97df5fc4b3f260b410628b3c62fb2562f26e85e44b6cdfdf1b58d04f8 bt-tag_IN_app_2.3.1-000.gbl
caf3e333721852077945c8a766db32ee5e478f1e7844dcb3e0e3d700dbab009f bt-tag_IN_apploader_3.2.3-000.gbl
3235db7bb9a9cca0d5e59ae774c3cd004be4e58b44c1ae40e6e3bb84feb077a6 bt-tag_OUT_app_2.3.1-000.gbl
caf3e333721852077945c8a766db32ee5e478f1e7844dcb3e0e3d700dbab009f bt-tag_OUT_apploader_3.2.3-000.gbl
```

使用應用仔細檢查標籤當前的韌體版本：

![](/img/14a184e0b741ea78.webp)

例如，已知標籤是 **TG-BT5-IN** 型號，且當前版本是 **1.6.1-000**，我們可以推斷最新版本是 "bt-tag_IN_app_2.3.1-000.gbl"。

請注意，對於大多數標籤，韌體版本將是 1.6.1-**0rr**（而不是 1.6.1-**000**）。你需要改用 x.x.x-**0rr** 檔案。

要下載實際的韌體檔案，請將連結中的 "latest" 部分更改為 "bt-tag_IN_app_2.3.1-000.gbl"。

因此，如果你的當前版本例如是 "1.6.1-000"（TG-BT5-IN 標籤），則可以使用以下連結下載韌體：

https://download.mikrotik.com/firmware/bt-tag/bt-tag_IN_app_2.3.1-000.gbl

如果你的當前版本例如是 "1.6.1-0rr"（TG-BT5-OUT 標籤），則可以使用以下連結下載韌體：

https://download.mikrotik.com/firmware/bt-tag/bt-tag_OUT_app_2.3.1-0rr.gbl

##### 升級設定 {#upgrade-settings}

:::warning
**如果你在標籤更新時遇到問題，標籤一直停留在 OTA/update 模式 → 請嘗試啟用 "Reliable write"！**

當標籤在 OTA/upgrade 模式中“卡住”時，可能會發生兩種情況：
a) Beacon Manager 標籤列表仍會在列表中顯示該標籤，但不會有標籤可“配置”的指示。你仍然可以在列表中點選該標籤（即使沒有顯示“齒輪”圖示），並在不啟用磁開關的情況下瀏覽其設定；

b) 標籤可能會從可管理標籤列表中消失。在這種情況下，請嘗試使用二維條碼讀取器功能手動新增標籤，並批准 "configuration"。
:::

要進入額外的升級設定選單，請點選 "Upgrade settings" 按鈕：

![](/img/5932d0f0e68843b5.webp)

這將允許你更改 "Reliable write" 配置：

![](/img/e7f10488893d6926.webp)

啟用後，該複選框可讓你使 Bluetooth 升級過程“更慢”但更“可靠”（此時手機和標籤之間會進行額外的交換和驗證步驟）。

### 匯入/匯出 {#importexport}

在介面右上角，你可以選擇匯入/匯出當前設定：

![](/img/06e3cc23cc4cd1b4.webp)

如果你按下匯出按鈕，應用將開啟手機的檔案選單，你可以在其中命名配置檔案並儲存。

如果你按下匯入按鈕，應用將開啟手機的檔案選單，你可以在其中選擇配置檔案並應用它。
