---
title: "PPP AAA"
description: "MikroTik RouterOS PPP AAA 功能提供驗證、授權與計費，並支援本機與 RADIUS。PPP 設定檔定義使用者存取記錄的預設設定，包括橋接組態、速率限制，以及 Encryption 與壓縮等安全選項。"
tags:
  - 'ppp'
  - 'aaa'
  - 'radius'
source: https://manual.mikrotik.com/docs/7.24/authentication-authorization-accounting/ppp-aaa
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

## 摘要 {#summary}

**子選單：** `/ppp`

MikroTik RouterOS 提供可擴充的驗證、授權與計費（AAA）功能。

本機驗證使用使用者資料庫與設定檔資料庫執行。指定使用者的實際設定，是由使用者資料庫中對應的使用者記錄、設定檔資料庫中相關的項目，以及設定檔資料庫中針對該使用者正在驗證的服務所設為預設的項目組合而成。設定檔資料庫中的預設設定優先順序最低，而使用者資料庫中的使用者存取記錄設定優先順序最高；唯一的例外是特定 IP 位址在 `local-address` 與 `remote-address` 設定中會優先於 IP 集區，詳情將於後文說明。

支援 RADIUS 驗證可讓 ISP 或網路管理員從單一伺服器管理整個大型網路中的 PPP 使用者存取與計費。MikroTik RouterOS 具有 [RADIUS client](/docs/authentication-authorization-accounting/radius)，可驗證 PPP、[PPPoE](/docs/virtual-private-networks/pppoe)、[PPTP](/docs/virtual-private-networks/pptp)、[L2TP](/docs/virtual-private-networks/l2tp)、[OpenVPN](/docs/virtual-private-networks/openvpn) 與 ISDN 連線。從 RADIUS 伺服器收到的屬性會覆寫預設設定檔中設定的屬性，但若未收到某些參數，則會從對應的預設設定檔取得。

## 使用者設定檔 {#user-profiles}

**子選單：** `/ppp/profile`

PPP 設定檔用於定義儲存在 `/ppp/secret` 子選單下的使用者存取記錄預設值。`/ppp/secret` 使用者資料庫中的設定會覆寫對應的 `/ppp/profile` 設定，但當指定為 `local-address` 或 `remote-address` 參數時，單一 IP 位址一律優先於 IP 集區。

### 屬性 {#properties}

| Property | Description |
| :-- | :-- |
| **address-list** (*string*; Default: ) | 將新增 ppp 在伺服器端指派或在使用者端接收之位址的 [Address list](/docs/firewall-and-quality-of-service/firewall/address-lists) 名稱。 |
| **remote-ipv6-prefix-reuse** (*no \| yes*; Default: **no**) | 若指定 "remote-ipv6-prefix-pool" 且其中包含單一 "/64" 前綴，則該前綴只能供單一 PPP 用戶端用於 RADVD 設定。當此選項設為 "yes" 時，相同前綴可在所有使用此 PPP profile 的用戶端之間重複使用。 |
| **bridge** (*string*; Default: ) | 要將 ppp 介面以從屬埠新增至的 [bridge](/docs/bridging-and-switching) 介面名稱。若要讓此功能生效，隧道兩端（伺服器與用戶端）都必須位於 bridge 中，詳情請參閱 bridging 手冊。 |
| **bridge-horizon** (*integer 0..429496729*; Default: ) | 用於動態建立之 bridge 埠的 split-horizon 值。可用於避免橋接迴圈並隔離流量。為一組埠設定相同值，可避免它們將資料傳送給具有相同 horizon 值的埠。 |
| **bridge-learning** (*default \| no \| yes*; Default: **default**) | 變更動態建立之 bridge 埠的 MAC 學習行為：<ul><li>yes - 啟用 MAC 學習</li><li>no - 停用 MAC 學習</li><li>default - 從介面預設 profile 衍生此值；若此為介面預設 profile，則等同於 yes</li></ul> |
| **bridge-path-cost** (*integer 1..200000000*; Default: ) | 用於動態建立之 bridge 埠的路徑成本，STP/RSTP 會用它來判斷最佳路徑，MSTR 會用它來判斷區域之間的最佳路徑。當 bridge protocol-mode 設為 none 時，此屬性沒有作用。 |
| **bridge-port-priority** (*integer 0..240*; Default: ) | 用於動態建立之 bridge 埠的優先順序，STP/RSTP 會用它來判斷根埠，MSTP 會用它來判斷區域之間的根埠。當 bridge protocol-mode 設為 none 時，此屬性沒有作用。 |
| **bridge-port-vid** (*integer 1..4094*; Default: **1**) | 用於為動態建立的介面指派 PVID 參數。只有當 bridge vlan-filtering 設為 yes 時，此屬性才會生效。 |
| **bridge-port-trusted**(*no \| yes*;Default: **no**) | 用於將動態建立的介面設為 DHCP trusted。 |
| **change-tcp-mss** (*yes \| no \| default*; Default: **no**) | 修改連線 MSS 設定（僅適用於 IPv4）：<ul><li>yes - 調整連線 MSS 值</li><li>no - 不調整連線 MSS 值</li><li>default - 從介面預設 profile 衍生此值；若此為介面預設 profile，則等同於 no</li></ul> |
| **comment** (*string*; Default: ) | Profile 註解 |
| **dhcpv6-lease-time** (*string*; Default: ) | 從 7.20ab202 開始可設定租約時間，預設為 1d。 |
| **dhcpv6-lease-time** (*string*; Default: ) | 從 7.20ab202 開始可設定租約時間，預設為 1d。 |
| **dhcpv6-pd-pool** (*string*; Default: ) | 當用戶端連線時，動態建立的 [DHCPv6 server](/docs/network-management/dhcp#dhcpv6-server) 將使用的 [IPv6 pool](/docs/cli-reference/ipv6/pool) 名稱。[`Read more >>`](/docs/virtual-private-networks/pppoe/ipv6-pd-over-ppp) |
| **dhcpv6-use-radius** (*no \| yes*; Default: **no**) | 指定為動態產生的 DHCPv6 PD 伺服器所選取的 "use-radius" 選項值。 |
| **dns-server** (*IP*; Default: ) | 提供給 PPP 用戶端的 DNS 伺服器 IP 位址 |
| **idle-timeout** (*time*; Default: ) | 指定在沒有活動時終止連結前所經過的時間。預設未設定逾時。 |
| **incoming-filter** (*string*; Default: ) | 傳入封包的防火牆 chain 名稱。指定的 chain 會取得來自用戶端之每個封包的控制權。必須手動新增 ppp chain，並將 action=jump jump-target=ppp 的規則新增至其他相關 chain，此功能才會運作。詳情請參閱 Examples 章節。 |
| **insert-queue-before** (*bottom \| first \| queue name* ; Default: ) | 將新佇列插入為最後一個、第一個，或指定佇列之前 |
| **interface-list** (*interface list name*; Default: ) | 指定要將 profile 介面新增至的介面清單 |
| **local-address** (*IP address \| pool*; Default: ) | 隧道位址，或從中將位址指派給本機 ppp 介面的 [pool](/docs/cli-reference/ip/pool) 名稱 |
| **name** (*string*; Default: ) | PPP profile 名稱 |
| **on-up** (*script*; Default: ) | 在使用者登入事件時執行指令碼。事件指令碼可存取下列變數：<ul><li>user</li><li>local-address</li><li>remote-address</li><li>caller-id</li><li>called-id</li><li>interface</li></ul> <em>interface</em> 變數會傳回介面 id 值，而不是介面名稱。 |
| **on-down** (*script*; Default: ) | 在使用者登出時執行指令碼。詳情請參閱 ***on-up*** |
| **only-one** (*yes \| no \| default*; Default: **default**) | 定義是否允許使用者同時擁有一個以上的 ppp 工作階段<ul><li>yes - 不允許使用者同時擁有一個以上的 ppp 工作階段</li><li>no - 允許使用者同時擁有一個以上的 ppp 工作階段</li><li>default - 從介面預設 profile 衍生此值；若此為介面預設 profile，則等同於 no</li></ul> |
| **outgoing-filter** (*string*; Default: ) | 傳出封包的防火牆 chain 名稱。指定的 chain 會取得傳往用戶端之每個封包的控制權。必須手動新增 PPP chain，並將 action=jump jump-target=ppp 的規則新增至其他相關 chain，此功能才會運作。詳情請參閱 Examples 章節。 |
| **parent-queue** (*none* \| *queue name*; Default: ) | 指定父佇列 |
| **queue-type** (*default \| ethernet-default \| wireless-default \| synchronous-default \|* *hotspot-default \| pcq-upload-default \| pcq-download-default \| only-hardware-queue \| multi-queue-ethernet-default \| default-small \| custom queue type name* ; Default: ) | 指定佇列類型。從 7.19 開始，可針對用戶端的 "upload" 與 "download" 分別指定 rx/tx 佇列類型。使用 / 設定個別佇列類型，第一個是 rx 佇列類型，第二個是 tx 佇列類型。 |
| **rate-limit** (*string*; Default: ) | 速率限制格式為 **rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]**，以路由器角度來看（因此 "rx" 是用戶端 upload，"tx" 是用戶端 download）。所有速率均以位元每秒為單位，除非後面接選用的 'k' 後綴（千位元每秒）或 'M' 後綴（百萬位元每秒）。若未指定 tx-rate，則 rx-rate 也會作為 tx-rate。tx-burst-rate、tx-burst-threshold 與 tx-burst-time 亦同。若 rx-burst-threshold 與 tx-burst-threshold 都未指定（但指定了 burst-rate），則 rx-rate 與 tx-rate 會作為突發臨界值。若 rx-burst-time 與 tx-burst-time 都未指定，則預設使用 1s。Priority 值為 1..8，其中 1 表示最高優先順序，8 表示最低。若未指定 rx-rate-min 與 tx-rate-min，則使用 rx-rate 與 tx-rate 值。rx-rate-min 與 tx-rate-min 值不得超過 rx-rate 與 tx-rate 值。 |
| **remote-address** (*IP*; Default: ) | 隧道位址，或從中將位址指派給遠端 ppp 介面的 [pool](/docs/cli-reference/ip/pool) 名稱。 |
| **remote-ipv6-prefix-pool** (*string \| none*; Default: **none**) | 從 IPv6 pool 指派前綴給用戶端，並安裝對應的 IPv6 路由。 |
| **session-timeout** (*time*; Default: ) | 連線可保持運作的最長時間。預設未設定時間限制。 |
| **use-compression** (*yes \| no \| default*; Default: **default**) | 指定是否使用資料壓縮。<ul><li>yes - 啟用資料壓縮</li><li>no - 停用資料壓縮</li><li>default - 從介面預設 profile 衍生此值；若此為介面預設 profile，則等同於 no</li></ul>此設定不會影響 OVPN 隧道。 |
| **use-encryption** (*yes \| no \| default \| require*; Default: **default**) | 指定是否使用資料加密。<ul><li>yes - 啟用資料加密</li><li>no - 停用資料加密</li><li>default - 從介面預設 profile 衍生此值；若此為介面預設 profile，則等同於 no</li><li>require - 明確要求加密</li></ul>此設定不適用於 OVPN 與 SSTP 隧道。 |
| **use-ipv6** (*yes \| no \| default \| require*; Default: **default**) | 指定是否允許 IPv6。預設會在安裝 IPv6 套件時啟用。<ul><li>yes - 啟用 IPv6 支援</li><li>no - 停用 IPv6 支援</li><li>default - 從介面預設 profile 衍生此值；若此為介面預設 profile，則等同於 no</li><li>require - 明確要求 IPv6 支援</li></ul> |
| **use-mpls** (*yes \| no \| default \| require*; Default: **default**) | 指定是否允許在 PPP 上使用 MPLS。<ul><li>yes - 啟用 MPLS 支援</li><li>no - 停用 MPLS 支援</li><li>default - 從介面預設 profile 衍生此值；若此為介面預設 profile，則等同於 no</li><li>require - 明確要求 MPLS 支援</li></ul> |
| **use-upnp** (*yes \| no \| default*; Default: **default**) | 指定是否允許 UPnP：<ul><li>yes - 啟用 UPnP。</li><li>no - 停用 UPnP。</li><li>default - 從介面預設 profile 衍生此值；若此為介面預設 profile，則等同於 no。</li></ul> |
| **wins-server** (*IP address*; Default: ) | 提供給 Windows 用戶端的 WINS 伺服器 IP 位址 |

### 附註 {#notes}

兩個預設 profile 無法移除：

```ros
[admin@rb13] /ppp/profile> print
Flags: * - default
 0 * name="default" use-compression=no use-encryption=no only-one=no
     change-tcp-mss=yes
 1 * name="default-encryption" use-compression=default use-encryption=yes
     only-one=default change-tcp-mss=default
[admin@rb13] /ppp/profile>
```

*incoming-filter* 與 *outgoing-filter* 參數會將動態 jump 規則新增至 chain *ppp*，其中 jump-target 參數會等於 profile 中的 *incoming-filter* 或 *outgoing-filter* 參數。因此，在變更這些參數之前，應先手動新增 chain *ppp*。

若使用 RADIUS 驗證，則會忽略 only-one 參數。

PPP 隧道使用 LCP 協定進行 MTU 協商，會在連線建立時立即發生。不支援 Framed MTU 屬性，因為它只會在使用 Radius 完成驗證後傳送。

## 使用者資料庫 {#user-database}

**子選單：** `/ppp/secret`

PPP 使用者資料庫會儲存 PPP 使用者存取記錄，並為每位使用者指派 PPP 使用者設定檔。

## 屬性 {#properties-1}

| 屬性 | 說明 |
| :-- | :-- |
| **caller-id** (*string*; Default: ) | 對 [PPTP](/docs/virtual-private-networks/pptp) 與 [L2TP](/docs/virtual-private-networks/l2tp) 而言，是用戶端必須從該 IP 位址連線。對 [PPPoE](/docs/virtual-private-networks/pppoe) 而言，是用戶端必須從該 MAC 位址連線（以大寫字母撰寫）。對 ISDN 而言，是用戶端可撥入的來電號碼（可能由電信業者提供，也可能未提供） |
| **comment** (*string*; Default: ) | 使用者的簡短說明。 |
| **disabled** (*yes \| no*; Default: **no**) | 是否使用該 secret。 |
| **limit-bytes-in** (*integer*; Default: **0**) | 用戶端在單一工作階段中可上傳的最大位元組數。 |
| **limit-bytes-out** (*integer*; Default: **0**) | 用戶端在單一工作階段中可下載的最大位元組數。 |
| **local-address** (*IP address*; Default: ) | 將在 ppp 介面上本機設定的 IP 位址。 |
| **name** (*string*; Default: ) | 用於驗證的名稱 |
| **password** (*string*; Default: ) *[sensitive](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters)* | 用於驗證的密碼 |
| **profile** (*string*; Default: **default**) | 要使用的 [使用者設定檔](#user-profiles) |
| **remote-address** (*IP*; Default: ) | 將指派給遠端 ppp 介面的 IP 位址。 |
| **remote-ipv6-prefix** (*IPv6 prefix*; Default: ) | 指派給 ppp 用戶端的 IPv6 前綴。該前綴會加入 [ND prefix list](/docs/system-information-and-utilities/neighbor-discovery)，在 ppp 介面上啟用 [stateless](/docs/getting-started/networking-fundamentals/ipv6-neighbor-discovery#stateless-address-autoconfiguration) 位址自動設定。 |
| **routes** (*string*; Default: ) | 用戶端連線時出現在伺服器上的路由。路由格式為：dst-address gateway metric（例如 10.1.0.0/ 24 10.0.0.1 1）。不接受其他語法，因為可能無法正確表示。可指定多筆路由，並以逗號分隔。對 [OpenVPN](/docs/virtual-private-networks/openvpn) 而言，此參數將被忽略。 |
| **service** (*any \| async \| isdn \| l2tp \| pppoe \| pptp \| ovpn \| sstp*; Default: **any**) | 指定特定使用者可使用的服務。 |

## 使用中使用者 {#active-users}

**子選單：** `/ppp/active`

此子選單可監控使用中（已連線）的使用者。

`/ppp/active/print` 指令會顯示目前所有已連線的使用者。

`/ppp/active/print stats` 指令會顯示接收／傳送的位元組與封包數

## 屬性 {#properties-2}

| 屬性 | 說明 |
| :-- | :-- |
| **address** (*IP 位址*) | 用戶端從伺服器取得的 IP 位址 |
| **bytes** (*整數*) | 透過此連線傳輸的位元組數。第一個數字表示從路由器角度來看傳送的流量，第二個數字則表示接收的流量。 |
| **caller-id** (*字串*) | 對於 [PPTP](/docs/virtual-private-networks/pptp) 與 [L2TP](/docs/virtual-private-networks/l2tp)，這是用戶端連入的 IP 位址。對於 [PPPoE](/docs/virtual-private-networks/pppoe)，這是用戶端連入的 MAC 位址。 |
| **encoding** (*字串*) | 顯示此連線使用的加密與編碼（若不對稱，則以 '/' 分隔） |
| **limit-bytes-in** (*整數*) | 允許使用者傳送至路由器的最大位元組數。 |
| **limit-bytes-out** (*整數*) | 允許使用者傳送至用戶端的最大位元組數。 |
| **name** (*字串*) | 在驗證階段提供的使用者名稱 |
| **packets** (*整數/整數*) | 透過此連線傳輸的封包數。第一個數字表示從路由器角度來看傳送的流量，第二個數字則表示接收的流量 |
| **service** (*async \| isdn \| l2tp \| pppoe \| pptp \| ovpn \| sstp*) | 使用者使用的服務類型。 |
| **session-id** (*字串*) | 顯示唯一的用戶端識別碼。 |
| **uptime** (*時間*) | 使用者的連線時間 |

## 遠端 AAA {#remote-aaa}

**子選單：** `/ppp/aaa`

此子選單中的設定可設定 RADIUS 計費與驗證。請注意，只有在本機使用者資料庫中找不到所需的使用者名稱時，才會查詢 RADIUS 使用者資料庫。

## 屬性 {#properties-3}

| 屬性 | 說明 |
| :-- | :-- |
| **accounting** (*yes \| no*；預設：**yes**) | 啟用 RADIUS 計費 |
| **interim-update** (*時間*；預設：**0s**) | Interim-Update 時間間隔 |
| **use-radius** (*yes \| no*；預設：**no**) | 透過 RADIUS 啟用使用者驗證。若在本機 secret 資料庫中找不到項目，則用戶端會透過 RADIUS 進行驗證。 |
| **enable-ipv6-accounting** (*yes \| no*；預設：**no**) | 啟用 IPv6 獨立計費。PPP 服務預設在向 RADIUS 伺服器回報網路使用量統計時，會將 Layer2、IPv4 與 IPv6 資料全部合併計算。若需要區分 IPv4 與 IPv6 流量，可以啟用此選項。其運作前提為必須透過 PPP 服務將前綴指派給用戶端，並且必須提供 rate-limit。動態建立的佇列統計會作為 IPv6 資料的計數器，隨後會以獨立 IPv6 統計屬性包含在計費封包中。對於由動態建立的 DHCPv6 伺服器因提供的前綴集區或 PPP/Profile 設定而指派的前綴，此功能無法運作。此時前綴指派是由 DHCP 服務處理，而非 PPP，因此計費無法由 PPP 服務管理。 |

## 範例 {#examples}

#### 新增設定檔 {#add-new-profile}

若要新增設定檔 ex，將 10.0.0.1 位址指派給路由器本身，並將 ex 集區中的位址指派給用戶端，同時透過 mypppclients 鏈篩選來自用戶端的流量：

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

#### 新增使用者 {#add-new-user}

若要新增使用者「ex」，密碼為「lkjrht」，且設定檔為「ex」，僅供 PPTP 服務使用，請輸入下列指令：

```ros
[admin@rb13] /ppp/secret> add name=ex password=lkjrht service=pptp profile=ex
[admin@rb13] /ppp/secret> print
Flags: X - disabled
 #   NAME                SERVICE CALLER-ID         PASSWORD          PROFILE            REMOTE-ADDRESS
 0   ex                  pptp                      lkjrht            ex                 0.0.0.0
[admin@rb13] /ppp/secret>
```
