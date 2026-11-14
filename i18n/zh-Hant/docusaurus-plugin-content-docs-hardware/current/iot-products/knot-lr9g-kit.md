---
title: "KNOT LR9G 套件"
slug: /knot-lr9g-kit
source: https://manual.mikrotik.com/hardware/knot-lr9g-kit
captured_at: '2026-11-04T09:53:20+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

→ 本指南可以下載為 <a href="/assets/files/knot-lr9g-kit-b74fa0b50265ed036c2a40802b068492.pdf" target="_blank" rel="noopener">PDF 檔案</a>。

![](/img/d2de7c6aedce0031.webp)

### [KNOT LR9G kit](https://mikrotik.com/product/knot_lr9g_kit)（RB924iR-2nD-BT5&BG770A&R11e-LR9G） {#knot-lr9g-kit-rb924ir-2nd-bt5bg770ar11e-lr9g}

→ 適用於最具多樣性和成本效益的部署環境的 IoT 閘道器。完整規格和產品宣傳冊請參見 [KNOT LR9G kit 產品頁面](https://mikrotik.com/product/knot_lr9g_kit)。

## 安全警告 {#safety-warnings}

- 客戶有責任遵守當地國家法規，包括在合法頻段內執行、發射功率、佈線要求以及 Dynamic Frequency Selection (DFS) 要求。所有 MikroTik 無線電裝置必須由專業人員安裝。

→ **射頻輻射暴露：** 本 MikroTik 裝置符合 FCC、IC 和歐盟針對非受控環境規定的輻射暴露限值。安裝和操作本 MikroTik 裝置時，裝置與您的身體、職業使用者或公眾之間的距離不得小於 20 釐米。

## 快速開始 {#quickstart}

- 設定路由器密碼。

→ *U.FL 轉 SMA 轉接線和外部藍牙天線不隨包裝提供。*

## 主要特性 {#key-features}

![](/img/b1e92974169eba45.webp)

![](/img/7e01ab6b4a4d437f.webp)

![](/img/944d0bd720be0572.webp)

![](/img/865c394907132195.webp)

## 規格 {#specifications}

<table><thead><tr><th>引數</th><th>描述</th></tr></thead><tbody><tr><td>**產品程式碼**</td><td>RB924iR-2nD-BT5&BG770A&R11e-LR9G</td></tr><tr><td>**架構**</td><td>MIPSBE</td></tr><tr><td>**CPU**</td><td>QCA9531，1 核，650 MHz</td></tr><tr><td>**RAM**</td><td>64 MB</td></tr><tr><td>**儲存**</td><td>128 MB NAND</td></tr><tr><td>**RouterOS 許可證**</td><td>4</td></tr><tr><td>**作業系統**</td><td>RouterOS v7</td></tr><tr><td>**乙太網**</td><td>2 × 10/100 (Auto MDI/X)</td></tr><tr><td>**PoE 輸入**</td><td>802.3af/at，12–57 V DC</td></tr><tr><td>**PoE 輸出**</td><td>Ether2，被動 PoE，最高 57 V</td></tr><tr><td>**最大功耗**</td><td>20 W</td></tr><tr><td>**無線 2.4 GHz**</td><td>802.11b/g/n，2×2，1.5 dBi</td></tr><tr><td>**藍牙**</td><td>5.2</td></tr><tr><td>**USB**</td><td>1 × microUSB（AB 型）</td></tr><tr><td>**SIM**</td><td>1 × nano-SIM</td></tr><tr><td>**序列埠**</td><td>RS485</td></tr><tr><td>**LoRa 卡**</td><td>R11e-LR9G，902–928 MHz (US)，最高 27 dBm，Class A/C，GPS 透過 U.FL</td></tr><tr><td>**尺寸**</td><td>122 × 87 × 26 mm</td></tr><tr><td>**工作溫度**</td><td>−40 °C … +70 °C</td></tr><tr><td>**防護等級**</td><td>IP20</td></tr><tr><td>**MTBF**</td><td>≈ 100 000 h @ 25 °C</td></tr><tr><td>**認證**</td><td>CE、FCC、IC、EAC、RoHS</td></tr></tbody></table>

## 安裝 {#mounting}

![](/img/60a25f0b55a2a55d.webp)

- 或者，也可以使用裝置背面的螺釘孔將裝置固定到牆上。裝置應以線纜開口朝下的方式安裝，如圖所示。**警告：** 本裝置應在與身體保持至少 20 cm 距離的情況下安裝和操作。本裝置在住宅環境中執行可能會導致無線電干擾。本裝置的安裝和配置應由合格人員完成。

## 供電 {#powering}

- 將乙太網線從本地網路 (LAN) 連線到 PoE 介面卡。

- 將電源線連線到介面卡，然後將電源線插入電源插座。

## 擴充套件插槽和埠 {#extension-slots-and-ports}

![](/img/46b18e887e695663.webp)

- Bluetooth 版本 5.2，天線增益 2 dBi。

→ **KNOT LR9G kit：**

- LR9G 卡。

## Modbus {#modbus}

→ KNOT 的 Modbus [配置指南](/docs/internet-of-things/modbus)。

## Bluetooth 天線 {#bluetooth-antenna}

→ 對於 KNOT LR8 kit、KNOT LR8G kit、KNOT LR9 kit 和 KNOT LR9G kit，藍牙外接天線轉接線的預留位置**不可用**（此處已有一個由 LoRa 使用的 SMA 插槽）。

要使用外接天線，您需要一個 U.FL (female) 轉 SMA 聯結器（pigtail）以及一個 Bluetooth 天線（可連線到 SMA）。

要使用外接天線，您需要一個 U.FL (female) 轉 SMA 聯結器（pigtail）以及一個 Bluetooth 天線（可連線到 SMA）。

![](/img/fdb0c8a7e4b9a21f.webp)

- 將 Bluetooth 天線連線到 SMA 插槽。您需要在 RouterOS 設定中更改您希望使用的天線（新連線的 "external" 或內建的 "internal"）（在 IoT→ Bluetooth→Devices→雙擊 Bluetooth 介面→ 在 Antenna 欄位中）：

![](/img/0b9b0fd9fbf0ff90.webp)

→ U.FL 轉 SMA 轉接線和外部藍牙天線不隨包裝提供。

## GPS 與 NB/CAT-M {#gps-and-nbcat-m}

→ 將您的天線連線到 SMA 聯結器：

![](/img/fa4fa700c587500b.webp)

→ 使用窄帶調變解調器和 GPS 時必須連線外部天線。不隨包裝提供。

必須連線外部天線才能使用窄帶調變解調器和 GPS。包裝中不提供。

名為 "modem" 的埠用於蜂窩連線（serial/PPP 連線）和 GPS 接收：

```
/port print
Flags: I - INACTIVE
Columns: DEVICE, NAME, CHANNELS, USED-BY, BAUD-RATE
#   DEVICE  NAME    CHANNELS  USED-BY  BAUD-RATE
0           modbus         1                9600
1   1-1.4   modem          5              115200

```

2 - AT/modem 埠；

→ 2 - AT/modem 埠；

2 - AT/modem 埠；

4 - AUX AT/modem 埠 - 最大頻寬 115200bps，僅適用於 KNOT LoRa 套件和帶內部 USB 集線器的 KNOT。

### 蜂窩調變解調器配置 {#cellular-modem-configuration}

→ BG77 調變解調器的 AT 命令可在 [BG77 AT Commands Manual](https://mikrotik.com/product/knot#tab0) 中找到。

KNOT 預設具有 serial/PPP 連線預設：

KNOT 預設具有 serial/PPP 連線預設：

```
/interface ppp-client print
Flags: X - disabled; R - running
 0 R  name="ppp-out1" max-mtu=1500 max-mru=1500 mrru=disabled port=modem data-channel=2 info-channel=4 apn="internet"
      pin="" user="" password="" profile=default phone="" dial-command="ATDT" modem-init="AT+QGPSCFG="priority",1"
      null-modem=no dial-on-demand=yes add-default-route=yes default-route-distance=1 use-peer-dns=yes keepalive-timeout=30
      allow=pap,chap,mschap1,mschap2

```

有關 serial/PPP 連線的更多詳細資訊，請檢視 [PPP Client](/docs/mobile-networking/ppp) 文件。

有關 serial/PPP 連線的更多詳細資訊，請檢視 [PPP Client](/docs/mobile-networking/ppp) 文件。

### GPS 配置 {#gps-configuration}

→ 如果遇到 GPS 接收問題：

→ - 取下 KNOT 的外殼，確認 U.FL 轉接線已從 LoRa 卡連線到 SMA 埠。

- 確保外部 GPS 天線已正確連線到標有 GNSS 的 SMA 埠。

### 蜂窩調變解調器韌體升級 {#cellular-modem-firmware-upgrade}

→ - DFOTA 韌體檢查/升級可以使用任何網際網路連線完成（包括 wi-fi 和乙太網上行鏈路）。因此，即使 BG77 沒有蜂窩連線（例如僅用作 GPS 接收器）的裝置也可以升級調變解調器韌體。

- 當 BG77 調變解調器的 serial/PPP 介面使用主 AT/modem 通道（data-channel=2）時，支援韌體升級。要檢查當前安裝的 BG77 韌體版本，請使用以下命令指定 "upgrade=no" 引數：

```
/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=no
  installed: BG77LAR02A04_01.001.01.001
     latest: BG77LAR02A04_01.009.01.009

```

→ 要更新 BG77 調變解調器韌體，請將引數設定為 "upgrade=yes"：

```
/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=yes

```

## 按鈕和跳線 {#buttons-and-jumpers}

→ - 要使用 [Netinstall](/docs/getting-started/installation-and-upgrade/netinstall) 實用工具重新安裝 RouterOS，請讓裝置進入 BOOTP 模式。有兩種 booter 選項可用：**Regular Booter** 和 **Backup Booter**。建議在其中一個不起作用時對兩種選項都進行驗證。

- **Regular Booter:** 要進入 etherboot 模式，請在給裝置通電並等待 1–2 秒後按下 **Reset** 按鈕。

- **Regular Booter:** 要進入 etherboot 模式，請在給裝置通電並等待 1–2 秒後按下 **Reset** 按鈕。
- **Backup Booter:** 關閉裝置。按住 **Reset** 按鈕，然後給裝置上電。等待 **LED** 序列（閃爍 → 常亮 → 熄滅），然後鬆開按鈕。裝置將啟動進入 **BOOTP** 模式，可透過 Netinstall 重新安裝 RouterOS。視型號而定，這可能由 **USR, USER, System** 或 **ACT** LED 指示，或由 SFP 埠 LED 指示。

→ 無論使用上述哪種選項，如果在裝置通電之前按下按鈕，系統都將載入備份 RouterBOOT 載入程式。這對於 RouterBOOT 偵錯和恢復很有用。

## GPIO 引腳排列 {#gpio-pinout}

→ GPIO 引腳位於外殼下方的電路板上，如圖所示：

![](/img/aa56f6a091950f7a.webp)

→ ADC 輸入/模擬輸入（pin2 或 pin3）：

![](/img/0201b8beb9b054ef.webp)

已連線的繼電器（pin4 或 pin6）：

已連線的繼電器（pin4 或 pin6）：

![](/img/4b8f177a2150596d.webp)

→ *注意：最大功耗（數字輸出開漏電晶體）為 0.48 W。建議在連續工作時不要超過 24V 或 0.5A。絕對最大漏源電壓為 30V，最大電流為 2.8A。*

![](/img/4c01507e5fd17337.webp)

防拆開關（pin5）：

防拆開關（pin5）：

![](/img/597abb74d2c7dc9c.webp)

→ *要在引腳上獲得邏輯 "0"，電壓應在 0-1.47 V 之間；*

-

*要在引腳上收到邏輯 "1"，電壓應在 1.48-2.5 V 之間。* *使用 PCB 上拉電阻時：*

→ *要在引腳上獲得邏輯 "1"，電壓應在 1.48-2.5 V 之間。* *有 PCB 上拉電阻時：*

-

*要在引腳上收到邏輯 "1"，電壓應在 1.48-2.5 V 之間。* *使用 PCB 上拉電阻時：*

→ *要在引腳上獲得邏輯 "0"，電壓應在 0-1.34 V 之間；*

*要在引腳上收到邏輯 "0"，電壓應在 0-1.34 V 之間；*

*要在引腳上收到邏輯 "1"，電壓應在 1.35-2.5 V 之間。* *較新的 routerboard 將在 PCB（板上）上帶有 10k ohm 上拉電阻。較舊的板（首批發布批次）可能需要外部上拉電阻。*

*要在引腳上收到邏輯 "1"，電壓應在 1.35-2.5 V 之間。* *較新的 routerboard 將在 PCB（板上）上帶有 10k ohm 上拉電阻。較舊的板（首批發布批次）可能需要外部上拉電阻。*

## 配件 {#accessories}

→ - SET2_ K-74 DIN 導軌安裝套裝。

- Modbus 聯結器，A+，B-。

→ HGO-LTE-W 天線可單獨購買。

![](/img/90314e3eea2eb9bb.webp)

## 作業系統支援 {#operating-system-support}

→ 本裝置支援 RouterOS v7 及以上版本。出廠安裝的具體版本列於 /system resource 中。其他作業系統尚未經過測試。

## 配置 {#configuration}

如果您擁有 LR8 或 LR9 KNOT 變體，並且有興趣使用 LoRa 協定，請點選我們的 LoRa 指南。

→ 如果您使用的是 LR8 或 LR9 KNOT 版本，並且希望使用 LoRa 協定，請點選我們的 LoRa 指南。

如果您擁有 LR8 或 LR9 KNOT 變體，並且有興趣使用 LoRa 協定，請點選我們的 LoRa 指南。

要檢視其他 IoT 功能，請訪問 IoT 頁面。

## 概述 {#overview}

→ 您需要做的只是配置一個指令碼。該指令碼可以過濾廣播資訊並將其推送到網際網路。

本文介紹如何配置 KNOT 以使用 MQTT 或 http 協定釋出資料。

→ 本文介紹如何配置 KNOT 以使用 MQTT 或 http 協定釋出資料。

本文介紹如何配置 KNOT 以使用 MQTT 或 http 協定釋出資料。

必須連線外部天線才能使用窄帶調變解調器和 GPS。包裝中不提供。

## 報告 {#reports}

您可以在 Advertising reports 標籤頁中找到所有廣播裝置。

您可以在 Advertising reports 標籤頁中找到所有廣播裝置。

![](/img/4ee647301a86eb0c.webp)

→ 在此選單中，您可以按下 Filter 圖示來設定過濾器。例如，在知道裝置 MAC 地址的情況下，您可以設定過濾器以僅顯示特定的報告。

![](/img/bf2032dfd2080349.webp)

您可以使用 - 圖示移除篩選選項。

您可以使用 - 圖示移除篩選選項。

## MQTT Broker 配置 {#mqtt-broker-configuration}

您可以透過 + 按鈕新增新的 broker。

您可以透過 + 按鈕新增新的 broker。

![](/img/1a3a89d9fc694e82.webp)

<table><thead><tr><th>屬性</th><th>描述</th></tr></thead><tbody><tr><td>名稱</td><td>標識。Broker 的名稱。</td></tr><tr><td>地址</td><td>MQTT broker 的 IP 地址或 FQDN 名稱，不帶 ssl:// 或 tcp:// 字首。</td></tr><tr><td>埠</td><td>broker 的網路埠。通常為 1883 或 8883（用於 SSL）。</td></tr><tr><td>SSL</td><td>啟用/停用 Secure Socket Layer。如果伺服器使用自簽名證書或由不受信任的 CA 簽發的證書，您必須將伺服器的證書 &lt;crt&gt; 檔案上傳到 RouterOS。將 .cer 檔案上傳到 Files 選單，並在 System&gt;Certificates 標籤頁中將該檔案匯入到 certificates。</td></tr><tr><td>使用者名稱</td><td>MQTT broker 的使用者名稱。</td></tr><tr><td>密碼</td><td>MQTT broker 的密碼。</td></tr><tr><td>Client Id</td><td>用於連線的唯一 ID。broker 使用此 ID 來識別用戶端。</td></tr><tr><td>證書</td><td>如果雙向認證需要，請選擇證書。</td></tr></tbody></table>

**注意：** Name、Address 和 Port 欄位配置是必需的。其他引數可以是可選的或必需的 - 取決於伺服器/broker 的設定方式。

**注意：** Name、Address 和 Port 欄位配置是必需的。其他引數可以是可選的或必需的 - 取決於伺服器/broker 的設定方式。

## 釋出 {#publish}

→ 建立 broker 後，單擊 Publish 按鈕。此對話方塊允許您選擇 broker 並指定訊息資訊。

![](/img/d3b62757ecbe08c5.webp)

→ 然後您可以指定 Topic（broker 用於過濾訊息的字串）、Message（訊息本身）、QoS（指示訊息的服務質量等級）和 Retain（是保留訊息還是丟棄訊息）引數。

**注意：** Broker 和 Topic 欄位配置是必需的。Message、QoS 和 Retain 可以是可選的或必需的 - 取決於伺服器/broker 的設定方式。

**注意：** Broker 和 Topic 欄位配置是必需的。Message、QoS 和 Retain 可以是可選的或必需的 - 取決於伺服器/broker 的設定方式。

## MQTT 與指令碼場景 {#mqtt-with-script-scenario}

每一行以符號 "**#**" 開頭的都是說明性內容，它描述將在該行下方配置的引數。請更改引號 "" 內適用於您具體情況的引數。

→ 每一行以符號 "**#**" 開頭的都是說明性內容，描述該行下方將要配置的引數。請修改引號 "" 內適用於您具體情況的引數。

每一行以符號 "**#**" 開頭的都是說明性內容，它描述將在該行下方配置的引數。請更改引號 "" 內適用於您具體情況的引數。

指令碼示例：

```
## Required packages: iot

################################ Configuration ################################
## Name of an existing MQTT broker that should be used for publishing
:local broker "Demo Device"

## MQTT topic where the message should be published
:local topic "v1/devices/me/telemetry"

## Interface whose MAC should be used as 'Locator ID'
:local locatorIface "ether1"

## POSIX regex for filtering advertisement Bluetooth addresses. E.g. "^BC:33:AC"
## would only include addresses which start with those 3 octets.
## To disable this filter, set it to ""
:local addressRegex ""

## POSIX regex for filtering Bluetooth advertisements based on their data. Same
## usage as with 'addressRegex'.
:local advertisingDataRegex ""

## Signal strength filter. E.g. -40 would only include Bluetooth advertisements
## whose signal strength is stronger than -40dBm.
## To disable this filter, set it to ""
:local rssiThreshold ""

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
## Health is a bit iffy since '/system health' does not have 'find' in ROS6
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
        rssi > $rssiThreshold]
:local advJson ""
:local advCount 0
:local advSeparator ""
:local lastAdvTimestamp 0
## Remove semicolons from MAC/Bluetooth addresses
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

→ 要執行此指令碼，Broker 應已預先配置：

![](/img/ce0edf2496617c43.webp)

→ 例如，thingsboard 只需要上圖所示的設定。成功配置 broker 後，指令碼中唯一需要更改的是：

```
:local broker "Demo Device"

```

行，你應在引號 "" 內指定 broker 的名稱。

另一個需要考慮的行是：

```
:local topic "v1/devices/me/telemetry"

```

導航到 System &gt; Scripts，並在那裡新增新指令碼（為其命名，例如 script1）。

指令碼配置的其餘部分取決於整體需求。指令碼中說明了配置了哪些確切引數用於釋出。

導航到 System &gt; Scripts，並在那裡新增新指令碼（為其命名，例如 script1）。

要執行指令碼，您可以使用命令列：

/system script run script1

## HTTP fetch 與指令碼場景 {#http-fetch-with-script-scenario}

→ 建立一個新指令碼，以該模板作為參考，相應修改引數並執行指令碼。

每一行以符號 "**#**" 開頭的都是說明性內容，它描述將在該行下方配置的引數。請更改引號 "" 內適用於您具體情況的引數。

→ 每一行以符號 "**#**" 開頭的都是說明性內容，描述該行下方將要配置的引數。請修改引號 "" 內適用於您具體情況的引數。

每一行以符號 "**#**" 開頭的都是說明性內容，它描述將在該行下方配置的引數。請更改引號 "" 內適用於您具體情況的引數。

指令碼示例：

```
## Required packages: iot

################################ Configuration ################################
## Interface whose MAC should be used as 'Locator ID'
:local locatorIface "ether1"

## POSIX regex for filtering advertisement Bluetooth addresses. E.g. "^BC:33:AC"
## would only include addresses which start with those 3 octets.
## To disable this filter, set it to ""
:local addressRegex ""

## POSIX regex for filtering Bluetooth advertisements based on their data. Same
## usage as with 'addressRegex'.
:local advertisingDataRegex ""

## Signal strength filter. E.g. -40 would only include Bluetooth advertisements
## whose signal strength is stronger than -40dBm.
## To disable this filter, set it to ""
:local rssiThreshold ""

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
## Health is a bit iffy since '/system health' does not have 'find' in ROS6
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
        rssi > $rssiThreshold]
:local advJson ""
:local advCount 0
:local advSeparator ""
:local lastAdvTimestamp 0
## Remove semicolons from MAC/Bluetooth addresses
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
/tool fetch http-method=post http-header-field="Content-Type:application/json" http-data=$message url="https://demo.thingsboard.io/api/v1/Q99YlBqv59NdzOel6tyP/telemetry"
:put ("[*] Done")

```

→ 請相應更改 URL（取決於伺服器配置）。

```
/tool fetch http-method=post http-header-field="Content-Type:application/json" http-data=$message url="https://demo.thingsboard.io/api/v1/Q99YlBqv59NdzOel6tyP/telemetry"

```

導航到 System &gt; Scripts，並在那裡新增新指令碼（為其命名，例如 script1）。

要執行指令碼，您可以使用命令列：

/system script run script1

## MikroTik 移動應用 {#mikrotik-mobile-app}

使用 MikroTik 智慧手機應用可在現場配置路由器，或為您的 MikroTik 家用接入點應用最基本的初始設定。

![](/img/9bcba09a7b6a0d53.webp)

- 可以使用高階選單來完整配置所有必要設定。

**Bluetooth 合格產品**

**Bluetooth 合格產品**

![](/img/cf3c8d2919f980e2.webp)

→ 本產品已成功完成藍牙認證流程。有關藍牙認證產品的更多資訊，請使用以下連結：[https://launchstudio.bluetooth.com/Listings/Search](https://launchstudio.bluetooth.com/Listings/Search)
