---
sidebar_key: "virtual-private-networks/pppoe/index"
sidebar_position: 2
title: "PPPoE"
sidebar_label: "PPPoE"
description: "PPPoE 支援透過 PPP 和 MLPPP 跨乙太網鏈路進行 IPv6 字首委派，同時支援用戶端到伺服器和伺服器到用戶端兩種配置。它分發現階段和會話階段執行，使用 LCP/CHAP 身份驗證，並透過 IPCP 分配 IP 地址。MTU 相關考量可確保正確封裝，而身份驗證方法和按需撥號等用戶端屬性則增強了靈活性。"
tags:
  - 'pppoe'
  - 'discovery-phase'
  - 'mtu'
source: https://manual.mikrotik.com/docs/7.24/virtual-private-networks/pppoe
captured_at: '2026-11-04T11:34:45+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

本節介紹 PPPoE 示例。可使用這些示例透過 PPP 配置 IPv6 字首委派，以及透過一條或多條鏈路配置 MLPPP。

<DocCardList />

乙太網點對點（PPPoE）只是一種將 PPP 報文封裝到乙太網幀中的方法。PPPoE 是標準點對點協定（PPP）的擴充套件，也是 PPPoA 的後續協定。PPPoE 標準定義於 [RFC 2516](https://tools.ietf.org/html/rfc2516)。PPPoE 用戶端和伺服器可在路由器上的任意 Layer2 Ethernet 層介面上工作，例如 Wireless、Ethernet、EoIP 等。一般來說，PPPoE 用於根據使用者名稱（以及如果需要，根據工作站）認證向用戶端分配 IP 地址，而不是僅使用工作站認證並使用靜態 IP 地址或 DHCP。出於顯而易見的安全原因，建議不要在與 PPPoE 相同的介面上使用靜態 IP 地址或 DHCP。

## 簡介 {#introduction}

PPPoE 能夠透過簡單的橋接接入裝置將一組主機連線到遠端接入集中器。

支援的連線：

- MikroTik RouterOS PPPoE 用戶端連線到任意 PPPoE 伺服器。
- MikroTik RouterOS 伺服器（接入集中器）連線到多個 PPPoE 用戶端（用戶端幾乎適用於所有作業系統和大多數路由器）。

## PPPoE 工作過程 {#pppoe-operation}

PPPoE 有兩個不同的階段：

1. 發現階段。
2. 會話階段。

### 發現階段 {#discovery-phase}

發現階段有四個步驟。當該階段完成時，雙方都知道 PPPoE *SESSION\_ID* 和對端的 Ethernet 地址，這兩者共同唯一標識該 PPPoE 會話：

1. **PPPoE Active Discovery Initialization (PADI) -** PPPoE 用戶端向廣播地址傳送 *PADI* 報文。如果在 PPPoE 用戶端的撥號網路屬性中輸入了服務名稱，此報文還可以填充 "service-name" 欄位。如果未輸入服務名稱，則不會填充此欄位。
2. **PPPoE Active Discovery Offer (PADO) -** 如果接入集中器能夠處理 *PADI* 報文中列出的 "service-name" 欄位，則 PPPoE 伺服器或接入集中器應使用 *PADO* 響應 *PADI*。如果未列出 "service-name" 欄位，接入集中器將使用 *PADO* 報文進行響應，並將 "service-name" 欄位填充為接入集中器可提供的服務名稱。*PADO* 報文會發送到 PPPoE 用戶端的單播地址。
3. **PPPoE Active Discovery Request (PADR) -** 當收到 *PADO* 報文時，PPPoE 用戶端使用 *PADR* 報文進行響應。此報文會發送到接入集中器的單播地址。用戶端可能收到多個 *PADO* 報文，但用戶端會響應其收到的第一個有效 *PADO*。如果初始 *PADI* 報文的 "service-name" 欄位為空，用戶端會用 *PADO* 報文中返回的第一個服務名稱填充 *PADR* 報文的 "service-name" 欄位。
4. **PPPoE Active Discovery Session Confirmation (PADS) -** 當收到 *PADR* 時，接入集中器會為點對點協定（PPP）會話生成唯一的會話標識（ID），並在 *PADS* 報文中將此 ID 返回給 PPPoE 用戶端。此報文會發送到用戶端的單播地址。

### PPPoE 會話終止 {#pppoe-session-termination}

- **PPPoE Active Discovery Terminate (PADT) -** 可在會話建立後的任意時間傳送，以表示 PPPoE 會話已終止。伺服器或用戶端均可傳送。

### 會話階段 {#session-phase}

當發現階段完成後，雙方都知道 *PPPoE Session ID* 和對端的 *Ethernet（MAC）地址*，這兩者共同定義該 PPPoE 會話。PPP 幀被封裝在 PPPoE 會話幀中，這些幀的 Ethernet 幀型別為 **0x8864**。
當伺服器傳送確認且用戶端收到確認後，PPP 會話啟動，包括以下階段：

1. **LCP 協商**階段。
2. **認證（CHAP/PAP）**階段。
3. **IPCP 協商**階段 - 在此階段為用戶端分配 IP 地址。

:::warning
如果任一過程失敗，將重新開始 LCP 協商建立階段。
:::

PPPoE 伺服器向用戶端傳送 *Echo-Request* 報文以確定會話狀態，否則，在用戶端未傳送 *Terminate-Request* 報文就終止會話的情況下，伺服器將無法確定會話已終止。

## MTU {#mtu}

通常，可在不分片的情況下傳輸的最大 Ethernet 幀為 1500 位元組。PPPoE 又增加了 6 位元組開銷，PPP 欄位再增加兩位元組，因此為 IP 封包留下 1492 位元組。因此，PPPoE 的最大 MRU 和 MTU 值不得大於 1492。

TCP 棧會盡量避免分片，因此使用 MSS（最大報文段大小）。預設情況下，MSS 取為出介面的 MTU 減去 TCP 和 IP 頭部的通常大小（40 位元組），對於 Ethernet 介面，結果為 1460 位元組。不幸的是，可能存在 MTU 較低的中間鏈路，這會導致分片。在這種情況下，TCP 棧會執行路徑 MTU 發現。無法在不分片的情況下轉發封包的路由器應丟棄該報文，並向源主機發送 *ICMP-Fragmentation-Required*。當主機收到這樣的 ICMP 報文時，會嘗試降低 MTU。這在理想情況下應該可行；然而在現實環境中，許多路由器不會生成要求分片的封包；此外，許多防火牆會丟棄所有 ICMP 封包。

解決此問題的方法是在 MSS 過大時[調整 MSS](../../firewall-and-quality-of-service/firewall/mangle.md#change-mss)。

## PPPoE 用戶端 {#pppoe-client}

### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **ac-name** (*string*; Default: **""**) | 接入集中器名稱；可留空，此時用戶端將連線到廣播域中的任意接入集中器 |
| **add-default-route** (*yes\|no*; Default: **no**) | 啟用/停用是否自動新增預設路由 |
| **allow** (*mschap2\|mschap1\|chap\|pap*; Default: **mschap2,mschap1,chap,pap**) | 允許的認證方法，預設允許所有方法 |
| **default-route-distance** (*byte [0..255]*; Default:**1**) | 設定應用於自動建立預設路由的 distance 值，前提是同時選擇了 add-default-route |
| **dial-on-demand** (*yes\|no*; Default: **no**) | 僅在有出站流量時連線到 AC。如果選中，則在連線尚未建立時，將新增閘道器地址來自 10.112.112.0/24 網路的路由。 |
| **interface** (*string*; Default: ) | 用戶端將在其上執行的介面名稱 |
| **keepalive-timeout** (*integer*; Default:**10**) | 設定 keepalive 超時時間（秒）。 |
| **max-mru** (*integer*; Default: **1492**) | 最大接收單元 |
| **max-mtu** (*integer*; Default: **1492**) | 最大傳輸單元 |
| **mrru** (*integer: 512..65535\|disabled*; Default: **disabled**) | 鏈路上可接收的最大報文大小。如果報文大於隧道 MTU，它將被拆分為多個報文，從而允許透過隧道傳送完整大小的 IP 或 Ethernet 報文。 |
| **name** (*string*; Default: **pppoe-out[i]**) | PPPoE 介面名稱；如果未指定，則由 RouterOS 生成 |
| **password** (*string*; Default: ) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於認證的密碼 |
| **profile** (*string*; Default: **default**) | 指定建立隧道時將使用的 PPP 配置檔案。 |
| **service-name** (*string*; Default: **""**) | 指定接入集中器上設定的服務名稱；可留空以連線到任意 PPPoE 伺服器 |
| **use-peer-dns** (*yes\|no*; Default: **no**) | 啟用/停用從對端獲取 DNS 設定 |
| **user** (*string*; Default: **""**) | 用於認證的使用者名稱 |

### 狀態 {#status}

命令 `/interface/pppoe-client/monitor` 將顯示當前 PPPoE 狀態。

可用的只讀屬性：

| 屬性 | 描述 |
| :-- | :-- |
| **ac-mac** (*MAC address*) | 用戶端所連線接入集中器（AC）的 MAC 地址 |
| **ac-name** (*string*) | 接入集中器的名稱 |
| **active-links** (*integer*) | 繫結的 MLPPP 連線數（未使用 MLPPP 時為 '1'） |
| **encoding** (*string*) | 此連線使用的加密和編碼（如果不對稱，則用 '/' 分隔） |
| **local-address** (*IP Address*) | 分配給用戶端的 IP 地址 |
| **remote-address** (*IP Address*) | 分配給伺服器的遠端 IP 地址（即閘道器地址） |
| **mru** (*integer*) | 鏈路的有效 MRU |
| **mtu** (*integer*) | 鏈路的有效 MTU |
| **service-name** (*string*) | 使用的服務名稱 |
| **status** (*string*) | 當前鏈路狀態。可用值包括：dialing、verifying password...、connected、disconnected。 |
| **uptime** (*time*) | 連線時間，以天、小時、分鐘和秒顯示 |

### 掃描器 {#scanner}

PPPoE 掃描器允許掃描 layer2 廣播域中的所有活動 PPPoE 伺服器。執行掃描器的命令如下：

```ros
/interface/pppoe-client/scan [interface]
```

#### 可用的只讀屬性 {#available-read-only-properties}

| 屬性 | 描述 |
| :-- | :-- |
| **service** (*string*) | 伺服器上配置的服務名稱 |
| **mac-address** (*MAC*) | 檢測到的伺服器的 MAC 地址 |
| **ac-name** (*string*) | 接入集中器的名稱 |

:::warning
對於 Windows，某些連線說明可能使用這樣的形式：指定“電話號碼”，例如 "MikroTik\_AC\mt1"，以表示 "MikroTik\_AC" 是接入集中器名稱，"mt1" 是服務名稱。

**警告：** 指定 MRRU 意味著在單條鏈路上啟用 MP（Multilink PPP）。此協定用於將大報文拆分為較小報文。在 Windows 中，可在網路標籤頁的設定按鈕中啟用“為單鏈路連線協商多鏈路”。在 Windows 上，MRRU 硬編碼為 1614。此設定有助於克服 PathMTU 發現失敗。應在雙方對端上都啟用 MP 設定。
:::

## PPPoE 伺服器 {#pppoe-server}

PPPoE 伺服器配置中有兩類介面（隧道）項——靜態使用者和動態連線。為每個建立到給定伺服器的隧道建立一個介面。如果需要引用為特定使用者建立的特定介面名稱（在防火牆規則或其他位置），則會以管理方式新增靜態介面。每當使用者連線且其使用者名稱不匹配任何現有靜態條目時，動態介面會自動新增到此列表（或者如果該條目已處於活動狀態，因為不能有兩個單獨的隧道介面使用同一名稱引用——如果這是個問題，請設定 *one-session-per-host* 值）。動態介面在使用者連線時出現，並在使用者斷開後消失，因此無法在路由器配置中（例如在防火牆中）引用為該使用者建立的隧道，所以如果你需要為該使用者設定持久規則，請為其建立靜態條目。否則，使用動態配置是安全的。

:::warning
無論哪種情況，都必須正確配置 PPP 使用者——靜態條目不能替代 PPP 配置。
:::

### 接入集中器 {#access-concentrator}

**子選單：** `/interface/pppoe-server/server`

#### 屬性 {#properties-1}

| 屬性 | 描述 |
| :-- | :-- |
| **accept-untagged** (*yes \| no*; Default: **yes**) | 當指定了 `pppoe-over-vlan-range` 時，此設定控制 PPPoE 伺服器是否會在其介面上接受未打標籤（非 VLAN）的 PPPoE 報文。預設情況下，未打標籤的 PPPoE 報文會被接受。如果你使用 `pppoe-over-vlan-range` 屬性（該屬性啟用基於 802.1Q VLAN 的 PPPoE），此選項可讓你決定是否仍允許同一介面上的未打標籤用戶端。如果你不使用 `pppoe-over-vlan-range`，此設定沒有任何效果。 |
| **authentication** ( *mschap2 \| mschap1 \| chap \| pap*; Default: **"mschap2, mschap1, chap, pap"**) | 認證演算法。 |
| **default-profile** (*string*; 預設值： **"default"**) |  |
| **interface** (*string*; Default: **""**) | 用戶端所連線的介面。 |
| **keepalive-timeout** (*time*; Default: **"10", or disabled**) | 定義時間段（以秒為單位），超過該時間後，路由器開始每秒傳送 keepalive 報文。如果在該時間段內（即 2 \* keepalive-timeout）沒有流量且未收到 keepalive 響應，則無響應的用戶端被判定為斷開。**重要：** 在 LCP 握手成功後，用戶端會發送 LCP echo 報文以驗證 MTU 轉發；如果未收到回覆，則回退到備用 MTU 1480。新選項 `keepalive-timeout=disabled` 會停用傳送 echo 報文，從而有效關閉 MTU 測試。     |
| **max-mru** (*integer*; Default: **1480**) | 最大接收單元。最佳值是隧道所執行介面的 MTU 減去 20（因此，對於 1500 位元組的 Ethernet 鏈路，將 MTU 設定為 1480 以避免報文分片） |
| **max-mtu** (*integer*; Default: **1480**) | 最大傳輸單元。最佳值是隧道所執行介面的 MTU 減去 20（因此，對於 1500 位元組的 Ethernet 鏈路，將 MTU 設定為 1480 以避免報文分片） |
| **max-sessions** (*integer*; Default: **"0"**) | AC 可服務的最大用戶端數。'0' = 無限制。 |
| **mrru** (*integer: 512..65535 \| disabled*; Default: **"disabled"**) | 鏈路上可接收的最大報文大小。如果報文大於隧道 MTU，它將被拆分為多個報文，從而允許透過隧道傳送完整大小的 IP 或 Ethernet 報文。 |
| **one-session-per-host** (*yes \| no*; Default: **"no"**) | 每個主機僅允許一個會話（由 MAC 地址確定）。如果主機嘗試建立新會話，舊會話將被關閉。 |
| **pppoe-over-vlan-range** (*integer 1..4094*; Default: "") | 此設定允許 PPPoE 伺服器在 802.1Q VLAN 上執行。預設情況下，PPPoE 伺服器只接受其介面上的未打標籤報文。但是，在用戶端位於不同 VLAN 的場景中，無需建立多個 802.1Q VLAN 介面並將它們橋接在一起，也無需為每個 VLAN 配置單獨的 PPPoE 伺服器，你可以直接在 PPPoE 伺服器設定中指定所需的 VLAN。指定 VLAN ID 後，PPPoE 伺服器將接受來自用戶端的 802.1Q 帶標籤報文，並使用同一 VLAN 進行回覆。然後，你可以使用 `accept-untagged` 屬性選擇在同一介面上接受還是丟棄未打標籤的 PPPoE 用戶端。你甚至可以在 [VLAN 介面](../../bridging-and-switching/vlan.md) 上使用 `pppoe-over-vlan-range` 設定配置 PPPoE 伺服器，從而也支援 QinQ 部署。但請記住，內層 VLAN 標籤應為 802.1Q。該設定支援 VLAN ID 範圍，也支援使用逗號分隔值指定的單個 VLAN。例如：pppoe-over-vlan-range=100-115,120,122,128-130。**注意：** 避免在介面上配置帶有 `pppoe-over-vlan-range` 的伺服器，同時又建立 VLAN ID 落在該範圍內的 VLAN 介面。例如：  `/interface/vlan``add interface=ether2 name=vlan15 vlan-id=15``/interface/pppoe-server/server``add disabled=no interface=ether2 pppoe-over-vlan-range=10-20`  如果你需要這種設定，請從 `pppoe-over-vlan-range` 中移除重疊的 VLAN ID，並直接在 VLAN 介面上建立單獨的 PPPoE 伺服器例項，如下所示：  `/interface/vlan``add interface=ether2 name=vlan15 vlan-id=15``/interface/pppoe-server/server``add disabled=no interface=ether2 pppoe-over-vlan-range=10-14,16-20``add disabled=no interface=vlan15`    |
| **service-name** (*string*; Default: **""**) | PPPoE 服務名稱。伺服器將接受傳送的 PADI 報文中服務名稱與此設定匹配的用戶端，或者 PADI 報文中的 service-name 欄位未設定的用戶端。 |

PPPoE 伺服器（接入集中器）支援為每個介面配置多個伺服器——使用不同的服務名稱。用戶端使用接入集中器名稱和 PPPoE 服務名稱來標識要註冊的接入集中器。接入集中器名稱與命令提示符前顯示的路由器身份相同。身份可以在 *`/system/identity`* 子選單中設定。

:::danger
不要為接收 PPPoE 請求的介面分配 IP 地址。
:::

指定 MRRU 意味著在單條鏈路上啟用 MP（Multilink PPP）。此協定用於將大報文拆分為較小報文。MRRU 硬編碼為 1614。此設定有助於克服 PathMTU 發現失敗。應在雙方對端上都啟用 MP 設定。

:::warning
預設的 *keepalive-timeout* 值 10s 在大多數情況下沒問題。如果將其設定為 0，路由器將不會斷開用戶端，直到用戶端顯式登出或路由器重啟。要解決此問題，可以使用 one-session-per-host 屬性。
:::

## 快速示例 {#quick-example}

![](/img/a34ca577e7a80a70.jpg)

### PPPoE 用戶端 {#pppoe-client-1}

要將 MikroTik RouterOS 配置為 PPPoE 用戶端，只需按示例新增一個 PPPoE 用戶端並設定以下引數：

```ros
[admin@MikroTik] > interface pppoe-client add interface=ether2 password=StrongPass service-name=pppoeservice name=PPPoE-Out disabled=no user=MT-User
[admin@MikroTik] > interface pppoe-client print
Flags: X - disabled, I - invalid, R - running 
 0  R name="PPPoE-Out" max-mtu=auto max-mru=auto mrru=disabled interface=ether2 user="MT-User" 
      password="StrongPass" profile=default keepalive-timeout=10 service-name="pppoeservice" ac-name="" 
      add-default-route=no dial-on-demand=no use-peer-dns=no allow=pap,chap,mschap1,mschap2
```

### PPPoE 伺服器 {#pppoe-server-1}

要將 MikroTik RouterOS 配置為接入集中器（PPPoE 伺服器）：

- 為用戶端新增 IP 地址池，範圍為 10.0.0.2-10.0.0.5。
- 新增 PPP 配置檔案。
- 新增 PPP secret（使用者名稱/密碼）。
- 新增 PPPoE 伺服器本身。

```ros
[admin@MikroTik] > /ip/pool
add name=pppoe-pool ranges=10.0.0.2-10.0.0.5
[admin@MikroTik] > /ppp/profile
add local-address=10.0.0.1 name=for-pppoe remote-address=pppoe-pool
[admin@MikroTik] > /ppp/secret
add name=MT-User password=StrongPass profile=for-pppoe service=pppoe
[admin@MikroTik] > /interface/pppoe-server/server
add default-profile=for-pppoe disabled=no interface=ether3 service-name=pppoeservice
```

## 說明 {#notes}

不建議在一臺裝置上使用大量 PPPoE 用戶端。
