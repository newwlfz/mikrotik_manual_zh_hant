---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/health"
sidebar_position: 13
title: "健康"
sidebar_label: "健康"
description: "本頁介紹 MikroTik RouterOS 硬體健康監控，涵蓋溫度、電壓、電流、電源和功耗讀數、風扇控制設定、SNMP OID，以及用於告警的 REST API 和指令碼示例。"
tags:
  - 'system-health'
  - 'fan-control'
  - 'temperature'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/health
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

支援監控的硬體會報告硬體狀態資訊，例如溫度、電壓、電流、風扇轉速、電源狀態和功耗。相同的讀數也可在 Winbox 的 **System → Health** 標籤頁中檢視。沒有硬體感測器的裝置不會輸出任何內容：這包括 CHR 和虛擬機器，以及根本沒有感測器的板卡（例如 hAP ax²）。

CCR1072-1G-8S+ 裝置上的示例：

```ros
[admin@MikroTik] > /system/health/print 
Columns: NAME, VALUE, TYPE
 #  NAME                VALUE  TYPE
 0  power-consumption   50.8   W   
 1  cpu-temperature     43     C   
 2  fan1-speed          5654   RPM 
 3  fan2-speed          5825   RPM 
 4  fan3-speed          5800   RPM 
 5  fan4-speed          5750   RPM 
 6  board-temperature1  29     C   
 7  board-temperature2  28     C   
 8  psu1-voltage        0      V   
 9  psu2-voltage        12.1   V   
10  psu1-current        0      A   
11  psu2-current        4.2    A
```

`TYPE` 列顯示讀數的單位：`C` 為攝氏度，`RPM` 為風扇轉速，`V` 為電壓，`A` 為電流，`W` 為功耗。指令碼看到的值與 CLI 顯示的值相同。SNMP 對溫度、電壓和功率使用十分之一單位（23.8 V → 238），電流在舊版 OID 中以 mA 為單位，或在動態儀表表中以 dA 為單位（參見下面的 SNMP 部分）。

要列印單個讀數，請按名稱過濾：

```ros
[admin@MikroTik] > /system/health/print where name="cpu-temperature"
Columns: NAME, VALUE, TYPE
 #  NAME             VALUE  TYPE
 0  cpu-temperature  43     C   
```

要檢視特定 RouterBOARD 產品支援哪些健康資料，請檢視 [mikrotik.com](https://mikrotik.com/products) 上的產品規格。

## 讀數 {#readings}

| 讀數 | 單位 | 描述 |
| :-- | :-- | :-- |
| `voltage` | V | 具有單個電源輸入的裝置上的供電電壓 |
| `psuN-voltage` | V | 電源 N 的電壓 |
| `psuN-input-voltage` | V | 電源 N 的輸入（市電）電壓 |
| `jack-voltage`, `2pin-voltage`, `poe-in-voltage` | V | 特定電源輸入的電壓（在無 PSU 的裝置上） |
| `poe-outN-voltage` | V | PoE-out 埠 N 上的電壓 |
| `psuN-current` | A | 電源 N 消耗的電流 |
| `power-consumption` | W | 總功耗 |
| `poe-out-consumption` | W | 當前 PoE-out 功耗 |
| `psuN-power` | W | 電源 N 的功率 |
| `temperature` | C | 具有單個感測器的裝置上的裝置溫度 |
| `cpu-temperature` | C | CPU 溫度 |
| `board-temperatureN` | C | 板卡溫度感測器 N |
| `phy-temperature` | C | PHY 溫度 |
| `sfp-temperature` | C | SFP 模組溫度 |
| `switch-temperature` | C | 交換晶片溫度 |
| `pcie-switch-temperature` | C | PCIe 交換晶片溫度 |
| `psuN-temperature` | C | 電源 N 的溫度 |
| `fan-state` | — | 風扇狀態：`ok` 或 `fail` |
| `fanN-speed` | RPM | 風扇 N 的轉速 |
| `psuN-fan-speed` | RPM | 電源 N 內部風扇的轉速 |
| `psuN-state` | — | 電源 N 狀態（參見下文的狀態表） |

帶編號的名稱（`psuN`、`fanN`、`board-temperatureN`、`poe-outN`）使用從 1 開始的索引，數量取決於裝置。具體存在哪些讀數取決於裝置的硬體感測器。

當裝置溫度較高時，風扇轉速讀數為 0 RPM 可能意味著風扇已停止或發生故障。

### 電壓 {#voltage}

支援電壓監控的路由器會顯示供電電壓值。在 CLI、Winbox 和指令碼中，它以伏特為單位報告；透過 SNMP 時，它以 dV 為單位（CLI 值乘以 10）。

具有 PEXT 和 PoE 電源輸入的路由器使用 PEXT 進行校準。因此，由於額外的乙太網保護鏈路，透過 PoE 顯示的值可能低於輸入電壓。

```ros
[admin@MikroTik] > /system/health/print 
Columns: NAME, VALUE, TYPE
#  NAME         VALUE  TYPE
0  voltage      23.8   V   
1  temperature  39     C 
```

### 溫度 {#temperature}

支援溫度監控的路由器會顯示溫度讀數。在 CLI、Winbox 和指令碼中，它以攝氏度報告；透過 SNMP 時，該值會乘以 10。不同裝置使用不同的溫度感測器，例如 `cpu-temperature`、`board-temperature1`、`sfp-temperature`、`phy-temperature` 或 `switch-temperature`。某些讀數僅在相應元件存在時才會出現，例如 `sfp-temperature` 僅在安裝了 SFP 模組時才會顯示。您可以在 [mikrotik.com](https://mikrotik.com/products) 的規格說明中找到裝置經過測試的環境溫度範圍。經過測試的環境溫度範圍是裝置可實際放置的溫度。它**不**等同於系統健康監視器報告的溫度。

### 電源狀態 {#power-supply-states}

具有冗餘電源的裝置會報告每個電源的狀態。對於帶電池備用的裝置，請參閱 [UPS](../system-information-and-utilities/ups.md) 頁面。可能的值為：

| 值 | 描述 |
| :-- | :-- |
| `ok` | 電源正常工作。 |
| `fail` | 電源發生故障。 |
| `not-present` | 此插槽中未檢測到電源。 |
| `idle` | 電源存在但處於空閒狀態。 |
| `no-input` | 電源沒有輸入電力。 |

值為 `fail` 或 `no-input` 表示電源或其供電來源存在問題。

### 舊版裝置 {#legacy-devices}

如果舊版 CRS112、CRS210 和 CRS109 裝置透過 PoE 供電，Health 僅在最高 26.7 V 時顯示正確電壓。如果使用更高電壓，Health 將顯示恆定的 16 V。

基於 x86（舊式 PC 硬體）的裝置使用另一組讀數名稱，例如 `core`、`3.3v`、`5v`、`12v`、`lm87-temp`、`cpu-temp`、`board-temp`、`voltageN`、`tempN` 和 `fanN`。

## 風扇控制與行為 {#fan-control-and-behavior}

[/system/health/settings](../cli-reference/system/health/settings/index.md) 選單控制帶有風扇裝置上的風扇行為。

有三個引數可以啟動風扇：PoE-out 功耗、SFP 溫度和 CPU 溫度。當其中一個引數超過最佳值時，風扇啟動。

### PoE-out 功耗 {#poe-out-consumption}

如果裝置具有 PoE-out，則風扇 RPM 將如下所述變化：

| PoE-out 負載 | 最大風扇轉速的 RPM % |
| :-- | :-- |
| 0%..24% | 風扇轉速 0% |
| 25%..46% | 風扇轉速 25% |
| 47%..70% | 風扇轉速 50% |
| 71%..92% | 風扇轉速 75% |
| 93%.. | 風扇轉速 100% |

對於配備 **PWM** 風扇的裝置，轉速將從 9..88% 線性增加或降低（低於 100 W 時風扇 RPM 為 0）。

### 手動風扇控制選項 {#manual-fan-control-option}

手動風扇控制適用於 CRS3xx、CRS5xx 和 CCR2xxx 裝置，以及修訂版 CCR1036-8G-2S+-r2、CCR1036-12G-4S-r2 和 CCR1016-12S-1S+-r2 裝置。

在 [`/system/health/settings`](../cli-reference/system/health/settings/index.md) 中設定它們——每個引數，包括手動風扇控制選項 `fan-mode`、`use-fan`、`use-fan2`、`fan-switch` 和 `fan-on-threshold`，以及只讀的 `active-fan`/`active-fan2` 狀態，都在 CLI 參考中描述。帶有主風扇和輔助風扇的裝置，例如 RB1100、CCR1016 和 CCR1036 裝置，也支援手動風扇控制。

例如，要讓風扇至少以其最大轉速的四分之一執行：

```ros
/system/health/settings/set fan-min-speed-percent=25
```

當主風扇發生故障時，裝置會自動切換到輔助風扇，並且 `active-fan`（或 `active-fan2`）會變為 `auxiliary`。在 CRS3xx、CRS5xx、CCR2xxx、CCR1016r2 和 CCR1036r2 裝置上，風扇狀態變化也會寫入日誌。

使用 `/system/health/settings/detect-fans` 命令檢測連線到裝置的風扇，例如在安裝或更換風扇之後。

### 風扇控制詳解 {#fan-control-in-detail}

如果內部測得溫度（CPU、SFP、交換器、主機板）中至少有一項超過 **fan-target-temp**，風扇就會開始轉動。溫度越高，風扇轉速越快。

- 配備 PWM 風扇的裝置：風扇會線性提高其 RPM，以儘可能將溫度保持在 **fan-target-temp**；當溫度達到或超過 **fan-full-speed-temp** 時，風扇會達到最大 RPM。
- 配備 DC 風扇的裝置：預設情況下，風扇會以較高的最低 RPM 開始轉動。這可能會使裝置降溫過多，以至於如果 **fan-min-speed-percent** 為 **0%**，風扇會完全關閉；而在預設 **12%** 下，風扇永遠不會完全停止，這可以減少噪聲和啟停峰值。當溫度回升到 **fan-target-temp** 時，風扇會再次開啟。

一個例外：S+RJ10 模組在觸發風扇之前具有 65 C 的溫度閾值，因此風扇會以較高的初始轉速開始轉動以冷卻裝置。前面提到的所有功能都與 **fan-control-interval** 引數值直接相關，因為它決定了風扇控制器監控所有感測器資料並應用風扇控制更改的頻率。

PWM 和 DC 風扇對風扇控制的反應不同。PWM 風扇會以線性方式提高或降低其 RPM。然而，DC 風扇只有少數幾種可執行的速度檔位。

所有讀數均為近似值。其目的是告知使用者可能發生或即將發生的故障。

## 監控健康狀況並獲取警報 {#monitor-health-and-get-alerts}

### SNMP trap {#snmp-trap}

對於基於 SNMP 的監控，請啟用 `temp-exception` trap 生成器。當溫度達到 100 C 或達到由 `cpu-overtemp-threshold` 設定的值時，路由器會發送 SNMP trap。有關詳細資訊，請參見 [SNMP](./snmp.md) 頁面。

### SNMP OID {#snmp-oids}

所有健康讀數都在 [MIKROTIK-MIB](https://mikrotik.com/download) 的 `1.3.6.1.4.1.14988.1.1.3` 子樹下公開，格式為 `.1.3.6.1.4.1.14988.1.1.3.<index>.0`：

| 索引 | 物件名稱 | 讀數 |
| :-- | :-- | :-- |
| 1 | `mtxrHlCoreVoltage` | 核心電壓（V） |
| 2 | `mtxrHlThreeDotThreeVoltage` | 3.3 V 供電軌電壓 |
| 3 | `mtxrHlFiveVoltage` | 5 V 供電軌電壓 |
| 4 | `mtxrHlTwelveVoltage` | 12 V 供電軌電壓 |
| 5 | `mtxrHlSensorTemperature` | 感測器晶片溫度（C） |
| 6 | `mtxrHlCpuTemperature` | CPU 溫度 |
| 7 | `mtxrHlBoardTemperature` | 板卡溫度 |
| 8 | `mtxrHlVoltage` | 主電壓 |
| 9 | `mtxrHlActiveFan` | 活動風扇的名稱 |
| 10 | `mtxrHlTemperature` | 溫度 |
| 11 | `mtxrHlProcessorTemperature` | 處理器溫度 |
| 12 | `mtxrHlPower` | 功耗（W） |
| 13 | `mtxrHlCurrent` | 電流（mA） |
| 14 | `mtxrHlProcessorFrequency` | CPU 頻率（MHz） |
| 15 | `mtxrHlPowerSupplyState` | 電源狀態（0 = 不正常，1 = 正常） |
| 16 | `mtxrHlBackupPowerSupplyState` | 備用電源狀態（0 = 不正常，1 = 正常） |
| 17 | `mtxrHlFanSpeed1` | 風扇 1 轉速（RPM） |
| 18 | `mtxrHlFanSpeed2` | 風扇 2 轉速（RPM） |
| 19 | `mtxrAlarmSocketStatus` | 告警插座狀態（0 = 未啟用，1 = 啟用） |

溫度、電壓和功率值會乘以 10（要得到該值請除以 10）。電流以 mA 為單位報告，頻率以 MHz 為單位，風扇轉速以 RPM 為單位。哪些索引會返回值取決於裝置的硬體感測器；在裝置上執行 `/system/health/print oid` 可檢視其實際的 OID 對映。

表中的靜態 OID 是固定的舊版集合。較新的讀數——例如風扇 2 以上的風扇轉速、每路電源的讀數（`psuN-*`）、`pcie-switch-temperature` 和 PoE-out 電壓——可在位於 `.1.3.6.1.4.1.14988.1.1.3.100` 的動態 gauge 表中獲取。該表的每一行都按名稱（`mtxrGaugeName`）列出一項讀數，並列出其原始值（`mtxrGaugeValue`）和單位（`mtxrGaugeUnit`：`celsius(1)`、`rpm(2)`、`dV(3)`、`dA(4)`、`dW(5)` 或 `status(6)`）。`dV`、`dA` 和 `dW` 單位分別是分伏、分安和分瓦，因此請將原始值除以 10。

### REST API {#rest-api}

使用 REST API，你可以以 JSON 讀取相同的讀數：

```bash
curl -k -u admin https://192.168.88.1/rest/system/health
```

有關詳細資訊，請參閱 [REST API](../developer-guides/rest-api.md) 頁面。

### 傳送電子郵件警報 {#send-an-email-alert}

透過指令碼，你可以使用 scheduler 定期檢查讀數，並在超出限制時傳送電子郵件。首先配置 [E-mail](../system-information-and-utilities/e-mail.md) 設定，然後新增指令碼和 scheduler 條目：

```ros
/system/script/add name=temp-alert source={
    :local t [/system/health/get [find name="cpu-temperature"] value]
    :if ($t > 65) do={/tool/e-mail/send to="admin@example.com"
        subject="Router overheating" body=("CPU temperature: " . $t)}
}
/system/scheduler/add name=temp-alert start-time=startup interval=5m on-event=temp-alert
```

在指令碼中，這些值是由 CLI 列印的純數字（54 表示 54 C），因此示例是與 65 進行比較。

有關所有引數，請參閱 [`/system/health`](../cli-reference/system/health/index.md) 和 [`/system/health/settings`](../cli-reference/system/health/settings/index.md) CLI 參考頁面。
