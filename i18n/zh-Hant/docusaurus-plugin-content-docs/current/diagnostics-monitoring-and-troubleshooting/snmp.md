---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/snmp"
sidebar_position: 12
title: "SNMP"
sidebar_label: "SNMP"
description: "啟用 SNMP 代理，控制哪些 community 可以讀取路由器以及可以更改哪些內容，並接收 trap。涵蓋 community 訪問模型、SNMPv3 安全性、查詢 OID、trap，以及透過 SNMP 寫入路由器設定（identity、scripts、reboot）。"
tags:
  - 'snmp'
  - 'monitoring'
  - 'security'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/snmp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Simple Network Management Protocol (SNMP) 是用於監控和管理 IP 網路上裝置的網際網路標準協定。RouterOS 執行一個 SNMP 代理，用於應答有關路由器及其介面的查詢。諸如 [The Dude](https://mikrotik.com/product/the-dude)、LibreNMS、Zabbix、Cacti 或 MRTG 等工具會使用這些應答來採集、視覺化和繪製系統資料圖表。

在你開啟之前，該代理處於停用狀態。使用 `/snmp/set enabled=yes` 啟用它；隨後路由器會在 UDP 埠 161 上應答 SNMP 查詢。預設情況下，一個名為 `public` 的團體可以讀取任何內容，因此在將路由器接入不受信任的網路之前，請對其進行限制。

![SNMP traffic graph rendered by The Dude (RRDtool), showing download traffic for a router interface](/img/06ecaf368aba6a7c.webp)

:::tip
啟用 SNMP 就足以開始監控：路由器會在 UDP 埠 161 上應答，並且預設的 `public` 團體對所有內容都具有讀取許可權，因此同一網路上的採集器可以立即讀取路由器。這也意味著該配置對該網路上的任何人開放，因此在路由器上線前，請限制或刪除 `public`（[限制團體](#restrict-a-community)）。
:::

## 為採集器啟用 SNMP {#enable-snmp-for-a-collector}

開啟代理，併為採集器提供一個限制在其網路範圍內的團體。團體名稱相當於 SNMPv1 和 v2c 的密碼，並且每次輪詢路由器時都會以明文傳輸。示例使用文件地址範圍 `192.0.2.0/24`；請將其替換為你的採集器網路，並將 `192.0.2.1` 替換為路由器地址。

```ros
/snmp/set enabled=yes contact="NOC" location="Server room"
/snmp/community/add name=monit addresses=192.0.2.0/24 \
    security=none read-access=yes
```

```text
           enabled: yes
           contact: NOC
          location: Server room
  engine-id-suffix:
         engine-id: 80003a8c04cca063f65a2d89956b75a4daa36094f61e08c68fc99350599b77b4
       src-address: ::
       trap-target:
    trap-community: public
      trap-version: 1
   trap-generators: temp-exception
               vrf: main
```

團體輸出會顯示採集器可以使用哪些地址以及它能執行哪些操作：

```ros
[admin@MikroTik] /snmp/community> print detail where name=monit or name=public
```

```text
Flags: * - DEFAULT
0  * name="public" addresses=::/0 security=none read-access=yes write-access=no
     denied-oids="" authentication-protocol=MD5 encryption-protocol=DES
 
1    name="monit" addresses=192.0.2.0/24 security=none read-access=yes
     write-access=no denied-oids="" authentication-protocol=MD5
     encryption-protocol=DES
```

檢查路由器是否能應答來自採集器的查詢，例如使用 `snmpwalk`（Linux 和 macOS 上 net-snmp 的一部分；其他作業系統有等效的 SNMP 工具）：

```bash
snmpwalk -v2c -c monit 192.0.2.1 1.3.6.1.4.1.14988.1.1.4.1.0
```

```text
SNMPv2-SMI::enterprises.14988.1.1.4.1.0 = STRING: "QMBK-S7GS"
```

該值是路由器的軟體 ID；每臺路由器有所不同。

預設的 `public` 團體仍可從任何地址讀取（`addresses=::/0`）。要麼刪除它並僅保留你建立的團體，要麼將其縮小到你的管理網路：

```ros
/snmp/community/set [find name=public] addresses=192.0.2.0/24
```

## 限制 community {#restrict-a-community}

所有屬性都涵蓋在 [`/snmp` CLI 參考](../cli-reference/snmp/index.md) 和 [`/snmp/community` CLI 參考](../cli-reference/snmp/community.md) 中。

每個 community 都是一組訪問規則：允許哪些源地址（`addresses`）、使用哪個安全級別（`security`），以及它能否讀取、寫入或兩者兼有。只有當請求來自 `addresses` 內的地址，並且指定了規則匹配的 community 時，請求才會得到應答；其他所有請求都會得到 **完全無回覆**，在採集器看來就像一臺死掉的主機。當多個採集器共享一個網路時，請使用字首而不是單個主機，併為 IPv6 採集器提供 IPv6 字首。

讀訪問（`read-access=yes`）允許採集器遍歷代理實現的每個 MIB。寫訪問（`write-access=yes`）還允許更改系統標識、執行 [指令碼](../developer-guides/scripting/index.md) 以及重啟路由器；寫 community 是一種強大的憑據，應使用難以猜測的名稱和較窄的 `addresses` 範圍。請參閱 [SNMP 寫入](#snmp-write) 部分。

`denied-oids` 會將特定 OID 或子樹列入黑名單，使 community 無法讀取它們：直接 GET 被列入黑名單的 OID 會返回 "No Such Object"，而遍歷會跳過被阻止的子樹，因此輪詢不會失敗。該設定按 community 生效，因此應在每個可能查詢該 OID 的 community 上設定它。當監控工具在路由器上遍歷開銷很大或不相關的內容時（例如空表或另一個工具已覆蓋的子樹），可以使用它。多個 OID 以逗號分隔列表傳入：

```ros
/snmp/community/set [find name=monit] \
    denied-oids=1.3.6.1.4.1.14988.1.1.13,1.3.6.1.4.1.14988.1.1.7.1.0
```

### SNMPv3 安全性 {#snmpv3-security}

對於 `security=none` 的 community，community 名稱是唯一的保護措施，v1 和 v2c 用戶端可以直接使用它。`authorized` 和 `private` 級別使用 SNMPv3，該級別會對用戶端進行認證（`authorized`），或進行認證並加密（`private`）。不匹配該級別的請求會被忽略，因此使用相同名稱的 v1/v2c 輪詢不會從這些 community 得到應答。

| 安全 | 含義 | 協定 |
| :-- | :-- | :-- |
| `none` | 無身份驗證，無加密 (`noAuthNoPriv`) | 僅 community 名稱 |
| `authorized` | 需要身份驗證 (`authNoPriv`) | MD5、SHA1、SHA256、SHA384、SHA512 |
| `private` | 需要身份驗證和加密 (`authPriv`) | MD5、SHA1、SHA256、SHA384、SHA512，配合 DES 或 AES |

密碼必須至少為 8 個字元。對於更短的密碼，路由器會以 `failure: authentication password minimum length is 8 symbols` 拒絕。

要新增 `private` 團體，請選擇認證協定（SHA256 是不錯的預設值）、加密協定和兩個密碼：

```ros
/snmp/community/add name=monit-v3 security=private \
    addresses=192.0.2.0/24 authentication-protocol=SHA256 \
    encryption-protocol=AES \
    authentication-password=change-me-a1 \
    encryption-password=change-me-b2
```

使用 `/tool/snmp-get` 測試它，這樣語法與監控工具使用的語法相同。從該網路中的一臺路由器上執行它（路由器也可以透過自己的地址輪詢自身）；測試地址必須位於該團體的 `addresses` 內（如果不在，請新增它）：

```ros
/tool/snmp-get address=192.0.2.1 oid=1.3.6.1.2.1.1.5.0 version=3 \
    security=private community=monit-v3 authentication-protocol=SHA256 \
    authentication-password=change-me-a1 encryption-protocol=AES \
    encryption-password=change-me-b2
```

```text
OID                            TYPE             VALUE
1.3.6.1.2.1.1.5.0              octet-string     MikroTik
```

## 查詢 OID {#find-an-oid}

代理能夠應答的每個值都有一個物件識別符號（即 OID）。RouterOS 會直接在控制檯中列印頁面中每個引數的 OID，因此無需閱讀 MIB 檔案即可構建採集器模板。在任意選單中，使用 `oid` 關鍵字執行相同的 `print` 命令：

```ros
[admin@MikroTik] /interface> print oid where name=ether1
```

末尾的數字（`.4`）是該介面在此路由器上的索引；在你的路由器上，索引以及因此 OID 會有所不同。前導點表示絕對 OID；監控工具接受帶點或不帶點的形式。`S` 標誌僅將該介面標記為網橋從介面，不影響 OID。

```text
Flags: S - SLAVE
0 S name=.1.3.6.1.2.1.2.2.1.2.4 actual-mtu=.1.3.6.1.2.1.2.2.1.4.4
    mac-address=.1.3.6.1.2.1.2.2.1.6.4 admin-status=.1.3.6.1.2.1.2.2.1.7.4
    oper-status=.1.3.6.1.2.1.2.2.1.8.4 bytes-in=.1.3.6.1.2.1.31.1.1.1.6.4
    packets-in=.1.3.6.1.2.1.31.1.1.1.7.4 discards-in=.1.3.6.1.2.1.2.2.1.13.4
    errors-in=.1.3.6.1.2.1.2.2.1.14.4 bytes-out=.1.3.6.1.2.1.31.1.1.1.10.4
    packets-out=.1.3.6.1.2.1.31.1.1.1.11.4 discards-out=.1.3.6.1.2.1.2.2.1.19.4
    errors-out=.1.3.6.1.2.1.2.2.1.20.4
```

在任何其他選單上執行相同命令會列舉該選單的 OID。這些 OID 的完整定義和表列表位於 [MIKROTIK-MIB 檔案](https://mikrotik.com/download/tools) 中，該檔案隨每個 RouterOS 版本釋出。大多數監控工具期望標準 MIB（MIB-2、IF-MIB、HOST-RESOURCES-MIB、IP-MIB、IP-FORWARD-MIB、IPv6-MIB、BRIDGE-MIB），代理會連同 MIKROTIK-MIB 一起實現這些標準 MIB；確切列表見[技術細節](#technical-details)。

## 接收 trap {#receive-traps}

SNMP trap 讓路由器將事件推送到採集器，而不是等待被輪詢。採集器監聽 UDP 埠 162；路由器透過能夠到達目標的介面將 trap 傳送到該埠。

```ros
/snmp/set trap-target=192.0.2.50,192.0.2.51 \
    trap-community=monit \
    trap-version=2 \
    trap-generators=interfaces
```

- `trap-target` - 應接收 trap 的收集器的 IP 地址。
- `trap-community` - 用於 trap 的團體。它必須存在於 `/snmp/community` 下；其安全級別決定 trap 如何受到保護（`none` 時為明文，`authorized` 或 `private` 時為認證或加密）。團體的 `addresses` 限制誰可以查詢代理，不影響 trap 傳送到哪裡，因此收集器不必在該列表中。
- `trap-version` - 用於 trap 的協定版本：`1`、`2` 或 `3`。
- `trap-generators` - 生成 trap 的事件。`interfaces` 為介面狀態變化傳送 `linkDown`/`linkUp`，`temp-exception` 在 CPU 溫度達到 [`/system/health`](./health.md) 中的值時傳送 trap。預設情況下 `trap-generators` 為 `temp-exception`，因此一旦設定了 `trap-target`，溫度 trap 就會啟用。

使用 `trap-interfaces` 將 `interfaces` 縮小到其變化有意義的介面：僅為列出的介面生成 trap，其他介面保持靜默。`interfaces` 通知是標準的 `linkDown`/`linkUp` trap，並攜帶受影響介面的索引，因此收集器可以獲知哪個埠斷開。

```ros
/snmp/set trap-interfaces=ether1,ether2
```

要在不更改正在使用的介面的情況下檢查收集器和 trap 路徑，請使用 `send-trap` 手動傳送一個 trap：

```ros
/snmp/send-trap oid=1.3.6.1.2.1.1.5.0 type=string value="test trap"
```

收集器會收到來自路由器的一個數據包，其中帶有團體，並且在負載中包含 MikroTik trap OID `1.3.6.1.4.1.14988.1.1.9.0.1`，後跟您傳遞的 OID 和值（使用 `trap-version=1` 時，該封包是不帶該包裝器的經典 v1 企業 trap）。在收集器上使用嗅探器確認，例如用 Wireshark 過濾 `udp port 162`。

## SNMP 寫入 {#snmp-write}

寫訪問允許管理系統更改路由器，而不僅僅是讀取它。它需要具有 `write-access=yes` 的團體，並且僅適用於固定的一組 OID：系統身份、指令碼執行條目和重啟控制，本節將對此進行描述。

將寫團體限制到監控網路，並給它一個難以猜測的名稱，因為名稱就是密碼。本節中的命令假定存在這樣一個名為 `monit-admin` 的團體。

```ros
/snmp/community/add name=monit-admin addresses=192.0.2.0/24 \
    security=none read-access=yes write-access=yes
```

:::danger
具有寫訪問許可權的團體允許任何知道其名稱的人更改路由器身份、執行指令碼並重啟路由器。不要在一個同時可從不受信任網路讀取的團體上啟用寫訪問許可權，並儘可能對寫團體使用 SNMPv3。
:::

### 更改身份 {#change-the-identity}

透過寫入 `sysName.0`（`1.3.6.1.2.1.1.5.0`）來經 SNMP 設定路由器身份，例如在 Linux 或 macOS 上使用 `snmpset`：

```bash
snmpset -v 1 -c monit-admin 192.0.2.1 1.3.6.1.2.1.1.5.0 s Branch-GW
```

```text
SNMPv2-MIB::sysName.0 = STRING: Branch-GW
```

在示例中，`-v 1` 選擇協定版本，`-c monit-admin` 指定團體，而 `s` 標記該值為字串（`snmpset` 的引數型別不是 OID 型別；這些 OID 接受字串值）。

沒有寫訪問許可權的 `public` 團體以 `readOnly` 拒絕同一請求。具有寫訪問許可權的團體還可以更改其他設定並重啟路由器，這就是為什麼它需要前面描述的這些限制。請參閱[身份](../system-information-and-utilities/identity.md)，瞭解從控制檯和 WinBox 執行相同操作的方法。

### 執行指令碼 {#run-a-script}

採集器可以在路由器上執行指令碼，這是一種讓監控系統無需登入即可執行維護或報告步驟的方式。指令碼必須存在於[系統指令碼](../developer-guides/scripting/index.md)中：

```ros
/system/script/add name=status-report owner=admin \
    policy=read,write,test source=":put \"status ok\""
```

執行指令碼需要具有寫訪問許可權的團體（如 `monit-admin`），因為它可能更改路由器。指令碼透過向 `1.3.6.1.4.1.14988.1.1.18.1.1.2.<N>` 傳送 SNMP GET 來啟動，其中 `<N>` 是指令碼在 `/system/script/print` 中的位置（第一項為 1，第二項為 2，依此類推）。GET 返回指令碼列印的任何內容：

```bash
snmpget -v2c -c monit-admin 192.0.2.1 1.3.6.1.4.1.14988.1.1.18.1.1.2.1
```

```text
SNMPv2-SMI::enterprises.14988.1.1.18.1.1.2.1 = STRING: "status ok"
```

指令碼列表及其編號可透過 `1.3.6.1.4.1.14988.1.1.8` 處的 SNMP 表獲取，因此採集器可以透過遍歷來發現它們，而不必固定編號。

```bash
snmpwalk -v2c -c monit-admin 192.0.2.1 1.3.6.1.4.1.14988.1.1.8
```

```text
iso.3.6.1.4.1.14988.1.1.8.1.1.2.1 = STRING: "status-report"
iso.3.6.1.4.1.14988.1.1.8.1.1.3.1 = INTEGER: 0
```

同一指令碼也可以透過向 `1.3.6.1.4.1.14988.1.1.8.1.1.3.<N>` 傳送 SET 來啟動。寫入的值無關緊要——`0` 與任何其他值一樣會執行它：

```bash
snmpset -v2c -c monit-admin 192.0.2.1 1.3.6.1.4.1.14988.1.1.8.1.1.3.1 s 1
```

SNMP 僅以有限的一組策略執行指令碼：`ftp`、`reboot`、`read`、`write`、`test` 和 `romon`。需要任何其他策略（例如 `password`、`sniff` 或 `sensitive`）的指令碼會被拒絕，並且 GET 返回 `error: not enough permissions`。請將透過 SNMP 執行的指令碼限制在該策略集內。

### 重啟路由器 {#reboot-the-router}

將值 `1` 寫入重啟 OID `1.3.6.1.4.1.14988.1.1.7.1.0` 會重啟路由器：

```bash
snmpset -v 1 -c monit-admin 192.0.2.1 1.3.6.1.4.1.14988.1.1.7.1.0 s 1
```

這會在路由器啟動期間斷開所有用戶端，包括髮送請求的管理系統。

:::note
預設的 `public` 團體沒有寫入許可權，因此保持預設配置的路由器無法透過 SNMP 進行更改或重啟。

要檢視哪些路由器選單會透過管理通道暴露類似密碼的值，請參閱[帶敏感引數的選單列表](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)。
:::

## 檢查與故障排除 {#check-and-troubleshoot}

- 要檢視代理記錄了什麼：新增 `snmp` 主題（`/system/logging/add topics=snmp`）。`snmp,debug` 級別還會記錄請求和回覆；在繁忙的路由器上會變得很冗長。
- 收集器超時：除了後面介紹的代理檢查外，還要確保沒有 [防火牆](../firewall-and-quality-of-service/firewall/index.md) 規則或其他過濾器丟棄來自該收集器的 UDP 161（以及用於 trap 的 UDP 162）。
- 所有設定都正確但收集器超時：檢查代理是否已啟用、請求是否來自 community 的 `addresses` 內的地址，以及 community 名稱是否拼寫完全正確。任何一項不滿足的請求都完全得不到回覆，看起來就像主機已宕機。
- v1/v2c 收集器無法讀取 `security=authorized` 或 `private` 的 community：這些級別需要 SNMPv3。為 v1/v2c 收集器建立一個 `security=none` 的 community，並將其限制為它們的地址。
- 設定 `src-address` 後輪詢中斷：此時路由器只應答發往該地址的請求（並且，對於 IPv4 值，不應答 IPv6 請求），因此查詢任何其他地址的收集器都會超時。清除 `src-address`，或將其設定為收集器輪詢的地址。
- 當某個服務繁忙，或某個 OID 的應答開銷很大時（例如在大型路由器上遍歷完整 routing-table walk），路由器應答 walk 會很慢，並記錄 `snmp,warning` 條目，例如 `timeout while waiting for program` 或 `SNMP did not get OID data within expected time, ignoring OID`。代理會記錄該 OID，在一段時間內跳過它，並照常應答後續請求。從收集器中排除此類 OID，或按 community 章節所述用 `denied-oids` 將它們加入黑名單，而不是不斷輪詢它們。

## 技術細節 {#technical-details}

### SNMP 引擎 ID {#snmp-engine-id}

代理透過 engine ID 向 SNMPv3 用戶端標識自身，`/snmp/print` 會將其顯示為 `engine-id`。可配置的 `engine-id-suffix` 只是該值的末尾部分：路由器會以 ASCII 十六進位制形式將字尾寫入 engine ID，因此 `engine-id-suffix=1234` 會生成 engine ID `80003a8c0431323334`。將字尾留空可使用自動生成的 engine ID，該 ID 在每臺路由器上不同，並且在多次重啟後保持不變；大多數 SNMPv3 收集器會發現它，因此很少需要固定字尾。

### 回覆源和 `src-address` {#reply-source-and-src-address}

預設情況下，代理從接收請求的介面地址進行應答，因此回覆所使用的源地址與採集器傳送請求時的目標地址相同。設定 `src-address` 會強制代理使用該地址：此時它只應答發往你所設值的請求，並且當該值為 IPv4 時不再透過 IPv6 應答。僅當輪詢透過某個無法在採集器上更改的地址到達路由器時才設定它，並讓採集器指向同一個地址。

### SNMP 寫 OID {#snmp-write-oids}

寫訪問涵蓋一組固定的 OID：系統標識（`1.3.6.1.2.1.1.5.0`）、位於 `1.3.6.1.4.1.14988.1.1.8` 和 `1.3.6.1.4.1.14988.1.1.18` 下的指令碼執行條目，以及重啟控制（`1.3.6.1.4.1.14988.1.1.7.1.0`）。其他 MIB 物件為只讀。

### 代理實現的 MIB {#mibs-the-agent-implements}

代理應答標準 MIB-2 組（system、interfaces、IP、IP forwarding、IPv6、ICMP、TCP、UDP）以及 [HOST-RESOURCES-MIB](https://datatracker.ietf.org/doc/html/rfc2790)、[IF-MIB](https://datatracker.ietf.org/doc/html/rfc2863)、[IP-MIB](https://datatracker.ietf.org/doc/html/rfc4293)、[IP-FORWARD-MIB](https://datatracker.ietf.org/doc/html/rfc4292)、[IPV6-MIB](https://datatracker.ietf.org/doc/html/rfc4293)、[BRIDGE-MIB](https://datatracker.ietf.org/doc/html/rfc4188)，以及 [UPS-MIB](https://datatracker.ietf.org/doc/html/rfc1628) 和 [Web 代理](../network-management/proxy/web-proxy.md) 所使用的 SQUID-MIB。專有的 [MIKROTIK-MIB](https://mikrotik.com/download/tools) 承載不適合任何標準 MIB 的 RouterOS 值，例如軟體 ID、健康狀態值和指令碼表。

LLDP-MIB 遠端表（`lldpRemTable`）包含與 [`/ip/neighbor/lldp`](../cli-reference/ip/neighbor/lldp.md) 相同的 LLDP 發現的鄰居。僅由 CDP 或 MNDP 發現的鄰居不包含在內。

`/snmp` 和 `/snmp/community` 的所有引數，以及 `/snmp/send-trap` 命令，均記錄在 [SNMP CLI 參考](../cli-reference/snmp/index.md) 中。
