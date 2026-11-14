---
sidebar_key: "internet-of-things/bluetooth/user-guides/https-post-and-azure-configuration"
sidebar_position: 3
title: "HTTPS post 與 Azure 配置"
sidebar_label: "HTTPS post 與 Azure 配置"
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/bluetooth/user-guides/https-post-and-azure-configuration
captured_at: '2026-11-04T11:18:15+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 簡介 {#introduction}

本文將演示如何配置 [Azure](https://azure.microsoft.com/en-us) 和 RouterOS，以使用 HTTPS 協定釋出資料。在此場景中，RouterOS 將充當閘道器，並把 BLEtag 廣播的資料釋出到雲端（Azure）。

在繼續設定之前，你需要在 Azure 系統中建立一個賬戶。你可以透過這個[連結](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account?icid=azurefreeaccount)找到有關如何操作的更多資訊。

Azure 提供許多不同的選項和服務，其中許多選項/服務都有價目表。你可以透過這個[連結](https://www.azure.cn/en-us/pricing/)找到有關定價的更多資訊。

### Azure 配置 {#azure-configuration}

完成訂閱設定後（Azure Portal>All Services>Subscriptions），你需要配置資源組、IoT Hub、裝置，並生成 SAS 令牌。

#### 資源組 {#resource-group}

轉到 All Services>Resource groups 並建立一個。

![](/img/49ca1fcea673b94e.png)

你可以透過這個[連結](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal)找到更詳細的指南。

成功配置資源組後，你需要建立一個 IoT Hub。

#### IoT Hub {#iot-hub}

導航到 All services>IoT Hub 並建立一個。

![](/img/488293d4d2aa6e3b.png)

將你的 IoT Hub 關聯到之前建立的資源組。不要忘記檢查/設定 "Networking"（網路連線）和 Management（[訂閱層級](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-scaling)）標籤頁。

你可以透過[此處](https://learn.microsoft.com/en-us/azure/iot-hub/iot-concepts-and-iot-hub)找到更多資訊。

#### 裝置 {#devices}

導航到你的 IoT Hub>IoT Devices 並新增一個新裝置：

![](/img/ff71dfe858dcad62.webp)

選擇 `Authentication type=Symmetric Key` 並儲存設定。

#### SAS 令牌 {#sas-token}

在我們的示例中，我們將使用 [Visual Studio Code](https://code.visualstudio.com/) 程式來生成 [SAS 令牌](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)。

只需下載該程式並將其連線到你的 [IoT Hub](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-toolkit)。

完成後，當之前配置的裝置名稱出現在你的 IoT HUB 中時，右鍵單擊該裝置名稱，並按下方截圖所示生成令牌：

![](/img/bfcfb4024079eae8.webp)

系統會要求你輸入令牌的過期時間（以小時為單位），並按 "enter" 確認設定。

完成此步驟後，令牌應生成在 "OUTPUT" 欄位中：

![](/img/fca492d6f6a82ace.webp)

複製該令牌，因為稍後將在我們的 HTTPS 釋出指令碼中使用它。

至此，Azure 部分的配置就完成了。

### RouterOS 配置 {#routeros-configuration}

在本指南中，我們使用 [KNOT](https://mikrotik.com/product/knot) 作為閘道器，並使用一個（專為 KNOT 建立的）指令碼釋出資料。在你的具體應用場景中，你可以使用任何 RouterOS 裝置來發布你需要的任何資料。

#### 使用指令碼透過 HTTPS 釋出 {#https-post-with-a-script}

HTTPS 釋出可以使用 [fetch 工具](../../../system-information-and-utilities/fetch.md)來實現。為了把來自 Bluetooth 標籤（在我們的示例中為 TG-BT5-XX）的資料釋出到 Azure，我們將使用該指令碼。指令碼示例如下所示。

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

#################################### message #####################################
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
/tool fetch http-method=post output=user http-header-field="authorization:{sas_token}" http-data=$message url="https://{iot_hub_name}.azure-devices.net/devices/{device_id}/messages/events\?api-version=2020-03-13"

:put ("[*] Done")
```

有 1 行指令碼需要特別注意：

```ros
/tool fetch http-method=post output=user http-header-field="authorization:{sas_token}" http-data=$message url="https://{iot_hub_name}.azure-devices.net/devices/{device_id}/messages/events\?api-version=2020-03-13"
```

將 HTTP 頭中的 `{sas_token}` 更改為在 SAS 令牌部分生成的令牌。

將 URL 中的 `{iot_hub_name}` 和 `{device_id}` 更改為在 Azure 門戶中配置的實際 IoT Hub 名稱和 Device ID。

指令碼配置的其餘部分取決於整體需求。指令碼中說明了配置了哪些確切引數用於釋出。

導航到 System>Scripts，在那裡新增一個新指令碼，並貼上上方所示的指令碼（例如將其命名為 script1）。

要執行指令碼，您可以使用命令列：

```ros
/system script run script1
```

### 驗證 {#verification}

在 Azure 門戶上檢視接收/釋出的訊息有很多不同的方法。請檢視 Azure 教程瞭解你可用的選項。

我們將使用 [Visual Studio Code](https://code.visualstudio.com/) 程式來驗證結果。

開啟你的 IoT Hub 並開始監控終結點（裝置）：

![](/img/da7967098f77735b.webp)

你可以按下圖所示在 "OUTPUT" 部分檢視已釋出的訊息。只需執行指令碼並檢查接收到的訊息：

![](/img/9f41852699b32df6.webp)
