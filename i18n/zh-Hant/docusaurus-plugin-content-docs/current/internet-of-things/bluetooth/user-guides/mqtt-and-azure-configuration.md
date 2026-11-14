---
sidebar_key: "internet-of-things/bluetooth/user-guides/mqtt-and-azure-configuration"
sidebar_position: 5
title: "MQTT 和 Azure 配置"
sidebar_label: "MQTT 和 Azure 配置"
description: "將 MikroTik MQTT 資料釋出到 Microsoft Azure IoT，涵蓋 Azure 賬戶設定、裝置憑據和 MQTT broker 配置。"
source: https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/mqtt-and-azure-configuration
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 簡介 {#introduction}

你可以用來監控 MQTT 釋出者所傳送資訊的眾多雲服務之一，是 Microsoft [Azure](https://azure.microsoft.com/en-us)。本文將演示如何同時配置 Azure 和 RouterOS，以使用 MQTT 協定釋出資料。在此場景中，RouterOS 將充當閘道器，並把 BLEtag 廣播的資料釋出到雲（Azure）。在此場景中，Azure 將充當 MQTT broker 和 MQTT 訂閱者（用於釋出/顯示資料的伺服器）。

在繼續設定之前，你需要在 Azure 系統中建立一個賬戶。你可以透過這個[連結](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account?icid=azurefreeaccount)找到有關如何操作的更多資訊。

Azure 提供許多不同的選項和服務，其中許多選項/服務都有價目表。你可以透過這個[連結](https://www.azure.cn/en-us/pricing/)找到有關定價的更多資訊。

### Azure 配置 {#azure-configuration}

完成訂閱設定後（Azure Portal>All Services>Subscriptions），你將需要配置資源組、IoT Hub、證書和裝置。

#### 資源組 {#resource-group}

轉到 All Services>Resource groups 並建立一個。

![](/img/49ca1fcea673b94e.png)

將你的 IoT Hub 關聯到之前建立的資源組。不要忘記檢查/設定 "Networking"（網路連線）和 Management（[訂閱層級](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-scaling)）標籤頁。

你可以透過[此處](https://learn.microsoft.com/en-us/azure/iot-hub/iot-concepts-and-iot-hub)找到更多資訊。

#### IoT Hub {#iot-hub}

導航到 All services>IoT Hub 並建立一個。

![](/img/488293d4d2aa6e3b.png)

將你的 IoT Hub 連結到之前建立的資源組。不要忘記檢查/設定 "Networking"（網路連線）和 Management（訂閱層級）標籤頁。

你可以在這裡瞭解更多資訊。

#### 證書 {#certificates}

在本示例中，我們將重點介紹 [X.509 CA-signed](https://learn.microsoft.com/en-us/azure/iot-edge/how-to-authenticate-downstream-device?view=iotedge-2020-11#x509-ca-signed-authentication) 身份驗證。

你可以使用 [Microsoft 提供的指令碼](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows))或 [open SSL](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows) 生成測試證書。

生成 RootCA 後，轉到 IoT Hub>Certificates 並在那裡新增證書：

![](/img/4e87fb5da7e31a84.webp)

成功新增 RootCA 後，你需要[證明所有權](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows)（驗證它）。

如果你使用指令碼，[教程（步驟 3）](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-3---prove-possession)中有詳細描述和展示；如果你使用 open ssl，則請參閱[教程（步驟 7）](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-7---demonstrate-proof-of-possession)。

證書成功驗證後，你需要建立[裝置證書](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-4---create-a-new-device)（如果你使用 open ssl，請遵循此[連結](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-8---create-a-device-in-your-iot-hub)）。

#### 裝置 {#devices}

導航到你的 IoT Hub>IoT Devices 並新增一個新裝置：

![](/img/da21843851a2de33.webp)

請注意 "Device ID" 欄位。Device ID 應與裝置證書的 "Common name" 匹配。

選擇 `Authentication type=X.509 CA Signed` 並儲存設定。

現在你可以生成所需最後一項證書——[裝置證書](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-4---create-a-new-device)（如果你使用 open ssl，請遵循此[連結](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-8---create-a-device-in-your-iot-hub)）。

至此，Azure 部分的配置就完成了。

### RouterOS 配置 {#routeros-configuration}

:::info
為了配置 MQTT，請確保事先已安裝 **iot** 軟體包。
:::
在我們的示例中，我們使用 [KNOT](https://mikrotik.com/product/knot) 作為閘道器，並使用一個（專為 KNOT 建立的）指令碼來發布資料。在你的具體應用場景中，你可以使用任何 RouterOS 裝置（已安裝 iot 軟體包）來發布你需要的任何資料。

#### 證書 {#certificates-1}

由於我們使用 SSL 連線，因此需要之前生成的裝置證書及其私鑰。我們還將使用 [Baltimore CyberTrust Root 證書](https://learn.microsoft.com/en-us/azure/security/fundamentals/azure-certificate-authority-details?tabs=root-and-subordinate-cas-list)。

轉到 "Files" 選單，並在那裡新增以下證書——*Baltimore CyberTrust Root 證書、之前生成的裝置證書及其私鑰*。

![](/img/436f4a58da3dbccc.webp)

轉到 System>Certificates，並匯入全部 3 個檔案（透過 "Import" 按鈕——逐個匯入）：

![](/img/7063592cc6f64e86.webp)

:::info
*請再次確認 "Common Name" 與 Azure 門戶中為該裝置配置的 Device ID 相匹配。在我們的示例中，Device ID 為 "testor"，並且與 "Common Name" 欄位匹配。*
:::
確保兩個證書均已受信任（T），並且私鑰（K）已新增到裝置證書中。

#### MQTT 代理 {#mqtt-broker}

轉到 IoT>MQTT 並新增新的 broker（"+" 按鈕）：

![](/img/49a6543b8655b546.webp)

- 在 "Name" 欄位中為 broker 命名（例如，**Azure**）。
- 在 "Address" 欄位中輸入/貼上 Azure 主機名地址（你可以在 IoT Hub>Overview 選單中找到該主機名）：

![](/img/f1970f1b2c9d830e.webp)

- 在 "Port" 欄位中配置 broker 使用的埠，並透過 SSL 複選框啟用 SSL（在本例中，Azure 使用 **8883**，並且由於我們使用證書，因此需要**啟用 SSL**）。
- "Username" 欄位應按以下方式配置——`{iothubhostname}/{device_id}/?api-version=2018-06-30`，其中 `{iothubhostname}` 是你的 IoT Hub 的主機名，`{device_id}` 是在 Azure 門戶中設定的 Device ID（與證書的 "Common Name" 相同，在我們的示例中為 "testor"）。
- 此場景中不需要 "Password" 欄位（此配置取決於 broker 的設定——跳過此欄位）。
- "Client Id" 應與裝置的 ID 相同（在我們的示例中為 **testor**）。
- 由於使用了 SSL，必須在 "Certificate" 欄位中選擇證書（選擇裝置證書）。

你可以透過[此處](https://learn.microsoft.com/en-us/azure/iot-hub/iot-mqtt-connect-to-iot-hub#using-the-mqtt-protocol-directly-as-a-device)瞭解有關所需設定的更多資訊。

單擊 "Apply" 和 "OK" 完成 broker 設定。

#### 使用指令碼進行 MQTT 釋出 {#mqtt-publish-with-a-script}

為了將藍牙標籤（在我們的示例中為 TG-BT5-IN）中的資料釋出到 Azure，我們將使用指令碼。指令碼示例如下所示。

每一行以符號 `#` 開頭的文字都是說明性內容，它描述將在該行下方配置的引數。請修改引號 `""` 內適用於你具體情況的引數。

```ros
## 所需软件包：iot

################################ Configuration ################################
## 用于发布的现有 MQTT broker 的名称
:local broker "Azure"

## 消息应发布到的 MQTT 主题
:local topic "devices/testor/messages/events/"

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

:set $btOldestAdvertisementTimestamp $lastAdvTimestamp
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

應考慮 2 行指令碼：

```
:local broker "Azure"
```

這一行，你應在引號 `""` 內指定 broker 的名稱（在我們的示例中為 **Azure**）。

```
:local topic "devices/testor/messages/events/"
```

這一行，你應在引號 `""` 內指定正確的 topic。Azure 預設使用 topic `devices/{device_id}/messages/events/` 進行釋出（如[此處](https://learn.microsoft.com/en-us/azure/iot-hub/iot-mqtt-connect-to-iot-hub#for-azure-iot-tools)的手冊所述）。不要忘記將 `{device_id}` 部分更改為你在 Azure 門戶中配置的 "Device ID"。

指令碼配置的其餘部分取決於整體需求。指令碼中說明了配置了哪些確切引數用於釋出。

導航到 System>Scripts，在那裡新增一個新指令碼，並貼上上方所示的指令碼（例如將其命名為 script1）。

要執行指令碼，您可以使用命令列：

```
/system script run script1
```

### 驗證 {#verification}

在 Azure 門戶上檢視接收/釋出的訊息有很多不同的方法。請檢視 Azure 教程瞭解你可用的選項。

在我們的示例中，我們將使用 [Visual Studio Code 程式](https://code.visualstudio.com/)驗證結果。

下載該程式並將其連線到你的 [IoT Hub](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-toolkit)。

新增 IoT Hub 後，你就可以開始監控端點：

![](/img/da76f9f1ace22e06.webp)

並且你可以在 "OUTPUT" 部分檢視已釋出的訊息，如下圖所示：

![](/img/a5d4b0d6ff3c1a13.webp)
