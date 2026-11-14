---
sidebar_key: "internet-of-things/bluetooth/user-guides/sending-temperature-readings-from-tg"
sidebar_position: 7
title: "傳送 TG-BT5-OUT 標籤的溫度讀數到 ThingsBoard"
sidebar_label: "傳送 TG-BT5-OUT 標籤的溫度讀數到 ThingsBoard"
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/bluetooth/user-guides/sending-temperature-readings-from-tg
captured_at: '2026-11-04T11:18:56+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 簡介 {#introduction}

我們的 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out) 藍牙標籤型號內建了溫度感測器。這意味著它可以用於測量周圍溫度。

溫度值會被“寫入”標籤將要透過藍牙廣播通道廣播的廣播負載中。根據你配置標籤的方式，標籤可以定期廣播負載，和/或在檢測到觸發時廣播。你可以在[連結的章節](../mikrotik-beacon-manager/index.md)中找到有關標籤配置選項的更多資訊。

你可以使用我們的 [KNOT](https://mikrotik.com/product/knot) 型號在 **IoT>Bluetooth>Advertising reports** 標籤頁下檢視/顯示這些負載：

![](/img/f27669ef09b2c2b0.webp)

負載將顯示在“Advertisement (hex)”欄位中，並且將採用**十六進位制**格式。

當標籤配置為 MikroTik 格式時，負載的第 14 和第 15 個八位組表示溫度（以攝氏度為單位的環境溫度，採用**有符號 16 位整數 [二進位制補碼] 8.8 定點格式**），該溫度是在廣播時刻“感測”到的。

下面展示了 MikroTik 格式的負載示例：

| 15ff4f09010032a500000000ffff `5019` bd5954000061 |
| --- |

請注意，負載中的所有多位元組值都採用小端序。因此，如果第 #14 和第 #15 個八位組表示的溫度為“**50 19**” → 你需要交換八位組的位置，變為 0x**1950**。

正溫度：

我們捕獲到的溫度為 0x**1950**（十六進位制）→ **6480**（十進位制）。要得到實際溫度值，請將結果除以 256 → 6480/256=**25.31 C**。

負溫度：

我們捕獲到的溫度為 0x**FE80**（十六進位制）。請記住使用的是**二進位制補碼格式** → **-384**（有符號二進位制補碼的十進位制值）。要得到實際溫度值，請將結果除以 256 → -384/256=**-1.5 C**。

藉助這些知識，我們可以利用 RouterOS 指令碼將接收到的負載組織成一條訊息，並將其傳送到 MQTT/HTTP 伺服器。建議由伺服器負責將資料從**十六進位制**格式轉換為**十進位制**格式。**但是！** 如果你願意給 RouterOS 裝置增加負載，你可以使用 RouterOS 指令碼執行**十六進位制**值到**十進位制**格式的轉換（這會增加裝置負載並可能影響 RouterOS 效能 → 我們建議在伺服器上轉換值，而不是在 RouterOS 上）。在本指南中，我們將透過向 [ThingsBoard](https://thingsboard.io/) 傳送 MQTT 訊息來實現結果。

### ThingsBoard 伺服器與 MQTT 配置 {#thingsboard-server-and-mqtt-configuration}

你需要有一個正在執行的 ThingsBoard 伺服器。你可以透過訪問[連結](https://thingsboard.io/docs/installation/)找到有關如何設定伺服器的有用資訊。你可以將伺服器本地安裝到一臺機器上，或使用他們的雲解決方案。

伺服器準備好後，你需要對其進行配置，使其能夠接收 MQTT 訊息。請按照 [ThingsBoard 配置](../../mqtt/mqtt-and-thingsboard-configuration.md)連結來設定你的“裝置”。

### RouterOS 配置 {#routeros-configuration}

請檢視[這裡的連結](../../mqtt/mqtt-and-thingsboard-configuration.md)，瞭解如何根據 ThingsBoard 伺服器使用的裝置憑據設定你的 MQTT broker。

設定好 broker 後，確認藍牙標籤正在廣播資訊，如上圖在 **IoT>Bluetooth>Advertising reports** 標籤頁下所示。

#### 指令碼 {#script}

將下面的指令碼貼上進去（在 **System>Scripts>Add** 下）：

```ros
## 所需软件包：iot

################################ Configuration ################################
## 用于发布的现有 MQTT broker 的名称
 :local broker "tb"

## 消息应发布到的 MQTT 主题
 :local topic "v1/devices/me/telemetry"

 # Interface whose MAC should be used as 'Locator ID'
:local locatorIface "ether1"

## 用于过滤蓝牙广播地址的 POSIX 正则表达式。例如 "^BC:33:AC"
## 将只包含以这 3 个八位组开头的地址。
## 要禁用此过滤器，请将其设置为 ""
:local addressRegex "2C:C8:1B:4B:BB:0A"

## 用于根据蓝牙广播数据过滤蓝牙广播的 POSIX 正则表达式。与
## 使用 'addressRegex' 时的用法相同。
:local advertisingDataRegex ""

## 信号强度过滤器。例如，-40 将只包括蓝牙广播
## 其信号强度强于 -40dBm。
## 要禁用此过滤器，请将其设置为 ""
:local rssiThreshold ""

####The lines below are used for the data conversion from hex to dec###

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

################################## Bluetooth ##################################
:put ("[*] Gathering Bluetooth info...")
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
    :set $btOldestAdvertisementTimestamp 0
}
:local btProcessingStart [/system clock get time]
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex and \
        data ~ $advertisingDataRegex and \
        rssi > $rssiThreshold
]
:local advJson ""
:local advCount 0
:local advSeparator ""
:local lastAdvTimestamp 0
## 从 MAC/蓝牙地址中移除分号
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
    :local ts ($adv->"epoch")
    :local rssi ($adv->"rssi")
    :local ad ($adv->"data")
    :local tempf [:pick ($adv->"data") 28 32]

#下面一行将以十六进制格式设置温度，例如 "0x1950"
    :local temp ([:pick $tempf 2 4].[:pick $tempf 0 2])

#下面一行将以十进制格式设置温度，例如 "25313"。它用 "#" 注释掉了，因此如果你希望使用它而不是十六进制格式值，请注释上面一行，并取消注释下面一行 > 从下面一行移除 "#"，并向上面一行添加 "#"。

##    :local temp [$from88 [:pick $ad 28 32]]

    :local obj "{\
        \
           \"ts\":$ts,\
           \"values\":{\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"rssi\":\"$rssi\",\
            \"temp\":\"$temp\",\
            \"ad\":\"$ad\"\
            }\
        }"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $ts
    # Ensure that the last object is not terminated by a comma
    :set $advJson "$advJson$advSeparator$obj"
    :if ($advSeparator = "") do={
        :set $advSeparator ","}
}

:if ($advCount > 0) do={

    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp

}

:put ("[*] Found $advCount new advertisements \
    (processing time: $[([/system clock get time] - $btProcessingStart)])")

#################################### MQTT #####################################
:local message \
    "[$advJson]"
:log info "$message";
:put ("[*] Total message size: $[:len $message] bytes")
:put ("[*] Sending message to MQTT broker...")
/iot mqtt publish broker=$broker topic=$topic message=$message
:put ("[*] Done")
```

**更改你為 MQTT broker 選擇的 broker 名稱**，位於引號內（在我們的示例中，我們將其稱為 **tb**）：

```
 :local broker "tb"
```

ThingsBoard 使用的預設主題是（你無需更改它）：

```
 :local topic "v1/devices/me/telemetry"
```

**更改你希望監控的標籤的 MAC 地址**（在我們的示例中，MAC 地址為 **2C:C8:1B:4B:BB:0A**）：

```
:local addressRegex "2C:C8:1B:4B:BB:0A"
```

下面的行將獲取負載的第 14 和第 15 個八位組，並將值從“ABCD”“重新組織”為“CDAB”（根據我們在**簡介**部分的示例，從“**5019**”變為“**1950**”）→ 基本上就是用**十六進位制**格式的溫度來組織訊息：

```
    :local tempf [:pick ($adv->"data") 28 32]
    :local temp ([:pick $tempf 2 4].[:pick $tempf 0 2])
```

你的第二個選擇是使用 RouterOS 將溫度從**十六進位制**格式轉換為**十進位制**格式（如果你想保留十六進位制格式——忽略此步驟）。這可以透過對上一行進行“註釋”（新增 `#`）（或將其完全刪除），並對下一行進行“取消註釋”（移除 `#`）來實現，如下所示：

```
#  :local temp ([:pick $tempf 2 4].[:pick $tempf 0 2])
    :local temp [$from88 [:pick $ad 28 32]]
```

由於不支援浮點數 → 小數點後的每次計算都會被“向上舍入”為整數。這就是指令碼會計算**按 1000 縮放**（乘以 **1000**）的溫度的原因，結果溫度看起來會像“**25546**”（這意味著 25.546 C）。你可以新增額外的指令碼設定小數點（但請記住，額外的操作會增加裝置負載），你也可以在伺服器本身上執行此操作。

我們要釋出的 MQTT 訊息在以下部分中組織（你無需更改它）：

```
    :local obj "{\
        \
           \"ts\":$ts,\
           \"values\":{\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"rssi\":\"$rssi\",\
            \"temp\":\"$temp\",\
            \"ad\":\"$ad\"\
            }\
        }"
```

按上述示例組織的訊息將以 JSON 顯示（我們唯一關注的實際值是 "timestamp"→ "ts" 和 "temperature"→ "temp"，因此請隨意刪除其他引數）。如果溫度以**十六進位制**格式計算，訊息將如下所示：

```
[
  {
    "ts": 1661333913375,
    "values": {
      "id": "2CC81B4BBB0A",
      "rssi": "-43",
      "temp": "1939",
      "ad": "15ff4f0901002de0ffff010000003919877c54000061"
    }
  }
]
```

如果溫度以**十進位制**格式計算，則如下所示：

```
[
  {
    "ts": 1661333913375,
    "values": {
      "id": "2CC81B4BBB0A",
      "rssi": "-43",
      "temp": "25222",
      "ad": "15ff4f0901002de0ffff010000003919877c54000061"
    }
  }
]
```

儲存指令碼並執行它：

```ros
[admin@MikroTik] > system script run name_of_the_script
[*] Gathering system info...
[*] Gathering Bluetooth info...
[*] Found 1 new advertisements (processing time: 00:00:00)
[*] Total message size: 134 bytes
[*] Sending message to MQTT broker...

[*] Done
[admin@MikroTik] > 
```

#### 排程器 {#scheduler}

為指令碼應用排程器，以所需間隔執行它。**請注意！** 如果你已將排程器設定為執行指令碼，例如每 2 分鐘一次，這意味著在 2 分鐘間隔內收到的每個負載（由標籤廣播）都會被“組織”成 MQTT 訊息。你很可能不需要每 2-5 秒就知道標籤的溫度，因此你可以更改要組織的 MQTT 訊息，使其僅釋出最新的溫度讀數，或者只需將 **IoT>Bluetooth>Scanners** 設定中的 **Filter duplicates** 改為“**keep-newest**”（這樣，藍牙掃描器將覆蓋來自每個單獨標籤 MAC 地址的每個新報告），指令碼將只發布執行指令碼時“掃描”到的 1 個負載。

#### 結果 {#results}

你將能夠在為 ThingsBoard 建立的裝置下的 **Latest telemetry** 部分驗證結果（在我們的示例中，我們將“裝置”稱為 **KNOT**）：

![](/img/0e9796c6af1fc040.webp)

結果是成功的 MQTT 釋出！從上面的截圖可以看出，**temp** 引數採用**十六進位制**格式。

**但是！** 我們希望以**十進位制**格式顯示溫度（**temp** 引數），並且我們還希望以更易於理解的方式顯示資料。

而且，如果我們以**十進位制**格式釋出了溫度，我們還希望設定小數點。

這時 [小元件](https://thingsboard.io/docs/reference/widgets/widget-library/) 就派上用場了。

### ThingsBoard 小元件 {#thingsboard-widgets}

在 **Latest telemetry** 部分收到值後，你可以在 [**小元件**](https://thingsboard.io/docs/reference/widgets/widget-library/) 上顯示它。

小元件中使用的 Javascript 應能夠將資料從十六進位制格式轉換為十進位制格式。

在小元件中選擇你希望顯示的值（在我們的示例中為 **temp**），然後單擊“**Show on widget**”按鈕：

![](/img/9a72513b07ecb866.webp)

你將能夠在彈出的視窗中瀏覽這些小元件：

![](/img/425bf9428fc12142.webp)

單擊“**Add to dashboard**”按鈕：

![](/img/41301e711031f806.webp)

選擇要建立的新儀表板，或選擇你已預安裝/預先製作的現有儀表板。單擊“**Add**”。

勾選“**Open dashboard**”複選框後，你將重定向到儀表板選單，或者你也可以手動前往那裡。

我們還添加了第二個表格，結果我們的測試儀表板如下所示：

![](/img/2f1fe9db70477aaa.webp)

#### 如果我們以十六進位制格式釋出資料 {#in-case-we-post-the-date-in-hexadecimal-format}

兩個表格都會以**十六進位制格式**顯示值，如“17f9”（即我們從 KNOT 傳送的原始值 → 表格的 javascript 尚未將其轉換為十進位制值）。

由於我們標籤負載中的值採用有符號 8.8 定點格式（請記住二進位制補碼格式），我們將需要新增額外的 javascript 程式碼來將資料“轉換”為十進位制值。

進入“**Edit**”模式，然後單擊“**Edit widget**”按鈕：

![](/img/d660e0155664ce0e.webp)

單擊“**edit**”按鈕以編輯引數 **temp**：

![](/img/8c092989aafd5e24.webp)

在彈出的“**Data key configuration**”視窗中，啟用“**Use data post-processing function**”複選框，並輸入下面顯示的程式碼：

![](/img/d4991082836ee6e1.webp)

程式碼：

```
function f(p){

this.p = p;

}

f.prototype.calculate = function(mes){

let intValue = parseInt(mes, 16);

let sign = 1;

if(intValue & 0x8000) {

intValue = (~intValue + 1) & 0xFFFF;

sign = -1;

}

intValue = sign * intValue / Math.pow(2, this.p);

return intValue;

}

let res = new f(8);

return (res.calculate(value));
```

儲存並應用更改。

對第二個/第一個表格執行相同步驟。

#### 如果我們以十進位制格式釋出資料 {#in-case-we-post-the-date-in-decimal-format}

你將看到如下結果：

![](/img/8bb9762b131302ce.webp)

執行與上面示例完全相同的步驟，但在此場景中，**將結果除以“1000”**：

![](/img/e0c5860cefccf0bf.webp)

儲存並應用更改。

#### 驗證 {#verification}

最終結果應如下所示：

![](/img/33deb05fef380365.webp)

現在兩個表格都顯示**十進位制溫度**。
:::info
你也可以在將遙測資料儲存到 ThingsBoard 之前對其進行轉換。使用此方案時，每次開啟儀表板都不會對資料進行後處理。

以下指南可作為轉換資料的通用方法：[轉換節點](https://thingsboard.io/docs/user-guide/rule-engine-2-0/transformation-nodes/)。
:::
