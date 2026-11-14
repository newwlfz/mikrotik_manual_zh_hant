---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/bandwidth-test"
sidebar_position: 5
title: "頻寬測試"
sidebar_label: "頻寬測試"
description: "MikroTik RouterOS 中的頻寬測試功能允許使用 TCP 或 UDP 協定測量路由器之間的網路吞吐量，並詳細說明其行為和限制。它包括頻寬伺服器的配置選項，例如埠範圍、身份驗證和會話限制，還提供了在無需用戶端身份驗證的情況下啟用伺服器的示例。"
tags:
  - 'bandwidth'
  - 'tcp'
  - 'udp'
source: https://manual.mikrotik.com/docs/7.24/diagnostics-monitoring-and-troubleshooting/bandwidth-test
captured_at: '2026-11-04T11:27:51+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

**子選單：** `/tool` **所需軟體包：** `system`

頻寬測試器可用於測量到另一臺 MikroTik 路由器（有線或無線）的吞吐量，從而幫助發現網路“瓶頸”。

TCP 測試使用帶確認的標準 TCP 協定，並遵循 TCP 演算法根據延遲、丟棄的封包以及 TCP 演算法中的其他特性來決定傳送多少封包。請查閱 TCP 協定，瞭解其內部速度設定以及如何分析其行為。吞吐量統計使用整個 TCP 資料流的大小計算。由於確認是 TCP 的內部工作機制，其大小和對鏈路的使用不計入吞吐量統計。因此，在估算吞吐量時，該統計不如 UDP 統計可靠。

UDP 測試器傳送的封包比鏈路另一端當前報告接收到的封包多 110% 或更多。要檢視鏈路的最大吞吐量，封包大小應設定為鏈路允許的最大 MTU，通常為 1500 位元組。UDP 不需要確認；這種實現意味著可以看到最接近的吞吐量近似值。

:::warning
頻寬測試會使用所有可用頻寬和系統資源，並可能影響網路可用性。如果要測試路由器的真實吞吐量，應透過被測試的路由器執行頻寬測試，而不是從該路由器發起或發往該路由器。為此，至少需要 3 臺串聯的路由器：頻寬服務端、被測試的路由器和頻寬用戶端。
:::

:::note
如果使用 UDP 協定，頻寬測試會計入 IP 頭+UDP 頭+UDP 資料。如果使用 TCP，頻寬測試只計入 TCP 資料（不包括 TCP 頭和 IP 頭）。
:::

## 頻寬測試服務端 {#bandwidth-test-server}

|  |  |
| :-- | :-- |
**子選單：** `/tool/bandwidth-server`

| 屬性 | 描述 |
| :-- | :-- |
| **allocate-udp-ports-from** (*integer 1000..64000*；預設：**2000**) | UDP 埠範圍的起始值 |
| **authenticate** (*yes \| no*；預設：**yes**) | 僅與已認證的用戶端通訊 |
| **enabled** (*yes \| no*；預設：**yes**) | 定義頻寬服務端是否啟用 |
| **max-sessions** (*integer 1..1000*；預設：**100**) | 最大同時測試數量 |

### 示例 {#example}

頻寬服務端：

```ros
[admin@MikroTik] /tool/bandwidth-server> print                                  
                  enabled: yes                                                  
             authenticate: yes                                                  
  allocate-udp-ports-from: 2000                                                 
             max-sessions: 100                                                  
[admin@MikroTik] /tool/bandwidth-server>
```

活動會話：

```ros
[admin@MikroTik] /tool/bandwidth-server/session> print
  # CLIENT          PROTOCOL DIRECTION USER
  0 35.35.35.1      udp      send      admin
  1 25.25.25.1      udp      send      admin
  2 36.36.36.1      udp      send      admin
[admin@MikroTik] /tool/bandwidth-server/session>
```

要啟用 **bandwidth-test** 服務端而不進行用戶端認證：

```ros
[admin@MikroTik] /tool/bandwidth-server> set enabled=yes authenticate=no        
[admin@MikroTik] /tool/bandwidth-server> print                                  
                  enabled: yes                                                  
             authenticate: no                                                   
  allocate-udp-ports-from: 2000                                                 
             max-sessions: 100                                                  
[admin@MikroTik] /tool/bandwidth-server>
```

## 頻寬測試用戶端 {#bandwidth-test-client}

**子選單：** `/tool/bandwidth-test`

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*IP address \| IPv6 prefix[%interface]*；預設：) | 主機的 IP 地址 |
| **direction** (*both \| receive \| transmit*；預設：**receive**)  | 資料流方向 |
| **duration** (*time*；預設：) | 測試持續時間 |
| **interval** (*time: 20ms..5s*；預設：**1s**) | 報告之間的延遲（秒） |
| **local-tx-speed** (*integer 0..18446744073709551615*；預設： ) | 傳輸測試最大速度（位元每秒） |
| **local-udp-tx-size** (*integer: 28..64000*) | 本地傳送封包大小（位元組） |
| **password** (*string*；預設：**""**) | 遠端使用者的密碼 |
| **protocol** (*udp \| tcp*；預設：**udp**) | 要使用的協定 |
| **random-data** (*yes \| no*；預設：**no**) | 如果 random-data 設定為 yes，頻寬測試封包的負載將包含不可壓縮的隨機資料流，因此使用資料壓縮的鏈路不會扭曲結果（這會大量消耗 CPU，對於低速 CPU 應將 random-data 設定為 no） |
| **remote-tx-speed** (*integer 0..18446744073709551615*；預設： ) | 接收測試最大速度（位元每秒） |
| **remote-udp-tx-size** (*integer: 28..64000*) | 遠端傳送封包大小（位元組） |
| **connection-count** (*integer 1..255*；預設：) | 要使用的 TCP 連線數 |
| **user** (*string*；預設：**""**) | 遠端使用者 |

### 示例 {#example-1}

要對 **10.0.0.32** 主機執行持續 15 秒的頻寬測試，傳送和接收 **1000** 位元組的 UDP 封包，並使用使用者名稱 **admin** 連線：

```ros
[admin@MikroTik] /tool> bandwidth-test 10.0.0.32 duration=15s \
\... direction=both local-udp-tx-size=1000 protocol=udp \
\... remote-udp-tx-size=1000 user=admin
                status: done testing
              duration: 15s
            tx-current: 272.8Mbps
  tx-10-second-average: 200.3Mbps
      tx-total-average: 139.5Mbps
            rx-current: 169.6Mbps
  rx-10-second-average: 164.8Mbps
      rx-total-average: 117.0Mbps
          lost-packets: 373
           random-data: no
             direction: both
               tx-size: 1000
               rx-size: 1000
[admin@MikroTik] /tool>
```

### 鏈路本地 IPv6 示例 {#link-local-ipv6-example}

```ros
[admin@MikroTik] > /tool/bandwidth-test fe80::34:23ff:fe6a:570c%local
                status: running
              duration: 5s
            rx-current: 23.9Mbps
  rx-10-second-average: 15.1Mbps
      rx-total-average: 15.1Mbps
          lost-packets: 0
           random-data: no
             direction: receive
               rx-size: 1500
```
