---
sidebar_key: "internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-tag-advertisement-formats"
sidebar_position: 4
title: "MikroTik 標籤通告格式"
sidebar_label: "MikroTik 標籤通告格式"
source: https://manual.mikrotik.com/docs/7.24/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-tag-advertisement-formats
captured_at: '2026-11-04T11:30:12+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 簡介 {#introduction}

TG-BT5-XX 標籤可以在 4 種不同模式下工作：

- 出廠休眠模式
- 配置模式
- 廣播模式
- 升級模式

在廣播模式下，標籤會透過藍牙廣播封包廣播自身資訊。所廣播的資訊取決於廣播封包的型別。

目前，以下是可透過 MikroTik Beacon Manager 應用配置的所有受支援型別：

DeviceName、MikroTik、[Eddystone-TLM](https://play.google.com/store/apps/details?id=com.mikrotik.android.bt5&hl=en_US&gl=US&pli=1)、[Eddystone-UID](https://github.com/google/eddystone/tree/master/eddystone-uid) 和 [iBeacon](https://developer.apple.com/ibeacon/)。

藍牙技術在進行資料交換時使用 2 種類型的通道（各自使用不同的頻率）：

- 專用於資料傳輸的資料通道；
- 專用於廣播的廣播通道。

共有 40 個獨立的頻段（通道），每個頻段間隔 2 MHz。37、38 和 39 號通道用於廣播，0-36 號用於資料傳輸。

在廣播過程中，BLE 廣播封包會被廣播出去。該封包包含 Preamble、Access Address、PDU 和 CRS 欄位。

Preamble 和 Access Address 欄位幫助接收方檢測幀。CRS 欄位用於檢查錯誤。PDU 定義封包本身。

MikroTik 標籤支援傳統（legacy）的不可連線、不可掃描的非定向廣播（`ADV_NOCONN_IND`）。在這種情況下，Payload 由 "AdvA"（包含廣播方地址資訊的欄位）和 "AdvData"（包含資料資訊的欄位）欄位組成。

1 個八位組 = 1 位元組 = 8 位

| 屬性 | 描述 |
| --- | --- |
| Preamble | 1 個八位組 |
| Access-Address | 4 個八位組 |
| PDU |PDU Header = 2 個八位組 PDU Payload = AdvA（6 個八位組）+AdvData（0...31 個八位組）|
| CRS | 3 個八位組 |

## MikroTik 封包結構 {#mikrotik-packet-structure}

"AdvData" 欄位結構（最多 31 個八位組/位元組）：

| 屬性 | 描述 | |
| --- | --- | --- |
| Flags | Flags 欄位的長度、型別和資料。用於"告知"周圍的掃描器裝置處於何種狀態。 | 3 個八位組（`020106`）：  第 1 個八位組 - 長度  第 2 個八位組 - 型別 第 3 個八位組 - 資料|
| Length | 載荷的長度。 | 1 個八位組（`15`） |
| Type | 廠商特定資料。 | 1 個八位組（`ff`） |
| ManufacturerData | 公司識別符號。 | 2 個八位組（`4F09`） |
| Version | 此廣播結構的版本。 | 1 個八位組（uint） |
| UserData | 使用者配置的載荷部分。 | 1 個八位組（uint） |
| Secret | 載荷中可選加密（AES-ECB）的部分。 |  secret: salt（用於加密的鹽值）= 2 個八位組（uint）  secret: acceleration（加速度，採用有符號 8.8 定點格式，三個軸的加速度（0=x，1=y，2=z））= 6 個八位組（uint）  secret: temperature（環境溫度，單位為攝氏度，採用有符號 8.8 定點格式）= 2 個八位組（int）  secret: uptime（執行時間，單位為秒）= 4 個八位組（uint）  secret: flags（標誌位掩碼）= 1 個八位組（uint）  secret: batteryPercentage（電池電量百分比）= 1 個八位組（uint）  |

:::info
請注意，所有多位元組數值均為小端序。這意味著，例如，如果你想獲取溫度值，而第 14 和第 15 個八位組表示的溫度為 "a1 19"（"正"溫度）→ 實際溫度值將是 (0x19a1)/256 = 25.6 C。
:::
關於如何將載荷的**十六進位制**值轉換為**十進位制**值的詳細示例，將在後文的 **PDU 載荷結構** 章節中展示。

UserData 和 Secret 欄位藉助 `flags` 進行配置。在 "UserData" 部分中，控制 "Secret" 是否加密的引數名為 `FLAG_ENCRYPTED`。當 `FLAG_ENCRYPTED=0` 時，表示 secret 未加密（第 6 個八位組中的第 1 位將置為 0）；當 `FLAG_ENCRYPTED=1` 時，表示 secret 已加密（第 6 個八位組中的第 1 位將置為 1）。

在 "Secret" 部分中共有 7 個 `flags`（第 24 個八位組）：

- `FLAG_REED_SWITCH`（第 1 位 - 若置為 1，表示廣播時簧片開關處於閉合狀態）
- `FLAG_ACCEL_TILT`（第 2 位 - 若置為 1，表示該廣播是透過傾斜裝置傳送的）
- `FLAG_ACCEL_FREE_FALL`（第 3 位 - 若置為 1，表示該廣播是透過使裝置自由落體傳送的）
- `FLAG_IMPACT_X`（第 4 位 - 若置為 1，表示廣播時在 x 軸上受到了衝擊）
- `FLAG_IMPACT_Y`（第 5 位 - 若置為 1，表示廣播時在 y 軸上受到了衝擊）
- `FLAG_IMPACT_Z`（第 6 位 - 若置為 1，表示廣播時在 z 軸上受到了衝擊）
- `FLAG_ACCEL_DISABLED`（第 7 位 - 若置為 1，表示加速度計已被停用）
例如，如果你看到十六進位制訊息的第 24 個八位組為 "02"（將 **十六進位制** 值 "02" 轉換為 **二進位制** 即為 "0010" → 第 2 位置為 1）→ 表示裝置被傾斜了。如果看到 "04"（**十六進位制** "04" 轉換為 **二進位制** 為 "0100" → 第 3 位置為 1）→ 表示裝置被掉落（觸發了自由落體）。如果看到 "38"（**十六進位制** 轉換為 **二進位制** 為 "00111000" → 第 4、5、6 位均置為 1）→ 表示在傳送廣播時，加速度計在 x/y/z 三個軸上都檢測到衝擊/喚醒。

更多示例（針對第 24 個八位組的值）：

- "08" 表示僅在 x 軸上受到衝擊；
- "18" 表示在 x 軸和 y 軸上受到衝擊；
- "28" 表示在 x 軸和 z 軸上受到衝擊；
- "10" 表示僅在 y 軸上受到衝擊；
- "30" 表示在 y 軸和 z 軸上受到衝擊；
- "20" 表示僅在 z 軸上受到衝擊。
- "40" 表示加速度計已停用。

### MikroTik PDU 載荷結構 {#mikrotik-pdu-payload-structure}

| 八位組 | 值 | | |
| --- | --- | --- | --- |
| 0 | 02 | Flags | flags 欄位的長度 |
| 1 | 01 | Flags | flags 欄位的型別 |
| 2 | 06 | Flags | flags 欄位的資料 |
| 3 | 15 | Length | 載荷的長度 |
| 4 | FF | Type | 廠商特定資料 |
| 5 | 4F | 公司識別符號 | MikroTik |
| 6 | 09 | 公司識別符號 | MikroTik |
| 7 | 01 | Version | 此廣播結構的版本 |
| 8 | 00 | UserData | 使用者配置的載荷部分 |
| 9 | xx* | Secret | secret: 鹽值 |
| 10 | xx* | Secret | secret: 鹽值 |
| 11 | xx* | Secret | secret: X 軸加速度 |
| 12 | xx* | Secret | secret: X 軸加速度 |
| 13 | xx* | Secret | secret: Y 軸加速度 |
| 14 | xx* | Secret | secret: Y 軸加速度 |
| 15 | xx* | Secret | secret: Z 軸加速度 |
| 16 | xx* | Secret | secret: Z 軸加速度 |
| 17 | xx* | Secret | secret: 溫度 |
| 18 | xx* | Secret | secret: 溫度 |
| 19 | xx* | Secret | secret: 執行時間 |
| 20 | xx* | Secret | secret: 執行時間 |
| 21 | xx* | Secret | secret: 執行時間 |
| 22 | xx* | Secret | secret: 執行時間 |
| 23 | 00 | Secret | secret: flags |
| 24 | xx* | Secret | secret: batteryPercentage |

\* - 可能有所不同

#### 示例 {#example}

以 MikroTik 格式配置的載荷（非加密）示例如下：

| 02010615ff4f090100cea6000000000200a01c91085700005f |
| --- |

**020106**（前 3 個八位組）→ Flags 欄位的長度、型別和資料。

**15ff4f09**（第 4、5、6、7 個八位組）→ Length（0x15 **十六進位制轉十進位制** 為 21）。Type（0xff）。公司識別符號（0x4f09）。

**01**（第 8 個八位組）  →  載荷結構的當前版本。每個載荷都應相同（常量資料）。

**00**（第 9 個八位組）→ 表示該載荷未加密。"01" 則表示已加密。

**cea6**（第 10 和第 11 個八位組）→ 鹽值。每個新載荷都應生成不同的鹽值。你可以使用該值來檢查相同的載荷是否被以不同方式加密。**該值本身不包含任何有用的資訊**。如果你發現兩個在不同時間間隔收到的載荷具有相同的鹽值，那就說明收到的這兩個載荷完全相同。你可以使用與執行時間計算相同的原理來計算鹽值 - 見下文。

**0000**（第 12 和第 13 個八位組）→ 廣播時刻 X 軸的加速度 = **0 m/s<sup>2</sup>**。請參閱下文 Z 軸的加速度計算。

**0000**（第 14 和第 15 個八位組）→ 廣播時刻 Y 軸的加速度 = **0 m/s<sup>2</sup>**。請參閱下文 Z 軸的加速度計算。

**0200**（第 16 和第 17 個八位組）→ 廣播時刻 Z 軸的加速度 = **0.0078 m/s<sup>2</sup>**。要從十六進位制格式得到十進位制值，需要按以下步驟操作：

- 如前所述，多位元組數值為小端序，這意味著要計算真實值，需要交換八位組的位置（交換八位組順序）。因此第一步是把 0x**0200** 的值交換為 0x**0002**。0x**0002** 從**十六進位制**轉換為**十進位制**是 **02**。
- 請記住，加速度採用有符號 8.8 定點格式（二進位制補碼），這意味著你基本上需要將結果除以 "256"。第二步是將該值除以 256 → (0x**0002** **十六進位制** 或 **02** **十進位制**)/256 = 0.0078 m/s<sup>2</sup>。
- 同樣的計算原理適用於 X 軸和 Y 軸的加速度。在我們的示例中，它們恰好為 0 → 0x0000/256=0。

**a01c**（第 18 和第 19 個八位組）→ 標籤檢測到的溫度（攝氏度）= **28.625 C**。溫度採用小端序（因為它是多位元組值），並且採用 **有符號 16 位整數 [二進位制補碼] 8.8 定點格式**，因此這裡同樣適用相同的"公式"：
0x1ca0/256=28.625 C。

**91085700**（第 20、21、22、23 個八位組）→ 標籤的執行時間（秒）= **5703825 s**。0x91085700 為小端序，因此只需將八位組交換為 0x00570891，結果即為十進位制的 5703825。也就是 1584.395833 小時，或 66 天的執行時間。

**00**（第 24 個八位組）→ 傳送該載荷的觸發器（標誌）。如果為 "**00**"，表示未檢測到任何觸發器，它只是一個週期性廣播的載荷（基於為標籤配置的廣播間隔）。如果該值為 "**04**"，則表示裝置被掉落（觸發了自由落體）。有關 "flags" 和 "Secret" 的更多資訊，可在上文 **封包結構** 章節中找到。

**5f**（第 25 個八位組）→ 標籤的電池電量百分比 = **95 %**。0x**5f** 從十六進位制轉換為十進位制是 95。

:::info
從 v**7.11** 開始，你可以使用 Peripheral Device 部分和/或 Decode-ad 功能來檢視解碼後的值！
:::

```
#### Script for decoding
Add a new script under the "**System>Scripts**" tab and import the script there (for non-encrypted payloads).

# POSIX regex for filtering advertisement Bluetooth addresses. E.g. "^BC:33:AC"
# would only include addresses which start with those 3 octets.
# To disable this filter, set it to ""
:local addressRegex "2C:C8:1B:4B:BB:0A"

# POSIX regex for filtering Bluetooth advertisements based on their data. Same
# usage as with 'addressRegex'.
:local advertisingDataRegex ""

# Signal strength filter. E.g. -40 would only include Bluetooth advertisements
# whose signal strength is stronger than -40dBm.
# To disable this filter, set it to ""
:local rssiThreshold ""

################################## Bluetooth ##################################
:global invertU16 do={
    :local inverted 0
    :for idx from=0 to=15 step=1 do={
        :local mask (1 &lt;&lt; $idx)
        :if ($1 & $mask = 0) do={
            :set $inverted ($inverted | $mask)
        }
    }
    return $inverted
}
:global le16ToHost do={
    :local lsb [:pick $1 0 2]
    :local msb [:pick $1 2 4]
    :return [:tonum "0x$msb$lsb"]
}
:local le32ToHost do={
    :local lsb [:pick $1 0 2]
    :local midL [:pick $1 2 4]
    :local midH [:pick $1 4 6]
    :local msb [:pick $1 6 8]
    :return [:tonum "0x$msb$midH$midL$lsb"]
}
:local from88 do={
    :global invertU16
    :global le16ToHost
    :local num [$le16ToHost $1]
    # Handle negative numbers
    :if ($num & 0x8000) do={
        :set num (-1 * ([$invertU16 $num] + 1))
    }
    # Convert from 8.8. Scale by 1000 since floating point is not supported
    :return (($num * 125) / 32)
}
:local flagStr do={
    :local str ""
    :if ($1 & 0x01) do={ :set $str " switch" }
    :if ($1 & 0x02) do={ :set $str "$str tilt" }
    :if ($1 & 0x04) do={ :set $str "$str free_fall" }
    :if ($1 & 0x08) do={ :set $str "$str impact_x" }
    :if ($1 & 0x10) do={ :set $str "$str impact_y" }
    :if ($1 & 0x20) do={ :set $str "$str impact_z" }
    :if ([:len $str] = 0) do={ :return "" }
    :return [:pick $str 1 [:len $str]]
}
# Find fresh Bluetooth advertisements
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
    :set $btOldestAdvertisementTimestamp 0
}
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex and \
        data ~ $advertisingDataRegex and \
        rssi > $rssiThreshold
]
:local advCount 0
:local lastAdvTimestamp 0
:local advJson ""
:local advSeparator ""
# Remove semicolons from MAC/Bluetooth addresses
:local minimizeMac do={
    :local minimized
    :local lastIdx ([:len $address] - 1)
    :for idx from=0 to=$lastIdx step=1 do={
        :local char [:pick $address $idx]
        :if ($char != ":") do={
            :set $minimized "$minimized$char"
        }
    }
    :return $minimized
}
:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local rssi ($adv->"rssi")
    :local epoch ($adv->"epoch")
    :local ad ($adv->"data")
    :local version [:tonum "0x$[:pick $ad 14 16]"]
    :local encrypted [:tonum "0x$[:pick $ad 16 18]"]
    :local salt [$le16ToHost [:pick $ad 18 22]]
    :local accelX [$from88 [:pick $ad 22 26]]
    :local accelY [$from88 [:pick $ad 26 30]]
    :local accelZ [$from88 [:pick $ad 30 34]]
    :local temp [$from88 [:pick $ad 34 38]]
    :local uptime [$le32ToHost [:pick $ad 38 46]]
    :local flags [:tonum "0x$[:pick $ad 46 48]"]
    :local bat [:tonum "0x$[:pick $ad 48 50]"]
    :put ("$advCount: \
        address=$address \
        ts=$epoch \
        rssi=$rssi \
        version=$version \
        encrypted=$encrypted \
        salt=$salt \
        accelX=$accelX \
        accelY=$accelY \
        accelZ=$accelZ \
        temp=$temp \
        uptime=$uptime \
        flags=\"$[$flagStr $flags]\" \
        bat=$bat" \
    )
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $epoch
}
:if ($advCount > 0) do={
    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp
}
```

你唯一需要修改的行是：

```
:local addressRegex "2C:C8:1B:4B:BB:0A"
```

這一行，你需要在此輸入標籤的 MAC 地址。

用任意你喜歡的名稱儲存指令碼，例如 **decode**。

透過命令列介面（Winbox/Webfig 中的 "**New Terminal**" 按鈕）執行指令碼：

```ros
[admin@MikroTik] > system script run decode
0: address=2C:C8:1B:4B:BB:0A ts=1662553431348 rssi=-45 version=1 encrypted=0 salt=57919 accelX=3 accelY=-35 accelZ=-70 temp=25535 uptime=1046174 flags="" bat=99
1: address=2C:C8:1B:4B:BB:0A ts=1662553436349 rssi=-40 version=1 encrypted=0 salt=24154 accelX=-19 accelY=-23 accelZ=0 temp=25546 uptime=1046179 flags="" bat=99
2: address=2C:C8:1B:4B:BB:0A ts=1662553446351 rssi=-37 version=1 encrypted=0 salt=37822 accelX=-15 accelY=35 accelZ=15 temp=25550 uptime=1046189 flags="" bat=99
```

從上面的示例可以看到，指令碼會將所有載荷從**十六進位制**格式"翻譯"為**十進位制**格式，並將它們列印到終端中。

你還可以進一步修改指令碼，用這些"已解碼"的值構造一條訊息，並將其傳送到你所選擇的 EMAIL、MQTT 或 HTTP 伺服器，**但是！**請記住，這可能會給裝置帶來更大的負載。因此你需要測試執行該指令碼時的效能。在伺服器端進行解碼對 RouterOS 資源來說會更輕鬆。
:::info
由於不支援浮點數 → 小數點之後的每次計算都會"向上取整"為整數。這就是指令碼計算溫度和加速度值時會**乘以 1000**（放大 **1000** 倍）的原因。
因此，如果你看到溫度為 **temp=25546**，則實際溫度為 **25.546 C**（25546/1000）；如果你看到 **accelZ=15**，則相對 z 軸的實際加速度為 **0.015 m/s<sup>2</sup>**（15/1000）。
:::

## iBeacon 封包結構 {#ibeacon-packet-structure}

iBeacon 是受支援的廣播封包型別之一。你可以透過[連結](https://en.wikipedia.org/wiki/IBeacon)瞭解有關該協定的更多資訊。

在這種情況下，PDU Payload 由 "AdvA"（長度為 6 個八位組）和 "AdvData"（包含資料資訊的欄位）欄位組成。傳統藍牙裝置只能支援 31 位元組長的信標訊息。UUID 長度為 16 位元組（MikroTik 預設 UID=b2b98de4-c81c-47c2-b14e-791b3e5587ec）。

"AdvData" 欄位結構：

| 屬性 | 描述 | |
| --- | --- | --- |
| Flags | Flags 欄位的長度、型別和資料。用於"告知"周圍的掃描器裝置處於何種狀態。 | 3 個八位組（`020106`）：  第 1 個八位組 - 長度  第 2 個八位組 - 型別  第 3 個八位組 - 資料 |
| ManufacturerData | 公司識別符號 | 4 個八位組（`1aff4c00`） |
| BeaconType | 次級識別符號 | 1 個八位組（const） |
| RemainingDataLength | 以位元組為單位定義載荷的剩餘長度 | 1 個八位組（const） |
| UserData | 使用者配置的載荷部分 |  Proximity UUID（通用唯一識別符號）= 16 個八位組（uint）  Major Number（特定分組識別符號）= 2 個八位組（uint）  Minor Number（特定信標識別符號）= 2 個八位組（uint） |
| TxPower | 表示距裝置一米處的訊號強度 | 1 個八位組（int） |

### iBeacon PDU 載荷結構 {#ibeacon-pdu-payload-structure}

| 八位組 | 值 | | |
| --- | --- | --- | --- |
| 0 | 02 | Flags | flags 欄位的長度 |
| 1 | 01 | Flags | flags 欄位的型別 |
| 2 | 06 | Flags | flags 欄位的資料 |
| 3 | 1a | ManufacturerData | 公司識別符號 |
| 4 | ff | ManufacturerData | 公司識別符號 |
| 5 | 4c | ManufacturerData | 公司識別符號 |
| 6 | 00 | ManufacturerData | 公司識別符號 |
| 7 | 02 | BeaconType | 次級識別符號 |
| 8 | 15 | RemainingDataLength | 以位元組為單位定義載荷的剩餘長度 |
| 9 | xx* | UserData | Proximity UUID |
| 10 | xx* | UserData | Proximity UUID |
| 11 | xx* | UserData | Proximity UUID |
| 12 | xx* | UserData | Proximity UUID |
| 13 | xx* | UserData | Proximity UUID |
| 14 | xx* | UserData | Proximity UUID |
| 15 | xx* | UserData | Proximity UUID |
| 16 | xx* | UserData | Proximity UUID |
| 17 | xx* | UserData | Proximity UUID |
| 18 | xx* | UserData | Proximity UUID |
| 19 | xx* | UserData | Proximity UUID |
| 20 | xx* | UserData | Proximity UUID |
| 21 | xx* | UserData | Proximity UUID |
| 22 | xx* | UserData | Proximity UUID |
| 23 | xx* | UserData | Proximity UUID |
| 24 | xx* | UserData | Proximity UUID |
| 25 | xx* | UserData | 主版本號 |
| 26 | xx* | UserData | 主版本號 |
| 27 | xx* | UserData | 次版本號 |
| 28 | xx* | UserData | 次版本號 |
| 29 | xx* | TxPower | 表示距裝置一米處的訊號強度 |

\* - 可能有所不同

## Eddystone-TLM 封包結構 {#eddystone-tlm-packet-structure}

Eddystone-TLM 是受支援的廣播封包型別之一。你可以透過[連結](https://github.com/google/eddystone/blob/master/eddystone-tlm/tlm-plain.md)瞭解有關該協定的更多資訊。

在這種情況下，PDU Payload 由 "AdvA"（長度為 6 個八位組）和 "AdvData"（包含資料資訊的欄位）欄位組成。MikroTik 預設 CompleteUUID=03 03 aa fe；ServiceData=11 16 aa fe。

"AdvData" 欄位結構：

| 屬性 | 描述 | |
| --- | --- | --- |
| Flags | Flags 欄位的長度、型別和資料。用於"告知"周圍的掃描器裝置處於何種狀態。 | 3 個八位組（`020106`）：  第 1 個八位組 - 長度  第 2 個八位組 - 型別  第 3 個八位組 - 資料 |
| CommonPayload | 所有 Eddystone 幀型別共有的廣播載荷部分 |  CompleteUUID（通用唯一識別符號）= 4 個八位組（const）  ServiceData（*16 位 UUID* 資料型別）= 4 個八位組（const）  FrameType（值 = `0x20`）= 1 個八位組（const） |
| TlmPayload | Eddystone-TLM 幀載荷 |  Version（TLM 版本）= 1 個八位組（const）  BatteryVoltageMv（電池電壓，1 mV/位）= 2 個八位組（uint）  TemperatureC（信標溫度，單位為攝氏度）= 2 個八位組（int）  AdvertisementCount（廣播 PDU 計數）= 4 個八位組（uint）  UptimeCounter（自開機或重啟以來的時間）= 4 個八位組（uint） |

### Eddystone-TLM PDU 載荷結構 {#eddystone-tlm-pdu-payload-structure}

| 八位組 | 值 | | |
| --- | --- | --- | --- |
| 0 | 02 | Flags | flags 欄位的長度 |
| 1 | 01 | Flags | flags 欄位的型別 |
| 2 | 06 | Flags | flags 欄位的資料 |
| 3 | 03 | CommonPayload | CompleteUUID |
| 4 | 03 | CommonPayload | CompleteUUID |
| 5 | aa | CommonPayload | CompleteUUID |
| 6 | fe | CommonPayload | CompleteUUID |
| 7 | 11 | CommonPayload | ServiceData |
| 8 | 16 | CommonPayload | ServiceData |
| 9 | aa | CommonPayload | ServiceData |
| 10 | fe | CommonPayload | ServiceData |
| 11 | 20 | CommonPayload | FrameType |
| 12 | 00 | TlmPayload | Version |
| 13 | xx* | TlmPayload | BatteryVoltageMv |
| 14 | xx* | TlmPayload | BatteryVoltageMv |
| 15 | xx* | TlmPayload | TemperatureC |
| 16 | xx* | TlmPayload | TemperatureC |
| 17 | xx* | TlmPayload | AdvertisementCount |
| 18 | xx* | TlmPayload | AdvertisementCount |
| 19 | xx* | TlmPayload | AdvertisementCount |
| 20 | xx* | TlmPayload | AdvertisementCount |
| 21 | xx* | TlmPayload | UptimeCounter |
| 22 | xx* | TlmPayload | UptimeCounter |
| 23 | xx* | TlmPayload | UptimeCounter |
| 24 | xx* | TlmPayload | UptimeCounter |

\* - 可能有所不同

## Eddystone-UID 封包結構 {#eddystone-uid-packet-structure}

Eddystone-UID 是受支援的廣播封包型別之一。你可以透過[連結](https://github.com/google/eddystone/blob/master/eddystone-uid/README.md)瞭解有關該協定的更多資訊。

在這種情況下，PDU Payload 由 "AdvA"（長度為 6 個八位組）和 "AdvData"（包含資料資訊的欄位）欄位組成。MikroTik 預設 CompleteUUID=03 03 aa fe；ServiceData=17 16 aa fe。

"AdvData" 欄位結構：

| 屬性 | 描述 | |
| --- | --- | --- |
| Flags | Flags 欄位的長度、型別和資料。用於"告知"周圍的掃描器裝置處於何種狀態。 | 3 個八位組（`020106`）：  第 1 個八位組 - 長度  第 2 個八位組 - 型別  第 3 個八位組 - 資料 |
| CommonPayload | 所有 Eddystone 幀型別共有的廣播載荷部分 |  CompleteUUID（通用唯一識別符號）= 4 個八位組（const）  ServiceData（*16 位 UUID* 資料型別）= 4 個八位組（const）  FrameType（值 = `0x00`）= 1 個八位組（const） |
| UidPayload | Eddystone-UID 幀載荷 |  Ranging Data（0 米處校準的發射功率）= 1 個八位組（int）  Nspace（自行分配的唯一信標 ID 名稱空間）= 10 個八位組（uint）  Instance（名稱空間內的唯一 ID）= 6 個八位組（uint）  RFU1（保留供將來使用，值=`0x00`）= 1 個八位組（const）  RFU2（保留供將來使用，值=`0x00`）= 1 個八位組（const） |

### Eddystone-UID PDU 載荷結構 {#eddystone-uid-pdu-payload-structure}

| 八位組 | 值 | | |
| --- | --- | --- | --- |
| 0 | 02 | Flags | flags 欄位的長度 |
| 1 | 01 | Flags | flags 欄位的型別 |
| 2 | 06 | Flags | flags 欄位的資料 |
| 3 | 03 | CommonPayload | CompleteUUID |
| 4 | 03 | CommonPayload | CompleteUUID |
| 5 | aa | CommonPayload | CompleteUUID |
| 6 | fe | CommonPayload | CompleteUUID |
| 7 | 17 | CommonPayload | ServiceData |
| 8 | 16 | CommonPayload | ServiceData |
| 9 | aa | CommonPayload | ServiceData |
| 10 | fe | CommonPayload | ServiceData |
| 11 | 00 | CommonPayload | FrameType |
| 12 | xx* | UidPayload | 測距資料 |
| 13 | xx* | UidPayload | Nspace |
| 14 | xx* | UidPayload | Nspace |
| 15 | xx* | UidPayload | Nspace |
| 16 | xx* | UidPayload | Nspace |
| 17 | xx* | UidPayload | Nspace |
| 18 | xx* | UidPayload | Nspace |
| 19 | xx* | UidPayload | Nspace |
| 20 | xx* | UidPayload | Nspace |
| 21 | xx* | UidPayload | Nspace |
| 22 | xx* | UidPayload | Nspace |
| 23 | xx* | UidPayload | Instance |
| 24 | xx* | UidPayload | Instance |
| 25 | xx* | UidPayload | Instance |
| 26 | xx* | UidPayload | Instance |
| 27 | xx* | UidPayload | Instance |
| 28 | xx* | UidPayload | Instance |
| 29 | 00 | UidPayload | RFU1 |
| 30 | 00 | UidPayload | RFU2 |

\* - 可能有所不同

## 裝置名稱 {#device-name}

啟用後，標籤將廣播一個包含所配置 "Device Name" 的短載荷。

| 屬性 | 描述 | |
| --- | --- | --- |
| Flags | Flags 欄位的長度、型別和資料。用於"告知"周圍的掃描器裝置處於何種狀態。 | 3 個八位組（`020106`）：  第 1 個八位組 - 長度  第 2 個八位組 - 型別  第 3 個八位組 - 資料 |
| Complette Local Name | 廣播載荷中包含本地名稱資訊的部分。 |  Length = 1 個八位組  AD type = 1 個八位組  Name bytes = x 個八位組。 |

### 裝置名稱 PDU 載荷結構 {#device-name-pdu-payload-structure}

如果我們將 "Device Name" 配置為 "TG-BT5-OUT"：

| 八位組 | 值 | | |
| --- | --- | --- | --- |
| 0 | 02 | Flags | flags 欄位的長度 |
| 1 | 01 | Flags | flags 欄位的型別 |
| 2 | 06 | Flags | flags 欄位的資料 |
| 3 | 0b | Length | 長度位元組 |
| 4 | 09 | AD Type | 完整本地名稱的型別位元組 |
| 5 | 54 | 名稱位元組 #1 | ASCII "T" |
| 6 | 47 | 名稱位元組 #2 | ASCII "G" |
| 7 | 2d | 名稱位元組 #3 | ASCII "-" |
| 8 | 42 | 名稱位元組 #4 | ASCII "B" |
| 9 | 54 | 名稱位元組 #5 | ASCII "T" |
| 10 | 35 | 名稱位元組 #6 | ASCII "5" |
| 11 | 2d | 名稱位元組 #7 | ASCII "-" |
| 12 | 4f | 名稱位元組 #8 | ASCII "O" |
| 13 | 55 | 名稱位元組 #9 | ASCII "U" |
| 14 | 54 | 名稱位元組 #10 | ASCII "T" |
