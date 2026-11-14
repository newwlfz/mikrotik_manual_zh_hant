---
sidebar_key: "management-tools/serial-console"
sidebar_position: 5
title: "序列控制檯"
sidebar_label: "序列控制檯"
description: "Serial Console 和 Terminal 工具支援透過序列埠進行直接裝置通訊，用於初始配置或恢復配置，最多支援 132 臺裝置。本頁介紹用於硬體流控制的零調變解調器電纜配置，包括無握手以及具有部分或完整握手能力的選項。"
tags:
  - 'serial-console'
  - 'null-modem-cables'
  - 'rs232'
source: https://manual.mikrotik.com/docs/7.24/management-tools/serial-console
captured_at: '2026-11-04T11:32:08+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

序列控制檯和序列終端是用於與透過序列埠互連的裝置和其他系統進行通訊的工具。序列終端可用於監控和配置許多裝置——包括調變解調器、網路裝置（包括 MikroTik 路由器），以及任何可連線到序列（非同步）埠的裝置。

序列控制檯功能用於配置直接訪問式配置設施（顯示器和鍵盤以及序列埠），這些設施主要用於初始配置或恢復配置。連線兩臺主機（例如兩臺 PC 或兩臺路由器；而不是調變解調器）需要使用專用的零調變解調器電纜。請注意，從另一臺計算機訪問序列控制檯需要使用終端模擬程式（例如 Windows 上的 HyperTerminal 或 Linux 上的 minicom）。路由器序列埠的預設設定為 115200 bits/s（x86 的預設值為 9600 bits/s）、8 個數據位、1 個停止位、無奇偶校驗、硬體 (RTS/CTS) 流控制。

一些客戶描述了序列終端（管理側）功能會很有用的情況：

- 在山頂上，MikroTik 無線安裝旁邊有無法帶內管理（透過 IP 網路使用 telnet）的裝置（包括交換器和 Cisco 路由器）。
- 透過序列埠監控氣象報告裝置。
- 連線到需要透過序列連線進行監控和管理的高速微波調變解調器。

使用 MikroTik 的 serial-terminal 功能，最多可以監控和控制 132 臺（甚至可能更多）裝置。

## 序列控制檯連線 {#serial-console-connections}

裝置之間的序列通訊使用 RS232 完成。它是計算機世界中最古老、最廣泛的通訊方法之一。它曾用於與調變解調器或其他 DTE/DCE 外圍裝置通訊。在現代，序列通訊的主要用途是 DTE/DTE 通訊（資料終端裝置），例如使用零調變解調器電纜。零調變解調器電纜有幾種型別，其中一些可能完全無法與 RouterBoard 配合使用。

### 無握手的零調變解調器 {#null-modem-without-handshake}

這種電纜完全不使用握手引腳：

| 側1 (DB9f) | 側2 (DB9f) | 功能 |
| --: | --: | :-- |
| 2 | 3 | Rx ← Tx |
| 3 | 2 | Tx → Rx |
| 5 | 5 | GND |

它允許在交叉連線的 Rx/Tx 線路上進行僅資料傳輸。這種型別的電纜無法使用硬體流控制。執行流控制的唯一方式是使用 XOFF 和 XON 字元進行軟體流控制。

### 帶回環握手的零調變解調器 {#null-modem-with-loopback-handshake}

第一種電纜的問題在於，當連線到啟用了硬體流控制的裝置時，軟體在檢查調變解調器訊號線時可能會掛起。

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

這種電纜無法使用硬體流控制。此外，如果遠端軟體不向 DTR 輸出傳送其自身的就緒訊號，通訊將會掛起。

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

下面的彙總表可幫助您為應用選擇正確的電纜。

|  | 無握手 | 迴環握手 | 部分握手 | 完全握手 |
| :-- | :-- | :-- | :-- | :-- |
| 埠功能受限的 RouterBoard | Y | Y | N\* | N |
| 具備完整功能的 RouterBoard | Y | Y | Y | N |

\* - 僅在硬體流控制停用時可能有效

|  | 無握手 | 迴環握手 | 部分握手 | 完全握手 |
| :-- | :-- | :-- | :-- | :-- |
| 僅軟體流控制 | Y | Y\* | Y\*\* | Y\*\* |
| 低速 DTE/DCE 相容硬體流控制 | N | Y | Y\* | N |
| 高速 DTE/DCE 相容硬體流控制 | N | Y | Y\*\* | N |
| 使用特殊軟體的高速通訊 | N | N | Y\* | Y |

\* - 可作為替代方案使用

\*\* - 可以工作，但不推薦

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

RouterOS 允許使用 `/system/serial-terminal` 命令與透過序列埠連線到路由器的裝置和其他系統通訊。所有鍵盤輸入都會轉發到序列埠，來自埠的所有資料都會輸出到所連線的裝置。

首先，必須有一個可用的序列埠。如果裝置只有一個序列埠（例如所有 RouterBoard、WRAP/ALIX 板等），則必須停用此序列埠上的系統控制檯，才能將其用作**序列終端**來連線其他裝置（交換器、調變解調器等）：

```ros
/system/console/disable 0
```

請務必只停用控制檯，而不是刪除它；因為如果實際刪除，RouterOS 會在下次重啟後重新建立該控制檯。

:::danger
**請注意，有一些注意事項需要了解！請花時間理解這些限制，以避免將裝置連線到 RouterBoard 上的序列埠時發生異常情況：**

- 透過如上所述重新配置 RouterBoard 上的 Serial0 埠，您將失去對 RouterOS 的序列控制檯訪問許可權。這意味著，如果您再也無法透過網路訪問 RouterBoard，甚至可能需要重設其整個配置才能重新獲得訪問許可權。
- 重啟 RouterBoard 時，引導載入程式 (RouterBOOT) 將始終使用序列控制檯（RouterBoard 上的 Serial0）傳送一些啟動訊息，並提供對 RouterBOOT 選單的訪問。

  序列埠向已連線裝置輸出文字可能會使所連線的裝置產生混淆。此外，在標準配置中，按下**任意**鍵即可進入 RouterBOOT 選單。因此，如果序列裝置在啟動期間向 RouterBoard 的序列埠傳送任何字元，RouterBoard 將進入 RouterBOOT 選單，並且除非您手動干預，否則將**不會**啟動 RouterOS！

  您可以重新配置 RouterBOOT，使其僅在收到 <kbd>Delete</kbd> 字元時進入 RouterBOOT 選單——使用此設定可降低重啟時路由器卡住的可能性！

  或者，如果使用較新版本，可以使用 ["Silent boot"](../getting-started/installation-and-upgrade/routerboot.md) 功能來抑制序列介面上的任何輸出，包括移除啟動聲音。

:::

接下來，您必須根據所連線裝置的序列埠設定來配置序列埠。使用以下命令將序列埠設定為 19200 Baud 8N1。您需要使用哪些設定取決於所連線的裝置：

```ros
/port/set serial0 baud-rate=19200 data-bits=8 parity=none stop-bits=1
```

您也可以讓 RouterOS 透過設定以下內容來猜測所需的波特率

```ros
/port/set serial0 baud-rate=auto
```

如果尚未連線裝置，現在就可以連線了。通常，您需要使用[零調變解調器電纜](#serial-console-connections)（相當於乙太網的交叉電纜）。現在可以開始了：

```ros
/system/serial-terminal serial0
```

這將使您能夠訪問連線到 Serial0 埠的裝置。*<kbd>Control</kbd>+<kbd>A</kbd>* 是字首鍵，這意味著您將進入一個小型“選單”。如果需要將 *<kbd>Control</kbd>+<kbd>A</kbd>* 字元傳送到遠端裝置，請按兩次 *<kbd>Control</kbd>+<kbd>A</kbd>*。

如果要退出與序列裝置的連線，請鍵入 *<kbd>Control</kbd>+<kbd>A</kbd>*，然後按 ***Q***。這將返回到 RouterOS 控制檯。

:::danger
不要以錯誤的速度連線裝置，並避免轉儲二進位制資料。
:::

## 特殊登入 {#special-login}

特殊登入可用於透過開啟 telnet/ssh 會話訪問透過序列電纜連線的另一臺裝置（例如交換器），該會話會讓您直接進入該裝置（無需先登入 RouterOS）。

在本演示中，我們將使用兩臺 RouterBoard 和一臺 PC。

![](/img/060c953cc7f1d5cd.webp)

路由器 R1 和 R2 透過序列電纜連線，PC 透過乙太網連線到 R1。假設我們想透過序列電纜從 PC 訪問路由器 R2。為此，必須在 R1 上設定序列介面代理。這可以透過名為 **special-login** 的功能來完成。

:::info
預設情況下，控制檯繫結到序列埠。
:::

第一步是解除控制檯與序列埠的繫結，只需停用 `/system/console` 選單中的條目：

```ros
[admin@MikroTik] /system/console> print
Flags: X - disabled, U - used, F - free
 #   PORT                                                                    TERM
 0 X serial0                                                                 vt102
```

下一步是新增一個新使用者，在本例中為 *serial*，並將其繫結到序列埠

```ros
[admin@MikroTik] > /user/add name=serial group=full
[admin@MikroTik] > /special-login/add user=serial port=serial0 disabled=no
[admin@MikroTik] > /special-login/print
Flags: X - disabled
 #   USER                                                                    PORT
 0   serial                                                                  serial0
```

現在可以從 PC 訪問 R2 了。

```ros
maris@bumba:/$ ssh serial@10.1.101.146

[Ctrl-A is the prefix key]
R2 4.0beta4
R2 Login:

[admin@R2] >
```

要退出特殊登入模式，請按 <kbd>Ctrl</kbd>+<kbd>A</kbd> 和 Q

```ros
[admin@MikroTik] >
[Q - quit connection]      [B - send break]
[A - send Ctrl-A prefix]   [R - autoconfigure rate]

Connection to 10.1.101.146 closed.
```

:::danger
路由器重啟並連線序列電纜後，路由器可能會卡在 Bootloader 主選單。
:::

要解決此問題，需要將訪問 bootloader 主選單的按鍵從 `<any>` 改為 `<delete>`：

- 進入 bootloader 選單。
- 按 'k' 進入啟動鍵選項。
- 按 '2' 將按鍵改為 `<delete>`。

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
