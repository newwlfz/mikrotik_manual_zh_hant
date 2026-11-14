---
sidebar_key: "internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-for-ios-devices"
sidebar_position: 2
title: "適用於 iOS 裝置的 MikroTik Beacon Manager"
sidebar_label: "適用於 iOS 裝置的 MikroTik Beacon Manager"
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-for-ios-devices
captured_at: '2026-11-04T11:19:40+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

##

## 概述 {#overview}

MikroTik Beacon Manager 應用用於 Bluetooth 標籤（TG-BT5-XX）配置。由於這些標籤是基於 Bluetooth 的裝置，在繼續配置之前，你必須在手機上啟用 Bluetooth。

對於 iOS 裝置，您可以透過[連結](https://apps.apple.com/id/app/mikrotik-beacon-manager/id1561796698)找到該應用。

![](/img/6f29fdbe1437d3b0.png)

## 我的裝置 {#my-devices}

啟動應用後看到的第一個螢幕是“我的裝置”螢幕，其中會顯示所有附近的藍牙標籤。

![](/img/3bbbbe7dcb472252.webp)

如果列表為空，表示所有附近的標籤都處於出廠睡眠模式。一旦標籤進入廣播模式或配置模式，它就會顯示在列表中。要將標籤從出廠睡眠模式喚醒，請將磁鐵放在標籤上（啟用簧片開關）3-10 秒。

螢幕底部有 2 個選項——留在“我的裝置”標籤頁，或在“設定”標籤頁下更改應用設定。

## 設定 {#settings}

如果您選擇更改應用程式的“設定”，您將看到以下螢幕：

![](/img/8c97c345ed56c27b.webp)

“設定”標籤頁分為“發現”、“其他”和“關於”部分。

在“發現”部分，您可以啟用“僅 MirkoTik 封包”複選框，這將確保“我的裝置”列表中只顯示 MikroTik 裝置。停用後，所有藍牙裝置都會顯示在“我的裝置”列表中。

在“其他”部分，可以更改應用的語言（英語、俄語、拉脫維亞語和葡萄牙語）以及外觀（系統、深色和淺色）。

“關於”部分僅顯示應用的版本。

## 標籤管理 {#tag-management}

當標籤在列表中時，您可以點選它，然後進入該標籤的單獨概覽頁面：

![](/img/c5f4359cd479fc0d.webp)

![](/img/b40760171e0f24ca.webp)

您首先應該注意的是訊號強度指示（標籤的 RSSI 訊號——表示標籤距離有多遠）。當所有圓圈都填充/完成時，表示訊號強度約為 -60 RSSI。當僅填充 2 個圓圈時，表示訊號強度約為 -70 RSSI。當僅填充一個圓圈時，表示訊號強度為 -80 RSSI。當沒有圓圈填充時，表示訊號強度為 -90 RSSI 或更低。

在訊號強度指示下方，您可以檢視標籤的電池電量、溫度和加速度。

:::info
TG-BT5-IN 型號沒有溫度感測器！
:::

在“感測器觸發”欄位中，您可以檢視標籤報告的觸發事件（裝置是否被傾斜、拋擲或跌落）：

![](/img/2e91939c91ff19ed.webp)

在“顯示名稱”欄位中，您可以更改標籤的名稱。

在“裝置圖示”欄位中，您可以為標籤分配圖示。

如果您選擇“移除裝置”按鈕 → 您可以取消配對該裝置並將其從裝置列表中移除。

## 標籤配置 {#tag-configuration}

要訪問標籤的配置選單，您需要將標籤置於“配置模式”：

![](/img/c0dbe0bff6b22fe4.webp)

要進入裝置配置，請將磁鐵保持在簧片開關上方，直到其 LED 停止閃爍。

成功進入配置模式後，“設定/齒輪”圖示（位於右上角）會變成橙色，並且您應該在螢幕底部看到“配置模式已啟用”訊息，如下圖所示：

![](/img/ad498dd9c76fce4e.webp)

點選螢幕右上角的橙色“設定/齒輪”圖示，您將進入標籤的配置頁面：

![](/img/cdc8d3a19ccce0a0.webp)

此頁面會要求您為標籤同步時間和日期。

![](/img/76671aace50d8565.webp)

應用會在“裝置狀態”標籤頁下顯示有關標籤的常規資訊（如上方截圖所示）。

:::info
TG-BT5-IN 型號沒有溫度感測器！
:::

可以在“配置”標籤頁中更改設定：

![](/img/a239c9e844cb153f.webp)

![](/img/ef18782a567b4bf3.webp)

### “加速度計”設定 {#accelerometer-settings}

此部分允許您更改“電源模式”、“測量”、“喚醒閾值和持續時間”、“自由落體閾值和持續時間”、“角度閾值”和“低噪聲濾波器”設定。

#### 電源模式 {#power-mode}

![](/img/6dc6d8f52961c489.webp)

此選單允許你在 2 種模式之間選擇："Low power" 和 "High power"。在 "Low power" 模式下，你將獲得較低精度，但功耗也更低。在 "High power" 模式下，你將獲得較高精度，但功耗也更高。

“scale factor”是測量範圍（scale factor 越低，精度越好，但請記住，無法測量更大的加速度峰值）。

#### 測量 {#measurements}

![](/img/6b42f60ad0eeb4ac.webp)

"Data Rate" 設定表示 1 秒視窗內的加速度測量次數（測量頻率）。每秒傳送的封包越少 → 功耗越低。

“Bandwith filter”是數字濾波截止頻率（高通濾波器頻寬）。

如果頻寬 = "x" Hz，則標籤會過濾掉每秒發生次數少於 "x" 次的加速度變化。

例如，如果裝置平放在桌面上，即使存在地球重力，加速度也會顯示為 0g（而不是 1g）→（因為地球重力是恆定的 - 其變化頻率為 0 Hz，即 &lt; "x" Hz）它會被過濾掉。

#### 喚醒閾值與持續時間 {#wakeup-threshold-and-duration}

![](/img/be5cdce0ca290fb7.webp)

"Wakeup Threshold" 定義喚醒區域/加速度範圍。"Wakeup Duration" 定義加速度超過所配置喚醒閾值的時間。當任一軸（X、Y 或 Z）上的加速度在配置的喚醒持續時間內超過閾值時，將生成喚醒事件（觸發喚醒條件）。要更好地理解“任一軸（X、Y 或 Z）上的加速度”的含義，請想象一個三維笛卡爾座標系，並在原點（公共點）放置標籤的加速度計或標籤本身：

![](/img/13cf2251bb92b747.png) ![](/img/03b6ed29411f1e34.png)

例如，喚醒閾值設定為 1.0g（表示 -1.0g 到 +1.0g 之間的任何加速度都屬於配置的閾值/加速度範圍），喚醒持續時間設定為 0.12s。因此，一旦裝置被推動/拋向任一軸方向（裝置開始向任意方向移動），且加速度超過配置閾值（acceleration> +1.0g 或 acceleration&lt; -1.0g）的時間長於 0.12s → 就會觸發喚醒條件。

#### 自由落體閾值與持續時間 {#free-fall-threshold-and-duration}

![](/img/a1a13c13d5d2af9c.webp)

“自由落體閾值”定義自由落體區域/加速度範圍。“自由落體持續時間”定義加速度將處於所配置自由落體閾值內的時間。當所有 3 個軸（X、Y 和 Z）上的加速度在自由落體區域/閾值內持續所配置的自由落體持續時間時，將生成自由落體事件（觸發自由落體條件）。要更好地理解“所有軸（X、Y 和 Z）上的加速度”是什麼意思，請檢視上方“喚醒閾值和持續時間”部分中的裝置照片。

例如，自由落體閾值設定為 156.25g（表示 -156.25g 到 +156.25g 之間的任何加速度都屬於配置的閾值/加速度範圍），自由落體持續時間設定為 0.2s。因此，一旦裝置處於自由落體狀態，且所有軸上的加速度在配置閾值內（-156.25g&lt;acceleration&lt;+156.25g）的時間長於 0.2s → 就會觸發自由落體條件。

#### 角度閾值 {#angle-threshold}

![](/img/39fc273ae65491c6.webp)

可在 50°...80° 之間變化。它是傾斜功能的閾值。例如，當觸發器設定為 60°，且裝置傾斜到該角度時——就會觸發傾斜動作併發送廣播封包。

#### 低噪聲濾波器 {#low-noise-filter}

![](/img/1d1bbb54dc3c889e.webp)

用於啟用或停用低噪聲濾波器的選項。低噪聲濾波器用於降低測量中的噪聲密度。啟用此功能會略微增加功耗。

### “傳輸”設定 {#transmission-settings}

此部分允許您配置標籤的“Tx power level”。

#### 發射功率級別 {#tx-power-level}

![](/img/0c8f0f4875b2a82e.webp)

以分貝毫瓦為單位的發射功率級別。可在 -28dBm...6dBm 之間變化。Tx Power 僅用於增大/減小標籤的發射功率。

### “廣播”設定 {#advertismenet-settings}

在廣播模式下，標籤透過 Bluetooth 廣播封包廣播自身資訊。資訊取決於廣播封包型別（該型別可在設定中更改）。

目前，支援的型別如下：

MikroTik、[Eddystone-TLM](https://play.google.com/store/apps/details?id=com.mikrotik.android.bt5&hl=en_US&gl=US&pli=1)、[Eddystone-UID](https://github.com/google/eddystone/tree/master/eddystone-uid) 和 [iBeacon](https://developer.apple.com/ibeacon/)。

Eddystone-TLM、Eddystone-UID 和 iBeacon 格式有一個用於配置 4 個引數的選項。MikroTik 格式有一個用於配置名為“encrypt packets”的附加引數的選項：

![](/img/331b16485e7ad4b4.webp)

一旦啟用“啟用廣播”複選框，您將能夠配置以下引數：

| 屬性 | 描述 |
| --- | --- |
| 廣播間隔（20ms...10s 或停用） | 標籤廣播廣播封包的時間間隔（毫秒） |
| 自由落體檢測（開/關） | 當加速度計（標籤）檢測到自由落體觸發時，是否傳送廣播封包 |
| 傾斜檢測（開/關） | 當加速度計（標籤）檢測到傾斜觸發時，是否傳送廣播 |
| 衝擊檢測（開/關） | 當加速度計（標籤）檢測到衝擊/喚醒觸發時，是否傳送廣播 |
| 加密封包（開/關）——僅適用於 MikroTik 格式 | 是否在十六進位制有效載荷中加密加速度、溫度、執行時間、觸發動作和電池百分比引數 |

- 當您僅配置了廣播間隔而未啟用任何觸發時——廣播封包將根據設定的間隔時間進行廣播（每 **x** 秒）。
- 當傾斜觸發已啟用且裝置發生傾斜時——廣播封包將立即廣播。
- 當自由落體觸發已啟用並檢測到自由落體時，標籤一旦檢測到自由落體條件——就會發送封包。
- 當衝擊觸發已啟用且裝置被推動/移動時——會立即傳送廣播封包。
- 當啟用加密引數時，十六進位制有效載荷資料（如加速度、溫度、執行時間、觸發動作和電池百分比）會使用私鑰加密。此金鑰只有標籤所有者知道（在購買時獲得）。

### “系統”設定 {#system-settings}

系統部分允許您重設標籤設定並將標籤置於工廠睡眠模式。

#### 重設裝置 {#reset-device}

此選項將標籤置於廣播模式（以關閉設定）：

![](/img/d1044761869223cf.webp)

#### 出廠睡眠 {#factory-sleep}

此選項將裝置設定為工廠睡眠模式：

![](/img/5931ae603b3e6e17.webp)
