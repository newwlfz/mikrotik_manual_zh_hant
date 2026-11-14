---
sidebar_key: "internet-of-things/mqtt/index"
sidebar_position: 2
title: "MQTT"
sidebar_label: "MQTT"
description: "本頁介紹 MikroTik RouterOS 中的 MQTT 整合，涵蓋面向 Kaa 和 ThingsBoard 等 IoT 平臺的釋出者/訂閱者工作流程。其中講解了 MQTT 協定基礎、RouterOS 作為 MQTT broker/client 的能力，並提供了針對 AWS/Azure 雲平臺的配置示例。"
tags:
  - 'mqtt'
  - 'iot'
  - 'publish-subscribe'
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/mqtt
captured_at: '2026-11-04T11:19:13+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 MQTT 整合示例。可透過這些示例把 RouterOS 的 MQTT 釋出與訂閱工作流接入 Kaa IoT、ThingsBoard 等物聯網平臺。

<DocCardList />

MQTT 是一種開放、遵循 OASIS 和 ISO 標準的輕量級釋出-訂閱網路協定，用於在裝置之間傳輸訊息。典型的 MQTT 通訊拓撲包括：

- MQTT 釋出者 → 向伺服器傳送資訊的裝置。
- MQTT broker → 儲存資料的伺服器。
- MQTT 訂閱者 → 讀取/監視伺服器上已釋出資料的裝置。

RouterOS 可以充當 MQTT 釋出者和訂閱者（從 **7.11beta2** 開始）。你也可以透過 [container](../../containers/index.md) 功能執行 MQTT broker/伺服器。有關 Mosquitto MQTT broker 的配置，請訪問[此連結](../../containers/user-guides/container-mosquitto-mqtt-server.md)。

以下是可以找到的 MQTT 釋出場景應用示例：

a) [使用 AWS 雲平臺的 MQTT/HTTPS 示例](https://help.mikrotik.com/docs/pages/viewpage.action?pageId=63045633)

b) [使用 Azure 雲平臺的 MQTT 示例](https://help.mikrotik.com/docs/display/UM/MQTT+and+Azure+configuration)

c) [MQTT 與 ThingsBoard 配置](./mqtt-and-thingsboard-configuration.md)

請注意，AWS 和 Azure 示例（指令碼）演示的是釋出藍牙標籤資料。目前只有 [KNOT](https://mikrotik.com/product/knot) 內建藍牙晶片。

## 配置 {#configuration}

**子選單：** `/iot/mqtt`

***注意**：* 需要 **iot** 軟體包。

IoT 軟體包從 RouterOS 6.48.3 版本開始提供。你可以從我們的[下載頁面](https://mikrotik.com/download)獲取它——位於“Extra packages”下。

| 屬性 | 描述 |
| :-- | :-- |
| **brokers** | 已配置的 MQTT broker 列表。 |
| **connect** | 用於指定要連線哪個 broker 的命令。 |
| **disconnect** | 用於指定要斷開哪個 broker 的命令。 |
| **publish** | 用於定義需要釋出的 MQTT 訊息的命令。 |
| **subscribe** | 用於定義要訂閱的 MQTT 主題的命令。 |
| **subscriptions** | 已訂閱主題和已接收訊息的列表。 |
| **unsubscribe** | 用於指定要取消訂閱哪個主題的命令。 |

### Brokers {#brokers}

**子選單：** `/iot/mqtt/brokers`

要新增新的 MQTT broker（或 MQTT 伺服器），請執行以下命令：

```ros
/iot/mqtt/brokers/add
```

可配置屬性如下所示：

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP\|hostname*; Default: ) | 代理伺服器的 IP 地址或主機名。 |
| **auto-connect** (*yes \| no*; Default: **no**) | 啟用後，當與 MQTT 代理伺服器的連線斷開/中斷時，RouterOS 將不斷嘗試重新建立連線。 |
| **certificate** (*string*; Default: ) | [證書儲存中的證書](../../authentication-authorization-accounting/certificates.md)，將用於 SSL 連線。 |
| **client-id** (*string*; Default: ) | 用於連線的唯一 ID。代理伺服器使用此 ID 來識別用戶端。 |
| **keep-alive** (*integer:30..64800*; Default: **60**) | 定義時間（以秒為單位）的引數，超過該時間後，用戶端應向 MQTT 代理伺服器“ping”以表明自己“存活”，從而確保連線保持進行。此值應根據 MQTT 代理伺服器設定進行設定。 |
| **name** (*string*; Default: ) | 代理伺服器的描述性名稱。 |
| **parallel-scripts-limit**(*integer:3..1000;* Default: off) | 定義此代理伺服器的 [on-message](#subscriptions) 功能允許同時執行多少個指令碼的引數。在持續釋出大量訊息的情況下，可用於降低 CPU 使用率。 |
| **password** (*string*; Default: ) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 代理伺服器的密碼（如果代理伺服器要求）。 |
| **port** (*integer:*0..4294967295**; Default: **1883**) | 代理伺服器使用的網路埠。 |
| **ssl** (*yes \| no*; Default: **no**) | Secure Socket Layer 配置。 |
| **username** (*string*; Default: ) | 代理伺服器的使用者名稱（如果代理伺服器要求）。 |
| **will-message** (*string*; Default: ) | 配置 Last Will and Testament (LWT) 訊息，該訊息將在連線期間傳送到代理伺服器。此訊息將儲存在代理伺服器上。除非 RouterOS 意外斷開與代理伺服器的連線（未傳送正確的“DISCONNECT”封包），否則該訊息不會（由代理伺服器）釋出。 |
| **will-qos**(*integer*; Default: ) | 配置 LWT 訊息的 QoS 值。 |
| **will-retain**(yes \| no; Default: ) | 配置是保留 LWT 訊息還是不保留。 |
| **will-topic**(*string*; Default: ) | 配置 LWT 主題，**will-message** 應釋出到該主題。 |

新增 broker 的示例：

```ros
/iot/mqtt/brokers/add name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60
```

結果：

```ros
/iot/mqtt/brokers/print
 0 name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60 connected=no 
```

### Connect {#connect}

**子選單：** `/iot/mqtt/connect`

要連線到預先配置的 MQTT broker，請執行以下命令：

```ros
/iot/mqtt/connect broker="broker"
```

如果連線成功，“**connected**”引數應變為“**yes**”：

```ros
/iot/mqtt/brokers/print
 0 name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60 connected=yes
```

### Disconnect {#disconnect}

**子選單：** `/iot/mqtt/disconnect`

要斷開與 MQTT broker 的連線，請執行以下命令：

```ros
/iot/mqtt/disconnect broker="broker"
```

要確認 broker 已斷開連線，請執行下面的命令，它應顯示“**connected=no**”：

```ros
/iot/mqtt/brokers/print            
 0 name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60 connected=no 
```

### Publish {#publish}

**子選單：** `/iot/mqtt/publish`

Publish 選單用於向 MQTT broker 傳送 MQTT 訊息。

| 屬性 | 描述 |
| :-- | :-- |
| **broker** (*string*; Default: ) | 選擇要將訊息釋出到哪個 broker。 |
| **disconnect-after** (*yes \| no*; Default: **no**) | 該引數確保在釋出訊息傳送後，與 broker 的連線會被自動斷開。 |
| **force** (*yes \| no*; Default: **yes**) | 如果設定為“yes”，當尚未與 broker 建立連線（“**connected=no**”）而嘗試釋出訊息時，RouterOS 會先嚐試與指定的 broker 建立 MQTT 連線，然後再發布訊息。如果設定為“no”，除非事先已建立連線（“**connected=yes**”），否則 RouterOS 將無法傳送該訊息。 |
| **message** (*string*; Default: ) | 你希望釋出到 broker 的訊息。 |
| **qos** (*integer:*0..2**; Default: **0**) | 由 broker 定義的服務質量引數。qos=0 → 訊息最多被接收一次（訊息發出後即不再管，發後即忘）；qos=1 → 訊息至少被接收一次（訊息會持續傳送，直到釋出者從 broker 收到確認封包 <code>PUBACK</code>）；qos=2 → 訊息恰好被接收一次（訊息會被髮送，並透過四次封包互動確保只投遞一次）； |
| **retain** (*yes \| no*; Default: **no**) | 是保留訊息，還是在無人訂閱該主題時將其丟棄。此引數由 broker 定義。保留的訊息會儲存在 broker 上，並由 broker 自動傳送給新的訂閱者。 |
| **topic** (*string*; Default: ) | 由 broker 定義的主題。 |

釋出訊息的示例：

```ros
/iot/mqtt/publish message="test-message" broker="broker" topic="my/test/topic"
```

### Subscribe {#subscribe}

**子選單：** `/iot/mqtt/subscribe`

:::info
請記住，如果你與 broker 已有正在進行的連線（連線處於“**connected=yes**”狀態），並且你透過該 broker 訂閱主題，那麼你必須重新建立連線！
:::

此選單用於訂閱 broker 上的 MQTT 主題。

| 屬性 | 描述 |
| :-- | :-- |
| **broker** (*string*; Default: ) | 選擇要訂閱的 broker。 |
| **force** (*yes \| no*; Default: **yes**) | 如果設定為“yes”，當尚未與 broker 建立連線（“**connected=no**”）而嘗試訂閱時，RouterOS 會先嚐試與指定的 broker 建立 MQTT 連線，然後再訂閱該主題。如果設定為“no”，除非事先已建立連線（“**connected=yes**”），否則 RouterOS 將無法訂閱該主題。 |
| **qos** (*integer:*0..2**; Default: **0**) | 由 broker 定義的服務質量引數。 |
| **topic** (*string*; Default: ) | 要訂閱的主題，由 broker 定義。 |

#### 訂閱示例 {#an-example-of-a-subscription}

```ros
/iot/mqtt/subscribe broker="broker" topic="my/test/topic"
```

也支援萬用字元（單層“**+**”和多層“**#**”）訂閱（RouterOS **不允許向萬用字元主題釋出**，**但允許訂閱**它們）：

```ros
/iot/mqtt/subscribe broker="broker" topic="my/test/#"
/iot/mqtt/subscribe broker="broker" topic="my/test/+"
```

這意味著，如果你訂閱 `topic="my/test/#"`，你將能收到釋出到任何以萬用字元符號“#”之前的模式開頭的主題的訊息（例如 `"my/test/topic"`、`"my/test/topic/something"`）。

另外，如果你訂閱 `topic="my/test/+"`，你將能收到釋出在該主題 +1 層級上的訊息（例如 `"my/test/topic"`、`"my/test/something"`）。

### Subscriptions {#subscriptions}

**子選單：** `/iot/mqtt/subscriptions`

本節用於管理已新增的訂閱（即之前透過 [Subscribe](./index.md#subscribe) 部分新增的訂閱）。

它的屬性與 [Subscribe](./index.md#subscribe) 部分相同。

:::info
從 **v7.12beta9** 開始，此選單允許你為訂閱新增“**on-message**”設定。
:::

| 屬性 | 描述 |
| :-- | :-- |
| **on-message** (*string*; Default: ) | 配置一個[指令碼](../../developer-guides/scripting/index.md)，每當訂閱的主題中收到新訊息時，該指令碼就會被自動啟動/執行。 |

要檢視已訂閱的主題，請執行以下命令：

```ros
/iot/mqtt/subscriptions/print
0 broker=broker topic="my/test/topic" qos=0
```

按上文 **Publish** 部分的說明發布一條測試訊息後：

```ros
/iot/mqtt/publish message="test-message" broker="broker" topic="my/test/topic"
```

你應該能在以下位置檢視收到的訊息：

```ros
/iot/mqtt/subscriptions/recv/print
 0 broker=broker topic="my/test/topic" data="test-message" time=2023-05-22 16:57:00 
```

:::info
已接收訊息列表最多保留 1024 條，超過後較舊的條目會被新條目覆蓋。
:::

要清除已儲存的訊息，請執行以下命令：

```ros
/iot/mqtt/subscriptions/recv/clear
```

要在訂閱的主題中出現任何新訊息時執行[指令碼](../../developer-guides/scripting/index.md)（例如一個基本的“log”指令碼），可以使用 `on-message` 功能：

```ros
/iot/mqtt/subscriptions/set on-message={:log info "Got data {$msgData} from topic {$msgTopic}"} broker=broker 0
```

指令碼可以使用 **$msgData** 和 **$msgTopic** 變數。**$msgData** 表示已釋出的 MQTT 訊息，**$msgTopic** 表示該訊息釋出到的 MQTT 主題。這兩個變數都會在出現新訊息時自動生成。

:::note

- **$msgData** 和 **$msgTopic** 變數在用於“**System>Script**”部分建立的指令碼時不會起作用，也就是說，它們在透過 "/iot/mqtt/subscriptions/set **on-message=\{`/system/script/run` x}**" 新增的指令碼內部不會起作用。這兩個變數只有在“**on-message=\{}**”所編寫的指令碼內部使用時才有效，例如“**on-message=\{:log info "Got data \{$msgData} from topic \{$msgTopic}"}**”。
- [global](../../developer-guides/scripting/index.md#scopes) 變數的使用也是如此。如果有透過其他指令碼“生成”的全域性變數（即出現在 System>Script>Environment 部分下的變數），它們在“on-message”指令碼內部不會生效。

:::

在向訂閱的主題釋出一條新的 MQTT 訊息後，應出現一條新的日誌條目：

```ros
/log/print
10:19:15 script,info Got data {test-message} from topic {my/test/topic}
```

第二個示例展示瞭如何在出現特定訊息（訊息中的關鍵字）時執行指令碼。要在 MQTT 訊息具有特定內容或關鍵字時才執行指令碼，我們可以使用 **if** [條件語句](../../developer-guides/scripting/index.md#conditional-statement)：

```ros
/iot/mqtt/subscriptions/set 0 on-message={:if ($msgData~"\\{\"test\":\"123\"\\}") do={:log info "Got data {$msgData} from topic {$msgTopic}"}}
```

或者：

```ros
/iot/mqtt/subscriptions/set 0 on-message={:if ($msgData~"test") do={:log info "Got data {$msgData} from topic {$msgTopic}"}}
```

因此，每收到一條 MQTT 訊息，指令碼都會檢查 if 條件是否為真。如果為真（即 **$msgData** 包含 JSON 字串 **\{"test":"123"}**，或 **$msgData** 包含字串“**test**”），就會生成日誌條目。否則什麼也不會發生。

也就是說，只有當你釋出如下所示的訊息時，指令碼才會執行：

```ros
/iot/mqtt/publish broker=broker topic="my/test/topic" message="{\"test\":\"123\"}"
```

當你收到的訊息所屬的主題同時匹配多個配置了 `on-message` 的訂閱時，只會執行 **x1** 個 `on-message` 指令碼。RouterOS 會按照以下邏輯/優先順序來選擇執行哪個 `on-message` 指令碼：

1. 如果訂閱配置的主題完全匹配 → 第一優先順序。
2. 如果主題名稱不是完全匹配（使用了萬用字元）→ 第二優先順序是單層萬用字元主題。
3. 如果主題不屬於單層萬用字元類別 → 第三優先順序是根據主題層級匹配的多層萬用字元主題。

示例：

```ros
/iot/mqtt/subscriptions/print
 0 broker=broker topic="some/sort/of/topic" qos=0 on-message="/system/script/run script1" 

 1 broker=broker topic="some/#" qos=0 on-message="/system/script/run script2" 

 2 broker=broker topic="some/sort/of/+" qos=0 on-message="/system/script/run script3"  

 3 broker=broker topic="some/thing/#" qos=0 on-message="/system/script/run script4"   
```

當你把資料釋出到 `some/sort/of/topic` 時，將啟動 script1，因為該主題完全匹配。

當你把資料釋出到 `some/sort/of/thing` 時，將啟動 script3 → 因為它屬於單層萬用字元主題名稱。

當你把資料釋出到 `some/name` 時，將啟動 script2 → 因為它屬於多層萬用字元主題名稱。

當你把資料釋出到 `some/thing/else` 時，將啟動 script 4 → 因為它屬於多層萬用字元主題名稱（儘管它同時也匹配 `some/#` 萬用字元，但它距離 `some/thing/#` 條目更近一層）。

### Unsubscribe {#unsubscribe}

**子選單：** `/iot/mqtt/unsubscribe`

| 屬性 | 描述 |
| :-- | :-- |
| **broker** (*string*; Default: ) | 選擇要取消訂閱的 broker。 |
| **topic** (*string*; Default: ) | 選擇要取消訂閱的主題，由 broker 定義。 |

下面展示了從 broker 和主題取消訂閱的示例：

```ros
/iot/mqtt/unsubscribe broker="broker" topic="my/test/topic"
```

## 使用指令碼釋出 RouterOS 統計資訊 {#publishing-routeros-statistics-using-scripts}

你還可以使用[指令碼](../../developer-guides/scripting/index.md)來組織包含 RouterOS 統計資訊的 MQTT 訊息。然後，可以應用[排程器](../../system-information-and-utilities/scheduler.md)在你需要的時候執行該指令碼。

例如，你可以執行類似 [mqttpublish.rsc](pathname:///assets/200573055_mqttpublish.rsc) 的指令碼（將下面所示 RouterOS 程式碼的內容複製到新的終端中，然後按 <kbd>Enter</kbd>）：

```ros
/system/script/add dont-require-permissions=no name=mqttpublish owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#\
    \_Required packages: iot\r\
    \n\r\
    \n################################ Configuration #########################\
    #######\r\
    \n# Name of an existing MQTT broker that should be used for publishing\r\
    \n:local broker \"broker\"\r\
    \n\r\
    \n# MQTT topic where the message should be published\r\
    \n:local topic \"my/test/topic\"\r\
    \n\r\
    \n#################################### System ############################\
    #######\r\
    \n:put (\"[*] Gathering system info...\")\r\
    \n:local cpuLoad [/system/resource/get cpu-load]\r\
    \n:local freeMemory [/system/resource/get free-memory]\r\
    \n:local usedMemory ([/system/resource/get total-memory] - \$freeMemory)\r\
    \n:local rosVersion [/system/package/get value-name=version \\\r\
    \n\A0 \A0 [/system/package/find where name ~ \"^routeros\"]]\r\
    \n:local model [/system/routerboard/get value-name=model]\r\
    \n:local serialNumber [/system/routerboard/get value-name=serial-number]\r\
    \n:local upTime [/system/resource/get uptime]\r\
    \n\r\
    \n#################################### MQTT ##############################\
    #######\r\
    \n:local message \\\r\
    \n\A0 \A0 \"{\\\"model\\\":\\\"\$model\\\",\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"sn\\\":\\\"\$serialNumber\\\",\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"ros\\\":\\\"\$rosVersion\\\",\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"cpu\\\":\$cpuLoad,\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"umem\\\":\$usedMemory,\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"fmem\\\":\$freeMemory,\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"uptime\\\":\\\"\$upTime\\\"}\"\r\
    \n\r\
    \n:log info \"\$message\";\r\
    \n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
    \n:put (\"[*] Sending message to MQTT broker...\")\r\
    \n/iot/mqtt/publish broker=\$broker topic=\$topic message=\$message\r\
    \n:put (\"[*] Done\")"
```

該指令碼從 RouterOS 收集資料（型號名稱、序列號、RouterOS 版本、當前 CPU、已用記憶體、空閒記憶體和執行時間），並以 JSON 格式把訊息（資料）釋出到 broker：

```ros
/system/script/run mqttpublish
[*] Gathering system info...
[*] Total message size: 125 bytes
[*] Sending message to MQTT broker...

[*] Done
```

你可以訂閱該主題來檢視結果：

```ros
/iot/mqtt/subscriptions/recv/print
 0 broker=broker topic="my/test/topic" data="{"model":"RB924i-2nD-BT5&BG77","sn":"E9C80EAEXXXX","ros":"7.9","cpu":13,"umem":47476736,
     "fmem":19632128,"uptime":"02:21:18"}" 
   time=2023-05-22 17:03:52 
```

別忘了根據你的設定修改指令碼中的“Configuration”部分（主題和 broker）。
