---
sidebar_key: "firewall-and-quality-of-service/firewall/raw"
sidebar_position: 7
title: "RAW"
sidebar_label: 'RAW'
description: 'The RAW firewall table in RouterOS processes packets before connection tracking. Use it to drop unwanted packets early, or to exclude traffic from connection tracking with action=notrack.'
tags:
  - 'firewall'
  - 'raw'
source: https://manual.mikrotik.com/docs/firewall-and-quality-of-service/firewall/raw
---

防火牆 RAW 表會在[連線追蹤](/docs/firewall-and-quality-of-service/connection-tracking)之前處理封包。它有兩種用途：

- 在連線追蹤以及 mangle、NAT 與 filter 規則處理之前，先丟棄不要的封包。
- 使用 `action=notrack` 將流量排除於連線追蹤之外。

在上述兩種情況下，路由器都不會為該封包建立連線追蹤項目。

RAW 規則在 IPv4 上位於 `/ip/firewall/raw`，在 IPv6 上位於 `/ipv6/firewall/raw`。此表有兩個內建鏈：

- **prerouting** - 進入路由器的每個封包，包括要給路由器本身的封包與通過路由器的封包。
- **output** - 路由器本身送出的封包。

RAW 規則不具狀態：每條規則各自檢視每個封包，並不知道該封包屬於哪個連線。

## 在連線追蹤之前丟棄不要的流量

丟棄從網際網路進來、且來源位址在該處永遠不可能合法的封包。`WAN` 是預設設定中包含網際網路埠的介面清單：

```ros
/ip/firewall/address-list
add list=bad_src address=0.0.0.0/8 comment="This network"
add list=bad_src address=127.0.0.0/8 comment="Loopback"
add list=bad_src address=224.0.0.0/4 comment="Multicast"
add list=bad_src address=240.0.0.0/4 comment="Reserved"
/ip/firewall/raw
add chain=prerouting action=drop in-interface-list=WAN \
    src-address-list=bad_src comment="Drop invalid source addresses"
```

此規則會丟棄來自這些位址、從 WAN 進入的每個封包，且是在路由器為其建立連線追蹤項目之前。由於此規則不具狀態，它也會丟棄您自己的主機對這些位址開啟之連線的回覆封包。只把絕對不能連到您的位址放入清單。如需維護清單，請參閱 [位址清單](/docs/firewall-and-quality-of-service/firewall/address-lists)。

若要確認規則是否生效，請查看其計數器：

```ros
[admin@MikroTik] > /ip/firewall/raw/print stats
Flags: D - DYNAMIC
Columns: CHAIN, ACTION, BYTES, PACKETS
#   CHAIN       ACTION       BYTES  PACKETS
;;; special dummy rule to show fasttrack counters
0 D prerouting  passthrough      0        0
;;; Drop invalid source addresses
1   prerouting  drop           168        3
```

最上方的動態規則屬於 [FastTrack](/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fasttrack)。若要將計數器歸零，請使用 `/ip/firewall/raw/reset-counters-all`。

若要偵測並丟棄針對單一目的地的洪水攻擊，請參閱 [DDoS 防護](/docs/firewall-and-quality-of-service/user-guides/ddos-protection)。

## 將流量排除於連線追蹤之外

在兩個區域網路之間路由的路由器，只要不對該流量套用 NAT 與具狀態過濾，就不需要對該流量進行連線追蹤。在此範例中，網路為 192.168.88.0/24 與 192.168.99.0/24。

此範例適用於未對此流量啟用 FastTrack 的路由器，例如，因為您移除了 FastTrack 規則，以便在該路由器上使用佇列。預設設定中有一條針對已建立連線的 FastTrack 規則，而 FastTrack 規則不會比對未追蹤的封包，因此下列規則會讓該流量在該路由器上不經過 FastTrack。

一條連線的封包會雙向流動，因此請為每個方向各新增一條規則：

```ros
/ip/firewall/raw
add chain=prerouting action=notrack src-address=192.168.88.0/24 \
    dst-address=192.168.99.0/24 comment="Do not track LAN to LAN"
add chain=prerouting action=notrack src-address=192.168.99.0/24 \
    dst-address=192.168.88.0/24 comment="Do not track LAN to LAN"
```

符合 `action=notrack` 的封包會繼續通過其餘 RAW 規則，以及 mangle 與 filter 規則，但路由器不會在 `/ip/firewall/connection` 中為它們建立項目。在 mangle 與 filter 中，它們的連線狀態為 `untracked`。

filter 規則必須接受未追蹤的封包。預設設定會這麼做：其在 input 與 forward 鏈中接受 established 與 related 連線的規則也會列出 `untracked`。檢查您的防火牆：

```ros
[admin@MikroTik] > /ip/firewall/filter/print where connection-state~"untracked"
0  ;;; defconf: accept established,related,untracked
   chain=input action=accept connection-state=established,related,untracked

1  ;;; defconf: accept established,related, untracked
   chain=forward action=accept connection-state=established,related,untracked
```

如果您自己的規則只接受 established 與 related 連線，請將 `untracked` 加入這些規則：

```ros
/ip/firewall/filter
set [find action=accept connection-state="established,related"] \
    connection-state=established,related,untracked
```

若要確認流量已不再被追蹤，請從另一個網路對 192.168.88.0/24 中的主機執行 ping 五次。ping 完成後，立即統計兩個網路之間的連線項目：

```ros
/ip/firewall/connection/print count-only \
    where src-address~"^192.168.99\\." and dst-address~"^192.168.88\\."
```

命令會輸出 `0`。若沒有 `notrack` 規則，同一個 ping 會留下一個項目，該項目會在最後一個封包之後 10 秒到期。計數器不取決於時間點，而 `notrack` 規則會顯示每個方向的五個封包：

```ros
[admin@MikroTik] > /ip/firewall/raw/print stats
Flags: D - DYNAMIC
Columns: CHAIN, ACTION, BYTES, PACKETS
#   CHAIN       ACTION       BYTES  PACKETS
;;; special dummy rule to show fasttrack counters
0 D prerouting  passthrough      0        0
;;; Drop invalid source addresses
1   prerouting  drop           168        3
;;; Do not track LAN to LAN
2   prerouting  notrack        280        5
;;; Do not track LAN to LAN
3   prerouting  notrack        280        5
```

:::warning
未追蹤的封包沒有連線，因此所有依賴連線的功能都不適用於它們：

- NAT 規則不會處理它們。請勿對需要來源或目的 NAT 的流量使用 `notrack`，例如經由 masquerade 規則送出的流量。
- 會讀取連線項目的比對條件（例如 `connection-mark`）不會比對到它們，而 `action=mark-connection` 對它們沒有作用。`connection-state=untracked` 會比對到它們。
:::

新增規則時已開啟的連線會繼續運作。從那時起，它們的封包會變成未追蹤，舊項目則會留在連線表中，直到逾時為止。新增規則的期間，防火牆可能會將這些連線的少數封包視為 invalid 而丟棄。

### 排除單一服務

當你排除單一服務而非整個網路時，回覆的規則必須符合伺服器的來源位址與來源埠。例如，排除伺服器 192.168.88.2 使用 UDP 的 DNS 流量：

```ros
/ip/firewall/raw
add chain=prerouting action=notrack protocol=udp dst-port=53 \
    dst-address=192.168.88.2 comment="Do not track DNS queries"
add chain=prerouting action=notrack protocol=udp src-port=53 \
    src-address=192.168.88.2 comment="Do not track DNS replies"
```

若要檢查規則，請從其他網路透過伺服器解析名稱，並查看計數器。每條規則會計數一個封包：

```ros
[admin@MikroTik] > /ip/firewall/raw/print stats where comment~"DNS"
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN       ACTION   BYTES  PACKETS
;;; Do not track DNS queries
2 prerouting  notrack     54        1
;;; Do not track DNS replies
3 prerouting  notrack     70        1
```

在沒有第二條規則的情況下，回覆仍會被追蹤。連線追蹤並未看到查詢，因此會將 UDP 回覆視為從伺服器到用戶端的新連線，並為其建立項目。對於 TCP 服務，連線追蹤會將回覆視為無效，而預設防火牆會將其丟棄。

當服務在路由器本身執行時，回覆不會通過 prerouting 鏈。請將回覆的規則放在 output 鏈中。在此範例中，路由器的位址為 192.168.88.1：

```ros
/ip/firewall/raw
add chain=prerouting action=notrack protocol=udp dst-port=53 \
    dst-address=192.168.88.1 comment="Do not track DNS to the router"
add chain=output action=notrack protocol=udp src-port=53 \
    src-address=192.168.88.1 comment="Do not track DNS from the router"
```

## 在鏈中將規則分組

規則可以分組到自訂鏈中。當你新增第一條具有新鏈名稱的規則時，RouterOS 會建立該鏈。封包會透過帶有 `action=jump` 的規則進入鏈。它會透過 `action=return` 回到呼叫鏈的下一條規則，或在到達鏈尾時返回。若沒有 jump 規則導向某個鏈，該鏈中的規則就不會被處理。

將從網際網路抵達的 UDP 封包導向一個鏈，該鏈會丟棄常被濫用於放大攻擊的服務所產生的回覆：Chargen（埠 19）、SSDP（埠 1900）與 Memcached（埠 11211）。來自清單 `trusted` 中位址的封包會略過檢查：

```ros
/ip/firewall/address-list
add list=trusted address=198.51.100.20 comment="Office router"
/ip/firewall/raw
add chain=prerouting action=jump jump-target=udp-check \
    in-interface-list=WAN protocol=udp comment="Check UDP from the WAN"
add chain=udp-check action=return src-address-list=trusted \
    comment="Do not check trusted addresses"
add chain=udp-check action=drop protocol=udp src-port=19,1900,11211 \
    comment="Drop replies of common amplification services"
```

計數器會顯示進入鏈的封包數量，以及這些封包的處理結果。此處有兩個 UDP 封包進入鏈。其中一個的來源埠為 1900，已被丟棄；另一個到達鏈尾並返回：

```ros
[admin@MikroTik] > /ip/firewall/raw/print stats
Flags: D - DYNAMIC
Columns: CHAIN, ACTION, BYTES, PACKETS
#   CHAIN       ACTION       BYTES  PACKETS
;;; special dummy rule to show fasttrack counters
0 D prerouting  passthrough      0        0
;;; Drop invalid source addresses
1   prerouting  drop           168        3
;;; Do not track LAN to LAN
2   prerouting  notrack        280        5
;;; Do not track LAN to LAN
3   prerouting  notrack        280        5
;;; Check UDP from the WAN
4   prerouting  jump           292        2
;;; Do not check trusted addresses
5   udp-check   return           0        0
;;; Drop replies of common amplification services
6   udp-check   drop            57        1
```

## IPv6

IPv6 RAW 表是獨立的，並且具有相同的鏈與動作。例如，丟棄從網際網路進入且來源位址為文件專用前綴的封包：

```ros
/ipv6/firewall/raw
add chain=prerouting action=drop in-interface-list=WAN \
    src-address=2001:db8::/32 comment="Drop the documentation prefix"
```

比對器有幾處不同。IPv6 規則具有 `headers` 與 `hop-limit`。它們沒有 `fragment`、`hotspot`、`ipv4-options`、`psd` 與 `ttl`。

## RAW 規則的行為

### 在封包流程中的位置

RAW 規則是封包在 IP 防火牆中遇到的第一批規則。完整流程圖請參閱 [RouterOS 中的封包流程](/docs/firewall-and-quality-of-service/packet-flow-in-routeros)。此位置有以下影響：

- 由於連線追蹤尚未處理到此封包，RAW 規則沒有依賴連線追蹤的比對器。
- NAT 尚未套用。在 prerouting 鏈中，`dst-address` 是封包在目的 NAT 之前的目的位址。
- 在 RAW 表中丟棄的封包不會建立連線追蹤項目。

### 規則處理

規則會從鏈頂端依序處理。`accept`、`drop` 與 `notrack` 的差異在於後續處理方式：

- `accept` - 封包會略過其餘的 RAW 規則，並繼續交由連線追蹤處理。
- `drop` - 封包會被捨棄。
- `notrack` - 封包會被標記為繞過連線追蹤，並繼續前往下一條 RAW 規則。

其他動作（`log`、`passthrough`、`add-src-to-address-list` 與 `add-dst-to-address-list`）會執行各自的處理，並將封包傳遞至下一條規則。`jump` 與 `return` 則會在鏈之間移動封包。

沒有 `action` 的規則會接受封包。未符合任何規則的封包也會被接受。

路由器會拒絕 prerouting 鏈中含有 `out-interface` 的規則，以及 output 鏈中含有 `in-interface` 的規則。

### 與 filter 的差異

| | Filter | RAW |
| :-- | :-- | :-- |
| 內建鏈 | input, forward, output | prerouting, output |
| 位置 | 連線追蹤之後 | 連線追蹤之前 |
| 依賴連線追蹤的比對條件 | 是 | 否 |
| 另一個表所缺少的動作 | `fasttrack-connection`, `reject`, `tarpit` | `notrack` |

下列 filter 屬性無法在 RAW 表中使用：`connection-bytes`、`connection-limit`、`connection-mark`、`connection-nat-state`、`connection-rate`、`connection-state`、`connection-type`、`hw-offload`、`layer7-protocol`、`p2p`、`realm`、`reject-with` 與 `routing-mark`。

### 分段封包

IPv4 與 IPv6 的 RAW 規則對分段封包的處理方式不同：

- **IPv4**：RAW 規則會在封包組裝前，將每個分段視為獨立個體來檢視，即使已啟用連線追蹤也是如此。`fragment=yes` 會比對除了第一個以外的所有分段，而 `packet-size` 比對的是單一分段的大小，而非整個封包的大小。經過 RAW 表之後，連線追蹤會組裝封包，其他防火牆表看到的則是一個完整封包。
- **IPv6**：RAW 規則看到的是已組裝的封包。

以 `action=notrack` 繞過連線追蹤的 IPv4 封包不會被組裝。當路由器轉送此類封包時，它在 mangle 與 filter 規則中仍保持分段狀態，且只有第一個分段帶有埠號。送往路由器本身的封包則會在 input 鏈之前完成組裝。

## 延伸閱讀

- [Filter](/docs/firewall-and-quality-of-service/firewall/filter)
- [Address lists](/docs/firewall-and-quality-of-service/firewall/address-lists)
- [Connection tracking](/docs/firewall-and-quality-of-service/connection-tracking)
- [Building advanced firewall](/docs/firewall-and-quality-of-service/user-guides/building-advanced-firewall)

如需所有規則屬性的說明，請參閱 [`/ip/firewall/raw`](/docs/cli-reference/ip/firewall/raw/) 與 [`/ipv6/firewall/raw`](/docs/cli-reference/ipv6/firewall/raw/) 的 CLI 參考文件。
