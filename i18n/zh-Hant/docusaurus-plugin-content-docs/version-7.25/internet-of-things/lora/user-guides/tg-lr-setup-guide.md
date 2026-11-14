---
sidebar_key: "internet-of-things/lora/user-guides/tg-lr-setup-guide"
sidebar_position: 4
title: "TG-LR 設定指南"
sidebar_label: "TG-LR 設定指南"
description: "本頁是 MikroTik TG-LR82 和 TG-LR92 LoRaWAN 感測器標籤的設定指南，涵蓋啟用、入網、遙測與感測器配置、磁開關命令、下行鏈路命令編碼、資料幀以及已知問題。"
tags:
  - 'lora'
  - 'lorawan'
  - 'iot'
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/lora/user-guides/tg-lr-setup-guide
captured_at: '2026-11-04T11:18:59+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 快速入門指南 {#quickstart-guide}

- 在 LoRaWAN 網路伺服器上註冊裝置。如果裝置型號不受支援，請使用 [tg-lrx2-2.0-ul-dec.js](pathname:///assets/tg-lrx2-2.0-ul-dec.js) 載荷解碼指令碼。

- 可選：部署 Grafana + Influx（[telemetry_hub.zip](pathname:///assets/telemetry_hub.zip)）Docker 服務，用於評估裝置能力。

- 將磁鐵靠近簧片開關以啟用裝置，並等待 LED 閃爍 2 次（約 1.5 秒）。

## 功能 {#functionality}

新裝置處於 SHUTDOWN 模式。要啟用，請使用磁開關命令。

**表 1 型號**

| 型號 | 描述 | 感測器 |
| --- | --- | --- |
| TG-LR82 | LoRaWAN 1.0.4 Class A、B，863.0 - 869.0 MHz 頻段。 | TMP116N、HDC2010、LIS2DW12 |
| TG-LR92 | LoRaWAN 1.0.4 Class A、B，900.0 - 928.0 MHz 頻段。 | TMP116N、HDC2010、LIS2DW12 |

**表 2 頻段**

| 數字程式碼 | 名稱 | 描述 |
| --- | --- | --- |
| 1 | BAND_1GHz | Sub-GHz 工作頻段。頻率範圍取決於裝置型號。 |
| 2 | BAND_2GHz | 2.4GHz ISM 頻段。 |

**表 3 執行模式**

| 數字程式碼 | 模式 | 描述 |
| --- | --- | --- |
| 0 | SHUTDOWN | 裝置處於低功耗模式，所有功能已停用。 |
| 1 | RUN | 裝置加入網路，並根據當前配置檔案和配置傳送上行鏈路。 |

**表 4 支援的區域**

| X-Y 程式碼 | 下行 | 通用名稱 | TG-LR82 | TG-LR92 |
| --- | --- | --- | --- | --- |
| 1-1 | 1 | EU868 | yes |  |
| 2-1 | 2 | AS923_GRP1 |  | yes |
| 3-1 | 3 | US915 |  | yes |
| 4-1 | 4 | AU915 |  | yes |
|  |  | WW2G4 | yes | yes |
| 6-1 | 7 | AS923_GRP2 |  | yes |
| 7-1 | 8 | AS923_GRP3 |  | yes |
| 8-1 | 9 | IN865 | yes |  |
| 9-1 | 10 | KR920 |  | yes |

### LoRaWAN {#lorawan}

裝置支援 Class A 和 B，並且可在兩個頻段中工作：BAND_1GHz 和 BAND_2GHz。使用者可以配置週期性鏈路檢查、MAC 時間同步（DeviceTimeReq）和網路 ADR。

#### 入網過程 {#join-procedure}

一旦啟用（RUN），裝置將嘗試加入網路。裝置在主頻段上傳送 Join-Request；如果未收到 Join-Accept，它將等待退避間隔，並在啟用輔助頻段時在輔助頻段上傳送下一個 Join-Request，否則再次在主頻段上傳送。

入網嘗試間隔取決於最後一個 Join-Request 的空中時間以及總入網時間。參見 1 第 7 節。如果最後一個入網請求使用了較慢的資料速率，則預計間隔會更長。

入網配置命令：`lora primary-band`、`lora second-band`、`lora join-cfg`。有關如何將文字命令轉換為下行鏈路二進位制編碼，請參見命令編碼。

#### 鏈路檢查 {#link-check}

裝置加入網路後，可以執行可選的週期性鏈路檢查。可以使用 `lora link-chk` 為每個頻段單獨配置鏈路檢查。如果鏈路檢查失敗，裝置會離開網路並重新開始入網過程。

任何網路下行鏈路都會重啟鏈路檢查定時器，以防止不必要的 LinkCheckReq。

#### 時間同步 {#time-synchronization}

裝置支援使用 DeviceTimeReq MAC 命令進行可選的時間同步。有關配置引數或請求立即同步，請參見命令 `lora clk-sync`。

#### Class B {#class-b}

裝置支援 Class B 執行。可以使用 `lora class` 手動請求 Class B 執行，也可以使用 `lora cfg-class-b` 將裝置配置為在入網時自動切換到 Class B。

#### ADR 配置 {#adr-configuration}

可以使用 `lora adr-cfg` 停用網路 ADR 並設定固定資料速率。

#### 離開網路 {#leaving-network}

如果鏈路檢查或確認上行鏈路失敗，裝置會離開網路並重新開始入網過程。

#### 憑證 {#credentials}

裝置具有出廠配置的預設憑證，隨每臺裝置提供：DevEUI、JoinEUI、AppKey。

DevEUI 和 JoinEUI 是 IEEE 64 位 EUI (2)，按 MSB 優先寫入。空中位元組順序為 LSB 優先。參見 1 第 6.2.5 節。

AppKey 是 16 位元組 AES128 加密金鑰，按裝置記憶體中儲存的形式寫入。AppKey 必須保密！

要更改 JoinEUI 和 AppKey，請使用命令：`lora join-eui`、`lora net-key` 和 `lora cred`。命令 `lora join-eui` 和 `lora net-key` 可按任意順序發出，並可多次發出，以寫入新的待處理入網憑證。

寫入新的待處理憑證後，可以執行“lora cred 600,1”或“app reset 0”，以嘗試使用新憑證入網。如果新憑證未透過 Join-Accept 確認，裝置將回退到之前的憑證。已知問題請參見 LORA-275、LORA-276！

下面示例寫入 JoinEUI 和 AppKey 並嘗試入網：

```none
lora join-eui 87904163,0x00,0x16,0xC0,0x01,0xFF,0xFE,0x00,0x00
lora net-key 87904163,0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F
lora cred 600
app reset 0
// device reboots and attempts join using new credentials with 600s timeout
```

上一個示例中的 JoinEUI 可按原樣 00 16 C0 01 FF FE 00 00 複製/貼上，用於註冊新裝置。`lora join-eui` 引數採用 MSB 優先。

:::warning
執行 *lora cred &lt;confirm-timeout-s>,87904163* 將在不驗證入網嘗試的情況下強制確認憑證！你可能會失去對裝置的訪問許可權！
:::

### 上行鏈路訊息 {#uplink-messages}

每個 LoRaWAN 上行鏈路訊息透過將待處理的 Data Frames ID 及其內容放入 FPort 和 FRMPayload 欄位來形成。所有待處理幀按升序打包，並且 ID 使用差分編碼。

有關幀編碼詳情，請參見 `tg-lrx2-2.0-ul-dec.js` 指令碼。該指令碼可直接用於應用伺服器載荷解碼器。

### 遙測 {#telemetry}

#### 裝置配置檔案 {#device-profiles}

裝置有 6 個可配置配置檔案。每個配置檔案儲存獨立的感測器和上行鏈路傳送配置。這使裝置無需昂貴的下行鏈路配置訊息即可快速更改執行特性。配置檔案可以使用裝置命令、磁鐵，甚至基於評估的資料規則進行切換。例如，在每天傳送幾次上行鏈路的週期性保活模式與每隔幾分鐘傳送更快速遙測之間切換。

MikroTik 可以支援你的特定用例；可提供具有自定義預設配置的新裝置。

裝置預配置了評估配置，以展示一些可能的用例：

**表 5 預設配置檔案配置**

| 配置檔案編號 | 名稱 | 描述 |
| --- | --- | --- |
| 0 | 感測器遙測 | 每 5 分鐘傳送 current-state、device-orientation。每 60 分鐘傳送其餘遙測。 |
| 1 | 活動監測 | 每 60 分鐘傳送 activity、full-activity、current-state，並在活動進入空閒狀態轉換時傳送 activity_state 事件。 |
| 2 | 磁開關 | 每 60 分鐘傳送 mag-switch、current-state、device-events，並在磁鐵移除至少 15 秒時傳送 mag_sw_cnt 事件。最多儲存 10 個事件。 |
| 3 | 朝向 | 每 60 分鐘傳送 current-state、device-events、device-orientation。在空閒約 30 秒後發生 30 度快速旋轉時傳送 device-orientation 幀。在特定朝向 V=(0,1,1) 時傳送 angle_1 事件。最多儲存 3 個事件。 |
| 4 | 資產監測 | 每 3 小時根據事件使用不同幀傳送資產健康資訊。 |
| 5 | 空 | |

有關確切的出廠預設配置命令，請參見 `default-cfg.txt`。

#### 配置感測器 {#configuring-sensors}

##### 取樣間隔 {#sampling-intervals}

可以使用 `data poll-cfg` 命令為特定用例配置週期性溫度、溼度和電池電壓取樣。裝置可以以高於上行鏈路幀傳送速率的速率取樣資料。這提供了傳送平均值或執行基於規則的決策的機會。由於取樣間隔會影響裝置功耗，因此可以利用這一點來延長使用壽命。

##### 平均 {#averaging}

裝置還會跟蹤取樣值的平均值：temperature_ema、humidity_ema、battery_mv_ema、angle_ema。命令 `data ema-cfg` 配置指數移動平均（EMA）週期，並且如果啟用了 *send-ema-**，還可選擇在 current-state、dev-health、device-orientation 中傳送 EMA 值。

`data ema-cfg` 中的計數引數 *temp-cnt*、*humid-cnt*、*bat-cnt*、*orient-cnt* 決定用於移動平均計算的係數 *a*。移動 EMA 根據前一個值 *ema* 和新值 *sample* 計算如下：

```none
ema(t) = sample(t) * a + ema(t-1) * (1 - a)
```

要獲得 EMA 的近似時間常數 *t*，需要使用由 `data poll-cfg` 和 `data orient-cfg` 配置的取樣間隔（*interval*）以及相應的計數引數（*N*）：

```none
t ~ (N + 1) * interval / 2
```

要獲得 `data ema-cfg` 所需的計數引數值：

```none
N ~ 2 * t / interval - 1
```

示例：

溫度取樣間隔 *th-poll-int* 使用 `data poll-cfg` 配置為 30s。要配置時間常數 t ~ 60 分鐘的 EMA：

```none
temp-cnt = 2 * 3600 / 30 - 1 = 239
```

假設使用配置檔案 #0，並且我們不想更改其他引數，則需要傳送命令：

```none
data ema-cfg 1,239
```

##### 直方圖 {#histogram}

所有周期性樣本都會新增到溫度和溼度直方圖中。直方圖可與常規遙測一起使用，也可以單獨用於監測溫度和溼度分佈。使用 `data temp-histo-cfg`、`data humid-histo-cfg` 命令配置箱和紀元間隔，和/或啟用 temp-histogram、humid-histogram 幀。所有直方圖幀都包含紀元編號，以檢測直方圖計數器重設。由於幀大小限制為每個箱 1B，如果內部箱計數器值高於 255，直方圖將在上行鏈路中歸一化（機率型別）。

示例配置：

```none
data temp-histo-cfg 1,86400,0,0,1,1,-10,0,10,15,17.5,20,22.5,25.0,30
data humid-histo-cfg 1,86400,0,0,1,1,10,20,30,40,50,60,70,80,90
```

##### 朝向 {#orientation}

![](/img/829309331472d215.webp)

圖 1 裝置加速度計軸。

可以使用命令 `data orient-cfg` 配置相對於地球的週期性裝置 3D 朝向取樣。此外，還可以配置 3 個使用者朝向向量 ref-1、ref-2、ref-3，以檢測特定的裝置朝向。使用者變數 angle_1、angle_2、angle_3 包含裝置最後取樣朝向與使用者定義向量之間的當前角度。這些變數可用於資料規則中，以在特定朝向時觸發。angle_ema 是最後取樣的裝置朝向與樣本 EMA 值之間的角度。此外，還可以透過 major_axis_orientation 變數獲得粗略朝向。

**表 6 major_axis_orientation 描述**

| 值 | 數字程式碼 | 描述 |
| --- | --- | --- |
| XH | 0 | X 向上 |
| HL | 1 | X 向下 |
| YH | 2 | Y 向上 |
| YL | 3 | Y 向下 |
| ZH | 4 | Z 向上 |
| ZL | 5 | Z 向下 |
| DISABLED | 7 | 感測器已停用 |

粗略朝向的優點是它會包含在 current-state 幀中傳送。

##### 活動監測 {#activity-monitor}

裝置具有基於加速度計的活動監測服務。該服務將自動管理一個簡單狀態機，以確定移動/活動。activity_s、high_activity_s、total_activity_s 統計每個狀態中累積的時間，activity_state、activity_state_etm 儲存狀態資訊。

命令 `data activity-cfg` 可用於配置活動監測的模式和閾值。`data activity-cal` 可用於自動執行特定模式的校準。

*level1-th* 和 *level2-th* 的單位是 *1/64 * 2G*，與其他加速度計設定無關（如 *data acc-cfg* 中）。*level2-cnt* 在內部計算，使用者不可配置。*level2-cnt* 始終在 7..15 範圍內，計算如下：

```none
level2-cnt = 7 + round((1 - ((level2-th - level1-th - 1) / 61)) * 8)
```

**表 7 activity_state 描述**

| 數字程式碼 | 值 |
| --- | --- |
| 0 | IDLE |
| 1 | LOW |
| 2 | HIGH |
| 3 | DISABLED |

###### 單模式 {#single-mode}

`data activity-cfg` 中的模式設定為 `single`。

- 如果任一軸上的加速度計取樣值高於 *level1-th*，裝置會從 IDLE 狀態轉換到 LOW 狀態。

- 如果所有采樣值在至少 1.3s 內低於 *level1-th*，裝置會從 LOW 狀態轉換到 IDLE 狀態。

示例：將配置檔案 #0 設定為單模式，閾值為 0.25G：

```none
data activity-cfg 1,1,8,63
```

###### 雙模式 {#dual-mode}

`data activity-cfg` 中的模式設定為 `dual`。

在雙模式下，LOW 狀態有兩個子狀態：LOW1 和 LOW2，兩者都表示 LOW。裝置在這兩個狀態期間都會報告 LOW 狀態，並且活動計數器值會像處於 LOW 狀態一樣遞增。唯一的區別是這些狀態之間的轉換邏輯。

**表 8 activity_state 雙模式狀態轉換**

| 當前 | 下一個 | 條件 |
| --- | --- | --- |
| IDLE | LOW2 | sample > *level1-th* |
| LOW2 | LOW1 | sample &lt; *level2-th* 至少 5s |
| LOW1 | LOW2 | sample > *level1-th* |
| LOW2 | HIGH | sample > *level2-th* 至少 *level2-cnt* 次 |
| LOW1 | IDLE | sample &lt; *level1-th* 至少 5s |
| HIGH | LOW1 | sample &lt; *level2-th* 至少 5s |

示例：將配置檔案 #0 設定為雙模式，閾值為 0.25G 和 0.5G：

```none
data activity-cfg 1,2,8,16
```

###### 校準 {#calibration}

除了手動配置 *level1-th* 和 *level2-th* 外，還有活動校準功能。執行命令 `data activity-cal` 將執行 *cal-level* 的自動校準。*level-one* 將校準 *level1-th*，*level-two* 將校準 *level2-th*，適用於 *profile-mask* 中選擇的所有配置檔案。對於雙模式，可以依次執行 *level-one* 和 *level-two*。校準時間為 15s。此功能主要適用於週期性運動/振動。

在校準過程或活動監測測試期間啟用 LED 可能有助於確保正確執行。

示例：使用單級活動監測校準配置檔案 #0：

:::warning
啟用朝向時進行活動校準會導致故障和裝置重啟。校準前使用 `data orient-cfg` 停用，完成後重新啟用。參見 LORA-279。
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

校準後，可以使用命令 `data activity-cfg` 手動更改 *level1-th* 和 *level2-th*。

##### 衝擊與自由落體 {#impact-and-free-fall}

命令 `data acc-cfg` 可用於配置裝置加速度計以進行基本衝擊和自由落體檢測。幀：motion-events、impact-count 包含相關資料欄位。current-state 包含 impact_evnt、free_fall_evnt 標誌，用於指示新事件。如果更傾向於顯式讀取，可以使用這些標誌。

變數 impact_cnt、impact_cnt_x、impact_cnt_y、impact_cnt_z、impact_etm、free_fall_cnt、free_fall_etm 允許基於規則的邏輯。

如果啟用了活動監測，則無法使用衝擊和自由落體檢測，這些檢測將被忽略。

#### 資料規則 {#data-rules}

最多可使用命令配置 32 條自定義使用者規則：`data set-rule`、`data del-rule`。規則具有測試表達式、可選輸入規則和要執行的動作。

新增或覆蓋規則的命令語法：

```none
data set-rule [<rule-num>],<test-expr>,[<input-expr>],[<switch-profile>],[<make-event-0>],[<make-event-1>], [<make-event-2>],[<make-event-3>],[<send-frame-0>],[<send-frame-1>],[<send-frame-2>],[<send-frame-3>],[<clr-timer-mask>]
```

##### 測試表達式 {#test-expression}

&lt;test-expr&gt;: [^] variable-type &lt;operator> &lt;argument>

| [^] | 在表示式中使用變數絕對值 |
| --- | --- |
| variable-type | 變數名或 ID |
| &lt;operator> | >, >=, &lt;, &lt;=, ==, !=, % |
| &lt;argument> | 數值 |

示例：

```none
data set-rule 0,profile == 0
data set-rule 1,^temperature > 30.55
data set-rule 2,impact_etm < 60
```

相同的規則可以使用使用者變數數字 ID 給出：

```none
data set-rule 0,0 == 0
data set-rule 1,^8 > 30.55
data set-rule 2,24 < 60
```

##### 輸入表示式 {#input-expression}

如果規則需要依賴其他規則的結果，則使用輸入表示式。這允許基於多個測試表達式構造複雜邏輯。

&lt;input-expr&gt;: [&][|][!]&lt;input-rule>[&lt;]

| [&] | &lt;rule-num> 和 &lt;input-rule> 的邏輯與 |
| --- | --- |
| [\|] | &lt;rule-num> 和 &lt;input-rule> 的邏輯或 |
| [!] | 輸入值的邏輯非 |
| &lt;input-rule> | 要作為輸入新增的規則編號 |
| [&lt;] | 使用規則組合狀態作為輸入值，否則使用本地狀態。 |

以下配置將在磁開關狀態在 15s 內發生變化且溫度或溼度超出範圍（-5..55 和 10..90%）時傳送 current-state 資料幀：

```none
data del-rule
data set-rule 0,temperature < -5
data set-rule 1,temperature > 55
data set-rule 2,humidity < 10
data set-rule 3,humidity > 90,|0|1|2
data set-rule 4,mag_sw_etm < 15,&3<,,,,,,current-state
```

輸入規則按數字順序評估，與 `set-rule` 命令中的順序無關。

##### 動作 {#actions}

規則測試表達式的評估值表示資料規則本地狀態。使用可選輸入規則評估的本地狀態表示組合狀態。

如果組合狀態變為 TRUE 狀態，則執行可選規則動作：配置檔案切換、事件生成、幀排程、使用者定時器重設。

如果給出了 &lt;switch-profile> 引數，則將更改當前配置檔案。例如，如果溫度降到 15 C 以下，裝置將切換到配置檔案 5（裝置配置檔案）：

```none
data set-rule 1,temperature < 15,,5
```

每條規則最多可排程 4 個不同的資料幀：

```none
data set-rule 0,impact_cnt % 10,,,,,,,current-state,device-orientation,dev-health,ema-temp
```

如果需要傳送超過 4 個幀，可以使用規則鏈。

每條規則最多可生成 4 個不同事件：

```none
data set-rule 0,impact_cnt % 10,,,temperature_ema,humidity_ema,activity_state,timer_1
```

##### 事件 {#events}

動作可以選擇生成事件。事件是帶時間戳的使用者變數，會在 device-events 幀中傳送。可以使用 `data event-cfg` 命令配置事件儲存。如果裝置已使用時間同步接收到絕對時間，事件將具有 POSIX 時間戳。這允許收集特定歷史資料以便稍後報告。事件上行鏈路可以週期性觸發、基於某些規則觸發，或使用下行鏈路命令手動觸發。

### 磁開關 {#magnet-switch}

裝置具有磁開關，可用於命令輸入或作為磁場感測器。如果未使用，可以使用 `mag svc` 命令完全停用命令輸入或對其進行 PIN 保護。

每臺裝置都帶有唯一 PIN 碼。

#### 命令輸入 {#command-input}

使用者必須輸入 1 到 4 位數字的命令序列。每位數字連續輸入。空閒 2.5s 後，有效輸入命令將被執行，裝置使用 LED 指示結果。成功執行的命令以 3 次 0.2s LED 閃爍指示，失敗則以 1s 長 LED 脈衝指示。無效命令會被忽略。

當向裝置施加磁場時，LED 開始以 500ms 亮、500ms 滅的間隔閃爍（或根據 `mag cfg` 配置的 blink-mode）。當 LED 點亮時，內部計數器從 0 開始遞增。當移除磁場時，計數器值被鎖存為使用者輸入數字。如果再次施加磁場，則開始輸入序列中的下一位數字。如果施加數字後的間隔大於 2.5s，則評估該序列。

基於時間施加輸入程式碼時，請確保遵循以下公式：T = N - 0.5，其中 N 是 1 到 9 的輸入數字，T 是施加磁場的秒數。數字之間的間隔必須小於 2.5s，但大於 200ms。

某些命令需要進入 PIN 模式，某些命令可以選擇由 PIN 模式保護。參見表 磁開關命令。要進入 PIN 模式，使用者必須輸入裝置隨附的 PIN 數字序列。進入 PIN 模式後，它將在可配置時間後過期，裝置將返回正常模式。

也可以完全停用磁命令。重新啟用的唯一方法是使用 LoRaWAN 下行鏈路命令。如果磁感測器僅用於檢測外部訊號，並且不期望或不允許使用者命令，這將很有用。

**表 9 磁開關命令**

| 序列 | PIN 模式 | 命令描述 |
| --- | --- | --- |
| 2 | 可選 | 啟用 - 啟用 RUN 模式。 |
| 3-1 | 可選 | 觸發 current-state 幀上行鏈路。 |
| 4-1-X | 可選 | 切換裝置配置檔案，其中 X 為配置檔案編號 + 1 [1..6]。 |
| 4-2-1 | 可選 | 將主頻段設定為 BAND_1GHz。 |
| 4-2-2 | 可選 | 將主頻段設定為 BAND_2GHz。 |
| 4-3-1 | 可選 | 啟用輔助頻段。 |
| 4-3-9 | 可選 | 停用輔助頻段。 |
| 6-1 | 可選 | 裝置重啟。 |
| 6-2-9 | 可選 | 停用裝置 - SHUTDOWN 模式。 |
| 9-X-Y | 可選 | 按照支援的區域設定 sub GHz 頻段的區域。 |
| 6-9-9 | 必需 | 裝置恢復出廠設定。 |
| 3-1-5 | 必需 | 退出 PIN 模式。 |
| A-B-C-D | – | 進入 PIN 模式。A-B-C-D 是裝置出廠 PIN 碼的數字。 |
| 5-3-1 | 可選 | 保留。 |

數字輸入期間的 LED 指示可根據裝置配置進行更改。可以使用 `mag cfg` 更改或完全停用 LED 指示。

#### 磁感測器 {#magnet-sensor}

磁感測器始終執行（即使應用了命令）。該感測器可用於檢測開關事件 mag_sw_flag 或統計這些事件的數量 mag_sw_cnt。裝置可以報告當前開關狀態、狀態變化次數和最後時間戳（UNIX/uptime）mag_switch_ts。此外，你可以基於這些屬性建立規則。

### 命令編碼 {#command-encoding}

裝置命令採用二進位制編碼，以減小下行鏈路訊息大小。我們提供 Python 工具來驗證、編碼並將命令釋出為 LoRaWAN 二進位制下行鏈路訊息。

[tg-lrx2-utils.zip](pathname:///assets/tg-lrx2-utils.zip) 或使用 *pip install tg-lrx2-utils* 安裝

示例配置：每 600 秒傳送 current-state 和 activity 幀上行鏈路，每 43200 秒傳送 mag-switch，作為確認訊息：

```none
# lora-script.txt
frame set-cfg 1,601,0,0,current-state,activity
frame set-cfg 1,43200,1,0,mag-switch
```

我們可以使用 *tg-lrx2-encode* 將文字命令轉換為用於下行鏈路的二進位制訊息：

```none
tg-lrx2-encode --script ./lora-script.txt --dev-desc ./tg-lrx2-2.0-desc.yml --max-len=50 --out ./lora-pub.yml
```

[tg-lrx2-2.0-desc.yml](pathname:///assets/tg-lrx2-2.0-desc.yml) 包含完整的裝置特性描述，並供其他工具使用。請確保為特定裝置和 FW 版本使用正確的檔案！

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

引數 &lt;key> 和 &lt;delay-ms> 是必需的，但 &lt;fw-def> 是可選的，可以省略：

```none
app factory-reset 984651411,,2500
```

每個引數都有有效的輸入範圍和格式。某些引數只允許在引數之間進行特定選擇，或在範圍之間進行選擇。

大多數引數接受整數值。*%f* 表示引數接受小數值。使用這些值會導致更大的下行鏈路載荷，因此如果可能，應優先使用整數值。variable-type 表示引數接受使用者變數名或相應的整數 ID。frame-type 表示引數接受資料幀名或整數 ID。*tg-lrx2-encode* 會自動將這些名稱轉換為數字 ID。

#### app set-mode {#app-set-mode}

| app set-mode &lt;mode> | | |
| --- | --- | --- |
| 設定裝置執行模式 | | |
| 引數 | 範圍 | 描述 |
| mode | 0 | SHUTDOWN |
| | 1 | RUN |

#### app profile {#app-profile}

| app profile &lt;profile-num>,&lt;make-default> | | |
| --- | --- | --- |
| 切換活動配置檔案，並可選設為預設 | | |
| 引數 | 範圍 | 描述 |
| profile-num | 0..5 | |
| make-default | 0 | no |
|  | 1 | yes |

#### app reset {#app-reset}

| app reset &lt;type> | | |
| --- | --- | --- |
| 系統復位 | | |
| 引數 | 範圍 | 描述 |
| type | 0 | 主機板 |
| | 1 | 僅應用 |

#### app factory-reset {#app-factory-reset}

| app factory-reset &lt;key>,[&lt;fw-def>],&lt;delay-ms> | | |
| --- | --- | --- |
| 重啟裝置，清除已儲存配置並設定為預設值（可選） | | |
| 引數 | 範圍 | 描述 |
| key | 984651411 | |
| fw-def | 784565141 | 不應用預設配置 |
| delay-ms | 0..65535 | |

#### app led {#app-led}

| app led [&lt;enable>] | | |
| --- | --- | --- |
| 配置應用 LED 訊號 | | |
| 引數 | 範圍 | 描述 |
| enable | 0 | no |
|  | 1 | yes |

#### app set-time {#app-set-time}

| app set-time [&lt;unix-time-s>],&lt;uptime-s> | | |
| --- | --- | --- |
| 設定相對於裝置執行時間的 UNIX 時間 | | |
| 引數 | 範圍 | 描述 |
| unix-time-s | 0..4294967295 | |
| uptime-s | 0..4294967295 | |

#### lora set-region {#lora-set-region}

| lora set-region &lt;region-code> | | |
| --- | --- | --- |
| 設定 sub GHz 頻段的 LoRaWAN 區域 | | |
| 引數 | 範圍 | 描述 |
| region-code | 1 | EU868 |
| | 2 | AS923-1 |
| | 3 | US915 |
| | 4 | AU915 |
| | 7 | AS923-2 |
| | 8 | AS923-3 |
| | 9 | IN868 |
| | 10 | KR920 |

#### lora primary-band {#lora-primary-band}

| lora primary-band &lt;band> | | |
| --- | --- | --- |
| 選擇主頻段 | | |
| 引數 | 範圍 | 描述 |
| band | 1 | &lt;1GHz |
| | 2 | 2.45GHz |

#### lora second-band {#lora-second-band}

| lora second-band &lt;mode> | | |
| --- | --- | --- |
| 啟用或停用輔助頻段 | | |
| 引數 | 範圍 | 描述 |
| mode | 0 | 關 |
| | 1 | 開 |

#### lora join-cfg {#lora-join-cfg}

| lora join-cfg &lt;band>,&lt;duty> | | |
| --- | --- | --- |
| 配置頻段的入網佔空比 | | |
| 引數 | 範圍 | 描述 |
| band | 1 | &lt;1GHz |
| | 2 | 2.45GHz |
| duty | 0 | 0.1% |
| | 1..254 | |
| | 255 | 1% |

#### lora link-chk {#lora-link-chk}

| lora link-chk &lt;band>,&lt;int-minutes> | | |
| --- | --- | --- |
| 設定特定頻段的鏈路檢查間隔和超時 | | |
| 引數 | 範圍 | 描述 |
| band | 1 | &lt;1GHz |
| | 2 | 2.45GHz |
| int-minutes | 0 | 關 |
| | 5..500000 | |

#### lora adr-cfg {#lora-adr-cfg}

| lora adr-cfg &lt;en-netw-adr>,[&lt;fixed-data-rate>] | | |
| --- | --- | --- |
| 啟用網路 ADR 或配置固定資料速率 | | |
| 引數 | 範圍 | 描述 |
| en-netw-adr | 0 | 關 |
| | 1 | 開 |
| fixed-data-rate | 0..6 | |

#### lora clk-sync {#lora-clk-sync}

| lora clk-sync [&lt;int-minutes>],[&lt;leap-sec>],&lt;sync-now>,[&lt;retry-s>],[&lt;retry-cnt>] | | |
| --- | --- | --- |
| 絕對時間同步 | | |
| 引數 | 範圍 | 描述 |
| int-minutes | 0 | 關 |
| | 1..65535 | |
| leap-sec | -128..127 | |
| sync-now | 0 | no |
|  | 1 | yes |
| retry-s | 0..255 | |
| retry-cnt | 0..255 | |

#### lora cfg-class-b {#lora-cfg-class-b}

| lora cfg-class-b [&lt;auto-en>],[&lt;ping-slot-int-s>] | | |
| --- | --- | --- |
| 配置 LoRaWAN Class B | | |
| 引數 | 範圍 | 描述 |
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

| lora class &lt;class> | | |
| --- | --- | --- |
| 切換 LoRaWAN class | | |
| 引數 | 範圍 | 描述 |
| class | 0 | A |
| | 1 | B |

#### lora join-eui {#lora-join-eui}

| lora join-eui &lt;cred-ch-key>,&lt;eui-0>,&lt;eui-1>,&lt;eui-2>,&lt;eui-3>,&lt;eui-4>,&lt;eui-5>,&lt;eui-6>,&lt;eui-7> | | |
| --- | --- | --- |
| 覆蓋網路 JoinEUI | | |
| 引數 | 範圍 | 描述 |
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

| lora net-key &lt;cred-ch-key>,&lt;key-0>,&lt;key-1>,&lt;key-2>,&lt;key-3>,&lt;key-4>,&lt;key-5>,&lt;key-6>,&lt;key-7>,&lt;key-8>,&lt;key-9>,&lt;key-10>, &lt;key-11>,&lt;key-12>,&lt;key-13>,&lt;key-14>,&lt;key-15> | | |
| --- | --- | --- |
| 覆蓋網路 AppKey | | |
| 引數 | 範圍 | 描述 |
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

| lora cred [&lt;confirm-timeout-s>],[&lt;action>] | | |
| --- | --- | --- |
| 使用者網路憑證管理 | | |
| 引數 | 範圍 | 描述 |
| confirm-timeout-s | 60..65535 | 如果未入網則回退 |
| action | 0 | 清除待處理 |
| | 1 | 立即嘗試 |
| | 87904163 | 強制確認 |

#### frame send {#frame-send}

| frame send &lt;frame-id>,… | | |
| --- | --- | --- |
| 排程上行鏈路幀 | | |
| 引數 | 範圍 | 描述 |
| frame-id | frame-type | |

#### frame set-cfg {#frame-set-cfg}

| frame set-cfg &lt;profile-mask>,[&lt;ul-period-s>],[&lt;confirmed>],[&lt;on-join>],&lt;frame-id>,… | | |
| --- | --- | --- |
| 設定上行鏈路幀配置 | | |
| 引數 | 範圍 | 描述 |
| profile-mask | 1..63 | 位域 |
| ul-period-s | 0 | 關 |
| | 1..65535 | |
| confirmed | 0 | no |
|  | 1 | yes |
| on-join | 0 | no |
|  | 1 | yes |
| frame-id | frame-type | |

#### frame clear-cfg {#frame-clear-cfg}

| frame clear-cfg &lt;profile-mask> | | |
| --- | --- | --- |
| 清除指定配置檔案的所有幀配置（等同於 ‘set-cfg profile-mask,0,0,0,…’） | | |
| 引數 | 範圍 | 描述 |
| profile-mask | 1..63 | 位域 |

#### mag cfg {#mag-cfg}

| mag cfg [&lt;pin-timeout>],[&lt;pin-protect>],[&lt;blink-mode>] | | |
| --- | --- | --- |
| 設定配置 | | |
| 引數 | 範圍 | 描述 |
| pin-timeout | 0..65535 | |
| pin-protect | 0 | 關 |
| | 1 | 開 |
| blink-mode | 0 | 半佔空比 |
| | 1 | 脈衝 |
| | 2 | 關 |

#### mag svc {#mag-svc}

| mag svc &lt;new-state>,&lt;key> | | |
| --- | --- | --- |
| 啟用或停用磁命令介面 | | |
| 引數 | 範圍 | 描述 |
| new-state | 0 | 關 |
| | 1 | 開 |
| key | 649864801 | |

#### data sample {#data-sample}

| 資料示例 |
| --- |
| 強制感測器輪詢 |

#### data next-epoch {#data-next-epoch}

| data next-epoch &lt;type> | | |
| --- | --- | --- |
| 手動開始下一個直方圖紀元 | | |
| 引數 | 範圍 | 描述 |
| type | | |

#### data poll-cfg {#data-poll-cfg}

| data poll-cfg &lt;profile-mask>,[&lt;th-poll-int>],[&lt;sync-period>],[&lt;on-mag-switch>],[&lt;on-activity-change>],[&lt;on-impact>], [&lt;on-free-fall>],[&lt;on-ul-stale>],[&lt;bat-poll-int>] | | |
| --- | --- | --- |
| 設定資料輪詢配置 | | |
| 引數 | 範圍 | 描述 |
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

| data temp-histo-cfg &lt;profile-mask>,[&lt;epoch-interval-s>],[&lt;epoch-interval-cnt>],[&lt;epoch-max-bin-cnt>], [&lt;frame-on-new-epoch>],[&lt;lim-divider>],[&lt;bin-limit-0>],[&lt;bin-limit-1>],[&lt;bin-limit-2>],[&lt;bin-limit-3>],[&lt;bin-limit-4>], [&lt;bin-limit-5>],[&lt;bin-limit-6>],[&lt;bin-limit-7>],[&lt;bin-limit-8>] | | |
| --- | --- | --- |
| 設定溫度直方圖配置 | | |
| 引數 | 範圍 | 描述 |
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

| data humid-histo-cfg &lt;profile-mask>,[&lt;epoch-interval-s>],[&lt;epoch-interval-cnt>],[&lt;epoch-max-bin-cnt>], [&lt;frame-on-new-epoch>],[&lt;lim-divider>],[&lt;bin-limit-0>],[&lt;bin-limit-1>],[&lt;bin-limit-2>],[&lt;bin-limit-3>],[&lt;bin-limit-4>], [&lt;bin-limit-5>],[&lt;bin-limit-6>],[&lt;bin-limit-7>],[&lt;bin-limit-8>] | | |
| --- | --- | --- |
| 設定溼度直方圖配置 | | |
| 引數 | 範圍 | 描述 |
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

| data ema-cfg &lt;profile-mask>,[&lt;temp-cnt>],[&lt;humid-cnt>],[&lt;bat-cnt>],[&lt;orient-cnt>],[&lt;send-ema-temp>],[&lt;send-ema-humid>], [&lt;send-ema-bat>],[&lt;send-ema-orient>] | | |
| --- | --- | --- |
| 設定指數移動平均（EMA）配置 | | |
| 引數 | 範圍 | 描述 |
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

| data activity-cfg &lt;profile-mask>,[&lt;mode>],[&lt;level1-th>],[&lt;level2-th>],[&lt;en-led>] | | |
| --- | --- | --- |
| 設定活動監測配置 | | |
| 引數 | 範圍 | 描述 |
| profile-mask | 1..63 | 位域 |
| mode | 0 | 關 |
| | 1 | single |
| | 2 | dual |
| level1-th | 1..63 | |
| level2-th | 1..63 | |
| en-led | 0 | 關 |
| | 1 | 開 |

#### data acc-cfg {#data-acc-cfg}

| data acc-cfg &lt;profile-mask>,[&lt;full-scale>],[&lt;en-impact-x>],[&lt;en-impact-y>],[&lt;en-impact-z>],[&lt;impact-th>],[&lt;impact-dur>], [&lt;en-ff>],[&lt;ff-th>],[&lt;ff-dur>],[&lt;data-rate>],[&lt;filter>],[&lt;lp-mode>],[&lt;low-noise>] | | |
| --- | --- | --- |
| 設定加速度計配置 | | |
| 引數 | 範圍 | 描述 |
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

| data orient-cfg &lt;profile-mask>,[&lt;enable>],[&lt;max-1G-offset>],[&lt;poll-interval-s>],[&lt;ref-1-x>],[&lt;ref-1-y>],[&lt;ref-1-z>], [&lt;ref-2-x>],[&lt;ref-2-y>],[&lt;ref-2-z>],[&lt;ref-3-x>],[&lt;ref-3-y>],[&lt;ref-3-z>] | | |
| --- | --- | --- |
| 設定朝向感測配置 | | |
| 引數 | 範圍 | 描述 |
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

| data event-cfg &lt;profile-mask>,[&lt;max-count>],[&lt;send-th>],[&lt;discard>],[&lt;send-all>] | | | |
| --- | --- | --- | --- |
| 設定事件儲存配置 | | | |
| 引數 | 範圍 | 描述 | |
| profile-mask | 1..63 | 位域 | |
| max-count | 0 | 已停用 | |
| | 1..100 | | |
| send-th | 0..65535 | 如果 count >= send-th：send(device-events) | |
| discard | 0 | 最舊 | 如果沒有可用空間 |
| | 1 | 最新 | |
| send-all | 0 | 關 | |
| | 1 | 開 | |

#### data erase-events {#data-erase-events}

| data erase-events [&lt;num-oldest>] | | |
| --- | --- | --- |
| 如果提供 &lt;num-oldest>，則擦除該數量的事件；否則擦除全部 | | |
| 引數 | 範圍 | 描述 |
| num-oldest | 0..65535 | |

#### data del-rule {#data-del-rule}

| data del-rule [&lt;rule-num>] | | |
| --- | --- | --- |
| 如果提供 &lt;rule-num>，則刪除該數量的規則；否則刪除全部 | | |
| 引數 | 範圍 | 描述 |
| rule-num | 0..31 | |

#### data set-rule {#data-set-rule}

| data set-rule [&lt;rule-num>],&lt;test-expr>,[&lt;input-expr>],[&lt;switch-profile>],[&lt;make-event-0>],[&lt;make-event-1>], [&lt;make-event-2>],[&lt;make-event-3>],[&lt;send-frame-0>],[&lt;send-frame-1>],[&lt;send-frame-2>],[&lt;send-frame-3>],[&lt;clr-timer-mask>] | | |
| --- | --- | --- |
| 設定資料規則 &lt;rule-num> | | |
| 引數 | 範圍 | 描述 |
| rule-num | 0..31 | |
| test-expr | | |
| input-expr | | |
| switch-profile | 0..5 | |
| make-event-0 | variable-type | |
| make-event-1 | variable-type | |
| make-event-2 | variable-type | |
| make-event-3 | variable-type | |
| send-frame-0 | frame-type | |
| send-frame-1 | frame-type | |
| send-frame-2 | frame-type | |
| send-frame-3 | frame-type | |
| clr-timer-mask | 0..15 | |

#### data timer {#data-timer}

| 資料計時器 [&lt;timer_1>],[&lt;timer_2>],[&lt;timer_3>],[&lt;timer_4>] | | |
| --- | --- | --- |
| 設定使用者定時器值 | | |
| 引數 | 範圍 | 描述 |
| timer_1 | 0..4294967295 | timer_1 |
| timer_2 | 0..4294967295 | timer_2 |
| timer_3 | 0..4294967295 | timer_3 |
| timer_4 | 0..4294967295 | timer_4 |

#### data activity-cal {#data-activity-cal}

| data activity-cal &lt;profile-mask>,&lt;cal-level>,&lt;cal-led> | | |
| --- | --- | --- |
| 執行活動監測校準並將結果應用到配置檔案 | | |
| 引數 | 範圍 | 描述 |
| profile-mask | 1..63 | 位域 |
| cal-level | 1 | level-one |
| | 2 | level-two |
| cal-led | 0 | no |
|  | 1 | yes |

### 資料幀 {#data-frames}

| ID | 大小 [B] | 名稱 | 資料欄位 |
| --- | --- | --- | --- |
| 1 | 5 | current-state | temperature, humidity, mag_sw_cnt_u8, major_axis_orientation, activity_state, free_fall_evnt, impact_evnt, pending_evnt |
| 2 | variable | device-events | event-list |
| 3 | 11 | temp-histogram | temp_histo_epoch, temp_histo_bin[10] |
| 4 | 11 | humid-histogram | humid_histo_epoch, humid_histo_bin[10] |
| 5 | 3 | device-orientation | orientation_x, orientation_y, orientation_z |
| 6 | 9 | full-activity | activity_state, activity_s, high_activity_s |
| 7 | 8 | motion-events | impact_cnt, free_fall_cnt |
| 8 | 8 | mag-switch | mag_sw_cnt, mag_switch_ts |
| 9 | 8 | impact-count | impact_cnt_u16, impact_cnt_x_u16, impact_cnt_y_u16, impact_cnt_z_u16 |
| 10 | 2 | last-temp | temperature |
| 11 | 2 | ema-temp | temperature_ema |
| 12 | 1 | last-humid | humidity |
| 13 | 1 | ema-humid | humidity_ema |
| 14 | 5 | activity | activity_state, total_activity_s |
| 20 | 8 | dev-time | uptime_s, unix_time |
| 21 | 2 | dev-health | battery_mv |
| 22 | 11 | version | version_pid, version_maj, version_min, version_rev, version_hash[6] |
| 23 | 11 | serial-number | serial_number[11] |
| 24 | 10 | cfg-state | cfg_app_crc, cfg_net_crc, cfg_frames_crc, cfg_data_crc, cfg_rules_crc |
| 25 | variable | full-cfg | content-offset, content-final, content-len, content-binary-blob |
| 26 | variable | app-cfg | content-offset, content-final, content-len, content-binary-blob |
| 27 | variable | net-cfg | content-offset, content-final, content-len, content-binary-blob |
| 28 | variable | frame-cfg | content-offset, content-final, content-len, content-binary-blob |
| 29 | variable | data-cfg | content-offset, content-final, content-len, content-binary-blob |
| 30 | variable | rules-cfg | content-offset, content-final, content-len, content-binary-blob |

### 使用者變數 {#user-variables}

| ID | 大小 [B] | 編碼 | 名稱 | 描述 |
| --- | --- | --- | --- | --- |
| 0 | 1 | u8 | profile | 當前資料配置檔案（0..5） |
| 1 | 4 | u32 | profile_etm | 自上次配置檔案切換以來的經過時間 [s] |
| 2 | 4 | u32 | daytime_tm | 自 00:00 GMT 午夜以來的秒數，未知則為 0 |
| 3 | 4 | u32 | unix_time | 當前 UNIX 時間；如果未知則為裝置執行時間 |
| 4 | 4 | u32 | net_frame_etm | 自上次網路上行鏈路以來的經過時間 |
| 5 | 1 | bool | net_joined_flag | 網路入網狀態 |
| 6 | 1 | u8 | net_class | 當前選擇的 LoRaWAN class |
| 7 | 1 | u8 | net_region | 當前使用的 LoRaWAN 區域程式碼 |
| 8 | 2 | f8.8 | temperature | 最後測量的溫度 |
| 9 | 2 | f8.8 | temperature_ema | 測量溫度的 EMA |
| 10 | 1 | u8 | humidity | 最後測量的溼度 |
| 11 | 1 | u8 | humidity_ema | 測量溼度的 EMA |
| 12 | 4 | u32 | mag_sw_cnt | 磁開關狀態變化計數器 |
| 13 | 4 | u32 | mag_sw_etm | 自上次磁開關變化以來的經過時間 [s] |
| 14 | 1 | bool | mag_sw_flag | 磁開關的當前狀態 |
| 15 | 1 | activity | activity_state | 當前裝置活動狀態 |
| 16 | 4 | u32 | activity_s | 低活動（級別 1）狀態計數器 [s] |
| 17 | 4 | u32 | high_activity_s | 高活動（級別 2）狀態計數器 [s] |
| 18 | 1 | orient | major_axis_orientation | 粗略裝置朝向 |
| 19 | 4 | u32 | impact_cnt_x | X 軸衝擊事件計數器 |
| 20 | 4 | u32 | impact_cnt_y | Y 軸衝擊事件計數器 |
| 21 | 4 | u32 | impact_cnt_z | Z 軸衝擊事件計數器 |
| 22 | 4 | u32 | impact_cnt | 衝擊事件計數器 |
| 23 | 1 | bool | impact_evnt | 衝擊事件標誌，由 current-state、motion-events、impact-count 幀清除 |
| 24 | 4 | u32 | impact_etm | 自上次衝擊事件以來的經過時間 [s] |
| 25 | 4 | u32 | free_fall_cnt | 自由落體事件計數器 |
| 26 | 1 | bool | free_fall_evnt | 自由落體事件標誌，由 current-state、motion-events 幀清除 |
| 27 | 4 | u32 | free_fall_etm | 自上次自由落體事件以來的經過時間 [s] |
| 28 | 1 | u8 | angle_1 | 當前朝向與使用者 ref-1 向量之間的角度，參見 data orient-cfg |
| 29 | 1 | u8 | angle_2 | 當前朝向與使用者 ref-2 向量之間的角度，參見 data orient-cfg |
| 30 | 1 | u8 | angle_3 | 當前朝向與使用者 ref-3 向量之間的角度，參見 data orient-cfg |
| 31 | 1 | u8 | angle_ema | 當前朝向與裝置朝向 EMA 之間的角度 |
| 32 | 2 | u16 | battery_mv | 最後測量的電池電壓 [mV] |
| 33 | 2 | u16 | battery_mv_ema | 電池電壓的 EMA [mV] |
| 34 | 2 | u16 | meta_rule_id | 用於生成帶規則編號事件的元變數 |
| 35 | 4 | u32 | timer_1 | 可復位的持續向上計數定時器 [s] |
| 36 | 4 | u32 | timer_2 | 可復位的持續向上計數定時器 [s] |
| 37 | 4 | u32 | timer_3 | 可復位的持續向上計數定時器 [s] |
| 38 | 4 | u32 | timer_4 | 可復位的持續向上計數定時器 [s] |
| 39 | 4 | u32 | activity_state_etm | 自 activity_state 狀態變化以來的時間 [s] |

### 幀資料欄位 {#frame-data-fields}

| 大小 [B] | 編碼 | 名稱 | 描述 |
| --- | --- | --- | --- |
| 1 | u8 | mag_sw_cnt_u8 | 內部磁開關計數器 mag_sw_cnt 的 LSB |
| 1/8 | bool | pending_evnt | 表示裝置已儲存事件 |
| 0 | | event-list | 可變長度列表，包含：事件時間戳、程式碼和可選值 |
| 1 | u8 | temp_histo_epoch | 溫度直方圖紀元編號 |
| 10 | u8[10] | temp_histo_bin[10] | 溫度直方圖箱計數器值 |
| 1 | u8 | humid_histo_epoch | 溼度直方圖紀元編號 |
| 10 | u8[10] | humid_histo_bin[10] | 溼度直方圖箱計數器值 |
| 1 | i8 | orientation_x | 裝置朝向法向量 X 軸 |
| 1 | i8 | orientation_y | 裝置朝向法向量 Y 軸 |
| 1 | i8 | orientation_z | 裝置朝向法向量 Z 軸 |
| 4 | u32 | mag_switch_ts | 上次磁開關狀態變化的時間戳 |
| 2 | u16 | impact_cnt_u16 | 衝擊事件計數器 |
| 2 | u16 | impact_cnt_x_u16 | X 軸衝擊事件計數器 |
| 2 | u16 | impact_cnt_y_u16 | Y 軸衝擊事件計數器 |
| 2 | u16 | impact_cnt_z_u16 | Z 軸衝擊事件計數器 |
| 4 | u32 | total_activity_s | 總活動狀態時間（級別 1 + 級別 2） |
| 4 | u32 | uptime_s | 裝置 FW 執行時間 |
| 2 | u16 | version_pid | TG-LR82:0x0000, TG-LR92:0x0001 |
| 1 | u8 | version_maj | FW 版本主編號 |
| 1 | u8 | version_min | FW 版本次編號 |
| 1 | u8 | version_rev | FW 版本補丁編號 |
| 6 | u8[6] | version_hash[6] | FW 版本雜湊 |
| 11 | u8[11] | serial_number[11] | 裝置序列號的最後 11 個字元 |
| 2 | u16 | cfg_app_crc | app 和 mag 配置組 16 位校驗和 |
| 2 | u16 | cfg_net_crc | net 配置組 16 位校驗和 |
| 2 | u16 | cfg_frames_crc | frame 配置組 16 位校驗和 |
| 2 | u16 | cfg_data_crc | data 配置組 16 位校驗和 |
| 2 | u16 | cfg_rules_crc | 資料規則配置 16 位校驗和 |
| 1/8 | bool | content-final | 表示內容最後一塊的標誌 |
| 15/8 | u15 | content-offset | 內容資料的位元組偏移 |
| 1 | u8 | content-len | 內容長度 |
| 0 | | content-binary-blob | 內容塊的二進位制資料 |

### 已知問題 {#known-issues}

| ID | FW | 描述 |
| --- | --- | --- |
| LORA-275 | 2.0.0 | 停用輔助頻段時更改憑證沒有超時。 |
| LORA-276 | 2.0.0 | 憑證更改命令超時不正確。 |
| LORA-279 | 2.0.0 | 啟用朝向時進行活動校準會導致故障。 |

#### LORA-275 {#lora-275}

**描述：** 如果在停用輔助頻段的情況下發起憑證更改，裝置將不會在入網時超時。裝置將一直嘗試入網，直到成功或重啟。

**解決方法：** 如果新憑證無效，請使用磁開關命令物理重啟裝置。

#### LORA-276 {#lora-276}

**描述：** 執行 `lora cred` 時，裝置將在下一次入網嘗試時基於總執行時間而不是命令執行時間使入網過程超時。如果執行時間長於 *confirm-timeout-s* 引數，裝置將在單次入網嘗試失敗後立即超時。

**解決方法：** 在嘗試更改憑證之前發出裝置復位命令 `app reset`。或者手動多次重試憑證更改。

#### LORA-279 {#lora-279}

**描述：** 如果在啟用朝向檢測時執行活動校準，裝置可能發生故障並重啟。

**解決方法：** 在執行活動校準之前使用 `data orient-cfg` 停用朝向檢測，並在完成後重新啟用。

## 相關文件 {#related-documents}

| 編號 | 名稱 |
| --- | --- |
| 1 | TS001-1.0.4 LoRaWAN® L2 1.0.4 規範 |
| 2 | 64 位全域性識別符號（EUI-64）指南 |
