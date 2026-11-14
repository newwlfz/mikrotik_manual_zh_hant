---
sidebar_key: "internet-of-things/lora/user-guides/tg-lr-setup-guide"
sidebar_position: 4
title: "TG-LR 設定"
sidebar_label: "TG-LR 設定"
description: "本頁是 MikroTik TG-LR82 和 TG-LR92 LoRaWAN 感測器標籤的設定指南，涵蓋啟用、入網、遙測與感測器配置、磁開關命令、下行鏈路命令編碼、資料幀以及已知問題。"
tags:
  - 'lora'
  - 'lorawan'
  - 'iot'
source: https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/tg-lr-setup-guide
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

<span id="tg-lr"></span>

## 快速入門指南 {#quickstart-guide}

- 在 LoRaWAN 網路伺服器上註冊裝置。如果裝置型號不受支援，請使用 [`tg-lrx2-2.0-ul-dec.js`](pathname:///assets/tg-lrx2-2.0-ul-dec.js) 載荷解碼指令碼。

- 可選擇部署 Grafana + Influx（[`telemetry_hub.zip`](pathname:///assets/telemetry_hub.zip)）docker 服務，用於裝置能力評估。

- 將磁鐵靠近簧片開關以啟用裝置，並等待 LED 閃爍 2 次（約 1.5 秒）。

## 功能 {#functionality}

:::note

新裝置處於 [SHUTDOWN](#shutdown) 模式。要啟用，請使用[磁鐵開關命令](#mag-sw-cmd)。
:::

<span id="id42"></span>

**Models**

| <span id="model"></span>型號 | 描述 | 感測器 |
| --- | --- | --- |
| <span id="tg-lr82"></span>TG-LR82 | LoRaWAN 1.0.4 Class A, B，863.0 - 869.0 MHz 頻段。 | TMP116N, HDC2010, LIS2DW12 |
| <span id="tg-lr92"></span>TG-LR92 | LoRaWAN 1.0.4 Class A, B，900.0 - 928.0 MHz 頻段。 | TMP116N, HDC2010, LIS2DW12 |

<span id="id43"></span>

**Bands**

| 數字程式碼 | 名稱 | 描述 |
| --- | --- | --- |
| 1 | <span id="band-1ghz"></span>BAND_1GHz | 亞 GHz 工作頻段。頻率範圍取決於裝置 [型號](#model)。 |
| 2 | <span id="band-2ghz"></span>BAND_2GHz | 2.4GHz ISM 頻段。 |

<span id="id44"></span>

**執行模式**

| 數字程式碼 | 模式 | 描述 |
| --- | --- | --- |
| 0 | <span id="shutdown"></span>SHUTDOWN | 裝置處於低功耗模式，所有功能已停用。 |
| 1 | <span id="run"></span>RUN | 裝置加入網路，並根據當前配置檔案與配置傳送上行鏈路。 |

<span id="id45"></span>

**<span id="supported-regions"></span>支援的區域**

| [X-Y 程式碼](#x-y) | [下行鏈路](#lora-set-region) | 通用名稱 | [TG-LR82](#tg-lr82) | [TG-LR92](#tg-lr92) |
| --- | --- | --- | --- | --- |
| 1-1 | 1 | <span id="eu868"></span>EU868 | yes |  |
| 2-1 | 2 | <span id="as923-grp1"></span>AS923_GRP1 |  | Yes |
| 3-1 | 3 | <span id="us915"></span>US915 |  | yes |
| 4-1 | 4 | <span id="au915"></span>AU915 |  | yes |
|  |  | <span id="ww2g4"></span>WW2G4 | Yes | Yes |
| 6-1 | 7 | <span id="as923-grp2"></span>AS923_GRP2 |  | Yes |
| 7-1 | 8 | <span id="as923-grp3"></span>AS923_GRP3 |  | Yes |
| 8-1 | 9 | <span id="in865"></span>IN865 | yes |  |
| 9-1 | 10 | <span id="kr920"></span>KR920 |  | yes |

### LoRaWAN {#lorawan}

裝置支援 Class A 和 B，並且可以在兩個頻段中工作：[BAND_1GHz](#band-1ghz) 和 [BAND_2GHz](#band-2ghz)。
使用者可以配置週期性鏈路檢查、MAC 時間同步（DeviceTimeReq）和網路 ADR。

#### 入網過程 {#join-procedure}

啟用後（[RUN](#run)），裝置將嘗試加入網路。裝置在主頻段傳送 Join-Request，
如果未收到 Join-Accept，它將等待退避間隔，然後在啟用的情況下於次頻段傳送下一個 Join-Request，否則再次在 primary-band 傳送。

:::note

加入嘗試間隔取決於上一次 Join-Request 的空中時間和總加入時間。
參見 [1](#id40) 第 7 節。如果上一次加入請求使用了較慢的資料速率，則預期間隔會更長。
:::

加入配置命令：[lora primary-band](#lora-primary-band)、[lora second-band](#lora-second-band)、[lora join-cfg](#lora-join-cfg)。
關於如何將文字命令轉換為用於下行的二進位制編碼，請參閱 [命令編碼](#command-encoding)。

#### 鏈路檢查 {#link-check}

裝置加入網路後，可以執行可選的週期性鏈路檢查。可以使用 [lora link-chk](#lora-link-chk) 針對每個頻段單獨配置鏈路檢查。如果鏈路檢查失敗，裝置會離開網路並重新啟動加入流程。

:::note

任何網路下行鏈路都會重啟鏈路檢查計時器，以防止不必要的 LinkCheckReq。
:::

#### 時間同步 {#time-synchronization}

裝置支援使用 DeviceTimeReq MAC 命令進行可選的時間同步。有關配置引數或請求立即同步，請參閱命令 [lora clk-sync](#lora-clk-sync)。

#### Class B {#class-b}

裝置支援 Class B 操作。Class B 操作可以透過
[lora class](#lora-class) 手動請求，或者裝置可以配置為在加入網路時使用
[lora cfg-class-b](#lora-cfg-class-b) 自動切換到 class B。

#### ADR 配置 {#adr-configuration}

可以使用 [lora adr-cfg](#lora-adr-cfg) 停用 network ADR 並設定固定資料速率。

#### 離開網路 {#leaving-network}

當出現 [Link Check](#link-check) 或確認的上行鏈路故障時，裝置會離開網路並重新啟動加入流程。

#### 憑證 {#credentials}

裝置具有隨每臺裝置提供的出廠配置預設憑據：[DevEUI](#deveui)、[JoinEUI](#joineui)、[AppKey](#appkey)。

<span id="deveui"></span>DevEUI and <span id="joineui"></span>JoinEUI are IEEE 64-bit EUI ([2](#id41)) written MSB first.
On air byte order is LSB first. See [1](#id40) section 6.2.5.

<span id="appkey"></span>AppKey is 16 byte AES128 encryption key and is written as stored in device memory. AppKey must be kept secret!

要更改 [JoinEUI](#joineui) 和 [AppKey](#appkey)，請使用命令：[lora join-eui](#lora-join-eui)、[lora net-key](#lora-net-key) 和 [lora cred](#lora-cred)。
命令 [lora join-eui](#lora-join-eui) 和 [lora net-key](#lora-net-key) 可按任意順序執行，並可多次執行，以寫入新的待處理
加入憑據。

一旦寫入新的待處理憑據，就可以執行“[lora cred](#lora-cred) 600,1”或“[app reset](#app-reset) 0”以嘗試使用新憑據加入。
如果新憑據未透過 join accept 確認，裝置將恢復到之前的憑據。
有關已知問題，請參見 [LORA-275](#lora-275)、[LORA-276](#lora-276)！

下面示例寫入 JoinEUI 和 AppKey 並嘗試入網：

```none
lora join-eui 87904163,0x00,0x16,0xC0,0x01,0xFF,0xFE,0x00,0x00
lora net-key 87904163,0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F
lora cred 600
app reset 0
// device reboots and attempts join using new credentials with 600s timeout
```

JoinEUI 可從前面的示例中原樣複製/貼上為 00 16 C0 01 FF FE 00 00，以註冊新裝置。
[lora join-eui](#lora-join-eui) 引數為 MSB 在前。

:::warning

執行 *lora cred &lt;confirm-timeout-s&gt;,87904163* 將在不驗證加入嘗試的情況下強制確認憑據！你可能會失去對裝置的訪問許可權！
:::

### 上行鏈路訊息 {#uplink-messages}

每個 LoRaWAN 上行訊息透過將待處理的 [資料幀](#data-frames) ID 及其內容放入 FPort 和
FRMPayload 欄位來形成。所有待處理幀按升序打包，並且對 ID 使用差分編碼。

:::note

有關幀編碼詳細資訊，請參閱 [`tg-lrx2-2.0-ul-dec.js`](pathname:///assets/tg-lrx2-2.0-ul-dec.js) 指令碼。此指令碼可按原樣用於應用伺服器載荷解碼器。
:::

### 遙測 {#telemetry}

#### 裝置配置檔案 {#device-profiles}

裝置有 6 個可配置配置檔案。每個配置檔案獨立儲存感測器和上行傳送配置。
這允許裝置快速更改執行特性，而無需代價高昂的下行配置訊息。
可使用 [裝置命令](#device-commands)、[磁鐵](#mag-sw-cmd)，甚至基於評估後的 [資料規則](#data-rules) 來切換配置檔案。
例如，在每天僅數次上行的週期性 keepalive 模式與每幾分鐘更快速的遙測之間切換。

:::note

MikroTik 可以支援你的特定用例，提供具有自定義預設配置的新裝置。
:::

裝置預配置了評估配置，以展示一些可能的用例：

<span id="id46"></span>

**預設配置檔案配置**

| <span id="profile-number"></span>配置檔案編號 | 名稱 | 描述 |
| --- | --- | --- |
| 0 | Sensor Telemetry | 每 5 分鐘傳送 [current-state](#current-state)、[device-orientation](#device-orientation)。每 60 分鐘傳送其餘遙測資料。 |
| 1 | 活動監測 | 每 60 分鐘傳送 [activity](#activity)、[full-activity](#full-activity)、[current-state](#current-state)，並在活動空閒轉換時傳送 [activity_state](#activity-state) 事件。 |
| 2 | 磁力開關 | 每 60 分鐘傳送 [mag-switch](#mag-switch)、[current-state](#current-state)、[device-events](#device-events)，並在磁鐵被移除至少 15 秒時傳送 [mag_sw_cnt](#mag-sw-cnt) 事件。最多儲存 10 個事件。 |
| 3 | 方向 | 每 60 分鐘傳送 [current-state](#current-state)、[device-events](#device-events)、[device-orientation](#device-orientation)。在空閒約 30 秒後快速旋轉 30 度時傳送 [device-orientation](#device-orientation) 幀。在特定方向時傳送 [angle_1](#angle-1) 事件：V=(0,1,1)。最多儲存 3 個事件。 |
| 4 | 資產監測 | 每 3 小時根據事件傳送包含不同幀的資產健康資訊。 |
| 5 | 空 | |

請參閱 [`default-cfg.txt`](pathname:///assets/tg-lrx2-default-cfg.txt)，以獲取確切的出廠預設配置命令。

#### 配置感測器 {#configuring-sensors}

##### 取樣間隔 {#sampling-intervals}

可以針對特定用例使用 [data poll-cfg](#data-poll-cfg) 命令配置週期性溫度、溼度和電池電壓取樣。
裝置可以以高於上行幀傳送速率的速率對資料進行取樣。這為傳送平均值或執行基於規則的決策提供了機會。由於取樣間隔會影響裝置功耗，因此可以利用這一點來延長使用壽命。

##### 平均 {#averaging}

裝置還會跟蹤以下采樣值的平均值：[temperature_ema](#temperature-ema)、[humidity_ema](#humidity-ema)、[battery_mv_ema](#battery-mv-ema)、[angle_ema](#angle-ema)。命令
[data ema-cfg](#data-ema-cfg) 配置指數移動平均 (<span id="ema"></span>EMA) 週期，並且如果啟用了 *send-ema-**，可選擇將 [EMA](#ema) 值傳送到 [current-state](#current-state)、
[dev-health](#dev-health)、[device-orientation](#device-orientation) 中。

[data ema-cfg](#data-ema-cfg) 中的計數引數 *temp-cnt*、*humid-cnt*、*bat-cnt*、*orient-cnt* 決定用於移動
平均計算的係數 *a*。移動 EMA 根據前一個值 *ema* 和新值 *sample* 計算如下：

```none
ema(t) = sample(t) * a + ema(t-1) * (1 - a)
```

要獲得 EMA 的近似時間常數 *t*，你需要使用由 [data poll-cfg](#data-poll-cfg) 和 [data orient-cfg](#data-orient-cfg) 配置的取樣間隔
(*interval*) 以及相應的計數引數 (*N*)：

```none
t ~ (N + 1) * interval / 2
```

要獲取 [data ema-cfg](#data-ema-cfg) 所需的 `count` 引數值：

```none
N ~ 2 * t / interval - 1
```

示例：

溫度取樣間隔 *th-poll-int* 使用 [data poll-cfg](#data-poll-cfg) 配置為 30s。要將 EMA 配置為時間常數 t ~ 60 分鐘：

```none
temp-cnt = 2 * 3600 / 30 - 1 = 239
```

假設使用配置檔案 #0，並且我們不想更改其他引數，則需要傳送命令：

```none
data ema-cfg 1,239
```

##### 直方圖 {#histogram}

所有周期性取樣都會新增到溫度和溼度直方圖中。直方圖除常規遙測外還可使用，
也可單獨用於監測溫度和溼度分佈。使用 [data temp-histo-cfg](#data-temp-histo-cfg)、
[data humid-histo-cfg](#data-humid-histo-cfg) 命令配置 bin 和 epoch 間隔，和/或啟用 [temp-histogram](#temp-histogram)、[humid-histogram](#humid-histogram) 幀。所有直方圖幀都包含 epoch
編號，以檢測直方圖計數器重設。由於每個 bin 的幀大小限制為 1B，如果內部 bin 計數器值高於 255，直方圖
將針對上行鏈路進行歸一化（機率型別）。

示例配置：

```none
data temp-histo-cfg 1,86400,0,0,1,1,-10,0,10,15,17.5,20,22.5,25.0,30
data humid-histo-cfg 1,86400,0,0,1,1,10,20,30,40,50,60,70,80,90
```

##### 朝向 {#orientation}

![Device accelerometer axis.](/img/f1253ed3d2e4366d.png)

*裝置加速度計軸。*

相對於地球的週期性裝置三維姿態取樣可透過以下命令配置： [data orient-cfg](#data-orient-cfg)。此外，可配置 3 個使用者
方向向量 ref-1、ref-2、ref-3，以檢測特定的裝置姿態。使用者變數 [angle_1](#angle-1)、[angle_2](#angle-2)、
[angle_3](#angle-3) 包含裝置上次取樣姿態與使用者定義向量之間的當前角度。這些變數可用於
Data Rules 中，以在特定姿態時觸發。[angle_ema](#data-rules) 是裝置上次取樣姿態與 [EMA](#angle-ema) 值之間的
角度。此外，還可透過 [major_axis_orientation](#ema) 變數獲取粗略姿態。

<span id="id48"></span>

**[major_axis_orientation](#major-axis-orientation) 描述**

| 值 | 數字程式碼 | 描述 |
| --- | --- | --- |
| XH | 0 | X 向上 |
| HL | 1 | X 向下 |
| YH | 2 | Y 向上 |
| YL | 3 | Y 向下 |
| ZH | 4 | Z 向上 |
| ZL | 5 | Z 向下 |
| DISABLED | 7 | 感測器已停用 |

粗定向的優點是它會在 [current-state](#current-state) 幀中傳送。

##### 活動監測 {#activity-monitor}

裝置具有基於加速度計的活動監控服務。該服務將自動管理一個確定移動/活動的簡單狀態機。[activity_s](#activity-s)、[high_activity_s](#high-activity-s)、[total_activity_s](#total-activity-s) 統計每個狀態中累積的時間，[activity_state](#activity-state)、[activity_state_etm](#activity-state-etm) 儲存狀態資訊。

命令 [data activity-cfg](#data-activity-cfg) 可用於配置活動監控的模式和閾值。[data activity-cal](#data-activity-cal) 可用於
自動執行特定模式的校準。

*level1-th* 和 *level2-th* 的單位是 *1/64 * 2G*，與其他加速度計設定無關（如 *data acc-cfg* 中）。*level2-cnt* 在內部計算，使用者不可配置。*level2-cnt* 始終在 7..15 範圍內，計算如下：

```none
level2-cnt = 7 + round((1 - ((level2-th - level1-th - 1) / 61)) * 8)
```

<span id="id49"></span>

**[activity_state](#activity-state) 描述**

| 數字程式碼 | 值 |
| --- | --- |
| 0 | IDLE |
| 1 | LOW |
| 2 | HIGH |
| 3 | DISABLED |

###### 單模式 {#single-mode}

在 [data activity-cfg](#data-activity-cfg) 中，Mode 設定為 single。

- 如果任一軸上的加速度計取樣值高於 *level1-th*，裝置會從 IDLE 狀態轉換到 LOW 狀態。

- 如果所有采樣值在至少 1.3s 內低於 *level1-th*，裝置會從 LOW 狀態轉換到 IDLE 狀態。

示例：將配置檔案 #0 設定為單模式，閾值為 0.25G：

```none
data activity-cfg 1,1,8,63
```

###### 雙模式 {#dual-mode}

Mode 在 [data activity-cfg](#data-activity-cfg) 中設定為 dual。

在雙模式下，LOW 狀態有兩個子狀態：LOW1 和 LOW2，兩者都表示 LOW。裝置在這兩個狀態期間都會報告 LOW 狀態，並且活動計數器值會像處於 LOW 狀態一樣遞增。唯一的區別是這些狀態之間的轉換邏輯。

<span id="id50"></span>

**[activity_state](#activity-state) 雙模式狀態轉換**

| 當前 | 下一個 | 條件 |
| --- | --- | --- |
| IDLE | LOW2 | sample &gt; *level1-th* |
| LOW2 | LOW1 | sample &lt; *level2-th* 至少 5 秒 |
| LOW1 | LOW2 | sample &gt; *level1-th* |
| LOW2 | HIGH | 取樣值 &gt; *level2-th* 至少 *level2-cnt* 次 |
| LOW1 | IDLE | 取樣值 &lt; *level1-th* 至少 5 秒 |
| HIGH | LOW1 | 取樣值 &lt; *level2-th* 至少 5 秒 |

示例：將配置檔案 #0 設定為雙模式，閾值為 0.25G 和 0.5G：

```none
data activity-cfg 1,2,8,16
```

###### 校準 {#calibration}

除了手動配置 *level1-th* 和 *level2-th* 之外，還有活動校準功能。
執行命令 [data activity-cal](#data-activity-cal) 將對 *cal-level* 執行自動校準。*level-one* 將為 *profile-mask* 中選定的所有配置檔案校準 *level1-th*，
而 *level-two* 將校準 *level2-th*。對於雙模式，您可以依次執行 *level-one* 和
*level-two*。校準時間為 15 秒。此功能最適用於週期性運動/振動。

:::note

在校準過程或活動監視器測試期間啟用 LED 可能有助於確保正確執行。
:::

示例：使用單級活動監測校準配置檔案 #0：

:::warning

在啟用方向的情況下進行活動校準會導致故障和裝置重啟。
校準前使用 [data orient-cfg](#data-orient-cfg) 停用，完成後重新啟用。參見 [LORA-279](#lora-279)。
:::

- 將裝置放置在具有周期性運動/活動的環境中進行校準。

- 傳送命令：

  ```none
  data activity-cfg 1,1,,,1
  data activity-cal 1,1,1
  ```

- 觀察 LED 週期性閃爍 2 次/1.5s，持續約 15s。

- 測試運動檢測。在 LOW 活動期間，裝置將閃爍 LED 3 次/1s。

- 如果校準結果可接受，傳送命令以停用 LED：

  ```none
  data activity-cfg 1,,,,0
  ```

示例：使用雙級活動監測校準配置檔案 #0：

- 將裝置放置在具有周期性運動/活動的環境中進行級別 1 校準。

- 傳送命令：

  ```none
  data activity-cfg 1,2,,,1
  data activity-cal 1,1,1
  ```

- 觀察 LED 週期性閃爍 2 次/1.5s，持續約 15s。

- 將裝置放置在用於級別 2 校準的環境中。

- 傳送命令以校準級別 2：

  ```none
  data activity-cal 1,2,1
  ```

- 觀察 LED 週期性閃爍 2 次/1.5s，持續約 15s。

- 測試運動檢測。在 HIGH 活動期間，裝置將閃爍 LED 6 次/1s。

- 如果校準結果可接受，傳送命令以停用 LED：

  ```none
  data activity-cfg 1,,,,0
  ```

:::note

校準後，可以使用命令 [data activity-cfg](#data-activity-cfg) 手動更改 *level1-th* 和 *level2-th*。
:::

##### 衝擊與自由落體 {#impact-and-free-fall}

命令 [data acc-cfg](#data-acc-cfg) 可用於配置裝置加速度計，以實現基本的撞擊和自由落體檢測。
幀：[motion-events](#motion-events)、[impact-count](#impact-count) 包含相關資料欄位。[current-state](#current-state) 包含 [impact_evnt](#impact-evnt)、
[free_fall_evnt](#free-fall-evnt) 標誌，用於指示新事件。如果更傾向於顯式讀取，可以使用這些標誌。

變數 [impact_cnt](#impact-cnt)、[impact_cnt_x](#impact-cnt-x)、[impact_cnt_y](#impact-cnt-y)、[impact_cnt_z](#impact-cnt-z)、[impact_etm](#impact-etm)、[free_fall_cnt](#free-fall-cnt)、
[free_fall_etm](#free-fall-etm) 允許基於規則的邏輯。

:::warning

如果啟用了 [Activity Monitor](#activity-monitor)，則無法使用衝擊和自由落體檢測，它們將被忽略。
:::

#### 資料規則 {#data-rules}

透過命令可配置最多 32 條自定義使用者規則：[data set-rule](#data-set-rule)、[data del-rule](#data-del-rule)。規則具有測試表達式、可選的輸入規則以及要執行的操作。

新增或覆蓋規則的命令語法：

```none
data set-rule [<rule-num>],<test-expr>,[<input-expr>],[<switch-profile>],[<make-event-0>],[<make-event-1>], [<make-event-2>],[<make-event-3>],[<send-frame-0>],[<send-frame-1>],[<send-frame-2>],[<send-frame-3>],[<clr-timer-mask>]
```

##### 測試表達式 {#test-expression}

&lt;test-expr&gt;: [^] [variable-type](#variable-type) &lt;operator&gt; &lt;argument&gt;

| [^] | 在表示式中使用變數的絕對值 |
| --- | --- |
| [variable-type](#variable-type) | 變數名或 ID |
| &lt;運算子&gt; | &gt;, &gt;=, &lt;, &lt;=, ==, !=, % |
| &lt;引數&gt; | 數值 |

示例：

```none
data set-rule 0,profile == 0
data set-rule 1,^temperature > 30.55
data set-rule 2,impact_etm < 60
```

相同的規則可以使用 [使用者變數](#user-variables) 數字 ID 來給出：

```none
data set-rule 0,0 == 0
data set-rule 1,^8 > 30.55
data set-rule 2,24 < 60
```

##### 輸入表示式 {#input-expression}

如果規則需要依賴其他規則的結果，則使用輸入表示式。這允許基於多個測試表達式構造複雜邏輯。

`<input-expr>: [&][|][!]<input-rule>[<]`

| [&] | &lt;rule-num&gt; 和 &lt;input-rule&gt; 的邏輯與 |
| --- | --- |
| [\|] | &lt;rule-num&gt; 和 &lt;input-rule&gt; 的邏輯或 |
| [!] | 輸入值的邏輯非 |
| &lt;input-rule&gt; | 要作為輸入新增的規則編號 |
| [&lt;] | 使用規則的[組合狀態](#combined-state)作為輸入值，否則使用[本地狀態](#local-state)。 |

以下配置將在磁性開關狀態改變發生在不到 15 秒前，且 [temperature](#current-state) 或 [humidity](#temperature) 超出範圍（-5..55 和 10..90%）時，傳送 [current-state](#humidity) 資料幀：

```none
data del-rule
data set-rule 0,temperature < -5
data set-rule 1,temperature > 55
data set-rule 2,humidity < 10
data set-rule 3,humidity > 90,|0|1|2
data set-rule 4,mag_sw_etm < 15,&3<,,,,,,current-state
```

:::warning

輸入規則按數字順序評估，與 set-rule 命令中的順序無關。
:::

##### 動作 {#actions}

規則 [測試表達式](#test-expression) 的求值結果表示資料規則的 <span id="local-state"></span>本地狀態。本地狀態與可選輸入規則一起求值後表示 <span id="combined-state"></span>組合狀態。

如果 [組合狀態](#combined-state) 變為 TRUE 狀態，則執行可選規則操作：配置檔案切換、事件生成、幀排程、使用者計時器重設。

如果給出了 &lt;switch-profile&gt; 引數，當前配置檔案將被更改。例如，如果溫度
降至 15 C 以下，裝置將切換到配置檔案 5（[裝置配置檔案](#device-profiles)）：

```none
data set-rule 1,temperature < 15,,5
```

每條規則最多可以排程 4 種不同的 [資料幀](#data-frames)：

```none
data set-rule 0,impact_cnt % 10,,,,,,,current-state,device-orientation,dev-health,ema-temp
```

:::note

如果需要傳送超過 4 個幀，可以使用規則鏈。
:::

每條規則最多可生成 4 個不同事件：

```none
data set-rule 0,impact_cnt % 10,,,temperature_ema,humidity_ema,activity_state,timer_1
```

##### 事件 {#events}

[操作](#actions) 可以選擇性地生成事件。事件是帶時間戳的[使用者變數](#user-variables)，會透過 [device-events](#device-events) 幀傳送。事件儲存可以使用 [data event-cfg](#data-event-cfg) 命令配置。如果裝置已使用[時間同步](#time-synchronization)接收到絕對時間，事件將帶有 POSIX 時間戳。這樣可以收集特定的歷史資料以便稍後報告。事件上行鏈路可以定期觸發、基於某些規則觸發，或使用下行命令手動觸發。

### 磁開關 {#magnet-switch}

裝置帶有磁開關，可用於命令輸入或作為磁場感測器。如果不使用，可透過 [mag svc](#pin) 命令完全停用命令輸入，或使用 [PIN](#mag-svc) 對其進行保護。

:::note

每個裝置都附帶唯一的 <span id="pin"></span>PIN 碼。
:::

#### 命令輸入 {#command-input}

使用者必須輸入 1 到 4 位數字的命令序列。每位數字連續輸入。空閒 2.5s 後，有效輸入命令將被執行，裝置使用 LED 指示結果。成功執行的命令以 3 次 0.2s LED 閃爍指示，失敗則以 1s 長 LED 脈衝指示。無效命令會被忽略。

當對裝置施加磁場時，LED 開始以 500ms ON、500ms OFF 的間隔閃爍
（或根據 [mag cfg](#mag-cfg) 配置的 blink-mode）。當 LED 點亮時，內部計數器從 0 開始遞增。
當移除磁場時，計數器值被鎖存為使用者輸入數字。如果再次施加磁場，則開始輸入序列中的下一位數字。
如果輸入數字後的間隔大於 2.5s，則對序列進行求值。

:::note

當基於時間應用輸入碼時，請確保遵循以下公式：T = N - 0.5，其中
N 是從 1 到 9 的輸入數字，T 是施加磁場的時間（秒）。數字之間的間隔
必須小於 2.5s，但大於 200ms。
:::

某些命令需要進入 [PIN](#pin) 模式，而某些命令可以選擇性地受 [PIN](#pin) 模式保護。參見表
[磁開關命令](#mag-sw-cmd)。要進入 [PIN](#pin) 模式，使用者必須輸入裝置隨附的 [PIN](#pin) 數字
序列。進入 [PIN](#pin) 模式後，它將在可配置時間後過期，裝置將返回
正常模式。

:::warning

也可以完全停用 magnet 命令。重新啟用的唯一方法是使用
LoRaWAN 下行命令。如果磁感測器僅用於檢測外部訊號
且不希望或不允許使用者命令，這會很有用。
:::

<span id="mag-sw-cmd"></span>

**磁力開關命令**

| 序號 | PIN 模式 | 命令說明 |
| --- | --- | --- |
| 2 | 可選 | 啟用 - 啟用 [RUN](#run) 模式。 |
| 3-1 | 可選 | 觸發 [current-state](#current-state) 幀上行鏈路。 |
| 4-1-X | 可選 | 切換裝置配置檔案，其中 X 為 [配置檔案編號](#profile-number) + 1 [1..6]。 |
| 4-2-1 | 可選 | 將主頻段設定為 [BAND_1GHz](#band-1ghz)。 |
| 4-2-2 | 可選 | 將主頻段設定為 [BAND_2GHz](#band-2ghz)。 |
| 4-3-1 | 可選 | 啟用輔助頻段。 |
| 4-3-9 | 可選 | 停用輔助頻段。 |
| 6-1 | 可選 | 裝置重啟。 |
| 6-2-9 | 可選 | 停用裝置 - [SHUTDOWN](#shutdown) 模式。 |
| 9-<span id="x-y"></span>X-Y | 可選 | 按 [支援的頻段區域](#supported-regions) 設定 sub GHz 頻段區域。 |
| 6-9-9 | 必需 | 裝置恢復出廠設定。 |
| 3-1-5 | mandatory | 退出 PIN 模式。 |
| A-B-C-D | – | 進入 PIN 模式。A-B-C-D 是裝置出廠 [PIN](#pin) 碼的數字。 |
| 5-3-1 | 可選 | 保留。 |

:::note

數字輸入期間的 LED 指示可以根據裝置配置進行更改。可以使用 [mag cfg](#mag-cfg) 更改或完全停用 LED 指示。
:::

#### 磁感測器 {#magnet-sensor}

磁性感測器始終處於執行狀態（即使在應用命令時也是如此）。該感測器可用於檢測切換事件 [mag_sw_flag](#mag-sw-flag)，或統計這些事件的數量 [mag_sw_cnt](#mag-sw-cnt)。裝置可以報告當前開關狀態、狀態變化次數以及最後一次的時間戳（UNIX/uptime）[mag_switch_ts](#mag-switch-ts)。此外，你還可以基於這些屬性建立規則。

### 命令編碼 {#command-encoding}

裝置命令採用二進位制編碼，以減小下行鏈路訊息大小。我們提供 Python 工具來驗證、編碼並將命令釋出為 LoRaWAN 二進位制下行鏈路訊息。

使用 *pip install tg-lrx2-utils* 從 [PyPI](https://pypi.org/project/tg-lrx2-utils/) 安裝。

用於將 [current-state](#current-state) 和 [activity](#activity) 幀上行鏈路設定為每 600 秒、將 [mag-switch](#mag-switch) 設定為每 43200 秒作為確認訊息的示例配置：

```none
# lora-script.txt
frame set-cfg 1,601,0,0,current-state,activity
frame set-cfg 1,43200,1,0,mag-switch
```

我們可以使用 *tg-lrx2-encode* 將文字命令轉換為用於下行鏈路的二進位制訊息：

```none
tg-lrx2-encode --script ./lora-script.txt --dev-desc ./tg-lrx2-2.0-desc.yml --max-len=50 --out ./lora-pub.yml
```

:::note

[`tg-lrx2-2.0-desc.yml`](pathname:///assets/tg-lrx2-2.0-desc.yml) 包含完整的裝置特性描述，並被其他工具使用。
請確保為特定裝置和 FW 版本使用正確的檔案！
:::

*lora-pub.yml* 將包含用於下行鏈路的序列化二進位制載荷。你可以使用可用的 Web 工具手動排程它們，或使用 *tg-lrx2-pub* 在 The Things Network 上排程它們：

```none
tg-lrx2-pub --host ./ttn-app.yml --dl-msg ./lora-pub.yml device-id
```

示例 TTN 憑證檔案：

```none
# ttn-app.yml
app-id: "ttn-tag-demo@ttn"
host: "eu1.cloud.thethings.industries"
port: 1883
user: "ttn-tag-demo@ttn"
password: "NNSXS.5G..."
```

*tg-lrx2-encode* 也接受 CLI 上的命令字串。這可用於單行或少數幾行命令：

```none
tg-lrx2-encode --cmd $'frame send device-orientation\napp profile 1,0' --dev-desc ./tg-lrx2-2.0-desc.yml --max-len=50 --out ./lora-pub.yml
tg-lrx2-pub --host ./ttn-app.yml --dl-msg ./lora-pub.yml device-id
```

### 裝置命令 {#device-commands}

所有裝置命令由 *group-name* 和 *cmd-name* 組成。可選引數在方括號中給出。對於 *tg-lrx2-encode* 指令碼，引數必須用逗號分隔。*group-name* 和 *cmd-name* 也可以用逗號分隔，但也接受空格。

示例：

```none
app factory-reset <key>,[<fw-def>],<delay-ms>
```

引數 &lt;key&gt; 和 &lt;delay-ms&gt; 是必填項，而 &lt;fw-def&gt; 是可選的，可以省略：

```none
app factory-reset 984651411,,2500
```

每個引數都有有效的輸入範圍和格式。某些引數只允許在引數之間進行特定選擇，或在範圍之間進行選擇。

大多數引數接受整數值。*%f* 表示該引數接受小數值。使用這些值
會導致更大的下行有效載荷，因此如果可能，應優先使用整數值。[variable-type](#variable-type) 表示
該引數接受使用者變數名或相應的整數 ID。[frame-type](#frame-type) 表示該引數
接受資料幀名或整數 ID。*tg-lrx2-encode* 會自動將這些名稱轉換為數字 ID。

#### app set-mode {#app-set-mode}

<strong>app set-mode &lt;mode&gt;</strong>

設定裝置執行模式

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| mode | 0 | <a href="#shutdown">SHUTDOWN</a> |
|  | 1 | <a href="#run">RUN</a> |

  

#### app profile {#app-profile}

<strong>app profile &lt;profile-num&gt;,&lt;make-default&gt;</strong>

切換活動配置檔案，並可選地將其設為預設

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-num | 0..5 | |
| make-default | 0 | no |
|  | 1 | yes |

  

#### app reset {#app-reset}

<strong>app reset &lt;type&gt;</strong>

系統重設

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| type | 0 | 主機板 |
| | 1 | 僅應用 |

  

#### app factory-reset {#app-factory-reset}

<strong>app factory-reset &lt;key&gt;,[&lt;fw-def&gt;],&lt;delay-ms&gt;</strong>

重啟裝置，清除已儲存的配置並恢復為預設設定（可選）

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| key | 984651411 | |
| fw-def | 784565141 | 不應用預設配置 |
| delay-ms | 0..65535 | |

    
  

#### app led {#app-led}

<strong>app led [&lt;enable&gt;]</strong>

配置應用程式 LED 訊號

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| enable | 0 | no |
|  | 1 | yes |

  

#### app set-time {#app-set-time}

<strong>app set-time [&lt;unix-time-s&gt;],&lt;uptime-s&gt;</strong>

設定相對於裝置執行時間的 UNIX 時間

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| unix-time-s | 0..4294967295 | |
| uptime-s | 0..4294967295 | |

    
  

#### lora set-region {#lora-set-region}

<strong>lora set-region &lt;region-code&gt;</strong>

設定 sub GHz 頻段的 LoRaWAN 區域

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| region-code | 1 | EU868 |
| | 2 | AS923-1 |
| | 3 | US915 |
| | 4 | AU915 |
| | 7 | AS923-2 |
| | 8 | AS923-3 |
| | 9 | IN868 |
| | 10 | KR920 |

  

#### lora primary-band {#lora-primary-band}

<strong>lora primary-band &lt;band&gt;</strong>

選擇主頻段

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| band | 1 | &lt;1GHz |
| | 2 | 2.45GHz |

  

#### lora second-band {#lora-second-band}

<strong>lora second-band &lt;mode&gt;</strong>

啟用或停用輔助頻段

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| mode | 0 | 關 |
| | 1 | 開 |

  

#### lora join-cfg {#lora-join-cfg}

<strong>lora join-cfg &lt;band&gt;,&lt;duty&gt;</strong>

為頻段配置加入佔空比

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| band | 1 | &lt;1GHz |
| | 2 | 2.45GHz |
| duty | 0 | 0.1% |
| | 1..254 | |
| | 255 | 1% |

  

#### lora link-chk {#lora-link-chk}

<strong>lora link-chk &lt;band&gt;,&lt;int-minutes&gt;</strong>

設定特定頻段的鏈路檢查間隔和超時

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| band | 1 | &lt;1GHz |
| | 2 | 2.45GHz |
| int-minutes | 0 | 關 |
| | 5..500000 | |

    
  

#### lora adr-cfg {#lora-adr-cfg}

<strong>lora adr-cfg &lt;en-netw-adr&gt;,[&lt;fixed-data-rate&gt;]</strong>

啟用網路 ADR 或配置固定資料速率

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| en-netw-adr | 0 | 關 |
| | 1 | 開 |
| fixed-data-rate | 0..6 | |

    
  

#### lora clk-sync {#lora-clk-sync}

<strong>lora clk-sync [&lt;int-minutes&gt;],[&lt;leap-sec&gt;],&lt;sync-now&gt;,[&lt;retry-s&gt;],[&lt;retry-cnt&gt;]</strong>

絕對時間同步

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| int-minutes | 0 | 關 |
| | 1..65535 | |
| leap-sec | -128..127 | |
| sync-now | 0 | no |
|  | 1 | yes |
| retry-s | 0..255 | |
| retry-cnt | 0..255 | |

    
  

#### lora cfg-class-b {#lora-cfg-class-b}

<strong>lora cfg-class-b [&lt;auto-en&gt;],[&lt;ping-slot-int-s&gt;]</strong>

配置 LoRaWAN Class B

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| auto-en | 0 | 關 |
| | 1 | 開 |
| ping-slot-int-s | 1 | |
| | 2 | |
| | 4 | |
| | 8 | |
| | 16 | |
| | 32 | |
| | 64 | |
| | 128 | |

    
  

#### lora class {#lora-class}

<strong>lora class &lt;class&gt;</strong>

切換 LoRaWAN class

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| class | 0 | A |
| | 1 | B |

  

#### lora join-eui {#lora-join-eui}

<strong>lora join-eui &lt;cred-ch-key&gt;,&lt;eui-0&gt;,&lt;eui-1&gt;,&lt;eui-2&gt;,&lt;eui-3&gt;,&lt;eui-4&gt;,&lt;eui-5&gt;,&lt;eui-6&gt;,&lt;eui-7&gt;</strong>

覆蓋網路 JoinEUI

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| cred-ch-key | 87904163 | |
| eui-0 | 0..255 | |
| eui-1 | 0..255 | |
| eui-2 | 0..255 | |
| eui-3 | 0..255 | |
| eui-4 | 0..255 | |
| eui-5 | 0..255 | |
| eui-6 | 0..255 | |
| eui-7 | 0..255 | |

    
  

#### lora net-key {#lora-net-key}

<strong>lora net-key &lt;cred-ch-key&gt;,&lt;key-0&gt;,&lt;key-1&gt;,&lt;key-2&gt;,&lt;key-3&gt;,&lt;key-4&gt;,&lt;key-5&gt;,&lt;key-6&gt;,&lt;key-7&gt;,&lt;key-8&gt;,&lt;key-9&gt;,&lt;key-10&gt;, &lt;key-11&gt;,&lt;key-12&gt;,&lt;key-13&gt;,&lt;key-14&gt;,&lt;key-15&gt;</strong>

覆蓋網路 AppKey

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| cred-ch-key | 87904163 | |
| key-0 | 0..255 | |
| key-1 | 0..255 | |
| key-2 | 0..255 | |
| key-3 | 0..255 | |
| key-4 | 0..255 | |
| key-5 | 0..255 | |
| key-6 | 0..255 | |
| key-7 | 0..255 | |
| key-8 | 0..255 | |
| key-9 | 0..255 | |
| key-10 | 0..255 | |
| key-11 | 0..255 | |
| key-12 | 0..255 | |
| key-13 | 0..255 | |
| key-14 | 0..255 | |
| key-15 | 0..255 | |

    
  

#### lora cred {#lora-cred}

<strong>lora cred [&lt;confirm-timeout-s&gt;],[&lt;action&gt;]</strong>

使用者網路憑據管理

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| confirm-timeout-s | 60..65535 | 如果未入網則回退 |
| action | 0 | 清除待處理 |
| | 1 | 立即嘗試 |
| | 87904163 | 強制確認 |

  

#### frame send {#frame-send}

<strong>frame send &lt;frame-id&gt;,…</strong>

排程上行幀

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| frame-id | <a href="#frame-type">frame-type</a> |  |

    
  

#### frame set-cfg {#frame-set-cfg}

<strong>frame set-cfg &lt;profile-mask&gt;,[&lt;ul-period-s&gt;],[&lt;confirmed&gt;],[&lt;on-join&gt;],&lt;frame-id&gt;,…</strong>

設定上行鏈路幀配置

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-mask | 1..63 | 位域 |
| ul-period-s | 0 | 關 |
| | 1..65535 | |
| confirmed | 0 | no |
|  | 1 | yes |
| on-join | 0 | no |
|  | 1 | yes |
| frame-id | <a href="#frame-type">frame-type</a> |  |

    
  

#### frame clear-cfg {#frame-clear-cfg}

<strong>frame clear-cfg &lt;profile-mask&gt;</strong>

清除指定配置檔案的所有幀配置（等同於 ‘set-cfg profile-mask,0,0,0,…’）

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-mask | 1..63 | 位域 |

  

#### mag cfg {#mag-cfg}

<strong>mag cfg [&lt;pin-timeout&gt;],[&lt;pin-protect&gt;],[&lt;blink-mode&gt;]</strong>

設定配置

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| pin-timeout | 0..65535 | |
| pin-protect | 0 | 關 |
| | 1 | 開 |
| blink-mode | 0 | 半佔空比 |
| | 1 | 脈衝 |
| | 2 | 關 |

  

#### mag svc {#mag-svc}

<strong>mag svc &lt;new-state&gt;,&lt;key&gt;</strong>

啟用或停用 magnet 命令介面

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| new-state | 0 | 關 |
| | 1 | 開 |
| key | 649864801 | |

    
  

#### data sample {#data-sample}

| <strong>data sample</strong> |
| :-- |
| 強制感測器輪詢 |

  

#### data next-epoch {#data-next-epoch}

<strong>data next-epoch &lt;type&gt;</strong>

手動開始下一個直方圖週期

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| type | | |

    
    
  

#### data poll-cfg {#data-poll-cfg}

<strong>data poll-cfg &lt;profile-mask&gt;,[&lt;th-poll-int&gt;],[&lt;sync-period&gt;],[&lt;on-mag-switch&gt;],[&lt;on-activity-change&gt;],[&lt;on-impact&gt;], [&lt;on-free-fall&gt;],[&lt;on-ul-stale&gt;],[&lt;bat-poll-int&gt;]</strong>

設定資料輪詢配置

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-mask | 1..63 | 位域 |
| th-poll-int | 1..4294967295 | 溫度和溼度 |
| sync-period | 0 | no |
|  | 1 | yes |
| on-mag-switch | 0 | no |
|  | 1 | yes |
| on-activity-change | 0 | no |
|  | 1 | yes |
| on-impact | 0 | no |
|  | 1 | yes |
| on-free-fall | 0 | no |
|  | 1 | yes |
| on-ul-stale | 0 | no |
|  | 1 | yes |
| bat-poll-int | 1..4294967295 | 電池電壓 |

  

#### data temp-histo-cfg {#data-temp-histo-cfg}

<strong>data temp-histo-cfg &lt;profile-mask&gt;,[&lt;epoch-interval-s&gt;],[&lt;epoch-interval-cnt&gt;],[&lt;epoch-max-bin-cnt&gt;], [&lt;frame-on-new-epoch&gt;],[&lt;lim-divider&gt;],[&lt;bin-limit-0&gt;],[&lt;bin-limit-1&gt;],[&lt;bin-limit-2&gt;],[&lt;bin-limit-3&gt;],[&lt;bin-limit-4&gt;], [&lt;bin-limit-5&gt;],[&lt;bin-limit-6&gt;],[&lt;bin-limit-7&gt;],[&lt;bin-limit-8&gt;]</strong>

設定溫度直方圖配置

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-mask | 1..63 | 位域 |
| epoch-interval-s | 0 | 關 |
| | 1..4294967295 | |
| epoch-interval-cnt | 0 | 關 |
| | 1..4294967295 | |
| epoch-max-bin-cnt | 0 | 關 |
| | 1..4294967295 | |
| frame-on-new-epoch | 0 | no |
|  | 1 | yes |
| lim-divider | 1..4294967295 | |
| bin-limit-0 | -128..127 | °C |
| | %f | |
| bin-limit-1 | -128..127 | °C |
| | %f | |
| bin-limit-2 | -128..127 | °C |
| | %f | |
| bin-limit-3 | -128..127 | °C |
| | %f | |
| bin-limit-4 | -128..127 | °C |
| | %f | |
| bin-limit-5 | -128..127 | °C |
| | %f | |
| bin-limit-6 | -128..127 | °C |
| | %f | |
| bin-limit-7 | -128..127 | °C |
| | %f | |
| bin-limit-8 | -128..127 | °C |
| | %f | |

    
  

#### data humid-histo-cfg {#data-humid-histo-cfg}

<strong>data humid-histo-cfg &lt;profile-mask&gt;,[&lt;epoch-interval-s&gt;],[&lt;epoch-interval-cnt&gt;],[&lt;epoch-max-bin-cnt&gt;], [&lt;frame-on-new-epoch&gt;],[&lt;lim-divider&gt;],[&lt;bin-limit-0&gt;],[&lt;bin-limit-1&gt;],[&lt;bin-limit-2&gt;],[&lt;bin-limit-3&gt;],[&lt;bin-limit-4&gt;], [&lt;bin-limit-5&gt;],[&lt;bin-limit-6&gt;],[&lt;bin-limit-7&gt;],[&lt;bin-limit-8&gt;]</strong>

設定溼度直方圖配置

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-mask | 1..63 | 位域 |
| epoch-interval-s | 0 | 關 |
| | 1..4294967295 | |
| epoch-interval-cnt | 0 | 關 |
| | 1..4294967295 | |
| epoch-max-bin-cnt | 0 | 關 |
| | 1..4294967295 | |
| frame-on-new-epoch | 0 | no |
|  | 1 | yes |
| lim-divider | 1..4294967295 | |
| bin-limit-0 | 0..99 | RH% |
| | %f | |
| bin-limit-1 | 0..99 | RH% |
| | %f | |
| bin-limit-2 | 0..99 | RH% |
| | %f | |
| bin-limit-3 | 0..99 | RH% |
| | %f | |
| bin-limit-4 | 0..99 | RH% |
| | %f | |
| bin-limit-5 | 0..99 | RH% |
| | %f | |
| bin-limit-6 | 0..99 | RH% |
| | %f | |
| bin-limit-7 | 0..99 | RH% |
| | %f | |
| bin-limit-8 | 0..99 | RH% |
| | %f | |

    
  

#### data ema-cfg {#data-ema-cfg}

<strong>data ema-cfg &lt;profile-mask&gt;,[&lt;temp-cnt&gt;],[&lt;humid-cnt&gt;],[&lt;bat-cnt&gt;],[&lt;orient-cnt&gt;],[&lt;send-ema-temp&gt;],[&lt;send-ema-humid&gt;], [&lt;send-ema-bat&gt;],[&lt;send-ema-orient&gt;]</strong>

設定指數移動平均 (EMA) 配置

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-mask | 1..63 | 位域 |
| temp-cnt | 1..32766 | a = 2 / (temp-cnt + 1) |
| humid-cnt | 1..32766 | a = 2 / (humid-cnt + 1) |
| bat-cnt | 1..32766 | a = 2 / (bat-cnt + 1) |
| orient-cnt | 1..32766 | a = 2 / (orient-cnt + 1) |
| send-ema-temp | 0 | no |
|  | 1 | yes |
| send-ema-humid | 0 | no |
|  | 1 | yes |
| send-ema-bat | 0 | no |
|  | 1 | yes |
| send-ema-orient | 0 | no |
|  | 1 | yes |

  

#### data activity-cfg {#data-activity-cfg}

<strong>data activity-cfg &lt;profile-mask&gt;,[&lt;mode&gt;],[&lt;level1-th&gt;],[&lt;level2-th&gt;],[&lt;en-led&gt;]</strong>

設定活動監視器配置

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-mask | 1..63 | 位域 |
| mode | 0 | 關 |
| | 1 | single |
| | 2 | dual |
| level1-th | 1..63 | |
| level2-th | 1..63 | |
| en-led | 0 | 關 |
| | 1 | 開 |

  

#### data acc-cfg {#data-acc-cfg}

<strong>data acc-cfg &lt;profile-mask&gt;,[&lt;full-scale&gt;],[&lt;en-impact-x&gt;],[&lt;en-impact-y&gt;],[&lt;en-impact-z&gt;],[&lt;impact-th&gt;],[&lt;impact-dur&gt;], [&lt;en-ff&gt;],[&lt;ff-th&gt;],[&lt;ff-dur&gt;],[&lt;data-rate&gt;],[&lt;filter&gt;],[&lt;lp-mode&gt;],[&lt;low-noise&gt;]</strong>

設定加速度計配置

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-mask | 1..63 | 位域 |
| full-scale | 0 | 2G |
| | 1 | 4G |
| | 2 | 8G |
| | 3 | 16G |
| en-impact-x | 0 | 關 |
| | 1 | 開 |
| en-impact-y | 0 | 關 |
| | 1 | 開 |
| en-impact-z | 0 | 關 |
| | 1 | 開 |
| impact-th | 1..63 | impact-th * full-scale / 64 |
| impact-dur | 0..3 | |
| en-ff | 0 | 關 |
| | 1 | 開 |
| ff-th | 0..7 | |
| ff-dur | 0..63 | |
| data-rate | 2 | Hz |
| | 13 | |
| | 25 | |
| | 500 | |
| | 100 | |
| | 200 | |
| filter | 2 | cutoff = data-rate/filter |
| | 4 | |
| | 10 | |
| | 20 | |
| lp-mode | 0..3 | |
| low-noise | 0 | no |
|  | 1 | yes |

  

#### data orient-cfg {#data-orient-cfg}

<strong>data orient-cfg &lt;profile-mask&gt;,[&lt;enable&gt;],[&lt;max-1G-offset&gt;],[&lt;poll-interval-s&gt;],[&lt;ref-1-x&gt;],[&lt;ref-1-y&gt;],[&lt;ref-1-z&gt;], [&lt;ref-2-x&gt;],[&lt;ref-2-y&gt;],[&lt;ref-2-z&gt;],[&lt;ref-3-x&gt;],[&lt;ref-3-y&gt;],[&lt;ref-3-z&gt;]</strong>

設定方向感知配置

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-mask | 1..63 | 位域 |
| enable | 0 | 關 |
| | 1 | 開 |
| max-1G-offset | 1..20 | |
| poll-interval-s | 1..4294967295 | |
| ref-1-x | -32768..32767 | |
| ref-1-y | -32768..32767 | |
| ref-1-z | -32768..32767 | |
| ref-2-x | -32768..32767 | |
| ref-2-y | -32768..32767 | |
| ref-2-z | -32768..32767 | |
| ref-3-x | -32768..32767 | |
| ref-3-y | -32768..32767 | |
| ref-3-z | -32768..32767 | |

    
  

#### data event-cfg {#data-event-cfg}

<strong>data event-cfg &lt;profile-mask&gt;,[&lt;max-count&gt;],[&lt;send-th&gt;],[&lt;discard&gt;],[&lt;send-all&gt;]</strong>

設定事件儲存配置

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-mask | 1..63 | 位域 |
| max-count | 0 | disabled |
|  | 1..100 |  |
| send-th | 0..65535 | if count &gt;= send-th: send(device-events) |
| discard | 0 | 最舊 | 如果沒有可用空間 |
|  | 1 | newest |
| send-all | 0 | off |
| | 1 | 開 |

  

#### data erase-events {#data-erase-events}

<strong>data erase-events [&lt;num-oldest&gt;]</strong>

擦除最舊的 &lt;num-oldest&gt; 個事件（如已指定），否則擦除全部

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| num-oldest | 0..65535 | |

    
  

#### data del-rule {#data-del-rule}

<strong>data del-rule [&lt;rule-num&gt;]</strong>

如果提供了 &lt;rule-num&gt;，則刪除相應數量的規則，否則刪除全部規則

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| rule-num | 0..31 | |

    
  

#### data set-rule {#data-set-rule}

<strong>data set-rule [&lt;rule-num&gt;],&lt;test-expr&gt;,[&lt;input-expr&gt;],[&lt;switch-profile&gt;],[&lt;make-event-0&gt;],[&lt;make-event-1&gt;], [&lt;make-event-2&gt;],[&lt;make-event-3&gt;],[&lt;send-frame-0&gt;],[&lt;send-frame-1&gt;],[&lt;send-frame-2&gt;],[&lt;send-frame-3&gt;],[&lt;clr-timer-mask&gt;]</strong>

設定資料規則 &lt;rule-num&gt;

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| rule-num | 0..31 | |
| test-expr | | |
| input-expr | | |
| switch-profile | 0..5 | |
| make-event-0 | <a href="#variable-type">variable-type</a> |  |
| make-event-1 | <a href="#variable-type">variable-type</a> |  |
| make-event-2 | <a href="#variable-type">variable-type</a> |  |
| make-event-3 | <a href="#variable-type">variable-type</a> |  |
| send-frame-0 | <a href="#frame-type">frame-type</a> |  |
| send-frame-1 | <a href="#frame-type">frame-type</a> |  |
| send-frame-2 | <a href="#frame-type">frame-type</a> |  |
| send-frame-3 | <a href="#frame-type">frame-type</a> |  |
| clr-timer-mask | 0..15 | |

    
  

#### data timer {#data-timer}

<strong>data timer [&lt;timer_1&gt;],[&lt;timer_2&gt;],[&lt;timer_3&gt;],[&lt;timer_4&gt;]</strong>

設定使用者計時器值

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| timer_1 | 0..4294967295 | <a href="#timer-1">timer_1</a> |
| timer_2 | 0..4294967295 | <a href="#timer-2">timer_2</a> |
| timer_3 | 0..4294967295 | <a href="#timer-3">timer_3</a> |
| timer_4 | 0..4294967295 | <a href="#timer-4">timer_4</a> |

  

#### data activity-cal {#data-activity-cal}

<strong>data activity-cal &lt;profile-mask&gt;,&lt;cal-level&gt;,&lt;cal-led&gt;</strong>

執行活動監視器校準並將結果應用到 profiles

| 引數 | 範圍 | 描述 |
| :-- | :-- | :-- |
| profile-mask | 1..63 | 位域 |
| cal-level | 1 | level-one |
| | 2 | level-two |
| cal-led | 0 | no |
|  | 1 | yes |

  

### 資料幀 {#data-frames}

<span id="frame-type"></span>

| ID | 大小 [B] | 名稱 | 資料欄位 |
| --- | --- | --- | --- |
| 1 | 5 | <span id="current-state"></span>current-state | [temperature](#temperature), [humidity](#humidity), [mag_sw_cnt_u8](#mag-sw-cnt-u8), [major_axis_orientation](#major-axis-orientation), [activity_state](#activity-state), [free_fall_evnt](#free-fall-evnt), [impact_evnt](#impact-evnt), [pending_evnt](#pending-evnt) |
| 2 | variable | <span id="device-events"></span>device-events | [event-list](#event-list) |
| 3 | 11 | <span id="temp-histogram"></span>temp-histogram | [temp_histo_epoch](#temp-histo-epoch), [temp_histo_bin[10]](#temp-histo-bin-10) |
| 4 | 11 | <span id="humid-histogram"></span>humid-histogram | [humid_histo_epoch](#humid-histo-epoch), [humid_histo_bin[10]](#humid-histo-bin-10) |
| 5 | 3 | <span id="device-orientation"></span>device-orientation | [orientation_x](#orientation-x), [orientation_y](#orientation-y), [orientation_z](#orientation-z) |
| 6 | 9 | <span id="full-activity"></span>full-activity | [activity_state](#activity-state), [activity_s](#activity-s), [high_activity_s](#high-activity-s) |
| 7 | 8 | <span id="motion-events"></span>motion-events | [impact_cnt](#impact-cnt), [free_fall_cnt](#free-fall-cnt) |
| 8 | 8 | <span id="mag-switch"></span>mag-switch | [mag_sw_cnt](#mag-sw-cnt), [mag_switch_ts](#mag-switch-ts) |
| 9 | 8 | <span id="impact-count"></span>impact-count | [impact_cnt_u16](#impact-cnt-u16), [impact_cnt_x_u16](#impact-cnt-x-u16), [impact_cnt_y_u16](#impact-cnt-y-u16), [impact_cnt_z_u16](#impact-cnt-z-u16) |
| 10 | 2 | <span id="last-temp"></span>last-temp | [temperature](#temperature) |
| 11 | 2 | <span id="ema-temp"></span>ema-temp | [temperature_ema](#temperature-ema) |
| 12 | 1 | <span id="last-humid"></span>last-humid | [humidity](#humidity) |
| 13 | 1 | <span id="ema-humid"></span>ema-humid | [humidity_ema](#humidity-ema) |
| 14 | 5 | <span id="activity"></span>activity | [activity_state](#activity-state), [total_activity_s](#total-activity-s) |
| 20 | 8 | <span id="dev-time"></span>dev-time | [uptime_s](#uptime-s), [unix_time](#unix-time) |
| 21 | 2 | <span id="dev-health"></span>dev-health | [battery_mv](#battery-mv) |
| 22 | 11 | <span id="version"></span>version | [version_pid](#version-pid), [version_maj](#version-maj), [version_min](#version-min), [version_rev](#version-rev), [version_hash[6]](#version-hash-6) |
| 23 | 11 | <span id="serial-number"></span>serial-number | [serial_number[11]](#serial-number-11) |
| 24 | 10 | <span id="cfg-state"></span>cfg-state | [cfg_app_crc](#cfg-app-crc), [cfg_net_crc](#cfg-net-crc), [cfg_frames_crc](#cfg-frames-crc), [cfg_data_crc](#cfg-data-crc), [cfg_rules_crc](#cfg-rules-crc) |
| 25 | variable | <span id="full-cfg"></span>full-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |
| 26 | variable | <span id="app-cfg"></span>app-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |
| 27 | variable | <span id="net-cfg"></span>net-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |
| 28 | variable | <span id="frame-cfg"></span>frame-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |
| 29 | variable | <span id="data-cfg"></span>data-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |
| 30 | variable | <span id="rules-cfg"></span>rules-cfg | [content-offset](#content-offset), [content-final](#content-final), [content-len](#content-len), [content-binary-blob](#content-binary-blob) |

### 使用者變數 {#user-variables}

<span id="variable-type"></span>

| ID | 大小 [B] | 編碼 | 名稱 | 描述 |
| --- | --- | --- | --- | --- |
| 0 | 1 | u8 | <span id="profile"></span>profile | 當前資料配置 (0..5) |
| 1 | 4 | u32 | <span id="profile-etm"></span>profile_etm | 自上次配置切換以來經過的時間 [s] |
| 2 | 4 | u32 | <span id="daytime-tm"></span>daytime_tm | 自午夜 00:00 GMT 起的秒數，未知時為 0 |
| 3 | 4 | u32 | <span id="unix-time"></span>unix_time | 當前 UNIX 時間，未知時為裝置執行時間 |
| 4 | 4 | u32 | <span id="net-frame-etm"></span>net_frame_etm | 自上次網路上行以來經過的時間 |
| 5 | 1 | bool | <span id="net-joined-flag"></span>net_joined_flag | 網路加入狀態 |
| 6 | 1 | u8 | <span id="net-class"></span>net_class | 當前選定的 LoRaWAN [class](#lora-class) |
| 7 | 1 | u8 | <span id="net-region"></span>net_region | 當前使用的 LoRaWAN [區域程式碼](#lora-set-region) |
| 8 | 2 | f8.8 | <span id="temperature"></span>temperature | 上次測量的溫度 |
| 9 | 2 | f8.8 | <span id="temperature-ema"></span>temperature_ema | 測量溫度的 EMA |
| 10 | 1 | u8 | <span id="humidity"></span>humidity | 上次測量的溼度 |
| 11 | 1 | u8 | <span id="humidity-ema"></span>humidity_ema | 測量溼度的 EMA |
| 12 | 4 | u32 | <span id="mag-sw-cnt"></span>mag_sw_cnt | 磁性開關狀態變化計數器 |
| 13 | 4 | u32 | <span id="mag-sw-etm"></span>mag_sw_etm | 自上次磁性開關變化以來經過的時間 [s] |
| 14 | 1 | bool | <span id="mag-sw-flag"></span>mag_sw_flag | 磁性開關的當前狀態 |
| 15 | 1 | activity | <span id="activity-state"></span>activity_state | 裝置當前活動狀態 |
| 16 | 4 | u32 | <span id="activity-s"></span>activity_s | 低活動（級別 1）狀態計數器 [s] |
| 17 | 4 | u32 | <span id="high-activity-s"></span>high_activity_s | 高活動（級別 2）狀態計數器 [s] |
| 18 | 1 | orient | <span id="major-axis-orientation"></span>major_axis_orientation | 裝置的粗略方向 |
| 19 | 4 | u32 | <span id="impact-cnt-x"></span>impact_cnt_x | X 軸衝擊事件計數器 |
| 20 | 4 | u32 | <span id="impact-cnt-y"></span>impact_cnt_y | Y 軸衝擊事件計數器 |
| 21 | 4 | u32 | <span id="impact-cnt-z"></span>impact_cnt_z | Z 軸衝擊事件計數器 |
| 22 | 4 | u32 | <span id="impact-cnt"></span>impact_cnt | 衝擊事件計數器 |
| 23 | 1 | bool | <span id="impact-evnt"></span>impact_evnt | 衝擊事件標誌，由 [current-state](#current-state)、[motion-events](#motion-events)、[impact-count](#impact-count) 幀清除 |
| 24 | 4 | u32 | <span id="impact-etm"></span>impact_etm | 自上次衝擊事件以來經過的時間 [s] |
| 25 | 4 | u32 | <span id="free-fall-cnt"></span>free_fall_cnt | 自由落體事件計數器 |
| 26 | 1 | bool | <span id="free-fall-evnt"></span>free_fall_evnt | 自由落體事件標誌，由 [current-state](#current-state)、[motion-events](#motion-events) 幀清除 |
| 27 | 4 | u32 | <span id="free-fall-etm"></span>free_fall_etm | 自上次 free-fall 事件以來經過的時間 [s] |
| 28 | 1 | u8 | <span id="angle-1"></span>angle_1 | 當前朝向與使用者 ref-1 向量之間的角度，參見 [資料 orient-cfg](#data-orient-cfg) |
| 29 | 1 | u8 | <span id="angle-2"></span>angle_2 | 當前朝向與使用者 ref-2 向量之間的角度，參見 [資料 orient-cfg](#data-orient-cfg) |
| 30 | 1 | u8 | <span id="angle-3"></span>angle_3 | 當前朝向與使用者 ref-3 向量之間的角度，參見 [資料 orient-cfg](#data-orient-cfg) |
| 31 | 1 | u8 | <span id="angle-ema"></span>angle_ema | 當前朝向與裝置朝向的 EMA 之間的角度 |
| 32 | 2 | u16 | <span id="battery-mv"></span>battery_mv | 最近測量的電池電壓 [mV] |
| 33 | 2 | u16 | <span id="battery-mv-ema"></span>battery_mv_ema | 電池電壓的 EMA [mV] |
| 34 | 2 | u16 | <span id="meta-rule-id"></span>meta_rule_id | 用於傳送帶有規則編號的生成事件的 meta 變數 |
| 35 | 4 | u32 | <span id="timer-1"></span>timer_1 | 可復位、持續向上計數的定時器 [s] |
| 36 | 4 | u32 | <span id="timer-2"></span>timer_2 | 可復位、持續向上計數的定時器 [s] |
| 37 | 4 | u32 | <span id="timer-3"></span>timer_3 | 可復位、持續向上計數的定時器 [s] |
| 38 | 4 | u32 | <span id="timer-4"></span>timer_4 | 可復位、持續向上計數的定時器 [s] |
| 39 | 4 | u32 | <span id="activity-state-etm"></span>activity_state_etm | 自 [activity_state](#activity-state) 狀態變化以來的時間 [s] |

### 幀資料欄位 {#frame-data-fields}

| 大小 [B] | 編碼 | 名稱 | 描述 |
| --- | --- | --- | --- |
| 1 | u8 | <span id="mag-sw-cnt-u8"></span>mag_sw_cnt_u8 | 內部磁開關計數器的 LSB [mag_sw_cnt](#mag-sw-cnt) |
| 1/8 | bool | <span id="pending-evnt"></span>pending_evnt | 指示裝置已儲存事件 |
| 0 |  | <span id="event-list"></span>event-list | 可變長度列表，包含：事件時間戳、程式碼和可選值 |
| 1 | u8 | <span id="temp-histo-epoch"></span>temp_histo_epoch | 溫度直方圖紀元編號 |
| 10 | u8[10] | <span id="temp-histo-bin-10"></span>temp_histo_bin[10] | 溫度直方圖區間計數器值 |
| 1 | u8 | <span id="humid-histo-epoch"></span>humid_histo_epoch | 溼度直方圖紀元編號 |
| 10 | u8[10] | <span id="humid-histo-bin-10"></span>humid_histo_bin[10] | 溼度直方圖區間計數器值 |
| 1 | i8 | <span id="orientation-x"></span>orientation_x | 裝置方向法向量 X 軸 |
| 1 | i8 | <span id="orientation-y"></span>orientation_y | 裝置方向法向量 Y 軸 |
| 1 | i8 | <span id="orientation-z"></span>orientation_z | 裝置方向法向量 Z 軸 |
| 4 | u32 | <span id="mag-switch-ts"></span>mag_switch_ts | 磁開關狀態上次變化的時間戳 |
| 2 | u16 | <span id="impact-cnt-u16"></span>impact_cnt_u16 | 衝擊事件計數器 |
| 2 | u16 | <span id="impact-cnt-x-u16"></span>impact_cnt_x_u16 | X 軸衝擊事件計數器 |
| 2 | u16 | <span id="impact-cnt-y-u16"></span>impact_cnt_y_u16 | Y 軸衝擊事件計數器 |
| 2 | u16 | <span id="impact-cnt-z-u16"></span>impact_cnt_z_u16 | Z 軸衝擊事件計數器 |
| 4 | u32 | <span id="total-activity-s"></span>total_activity_s | 總活動狀態時間（level 1 + level 2） |
| 4 | u32 | <span id="uptime-s"></span>uptime_s | 裝置 FW 執行時間 |
| 2 | u16 | <span id="version-pid"></span>version_pid | TG-LR82:0x0000, TG-LR92:0x0001 |
| 1 | u8 | <span id="version-maj"></span>version_maj | FW 版本主版本號 |
| 1 | u8 | <span id="version-min"></span>version_min | FW 版本次版本號 |
| 1 | u8 | <span id="version-rev"></span>version_rev | FW 版本補丁號 |
| 6 | u8[6] | <span id="version-hash-6"></span>version_hash[6] | FW 版本雜湊 |
| 11 | u8[11] | <span id="serial-number-11"></span>serial_number[11] | 裝置序列號的最後 11 個字元 |
| 2 | u16 | <span id="cfg-app-crc"></span>cfg_app_crc | app 和 mag 配置組的 16 位校驗和 |
| 2 | u16 | <span id="cfg-net-crc"></span>cfg_net_crc | net 配置組的 16 位校驗和 |
| 2 | u16 | <span id="cfg-frames-crc"></span>cfg_frames_crc | frame 配置組的 16 位校驗和 |
| 2 | u16 | <span id="cfg-data-crc"></span>cfg_data_crc | 資料配置組 16 位校驗和 |
| 2 | u16 | <span id="cfg-rules-crc"></span>cfg_rules_crc | 資料規則配置 16 位校驗和 |
| 1/8 | bool | <span id="content-final"></span>content-final | 指示內容最後一塊的標誌 |
| 15/8 | u15 | <span id="content-offset"></span>content-offset | 內容資料的位元組偏移 |
| 1 | u8 | <span id="content-len"></span>content-len | 內容長度 |
| 0 |  | <span id="content-binary-blob"></span>content-binary-blob | 內容塊的二進位制資料 |

### 已知問題 {#known-issues}

| ID | FW | 描述 |
| --- | --- | --- |
| [LORA-275](#lora-275) | 2.0.0 | 在輔助頻段停用時更改憑據不會超時。 |
| [LORA-276](#lora-276) | 2.0.0 | 憑據更改命令超時時間不正確。 |
| [LORA-279](#lora-279) | 2.0.0 | 啟用方向檢測時進行活動校準會導致故障。 |
| [LORA-281](#lora-281) | 2.0.0 - 2.0.1 | 新的 ADR 配置在裝置重新加入或重啟之前不會生效。 |
| [LORA-282](#lora-282) | 2.0.0 - 2.0.1 | 只有 DR0 可作為配置的固定資料速率使用。 |

#### LORA-275 {#lora-275}

**描述：** 如果在停用輔助頻段的情況下發起憑證更改，裝置將不會在入網時超時。裝置將一直嘗試入網，直到成功或重啟。

**解決方法：** 如果新憑據無效，請使用[磁鐵開關命令](#mag-sw-cmd)物理重啟裝置。

#### LORA-276 {#lora-276}

**描述：** 當執行 [lora cred](#lora-cred) 後，裝置在下次加入嘗試時將基於總執行時間而非命令執行時間來超時加入過程。如果執行時間長於 *confirm-timeout-s* 引數，裝置將恰好在一次失敗的加入嘗試後超時。

**解決方法：** 在嘗試更改憑據之前，先執行裝置重設命令 [app reset](#app-reset)。或者手動多次重試更改憑據。

#### LORA-279 {#lora-279}

**描述：** 如果在啟用朝向檢測時執行活動校準，裝置可能發生故障並重啟。

**解決方法：** 在執行活動校準之前，使用 [data orient-cfg](#data-orient-cfg) 停用方向檢測，之後再重新啟用。

#### LORA-281 {#lora-281}

**描述：** 當裝置已加入時，使用 [lora adr-cfg](#lora-adr-cfg) 更改 ADR 設定可能不會生效，直到裝置重新加入或重啟。上行鏈路可能繼續使用之前的 ADR 模式和資料速率。

**解決方法：** 更改 ADR 設定後，使用 [app reset](#app-reset) 重設裝置。

#### LORA-282 {#lora-282}

**描述：** 當 network ADR 被停用時，只有 DR0 可作為已配置的固定資料速率工作。配置任何其他固定資料速率可能不會生效。

**變通方法：** 使用 [lora adr-cfg](#lora-adr-cfg) 啟用網路 ADR。

## 相關文件 {#related-documents}

| 序號 | 名稱 |
| --- | --- |
| <span id="id40"></span>1 | TS001-1.0.4 LoRaWAN® L2 1.0.4 規範 |
| <span id="id41"></span>2 | 64 位全域性識別符號 (EUI-64) 指南 |

export const Anchor = ({id}) => {
  useBrokenLinks().collectAnchor(id);
  return ;
};
