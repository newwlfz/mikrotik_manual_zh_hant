---
sidebar_key: "wireless/abgn/spectral-scan"
sidebar_position: 5
title: "頻譜掃描"
sidebar_label: "頻譜掃描"
description: "MikroTik RouterOS 中的 Spectral Scan 功能可以持續監控並可視化無線頻譜活動，其中包括利用 10MHz 增量的頻譜快照對 2.4GHz 和 5GHz 頻段進行干擾檢測，同時提供控制檯命令用於詳細分析，並可與 The Dude 網路監控工具整合。"
tags:
  - 'spectral-scan'
  - 'wireless'
  - 'monitoring'
source: https://manual.mikrotik.com/docs/7.25/wireless/abgn/spectral-scan
captured_at: '2026-11-04T11:23:57+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

頻譜掃描可以掃描無線網路卡支援的所有頻率，並直接在控制檯中繪製它們。確切的頻率範圍取決於網路卡。r52n 上允許的範圍：[4790; 6085]、[2182; 2549]。

無線網路卡可以為任何 20mhz 寬的通道生成 4us 長的頻譜快照。這被視為一個頻譜樣本。

為了提高資料質量，頻譜以 10mhz 的頻率增量進行掃描，這意味著在每個特定頻率上樣本覆蓋範圍翻倍（考慮到 20mhz 寬的樣本）。

:::warning
目前，Atheros 802.11ac 晶片（例如 QCA98xx、IPQ-4018）不支援。請參閱 [https://mikrotik.com/products](https://mikrotik.com/products) 以確定您裝置上的無線晶片。
:::

## 控制檯 {#console}

### 頻譜歷史 {#spectral-history}

![](/img/690b5cf44100ee79.webp)

```ros
/interface/wireless/spectral-history <wireless interface name> 
```

繪製頻譜圖。圖例和頻率標尺每 24 行列印一次。標尺中的數字對應其最左側字元位置的值。落在不同範圍內的功率值會以具有相同前景色和背景色的不同顏色字元列印，因此可以複製並貼上此命令的終端輸出。

- *value* -- 選擇在輸出中繪製的值。'interference' 比較特殊，它顯示檢測到的干擾源（受 'classify-samples' 引數影響）而不是功率讀數，並且不能設為可聽。
- *interval* -- 列印頻譜圖行的時間間隔。
- *duration* -- 在指定時間後終止命令。預設是無限期。
- *buckets* -- 在頻譜圖的每一行中顯示多少個值。此值受終端列數限制。如果使用 'audible'，減小此值會很有用。
- *average-samples* -- 在每個頻率上採集的 4us 頻譜快照數量，並據此計算平均能量和最大能量。（預設 10）。
- *classify-samples* -- 在每個頻率上採集並由干擾分類演算法處理的頻譜快照數量。通常，樣本越多，發現某些型別干擾的機會就越大（預設 50）。
- *range* --
  - 2.4ghz - 掃描整個 2.4ghz 頻段；
  - 5ghz - 掃描整個 5ghz 頻段；
  - current-channel - 僅掃描當前通道（20 或 40 MHz 寬）；
  - range - 掃描特定範圍。

- *audible=yes* -- 在列印每一行時播放該行。行與行之間有短暫的靜音。每一行從左到右播放，較高的頻率對應頻譜圖中較高的值。

### 頻譜掃描 {#spectral-scan}

![](/img/9b8c8528563f6d4e.webp)

```ros
 /interface/wireless/spectral-scan <wireless interface name> 
```

持續監控頻譜資料。此命令使用與 'spectral-history' 相同的資料來源，因此共享許多引數。

每一行顯示一個頻譜圖桶 -- 頻率、平均功率的數值，以及字元圖形條。條形用 ':' 字元顯示平均功率值，用 '.' 字元顯示平均峰值保持。最大值顯示為單獨浮動的 ':' 字元。

- *show-interference* -- 新增一列，顯示檢測到的干擾源；

可能分類的干擾型別：

- Bluetooth-headset
- Bluetooth-stereo
- cordless-phone
- microwave-oven
- CWA
- video-bridge
- wifi

## The Dude {#the-dude}

The Dude 是 MikroTik 提供的一款免費網路監控和管理程式。您可以[在此處下載](http://www.mikrotik.com/thedude.php)。

The Dude 內建了從任何配備受支援無線網路卡的 RouterOS 裝置執行圖形化頻譜掃描的功能。只需在 Dude 地圖中選擇此裝置，右鍵單擊並選擇 Tools -> Spectral Scan。

![](/img/dba8dc30746d8cee.webp)

這將開啟頻譜掃描 GUI，其中包含各種選項和不同的檢視模式：

![](/img/1f9413c23ef2332d.webp)
