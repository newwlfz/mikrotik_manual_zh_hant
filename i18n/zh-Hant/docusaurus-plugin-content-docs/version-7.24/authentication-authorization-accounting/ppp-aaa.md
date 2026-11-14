---
sidebar_key: "authentication-authorization-accounting/ppp-aaa"
sidebar_position: 4
title: "PPP AAA"
sidebar_label: "PPP AAA"
description: "MikroTik RouterOS PPP AAA 功能透過本地和 RADIUS 支援提供認證、授權和計費。PPP 配置檔案為使用者訪問記錄定義預設設定，包括網橋配置、速率限制以及加密和壓縮等安全選項。"
tags:
  - 'ppp'
  - 'aaa'
  - 'radius'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/ppp-aaa
captured_at: '2026-11-04T11:26:59+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

**子選單：** `/ppp`

MikroTik RouterOS 提供可擴充套件的認證、授權和計費 (AAA) 功能。

本地認證使用使用者資料庫和配置檔案資料庫執行。給定使用者的實際配置由使用者資料庫中的相應使用者記錄、配置檔案資料庫中的關聯項，以及配置檔案資料庫中為該使用者正在認證的給定服務設定為預設的項組合而成。配置檔案資料庫中的預設配置檔案設定優先順序最低，而使用者資料庫中的使用者訪問記錄設定優先順序最高，唯一例外是特定 IP 地址在 local-address 和 remote-address 設定中優先於 IP 地址池，這些設定將在後面描述。

對 RADIUS 認證的支援使 ISP 或網路管理員能夠透過一臺伺服器在整個大型網路中管理 PPP 使用者訪問和計費。MikroTik RouterOS 具有 [RADIUS 用戶端](./radius.md)，可為 PPP、[PPPoE](../virtual-private-networks/pppoe/index.md)、[PPTP](../virtual-private-networks/pptp.md)、[L2TP](../virtual-private-networks/l2tp/index.md)、[OpenVPN](../virtual-private-networks/openvpn.md) 和 ISDN 連線進行認證。從 RADIUS 伺服器收到的屬性會覆蓋預設配置檔案中設定的屬性，但如果未收到某些引數，則從相應的預設配置檔案獲取。

## 使用者配置檔案 {#user-profiles}

**子選單：** `/ppp/profile`

PPP 配置檔案用於為儲存在 `/ppp/secret` 子選單下的使用者訪問記錄定義預設值。`/ppp/secret` 使用者資料庫中的設定會覆蓋相應的 `/ppp/profile` 設定，但當指定為 local-address 或 remote-address 引數時，單個 IP 地址始終優先於 IP 地址池。

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **address-list** (*string*; 預設：) | [地址列表](../firewall-and-quality-of-service/firewall/address-lists.md) 名稱，ppp 分配（在伺服器上）或接收（在用戶端上）的地址將新增到該列表。 |
| **remote-ipv6-prefix-reuse** (*no \| yes*; 預設：**no**) | 如果指定了 "remote-ipv6-prefix-pool" 並且包含單個 "/64" 字首，則該字首只能用於單個 PPP 用戶端以進行 RADVD 配置。當此選項設定為值 "yes" 時，同一字首可在使用此 PPP 配置檔案的所有用戶端之間重複使用。 |
| **bridge** (*string*; 預設：) | [bridge](../bridging-and-switching/index.md) 介面的名稱，ppp 介面將作為從埠新增到該介面。兩個隧道端點（伺服器和用戶端）都必須位於 bridge 中才能使其正常工作，更多詳細資訊請參見 bridge 手冊。 |
| **bridge-horizon** (*integer 0..429496729*; 預設：) | 用於動態建立的 bridge 埠的 split-horizon 值。可用於防止橋接環路和隔離流量。為一組埠設定相同的值，以防止它們向具有相同 horizon 值的埠傳送資料。 |
| **bridge-learning** (*default \| no \| yes*; 預設：**default**) | 更改動態建立的 bridge 埠上的 MAC 學習行為：yes - 啟用 MAC 學習；no - 停用 MAC 學習；default - 從介面預設配置檔案派生此值；如果這是介面預設配置檔案，則與 yes 相同 |
| **bridge-path-cost** (*integer 1..200000000*; 預設：) | 用於動態建立的 bridge 埠的路徑開銷，由 STP/RSTP 用於確定最佳路徑，由 MSTR 用於確定區域之間的最佳路徑。當 bridge protocol-mode 設定為 none 時，此屬性無效。 |
| **bridge-port-priority** (*integer 0..240*; 預設：) | 用於動態建立的 bridge 埠的優先順序，由 STP/RSTP 用於確定根埠，由 MSTP 用於確定區域之間的根埠。當 bridge protocol-mode 設定為 none 時，此屬性無效。 |
| **bridge-port-vid** (*integer 1..4094*; 預設：**1**) | 用於為動態建立的介面分配 PVID 引數。僅當 bridge vlan-filtering 設定為 yes 時，此屬性才有效。 |
| **bridge-port-trusted**(*no \| yes*;預設：**no**) | 用於將動態建立的介面設定為 DHCP 信任介面。 |
| **change-tcp-mss** (*yes \| no \| default*; 預設：**no**) | 修改連線 MSS 設定（僅適用於 IPv4）：yes - 調整連線 MSS 值；no - 不調整連線 MSS 值；default - 從介面預設配置檔案派生此值；如果這是介面預設配置檔案，則與 no 相同 |
| **comment** (*string*; 預設：) | 配置檔案備註 |
| **dhcpv6-lease-time** (*string*; 預設：) | 租約時間可從 7.20ab202 開始設定，預設時間設定為 1d。 |
| **dhcpv6-pd-pool** (*string*; 預設：) | [IPv6 地址池](../cli-reference/ipv6/pool/index.md) 的名稱，當用戶端連線時，動態建立的 [DHCPv6 伺服器](../network-management/dhcp.md#dhcpv6-server) 將使用該地址池。  [`了解更多 >>`](../virtual-private-networks/pppoe/ipv6-pd-over-ppp.md) |
| **dhcpv6-use-radius** (*no \| yes*; 預設：**no**) | 指定為動態生成的 DHCPv6 PD 伺服器選擇的 "use-radius" 選項的值。 |
| **dns-server** (*IP*; 預設：) | 提供給 PPP 用戶端的 DNS 伺服器 IP 地址 |
| **idle-timeout** (*time*; 預設：) | 指定在沒有活動的情況下，鏈路將在多長時間後終止。預設不設定超時 |
| **incoming-filter** (*string*; 預設：) | 傳入封包的防火牆鏈名稱。指定鏈將控制來自用戶端的每個封包。應手動新增 ppp 鏈，並且應將 action=jump jump-target=ppp 的規則新增到其他相關鏈，此功能才能生效。更多資訊請參見示例部分。 |
| **insert-queue-before** (*bottom \| first \| queue name* ; 預設：) | 將新佇列插入為最後一個、第一個，或插入到指定佇列之前 |
| **interface-list** (*interface list name*; 預設：) | 指定將配置檔案介面新增到的介面列表 |
| **local-address** (*IP address \| pool*; 預設：) | 隧道地址，或用於為本地 ppp 介面分配地址的 [地址池](../cli-reference/ip/pool/index.md) 名稱 |
| **name** (*string*; 預設：) | PPP 配置檔名稱 |
| **on-up** (*script*; 預設：) | 在使用者登入事件時執行指令碼。事件指令碼可訪問以下變數：userlocal-addressremote-addresscaller-idcalled-idinterface。*interface* 變數將返回介面 id 值，而不是介面名稱。 |
| **on-down** (*script*; 預設：) | 在使用者登出時執行指令碼。更多詳細資訊請參見 ***on-up*** |
| **only-one** (*yes \| no \| default*; 預設：**default**) | 定義是否允許使用者同時擁有多個 ppp 會話：yes - 不允許使用者同時擁有多個 ppp 會話；no - 允許使用者同時擁有多個 ppp 會話；default - 從介面預設配置檔案派生此值；如果這是介面預設配置檔案，則與 no 相同 |
| **outgoing-filter** (*string*; 預設：) | 傳出封包的防火牆鏈名稱。指定鏈將控制發往用戶端的每個封包。應手動新增 PPP 鏈，並且應將 action=jump jump-target=ppp 的規則新增到其他相關鏈，此功能才能生效。更多資訊請參見示例部分。 |
| **parent-queue** (*none* \| *queue name*; 預設：) | 指定父佇列 |
| **queue-type** (*default \| ethernet-default \| wireless-default \| synchronous-default \|* *hotspot-default \| pcq-upload-default \| pcq-download-default \| only-hardware-queue \| multi-queue-ethernet-default \| default-small \| 自定義佇列型別名稱* ; 預設：) | 指定佇列型別。從 7.19 開始，可以為用戶端的“上傳”和“下載”分別指定 rx/tx 佇列型別。使用 / 配置單獨的佇列型別，第一個是 rx 佇列型別，然後是 tx 佇列型別。 |
| **rate-limit** (*string*; 預設：) | 從路由器角度來看的速率限制，格式為 **rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]**（因此 “rx” 是用戶端上傳，“tx” 是用戶端下載）。所有速率均以位元每秒為單位，除非後面帶有可選的 'k' 字尾（千位元每秒）或 'M' 字尾（兆位元每秒）。如果未指定 tx-rate，則 rx-rate 也用作 tx-rate。這同樣適用於 tx-burst-rate、tx-burst-threshold 和 tx-burst-time。如果既未指定 rx-burst-threshold 也未指定 tx-burst-threshold（但指定了 burst-rate），則使用 rx-rate 和 tx-rate 作為突發閾值。如果既未指定 rx-burst-time 也未指定 tx-burst-time，則預設使用 1s。priority 取值為 1..8，其中 1 表示最高優先順序，而 8 表示最低優先順序。如果未指定 rx-rate-min 和 tx-rate-min，則使用 rx-rate 和 tx-rate 值。rx-rate-min 和 tx-rate-min 值不能超過 rx-rate 和 tx-rate 值。 |
| **remote-address** (*IP*; 預設：) | 隧道地址，或用於為遠端 ppp 介面分配地址的 [地址池](../cli-reference/ip/pool/index.md) 名稱。 |
| **remote-ipv6-prefix-pool** (*string \| none*; 預設：**none**) | 從 IPv6 地址池向用戶端分配字首，並安裝相應的 IPv6 路由。 |
| **session-timeout** (*time*; 預設：) | 連線可保持的最長時間。預設情況下不設定時間限制。 |
| **use-compression** (*yes \| no \| default*; 預設：**default**) | 指定是否使用資料壓縮。yes - 啟用資料壓縮；no - 停用資料壓縮；default - 從介面預設配置檔案派生此值；如果這是介面預設配置檔案，則與 no 相同。此設定不影響 OVPN 隧道。 |
| **use-encryption** (*yes \| no \| default \| require*; 預設：**default**) | 指定是否使用資料加密。yes - 啟用資料加密；no - 停用資料加密；default - 從介面預設配置檔案派生此值；如果這是介面預設配置檔案，則與 no 相同；require - 明確要求加密。此設定在 OVPN 和 SSTP 隧道上不起作用。 |
| **use-ipv6** (*yes \| no \| default \| require*; 預設：**default**) | 指定是否允許 IPv6。預設情況下，如果安裝了 IPv6 軟體包，則啟用。yes - 啟用 IPv6 支援；no - 停用 IPv6 支援；default - 從介面預設配置檔案派生此值；如果這是介面預設配置檔案，則與 no 相同；require - 明確要求 IPv6 支援 |
| **use-mpls** (*yes \| no \| default \| require*; 預設：**default**) | 指定是否允許在 PPP 上使用 MPLS。yes - 啟用 MPLS 支援；no - 停用 MPLS 支援；default - 從介面預設配置檔案派生此值；如果這是介面預設配置檔案，則與 no 相同；require - 明確要求 MPLS 支援 |
| **use-upnp** (*yes \| no \| default*; 預設：**default**) | 指定是否允許 UPnP：yes - 啟用 UPnP。no - 停用 UPnP。default - 從介面預設配置檔案派生此值；如果這是介面預設配置檔案，則與 no 相同。 |
| **wins-server** (*IP address*; 預設：) | 提供給 Windows 用戶端的 WINS 伺服器 IP 地址 |

### 備註 {#notes}

兩個預設配置檔案無法刪除：

```ros
[admin@rb13] /ppp/profile> print
Flags: * - default
 0 * name="default" use-compression=no use-encryption=no only-one=no
     change-tcp-mss=yes
 1 * name="default-encryption" use-compression=default use-encryption=yes
     only-one=default change-tcp-mss=default
[admin@rb13] /ppp/profile>
```

*incoming-filter* 和 *outgoing-filter* 引數會向鏈 *ppp* 新增動態跳轉規則，其中 jump-target 引數將等於配置檔案中的 *incoming-filter* 或 *outgoing-filter* 引數。因此，在更改這些引數之前，應手動新增鏈 *ppp*。

如果使用 RADIUS 認證，則忽略 only-one 引數。

PPP 隧道使用 LCP 協定進行 MTU 協商，該協商在連線建立時立即發生。不支援 Framed MTU 屬性，因為它僅在透過 RADIUS 認證後才會傳送。

## 使用者資料庫 {#user-database}

**子選單：** `/ppp/secret`

PPP 使用者資料庫儲存 PPP 使用者訪問記錄，併為每個使用者分配 PPP 使用者配置檔案。

## 屬性 {#properties-1}

| 屬性 | 說明 |
| :-- | :-- |
| **caller-id** (*string*; 預設：) | 對於 [PPTP](../virtual-private-networks/pptp.md) 和 [L2TP](../virtual-private-networks/l2tp/index.md)，它是用戶端必須從其連線的 IP 地址。對於 [PPPoE](../virtual-private-networks/pppoe/index.md)，它是用戶端必須從其連線的 MAC 地址（以大寫字母書寫）。對於 ISDN，它是主叫號碼（可能由運營商提供，也可能不提供），用戶端可以從該號碼撥入 |
| **comment** (*string*; 預設：) | 使用者的簡短描述。 |
| **disabled** (*yes \| no*; 預設：**no**) | 是否使用該 secret。 |
| **limit-bytes-in** (*integer*; 預設：**0**) | 用戶端在一次會話中可上傳的最大位元組數。 |
| **limit-bytes-out** (*integer*; 預設：**0**) | 用戶端在一次會話中可下載的最大位元組數。 |
| **local-address** (*IP address*; 預設：) | 將在 ppp 介面本地設定的 IP 地址。 |
| **name** (*string*; 預設：) | 用於認證的名稱 |
| **password** (*string*; 預設：) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於認證的密碼 |
| **profile** (*string*; 預設：**default**) | 要使用哪個[使用者配置檔案](#user-profiles) |
| **remote-address** (*IP*; 預設：) | 將分配給遠端 ppp 介面的 IP 地址。 |
| **remote-ipv6-prefix** (*IPv6 prefix*; 預設：) | 分配給 ppp 用戶端的 IPv6 字首。該字首會新增到 [ND 字首列表](../system-information-and-utilities/neighbor-discovery.md)，從而在 ppp 介面上啟用[無狀態](../getting-started/networking-fundamentals/ipv6-neighbor-discovery.md#stateless-address-autoconfiguration)地址自動配置。 |
| **routes** (*string*; 預設：) | 當用戶端連線時出現在伺服器上的路由。路由格式為：dst-address gateway metric（例如，10.1.0.0/ 24 10.0.0.1 1）。其他語法不可接受，因為它可能被錯誤表示。可以指定多條路由，並用逗號分隔。對於 [OpenVPN](../virtual-private-networks/openvpn.md)，將忽略此引數。 |
| **service** (*any \| async \| isdn \| l2tp \| pppoe \| pptp \| ovpn \| sstp*; 預設：**any**) | 指定特定使用者可以使用的服務。 |

## 活動使用者 {#active-users}

**子選單：** `/ppp/active`

此子選單允許監控活動（已連線）使用者。

`/ppp/active/print` 命令將顯示所有當前連線的使用者。

`/ppp/active/print stats` 命令將顯示接收/傳送的位元組和封包

## 屬性 {#properties-2}

| 屬性 | 說明 |
| :-- | :-- |
| **address** (*IP address*) | 用戶端從伺服器獲取的 IP 地址 |
| **bytes** (*integer*) | 透過此連線傳輸的位元組數。第一個數字表示從路由器角度看已傳送的流量，第二個數字表示已接收的流量。 |
| **caller-id** (*string*) | 對於 [PPTP](../virtual-private-networks/pptp.md) 和 [L2TP](../virtual-private-networks/l2tp/index.md)，它是用戶端連線時所來自的 IP 地址。對於 [PPPoE](../virtual-private-networks/pppoe/index.md)，它是用戶端連線時所來自的 MAC 地址。 |
| **encoding** (*string*) | 顯示此連線中使用的加密和編碼（如果不對稱，則用 '/' 分隔） |
| **limit-bytes-in** (*integer*) | 允許使用者傳送到路由器的最大位元組數。 |
| **limit-bytes-out** (*integer*) | 允許使用者傳送到用戶端的最大位元組數。 |
| **name** (*string*) | 認證階段提供的使用者名稱 |
| **packets** (*integer/integer*) | 透過此連線傳輸的封包數。第一個數字表示從路由器角度看已傳送的流量，第二個數字表示已接收的流量 |
| **service** (*async \| isdn \| l2tp \| pppoe \| pptp \| ovpn \| sstp*) | 使用者正在使用的服務型別。 |
| **session-id** (*string*) | 顯示唯一的用戶端識別符號。 |
| **uptime** (*time*) | 使用者線上時間 |

## 遠端 AAA {#remote-aaa}

**子選單：** `/ppp/aaa`

此子選單中的設定允許設定 RADIUS 計費和認證。請注意，僅當在本地使用者資料庫中找不到所需使用者名稱時，才會查詢 RADIUS 使用者資料庫。

## 屬性 {#properties-3}

| 屬性 | 說明 |
| :-- | :-- |
| **accounting** (*yes \| no*; 預設：**yes**) | 啟用 RADIUS 計費 |
| **interim-update** (*time*; 預設：**0s**) | Interim-Update 時間間隔 |
| **use-radius** (*yes \| no*; 預設：**no**) | 啟用透過 RADIUS 進行使用者認證。如果在本地 secret 資料庫中找不到條目，則用戶端將透過 RADIUS 進行認證。 |
| **enable-ipv6-accounting** (*yes \| no*; 預設：**no**) | 啟用 IPv6 單獨計費。預設情況下，PPP 服務在向 RADIUS 伺服器報告網路使用統計資訊時，會將 Layer2、IPv4 和 IPv6 資料一起計入。如果需要區分 IPv4 和 IPv6 流量，則可以啟用此選項。其工作前提是必須透過 PPP 服務向用戶端分配字首，並且還必須提供 rate-limit。動態建立的佇列統計資訊將用作 IPv6 資料的計數器，然後作為單獨的 IPv6 統計屬性包含在計費封包中。對於由動態建立的 DHCPv6 伺服器根據所提供的字首池或 PPP/Profile 配置分配的字首，此功能將不起作用。此時字首分配由 DHCP 服務處理，而不是 PPP，因此計費無法由 PPP 服務管理。 |

## 示例 {#examples}

#### 新增新配置檔案 {#add-new-profile}

要新增配置檔案 ex，該配置檔案將 10.0.0.1 地址分配給路由器本身，並將 ex 地址池中的地址分配給用戶端，同時透過 mypppclients 鏈過濾來自用戶端的流量：

```ros
[admin@rb13] /ppp/profile> add name=ex local-address=10.0.0.1 remote-address=ex incoming-filter=mypppclients
[admin@rb13] /ppp/profile> print
Flags: * - default
 0 * name="default" use-compression=no use-vj-compression=no use-encryption=no only-one=no
     change-tcp-mss=yes
 1   name="ex" local-address=10.0.0.1 remote-address=ex use-compression=default
     use-vj-compression=default use-encryption=default only-one=default change-tcp-mss=default
     incoming-filter=mypppclients
 2 * name="default-encryption" use-compression=default use-vj-compression=default use-encryption=yes
     only-one=default change-tcp-mss=default
[admin@rb13] /ppp/profile>
```

#### 新增新使用者 {#add-new-user}

要新增使用者 "ex"，密碼為 "lkjrht"，配置檔案為 "ex"，且僅可用於 PPTP 服務，請輸入以下命令：

```ros
[admin@rb13] /ppp/secret> add name=ex password=lkjrht service=pptp profile=ex
[admin@rb13] /ppp/secret> print
Flags: X - disabled
 #   NAME                SERVICE CALLER-ID         PASSWORD          PROFILE            REMOTE-ADDRESS
 0   ex                  pptp                      lkjrht            ex                 0.0.0.0
[admin@rb13] /ppp/secret>
```
