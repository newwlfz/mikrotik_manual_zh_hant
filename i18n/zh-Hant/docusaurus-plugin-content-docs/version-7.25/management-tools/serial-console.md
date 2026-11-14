---
sidebar_key: "management-tools/serial-console"
sidebar_position: 6
title: "序列控制檯"
sidebar_label: "序列控制檯"
description: "Serial Console 和 Terminal 工具可透過序列埠實現裝置直接通訊，用於初始配置或恢復配置，最多支援 132 臺裝置。本頁說明用於硬體流控的 null-modem 電纜配置，包括無握手以及具有部分或完全握手能力的選項。"
tags:
  - 'serial-console'
  - 'null-modem-cables'
  - 'rs232'
source: https://manual.mikrotik.com/docs/7.25/management-tools/serial-console
captured_at: '2026-11-04T11:19:48+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

序列控制檯和序列終端是用於與透過序列埠互連的裝置和其他系統進行通訊的工具。序列終端用於監控和配置許多裝置——包括調變解調器、網路裝置（包括 MikroTik 路由器），以及任何可連線到序列（非同步）埠的裝置。

序列控制檯功能用於配置直接訪問配置設施（顯示器/鍵盤和序列埠），這些設施主要用於初始配置或恢復配置。連線兩臺主機（例如兩臺 PC 或兩臺路由器；不是調變解調器）需要一根特殊的零調變解調器電纜。從另一臺計算機訪問序列控制檯需要終端模擬程式（例如 Windows 上的 HyperTerminal 或 Linux 上的 minicom）。路由器序列埠的預設設定為 115200 bits/s（x86 的預設值為 9600 bits/s）、8 個數據位、1 個停止位、無奇偶校驗、硬體（RTS/CTS）流控。

序列終端（管理端）功能在以下情況下很有用：

- 在山頂上，MikroTik 無線安裝旁邊有無法帶內管理（透過 IP 網路使用 telnet）的裝置（包括交換器和 Cisco 路由器）。
- 透過序列埠監控氣象報告裝置。
- 連線到需要透過序列連線進行監控和管理的高速微波調變解調器。

藉助 MikroTik 的序列終端功能，最多可以監控和控制 132 臺（甚至更多）裝置。

## 序列控制檯連線 {#serial-console-connections}

裝置之間的序列通訊透過 RS232 完成。它是計算機領域中最古老、最廣泛使用的通訊方法之一。它曾用於與調變解調器或其他外圍裝置 DTE/DCE 進行通訊。在現代，序列通訊的主要用途是 DTE/DTE 通訊（資料終端裝置），例如使用零調變解調器電纜。零調變解調器電纜有多種型別，其中一些可能根本無法與 RouterBoards 配合使用。

### 無握手的零調變解調器 {#null-modem-without-handshake}

此電纜完全不使用握手引腳：

| 側1 (DB9f) | 側2 (DB9f) | 功能 |
| --: | --: | :-- |
| 2 | 3 | Rx ← Tx |
| 3 | 2 | Tx → Rx |
| 5 | 5 | GND |

它允許在交叉連線的 Rx/Tx 線路上僅傳輸資料。此類電纜無法進行硬體流控。執行流控的唯一方式是使用 XOFF 和 XON 字元進行軟體流控。

### 帶回環握手的零調變解調器 {#null-modem-with-loopback-handshake}

無握手電纜的問題在於，當連線到啟用了硬體流控的裝置時，軟體在檢查調變解調器訊號線時可能會掛起。

帶回環握手的零調變解調器電纜解決了這個問題；其主要目的是欺騙設計良好的軟體，使其認為有可用的握手：

| 側1 (DB9f) | 側2 (DB9f) | 功能 |
| :-- | :-- | :-- |
| 2 | 3 | Rx ← Tx |
| 3 | 2 | Tx → Rx |
| 5 | 5 | GND |
| 1+4+6 | - | DTR → CD + DSR |
| - | 1+4+6 | DTR → CD + DSR |
| 7+8 | - | RTS → CTS |
| - | 7+8 | RTS → CTS |

此電纜無法進行硬體流控。此外，如果遠端軟體不向 DTR 輸出傳送其自身的就緒訊號，通訊就會掛起。

### 帶部分握手的零調變解調器 {#null-modem-with-partial-handshake}

這種電纜可在啟用流控制時使用，同時不會與 DTE/DCE 通訊中使用流控制的原有方式不相容。

不建議將這種型別的電纜與 RouterOS 一起使用。

| 側1 (DB9f) | 側2 (DB9f) | 功能 |
| :-- | :-- | :-- |
| 1 | 7+8 | RTS2 → CTS2 + CD1 |
| 2 | 3 | Rx ← Tx |
| 3 | 2 | Tx → Rx |
| 4 | 6 | DTR → DSR |
| 5 | 5 | GND |
| 6 | 4 | DSR ← DTR |
| 7+8 | 1 | RTS1 → CTS1 + CD2 |

### 帶完全握手的零調變解調器 {#null-modem-with-full-handshake}

用於特殊軟體，不應與 RouterOS 一起使用。

| 側1 (DB9f) | 側2 (DB9f) | 功能 |
| --: | --: | :-- |
| 2 | 3 | Rx ← Tx |
| 3 | 2 | Tx → Rx |
| 4 | 6 | DTR → DSR |
| 5 | 5 | GND |
| 6 | 4 | DSR ← DTR |
| 7 | 8 | RTS → CTS |
| 8 | 7 | CTS ← RTS |

### 零調變解調器相容性 {#null-modem-compatibility}

以下彙總表可幫助您為應用選擇合適的電纜。

|  | 無握手 | 迴環握手 | 部分握手 | 完全握手 |
| :-- | :-- | :-- | :-- | :-- |
| 埠功能受限的 RouterBoard | Y | Y | N\* | N |
| 具備完整功能的 RouterBoard | Y | Y | Y | N |

\* - 僅在硬體流控制停用時可能有效

|  | 無握手 | 環回握手 | 部分握手 | 完全握手 |
| :-- | :-- | :-- | :-- | :-- |
| 僅軟體流控 | Y | Y\* | Y\*\* | Y\*\* |
| 低速 DTE/DCE 相容硬體流控 | N | Y | Y\* | N |
| 高速 DTE/DCE 相容硬體流控 | N | Y | Y\*\* | N |
| 使用特殊軟體進行高速通訊 | N | N | Y\* | Y |

\* - 可作為替代方案

\*\* - 可用但不推薦

### RJ45 型別序列埠 {#rj45-type-serial-port}

這種埠用於 RouterBOARD 2011、3011、4011、CCR1072、CCR1036 r2、CCR2xxx 和 CRS 系列裝置，有時稱為“Cisco 風格”序列埠。

#### RJ45 到 DB9 電纜引腳定義 {#rj45-to-db9-cable-pinout}

![](/img/3f6e76a55153f3e0.webp)

| 訊號 | 控制檯埠 (DTE) RJ-45 | RJ-45 反轉電纜 RJ-45 引腳 | 介面卡 DB-9 引腳 | 介面卡 DB-25 引腳 | 訊號 |
| :-- | --: | --: | --: | --: | :-- |
| RTS | 1 | 8 | 8 | 5 | CTS |
| DTR | 2 | 7 | 6 | 6 | DSR |
| TxD | 3 | 6 | 2 | 3 | RxD |
| 接地 | 4 | 5 | 5 | 7 | 接地 |
| Ground | 5 | 4 | 5 | 7 | Ground |
| RxD | 6 | 3 | 3 | 2 | TxD |
| DSR | 7 | 2 | 4 | 20 | DTR |
| CTS | 8 | 1 | 7 | 4 | RTS |

### RB M33G 附加序列排針 {#rb-m33g-additional-serial-header}

對於 RBM33G，可以將附加序列排針連線到 GPIO 引腳 U3\_RXD、GND、U3\_TXD 和 3V3

### CCR 序列排針 {#ccr-serial-header}

Cloud Core Router 系列裝置在 PCB 板上有一個序列排針，稱為 J402 或 100

該聯結器的引腳排列如下：

![](/img/ca319263debe6708.webp)

## 序列終端用法 {#serial-terminal-usage}

RouterOS 允許使用 [`/system/serial-terminal`](../cli-reference/system/serial-terminal.md) 命令，與透過序列埠連線到路由器的裝置和其他系統進行通訊。所有鍵盤輸入都會轉發到序列埠，埠中的所有資料都會輸出到連線的裝置。

首先，必須有一個空閒的序列埠。如果裝置只有一個序列埠（例如所有 RouterBoards、WRAP/ALIX 板等），則必須停用此序列埠上的系統控制檯，才能將其用作 **序列終端** 來連線其他裝置（例如交換器、調變解調器）：

```ros
/system/console/disable 0
```

請確保只是停用控制檯，而不是刪除它，因為如果實際刪除它，RouterOS 會在下次重啟後重新建立控制檯。

:::danger
將裝置連線到 RouterBoard 上的序列埠時需要注意以下事項：

- 如前所述，在 RouterBoard 上重新配置埠 Serial0 後，您將失去對 RouterOS 的序列埠控制檯訪問許可權。這意味著，如果您無法透過網路訪問 RouterBoard，您可能必須重設整個配置才能重新獲得訪問許可權。
- 重新啟動 RouterBoard 時，引導載入程式（RouterBOOT）始終使用序列埠控制檯（RouterBoard 上的 Serial0）傳送一些啟動訊息，並提供對 RouterBOOT 選單的訪問。

  從序列埠輸出到所連線裝置的文字可能會使您連線的裝置混淆。此外，在標準配置中，您可以透過按 **ANY** 鍵進入 RouterBOOT 選單。因此，如果您的序列埠裝置在啟動期間向 RouterBoard 的序列埠傳送任何字元，RouterBoard 將進入 RouterBOOT 選單，並且除非您手動干預，否則**不會**啟動 RouterOS！

  您可以重新配置 RouterBOOT，使其僅在收到 <kbd>Delete</kbd> 字元時才進入 RouterBOOT 選單——使用此設定可降低在重新啟動時路由器卡住的機率！

  或者，對於較新版本，可以使用 ["Silent boot"](../getting-started/installation-and-upgrade/routerboot.md) 功能來抑制序列埠介面上的任何輸出，包括移除啟動聲音。
:::

接下來，必須根據所連線裝置的序列埠設定來配置您的序列埠。透過以下命令，可將序列埠設定為 19200 Baud 8N1。需要使用哪些設定取決於您連線的裝置：

```ros
/port/set serial0 baud-rate=19200 data-bits=8 parity=none stop-bits=1
```

您也可以讓 RouterOS 透過設定以下內容來猜測所需的波特率

```ros
/port/set serial0 baud-rate=auto
```

如果尚未連線裝置，現在就可以連線了。通常，您需要一根[零調變解調器電纜](#serial-console-connections)（與乙太網交叉電纜相同）。現在可以開始了：

```ros
/system/serial-terminal serial0
```

這樣您就可以訪問連線到 Serial0 埠的裝置。<kbd>Control</kbd>+<kbd>A</kbd> 是字首鍵，這意味著您會進入一個小型“選單”。如果需要將 <kbd>Control</kbd>+<kbd>A</kbd> 字元傳送到遠端裝置，請按兩次 <kbd>Control</kbd>+<kbd>A</kbd>。

如果要退出與序列裝置的連線，請按 <kbd>Control</kbd>+<kbd>A</kbd>，然後按 <kbd>Q</kbd>。這將返回到 RouterOS 控制檯。

:::danger
不要以錯誤的速度連線裝置，並避免轉儲二進位制資料。
:::

## 特殊登入 {#special-login}

特殊登入可用於訪問透過序列電纜連線的另一臺裝置（例如交換器），方法是開啟一個 telnet/ssh 會話，讓您直接進入該裝置（無需先登入 RouterOS）。

本演示使用兩臺 RouterBoards 和一臺 PC。

![](/img/060c953cc7f1d5cd.webp)

路由器 R1 和 R2 透過序列電纜連線，PC 透過乙太網連線到 R1。要從 PC 透過序列電纜訪問路由器 R2，必須在 R1 上設定序列介面代理。這透過使用名為 **special-login** 的功能來完成。

:::info
預設情況下，控制檯繫結到序列埠。
:::

首先，透過停用 [`/system/console`](../cli-reference/system/console/index.md) 選單中的條目來解除控制檯與序列埠的繫結：

```ros
[admin@MikroTik] /system/console> print
Flags: X - disabled, U - used, F - free
 #   PORT                                                                    TERM
 0 X serial0                                                                 vt102
```

接下來，新增一個新使用者，在此示例中為 *serial*，並將其繫結到序列埠：

```ros
[admin@MikroTik] > /user/add name=serial group=full
[admin@MikroTik] > /special-login/add user=serial port=serial0 disabled=no
[admin@MikroTik] > /special-login/print
Flags: X - disabled
 #   USER                                                                    PORT
 0   serial                                                                  serial0
```

現在可以從 PC 訪問 R2。

```ros
maris@bumba:/$ ssh serial@10.1.101.146

[Ctrl-A is the prefix key]
R2 4.0beta4
R2 Login:

[admin@R2] >
```

要退出特殊登入模式，請按 <kbd>Control</kbd>+<kbd>A</kbd> 和 <kbd>Q</kbd>：

```ros
[admin@MikroTik] >
[Q - quit connection]      [B - send break]
[A - send Ctrl-A prefix]   [R - autoconfigure rate]

Connection to 10.1.101.146 closed.
```

:::danger
路由器重啟後，如果連線了序列電纜，路由器可能會卡在 Bootloader 主選單。
:::

要解決此問題，需要將進入 bootloader 主選單的方式從按 **任意** 鍵改為按 <kbd>Delete</kbd>：

- 進入 bootloader 選單。
- 選擇 `k` 進入啟動鍵選項。
- 選擇 `2` 將按鍵改為 <kbd>Delete</kbd>。

```
What do you want to configure?
d - boot delay
k - boot key
s - serial console
n - silent boot
o - boot device
u - cpu mode
f - cpu frequency
r - reset booter configuration
e - format nand
g - upgrade firmware
i - board info
p - boot protocol
b - booter options
t - call debug code
l - erase license
x - exit setup
your choice: k - boot key

Select key which will enter setup on boot:
 * 1 - any key
   2 - <Delete> key only

your choice: 2

```
