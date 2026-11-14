---
sidebar_key: "internet-of-things/bluetooth/user-guides/bluetooth-tag-tracking-mqtt-thingsboard"
sidebar_position: 1
title: "使用 MQTT 和 ThingsBoard 進行藍牙標籤追蹤"
sidebar_label: "使用 MQTT 和 ThingsBoard 進行藍牙標籤追蹤"
description: "本頁介紹使用 MikroTik RouterOS 結合 MQTT 和 ThingsBoard 進行藍牙標籤跟蹤，詳細說明 KNOT 裝置如何捕獲藍牙廣播封包、將其處理為 MQTT 訊息，並在 ThingsBoard 中視覺化，以跟蹤資產在多個區域間的移動。"
tags:
  - 'bluetooth'
  - 'mqtt'
  - 'thingsboard'
source: https://manual.mikrotik.com/docs/7.24/internet-of-things/bluetooth/user-guides/bluetooth-tag-tracking-mqtt-thingsboard
captured_at: '2026-11-04T11:34:43+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS 中的 Bluetooth 介面實現允許裝置捕獲透過 37、38 和 39 廣播通道廣播的 Bluetooth 廣播封包。更多資訊請參見[此處指南](../index.md)。

Bluetooth 標籤，例如 [TG-BT5-IN](https://mikrotik.com/product/tg_bt5_in) 和 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out)，正是這樣做的。它們透過上述通道廣播廣播負載。要了解負載中儲存了哪些型別的資訊，請務必檢視[連結](https://help.mikrotik.com/docs/display/UM/MikroTik+Tag+advertisement+formats#heading-MikroTikPDUPayloadstructure)。可以使用 [MikroTik Beacon Manager](https://help.mikrotik.com/docs/display/UM/MikroTik+Beacon+Manager) 應用配置這些標籤，使其按間隔和/或在檢測到移動、傾斜或自由落體觸發時自動廣播負載。簡單來說，標籤會定期向周圍所有 Bluetooth 掃描器（例如 [KNOT](https://mikrotik.com/product/knot)）“告知”（廣播）有關自身的資訊。

當標籤廣播負載，並且標籤位於 KNOT 的 Bluetooth 工作範圍內時，KNOT 將捕獲該負載，並在其 "scanner" Bluetooth 介面部分下顯示。如下所示：

```ros
/iot/bluetooth/scanners/advertisements/print
Columns: DEVICE, PDU-TYPE, TIME, ADDRESS-TYPE, ADDRESS, RSSI, LENGTH, DATA
#  DEVICE  PDU-TYPE        TIME                  ADDRESS-TYPE  ADDRESS            RSSI    LENGTH  DATA                                        
0  bt1     adv-noconn-ind  2023-03-07 12:11:57  public        DC:2C:6E:0F:C0:3D  -51dBm      22  15ff4f09010079100000ffff0000cf188a6b2b000064
1  bt1     adv-noconn-ind  2023-03-07 12:11:58  public        2C:C8:1B:4B:BB:0A  -49dBm      22  15ff4f090100168dfefffffffeffa51ae1362200005e 
```

上面的示例表明，KNOT 在其工作範圍內看到兩個 Bluetooth 標籤，MAC 地址分別為 "DC:2C:6E:0F:C0:3D" 和 "2C:C8:1B:4B:BB:0A"，以及它們各自的負載（"DATA" 欄位）和訊號強度（"RSSI" 欄位）。

:::info
在本地測試 KNOT 能處理多少負載時，我們取得了以下結果 → 在 300 個標籤（處於出廠設定）分散在 KNOT 周圍，並使用 Bluetooth 過濾器 "keep-newest"（它會用最新負載覆蓋每個唯一 MAC 地址之前收到的負載，因此 Bluetooth 列表在任何時候都會為每個唯一標籤 MAC 地址顯示 1 個負載）的情況下，所有 300 個 MAC 地址在 30-40 秒後出現在 KNOT 的範圍內。這裡需要記住，所有 300 個標籤同時在同一通道上廣播會造成干擾（接收延遲）。當我們“清空”Bluetooth 負載列表時，列表每秒新增 20 個條目，大約 ~15 秒後，列表中有 250-290 個負載。然後再過 ~15 秒，列表顯示了所有 300 個唯一標籤負載。**你的 KNOT 實際能夠處理的標籤數量在很大程度上取決於環境，因此最好在現場進行測試。**
:::

藉助 RouterOS [指令碼](../../../developer-guides/scripting/index.md) 和[排程](../../../system-information-and-utilities/scheduler.md)，我們可以讓 KNOT 自動定期掃描負載列表；如果列表中找到了特定負載或特定標籤的 MAC 地址，我們就可以讓 KNOT 構造一條 MQTT 訊息（根據上面示例中顯示的列印資訊），並透過 [MQTT](../../mqtt/index.md)、[電子郵件](../../../system-information-and-utilities/e-mail.md) 或 [HTTP](../../../system-information-and-utilities/fetch.md) POST 將其傳送到已配置的伺服器。指令碼示例將在本指南後面展示。

正如標題所示，目標是實現一個 **Bluetooth 標籤跟蹤解決方案**，思路非常簡單。**當你有 2 個 KNOT**（KNOT-A 和 KNOT-B），在排程器上執行相同的指令碼，**並且標籤在它們的 Bluetooth 工作範圍之間移動時**，**伺服器上的資料將指示**是 **KNOT-A 還是 KNOT-B** **傳送了**該標籤的**負載**。這將幫助你判斷標籤的遠近，即標籤是在 KNOT-A 區域還是 KNOT-B 區域廣播負載。

你將需要一臺用於儲存和視覺化資料的伺服器。在本指南中，我們將展示一個名為 [ThingsBoard](https://thingsboard.io/) 的平臺，以及如何使用 MQTT 協定與其通訊。

ThingsBoard 有云解決方案和不同的本地安裝選項（適用於不同作業系統）。由於我們添加了 [container](../../../containers/index.md) 功能，現在也可以在 RouterOS 內執行該平臺。為此，你需要一臺 RouterOS 裝置，至少有 2 GB 可用 RAM，或者在最小負載下有 1 GB 可用 RAM，具備增加儲存的選項（例如額外的 USB 埠），並且是 ARM64 或 AMD64 架構。可以考慮使用 [CHR](../../../getting-started/routeros-licensing/chr/index.md) 機器，它可能很合適。

### 設定要求 {#setup-requirements}

- 一臺正在執行的 ThingsBoard 伺服器。
- 2 臺以上 [KNOT](https://mikrotik.com/product/knot)，可透過乙太網、Wi-Fi 或蜂窩連線訪問伺服器網路（所需單元數量取決於需要覆蓋的區域大小）。
- 1 個以上 Bluetooth [TG-BT5-IN](https://mikrotik.com/product/tg_bt5_in) 和/或 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out) 標籤（取決於你需要跟蹤多少資產——每個資產 1 個標籤）。

## 場景說明 {#scenario-explanation}

讓我們先看一個基本示例。我們有 2 個 KNOT（KNOT-A 和 KNOT-B）。我們在自己的環境中測試了 Bluetooth 範圍，並確認兩個 KNOT 都能在 70 米距離捕獲標籤。如果我們將 KNOT-A 和 KNOT-B 安裝在相距 140 米的位置，它們的 Bluetooth 範圍將不會重疊，或只會輕微重疊。當標籤移動到 KNOT-A 範圍內 → 被監控標籤的負載將出現在 Bluetooth 掃描器列表中 → 指令碼將按設定的計劃啟動 → 帶有報告的 MQTT 訊息將傳送到伺服器 → 最後，伺服器將顯示標籤位於 KNOT-A 區域。當標籤移動到 KNOT-B 範圍內時，同樣的事情會發生，伺服器將顯示標籤位於 KNOT-B 區域內。

實際的 Bluetooth 工作距離會因現場而異，因為許多不同因素都會影響它，例如 2.4 GHz 干擾或所用周圍材料。例如，在無干擾的視距條件下，KNOT 能夠捕獲標籤廣播負載的距離可達 180 米（KNOT — ~180 米 — TG-BT5-OUT）。但你也必須記住，距離越遠，途中丟失的封包就越多。在辦公環境中，範圍可能降至 30-100 米。

從邏輯上講，如果 Bluetooth 工作範圍重疊，並且標籤位於重疊區域內（同時處於 KNOT-A 和 KNOT-B 的 Bluetooth 範圍內），兩個 KNOT 都會發送資料，伺服器將顯示標籤同時被兩個裝置報告。

**當然，會出現兩個或多個 KNOT 的 Bluetooth 範圍重疊的區域，你可以利用這一點**。基本上，你將獲得資訊：標籤當前位於特定 KNOT 區域之間 Bluetooth 範圍的邊緣。換句話說，當資產移動到重疊區域時，伺服器上的資訊會顯示該資產位於兩個 KNOT 工作範圍之間的某個位置，這是有用的資訊，**因為它提供了更高的精度**。

此外，**可以使用 [Tx power](https://help.mikrotik.com/docs/display/UM/MikroTik+Beacon+Manager+for+Android+devices#heading-TxPower) 引數降低標籤的輸出功率**。這意味著，即使標籤的負載廣播得太遠，並被其他本不應看到這些負載的 KNOT 捕獲（在更遠距離）→ 你也可以降低標籤的輸出功率，這會縮短 KNOT 能夠捕獲它們的距離。這樣，你就可以“調整”接收“範圍”，並避免“干擾”其他區域的訊號。

我們準備的指令碼還允許你設定一個過濾器（稍後會展示），該過濾器會讓 KNOT 忽略掃描器捕獲的負載，除非訊號強度（RSSI）強於指定值。在上面“[簡介](../index.md)”部分下顯示的 Bluetooth 掃描器示例列印中，我們可以看到 KNOT 看到其中一個標籤的 **RSSI** 訊號強度為 **-51 dBm**（MAC 地址為 "**DC:2C:6E:0F:C0:3D**" 的標籤），另一個標籤的 **RSSI** 訊號強度為 **-49 dBm**（MAC 地址為 "**2C:C8:1B:4B:BB:0A**" 的標籤）。因此，**如果我們**在指令碼中應用過濾器，**忽略**所有接收到的訊號強度（**RSSI**）**弱於 -50 dBm** 的負載，那麼我們的 **KNOT 將報告只有標籤 "2C:C8:1B:4B:BB:0A" 位於 Bluetooth 範圍內**，因為它的 RSSI 為 -49 dBm，而第二個標籤（RSSI 為 -51 dBm）將被忽略。本質上，這意味著第二種“調整”接收“範圍”的方法。實際訊號強度會因不同位置而異（如前所述，因為干擾和周圍材料），因此需要在現場進行測試。

### 示例 #1 {#example-1}

下面拓撲圖展示了其中一個用例：

![](/img/8fc762841be8f171.webp)

:::note
物件和 Bluetooth 工作範圍的比例僅作為示例展示，以幫助直觀理解和想象該拓撲！
:::

我們有一個倉庫區域，**我們有 3 個資產**（系統匣）需要跟蹤。**我們**還**有 3 個區域**：區域 **A**，用於存放新到達的系統匣；區域 **B**，我們的資產被轉移到那裡進行檢查；區域 **C**，資產在檢查後被移動到那裡。要實現 Bluetooth 資產跟蹤，只需每個區域安裝 1 臺 KNOT，每個資產安裝 1 個標籤。

如果 TAG 1 和 TAG 2（系統匣）到達“到達”區域 A，KNOT A 將向伺服器報告這兩個資產都在其 Bluetooth 範圍內。如果 TAG 3 被移動到區域 C，伺服器將指示它位於 KNOT C 範圍內。如果 TAG 1 和 TAG 2 向 B 區域移動，並停留在 A 和 B 區域之間的邊緣，伺服器將顯示它們處於重疊區域（同時處於 KNOT-A 和 KNOT-B 範圍內）。如果標籤移動到倉庫中間，伺服器將指示它們同時在所有 3 個區域內，即重疊區域。

#### 配置 {#configuration}

在本示例中，我們將展示一個基本拓撲：使用兩個 KNOT，我們只想知道標籤位於建築物的一部分還是另一部分（是位於區域 A 還是區域 B）。

##### ThingsBoard 準備 {#thingsboard-preparation}

檢視[此處](../../mqtt/mqtt-and-thingsboard-configuration.md)的指南，瞭解如何設定 ThingsBoard 和 RouterOS 以使用 MQTT 通訊。

:::tip
為簡單起見，本示例將展示 [access-token](../../mqtt/mqtt-and-thingsboard-configuration.md#access-token-scenario-1) 場景，但你也可以使用其他可用選項。對於生產環境，建議使用 SSL-MQTT，因為 non-SSL-MQTT 很容易被封包捕獲和檢查。

要了解如何在透過 [container](../../../containers/index.md) 執行的例項上實現 SSL-MQTT 通訊，請檢視[此處](../../../containers/user-guides/container-thingsboard-mqtt-http-server.md)連結的指南（[啟用 HTTPS 和 SSL MQTT](../../../containers/user-guides/container-thingsboard-mqtt-http-server.md#enabling-https-and-ssl-mqtt) 部分）。
:::

在 ThingsBoard GUI 中建立 2 個 KNOT，並將它們設為“閘道器”。

轉到“裝置”部分，點選“+”按鈕，然後點選“新增新裝置”：

![](/img/c96c5c3c49271e3d.webp)

為裝置命名並勾選“是閘道器”選項：

![](/img/68362bb2332cc62f.webp)

對你擁有的每個 KNOT 都執行此操作：

![](/img/332956b1a98eb64b.webp)

在你剛建立的裝置下，在“管理憑據”標籤頁中，為每個 KNOT 設定唯一的訪問令牌（唯一憑據）：

![](/img/0dfde7520370c11b.webp)

##### RouterOS 配置 {#routeros-configuration}

###### 準備工作 {#preparation}

在繼續之前，我們需要確認我們的 Bluetooth 標籤確實出現在 KNOT 的 Bluetooth 範圍內，並且 KNOT 能檢測到它。為此，你可以執行命令 `/iot/bluetooth/scanners/advertisements/print`：

```ros
/iot/bluetooth/scanners/advertisements/print
 # DEVICE     PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA                                           
 0 bt1        adv-noconn-ind  2023-03-08 12:35:15 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100b0110100ffff00000019d68d2300005d   
 1 bt1        adv-noconn-ind  2023-03-08 12:35:16 public       DC:2C:6E:0F:C0:3D        -39dBm         22 15ff4f0901008f3cfcfffbfffaff301783c22c000064   
 2 bt1        adv-noconn-ind  2023-03-08 12:35:35 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f09010084d500000400ffff0319ea8d2300005d   
 3 bt1        adv-noconn-ind  2023-03-08 12:35:45 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100e607faffffff03000319f48d2300005d   
```

或者你可以在 IoT>Bluetooth>Advertising reports 標籤頁下使用 [Webfig](../../../management-tools/webfig.md) 或 [Winbox](../../../management-tools/winbox.md) 檢查。

該列表可能很雜亂。由於掃描器會捕獲周圍的一切，隨機負載可能會出現在列表中。為幫助減少列表內容，你可以使用標籤的 MAC 地址 `/iot/bluetooth/scanners/advertisements/print where address=DC:2C:6E:0F:C0:3D` 對其進行過濾：

```ros
/iot/bluetooth/scanners/advertisements/print where address=DC:2C:6E:0F:C0:3D
 # DEVICE    PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA                                           
 0 bt1       adv-noconn-ind  2023-03-08 12:41:06 public       DC:2C:6E:0F:C0:3D        -49dBm         22 15ff4f0901005ab20100fdfffdff4017e1c32c000064   
 1 bt1       adv-noconn-ind  2023-03-08 12:41:26 public       DC:2C:6E:0F:C0:3D        -40dBm         22 15ff4f090100349704000000fcff4017f5c32c000064   
 2 bt1       adv-noconn-ind  2023-03-08 12:41:36 public       DC:2C:6E:0F:C0:3D        -49dBm         22 15ff4f09010073fb0000000000003017ffc32c000064   
 3 bt1       adv-noconn-ind  2023-03-08 12:41:46 public       DC:2C:6E:0F:C0:3D        -43dBm         22 15ff4f090100b88cffffffffffff401709c42c000064   
```

要了解如何解析負載，請檢視[此處](https://help.mikrotik.com/docs/display/UM/MikroTik+Tag+advertisement+formats#heading-Scriptfordecoding)的指南。

###### MQTT 代理 {#mqtt-broker}

在每個 KNOT 上設定一個 MQTT broker。

對於 KNOT A：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=1883 username=knot-A_access_token
```

其中：

- `name` 是你希望給 broker 指定的名稱，此名稱將在後面的指令碼中使用。
- `address` 是 broker/ThingsBoard 伺服器的 IP 地址。
- `port` 是 broker 監聽的 TCP 埠 → 對於非 SSL，通常為 TCP 1883。
- `username` 由 MQTT broker 決定，在我們的例子中，它是在 ThingsBoard 管理門戶中生成的 "access token"。

對於 KNOT B → 執行相同步驟。只需將 `username` 更改為為 KNOT B 裝置（閘道器）生成的相應訪問令牌即可。

###### 指令碼 {#script}

將下面顯示的指令碼匯入每個 KNOT。為此，只需複製下面顯示的“程式碼”，貼上到新的終端視窗中，然後按 <kbd>Enter</kbd>：

```ros
/system/script/add dont-require-permissions=no name=tracking owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="# Requ\
    ired packages: iot\r\
    \n\r\
    \n################################ Configuration ##############################\
    ##\r\
    \n# Name of an existing MQTT broker that should be used for publishing\r\
    \n:local broker \"tb\"\r\
    \n\r\
    \n# MQTT topic where the message should be published\r\
    \n:local topic \"v1/gateway/telemetry\"\r\
    \n\r\
    \n# POSIX regex for filtering advertisement Bluetooth addresses. E.g. \"^BC:33:\
    AC\"\r\
    \n# would only include addresses which start with those 3 octets.\r\
    \n# To disable this filter, set it to \"\"\r\
    \n:local addressRegex \"\"\r\
    \n\r\
    \n# POSIX regex for filtering Bluetooth advertisements based on their data. Sam\
    e\r\
    \n# usage as with 'addressRegex'.\r\
    \n:local advertisingDataRegex \"\"\r\
    \n\r\
    \n# Signal strength filter. E.g. -40 would only include Bluetooth advertisement\
    s\r\
    \n# whose signal strength is stronger than -40dBm.\r\
    \n# To disable this filter, set it to \"\"\r\
    \n:local rssiThreshold \"\"\r\
    \n\r\
    \n#Name the KNOT. Identity of the unit that will be sending the message. This n\
    ame will be reported to the MQTT broker.\r\
    \n:local gwName \"KNOT_A\"\r\
    \n\r\
    \n################################## Bluetooth ################################\
    ##\r\
    \n:put (\"[*] Gathering Bluetooth info...\")\r\
    \n\r\
    \n:global makeRecord do={\r\
    \n    :local jsonStr \"{\\\"ts\\\":\$ts,\\\"values\\\":{\\\"reporter\\\":\\\"\$\
    gwName\\\",\\\"rssi\\\":\$rssi}}\"\r\
    \n    :return \$jsonStr\r\
    \n}   \r\
    \n\r\
    \n# array of record strings collected for each advertising MAC address\r\
    \n:global macRecords [:toarray \"\"]\r\
    \n\r\
    \n# process advertisements and update macRecords\r\
    \n:local advertisements [/iot/bluetooth/scanners/advertisements/print detail as\
    -value where \\\r\
    \naddress ~ \$addressRegex and \\\r\
    \ndata ~ \$advertisingDataRegex and \\\r\
    \nrssi > \$rssiThreshold]\r\
    \n\r\
    \n/iot/bluetooth/scanners/advertisements/clear\r\
    \n\r\
    \n:foreach adv in=\$advertisements do={\r\
    \n:local address (\$adv->\"address\")\r\
    \n:local rssi (\$adv->\"rssi\")\r\
    \n:local epoch (\$adv->\"epoch\")\r\
    \n                \r\
    \n:local recordStr [\$makeRecord ts=\$epoch gwName=\$gwName rssi=\$rssi]\r\
    \n\r\
    \n:if ([:len (\$macRecords->\$address)] > 0) do={\r\
    \n:local str (\$macRecords->\$address)\r\
    \n:local newStr \"\$str,\$recordStr\"\r\
    \n:set (\$macRecords->\$address) \$newStr} else={:set (\$macRecords->\$address)\
    \_\$recordStr}}\r\
    \n\r\
    \n# TODO: add some logic to decide when we want to send data\r\
    \n:local sendData true\r\
    \n\r\
    \n:if (\$sendData) do={\r\
    \n:local jsonStr \"{\"\r\
    \n\r\
    \n:foreach addr,advRec in=\$macRecords do={\r\
    \n:set jsonStr \"\$jsonStr\\\"\$addr\\\":[\$advRec],\"}\r\
    \n\r\
    \n:local payloadlength\r\
    \n:set payloadlength [:len (\$jsonStr)]\r\
    \n:local remcom\r\
    \n:set remcom [:pick \$jsonStr 0 (\$payloadlength-1)]\r\
    \n:set jsonStr \"\$remcom}\"\r\
    \n:local message\r\
    \n:set message \"\$jsonStr\"\r\
    \n:log info \"\$message\";\r\
    \n:put (\"[*] Message structured: \$message\")\r\
    \n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
    \n:put (\"[*] Sending message to MQTT broker...\")\r\
    \n/iot/mqtt/publish broker=\"\$broker\" topic=\"\$topic\" message=\$message}"
```

該指令碼應出現在“System>Scripts>Script List”標籤頁下，名稱為 "tracking"，或者可以使用命令 `/system/script/print` 檢視。

有一些指令碼行需要注意。

broker 名稱配置行是你需要輸入已設定的 MQTT broker 名稱的地方：

>      :local broker "tb"

你需要輸入 MQTT broker 使用的正確 topic。更多詳細資訊請檢視 [ThingsBoard 文件](https://thingsboard.io/docs/reference/gateway-mqtt-api/)。預設情況下，topic 應為：

>      :local topic "v1/gateway/telemetry"

MAC 地址過濾選項位於指令碼本身內部。你可以輸入 MAC 地址的全部 6 個八位位元組（將過濾器應用於 1 個特定標籤），也可以使用少量/幾個八位位元組過濾列表，例如 "^BC:33:AC"（應用過濾器，以便只處理以 "BC:33:AC:..." 開頭的 MAC 地址）：

>     :local addressRegex "DC:2C:6E:0F:C0:3D"

負載內容/資料行。它允許你按特定負載內容過濾列表，例如 "[製造商資料](https://help.mikrotik.com/docs/display/UM/MikroTik+Tag+advertisement+formats#heading-MikroTikPDUPayloadstructure)"。例如，"15ff4f09" 將丟棄所有不是 MikroTik 格式負載的負載：

>     :local advertisingDataRegex "15ff4f09"

RSSI 訊號強度過濾選項。此過濾選項已在“[場景說明](#scenario-explanation)”部分提到。該過濾器允許你忽略任何 RSSI 弱於配置值的負載。例如，"-40" 將只包括訊號強度強於 -40dBm 的 Bluetooth 廣播：

>     :local rssiThreshold "-40"

KNOT 識別符號行。你需要為每個唯一 KNOT 更改它。例如，將你的第一個 KNOT 命名為 →  KNOT\_A，將第二個 KNOT 命名為 →  KNOT\_B：

> :local gwName "KNOT\_A"

指令碼的其餘部分無需更改/修改

執行指令碼時它如何工作？指令碼會使用應用的過濾器“檢查”“Advertising reports”標籤頁（負載列表標籤頁），並構造一條 JSON 訊息。JSON 訊息示例如下：

```
{
  "2C:C8:1B:4B:BB:0A": [
    {
      "ts": 1678967250600,
      "values": {
        "reporter": "KNOT_A",
        "rssi": -47
      }
    }
  ],
  "DC:2C:6E:0F:C0:3D": [
    {
      "ts": 1678967247850,
      "values": {
        "reporter": "KNOT_A",
        "rssi": -59
      }
    },
    {
      "ts": 1678967257849,
      "values": {
        "reporter": "KNOT_A",
        "rssi": -67
      }
    }
  ]
}
```

資料按照 [ThingsBoard 指南](https://thingsboard.io/docs/reference/gateway-mqtt-api/#telemetry-upload-api) 進行結構化，其中 `2C:C8:1B:4B:BB:0A` 和 `DC:2C:6E:0F:C0:3D` 是出現在 KNOT 範圍內的標籤的 MAC 地址，`ts` 是標籤廣播的每個負載的 Unix 時間戳（以毫秒為單位），`reporter` 指示是哪個特定 KNOT 傳送了訊息，`rssi` 是標籤廣播的每個負載的訊號強度（以 dBm 為單位）。

在“搜尋”負載列表並構造 JSON 訊息後，Bluetooth 介面負載列表會被“清空”（或“重新整理”），並且先前構造的 JSON 訊息會發送到 ThingsBoard MQTT broker。

要執行指令碼，請使用命令：

```ros
/system/script/run tracking
```

###### 排程器 {#scheduler}

為指令碼應用排程器，以便 RouterOS 定期自行啟動指令碼：

```ros
/system/scheduler/add name=bluetoothscheduler interval=30s on-event="/system/script/run tracking"
```

你可以設定更短或更長的間隔。如果你希望更頻繁地傳送資料，使資料更“新鮮” → 設定更短的時間間隔（10-15 秒）。如果你希望傳送更少訊息、頻率更低 → 可以設定更長的時間間隔（30 分鐘以上）。

使用指令碼構造的 JSON 訊息會為每個收到的負載分配一個 `ts` 值（時間戳）。這意味著，例如，**當指令碼每分鐘執行一次**，使用 1 個標籤，並且**該標籤每 10 秒廣播** 1 個負載（即**每分鐘 6 個負載**）→ ThingsBoard 資料（GUI）將每分鐘更新一次，並且每分鐘會出現 6 個新條目（每個條目將指示它是在前一個條目之後 10 秒收到的）。如果你每 15 分鐘傳送一次訊息，使用 1 個每 10 秒廣播一個負載的標籤（即每 15 分鐘 6\*15=90 個負載）→ ThingsBoard 資料（GUI）將每 15 分鐘更新一次，但會出現 90 個條目。

#### ThingsBoard 資料視覺化與結果驗證 {#thingsboard-data-visualization-and-result-verification}

使用 `/system/script/run tracking` 或透過排程器執行指令碼並重新整理 GUI 門戶後 → JSON 訊息中找到的所有 MAC 地址（標籤）都會在 ThingsBoard GUI 下建立為新裝置：

![](/img/b85bc55bbf5af1aa.webp)

為了幫助你視覺化資料，你可以使用內建的 [部件](https://thingsboard.io/docs/user-guide/ui/widget-library/) 或建立自己的部件。

從裝置列表中選擇標籤的 MAC 地址，轉到“最新遙測”部分，勾選 "reporter" 引數，然後點選“在部件上顯示”按鈕：

![](/img/abadead51b4a0341.webp)

選擇你想使用的部件，例如在“卡片”包下的“時間序列表”，然後點選“新增到儀表板”：

![](/img/412331282135c4b0.webp)

建立一個新儀表板，並隨意命名。點選“新增”：

![](/img/7df5a5ffd9f28fff.webp)

對出現在“裝置”標籤頁下的其他標籤執行相同步驟。在同一儀表板下為每個唯一標籤建立一個新部件。

將部件的“時間視窗”從“即時-最近一分鐘”（預設使用）更改為“即時-當天”：

![](/img/5c1412587045330c.webp)

結果，如果兩個標籤都在 **KNOT A** **範圍**內，儀表板將顯示：

![](/img/4d9e68c164725237.webp)

如果它們移動到 **KNOT B 範圍**，將顯示：

![](/img/a16fc000f709bea2.webp)

如果標籤移動到**重疊區域**，即兩個範圍內，兩個報告者（KNOT\_A 和 KNOT\_B）應在幾秒內先後出現，具體取決於排程器中使用的間隔：

![](/img/bbb25d4c9164e289.webp)

### 示例 #2 {#example-2}

在第二個示例中，我們將展示另一個拓撲：

![](/img/4b356536926ff91a.png)

我們有幾個倉庫、幾輛公司送貨車輛，以及 3 個我們感興趣跟蹤的資產。我們的資產是裝載貨物的系統匣，我們的目標是瞭解：

- 資產（配備標籤）當前位於哪個具體倉庫（配備 KNOT），以及它在那個具體倉庫內停留了多長時間。
- 資產（配備標籤）是否在路上、在倉庫之間運輸，以及它在車輛（配備 KNOT）內停留了多長時間。
- **（可選）如果使用 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out) 標籤**，在這整個過程中溫度是多少？你也可以/改為監控可從廣播[負載](https://help.mikrotik.com/docs/display/UM/MikroTik+Tag+advertisement+formats#heading-Example)中獲得的其他引數，例如加速度。
- **（可選）**找出 KNOT 的 GPS 位置。

要實現 Bluetooth 資產跟蹤，只需每個倉庫安裝 1 臺 KNOT，每輛車安裝 1 臺 KNOT，每個資產安裝 1 個標籤。

我們可以看到 TAG 1 在車輛內，而這輛車剛停在倉庫附近。KNOT 1 和 KNOT 4 都會向伺服器報告資產在它們的範圍內。這會告訴你資產已停放，但尚未被運輸。

我們可以看到 TAG 2 正在倉庫之間運輸，並且只位於 KNOT 5 的 Bluetooth 範圍內。在這種情況下，KNOT 5 將是唯一的報告者，伺服器上顯示的結果將意味著資產正在被運輸。

我們可以看到 TAG 3 在倉庫內。伺服器將僅指示這一點。

伺服器上的資料將顯示 KNOT 傳送的每份報告的時間戳，這將告訴你資產在特定裝置的 Bluetooth 範圍內停留了多長時間。

#### 配置 {#configuration-1}

在本示例中，我們將展示一個基本拓撲：有 2 個倉庫、1 輛在它們之間行駛的車輛/卡車，以及 1 個資產/系統匣/標籤。

##### ThingsBoard 準備 {#thingsboard-preparation-1}

檢視[此處](../../mqtt/mqtt-and-thingsboard-configuration.md)的指南，瞭解如何設定 ThingsBoard 和 RouterOS 以使用 MQTT 通訊。

:::tip
為簡單起見，本示例將展示 [access-token](../../mqtt/mqtt-and-thingsboard-configuration.md#access-token-scenario-1) 場景，但你也可以使用其他可用選項。對於生產環境，建議使用 SSL-MQTT，因為 non-SSL-MQTT 很容易被封包捕獲和檢查。

要了解如何在透過 [container](../../../containers/index.md) 執行的例項上實現 SSL-MQTT 通訊，請檢視[此處](../../../containers/user-guides/container-thingsboard-mqtt-http-server.md)連結的指南（[啟用 HTTPS 和 SSL MQTT](../../../containers/user-guides/container-thingsboard-mqtt-http-server.md#enabling-https-and-ssl-mqtt) 部分）。
:::

在 ThingsBoard GUI 中建立 3 個 KNOT，並將它們設為“閘道器”。

轉到“裝置”部分，點選“+”按鈕，然後點選“新增新裝置”：

![](/img/c96c5c3c49271e3d.webp)

為裝置命名並勾選“是閘道器”選項：

![](/img/8b73d8a2454be8c6.webp)

對你擁有的每個 KNOT 都執行此操作：

![](/img/0915d2aa21abcaa2.webp)

在你剛建立的裝置下，在“管理憑據”標籤頁中，為每個 KNOT 設定唯一的訪問令牌（唯一憑據）：

![](/img/16bbaaab7d956481.webp)

##### RouterOS 配置 {#routeros-configuration-1}

###### 準備工作 {#preparation-1}

在繼續之前，我們需要確認我們的 Bluetooth 標籤確實出現在 KNOT 的 Bluetooth 範圍內，並且 KNOT 能檢測到它。為此，你可以執行命令 `/iot/bluetooth/scanners/advertisements/print`：

```ros
/iot/bluetooth/scanners/advertisements/print
 # DEVICE     PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA                                           
 0 bt1        adv-noconn-ind  2023-03-08 12:35:15 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100b0110100ffff00000019d68d2300005d   
 1 bt1        adv-noconn-ind  2023-03-08 12:35:16 public       DC:2C:6E:0F:C0:3D        -39dBm         22 15ff4f0901008f3cfcfffbfffaff301783c22c000064   
 2 bt1        adv-noconn-ind  2023-03-08 12:35:35 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f09010084d500000400ffff0319ea8d2300005d   
 3 bt1        adv-noconn-ind  2023-03-08 12:35:45 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100e607faffffff03000319f48d2300005d   
```

或者你可以在 IoT>Bluetooth>Advertising reports 標籤頁下使用 [Webfig](../../../management-tools/webfig.md) 或 [Winbox](../../../management-tools/winbox.md) 檢查。

該列表可能很雜亂。由於掃描器會捕獲周圍的一切，隨機負載可能會出現在列表中。為幫助減少列表內容，你可以使用標籤的 MAC 地址 `/iot/bluetooth/scanners/advertisements/print where address=DC:2C:6E:0F:C0:3D` 對其進行過濾：

```ros
/iot/bluetooth/scanners/advertisements/print where address=DC:2C:6E:0F:C0:3D
 # DEVICE    PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA                                           
 0 bt1       adv-noconn-ind  2023-03-08 12:41:06 public       DC:2C:6E:0F:C0:3D        -49dBm         22 15ff4f0901005ab20100fdfffdff4017e1c32c000064   
 1 bt1       adv-noconn-ind  2023-03-08 12:41:26 public       DC:2C:6E:0F:C0:3D        -40dBm         22 15ff4f090100349704000000fcff4017f5c32c000064   
 2 bt1       adv-noconn-ind  2023-03-08 12:41:36 public       DC:2C:6E:0F:C0:3D        -49dBm         22 15ff4f09010073fb0000000000003017ffc32c000064   
 3 bt1       adv-noconn-ind  2023-03-08 12:41:46 public       DC:2C:6E:0F:C0:3D        -43dBm         22 15ff4f090100b88cffffffffffff401709c42c000064   
```

要了解如何解析負載，請檢視[此處](https://help.mikrotik.com/docs/display/UM/MikroTik+Tag+advertisement+formats#heading-Scriptfordecoding)的指南。

###### MQTT 代理 {#mqtt-broker-1}

在每個 KNOT 上設定一個 MQTT broker。

對於 KNOT\_1：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=1883 username=knot-1_access_token
```

其中：

- `name` 是你希望給 broker 指定的名稱，此名稱將在後面的指令碼中使用。
- `address` 是 broker/ThingsBoard 伺服器的 IP 地址。
- `port` 是 broker 監聽的 TCP 埠 → 對於非 SSL，通常為 TCP 1883。
- `username` 由 MQTT broker 決定，在我們的例子中，它是在 ThingsBoard 管理門戶中生成的 "access token"。

對於 KNOT\_2 和 KNOT\_3 → 執行相同步驟。只需將 `username` 更改為生成的相應訪問令牌即可。

###### 指令碼 {#script-1}

將下面顯示的指令碼匯入每個 KNOT。為此，只需複製下面顯示的“程式碼”，貼上到新的終端視窗中，然後按 <kbd>Enter</kbd>：

```ros
/system/script/add dont-require-permissions=no name=tracking owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="# Required package\
    s: iot\r\
    \n\r\
    \n################################ Configuration ################################\r\
    \n# Name of an existing MQTT broker that should be used for publishing\r\
    \n:local broker \"tb\"\r\
    \n\r\
    \n# MQTT topic where the message should be published\r\
    \n:local topic \"v1/gateway/telemetry\"\r\
    \n\r\
    \n# POSIX regex for filtering advertisement Bluetooth addresses. E.g. \"^BC:33:AC\"\r\
    \n# would only include addresses which start with those 3 octets.\r\
    \n# To disable this filter, set it to \"\"\r\
    \n:local addressRegex \"\"\r\
    \n\r\
    \n# POSIX regex for filtering Bluetooth advertisements based on their data. Same\r\
    \n# usage as with 'addressRegex'.\r\
    \n:local advertisingDataRegex \"\"\r\
    \n\r\
    \n# Signal strength filter. E.g. -40 would only include Bluetooth advertisements\r\
    \n# whose signal strength is stronger than -40dBm.\r\
    \n# To disable this filter, set it to \"\"\r\
    \n:local rssiThreshold \"\"\r\
    \n\r\
    \n#Name the KNOT. Identity of the unit that will be sending the message. This name will be \
    reported to the MQTT broker.\r\
    \n:local gwName \"1\"\r\
    \n\r\
    \n################################## Bluetooth ##################################\r\
    \n:put (\"[*] Gathering Bluetooth info...\")\r\
    \n\r\
    \n:global makeRecord do={\r\
    \n    :local jsonStr \"{\\\"ts\\\":\$ts,\\\"values\\\":{\\\"KNOT_\$gwName\\\":\\\"\$gwName\
    \\\",\\\"rssi\\\":\$rssi}}\"\r\
    \n    :return \$jsonStr\r\
    \n}   \r\
    \n\r\
    \n# array of record strings collected for each advertising MAC address\r\
    \n:global macRecords [:toarray \"\"]\r\
    \n\r\
    \n# process advertisements and update macRecords\r\
    \n:local advertisements [/iot/bluetooth/scanners/advertisements/print detail as-value where\
    \_\\\r\
    \naddress ~ \$addressRegex and \\\r\
    \ndata ~ \$advertisingDataRegex and \\\r\
    \nrssi > \$rssiThreshold]\r\
    \n\r\
    \n/iot/bluetooth/scanners/advertisements/clear\r\
    \n\r\
    \n:foreach adv in=\$advertisements do={\r\
    \n:local address (\$adv->\"address\")\r\
    \n:local rssi (\$adv->\"rssi\")\r\
    \n:local epoch (\$adv->\"epoch\")\r\
    \n                \r\
    \n:local recordStr [\$makeRecord ts=\$epoch gwName=\$gwName rssi=\$rssi]\r\
    \n\r\
    \n:if ([:len (\$macRecords->\$address)] > 0) do={\r\
    \n:local str (\$macRecords->\$address)\r\
    \n:local newStr \"\$str,\$recordStr\"\r\
    \n:set (\$macRecords->\$address) \$newStr} else={:set (\$macRecords->\$address) \$recordStr\
    }}\r\
    \n\r\
    \n# TODO: add some logic to decide when we want to send data\r\
    \n:local sendData true\r\
    \n\r\
    \n:if (\$sendData) do={\r\
    \n:local jsonStr \"{\"\r\
    \n\r\
    \n:foreach addr,advRec in=\$macRecords do={\r\
    \n:set jsonStr \"\$jsonStr\\\"\$addr\\\":[\$advRec],\"}\r\
    \n\r\
    \n:local payloadlength\r\
    \n:set payloadlength [:len (\$jsonStr)]\r\
    \n:local remcom\r\
    \n:set remcom [:pick \$jsonStr 0 (\$payloadlength-1)]\r\
    \n:set jsonStr \"\$remcom}\"\r\
    \n:local message\r\
    \n:set message \"\$jsonStr\"\r\
    \n:log info \"\$message\";\r\
    \n:put (\"[*] Message structured: \$message\")\r\
    \n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
    \n:put (\"[*] Sending message to MQTT broker...\")\r\
    \n/iot/mqtt/publish broker=\"\$broker\" topic=\"\$topic\" message=\$message}"
```

該指令碼應出現在“System>Scripts>Script List”標籤頁下，名稱為 "tracking"，或者可以使用命令 `/system/script/print` 檢視。

有一些指令碼行需要注意。

broker 名稱配置行，你需要輸入已設定的 MQTT broker 名稱：

>      :local broker "tb"

你需要輸入 MQTT broker 使用的正確 topic。更多詳細資訊請檢視 [ThingsBoard 文件](https://thingsboard.io/docs/reference/gateway-mqtt-api/)。預設情況下，topic 應為：

>      :local topic "v1/gateway/telemetry"

MAC 地址過濾選項位於指令碼本身內部。你可以輸入 MAC 地址的全部 6 個八位位元組（將過濾器應用於 1 個特定標籤），也可以使用少量/幾個八位位元組過濾列表，例如 "^BC:33:AC"（應用過濾器，以便只處理以 "BC:33:AC:..." 開頭的 MAC 地址）：

>     :local addressRegex "DC:2C:6E:0F:C0:3D"

負載內容/資料行。允許你按特定負載內容過濾列表，例如 "[製造商資料](https://help.mikrotik.com/docs/display/UM/MikroTik+Tag+advertisement+formats#heading-MikroTikPDUPayloadstructure)"。例如，"15ff4f09" 將丟棄所有不是 MikroTik 格式負載的負載：

>     :local advertisingDataRegex "15ff4f09"

RSSI 訊號強度過濾選項。此過濾選項已在“[場景說明](#scenario-explanation)”部分提到。該過濾器允許你忽略任何 RSSI 弱於配置值的負載。例如，"-40" 將只包括訊號強度強於 -40dBm 的 Bluetooth 廣播：

>     :local rssiThreshold "-40"

KNOT 識別符號行。你需要為每個唯一 KNOT 更改它。例如，將你的第一個 KNOT 的 ID 設為 "1"，第二個 KNOT 設為 "2"，第三個 KNOT 設為 "3"：

> :local gwName "1"

指令碼的其餘部分無需更改/修改

執行指令碼時它如何工作？指令碼會使用應用的過濾器“檢查”“Advertising reports”標籤頁（負載列表標籤頁），並構造一條 JSON 訊息。JSON 訊息示例如下：

```
{
  "2C:C8:1B:4B:BB:0A": [
    {
      "ts": 1680526087729,
      "values": {
        "KNOT_1": "1",
        "rssi": -47
      }
    }
  ],
  "DC:2C:6E:0F:C0:3D": [
    {
      "ts": 1680526065000,
      "values": {
        "KNOT_1": "1",
        "rssi": -49
      }
    },
    {
      "ts": 1680526075001,
      "values": {
        "KNOT_1": "1",
        "rssi": -50
      }
    }
  ]
}
```

資料按照 [ThingsBoard 指南](https://thingsboard.io/docs/reference/gateway-mqtt-api/#telemetry-upload-api) 進行結構化，其中 `2C:C8:1B:4B:BB:0A` 和 `DC:2C:6E:0F:C0:3D` 是出現在 KNOT 範圍內的標籤的 MAC 地址，`ts` 是標籤廣播的每個負載的 Unix 時間戳（以毫秒為單位），`KNOT_X` 指示是哪個特定 KNOT 傳送了訊息，`rssi` 是標籤廣播的每個負載的訊號強度（以 dBm 為單位）。

在“搜尋”負載列表並構造 JSON 訊息後，Bluetooth 介面負載列表會被“清空”（或“重新整理”），並且先前構造的 JSON 訊息會發送到 ThingsBoard MQTT broker。

要執行指令碼，請使用命令：

```ros
/system/script/run tracking
```

**包含溫度資料的指令碼（可選）**

如果你希望向構造的訊息中新增溫度報告，請使用下面的指令碼：

```ros
/system/script/add dont-require-permissions=no name=tracking+temp owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="# Required package\
    s: iot\r\
    \n\r\
    \n################################ Configuration ################################\r\
    \n# Name of an existing MQTT broker that should be used for publishing\r\
    \n:local broker \"tb\"\r\
    \n\r\
    \n# MQTT topic where the message should be published\r\
    \n:local topic \"v1/gateway/telemetry\"\r\
    \n\r\
    \n# POSIX regex for filtering advertisement Bluetooth addresses. E.g. \"^BC:33:AC\"\r\
    \n# would only include addresses which start with those 3 octets.\r\
    \n# To disable this filter, set it to \"\"\r\
    \n:local addressRegex \"\"\r\
    \n\r\
    \n# POSIX regex for filtering Bluetooth advertisements based on their data. Same\r\
    \n# usage as with 'addressRegex'.\r\
    \n:local advertisingDataRegex \"\"\r\
    \n\r\
    \n# Signal strength filter. E.g. -40 would only include Bluetooth advertisements\r\
    \n# whose signal strength is stronger than -40dBm.\r\
    \n# To disable this filter, set it to \"\"\r\
    \n:local rssiThreshold \"\"\r\
    \n\r\
    \n#Name the KNOT. Identity of the unit that will be sending the message. This name will be \
    reported to the MQTT broker.\r\
    \n:local gwName \"1\"\r\
    \n\r\
    \n################################## Bluetooth ##################################\r\
    \n:global invertU16 do={\r\
    \n    :local inverted 0\r\
    \n    :for idx from=0 to=15 step=1 do={\r\
    \n        :local mask (1 << \$idx)\r\
    \n        :if (\$1 & \$mask = 0) do={\r\
    \n            :set \$inverted (\$inverted | \$mask)\r\
    \n        }\r\
    \n    }\r\
    \n    return \$inverted\r\
    \n}\r\
    \n\r\
    \n:global le16ToHost do={\r\
    \n    :local lsb [:pick \$1 0 2]\r\
    \n    :local msb [:pick \$1 2 4]\r\
    \n\r\
    \n    :return [:tonum \"0x\$msb\$lsb\"]\r\
    \n}\r\
    \n:local from88 do={\r\
    \n    :global invertU16\r\
    \n    :global le16ToHost\r\
    \n    :local num [\$le16ToHost \$1]\r\
    \n\r\
    \n    # Handle negative numbers\r\
    \n    :if (\$num & 0x8000) do={\r\
    \n        :set num (-1 * ([\$invertU16 \$num] + 1))\r\
    \n    }\r\
    \n\r\
    \n    # Convert from 8.8. Scale by 1000 since floating point is not supported\r\
    \n    :return ((\$num * 125) / 32)\r\
    \n}\r\
    \n:put (\"[*] Gathering Bluetooth info...\")\r\
    \n\r\
    \n:global makeRecord do={\r\
    \n    :local jsonStr \"{\\\"ts\\\":\$ts,\\\"values\\\":{\\\"KNOT_\$gwName\\\":\\\"\$gwName\
    \\\",\\\"temp\\\":\$temp}}\"\r\
    \n    :return \$jsonStr\r\
    \n}   \r\
    \n\r\
    \n# array of record strings collected for each advertising MAC address\r\
    \n:global macRecords [:toarray \"\"]\r\
    \n\r\
    \n# process advertisements and update macRecords\r\
    \n:local advertisements [/iot/bluetooth/scanners/advertisements/print detail as-value where\
    \_\\\r\
    \naddress ~ \$addressRegex and \\\r\
    \ndata ~ \$advertisingDataRegex and \\\r\
    \nrssi > \$rssiThreshold]\r\
    \n\r\
    \n/iot/bluetooth/scanners/advertisements/clear\r\
    \n\r\
    \n:foreach adv in=\$advertisements do={\r\
    \n:local address (\$adv->\"address\")\r\
    \n:local ad (\$adv->\"data\")\r\
    \n:local rssi (\$adv->\"rssi\")\r\
    \n:local epoch (\$adv->\"epoch\")\r\
    \n:local temp [\$from88 [:pick \$ad 28 32]]\r\
    \n                \r\
    \n:local recordStr [\$makeRecord ts=\$epoch gwName=\$gwName temp=\$temp]\r\
    \n\r\
    \n:if ([:len (\$macRecords->\$address)] > 0) do={\r\
    \n:local str (\$macRecords->\$address)\r\
    \n:local newStr \"\$str,\$recordStr\"\r\
    \n:set (\$macRecords->\$address) \$newStr} else={:set (\$macRecords->\$address) \$recordStr\
    }}\r\
    \n\r\
    \n# TODO: add some logic to decide when we want to send data\r\
    \n:local sendData true\r\
    \n\r\
    \n:if (\$sendData) do={\r\
    \n:local jsonStr \"{\"\r\
    \n\r\
    \n:foreach addr,advRec in=\$macRecords do={\r\
    \n:set jsonStr \"\$jsonStr\\\"\$addr\\\":[\$advRec],\"}\r\
    \n\r\
    \n:local payloadlength\r\
    \n:set payloadlength [:len (\$jsonStr)]\r\
    \n:local remcom\r\
    \n:set remcom [:pick \$jsonStr 0 (\$payloadlength-1)]\r\
    \n:set jsonStr \"\$remcom}\"\r\
    \n:local message\r\
    \n:set message \"\$jsonStr\"\r\
    \n:log info \"\$message\";\r\
    \n:put (\"[*] Message structured: \$message\")\r\
    \n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
    \n:put (\"[*] Sending message to MQTT broker...\")\r\
    \n/iot/mqtt/publish broker=\"\$broker\" topic=\"\$topic\" message=\$message}"
```

在這種情況下，JSON 訊息將如下所示：

```
{
  "2C:C8:1B:4B:BB:0A": [
    {
      "ts": 1680527467840,
      "values": {
        "KNOT_1": "1",
        "temp": 26460
      }
    }
  ],
  "DC:2C:6E:0F:C0:3D": [
    {
      "ts": 1680527464996,
      "values": {
        "KNOT_1": "1",
        "temp": 24750
      }
    },
    {
      "ts": 1680527474996,
      "values": {
        "KNOT_1": "1",
        "temp": 24750
      }
    }
  ]
}
```

:::note
由於不支援浮點數 → 小數點後的每次計算都會被“向上舍入”為整數。這就是指令碼會計算溫度和加速度值並**按 1000 縮放**（乘以 **1000**）的原因。  
因此，如果你看到溫度為 **temp=24750**，實際溫度是 **24.750 C**。要新增小數點，你需要在伺服器端進行額外的結果“轉換”，或在 RouterOS 端進行額外指令碼處理，這會增加裝置的 CPU 使用率。
:::

###### 包含 GPS 資料的指令碼（可選） {#script-that-includes-gps-data-optional}

如果你還希望包含 GPS 資料（來自 KNOT 的經度和緯度值），請使用下面顯示的指令碼：

```ros
/system/script/add dont-require-permissions=no name=tracking+gps+temp owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="# Required package\
    s: iot\r\
    \n\r\
    \n################################ Configuration ################################\r\
    \n# Name of an existing MQTT broker that should be used for publishing\r\
    \n:local broker \"tb\"\r\
    \n\r\
    \n# MQTT topic where the message should be published\r\
    \n:local topic \"v1/gateway/telemetry\"\r\
    \n:local gwtopic \"v1/devices/me/telemetry\"\r\
    \n\r\
    \n# POSIX regex for filtering advertisement Bluetooth addresses. E.g. \"^BC:33:AC\"\r\
    \n# would only include addresses which start with those 3 octets.\r\
    \n# To disable this filter, set it to \"\"\r\
    \n:local addressRegex \"\"\r\
    \n\r\
    \n# POSIX regex for filtering Bluetooth advertisements based on their data. Same\r\
    \n# usage as with 'addressRegex'.\r\
    \n:local advertisingDataRegex \"15ff\"\r\
    \n\r\
    \n# Signal strength filter. E.g. -40 would only include Bluetooth advertisements\r\
    \n# whose signal strength is stronger than -40dBm.\r\
    \n# To disable this filter, set it to \"\"\r\
    \n:local rssiThreshold \"\"\r\
    \n\r\
    \n#Name the KNOT. Identity of the unit that will be sending the message. This name will be \
    reported to the MQTT broker.\r\
    \n:local gwName \"2\"\r\
    \n\r\
    \n###########GPS#############\r\
    \n:global lat\r\
    \n:global lon\r\
    \n\r\
    \n/interface/ppp-client/set ppp-out1 disabled=yes\r\
    \n:log info (\"disabling WWAN to get GPS coordinates\")\r\
    \n\r\
    \n/interface/ppp-client/at-chat ppp-out1 input=\"AT+QGPSCFG=\\\"priority\\\",0\"\r\
    \n:log info (\"enabling priority for GPS\")\r\
    \n\r\
    \n###the time in the delay below is the time that the device will wait for to get the coord\
    inate fix\r\
    \n:delay 32000ms\r\
    \n:log info (\"reading GPS coordinates\")\r\
    \n/system/gps/monitor once do={\r\
    \n:set \$lat \$(\"latitude\")\r\
    \n:set \$lon \$(\"longitude\")\r\
    \n}\r\
    \n:if (\$lat != \"none\") do={\\\r\
    \n:log info (\"enabling priority back to WWAN\")\r\
    \n/interface/ppp-client/at-chat ppp-out1 input=\"AT+QGPSCFG=\\\"priority\\\",1\"\r\
    \n:log info (\"enabling WWAN\")\r\
    \n/interface/ppp-client/set ppp-out1 disabled=no\r\
    \n:delay 1000ms\r\
    \n###if dial on demand is enabled\r\
    \n/ping 1.1.1.1 count=1\r\
    \n\r\
    \n#the delay below waits for 5 seconds for the ppp connection to get established - this tim\
    e can differ based on the signal strength\r\
    \n:delay 5000ms\r\
    \n:log info (\"posting coordinates via mqtt\")\r\
    \n:local gpsmessage \\\r\
    \n    \"{\\\"latitude\\\":\$lat,\\\r\
    \n    \\\"longitude\\\":\$lon}\"\r\
    \n/iot/mqtt/publish broker=\$broker topic=\$gwtopic message=\$gpsmessage} else={\\\r\
    \n:log info (\"could not read GPS coordinates...enabling back WWAN\")\r\
    \n/interface/ppp-client/at-chat ppp-out1 input=\"AT+QGPSCFG=\\\"priority\\\",1\"\r\
    \n/interface/ppp-client/set ppp-out1 disabled=no\r\
    \n:delay 1000ms\r\
    \n###if dial on demand is enabled\r\
    \n/ping 1.1.1.1 count=1\r\
    \n:delay 5000ms\r\
    \n}\r\
    \n\r\
    \n##################################Bluetooth##################################\r\
    \n:global invertU16 do={\r\
    \n    :local inverted 0\r\
    \n    :for idx from=0 to=15 step=1 do={\r\
    \n        :local mask (1 << \$idx)\r\
    \n        :if (\$1 & \$mask = 0) do={\r\
    \n            :set \$inverted (\$inverted | \$mask)\r\
    \n        }\r\
    \n    }\r\
    \n    return \$inverted\r\
    \n}\r\
    \n\r\
    \n:global le16ToHost do={\r\
    \n    :local lsb [:pick \$1 0 2]\r\
    \n    :local msb [:pick \$1 2 4]\r\
    \n\r\
    \n    :return [:tonum \"0x\$msb\$lsb\"]\r\
    \n}\r\
    \n:local from88 do={\r\
    \n    :global invertU16\r\
    \n    :global le16ToHost\r\
    \n    :local num [\$le16ToHost \$1]\r\
    \n\r\
    \n    # Handle negative numbers\r\
    \n    :if (\$num & 0x8000) do={\r\
    \n        :set num (-1 * ([\$invertU16 \$num] + 1))\r\
    \n    }\r\
    \n\r\
    \n    # Convert from 8.8. Scale by 1000 since floating point is not supported\r\
    \n    :return ((\$num * 125) / 32)\r\
    \n}\r\
    \n:put (\"[*] Gathering Bluetooth info...\")\r\
    \n\r\
    \n:global makeRecord do={\r\
    \n    :local jsonStr \"{\\\"ts\\\":\$ts,\\\"values\\\":{\\\"KNOT_\$gwName\\\":\\\"\$gwName\
    \\\",\\\"temp\\\":\$temp}}\"\r\
    \n    :return \$jsonStr\r\
    \n}   \r\
    \n\r\
    \n# array of record strings collected for each advertising MAC address\r\
    \n:global macRecords [:toarray \"\"]\r\
    \n\r\
    \n# process advertisements and update macRecords\r\
    \n:local advertisements [/iot/bluetooth/scanners/advertisements/print detail as-value where\
    \_\\\r\
    \naddress ~ \$addressRegex and \\\r\
    \ndata ~ \$advertisingDataRegex and \\\r\
    \nrssi > \$rssiThreshold]\r\
    \n\r\
    \n/iot/bluetooth/scanners/advertisements/clear\r\
    \n\r\
    \n:foreach adv in=\$advertisements do={\r\
    \n:local address (\$adv->\"address\")\r\
    \n:local ad (\$adv->\"data\")\r\
    \n:local rssi (\$adv->\"rssi\")\r\
    \n:local epoch (\$adv->\"epoch\")\r\
    \n:local temp [\$from88 [:pick \$ad 28 32]]\r\
    \n                \r\
    \n:local recordStr [\$makeRecord ts=\$epoch gwName=\$gwName temp=\$temp]\r\
    \n\r\
    \n:if ([:len (\$macRecords->\$address)] > 0) do={\r\
    \n:local str (\$macRecords->\$address)\r\
    \n:local newStr \"\$str,\$recordStr\"\r\
    \n:set (\$macRecords->\$address) \$newStr} else={:set (\$macRecords->\$address) \$recordStr\
    }}\r\
    \n\r\
    \n# TODO: add some logic to decide when we want to send data\r\
    \n:local sendData true\r\
    \n\r\
    \n:if (\$sendData) do={\r\
    \n:local jsonStr \"{\"\r\
    \n\r\
    \n:foreach addr,advRec in=\$macRecords do={\r\
    \n:set jsonStr \"\$jsonStr\\\"\$addr\\\":[\$advRec],\"}\r\
    \n\r\
    \n:local payloadlength\r\
    \n:set payloadlength [:len (\$jsonStr)]\r\
    \n:local remcom\r\
    \n:set remcom [:pick \$jsonStr 0 (\$payloadlength-1)]\r\
    \n:set jsonStr \"\$remcom}\"\r\
    \n:local message\r\
    \n:set message \"\$jsonStr\"\r\
    \n:log info \"\$message\";\r\
    \n:put (\"[*] Message structured: \$message\")\r\
    \n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
    \n:put (\"[*] Sending message to MQTT broker...\")\r\
    \n/iot/mqtt/publish broker=\"\$broker\" topic=\"\$topic\" message=\$message}"
```

這裡需要注意 [BG77 調變解調器行為](https://help.mikrotik.com/docs/display/UM/WWAN+and+GNSS+priority+automatization) → KNOT 中使用的 BG77 蜂窩調變解調器無法同時用於保持蜂窩 CAT-M/NB-IoT 連線和獲取 GPS 座標。

當指令碼執行時：

- PPP 介面被停用，並在 32 秒內將最高優先順序設定為 GPS 接收（此時蜂窩 PPP 介面處於關閉狀態）（此時間可在指令碼中更改）。
- （a）如果裝置在配置的 32 秒內成功獲取 GPS 緯度值（如果獲取的值不等於 "none"），指令碼將用捕獲的緯度和經度值構造一條 JSON 訊息，指令碼會將最高優先順序設定為 WWAN（將優先順序從 GPS 改為 WWAN），並重新啟用 PPP 介面（用於網際網路訪問）。之後，指令碼將透過第一次 MQTT 釋出傳送一條 GPS 資料 JSON 訊息，然後指令碼將執行 Bluetooth 部分，在該部分中構造 Bluetooth 資料 JSON 訊息並透過第二次 MQTT 釋出傳送（傳送 2 條 MQTT 訊息 → GPS 資料 MQTT 訊息和 Bluetooth 資料 MQTT 訊息）。
- （b）如果裝置在 32 秒間隔內未能獲取 GPS 緯度值（如果獲取的值等於 "none"），指令碼會將最高優先順序設定為 WWAN（將優先順序從 GPS 改為 WWAN），重新啟用 PPP 介面（用於網際網路訪問），然後僅處理 Bluetooth 部分，在該部分中構造 Bluetooth 資料 JSON 訊息並透過 MQTT 釋出傳送（基本上，如果無法獲取 GPS 資料，則傳送 1 條包含 Bluetooth 資料的 MQTT 訊息）。

###### 排程器 {#scheduler-1}

為指令碼應用排程器，以便 RouterOS 定期自行啟動指令碼：

```ros
/system/scheduler/add name=bluetoothscheduler interval=50s on-event="/system/script/run tracking"
```

你可以設定更短或更長的間隔。如果你希望更頻繁地傳送資料，使資料更“新鮮” → 設定更短的時間間隔（10-15 秒）。如果你希望傳送更少訊息、頻率更低 → 可以設定更長的時間間隔（30 分鐘以上）。

使用指令碼構造的 JSON 訊息會為每個收到的負載分配一個 `ts` 值（時間戳）。這意味著，例如，**當指令碼每分鐘執行一次**，使用 1 個標籤，並且**該標籤每 10 秒廣播** 1 個負載（即**每分鐘 6 個負載**）→ ThingsBoard 資料（GUI）將每分鐘更新一次，並且每分鐘會出現 6 個新條目（每個條目將指示它是在前一個條目之後 10 秒收到的）。如果你每 15 分鐘傳送一次訊息，使用 1 個每 10 秒廣播一個負載的標籤（即每 15 分鐘 6\*15=90 個負載）→ ThingsBoard 資料（GUI）將每 15 分鐘更新一次，但會出現 90 個條目。

#### ThingsBoard 資料視覺化與結果驗證 {#thingsboard-data-visualization-and-result-verification-1}

使用 `/system/script/run tracking` 或透過排程器執行指令碼並重新整理 GUI 門戶後 → JSON 訊息中找到的所有 MAC 地址（標籤）都會在 ThingsBoard GUI 下建立為新裝置：

![](/img/b85bc55bbf5af1aa.webp)

為了幫助你視覺化資料，你可以使用內建的 [部件](https://thingsboard.io/docs/user-guide/ui/widget-library/) 或建立自己的部件。

從裝置列表中選擇標籤的 MAC 地址，轉到“最新遙測”部分，選擇你要監控的 KNOT ID，然後點選“在部件上顯示”按鈕：

![](/img/2aba39a24468b22e.webp)

選擇你想使用的部件，例如在“圖表”包下的“時間序列柱狀圖”，然後點選“新增到儀表板”：

![](/img/0eadc5f212d7258e.webp)

建立一個新儀表板，並隨意命名。點選“新增”：

![](/img/4af97b4887f17f88.webp)

將部件的“時間視窗”從“即時-最近一分鐘”（預設使用）更改為“即時-最近 5 小時”，並停用“資料聚合函式”（選擇“無”）：

![](/img/dd359217e9a9672c.webp)

為了幫助你更好地視覺化結果，請編輯部件，然後編輯每個 "KNOT\_X" 引數/鍵。為每個鍵啟用“顯示點”複選框：

![](/img/a3b7272e4807b355.webp)

檢視 ThingsBoard 部件[指南](https://thingsboard.io/docs/user-guide/ui/chart-widget/#timeseries-bar-chart)，瞭解你可用的更多選項。

最終結果將如下所示：

![](/img/bc771871ad8da5bb.webp)

從儀表板可以看出：

- 從 ~11:00 到 ~11:30，我們的資產在 KNOT\_1 的 Bluetooth 範圍內（1 號倉庫內）。
- 從 ~11:30 到 ~11:35，我們的資產被轉移到停在倉庫附近的車輛（KNOT\_2）上（標籤同時處於兩個 KNOT 的範圍內）。
- 從 ~11:35 到 ~12:00，標籤在卡車（KNOT\_2）內——正前往另一個倉庫。
- 從 ~12:00 到 ~12:05，資產停在 2 號倉庫外，並且同時處於 KNOT\_2 和 KNOT\_3 的範圍內。
- 從 ~12:05 到 12:30，我們的資產存放在 2 號倉庫（KNOT\_3）內。
- 從 ~12:30 起，標籤再次上路，在卡車（KNOT\_2）內。

##### 溫度視覺化（可選） {#temperature-visualization-optional}

從裝置列表中選擇標籤的 MAC 地址，轉到“最新遙測”部分，勾選 `temp` 引數，然後點選“在部件上顯示”按鈕：

![](/img/9bab51d0ecf1d3f3.webp)

選擇你想使用的部件，例如在“圖表”包下的“時間序列折線圖”。點選“新增到儀表板”，然後選擇要新增該部件的儀表板。

結果將如下所示：

![](/img/d3abc7e9e479239e.webp)

現在你有一個額外的圖表，顯示標籤溫度在不同時間間隔內如何變化。

##### GPS 座標視覺化（可選） {#gps-coordinate-visualization-optional}

根據[包含 GPS 資料的指令碼](#script-that-includes-gps-data-optional)部分中的指令碼，指令碼會發送 2 條 MQTT 訊息。每條訊息傳送到不同的 MQTT topic。GPS 座標訊息將釋出到名為 "v1/devices/me/telemetry" 的 topic，而 Bluetooth 資料將釋出到名為 "v1/gateway/telemetry" 的 topic。你可以在 ThingsBoard 裝置列表中的特定閘道器下檢視座標：

![](/img/60ce4ad341008aa9.webp)

勾選 "latitude" 和 "longitude" 兩個引數，點選“在部件上顯示”按鈕，將“當前包”設定為“地圖”，然後選擇“路線圖 - OpenStreetMap”部件：

![](/img/75eb9bc9563359ff.webp)

最後，點選“新增到儀表板”按鈕，並選擇要顯示該部件的儀表板。

將 3 個部件新增到 1 個儀表板（溫度折線圖、Bluetooth 報告者柱狀圖和 GPS 座標地圖）後，你將得到類似下面的內容：

![](/img/c81d00920bd300cf.webp)

- 你將有一個顯示溫度變化（標籤周圍溫度）的圖表。
- 你將有一個圖表，指示是哪個特定 KNOT 傳送了報告，從而告訴你標籤當前位於哪個 KNOT 的 Bluetooth 範圍內。
- 你將有一張顯示 KNOT GPS 位置的地圖。
