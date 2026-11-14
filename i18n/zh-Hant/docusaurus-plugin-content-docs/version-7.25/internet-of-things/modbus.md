---
sidebar_key: "internet-of-things/modbus"
sidebar_position: 4
title: "Modbus"
sidebar_label: "Modbus"
source: https://manual.mikrotik.com/docs/7.25/internet-of-things/modbus
captured_at: '2026-11-04T11:19:10+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 簡介 {#introduction}

:::warning
目前，只有 [KNOT](https://mikrotik.com/product/knot)、[KNOT LR8G kit](https://mikrotik.com/product/knot_lr8g_kit) 和 [KNOT LR9G kit](https://mikrotik.com/product/knot_lr9g_kit) 支援 Modbus 協定（具有 RS-485 埠）。
:::
IoT 架構中廣泛使用的一種協定稱為 Modbus。

![](/img/09d4aa2b0f52e81e.webp)

你可以透過此連結查詢有關該協定的更多資訊。

支援 Modbus 的裝置應連線到 RS485 埠。該裝置支援兩線連線（A+/B-）（2 引腳端子塊）。

![](/img/de1335a743cac8c4.webp)

必須注意不要混淆兩個引腳。將 "A" 和 "B" 連線反接（極性錯誤）會導致通訊失敗。

另一點需要記住的是 Modbus 線纜距離。如果線纜長度小於 50 meters - 應該沒有問題。如果使用 50+ meters 線纜，則應在電纜末端安裝 120 Ohm 終端電阻。

KNOT 支援：

- **Modbus TCP 伺服器場景**，它允許你使用第三方 Modbus 用戶端，透過 Modbus TCP/IP 連線（TCP 埠 502）向 KNOT 的 IP 地址傳送功能碼命令。你可以使用任何 Modbus 用戶端軟體（網際網路上有很多），也可以用 Python 輕鬆編寫/配置。在這種情況下，KNOT 會將 Modbus TCP/IP 請求“轉換/橋接”為 Modbus RTU。
- **Modbus RTU 控制器場景 **(僅從 v**7.10** 開始提供)，它允許你透過 Modbus/RTU 直接從 RouterOS 命令列傳送功能碼命令。

#### Modbus TCP 封包結構 {#modbus-tcp-packet-structure}

你可以使用此[連結](https://en.wikipedia.org/wiki/Modbus)查詢有關 Modbus 封包結構的更多資訊。

查詢封包由事務 ID、協定、長度、單元 ID、功能碼和功能引數欄位組成，最大大小為 260 bytes。

- 事務 ID - 從 0 到 65535 的整數，用於標識對特定查詢的應答；
- 協定 - 0x0000 表示 Modbus；
- 長度 - 顯示長度欄位之後將跟隨多少 bytes；
- 單元 ID - 通常稱為“裝置地址”，0x00-0xff。特定系統中的每個終端裝置都應具有唯一 ID；
- 功能碼 - 描述將呼叫哪個功能。每個裝置都有多個暫存器，這些功能用於與暫存器互動。程式碼由標準定義，但製造商也可以使用特定程式碼實現自己的功能；
- 功能引數/資料 - 通常指定暫存器地址、資料長度，以及在使用 "write" 功能時要寫入的資料。
預設單元 ID、功能碼和引數可在特定產品的資料表中找到。應答訊息的結構類似，也應在產品資料表中進行描述。

### 配置 {#configuration}

**子選單：** `/iot modbus`

將板卡連線到 Modbus 裝置後，檢查 "modbus" 埠配置（如果所連線的 Modbus 裝置期望其他值，可以更改 baud-rate）：

```ros
[admin@MikroTik] > /port print
Columns: DEVICE, NAME, CHANNELS, USED-BY, BAUD-RATE
# DEVICE  NAME    CHANNELS  USED-BY  BAUD-RATE
0         modbus         1  modbus        9600
1 1-1     modem          4                9600
```

預設情況下，名稱為 "*modbus"* 的埠會分配給 Modbus 服務，但該服務本身處於停用狀態。要啟用 "Modbus" 服務，你需要執行如下所示的命令：

```ros
[admin@MikroTik] > /iot modbus print       
                disabled: yes
           hardware-port: modbus
                tcp-port: 502
                 timeout: 1000ms
  disable-security-rules: yes
[admin@MikroTik] > /iot modbus set disabled=no
```

此外，當你希望允許 Modbus 用戶端使用 TCP(502)/IP 協定與 Modbus 伺服器通訊時，需要確保裝置的 IP+502 TCP 埠可訪問。從 LAN 訪問時，預設應被允許，因為沒有任何防火牆規則限制此類訪問。從外部訪問時（如果 "slave" 裝置從 WAN 側連線）- 預設不允許。你可以使用手冊查詢有關如何配置防火牆的資訊。不建議讓所有人都能透過 public/WAN 訪問；如果需要此類訪問，你應指定允許的公共“用戶端”的源 IP 地址（藉助防火牆規則內的 **src-address** 引數）。否則，你就是在讓所有人都能探測 Modbus 埠。

| 屬性 | 描述 |
| --- | --- |
| **disabled**（yes \| no；預設值：yes） | 啟用或停用 Modbus 功能。 |
| **hardware-port**（*list of string*；預設值：modbus） | 為服務分配埠。使用預設 "modbus" 埠。 |
| **tcp-port**（*integer:0..4294967295*；預設值：502） | 指定裝置將用於 Modbus TCP 通訊的 TCP 埠。 |
| **timeout**（*integer:0..1000*；預設值：1000） | 指定超時值，單位為 milliseconds。允許傳送 Modbus 請求並接收應答的最長時間。如果請求與應答之間的時間超過配置值，則返回 "failure"。 |
| **disable-security-rules**（yes \| no；預設值：yes） | 啟用或停用安全規則功能。 |
| **interframe-gap**（*integer;* 預設值：0） | Modbus 是“半雙工” → 同一時間要麼開啟 Tx 視窗，要麼開啟 Rx 視窗。按照標準，在 Tx 之後，必須跟隨一個 3.5-character（不同 baud rates 下會有所不同）的靜默間隔。但是，並非所有 Modbus Slave 裝置都遵循該規則，它們可能會更早或更晚開始 Tx。這可能導致資訊位丟失和通訊失敗。此引數可用於 "slave" 裝置不遵循標準規則的情況。`interframe-gap=0` 表示 `~4 ms` 的 3.5-character 間隔。 |
| **rx-switch-offset**（integer；） | 定義 Modbus 視窗從 Tx 切換到 Rx（引腳方向）的速度。 |

### 透過 Modbus RTU 傳送功能碼命令 {#sending-function-code-commands-via-modbus-rtu}

僅從 v**7.10.** 開始提供。這適用於 "**Modbus RTU**" 場景。此功能允許直接從 RouterOS 傳送功能碼命令（支援所有功能碼）。對於 "Modbus TCP" 場景，你必須使用第三方軟體來發送功能碼命令。

**子選單：** `/iot modbus transceive`

| 屬性 | 描述 |
| --- | --- |
| **address**（*integer:0..255*；預設值：） | 指定裝置地址或單元 ID。 |
| **function**（*integer:0..255*；預設值：） | 指定功能碼。例如：function=3 → Read Holding Register 功能碼；function=6 → Write Single Holding Register 功能碼。 |
| **data**（*string, max length 504*；預設值：） | 輸入資料字串，通常指定暫存器地址和要傳送的資料。例如：data=20000001 資料字串長度為 4 bytes。"0x2000" 是發往暫存器的命令（長度為 2 bytes），而 "0x0001"（長度為 2 bytes）是裝置地址。有關需要傳送的確切資料字串，請參閱 Modbus 裝置的規格。 |
| **values**（*integer:0..4294967295*；預設值：） | 傳送資料的另一種方式（參見上方的 **data** 引數）。在這種情況下，指定的每個值代表資料載荷/字串的 1 byte。例如：values=32,0,0,1 等同於 data=20000001 的輸出。32(dec)=0x20(hex)、0(dec)=0x00(hex)、0(dec)=0x00(hex)、1(dec)=0x01(hex) → 0x20000001。 |

使用 "transceive" 功能傳送功能碼 3 命令的示例：

```ros
/iot modbus transceive address=1 function=3 data=20000001 
   address: 1
  function: 3
      data: 01030164
    values: 100
      time: apr/27/2023 14:05:15
    status: ok
```

從上面的輸出可以看出，連線 Modbus 的裝置回覆了值 "100" 或資料 "01030164"（01→ 地址；03→ 功能碼；01→ bytes 數量；64（hex 轉 dec=100）→ 應答）。

### 透過 Modbus TCP 傳送功能碼 "3" 命令 {#sending-function-code-3-command-via-modbus-tcp}

專門針對功能碼 3（這不適用於任何其他功能碼），你可以使用如下所示的附加選項：

```ros
[admin@device] > {:local output [/iot modbus read-holding-registers slave-id=0x03 num-regs=0x1 reg-addr=0x0 as-value once];:put [($output->"values")]}
2349
[admin@device] > {:local output [/iot modbus read-holding-registers slave-id=0x03 num-regs=0x5 reg-addr=0x0 as-value once];:put [($output->"values")]}
2353;3;500;75;38
```

可以變化的引數是 "reg-addr"（資料字串中的地址）、"num-regs"（發往暫存器的資料字串命令/暫存器數量）和 "slave-id"（裝置地址或單元 ID）。它們都取決於所連線的 MODBUS 裝置支援哪些值。

### Modbus 安全 {#modbus-security}

從 v**7.12** 開始提供。

**子選單：** `/iot modbus security-rules`

Modbus 安全功能允許你設定特定規則，這些規則可以限制或允許對連線 Modbus 的裝置的訪問。**這僅適用於 Modbus TCP 通訊**（這些規則不會用於 Modbus RTU 通訊）。它可以允許特定 IP 範圍/網路訪問特定功能碼命令。

要啟用該功能，請輸入命令：

```ros
/iot modbus set disable-security-rules=no
```

啟用該功能後，新增規則本身。例如：

```ros
/iot modbus security-rules add ip-range=0.0.0.0/0 allowed-function-codes=3,6
```

上述規則將允許任何可能的 IP 地址向連線 Modbus 的裝置傳送功能碼 3 和 6 命令。其他所有內容都會受到限制。

| 屬性 | 描述 |
| --- | --- |
| **ip-range**（*Address/Netmask*；預設值：） | 指定允許傳送功能碼命令的 IP 地址範圍（或網路）。 |
| **allowed-function-codes**（*integer:0..4294967295*；預設值：） | 指定只能從配置的 ip-range 訪問的功能碼。 |
