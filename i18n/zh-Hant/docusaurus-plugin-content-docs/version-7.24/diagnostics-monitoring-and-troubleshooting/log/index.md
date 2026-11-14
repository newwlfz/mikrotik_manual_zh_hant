---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/log/index"
sidebar_position: 2
title: "日誌"
sidebar_label: "日誌"
description: "本節概述了 MikroTik RouterOS 的日誌記錄功能，涵蓋如何使用 `/log` 選單即時檢視和過濾日誌訊息，以及透過 `/system/logging` 將日誌轉發到外部系統的詳細配置選項。"
tags:
  - 'logging'
  - 'system-management'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/log
captured_at: '2026-11-04T11:27:59+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹日誌匯出和整合示例。可使用本節內容將 RouterOS 日誌轉發到 Elasticsearch 等外部系統。

<DocCardList />

RouterOS 能夠記錄各種系統事件和狀態資訊。日誌可以儲存在路由器記憶體（RAM）、磁碟、檔案中，透過電子郵件傳送，甚至傳送到遠端 syslog 伺服器。

[影片：日誌記錄基礎](http://youtube.com/watch?v=E-QAhaWtsnU)

## 日誌訊息 {#log-messages}

**子選單：** `/log`

路由器本地記憶體中儲存的所有訊息都可以從 `/log` 選單列印。每個條目包含事件發生的時間和日期、該訊息所屬的主題以及訊息本身。

```ros
[admin@MikroTik] /log> print 
1970-01-02 02:00:09 system,info router rebooted 
sep/15 09:54:33 system,info,account user admin logged in from 10.1.101.212 via winbox 
sep/15 12:33:18 system,info item added by admin 
sep/15 12:34:26 system,info mangle rule added by admin 
sep/15 12:34:29 system,info mangle rule moved by admin 
sep/15 12:35:34 system,info mangle rule changed by admin 
sep/15 12:42:14 system,info,account user admin logged in from 10.1.101.212 via telnet 
sep/15 12:42:55 system,info,account user admin logged out from 10.1.101.212 via telnet 
01:01:58 firewall,info input: in:ether1 out:(none), src-mac 00:21:29:6d:82:07, proto UDP, 
10.1.101.1:520->10.1.101.255:520, len 452
```

如果在新增日誌條目的同一天列印日誌，則僅顯示時間。在上面的示例中可以看到，第二條訊息是在當前年份的 sep/15 新增的（未新增年份），而最後一條訊息是今天新增的，因此只顯示時間。

*Print* 命令接受多個引數，可用於檢測新日誌條目、僅列印必要訊息等。

例如，以下命令將列印所有主題之一為 info 的日誌訊息，並持續檢測新日誌條目，直到按下 <kbd>Control</kbd>+<kbd>C</kbd>。

```ros
[admin@MikroTik] /log > print follow where topics~".info"
12:52:24 script,info hello from script
-- Ctrl-C to quit.
```

在此示例中，它將僅列印 dhcp info 訊息：

```ros
[admin@MikroTik] /log/print where topics~"dhcp.info"
11:42:32 dhcp,info defconf deassigned 192.168.88.37 for B0:E4:5C:27:EF:F2 Samsung
11:42:32 dhcp,info defconf assigned 192.168.88.37 for B0:E4:5C:27:EF:F2 Samsung
```

如果 print 處於 follow 模式，您可以按鍵盤上的“空格”插入分隔符：

```ros
[admin@MikroTik] /log > print follow where topics~".info"
12:52:24 script,info hello from script

= = = = = = = = = = = = = = = = = = = = = = = = = = =

-- Ctrl-C to quit.
```

## 日誌記錄配置 {#logging-configuration}

**子選單：** `/system/logging`

| 屬性 | 描述 |
| :--- | :--- |
| **action** (*name*; Default: **memory**) | 指定系統預設動作之一，或 actions 選單中列出的使用者自定義動作。 |
| **prefix** (*string*; Default: none) | 新增到日誌訊息開頭的字首。 |
| **regex** (*string*; Default: none) | 用於匹配日誌訊息的正則表示式。如果正則表示式不匹配，則不會執行該動作，即使已為該主題配置日誌記錄也是如此。 |
| **topics** (*account, acme-client, amt, async, backup, bfd, bgp, bridge, calc, caps, certificate, clock, container, critical, ddns, debug, dhcp, discover, disk, dns, dot1x, dude, e-mail, error, event, evpn, fetch, firewall, gps, gsm, health, hotspot, igmp-proxy, info, interface, ipsec, iscsi, isdn, isis, kvm, l2tp, lora, ldp, lte, manager, mme, mpls, mqtt, mvrp, natpmp, netwatch, ntp, ospf, ovpn, packet, pim, poe-in, poe-out, ppp, pppoe, pptp, ptp, queue, radvd, radius, raw, read, rip, route, rpki, rproxy, rsvp, script, sertcp, simulator, smb, snmp, socksify, ssh, ssld, sstp, state, store, stp, system, telephony, tftp, timer, tr069, update, upnp, ups, vpls, vrrp, warning, watchdog, web-proxy, wiliot, wireguard, wireless, write, zerotier*; Default: **info**) | 記錄與指定主題或主題列表匹配的所有訊息。在主題前使用 **!** 字元可排除匹配的訊息。例如，要記錄不包含封包詳情的 NTP 偵錯訊息：`/system/logging/add topics=ntp,debug,!packet` |

### 操作 {#actions}

**子選單：** `/system/logging/action`

| 屬性 | 描述 |
| :--- | :--- |
| **add-topics-string** (*yes\|no*; 預設值： **no**) |  |
| **cef-event-delimiter** (string; Default: **\r\n**) | 該選項幫助遠端 syslog 區分已傳送批次中的各個事件 |
| **check-certificate** (*yes\|no*; Default: no) | 在遠端動作使用 TLS 型別日誌記錄時是否檢查伺服器證書。 |
| **disk-file-count** (*integer [1..65535]*; Default: **2**) | 指定用於儲存日誌訊息的檔案數量，僅在 action=disk 時適用 |
| **disk-file-name** (*string*; Default: **log**) | 用於儲存日誌訊息的檔名，僅在 action=disk 時適用 |
| **disk-lines-per-file** (*integer [1..65535]*; Default: **100**) | 指定檔案以行數表示的最大大小，僅在 action=disk 時適用 |
| **disk-stop-on-full** (*yes\|no*; Default: **no**) | 達到指定的 disk-lines-per-file 和 disk-file-count 數量後是否停止將日誌訊息儲存到磁碟，僅在 action=disk 時適用 |
| **email-cc (*string*; Default: )** | 日誌作為抄送傳送到的電子郵件地址，僅在 action=email 時適用 |
| **email-start-tls** (*yes \| no*; Default: **no**) | 傳送電子郵件時是否使用 tls，僅在 action=email 時適用 |
| **email-to** (*string*; Default: ) | 日誌傳送到的電子郵件地址，僅在 action=email 時適用 |
| **memory-lines** (*integer [1..65535]*; Default: **1000**) | 本地記憶體緩衝區中的記錄數，僅在 action=memory 時適用 |
| **memory-stop-on-full** (*yes\|no*; Default: **no**) | 達到指定的 memory-lines 數量後是否停止將日誌訊息儲存到本地緩衝區 |
| **name** (*string*; Default: ) | 動作的名稱。當 target=memory 時，該名稱也用作特定記憶體緩衝區的識別符號。可以建立多個 target=memory 的動作，每個動作都將日誌儲存在其各自獨立的緩衝區中。 |
| **remember** (*yes\|no*; Default: ) | 是否保留尚未在控制檯中顯示的日誌訊息，僅在 action=echo 時適用 |
| **remote-log-format** (*cef, default, syslog*; Default: **default**) | 傳送到遠端例項的日誌格式：cef - 日誌以 CEF 格式傳送；default - 日誌按原樣傳送；syslog - 日誌以 BSD-syslog 格式傳送 |
| **remote-port** (*integer [1..65535]*; Default: **514**) | 遠端日誌記錄伺服器的 UDP 埠（地址透過 **remote** 屬性配置）。 |
| **remote-protocol** (*tcp / udp / tls*; Default: **udp**) | 遠端日誌訊息使用的協定，TCP 和 TLS 僅適用於 CEF remote-log-format，對於 syslog 將始終使用 UDP，即使已設定 TCP / TLS |
| **script** |  |
| **src-address** (*IP address*; Default: **0.0.0.0**) | 向遠端伺服器傳送封包時使用的源地址 |
| **syslog-facility** (*auth, authpriv, cron, daemon, ftp, kern, local0, local1, local2, local3, local4, local5, local6, local7, lpr, mail, news, ntp, syslog, user, uucp*; 預設值： **daemon**) |  |
| **syslog-severity** (*alert, auto, critical, debug, emergency, error, info, notice, warning*; Default: **auto**) | RFC 3164 中定義的嚴重性級別指示符：Emergency：系統不可用；Alert：必須立即採取措施；Critical：嚴重狀況；Error：錯誤狀況；Warning：警告狀況；Notice：正常但重要的情況；Informational：資訊性訊息；Debug：偵錯級別訊息 |
| **syslog-time-format** (*bsd-syslog, iso8601*; Default: **bsd-syslog**) | 訊息的時間日誌格式 |
| **target** (*disk, echo, email, memory, remote, script*; Default: **memory**) | 日誌訊息的儲存設施或目標：disk - 日誌儲存到硬碟；echo - 日誌顯示在控制檯螢幕上；email - 日誌透過電子郵件傳送；memory - 日誌儲存在本地記憶體緩衝區或多個獨立緩衝區（RAM 檔案）中；remote - 日誌傳送到遠端主機；script - 當日志訊息匹配規則時，從 /system/script/ 執行指令碼。指令碼接收兩個變數：topics（日誌主題字串）和 message（日誌訊息內容）。 |
| **vrf** (*name*; Default: **main**) | 設定遠端日誌記錄用於傳出連線的 VRF，僅在 target=remote 時適用。該設定自 RouterOS 7.19 版本起可用。 |

### 建立獨立的記憶體日誌緩衝區 {#create-separate-memory-logging-buffers}

就像為不同備註使用不同文字檔案一樣，這些獨立的記憶體緩衝區允許您將特定型別的日誌訊息（基於主題）定向到記憶體中的不同儲存區域。

- **隔離：** 傳送到 `buffer_A` 的日誌與傳送到 `buffer_B` 的日誌完全分離。
- **獨立檢視：** 可以使用 `/log/print where buffer=buffer_name` 一次只檢視一個緩衝區的內容。
- **定向清除：** 可以使用 `/system/logging/action/clear action=buffer_name` 清除特定緩衝區的內容，而不會影響儲存在任何其他記憶體緩衝區中的日誌。

這可以更好地組織和控制儲存在記憶體中的日誌，尤其是在偵錯或監控時，而不會將它們全部混入單一的預設記憶體日誌中。

**子選單：** `/system/logging/action/clear`

從 7.20\_ab244 開始，可以使用以下命令清除記憶體日誌（target=memory）：**`/system/logging/action/clear` action=\<`logging` 动作名称>**  
  
主題

 每個日誌條目都有一個主題，用於描述日誌訊息的來源。一條日誌訊息可以分配多個主題。例如，OSPF 偵錯日誌有四個不同的主題：route、ospf、debug 和 raw。

```ros
11:11:43 route,ospf,debug SEND: Hello Packet 10.255.255.1 -> 224.0.0.5 on lo0 
11:11:43 route,ospf,debug,raw PACKET: 
11:11:43 route,ospf,debug,raw 02 01 00 2C 0A FF FF 03 00 00 00 00 E7 9B 00 00 
11:11:43 route,ospf,debug,raw 00 00 00 00 00 00 00 00 FF FF FF FF 00 0A 02 01 
11:11:43 route,ospf,debug,raw 00 00 00 28 0A FF FF 01 00 00 00 00 
```

#### 與設施無關的主題列表 {#list-of-facility-independent-topics}

| 主題 | 描述 |
| :-- | :-- |
| **critical** | 標記為 critical 的日誌條目；每次登入時，這些日誌條目都會列印到控制檯。 |
| **debug** | 偵錯日誌條目 |
| **error** | 錯誤訊息 |
| **info** | 資訊性日誌條目 |
| **packet** | 顯示接收/傳送封包內容的日誌條目 |
| **raw** | 顯示接收/傳送封包原始內容的日誌條目 |
| **warning** | 警告訊息。 |

#### 各種 RouterOS 設施使用的主題 {#topics-used-by-various-routeros-facilities}

| 主題 | 描述 |
| :-- | :-- |
| **account** | 由計費設施生成的日誌訊息。 |
| **async** | 由非同步裝置生成的日誌訊息 |
| **backup** | 由備份建立設施生成的日誌訊息。 |
| **bfd** | 由 BFD 協定生成的日誌訊息 |
| **bgp** | 由 BGP 協定生成的日誌訊息 |
| **calc** | 路由計算日誌訊息。 |
| **caps** | CAPsMAN 無線裝置管理 |
| **certificate** | 安全證書 |
| **clock** | 由時鐘、IP Cloud 時間更改生成的日誌訊息。 |
| **dns** | 與名稱伺服器查詢相關的資訊 |
| **ddns** | 由動態 DNS 工具生成的日誌訊息 |
| **dude** | 與 Dude 伺服器軟體包和 The Dude 工具相關的訊息 |
| **dhcp** | DHCP 用戶端、伺服器和中繼日誌訊息 |
| **e-mail** | 由電子郵件工具生成的訊息。 |
| **event** | 在路由事件發生時生成的日誌訊息。例如，新路由已安裝到路由表中。 |
| **firewall** | 在防火牆規則中設定 **action=log** 時生成的防火牆日誌訊息 |
| **gsm** | 由 GSM 裝置生成的日誌訊息 |
| **hotspot** | 與 Hotspot 相關的日誌條目 |
| **igmp-proxy** | 與 IGMP Proxy 相關的日誌條目 |
| **ipsec** | IPSec 日誌條目 |
| **iscsi** |  |
| **isdn** |  |
| **interface** |  |
| **kvm** | 與 KVM 虛擬機器功能相關的訊息 |
| **l2tp** | 由 L2TP 用戶端和伺服器生成的日誌條目 |
| **lte** | 與 LTE/4G 調變解調器配置相關的訊息 |
| **ldp** | 與 LDP 協定相關的訊息 |
| **manager** | User Manager 日誌訊息。 |
| **mme** | MME 路由協定訊息 |
| **mpls** | MPLS 訊息 |
| **ntp** | 由 sNTP 用戶端生成的日誌條目 |
| **ospf** | OSPF 路由協定訊息 |
| **ovpn** | OpenVPN 隧道訊息 |
| **pim** | 與組播 PIM-SM 相關的訊息 |
| **ppp** | ppp 設施訊息 |
| **pppoe** | 與 PPPoE 伺服器/用戶端相關的訊息 |
| **pptp** | 與 PPTP 伺服器/用戶端相關的訊息 |
| **radius** | 由 RADIUS 用戶端生成的日誌條目 |
| **radvd** | IPv6 radv 守護程式日誌訊息。 |
| **read** | SMS 工具訊息 |
| **rip** | RIP 路由協定訊息 |
| **route** | 路由設施日誌條目 |
| **rsvp** | 由資源預留協定生成的訊息。 |
| **script** | 由指令碼生成的日誌條目 |
| **sertcp** | 與負責 "/port remote-access" 的設施相關的日誌訊息 |
| **simulator** |  |
| **state** | DHCP 用戶端和路由狀態訊息。 |
| **store** | 由儲存設施生成的日誌條目 |
| **smb** | 與 SMB 檔案共享系統相關的訊息 |
| **snmp** | 與簡單網路管理協定（SNMP）配置相關的訊息 |
| **system** | 通用系統訊息 |
| **telephony** | *已過時！以前由 IP 電話軟體包使用* |
| **tftp** | 由 TFTP 伺服器生成的訊息 |
| **timer** | 與 RouterOS 中使用的計時器相關的日誌訊息。例如 bgp keepalive 日誌`12:41:40 route,bgp,debug,timer KeepaliveTimer expired``12:41:40 route,bgp,debug,timer     RemoteAddress=2001:470:1f09:131::1` |
| **ups** | 由 UPS 監控工具生成的訊息 |
| **vrrp** | 由 VRRP 生成的訊息 |
| **watchdog** | 由 Watchdog 生成的日誌條目 |
| **web-proxy** | 由 Web 代理生成的日誌訊息 |
| **wireless** | 無線日誌條目。 |
| **write** | SMS 工具訊息。 |

## 示例 {#examples}

### 建立獨立的記憶體日誌緩衝區 {#create-separate-memory-logging-buffers-1}

建立新的記憶體日誌緩衝區，用於將指定的日誌與預設記憶體日誌分開儲存。

```ros
/system/logging/action/add name=dhcpMemoryLog target=memory memory-lines=300
/system/logging/action/add name=wirelessLog target=memory memory-lines=500
```

為建立的緩衝區分配主題。此規則將所有 DHCP 日誌傳送到 dhcpMemoryLog，並將無線日誌傳送到 wirelessLog 緩衝區。

```ros
/system/logging/add topics=dhcp action=dhcpMemoryLog
/system/logging/add topics=wireless action=wirelessLog
```

```ros
# 仅查看存储在其专用缓冲区中的 DHCP 相关日志
/log/print where buffer=dhcpMemoryLog

# 仅查看存储在其专用缓冲区中的非 info 级别 Wireless 日志
/log/print where buffer=wirelessLog
```

```ros
/system/logging/action/clear action=dhcpMemoryLog
```

### 記錄到檔案 {#logging-to-file}

要將所有內容記錄到檔案，請新增新的日誌動作：

```ros
/system/logging/action/add name=file target=disk disk-file-name=log
```

然後使用這個新動作記錄所有內容：

```ros
/system/logging/add action=file
```

可以透過執行以下命令僅在其中記錄錯誤：

```ros
/system/logging/add topics=error action=file 
```

這將記錄到檔案 **log.0.txt** 和 **log.1.txt** 中。

可以透過指定 *disk-lines-per-file* 來指定檔案以行數表示的最大大小。**\<file>.0.txt** 是活動檔案，新日誌將追加到其中；一旦其大小達到最大值，它就會變為 **\<file>.1.txt**，並建立新的空 **\<file>.0.txt**。

可以透過在檔名前指定目錄名，將日誌記錄到 USB 快閃記憶體盤或 *MicroSD/CF*（在 RouterBOARD 上）。例如，如果可訪問的 USB 快閃記憶體盤在 */files* 下作為 **usb1** 目錄，則應執行以下命令：

```ros
/system/logging/action/add name=usb target=disk disk-file-name=usb1/log
```

:::warning
來自檔案的日誌條目將在重啟後重新儲存到記憶體中。
:::
