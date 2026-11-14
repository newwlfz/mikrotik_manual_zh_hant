---
sidebar_key: "firewall-and-quality-of-service/connection-tracking"
sidebar_position: 3
title: "連線跟蹤"
sidebar_label: "連線跟蹤"
description: "MikroTik RouterOS 中的連線跟蹤透過監控邏輯網路連線來實現有狀態防火牆功能，並支援 NAT 及多種防火牆特性。它將封包歸入 new、established、related、invalid 或 untracked 等狀態，其中 FastTrack 可最佳化 TCP/UDP 封包的轉發。"
tags:
  - 'connection-tracking'
  - 'firewall'
  - 'fasttrack'
source: https://manual.mikrotik.com/docs/firewall-and-quality-of-service/connection-tracking
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

連線跟蹤允許核心跟蹤所有邏輯網路連線或會話，從而將可能組成該連線的所有封包關聯起來。

NAT 依賴此資訊以相同方式轉換所有相關封包。

藉助連線跟蹤，即使使用 UDP 等無狀態協定，你也可以使用有狀態防火牆功能。

### 受連線跟蹤影響的防火牆功能 {#firewall-features-affected-by-connection-tracking}

- NAT
- 防火牆：
  - connection-bytes
  - connection-mark
  - connection-type
  - connection-state
  - connection-limit
  - connection-rate
  - layer7-protocol
  - new-connection-mark
  - tarpit

跟蹤連線列表可在 IPv4 的 `/ip/firewall/connection` 和 IPv6 的 `/ipv6/firewall/connection` 中檢視。

```text
      [admin@3C22-atombumba] /ip/firewall/connection> print
      Flags: S - seen-reply, A - assured
      #    PR.. SRC-ADDRESS           DST-ADDRESS           TCP-STATE   TIMEOUT
      0    udp  10.5.8.176:5678       255.255.255.255:5678              0s
      1    udp  10.5.101.3:646        224.0.0.2:646                     5s
      2    ospf 10.5.101.161          224.0.0.5                         9m58s
      3    udp  10.5.8.140:5678       255.255.255.255:5678              8s
      4 SA tcp  10.5.101.147:48984    10.5.101.1:8291       established 4m59s

```

```text
      [admin@3C22-atombumba] /ipv6/firewall/connection> print
      Flags: S - seen reply, A - assured
      #    PRO.. SRC-ADDRESS                 DST-ADDRESS                 TCP-STATE
      0    udp   fe80::d6ca:6dff:fe77:3698   ff02::1
      1    udp   fe80::d6ca:6dff:fe98:7c28   ff02::1
      2    ospf  fe80::d6ca:6dff:fe73:9822   ff02::5

```

## 連線狀態 {#connection-states}

基於連線表條目，到達的封包可被分配為以下連線狀態之一：**new, invalid, established, related,** 或 **untracked**。

當封包被視為 **new** 時，有兩種不同判定方法。第一種適用於無狀態連線（如 UDP），此時連線表中沒有連線條目。另一種適用於有狀態協定（TCP）。在這種情況下，啟動新連線的新封包始終是帶有 *SYN* 標誌的 TCP 封包。

如果封包不是 new，它可能屬於 ***established*** 或 ***related*** 連線，也可能不屬於任何連線，從而成為 ***invalid***。處於 ***established*** 狀態的封包（正如大多數人已經猜到的那樣）屬於連線跟蹤表中的現有連線。***related*** 狀態非常相似，區別在於該封包屬於與某個現有連線相關的連線，例如 ICMP 錯誤封包或 FTP 資料連線封包。

連線狀態 **untracked** 是一種特殊情況：使用 **RAW** 防火牆規則將該連線從連線跟蹤中排除。此規則會使所有轉發流量繞過連線跟蹤，從而提高封包透過裝置的處理速度。

任何其他封包都會被視為 ***invalid***，在大多數情況下應被丟棄。

基於此資訊，我們可以設定一組基本過濾規則，透過接受 *established/related* 封包、丟棄 *invalid* 封包，並僅對 *new* 封包進行更詳細的過濾，來加快封包過濾並降低 CPU 負載。

```ros
/ip/firewall/filter
add chain=input connection-state=invalid action=drop comment="Drop Invalid connections"
add chain=input connection-state=established,related,untracked action=accept comment="Allow Established/Related/Untracked connections"
```

:::danger
此類規則集不得應用於採用非對稱路由的路由器，因為非對稱路由的封包可能被視為 invalid 並被丟棄。
:::

## FastTrack {#fasttrack}

IPv4 FastTrack 是一種特殊處理程式，可繞過 Linux 設施，從而實現更快的封包轉發。該處理程式用於透過 `fasttrack-connection` 動作標記的 **TCP** 和 **UDP** 連線。IPv4 FastTrack 處理程式支援 NAT（SNAT、DNAT 或兩者）。

請注意，並非連線的所有封包都能被 FastTrack，因此即使連線已標記為 FastTrack，你仍可能看到一些封包走慢速路徑。這就是為什麼 **fasttrack-connection** 後通常緊跟一條相同的 `action=accept` 規則。

FastTrack 處理過的封包會繞過：

- 防火牆。
- 連線跟蹤。
- 簡單佇列。
- 帶 *parent=global* 的佇列樹。
- IP 流量統計。
- IPSec。
- Hotspot 通用用戶端。
- VRF 分配。

管理員需確保 FastTrack 不會干擾其他配置。

### 要求 {#requirements}

滿足以下條件時，IPv4 FastTrack 處於活動狀態：

- 沒有 mesh、metarouter 介面配置。
- Sniffer、torch 或流量生成器未執行。
- 未主動使用 *`/tool/mac-scan`*。
- 未主動使用 *`/tool/ip-scan`*。
- 在 *IP/Settings* 下啟用了 FastPath 和 Route cache。

### 示例 {#example}

例如，對於採用出廠預設配置的 SOHO 路由器，你可以將以下規則放在防火牆過濾器頂部，對所有 LAN 流量進行 FastTrack。還需要相同的接受規則：

```ros
/ip/firewall/filter/add chain=forward action=fasttrack-connection connection-state=established,related
/ip/firewall/filter/add chain=forward action=accept connection-state=established,related
```

:::tip

- 連線會一直保持 FastTrack 狀態，直到連線關閉、超時或路由器重啟。
- 只有在 FastTrack 防火牆規則被刪除/停用並且路由器重啟後，虛擬規則才會消失。
- 當裝置上同時啟用 FastPath 和 FastTrack 時，同一時間只能有一個處於活動狀態。

**警告：** 佇列（父級為介面的佇列樹除外）、防火牆過濾器和 mangle 規則不會應用於 FastTrack 流量。
:::

## 連線跟蹤設定 {#connection-tracking-settings}

連線跟蹤設定透過 `/ip/firewall/connection/tracking` 選單管理。

#### 屬性 {#properties}

| 屬性 | 描述 |
| :-- | :-- |
| **enabled** (*yes \| no \| auto*; 預設：**auto**) | 允許停用或啟用連線跟蹤。停用連線跟蹤後，上面列出的防火牆功能將停止工作。如果設定為 "auto"，則在至少新增一條防火牆規則之前，連線跟蹤處於停用狀態。 |
| **liberal-tcp-tracking** (*yes \| no;* 預設：**no**) | 透過切換核心引數 `nf_conntrack_tcp_be_liberal` 來啟用或停用寬鬆 TCP 連線跟蹤。設定為 **yes** 時，系統僅將視窗外的 RST 段標記為 INVALID。**注意：** 啟用此設定可能會允許本來會被防火牆的 `connection-state` 匹配器視為 `invalid` 的畸形封包透過。這會增加暴露於某些規避技術的風險。僅在排查故障或規避已知問題時才應啟用此屬性。  |
| **loose-tcp-tracking** (*yes \| no*; 預設：**yes**) | `loose-tcp-tracking=yes` 時，未看到首個初始 SYN 的握手第 2 部分（SYN,ACK）和第 3 部分（ACK）將被視為 ESTABLISHED；`loose-tcp-tracking=no` 時，未看到首個初始 SYN 的第 2 部分（SYN,ACK）和第 3 部分（ACK）將被視為 INVALID |
| **tcp-syn-sent-timeout** (*time*; 預設：**5s**) | TCP SYN 超時。 |
| **tcp-syn-received-timeout** (*time*; 預設：**5s**) | TCP SYN 超時。 |
| **tcp-established-timeout** (*time*; 預設：**1d**) | 已建立 TCP 連線超時的時間。 |
| **tcp-fin-wait-timeout** (*time*; 預設：**10s**) |  |
| **tcp-close-wait-timeout** (*time*; 預設：**10s**) |  |
| **tcp-last-ack-timeout** (*time*; 預設：**10s**) |  |
| **tcp-time-wait-timeout** (*time*; 預設：**10s**) |  |
| **tcp-close-timeout** (*time*; 預設：**10s**) |  |
| **udp-timeout** (*time*; 預設：**30s**) | 指定僅在一個方向上看到封包的 UDP 連線的超時時間 |
| **udp-stream-timeout** (*time*; 預設：**3m**) | 指定在兩個方向上都看到封包的 UDP 連線的超時時間 |
| **icmp-timeout** (*time*; 預設：**10s**) | ICMP 連線超時 |
| **generic-timeout** (*time*; 預設：**10m**) | 所有其他連線條目的超時時間 |
| tcp-max-retrans-timeout |  |
| tcp-unacked-timeout |  |

**只讀屬性**

| 屬性 | 描述 |
| :-- | :-- |
| **max-entries** (*integer*) | 連線跟蹤表可容納的最大條目數。此值取決於已安裝的 RAM 容量。請注意，系統啟動時不會建立最大尺寸的連線跟蹤表；如果情況需要且系統仍有空閒 RAM，該表可能會增大，但大小不會超過 1048576 |
| **total-entries** (*integer*) | 連線表當前儲存的連線數量 |
| active-ipv4  | |
| active-ipv6  | |
| total-ip4-entries  | |
| total-ip6-entries  | |

## 連線列表 {#connection-list}

跟蹤連線列表可在 IPv4 的 `/ip/firewall/connection` 和 IPv6 的 `/ipv6/firewall/connection` 中檢視。

### 屬性 {#properties-1}

連線列表中的所有屬性均為只讀

| 屬性 | 描述 |
| :-- | :-- |
| **assured** (*yes \| no*) | 表示此連線為 assured，並且即使達到可跟蹤連線的最大數量，也不會被清除。 |
| **confirmed** (*yes \| no*) | 連線為 confirmed，並且有封包從裝置發出 |
| **connection-mark** (*string*) | 由 mangle 規則設定的連線標記。 |
| **connection-type** (*pptp \| ftp*) | 連線型別；如果連線跟蹤無法確定預定義連線型別，則該屬性為空。 |
| **dst-address** (*ip*) | 目標地址。 |
| **dst-port**(*integer*) | 目標埠。 |
| **dstnat** (*yes \| no*) | 連線經過了 DST-NAT（例如埠轉發）。 |
| **dying** (*yes \| no*) | 由於連線超時，該連線正在消亡。 |
| **expected** (*yes \| no*) | 連線是使用連線輔助程式（預定義服務規則）建立的。 |
| **fasttrack** (*yes \| no*) | 連線是否經過 FastTrack。 |
| **gre-key** (*integer*) | GRE Key 欄位的內容。 |
| **gre-protocol** (*string*) | 封裝載荷的協定。 |
| **gre-version** (*string*) | 連線中使用的 GRE 協定版本。 |
| **hw-offload**(*yes \| no*) | 硬體解除安裝連線。 |
| **icmp-code** (*string*) | ICMP Code 欄位 |
| **icmp-id** (*integer*) | 包含 ICMP ID |
| **icmp-type** (*integer*) | ICMP 型別編號 |
| **orig-bytes** (*integer*) | 使用該特定連線從源地址傳送的位元組數。 |
| **orig-fasttrack-bytes** (*integer*) | 使用該特定連線從源地址傳送的 FastTrack 位元組數。 |
| **orig-fasttrack-packets** (*integer*) | 使用該特定連線從源地址傳送的 FastTrack 封包數。 |
| **orig-packets** (*integer*) | 使用該特定連線從源地址傳送的封包數。 |
| **orig-rate** (*integer*) | 使用該特定連線從源地址傳送封包的資料速率。 |
| **protocol** (*string*) | IP 協定型別 |
| **repl-bytes** (*integer*) | 使用該特定連線從目標地址接收的位元組數。 |
| **repl-fasttrack-bytes** (*integer*) | 使用該特定連線從目標地址接收的 FastTrack 位元組數。 |
| **repl-fasttrack-packets** (*integer*) | 使用該特定連線從目標地址接收的 FastTrack 封包數。 |
| **repl-packets** (*integer*) | 使用該特定連線從目標地址接收的封包數。 |
| **repl-rate** (*string*) | 使用該特定連線從目標地址接收封包的資料速率。 |
| **reply-dst-address** (*ip*) | 返回封包預期的目標地址。 |
| **reply-dst-port**(*integer*) | 返回封包預期的目標埠。 |
| **reply-src-address** (*ip*) | 返回封包預期的源地址。 |
| ****reply-src-port**** (*integer*) | 返回封包預期的源埠。 |
| **seen-reply** (*yes \| no*) | 目標地址已回覆源地址。 |
| **src-address** (*ip*) | 源地址。 |
| **src-port**(*integer*) | 源埠。 |
| **srcnat** (*yes \| no*) | 連線經過 SRC-NAT，包括透過 NAT 進行偽裝的封包。 |
| **tcp-state** (*string*) | TCP 連線的當前狀態："established""time-wait""close""syn-sent""syn-recv""fin-wait""close-wait""last-ack""listen" |
| **timeout** (*time*) | 連線將從連線列表中移除的時間。 |
| **uses-helper**(*yes \| no*) | 已將 "IP/Firewall/Service Port" 輔助程式應用於該特定連線。 |
