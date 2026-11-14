---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/torch"
sidebar_position: 3
title: "Torch"
sidebar_label: "Torch"
description: "Torch 顯示當前經過一個介面的流量，按地址、協定、埠和 DSCP 分組為流，並顯示每個方向上的速率。找出佔用頻寬的主機，監視某個協定或埠，檢查 VLAN 標籤和 DSCP 標記，檢視防火牆丟棄的流量，並檢視由哪個 CPU 處理。"
tags:
  - 'traffic-monitoring'
  - 'ipv6'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/torch
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Torch 顯示當前透過某個介面的流量。它把封包按流分組，每一行對應地址、協定、埠和 DSCP 值的一種組合，並顯示每條流在兩個方向上的速率。用它來查明誰在使用某條鏈路、鏈路上執行哪些協定，或者某個連線的報文是否到達。

Torch 在防火牆過濾之前就看到收到的報文，因此被防火牆規則丟棄的流量仍會顯示在其到達的介面上。路由器發出的報文在離開時被計數，因此在 forward 鏈中被丟棄的流量不會出現在出介面上。Torch 執行期間，路由器會關閉 IP fast path 和 FastTrack，與使用[封包嗅探器](./packet-sniffer.md)時一樣；在繁忙的路由器上，這段時間 CPU 負載會升高。若要檢視報文內容或將其儲存到檔案，請改用封包嗅探器。

Torch 會一直執行，直到你用 <kbd>Control</kbd>+<kbd>C</kbd> 停止它。若要在一段設定時間後停止，請新增 `duration`，例如 `duration=10s`。

觀看[關於 Torch 的影片](https://youtu.be/45E2uwI3xhc)。

## 檢視透過某個介面的流量 {#see-what-passes-an-interface}

為 Torch 指定要監視的介面。介面名可以不寫 `interface=`：

```ros
/tool/torch bridge
```

```text
Columns: MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, SRC-PORT, DST-ADDRESS, DST-PORT, TX, RX, TX-PACKETS, RX-PACKETS
MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS    SRC-PORT  DST-ADDRESS   DST-PORT        TX         RX         TX-PACKETS  RX-PACKETS
ip            icmp            0  192.168.88.21            192.168.88.1                  197.3kbps  197.3kbps          48          48
ip            tcp             0  192.168.88.20     58910  192.168.88.1  2000 (btserv)   1152bps    1152bps             2           2
ip            udp             0  192.168.88.20      2257  192.168.88.1  2001 (glimpse)  2.0Mbps    0bps              172           0
```

表格每秒更新一次，直到你停止 Torch。在本例中，192.168.88.21 向路由器傳送 ping，192.168.88.20 執行頻寬測試，從路由器接收 2 Mbps。

每一行是兩個地址之間的一條流：

- `SRC-ADDRESS` 和 `SRC-PORT` - 介面遠端的地址和埠：即介面從其一側接收流量的那一端。即使會話由路由器發起，或者流量由路由器轉發，這一點同樣成立。
- `DST-ADDRESS` 和 `DST-PORT` - 流的另一端。埠號會連同其服務名稱一起顯示，例如 `2000 (btserv)`。
- `RX` - 介面從 `SRC-ADDRESS` 接收流量的速率，單位為位元每秒。
- `TX` - 介面向 `SRC-ADDRESS` 傳送流量的速率，單位為位元每秒。
- `TX-PACKETS` 和 `RX-PACKETS` - 同樣這兩個方向上的包速率。

只有當某條流在某一列有值時，該列才會出現：僅當存在 TCP 或 UDP 流時，埠列才會出現。

## 找出佔用頻寬的主機 {#find-the-host-that-uses-the-bandwidth}

在 LAN 介面上，`SRC-ADDRESS` 是 LAN 主機，因此 `TX` 是該主機下載的流量，`RX` 是其上傳的流量。速率最高的行顯示誰在使用連線。連線很多的主機（例如網頁瀏覽器）會有很多行；按其地址過濾即可一起檢視。請監視 LAN 介面，而不是 WAN 介面：經過源 NAT 後，WAN 介面上的流攜帶的是路由器的公網地址，而不是各主機的地址。

要監視某一臺主機，請按其地址過濾：

```ros
/tool/torch bridge src-address=192.168.88.21/32
```

```text
Columns: MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, DST-ADDRESS, TX, RX, TX-PACKETS, RX-PACKETS
MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS    DST-ADDRESS   TX         RX         TX-PACKETS  RX-PACKETS
ip            icmp            0  192.168.88.21  192.168.88.1  197.3kbps  197.3kbps          48          48
```

地址過濾器按 Torch 顯示的各列進行匹配：`src-address` 匹配 `SRC-ADDRESS`，即介面遠端，`dst-address` 匹配 `DST-ADDRESS`。在 LAN 介面上，請用 `src-address` 過濾主機；把 `dst-address` 設為 LAN 主機在該介面上通常匹配不到任何內容。對於 IPv6，請使用 `src-address6` 和 `dst-address6`。

## 監視某一種協定或埠 {#watch-one-protocol-or-port}

要只顯示某一種 IP 協定或某一個埠，請使用 `ip-protocol` 和 `port`：

```ros
/tool/torch bridge ip-protocol=tcp port=443
```

`port` 匹配 `SRC-PORT` 或 `DST-PORT`。它只接受一個埠或 `any`；像 `port=80,443` 這樣的列表會失敗並報 `expected end of command`。埠過濾只適用於帶埠的流：不帶埠的流（例如 ICMP）在設定埠過濾後仍會出現。

## 檢查 VLAN 標籤和 DSCP 標記 {#check-vlan-tags-and-dscp-marking}

在承載帶標籤 VLAN 的介面上，Torch 會為帶標籤的流量增加一個 `VLAN-ID` 列。要檢查流量是否以正確的 DSCP 值到達正確的 VLAN，例如 VLAN 99 中 DSCP 46（Expedited Forwarding）的語音流量，請監視父介面。在本例中，一個標記為 DSCP 46 的測試 ping 在 VLAN 99 中執行：

```ros
/tool/torch ether1
```

```text
Columns: VLAN-ID, MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, DST-ADDRESS, TX, RX, TX-PACKETS, RX-PACKETS
VLAN-ID  MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS   DST-ADDRESS   TX         RX         TX-PACKETS  RX-PACKETS
     99  ip            icmp           46  198.51.100.1  198.51.100.2  237.3kbps  235.7kbps          48          48
         ip            icmp            0  203.0.113.1   203.0.113.2   120.5kbps  120.5kbps          48          48
```

第一行帶有 VLAN 99 標籤並標記為 DSCP 46；第二行不帶標籤。`vlan-id=99` 或 `dscp=46` 只顯示匹配的流。在 VLAN 介面本身上，幀已經不帶標籤，因此在那裡不會出現 `VLAN-ID` 列。對於不帶標籤的裝置（例如接在網橋埠上的電話），請監視網橋並按該電話的地址過濾，例如 `src-address=192.168.88.30/32`。

DSCP 值是流的一部分，因此當一次會話的兩個方向標記不同時，它們會顯示為兩行：一行只有 `RX`，一行只有 `TX`。此處請求以 DSCP 46 到達，應答以 DSCP 0 發出：

```ros
/tool/torch ether1
```

```text
Columns: MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, DST-ADDRESS, TX, RX, TX-PACKETS, RX-PACKETS
MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS  DST-ADDRESS  TX         RX         TX-PACKETS  RX-PACKETS
ip            icmp            0  203.0.113.1  203.0.113.2  165.6kbps  0bps               50           0
ip            icmp           46  203.0.113.1  203.0.113.2  0bps       165.6kbps           0          50
```

Torch 不顯示幀的 VLAN 優先順序（PCP）；請使用[封包嗅探器](./packet-sniffer.md)檢查。

## 檢視被防火牆丟棄的流量 {#see-traffic-that-the-firewall-drops}

Torch 在防火牆之前統計報文，因此它會顯示被防火牆規則丟棄的流量。在本例中，input 鏈中的一條規則丟棄來自 192.168.88.21 的 ping：

```ros
/tool/torch bridge src-address=192.168.88.21/32
```

```text
Columns: MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, DST-ADDRESS, TX, RX, TX-PACKETS, RX-PACKETS
MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS    DST-ADDRESS   TX    RX         TX-PACKETS  RX-PACKETS
ip            icmp            0  192.168.88.21  192.168.88.1  0bps  197.3kbps           0          48
```

請求到達（`RX`），而路由器沒有回送任何內容（`TX` 為 0）。流量只在一個方向上出現，這種情形也可能表示某個連線的應答走了另一條路徑或根本沒有到來，因此請檢查該規則自身的計數器以確認它丟棄了流量：`/ip/firewall/filter/print stats`（見[過濾器](../firewall-and-quality-of-service/firewall/filter.md)）。

## 檢視由哪個 CPU 處理流量 {#see-which-cpu-handles-the-traffic}

在多 CPU 的路由器上，`cpu=any` 會增加一個 `CPU` 列，每個處理過某條流中報文的 CPU 各佔一行。用它來檢視一條大流量是否讓單個 CPU 一直繁忙：

```ros
/tool/torch bridge cpu=any
```

```text
Columns: CPU, MAC-PROTOCOL, IP-PROTOCOL, DSCP, SRC-ADDRESS, DST-ADDRESS, TX, RX, TX-PACKETS, RX-PACKETS
CPU  MAC-PROTOCOL  IP-PROTOCOL  DSCP  SRC-ADDRESS    DST-ADDRESS   TX         RX         TX-PACKETS  RX-PACKETS
  0  ip            icmp            0  192.168.88.20  192.168.88.1  170.3kbps  389.3kbps          21          48
  0  ip            icmp            0  192.168.88.21  192.168.88.1  201.4kbps  201.4kbps          49          49
  1  ip            icmp            0  192.168.88.20  192.168.88.1  32.4kbps   0bps                4           0
  3  ip            icmp            0  192.168.88.20  192.168.88.1  186.5kbps  0bps               23           0
```

此處路由器發往 192.168.88.20 的 ping 從 CPU 0、1 和 3 發出，而應答在 CPU 0 上接收。

## 技術細節 {#technical-details}

### 快速路徑 {#fast-path}

Torch 執行期間，路由器會為所有流量關閉 IP fast path 和 FastTrack，而不僅是在被監視的介面上。Torch 停止後兩者都會恢復。

### Torch 看不到的流量 {#traffic-that-torch-does-not-see}

Torch 能看到在被監視介面上到達路由器 CPU 的報文：

- 在啟用硬體解除安裝的網橋上，交換晶片在埠之間轉發流量而不經過 CPU，因此 Torch 看不到它。未知單播、廣播和部分組播流量仍會到達 CPU，因而仍然可見。參見[啟用硬體解除安裝和 MAC 學習時的報文流](../bridging-and-switching/user-guides/layer2-misconfiguration.md#packet-flow-with-hardware-offloading-and-mac-learning)。
- 使用 [L3 硬體解除安裝](../bridging-and-switching/l3-hardware-offloading.md)時，由交換晶片轉發的路由流量同樣不會到達 CPU。
- 啟用用戶端到用戶端轉發時，無線用戶端之間的單播流量對 Torch 不可見。

Torch 顯示協定和 IP 地址，而不顯示 MAC 地址。要查詢主機的 MAC 地址，請檢視它在 [DHCP 伺服器](../network-management/dhcp/server.md#leases)中的租約。

有關所有引數，請參見 CLI 參考中的 [`/tool/torch`](../cli-reference/tool/torch.md)。
