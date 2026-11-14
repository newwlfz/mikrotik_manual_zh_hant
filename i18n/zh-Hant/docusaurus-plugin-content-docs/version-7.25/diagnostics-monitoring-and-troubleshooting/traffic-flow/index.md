---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/traffic-flow/index"
sidebar_position: 2
title: "流量監控"
sidebar_label: "流量監控"
description: "MikroTik Traffic-Flow 透過收集經過路由器的封包統計資訊來提供網路監控和計費，支援 NetFlow 版本 1、5、9 和 IPFIX，以實現靈活的流量分析。它允許配置介面、快取條目、超時、封包取樣以及用於流量資料傳輸的目標主機。"
tags:
  - 'traffic-flow'
  - 'netflow'
  - 'ipfix'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/traffic-flow
captured_at: '2026-11-04T11:15:30+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

MikroTik Traffic-Flow 是一個提供經過路由器的封包統計資訊的系統。除了網路監控和計費之外，系統管理員還可以藉助它找出網路中可能出現的各種問題。藉助 Traffic-Flow，可以分析和最佳化整體網路效能。由於 Traffic-Flow 與 Cisco NetFlow 相容，因此可以配合各種為 Cisco NetFlow 設計的工具使用。

Traffic Flow 只能處理由路由器 CPU 處理的流量，因此硬體解除安裝（HW offloaded）的流量不會出現在 Traffic Flow 流中（例如硬體解除安裝的橋接流量）。

Traffic-Flow 支援以下 NetFlow 格式：

- **version 1** - 這是 NetFlow 使用的原始格式。它提供有關流經路由器的 IP 封包的基本資訊，但不支援高階特性，例如不同型別的協定和 Type of Service (ToS)。
- **version 5** - 這是對 Version 1 的增強，支援 Type of Service (ToS)、TCP 標誌和自治系統號等附加特性。除 version 1 的功能外，version 5 還可以包含 BGP AS 和流序列號資訊。目前 RouterOS 不包含 BGP AS 號。
- **version 9** - 此版本引入了基於模板的匯出格式，具備可擴充套件性，並支援此前版本無法處理的新記錄型別。它可以基於定義的模板匯出資料，並且能夠匯出 IPv4 和 IPv6 的流資訊。
- **IPFIX** - 由 IETF 標準化，該協定基於 NetFlow Version 9。它進一步擴充套件了能力，允許更可定製、更靈活的流記錄。IPFIX 支援 NetFlow 未涉及的新技術，例如組播。

## 常規 {#general}

**子選單：** `/ip/traffic-flow`

本節列出 Traffic-Flow 的配置屬性。

| 屬性 | 描述 |
| :-- | :-- |
| **interfaces** (*string \| all*；預設值：**all**) | 這些介面的名稱將用於為 traffic-flow 收集統計資料。要指定多個介面，請用逗號分隔。 |
| **cache-entries** (*128k \| 16k \| 1k \| 256k \| 2k \| ...* ；預設值：**4k**) | 可同時位於路由器記憶體中的流數量。 |
| **active-flow-timeout** (*time*；預設值：**30m**) | 流的最大存活時間。 |
| **inactive-flow-timeout** (*time*；預設值：**15s**) | 流空閒時保持活動狀態的時長。如果某個連線在此超時時間內沒有收到任何封包，則 traffic-flow 會將其封包作為新流傳送出去。如果此超時值過小，可能會產生大量流並導致緩衝區溢位。 |
| **packet-sampling** (*no \| yes*；預設值：**no**) | 啟用或停用封包取樣功能。 |
| **sampling-interval** (*integer*；預設值：**0**) | 連續取樣的封包數量。 |
| **sampling-space** (*integer*；預設值：**0**) | 連續跳過的封包數量。 |

:::warning
資訊

封包取樣在 RouterOS **v7.** 中可用。
:::

在以下示例中：

```ros
/ip/traffic-flow/set packet-sampling=yes sampling-interval=2222 sampling-space=1111
```

將連續取樣 2222 個數據包，然後跳過 1111 個數據包。之後按此方式迴圈重複取樣。

## 目標 {#targets}

**子選單：** `/ip/traffic-flow/target`

透過 Traffic-Flow 目標，我們指定將從路由器收集 Traffic-Flow 資訊的主機。

| 屬性 | 描述 |
| :-- | :-- |
| **src-address** *(IP ；預設值：)* | 傳送 Traffic-Flow 統計資訊時用作源地址的 IP 地址 |
| **dst-address** (*IP*；預設值：) | 接收路由器傳送的 Traffic-Flow 統計封包的主機的 IP 地址。 |
| **port** *(Port；預設值：2055)* | 接收路由器傳送的 Traffic-Flow 統計封包的主機埠（UDP）。 |
| **v9-template-refresh** (*integer*；預設值：**20**) | 傳送多少個數據包後向接收主機發送模板（僅適用於 NetFlow version 9 和 IPFIX） |
| **v9-template-timeout** (*time*；預設值：) | 若模板尚未傳送，則在多長時間後傳送該模板。（僅適用於 NetFlow version 9 和 IPFIX） |
| **version** (*1 \| 5 \| 9 \| IPFIX*；預設值：) | 要使用的 NetFlow 版本格式 |

## IPFIX {#ipfix}

**子選單：** `/ip/traffic-flow/ipfix`

允許自定義流記錄

| 屬性 | 描述 |
| :-- | :-- |
| **bytes** | 流中已處理的位元組總數。 |
| **ip-total-length** | IP 封包的長度（位元組）。 |
| **src-address** | 流的源 IP 地址。 |
| **dst-address** | 流的目標 IP 地址。 |
| **ipv6-flow-label** | IPv6 頭部中的標籤欄位，用於對流進行分類。 |
| **src-address-mask** | 源地址的網路掩碼，在彙總資料時很有用。 |
| **dst-address-mask** | 目標地址的網路掩碼。 |
| **is-multicast** | 指示該流是否為組播流。 |
| **src-mac-address** | 源 MAC 地址。 |
| **dst-mac-address** | 目標 MAC 地址。 |
| **last-forwarded** | 流中最後一個被轉發封包的時間戳。 |
| **src-port** | 源埠號。 |
| **dst-port** | 目標埠號。 |
| **nat-dst-address** | 經 NAT 轉換後的目標 IP 地址。 |
| **sys-init-time** | 系統初始化時間，可用於時序分析。 |
| **first-forwarded** | 流中第一個被轉發封包的時間戳。 |
| **nat-dst-port** | 經 NAT 轉換後的目標埠號。 |
| **tcp-ack-num** | TCP 連線中的確認號。 |
| **gateway** | 流所經由的路由閘道器的 IP 地址。 |
| **nat-events** | 與該流的網路地址轉換相關的事件。 |
| **tcp-flags** | TCP 頭部中的標誌（例如 SYN、ACK）。 |
| **icmp-code** | 用於錯誤訊息和操作資訊的 ICMP 程式碼。 |
| **nat-src-address** | 經 NAT 轉換後的源 IP 地址。 |
| **icmp-type** | ICMP 訊息的型別，對診斷訊息很重要。 |
| **nat-src-port** | 經 NAT 轉換後的源埠號。 |
| **tcp-seq-num** | TCP 連線中的序列號。 |
| **tcp-window-size** | TCP 連線中的視窗大小，表示接收資料緩衝的規模。 |
| **igmp-type** | Internet Group Management Protocol 操作的型別。 |
| **out-interface** | 流的出向封包所經過的介面。 |
| **in-interface** | 流的入向封包所經過的介面。 |
| **packets** | 流中已處理的封包數量。 |
| **ip-header-length** | IP 頭部的長度。 |
| **protocol** | 協定號（例如 TCP、UDP、ICMP）。 |
| **tos** | IP 頭部中的 Type of Service 欄位，表示封包的優先順序和處理方式。 |
| **ttl** | 封包的 Time To Live，每個路由器都會遞減，以防止無限迴圈。 |
| **udp-length** | UDP 負載的長度。 |

## 說明 {#notes}

透過檢視[封包流向圖](../../firewall-and-quality-of-service/packet-flow-in-routeros.md)，可以看到 traffic flow 位於 input、forward 和 output 鏈棧的末端。這意味著 traffic flow 只會統計到達這些鏈之一的流量。

例如，你在交換器上設定了映象埠，將映象埠連線到路由器，並設定 traffic flow 來統計映象封包。遺憾的是，這樣的設定不會生效，因為映象封包在到達 input 鏈之前就被丟棄了。

如果流量經過其他介面以及監控介面，報告中也會出現這些介面。

## 示例 {#examples}

本示例演示如何在路由器上配置 Traffic-Flow

在路由器上啟用 Traffic-Flow：

```ros
[admin@MikroTik] /ip/traffic-flow> set enabled=yes
[admin@MikroTik] /ip/traffic-flow> print
                enabled: yes
             interfaces: all
          cache-entries: 4k
    active-flow-timeout: 30m
  inactive-flow-timeout: 15s
[admin@MikroTik] /ip/traffic-flow>
```

指定將接收 Traffic-Flow 封包的主機的 IP 地址和埠：

```ros
[admin@MikroTik] /ip/traffic-flow/target> add dst-address=192.168.0.2 port=2055 version=9
[admin@MikroTik] /ip/traffic-flow/target> print
Flags: X - disabled 
 #   SRC-ADDRESS       DST-ADDRESS        PORT     VERSION
 0   0.0.0.0           192.168.0.2        2055     9  
[admin@MikroTik] /ip/traffic-flow/target>
```

現在路由器開始傳送帶有 Traffic-Flow 資訊的封包。

:::info
要在 MikroTik 上使用 ntop-ng，你需要使用 Nprobe，這是一款付費軟體。
:::

### 另請參閱 {#see-more}

- [NetFlow 基礎](https://etutorials.org/Networking/network+management/Part+II+Implementations+on+the+Cisco+Devices/Chapter+7.+NetFlow/Fundamentals+of+NetFlow/)
- [在 MikroTik 上使用 Ntop 進行流量流分析](https://github.com/ntop/ntopng/issues/1575)

## 相關主題 {#related-topics}

<DocCardList />
