---
sidebar_key: "firewall-and-quality-of-service/user-guides/connection-rate"
sidebar_position: 3
title: "連線速率"
sidebar_label: "連線速率"
description: "Connection Rate 是 MikroTik RouterOS 的一項防火牆功能，它根據連線速度來監控和過濾流量，使用 ''connection-bytes'' 和 ''connection-rate'' 檢測高速連線，以便為其設定優先順序或進行限速。"
tags:
  - 'firewall'
  - 'traffic-management'
source: https://manual.mikrotik.com/docs/7.25/firewall-and-quality-of-service/user-guides/connection-rate
captured_at: '2026-11-04T11:15:59+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

Connection Rate 是一種防火牆匹配器，允許根據連線的當前速度捕獲流量。

## 理論 {#theory}

連線跟蹤表中的每個條目表示雙向通訊。每當封包與特定條目關聯時，封包大小值（包括 IP 頭）會加到該條目的 "connection-bytes" 值中。（換句話說，"connection-bytes" 同時包括上傳和下載）。

Connection Rate 根據 "connection-bytes" 的變化計算連線速度。連線速率每秒重新計算，並且沒有任何平均值。

"connection-bytes" 和 "connection-rate" 兩個選項僅適用於 TCP 和 UDP 流量。（你需要指定協定來啟用這些選項）。在 "connection-rate" 選項中，你可以指定想要捕獲的速度範圍：

```ros
ConnectionRate ::= [!]From-To
  From,To ::= 0..4294967295    (integer number)
```

### 規則示例 {#rule-example}

當連線速度低於 100kbps 時，這些規則將捕獲經過路由器的 TCP/UDP 流量：

```ros
/ip/firewall/filter
add action=accept chain=forward connection-rate=0-100k protocol=tcp
add action=accept chain=forward connection-rate=0-100k protocol=udp
```

## 應用示例 - 流量優先順序劃分 {#application-example---traffic-prioritization}

Connection-rate 可以有多種用法（這些用法仍有待實現），但最常見的設定是檢測 "重負載連線" 併為其設定較低的優先順序（即長時間保持高速率的連線（例如 P2P、HTTP、FTP 下載））。這樣做，你可以優先處理其他所有流量，這些流量通常包括 VoIP、HTTP 瀏覽和線上遊戲。

本示例中描述的方法可以與其他檢測流量並劃分優先順序的方法一起使用。由於 connection-rate 選項沒有任何平均值，我們需要確定用於識別 "重負載連線" 的閾值。如果我們假設正常的 HTTP 瀏覽連線長度小於 500kB（4Mb），並且 VoIP 要求的速度不超過 200kbps，那麼每個在前 500kB 之後仍保持高於 200kbps 速度的連線都可以被視為 "重負載連線"。

（在你的網路中，HTTP 瀏覽可能有不同的 "connection-bytes"，VoIP 可能有不同的 "connection-rate" - 因此，在應用此示例之前，請自行研究）

對於此示例，我們假設到 ISP 的上傳和下載連線均為 6Mbps。

### 給急於上手者的快速開始 {#quick-start-for-impatient}

```ros
/ip/firewall/mangle
add chain=forward action=mark-connection connection-mark=!heavy_traffic_conn new-connection-mark=all_conn
add chain=forward action=mark-connection connection-bytes=500000-0 connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=tcp
add chain=forward action=mark-connection connection-bytes=500000-0 connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=udp
add chain=forward action=mark-packet connection-mark=heavy_traffic_conn new-packet-mark=heavy_traffic passthrough=no
add chain=forward action=mark-packet connection-mark=all_conn new-packet-mark=other_traffic passthrough=no

/queue/tree
add name=upload parent=public max-limit=6M
add name=other_upload parent=upload limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_upload parent=upload limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
add name=download parent=local max-limit=6M
add name=other_download parent=download limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_download parent=download limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
```

#### 說明 {#explanation}

在 mangle 中，我們需要將所有連線分成兩組，然後標記來自這兩組的封包。由於我們討論的是用戶端流量，最合理的標記位置是 mangle 的 forward 鏈。

請記住，一旦 "重負載" 連線具有較低優先順序並且佇列達到 max-limit - 該重負載連線的速度就會下降，connection-rate 也會降低。這將導致其變為更高的優先順序，並且該連線能夠在短時間內獲得更多流量；當 connection-rate 再次升高時，這又會再次導致其變為較低的優先順序。為避免這種情況，我們必須確保一旦檢測到 "重負載連線"，就會始終將其標記為 "重負載連線"。

#### IP 防火牆 mangle {#ip-firewall-mangle}

此規則將確保 "重負載" 連線保持為重負載，並用預設連線標記標記其餘連線：

```ros
/ip/firewall/mangle
add chain=forward action=mark-connection connection-mark=!heavy_traffic_conn new-connection-mark=all_conn
```

這兩條規則將根據我們的標準標記所有重負載連線：即每個在前 500kB 之後仍保持高於 200kbps 速度的連線都可以被視為 "重負載"：

```ros
add chain=forward action=mark-connection connection-bytes=500000-0 \
    connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=tcp
add chain=forward action=mark-connection connection-bytes=500000-0 \
    connection-mark=all_conn connection-rate=200k-100M new-connection-mark=heavy_traffic_conn protocol=udp
```

mangle 中的最後兩條規則將簡單地標記來自相應連線的所有流量：

```ros
add chain=forward action=mark-packet connection-mark=heavy_traffic_conn new-packet-mark=heavy_traffic passthrough=no
add chain=forward action=mark-packet connection-mark=all_conn new-packet-mark=other_traffic passthrough=no
```

#### 佇列 {#queue}

這是一個放置在 Interface HTB 上的簡單佇列樹 - "public" 是你的 ISP 所連線的介面，"local" 是你的用戶端所在的介面。如果你有不止一個 "public" 或不止一個 "local"，你需要分別對上傳和下載進行 mangle，並將佇列樹放在 global-out 中：

```ros
/queue/tree
add name=upload parent=public max-limit=6M
add name=other_upload parent=upload limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_upload parent=upload limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
add name=download parent=local max-limit=6M
add name=other_download parent=download limit-at=4M max-limit=6M packet-mark=other_traffic priority=1
add name=heavy_download parent=download limit-at=2M max-limit=6M packet-mark=heavy_traffic priority=8
```
