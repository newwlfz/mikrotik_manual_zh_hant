---
sidebar_key: "management-tools/mac-server"
sidebar_position: 10
title: "MAC 伺服器"
sidebar_label: "MAC 伺服器"
description: "RouterOS 中的 MAC server 部分可用於配置 MAC Telnet、WinBox 和 Ping 伺服器，以便在路由器沒有 IP 地址的情況下訪問路由器。它允許將訪問限制為特定介面，並提供用於管理會話的工具，示例展示瞭如何啟用/停用 MAC Telnet 以及如何透過用戶端進行連線。"
tags:
  - 'mac-server'
  - 'mac-telnet'
  - 'mac-winbox'
source: https://manual.mikrotik.com/docs/7.24/management-tools/mac-server
captured_at: '2026-11-04T11:32:00+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MAC 伺服器部分允許你在 RouterOS 裝置上配置 MAC Telnet 伺服器、MAC WinBox 伺服器和 MAC Ping 伺服器。

MAC Telnet 用於提供對未設定 IP 地址的路由器的訪問。它的工作方式與 IP telnet 相同。MAC telnet 僅在兩臺 MikroTik RouterOS 路由器之間可行。

MAC WinBox 用於透過 MAC 地址提供對路由器的 WinBox 訪問。

MAC Ping 用於允許向路由器的 MAC 地址發起 MAC ping。

:::info
**MAC-server** 設定包含在 "system" 軟體包中。

:::

### MAC Telnet 伺服器 {#mac-telnet-server}

可以為屬於[介面列表](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)的特定介面設定 MAC Telnet 訪問：

```ros
[admin@device] /tool/mac-server/set allowed-interface-list=listBridge
[admin@device] /tool/mac-server/print
  allowed-interface-list: listBridge
```

在上例中，MAC Telnet 已針對介面列表 "listBridge" 進行配置，因此 MAC Telnet 將僅透過屬於該列表的介面工作（你可以向列表中新增多個介面）。

要停用 MAC Telnet 訪問，請執行以下命令（將 "allowed-interface-list" 設定為 "none"）：

```ros
[admin@device] /tool/mac-server/set allowed-interface-list=none
[admin@device] /tool/mac-server/print
  allowed-interface-list: none
```

可以使用以下命令檢查活動的 MAC Telnet 會話（裝置已接受的會話）：

```ros
[admin@device] > /tool/mac-server/sessions/print
Columns: INTERFACE, SRC-ADDRESS, UPTIME
#  INTERFACE  SRC-ADDRESS        UPTIME
0  ether5     64:D1:54:FB:E3:E6  17s 
```

#### MAC Telnet 用戶端 {#mac-telnet-client}

啟用 MAC Telnet 伺服器後，你可以使用另一臺 RouterOS 裝置透過 mac-telnet 用戶端連線到該伺服器：

```ros
[admin@device2] > tool mac-telnet B8:69:F4:7F:F2:E7    
Login: admin
Password: 
Trying B8:69:F4:7F:F2:E7...
Connected to B8:69:F4:7F:F2:E7

  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.1rc3 (c) 1999-2021       https://www.mikrotik.com/

Press F1 for help
  
[admin@device] > 
```

根據你的設定更改 MAC 地址，然後你應該就能進入伺服器的 CLI（如上例所示）。

:::tip
預設情況下，MAC Telnet 用戶端會嘗試透過所有活動介面訪問目標。這可能會產生不必要的流量。要將 MAC Telnet 用戶端限制到特定介面，請使用 `interface` 屬性（自 RouterOS v7.22 起可用）。例如：`/tool/mac-telnet 00:11:22:33:44:55 interface=ether1`

:::

#### MAC 掃描 {#mac-scan}

MAC 掃描功能會發現給定網路中所有支援 MAC telnet 協定的裝置。該命令要求你選擇一個應被掃描的介面：

```ros
[admin@Sw_Denissm] > /tool/mac-scan interface=all           
MAC-ADDRESS       ADDRESS                AGE
B8:69:F4:7F:F2:E7 192.168.69.1            26
2C:C8:1B:FD:F2:C3 192.168.69.3            56
```

在上例中，選擇了所有介面，掃描會無限執行，除非（按 "q"）停止。

你還可以新增 "duration" 引數，用於決定掃描應持續多長時間：

```ros
[admin@Sw_Denissm] > /tool/mac-scan interface=all duration=1
MAC-ADDRESS       ADDRESS                AGE
B8:69:F4:7F:F2:E7 192.168.69.1            48
2C:C8:1B:FD:F2:C3 192.168.69.3            17
```

在上例中，我們將 "duration" 引數設定為 1 秒。

### MAC WinBox 伺服器 {#mac-winbox-server}

與 MAC Telnet 相同，可以為屬於[介面列表](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)的特定介面設定 MAC WinBox 訪問：

```ros
[admin@device] > /tool/mac-server/mac-winbox/set allowed-interface-list=listBridge 
[admin@device] > /tool/mac-server/mac-winbox/print                   
  allowed-interface-list: listBridge
```

在上例中，MAC WinBox 訪問已針對介面列表 "listBridge" 進行配置，因此 MAC WinBox 將僅透過屬於該列表的介面工作。

要停用 MAC WinBox 訪問，請執行以下命令（將 "allowed-interface-list" 設定為 "none"）：

```ros
[admin@device] > /tool/mac-server/mac-winbox/set allowed-interface-list=none
[admin@device] > tool mac-server mac-winbox print                   
  allowed-interface-list: none
```

### MAC Ping 伺服器 {#mac-ping-server}

MAC Ping 伺服器可以設定為 "disabled" 或 "enabled"：

```ros
[admin@device] > /tool/mac-server/ping/print
  enabled: yes
```

你可以藉助以下命令啟用或停用 MAC ping（**enable=yes** → 啟用該功能；**enable=no** → 停用該功能）：

```ros
[admin@device] > /tool/mac-server/ping/set enabled=yes
[admin@device] > /tool/mac-server/ping/set enabled=no
```

啟用 MAC Ping 後，同一廣播域中的其他主機可以使用 ping 工具 ping 該 MAC 地址。例如，你可以執行以下命令檢查 MAC ping 結果：

```ros
[admin@device] > /ping 00:0C:42:72:A1:B0
HOST                                    SIZE  TTL TIME  STATUS                                         
00:0C:42:72:A1:B0                       56        0ms  
00:0C:42:72:A1:B0                       56        0ms  
    sent=2 received=2 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms 
```

:::warning
如果停用 **MAC server ping** 功能，主機的 **ARP ping** 功能也會被停用。

:::

:::tip
預設情況下，MAC ping 會嘗試透過所有活動介面訪問目標。如果目標可透過多個介面訪問，這可能會產生不必要的流量和重複回覆。要將 MAC ping 限制到特定介面，請使用介面選擇器（在 MAC 地址後追加 `%` 以及介面名稱）。例如：`/ping 00:11:22:33:44:55%ether1`

:::
