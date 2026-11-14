---
sidebar_key: "cli-reference/interface/vrrp"
sidebar_position: 38
title: "vrrp"
sidebar_label: 'vrrp'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/interface/vrrp
captured_at: '2026-11-01T21:23:08+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/vrrp {#interfacevrrp}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">VRRP 介面已被使用者停用。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">VRRP 介面處於 invalid 狀態，例如由於配置錯誤。</ArgTableRow>
<ArgTableRow arg="G" typ="grp-authority">VRRP 介面為 `group-authority`。它控制其他組成員的狀態，並且是唯一發送 VRRP 通告的介面。</ArgTableRow>
<ArgTableRow arg="g" typ="grp-member">VRRP 介面是組成員。其狀態機跟隨指定 `group-authority` 介面的狀態。</ArgTableRow>
<ArgTableRow arg="R" typ="running">running.</ArgTableRow>
<ArgTableRow arg="M" typ="master">VRRP 介面處於 master 狀態。</ArgTableRow>
<ArgTableRow arg="B" typ="backup">VRRP 介面處於 backup 狀態。</ArgTableRow>
<ArgTableRow arg="F" typ="failure">VRRP 介面處於 failure 狀態，例如由於其父介面 link-down。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">VRRP 介面名稱。</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }">[地址解析協定](../../getting-started/networking-fundamentals/index.md#arp-and-tying-it-all-together) 模式。</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">在未從 IP 收到封包後，ARP 記錄在 ARP 表中保留多長時間。值 `auto` 等於 IP/Settings 中 `arp-timeout` 的值，預設為 30s。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">VRRP 例項將在其上執行的介面名稱。</ArgTableRow>
<ArgTableRow arg="group-master" typ="iface_enum { :0, none:0, self }">deprecated.</ArgTableRow>
<ArgTableRow arg="group-authority" typ="iface_enum { :0, none:0, self }">
允許將多個 VRRP 介面分組，以便它們共享相同的 VRRP 狀態。在一個組內，會選擇一個組權威介面。它控制其他組成員的狀態，並且是唯一發送 VRRP 通告的介面。當 group-authority VRRP 介面轉換到 backup 狀態時，所有組成員也會轉換到 backup 狀態。如果在任何組成員上檢測到故障，例如由於其父介面 link-down，則所有組成員都會轉換到 failure 狀態。
- `none` - VRRP 介面不進行分組，並以其自身的 VRRP 狀態機獨立執行。
- `self` - VRRP 介面充當組權威。它控制其他已分組 VRRP 介面的狀態機，並負責傳送和接收 VRRP 通告。
- `vrrp-interface` - VRRP 介面是組成員。其狀態機跟隨指定 VRRP 介面的狀態。
</ArgTableRow>
<ArgTableRow arg="vrid" typ="num">虛擬路由器識別符號。每個虛擬路由器必須具有唯一的 id 編號。</ArgTableRow>
<ArgTableRow arg="priority" typ="num">Master 選舉演算法中使用的 VRRP 節點優先順序。數字越大表示優先順序越高。`255` 保留給擁有 VR IP 的路由器，`0` 保留給 Master 路由器，以表示其正在釋放職責。</ArgTableRow>
<ArgTableRow arg="interval" typ="time">
VRRP interval 定義 VRRP master 路由器向 backup 路由器傳送 Advertisement 封包的頻率。此間隔直接決定 backup 接收 keepalive 資訊的頻率，這些資訊確認 master 正在執行。
較短的間隔會提高 Advertisement 封包的傳送速率，從而可以更快地檢測到 master 故障，但也會增加對封包丟失、處理延遲和計時器不準確的敏感度。較長的間隔會減少控制流量並提高穩定性，但代價是故障轉移檢測更慢。Master Down 間隔由配置的 VRRP interval 和路由器優先順序推匯出來，其計算會允許在觸發故障轉移前錯過多個 Advertisement。

**警告：** 將 VRRP interval 配置為低於 1 秒可能導致不可預測的行為和意外的 master 角色變更。
</ArgTableRow>
<ArgTableRow arg="preemption-mode" typ="bool">master 節點是否始終具有優先權。設定為 `no` 時，即使 backup 節點具有更高優先順序，在當前 master 發生故障之前，也不會將 backup 節點選舉為 master。</ArgTableRow>
<ArgTableRow arg="authentication" typ="enum (none | simple | ah) { none:0, simple:1, ah:2 }">
用於 VRRP 通告封包的認證方法。
- `none` - 僅在低安全性網路中使用，例如 LAN 上的兩個 VRRP 節點。
- `ah` - IP Authentication Header。此演算法針對配置錯誤、重放攻擊以及封包損壞或修改提供強保護。當你對 LAN 上節點的管理控制有限時，應使用它。使用 HMAC-MD5。
- `simple` - 使用明文密碼。防止本地網路上路由器的意外錯誤配置。
</ArgTableRow>
<ArgTableRow arg="password" typ="string">認證所需的密碼。如果未使用認證，則可以忽略。</ArgTableRow>
<ArgTableRow arg="on-backup" typ="alt { script: string
 }">節點切換到 backup 狀態時要執行的指令碼。</ArgTableRow>
<ArgTableRow arg="on-master" typ="alt { script: string
 }">節點切換到 master 狀態時要執行的指令碼。</ArgTableRow>
<ArgTableRow arg="on-fail" typ="alt { script: string
 }">節點發生故障時要執行的指令碼。</ArgTableRow>
<ArgTableRow arg="version" typ="enum (2 | 3) { 2:2, 3:3 }">要使用的 VRRP 版本。</ArgTableRow>
<ArgTableRow arg="v3-protocol" typ="enum (ipv4 | ipv6) { ipv4:1, ipv6:2 }">VRRPv3 將使用的協定。僅當 `version` 為 3 時有效。</ArgTableRow>
<ArgTableRow arg="v3-checksum-as-v2" typ="bool">
控制 VRRPv3 IPv4 校驗和的計算是否包含 IPv4 偽首部。
不同供應商對 RFC 5798 第 5.2.8 節中有關 IPv4 校驗和計算中偽首部的解釋不同。基於 Linux 的實現（包括 FRR）會為 IPv4 和 IPv6 都包含偽首部，而 Cisco 僅為 IPv6 包含偽首部。
- `no`（預設）- 在校驗和計算中包含 IPv4 偽首部。與其他基於 Linux 的 VRRPv3 實現相容。
- `yes` - 在校驗和計算中排除 IPv4 偽首部。與 Cisco 及其他不為 IPv4 包含偽首部的供應商相容時使用此設定。

此設定僅適用於使用 IPv4 的 VRRPv3。它對 VRRPv3 IPv6 或 VRRPv2 沒有影響。

同一虛擬路由器中的所有 VRRP 路由器必須對此設定使用相同的值。值不匹配會導致 "bad checksum" 錯誤，並且 VRRP 通告封包將被丟棄。
</ArgTableRow>
<ArgTableRow arg="sync-connection-tracking" typ="bool">將連線跟蹤條目從 Master 同步到 Backup 裝置。VRRP 連線跟蹤同步要求 RouterOS 連線跟蹤正在執行。</ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr">
指定另一臺 VRRP 路由器的遠端地址，用於連線跟蹤同步。如果未設定，系統會透過 VRRP 自動檢測遠端地址。僅當啟用了 `sync-connection-tracking` 時才會使用遠端地址。顯式設定遠端地址有以下好處：
- 連線跟蹤同步啟動更快，因為無需等待 VRRP 的初始訊息交換來檢測遠端地址。
- VRRP Master 選舉更快。
- 連線跟蹤資料可以透過不同的網路介面傳送，例如兩臺路由器之間的專用安全線路。
同步連線跟蹤使用 UDP 埠 8275。
</ArgTableRow>
<ArgTableRow arg="connection-tracking-mode" typ="enum (passive-active | active-active) { passive-active:0, active-active:1 }">
指定連線跟蹤同步的模式。此設定僅在啟用了 `sync-connection-tracking` 時相關。
- `passive-active` - 將此模式用於傳統 VRRP 設定，即使用一個 master 和一個或多個 backup 路由器。在此模式下，只有 master 裝置透過向 backup 裝置傳送更新來執行連線跟蹤同步。Backup 裝置不傳送連線跟蹤資料。
- `active-active` - 將此模式用於具有多個 VRRP 組以實現負載均衡的設定。每個 VRRP 組都有自己的 master，而這些 master 可以位於不同的物理裝置上。在 active-active 模式下，所有活動 master 可以相互同步連線跟蹤資料。active-active 模式下的每個 VRRP 組必須使用唯一的 connection-tracking-port 值。在多個組之間重複使用同一埠可能導致連線跟蹤表不同步。

將多個 VRRP 組與 **passive-active** 模式一起使用可能導致連線跟蹤表不同步，因為只有一個 master 處理同步，其他 master 不交換跟蹤資料。
</ArgTableRow>
<ArgTableRow arg="connection-tracking-port" typ="num">指定用於連線跟蹤同步的 UDP 埠。此設定僅在啟用了 `sync-connection-tracking` 時相關。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="mtu" typ="num">Layer3 MTU 大小。VRRP 介面始終使用 slave 介面的 MTU。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">VRRP 介面的 MAC 地址。</ArgTableRow>
</ArgTable>
