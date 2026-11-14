---
sidebar_key: "internet-of-things/bluetooth/user-guides/mqtt-https-and-aws-configuration"
sidebar_position: 6
title: "MQTT/HTTPS 和 AWS 配置"
sidebar_label: "MQTT/HTTPS 和 AWS 配置"
description: "透過基於 HTTPS 的 MQTT 將 MikroTik Bluetooth 標籤資料轉發到 Amazon AWS，涵蓋 AWS 賬戶設定、證書和代理配置。"
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/bluetooth/user-guides/mqtt-https-and-aws-configuration
captured_at: '2026-11-04T11:18:58+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 簡介 {#introduction}

可用於監控藍牙標籤廣播資訊的選項之一是雲系統，例如 AWS（Amazon WEB Services）。本文將展示如何配置 AWS 和 RouterOS，以使用 MQTT 和 HTTPS 協定釋出資料。在此場景中，RouterOS 將充當閘道器，並將 BLEtag 廣播的資料釋出到雲（AWS）。在此場景中，AWS 將充當 MQTT broker 和 MQTT subscriber（用於釋出/顯示資料的伺服器）。

在繼續設定之前，您需要在 AWS 系統中建立賬戶。您可以訪問此[連結](https://repost.aws/knowledge-center/create-and-activate-aws-account)瞭解有關如何操作的更多資訊。

建立賬戶後，請確保支付卡在 **Your_Username>My account** 下透過驗證，否則賬戶將無法啟用。

轉到 **Services>Internet of Things>IoT Core**。

在 **Test** 部分，您可以使用內建的 MQTT 測試用戶端，以便測試釋出和訂閱主題。您有 **Subscribe to a topic** 和 **Publish to a topic** 標籤頁，可用於檢查這兩個過程。MQTT 測試用戶端部分還可以顯示 HTTPS 釋出內容。

### AWS IoT 配置 {#aws-iot-configuration}

:::info
本節所示的配置適用於 MQTT 釋出/訂閱場景，但您也可以使用相同的 AWS 設定測試 HTTPS 釋出。
:::

#### 事項 {#things}

步驟 1：轉到 **Manage>Things**。這是配置開始的選單（Things 選單表示裝置或邏輯實體）。

**

![](/img/e4b443fbae06aae6.webp)

**

按 **Create>Create a single thing>**選擇名稱**>Next>Create certificate.**

步驟 2：下載“AmazonRootCA1.pem”證書（AWS 的根 CA）、“xxxx.cert.pem”證書（用於“thing”的證書）和“xxxx.private.key”金鑰（私鑰）——“xxxx”部分對於每個新建立的證書都是唯一的。

![](/img/7b7c0c910ab10e9d.webp)

步驟 3：您可以選擇完成設定（透過選擇 **Done**），或者設定策略（透過選擇 **Attach a policy**）。您需要為建立的“thing”新增策略，但如果您使用新賬戶進行操作，可能沒有任何可供選擇的策略。不用擔心，您可以稍後手動建立它們。

還有兩個重要的選單——**Secure>Certificates** 和 **Secure>Policies**。

#### 證書 {#certificates}

在 **Certificates** 選單中，您可以建立證書、啟用證書並將其附加到策略。配置“Things”時應該已經建立了證書。只需確保證書已“啟用”。為此，選擇該證書，點選“**Actions**”，然後點選“**Activate**”。

![](/img/0ca286e97be93851.webp)

#### 策略 {#policies}

![](/img/61c2acd5a1f96b13.webp)

步驟 1：建立新策略。點選“**Create**”並輸入策略名稱。在“**Create a policy**”標籤頁中，您可以選擇設定“操作”。在本示例中，我們將使用 4 個操作（`iot:Publish`、`iot:Receive`、`iot:Subscribe` 和 `iot:Connect`）。您可以訪問此[連結](https://docs.aws.amazon.com/iot/latest/developerguide/example-iot-policies.html)瞭解有關策略及示例的更多資訊。

步驟 2：轉到“**Add statements**”部分。在“**Action**”欄位中，選擇 **iot:Publish** 和 **iot:Receive** 操作，並用逗號“,”分隔它們。在“**Resource ARN**”欄位中，將文字“`replaceWithATopic`”替換為實際相關的主題（例如“`my/test/topic`”）。在“**Effect**”複選框中勾選“**Allow**”。

![](/img/a0cdd99f9c91876a.webp)

步驟 3：透過點選“**Add statement**”新增新語句。透過選擇 **iot:Subscribe** 向語句新增操作，並將“**Resource ARN**”欄位中的文字“`replaceWithATopicFilter`”替換為實際相關的主題（例如“`my/test/topic`”）。在“**Effect**”複選框中勾選“**Allow**”。

![](/img/5c54b0d50ae0f057.webp)

步驟 4：新增最後一條語句並設定 **iot:Connect** 操作。僅將“`replaceWithAClientId`”部分更改為合適的 client-id（例如“`test-client`”），並勾選“**Allow**”複選框。要完成設定，請點選“**Create**”。

步驟 5：您需要將證書附加到新建立的策略。為此，請轉到 **Secure>Certificates**，選擇該證書，點選“**Actions**”和“**Attach policy**”。

![](/img/b72f51a124767122.webp)

選擇該策略並點選“**Attach**”。

![](/img/3585aca6bc3b85d9.webp)

至此，AWS 設定完成。

#### 端點地址（Broker 的地址） {#endpoint-address-brokers-address}

您可以在“**Settings**”部分（Settings>Device data endpoint）找到 **Endpoint** 地址。在 RouterOS 設定中，應將此地址配置為 broker 的 IP/FQDN 地址。

![](/img/c88cf0d50ff1a63b.webp)

### RouterOS 配置 {#routeros-configuration}

:::info
為了配置 MQTT，請確保事先已安裝 **iot** 軟體包。
:::
在我們的示例中，我們使用 [KNOT](https://mikrotik.com/product/knot) 作為閘道器，並使用一個（專為 KNOT 建立的）指令碼來發布資料。在你的具體應用場景中，你可以使用任何 RouterOS 裝置（已安裝 iot 軟體包）來發布你需要的任何資料。

#### 證書 {#certificates-1}

由於 AWS 使用 SSL 連線，我們需要之前下載的證書和金鑰。

轉到“Files”選單，並將 *AmazonRootCA1.pem*、*xxxx.cert.pem.crt* 和 *xxxx.private.pem.crt* 新增到“File list”。

![](/img/3d82fd90f15721b1.webp)

轉到 System>Certificates，並匯入全部 3 個檔案（透過 "Import" 按鈕——逐個匯入）：

![](/img/4cfb83ec34cf5d94.webp)

確保兩個證書都受信任（T），並且“xxxx.certificate.pem.crt”帶有私鑰（K）。

#### MQTT 代理 {#mqtt-broker}

轉到 IoT>MQTT 並新增新的 broker（“+”按鈕）。

![](/img/35928a714e886639.webp)

在“Name”欄位中為 broker 命名（例如 **AWS**）。

在“Address”欄位中輸入/貼上 AWS 地址（您可以在 AWS 設定“**Settings>Device data endpoint**”中找到它——**Endpoint address**）。

在“Port”欄位中配置 broker 使用的埠，並透過 SSL 複選框啟用 SSL（在此情況下，AWS 使用 **8883**，並且由於我們使用證書，因此需要**啟用 SSL**）。

“Username”和“Password”欄位在此場景中不是必需的（取決於 broker 的配置——跳過這兩個欄位）。

在“Client Id”欄位中設定 client-id（它是在 AWS 策略中配置的 ID——在本示例中為 **`test-client`**）。

由於使用了 SSL，必須在“Certificate”欄位中選擇證書（選擇 ***xxxx.certificate.pem.crt***）。

單擊 "Apply" 和 "OK" 完成 broker 設定。

#### 使用指令碼進行 MQTT 釋出 {#mqtt-publish-with-a-script}

為了將藍牙標籤（在本示例中為 TG-BT5-IN）的資料釋出到 AWS，我們將使用指令碼。指令碼示例如下所示。

每一行以符號 `#` 開頭的內容都是說明，它描述將在該行下方配置的引數。請修改引號 `\"\"` 內適用於你具體情況的引數。

```ros
## 所需软件包：iot

################################ Configuration ################################
## 用于发布的现有 MQTT broker 的名称
:local broker "AWS"

## 消息应发布到的 MQTT 主题
:local topic "my/test/topic"

## 应将其 MAC 用作 'Locator ID' 的接口
:local locatorIface "ether1"

## 用于过滤蓝牙广播地址的 POSIX 正则表达式。例如 "^BC:33:AC"
## 将只包含以这 3 个八位组开头的地址。
## 要禁用此过滤器，请将其设置为 ""
:local addressRegex ""

## 用于根据蓝牙广播数据过滤蓝牙广播的 POSIX 正则表达式。与
## 使用 'addressRegex' 时的用法相同。
:local advertisingDataRegex ""

## 信号强度过滤器。例如，-40 将只包括蓝牙广播
## 其信号强度强于 -40dBm。
## 要禁用此过滤器，请将其设置为 ""
:local rssiThreshold "-40"

#################################### System ###################################
:put ("[*] Gathering system info...")
:local ifaceMac [/interface get [/interface find name=$locatorIface] mac-address]
:local cpuLoad [/system resource get cpu-load]
:local freeMemory [/system resource get free-memory]
:local usedMemory ([/system resource get total-memory] - $freeMemory)
:local rosVersion [/system package get value-name=version \
    [/system package find where name ~ "^routeros"]]
:local model [/system routerboard get value-name=model]
:local serialNumber [/system routerboard get value-name=serial-number]
## 由于 ROS6 中的 '/system health' 没有 'find'，健康状态有点不太可靠
:local health [/system health print as-value]
:local supplyVoltage 0
:local boardTemp 0
:foreach entry in=$health do={
    :if ($entry->"name" = "voltage") do={:set $supplyVoltage ($entry->"value")}
    :if ($entry->"name" = "board-temperature1") do={:set $boardTemp ($entry->"value")}
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
    :local obj "\
        {\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"ts\":$ts,\
            \"rssi\":$rssi,\
            \"ed\":{\
                \"ad\":\"$ad\"\
            }\
        }"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $ts
    # Ensure that the last object is not terminated by a comma
    :set $advJson "$advJson$advSeparator$obj"
    :if ($advSeparator = "") do={
        :set $advSeparator ","
    }
}

:if ($advCount > 0) do={

    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp

}

:put ("[*] Found $advCount new advertisements \
    (processing time: $[([/system clock get time] - $btProcessingStart)])")

#################################### MQTT #####################################
:local message \
    "{\
        \"clientId\":\"$[/iot mqtt brokers get value-name=client-id \
            [/iot mqtt brokers find name=$broker]]\",\
        \"t\":0,\
        \"v\":1,\
        \"OldestAdvertisementTimestamp\":$btOldestAdvertisementTimestamp,\
        \"locs\":[{\
            \"id\":\"$[$minimizeMac address=$ifaceMac]\",\
            \"tags\":[$advJson],\
            \"ed\":{\
                \"model\":\"$model\",\
                \"sn\":\"$serialNumber\",\
                \"ros\":\"$rosVersion\",\
                \"cpu\":$cpuLoad,\
                \"umem\":$usedMemory,\
                \"fmem\":$freeMemory,\
                \"psu\":$supplyVoltage,\
                \"temp\":$boardTemp\
            }\
        }]\
    }"
:log info "$message";
:put ("[*] Total message size: $[:len $message] bytes")
:put ("[*] Sending message to MQTT broker...")
/iot mqtt publish broker=$broker topic=$topic message=$message
:put ("[*] Done")
```

應注意 2 行指令碼。

```
:local broker "AWS"
```

行，您需要在引號 `""` 中指定 broker 的名稱（在我們的示例中為 **AWS**）。

```
:local topic "my/test/topic"
```

行，您需要在引號 `""` 中指定正確的主題。主題在 AWS 策略中配置（在我們的示例中為 **my/test/topic**）。

指令碼配置的其餘部分取決於整體需求。指令碼中說明了配置了哪些確切引數用於釋出。

導航到 System>Scripts，在那裡新增一個新指令碼，並貼上上方所示的指令碼（例如將其命名為 script1）。

要執行指令碼，您可以使用命令列：

```
/system script run script1
```

#### 使用指令碼透過 HTTPS 釋出 {#https-post-with-a-script}

另一種可用於將資料從閘道器釋出到雲的協定是 HTTPS。這可以透過 [fetch 工具](../../../system-information-and-utilities/fetch.md)實現。在 RouterOS 7.1beta6 版本之前，fetch 沒有用於選擇用戶端證書進行身份驗證的選項（這意味著不支援使用用戶端證書進行 HTTPS 釋出），而在 7.1beta6 中添加了一項新功能，可啟用此設定/支援。使用 CURL 和 Python 的 HTTPS 釋出示例（以及其他有用資訊）顯示在 [AWS HTTPS 手冊](https://docs.aws.amazon.com/iot/latest/developerguide/http.html)中。

為了將藍牙標籤（在本示例中為 TG-BT5-IN）的資料釋出到 AWS，我們將使用指令碼。指令碼示例如下所示。

每一行以符號 `#` 開頭的內容都是說明，它描述將在該行下方配置的引數。請修改引號 `\"\"` 內適用於你具體情況的引數。

```ros
################################ Configuration ################################
## 应将其 MAC 用作 'Locator ID' 的接口
:local locatorIface "ether1"

## 用于过滤蓝牙广播地址的 POSIX 正则表达式。例如 "^BC:33:AC"
## 将只包含以这 3 个八位组开头的地址。
## 要禁用此过滤器，请将其设置为 ""
:local addressRegex ""

## 用于根据蓝牙广播数据过滤蓝牙广播的 POSIX 正则表达式。与
## 使用 'addressRegex' 时的用法相同。
:local advertisingDataRegex ""

## 信号强度过滤器。例如，-40 将只包括蓝牙广播
## 其信号强度强于 -40dBm。
## 要禁用此过滤器，请将其设置为 ""
:local rssiThreshold "-40"

#################################### System ###################################
:put ("[*] Gathering system info...")
:local ifaceMac [/interface get [/interface find name=$locatorIface] mac-address]
:local cpuLoad [/system resource get cpu-load]
:local freeMemory [/system resource get free-memory]
:local usedMemory ([/system resource get total-memory] - $freeMemory)
:local rosVersion [/system package get value-name=version \
    [/system package find where name ~ "^routeros"]]
:local model [/system routerboard get value-name=model]
:local serialNumber [/system routerboard get value-name=serial-number]
## 由于 ROS6 中的 '/system health' 没有 'find'，健康状态有点不太可靠
:local health [/system health print as-value]
:local supplyVoltage 0
:local boardTemp 0
:foreach entry in=$health do={
    :if ($entry->"name" = "voltage") do={:set $supplyVoltage ($entry->"value")}
    :if ($entry->"name" = "board-temperature1") do={:set $boardTemp ($entry->"value")}
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
    :local obj "\
        {\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"ts\":$ts,\
            \"rssi\":$rssi,\
            \"ed\":{\
                \"ad\":\"$ad\"\
            }\
        }"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $ts
    # Ensure that the last object is not terminated by a comma
    :set $advJson "$advJson$advSeparator$obj"
    :if ($advSeparator = "") do={
        :set $advSeparator ","
    }
}

:if ($advCount > 0) do={

    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp

}

:put ("[*] Found $advCount new advertisements \
    (processing time: $[([/system clock get time] - $btProcessingStart)])")

#################################### MQTT #####################################
:local message \
    "{\
        \"t\":0,\
        \"v\":1,\
        \"OldestAdvertisementTimestamp\":$btOldestAdvertisementTimestamp,\
        \"locs\":[{\
            \"id\":\"$[$minimizeMac address=$ifaceMac]\",\
            \"tags\":[$advJson],\
            \"ed\":{\
                \"model\":\"$model\",\
                \"sn\":\"$serialNumber\",\
                \"ros\":\"$rosVersion\",\
                \"cpu\":$cpuLoad,\
                \"umem\":$usedMemory,\
                \"fmem\":$freeMemory,\
                \"psu\":$supplyVoltage,\
                \"temp\":$boardTemp\
            }\
        }]\
    }"
:log info "$message";
:put ("[*] Total message size: $[:len $message] bytes")
/tool fetch certificate=f79dda4ec5-certificate.pem.crt.txt_0 http-method=post output=user http-header-field="Content-Type:application/json" http-data=$message url="https://xxxxx.iot.us-east-2.amazonaws.com:8443/topics/my/test/topic"

:put ("[*] Done")
```

有 1 行指令碼需要特別注意：

```
/tool fetch certificate=f79dda4ec5-certificate.pem.crt.txt_0 http-method=post output=user http-header-field="Content-Type:application/json" http-data=$message url="https://xxxxxx.iot.us-east-2.amazonaws.com:8443/topics/my/test/topic"
```

請根據您的具體情況更改證書名稱和 URL：

`url="https://xxxx:8443/topics/yyyy"`，其中“xxxx”是 AWS 端點地址，“yyyy”是在 AWS 策略中配置的主題——步驟 2 和 3（在本示例中為 my/test/topic）。

指令碼配置的其餘部分取決於整體需求。指令碼中說明了配置了哪些確切引數用於釋出。

轉到 System>Scripts，在其中新增新指令碼，並貼上上面顯示的指令碼（例如將其命名為 script2）。

要執行指令碼，您可以使用命令列：

`/system script run script2`

### 驗證 {#verification}

要驗證 AWS 是否收到資料，請返回 AWS 門戶。轉到 **Test** 頁面。使用 **Subscribe to a topic** 選項。在 **Topic filter** 欄位中輸入在 AWS 策略中配置的主題（在本示例中為 **my/test/topic**），然後按 **Subscribe**。在下方，您應該會看到 **Subscriptions** 部分，資料將顯示在其中。執行指令碼（在 RouterOS 中），您應該會在“**Subscriptions**”標籤頁中看到收集的資料。

![](/img/6aa5a7ba0bbb2709.webp)

同一頁面/標籤頁也應顯示透過 HTTPS 釋出的封包。
