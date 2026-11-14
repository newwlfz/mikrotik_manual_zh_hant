---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/snmp"
sidebar_position: 12
title: "SNMP"
sidebar_label: "SNMP"
description: "本頁介紹 MikroTik RouterOS 中的 SNMP 配置，涵蓋啟用服務、常規設定（如聯絡人資訊和 trap 配置）、SNMPv1/2c/3 的 community 訪問許可權，以及監控緩慢服務或 OID 時關於超時的警告。"
tags:
  - 'snmp'
  - 'community-settings'
  - 'security'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/snmp
captured_at: '2026-11-04T11:28:02+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

簡單網路管理協定（SNMP）是一種網際網路標準協定，用於監控和管理 IP 網路上的裝置。它可與 Cacti、MRTG 或 The Dude 等監控工具配合使用，以收集、視覺化和繪製系統資料圖表。

SNMP 寫訪問僅對選定的 OID 可用。對於受支援的 OID，可透過 SNMP v1、v2c 或 v3 執行寫操作。SNMP 回覆透過接收請求的同一介面傳送，從而確保響應所使用的源地址與原始發往路由器的請求中使用的目標地址相同。

![](/img/06ecaf368aba6a7c.webp)

:::warning
SNMP 服務會從系統上執行的各項服務中收集資料。如果 SNMP 與其中某個服務之間的通訊耗時超過預期，系統可能會記錄類似 timeout while waiting for program 或 SNMP did not get OID data within the expected time, ignoring OID 的警告。每個服務的超時時間為 30 秒，路由服務最長可達 5 分鐘。發生此類超時後，受影響的服務可能會暫時停止響應 SNMP 資料請求，然後再嘗試重新獲取所請求的資訊。

這些警告並不表示 SNMP 服務本身存在問題。在大多數情況下，它們出現在使用 SNMP 監控緩慢或負載過重的服務時。當監控不適合透過 SNMP 輪詢的 OID 時，也可能出現這些警告。在這種情況下，建議的解決方案是在監控工具配置中排除這些 OID。
:::

## 快速配置 {#quick-configuration}

要在 RouterOS 中啟用 SNMP：

```ros
[admin@MikroTik] /snmp> print 
enabled: no
contact: 
location: 
engine-id: 
trap-community: (unknown)
trap-version: 1
[admin@MikroTik] /snmp> set enabled yes
```

你也可以在上述設定中指定管理聯絡資訊。所有 SNMP 資料都將對在 *community* 選單中配置的 community 可用。

## 常規屬性 {#general-properties}

**子選單：** `/snmp`

 此子選單可用於啟用 SNMP 並配置常規設定。

| 屬性 | 描述 |
| :-- | :-- |
| **contact** (*string*; Default: **""**) | 聯絡資訊 |
| **enabled** (*yes \| no*; Default: **no**) | 用於停用/啟用 SNMP 服務 |
| **engine-id** (*string*; Default: **""**) | 用於 SNMP v3，作為識別符號的一部分。你可以使用此引數配置 engine id 的字尾部分。如果 SNMP 用戶端無法檢測到已設定的 engine-id 值，則必須使用此字首十六進位制值 0x80003a8c04 |
| **location** (*string*; Default: **""**) | 位置資訊 |
| **trap-community** (*string*; Default: **public**) | 在 *community* 選單中配置了哪些 community，以便在傳送 trap 時使用。 |
| **trap-generators** (*interfaces \| start-trap*; Default: ) | 什麼操作會生成 trap：<ul><li>interfaces - 介面變更；</li><li>start-trap - SNMP 伺服器在路由器上啟動</li><li>temp-exception - 當溫度達到 100c（或 <code>/system/health</code> 中為 cpu-overtemp-threshold 配置的值）時傳送 trap</li></ul> |
| **trap-interfaces** (*string \| all*; Default: ) | 將向其傳送 trap 的介面列表。 |
| **trap-target** (*list of IP/IPv6*; Default: **0.0.0.0**) | 必須接收 trap 的 SNMP 資料收集器的 IP（IPv4 或 IPv6）地址 |
| **trap-version** (*1\|2\|3*; Default: **1**) | 用於 trap 的 SNMP 協定版本 |
| **src-address** (*IPv4 or IPv6 address*; Default: **::**) | 強制路由器始終為所有 SNMP 訊息使用相同的 IP 源地址 |
| **vrf** (*VRF name*; 預設值：**main**) | 設定服務監聽傳入連線所在的 VRF |

:::note
engine-id 欄位儲存 engine-id 的字尾值，通常 SNMP 用戶端應能從路由器讀取的 SNMP 值中檢測到該值。但是，也可能存在無法檢測的情況。在這種情況下，必須按以下規則設定 engine-ID 值：\<engine-id prefix> + \<hex-dump suffix>，例如，如果你將字尾值設定為 1234，則必須提供 80003a8c04 + 31323334，組合後的十六進位制（結果）為 80003a8c0431323334
:::

## Community 屬性 {#community-properties}

**子選單：** `/snmp/community`

此子選單用於設定 SNMP 資料的訪問許可權。

v1 和 v2c 的安全性很低，只有一個明文 community 字串（„username“）以及按 IP 地址限制訪問的能力。

在生產環境中應使用 SNMP v3，因為它提供安全性——使用 MD5/SHA1 的授權（使用者 + 密碼），以及使用 DES 和 AES 的加密。

```ros
[admin@MikroTik] /snmp/community> print value-list 
name: public
address: 0.0.0.0/0
security: none
read-access: yes
write-access: no
authentication-protocol: MD5
encryption-protocol: DES
authentication-password: *****
encryption-password: *****
```

:::danger
預設設定只有一個名為 *public* 的 community，且沒有任何附加安全設定。這些設定應被視為不安全，應根據所需的安全配置檔案進行調整。
:::

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP/IPv6 address*; Default: **0.0.0.0/0**) | 允許連線到 SNMP 伺服器的地址 |
| **authentication-password** (*string*; Default: **""**) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於向伺服器認證連線（SNMPv3）的密碼。密碼長度必須至少為 8 個字元。 |
| **authentication-protocol** (*MD5 \| SHA1*; Default: **MD5**) | 用於認證的協定（SNMPv3） |
| **encryption-password** (*string*; Default: **""**) *[sensitive](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於加密的密碼（SNMPv3）。密碼長度必須至少為 8 個字元。 |
| **encryption-protocol** (*DES \| AES*; Default: **DES**) | 用於加密通訊的加密協定（SNMPv3）。AES（參見 rfc3826）自 v6.16 起可用。 |
| **name** (*string*; Default: ) | SNMP community 的名稱。 |
| **read-access** (*yes \| no*; Default: **yes**) | 此 community 是否啟用讀訪問 |
| **security** (*authorized \| none \| private*; Default: **none**) | 安全級別：none - 不需要加密或認證（noAuthNoPriv）；authorized - 不加密，但需要認證（authNoPriv）；private - 同時需要加密和認證（authPriv） |
| **write-access** (*yes \| no*; Default: **no**) | 此 community 是否啟用寫訪問 |

## 管理資訊庫（MIB） {#management-information-base-mib}

管理資訊庫（MIB）是由代理維護的資訊資料庫，管理端可以對其進行查詢。你可以從此處下載最新的 MikroTik RouterOS MIB 檔案：[https://mikrotik.com/download/tools](https://mikrotik.com/download/tools)

RouterOS 中使用的 MIB：

- MIKROTIK-MIB
- MIB-2
- HOST-RESOURCES-MIB
- IF-MIB
- IP-MIB
- IP-FORWARD-MIB
- IPV6-MIB
- BRIDGE-MIB
- DHCP-SERVER-MIB
- CISCO-AAA-SESSION-MIB
- ENTITY-MIB
- UPS-MIB
- SQUID-MIB

## 物件識別符號（OID） {#object-identifiers-oid}

每個 OID 標識一個可透過 SNMP 讀取的變數。儘管 MIB 檔案包含所有需要的 OID 值，你也可以在任意選單層級使用 **print oid** 命令在控制檯中列印各個 OID 的資訊：

```ros
[admin@MikroTik] /interface> print oid

Flags: D - dynamic, X - disabled, R - running, S - slave 
0 R name=.1.3.6.1.2.1.2.2.1.2.1 mtu=.1.3.6.1.2.1.2.2.1.4.1 
mac-address=.1.3.6.1.2.1.2.2.1.6.1 admin-status=.1.3.6.1.2.1.2.2.1.7.1 
oper-status=.1.3.6.1.2.1.2.2.1.8.1 bytes-in=.1.3.6.1.2.1.2.2.1.10.1 
packets-in=.1.3.6.1.2.1.2.2.1.11.1 discards-in=.1.3.6.1.2.1.2.2.1.13.1 
errors-in=.1.3.6.1.2.1.2.2.1.14.1 bytes-out=.1.3.6.1.2.1.2.2.1.16.1 
packets-out=.1.3.6.1.2.1.2.2.1.17.1 discards-out=.1.3.6.1.2.1.2.2.1.19.1 
errors-out=.1.3.6.1.2.1.2.2.1.20.1 
```

- MIKROTIK-MIB
- MIB-2
- HOST-RESOURCES-MIB
- IF-MIB
- IP-MIB
- IP-FORWARD-MIB
- IPV6-MIB
- BRIDGE-MIB
- DHCP-SERVER-MIB
- CISCO-AAA-SESSION-MIB
- ENTITY-MIB
- UPS-MIB
- SQUID-MIB

SNMP trap 使路由器能夠透過傳送 trap 來通知資料採集器介面變化和 SNMP 服務狀態變化。可以傳送帶有安全功能的 trap，以支援 SNMPv1（無安全）。SNMPv2、各變體，以及帶加密和授權的 SNMPv3。

對於 SNMPv2 和 v3，你必須將配置合適的 community 設定為 *trap-community*，以啟用所需功能（密碼或加密/授權）。

## SNMP 寫入 {#traps}

SNMP 寫入允許透過 SNMP 請求更改路由器配置。當啟用 SNMP 和寫訪問時，請考慮保護對路由器或路由器 SNMP 的訪問。

要透過 SNMP 請求更改設定，請使用下面的命令允許 SNMP 對選定的 community 進行寫入。

```ros
/snmp/community/set <number> write-access=yes
```

### 系統標識 {#system-identity}

可以透過 SNMP set 命令更改路由器系統標識。

```bash
snmpset -c public -v 1 192.168.88.1 1.3.6.1.2.1.1.5.0 s New_Identity
```

- *snmpset* - 用於傳送 SNMP SET 請求以在網路實體上設定資訊的 SNMP 應用程式；
- *public* - 路由器的 community 名稱；
- *192.168.88.1* - 路由器的 IP 地址；
- *1.3.6.1.2.1.1.5.0* - 路由器標識的 SNMP 值；

上面的 SNMPset 命令等同於以下 RouterOS 命令：

```ros
/system/identity/set identity=New_Identity
```

### 重啟 {#reboot}

可以透過 SNMP set 命令重啟路由器。你需要為 reboot SNMP 設定設定一個不等於 0 的值。

```bash
snmpset -c public -v 1 192.168.88.1 1.3.6.1.4.1.14988.1.1.7.1.0 s 1
```

- **1.3.6.1.4.1.14988.1.1.7.1.0**，路由器重啟的 SNMP 值。
- **s 1**，用於設定值的 snmpset 命令，該值不應等於 0。

Reboot SNMPset 命令等同於以下 RouterOS 命令：

```ros
/system/reboot
```

### 執行指令碼 {#run-script}

當你需要為指令碼的 SNMP 設定設定值時，SNMP 寫入允許從 **system script** 選單在路由器上執行指令碼。

```bash
snmpset -c public -v 1 192.168.88.1 1.3.6.1.4.1.14988.1.1.8.1.1.3.X s 1
```

- **X**，指令碼編號，編號從 1 開始。
- **s 1**，用於設定值的 snmpset 命令，該值不應等於 0。

在 RouterOS 上的相同命令：

```ros
/system/script> print 
Flags: I - invalid 
0 name="test" owner="admin" policy=ftp,reboot,read,write,policy,
test,winbox,password,sniff last-started=1970-01-01
01:31:57 run-count=23 source=:beep 

/system/script/run 0
```

:::danger
SNMP 僅限於 *ftp,reboot,**read,write,test,romon* 指令碼策略。如果指令碼的策略超出 *ftp,reboot,**read,write,test,romon*，則該指令碼將不會被執行。請確保你的指令碼不超過上述策略。
:::

### 使用 GET 執行指令碼 {#running-scripts-with-get}

可以透過對指令碼 OID 的 SNMP GET 請求來執行 `/system/scripts`（自 6.37 起）。為此，需要一個具有寫許可權的 SNMP community。由於該表是動態的，指令碼的 OID 可以透過 SNMPWALK 命令獲取。

#### 新增指令碼 {#add-script}

```ros
/system/script
add name=script1 owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/sy reboot "
add name=script2 owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="[:put output]"
```

#### 獲取指令碼 OID 表 {#get-the-script-oid-table}

```bash
$ snmpwalk -v2c -cpublic 192.168.88.1 1.3.6.1.4.1.14988.1.1.8
iso.3.6.1.4.1.14988.1.1.8.1.1.2.1 = STRING: "script1"
iso.3.6.1.4.1.14988.1.1.8.1.1.2.2 = STRING: "script2"
iso.3.6.1.4.1.14988.1.1.8.1.1.3.1 = INTEGER: 0
iso.3.6.1.4.1.14988.1.1.8.1.1.3.2 = INTEGER: 0
```

#### 要執行指令碼，請使用表 18 {#to-run-the-script-use-table-18}

```bash
$ snmpget -v2c -cpublic 192.168.88.1 1.3.6.1.4.1.14988.1.1.18.1.1.2.2
iso.3.6	.1.4.1.14988.1.1.18.1.1.2.2 = STRING: "output"
```

:::danger
SNMP 僅限於 *ftp,reboot,**read,write,test,romon* 指令碼策略。如果指令碼的策略超出 *ftp,reboot,**read,write,test,romon*，則該指令碼將不會被執行。請確保你的指令碼不超過上述策略。
:::
