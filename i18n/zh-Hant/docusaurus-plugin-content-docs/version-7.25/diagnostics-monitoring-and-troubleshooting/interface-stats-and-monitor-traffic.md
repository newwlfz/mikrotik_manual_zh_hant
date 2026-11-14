---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/interface-stats-and-monitor-traffic"
sidebar_position: 8
title: "介面統計與 monitor-traffic"
sidebar_label: "介面統計與 monitor-traffic"
description: "本頁介紹 MikroTik RouterOS 介面統計資訊以及 monitor-traffic 工具，用於即時監控物理和虛擬介面上的網路利用率、硬體效能、封包速率和位元率。其中包含用於檢視介面計數器、Fast Path 指標、鏈路穩定性以及排查頻寬瓶頸的命令。"
tags:
  - 'stats'
  - 'monitor-traffic'
  - 'interface'
source: https://manual.mikrotik.com/docs/7.25/diagnostics-monitoring-and-troubleshooting/interface-stats-and-monitor-traffic
captured_at: '2026-11-04T11:15:19+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

每個 RouterOS 介面都包含各種計數器，例如接收和傳送的封包數量、[Fast Path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path) 位元組數以及鏈路斷開次數。這些統計資訊可即時反映物理和虛擬介面上的網路利用率和硬體效能。要分析即時吞吐量和封包速率，monitor-traffic 工具可提供持續的資料流，用於故障排查和頻寬驗證。

## 統計 {#stats}

介面統計資訊可即時監控所有物理和虛擬介面上的資料流和硬體效能。使用 `stats` 或 `stats-detail` 命令可列印介面計數器，這些計數器跟蹤封包吞吐量、位元組數以及鏈路穩定性指標（如 uptime 和 flap 次數）。以 "fp" 開頭的值表示 [Fast Path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path) 計數器，而 "tx-queue-drop" 透過顯示 [介面佇列](../firewall-and-quality-of-service/queues/index.md#interface-queue) 丟棄的封包數量來提示潛在擁塞。

監控這些計數器有助於透過跟蹤 `link-downs` 計數和意外的流量下降來識別物理層問題。它還可透過將 `rx-byte` 和 `tx-byte` 值與特定鏈路的預期吞吐量進行比較，幫助排查頻寬瓶頸。

```ros
[admin@MikroTik] > /interface/print stats 
Flags: R - RUNNING
Columns: NAME, RX-BYTE, TX-BYTE, RX-PACKET, TX-PACKET, TX-QUEUE-DROP
#   NAME        RX-BYTE      TX-BYTE  RX-PACKET  TX-PACKET  TX-QUEUE-DROP
0 R ether1  205 149 015  147 887 338    158 132    150 015              2
1 R ether2   32 400 148  335 690 764         19    216 509              0
2 R ether3  944 043 040   32 392 350    617 271         17              0
3 R ether4    7 038 417   32 398 973          9          4              0
4 R ether5    7 036 903   32 502 437          5          9              0
5   sfp1              0            0          0          0              0
[admin@MikroTik] > /interface/print stats-detail  
Flags: D - dynamic; X - disabled, R - running; S - slave; P - passthrough 
 0  R   name="ether1" last-link-down-time=2022-07-19 12:37:06 last-link-up-time=2022-07-19 12:37:09 link-downs=2 
        rx-byte=205 164 277 tx-byte=147 977 500 rx-packet=158 254 tx-packet=150 156 tx-queue-drop=2 
        fp-rx-byte=199 271 067 fp-tx-byte=0 fp-rx-packet=1 473 603 fp-tx-packet=0 

 1  R   name="ether2" last-link-down-time=2022-07-19 12:46:06 last-link-up-time=2022-07-19 12:46:07 link-downs=10 
        rx-byte=32 400 148 tx-byte=335 690 764 rx-packet=19 tx-packet=216 509 tx-queue-drop=0 
        fp-rx-byte=33 718 434 fp-tx-byte=67 fp-rx-packet=60 037 fp-tx-packet=1 

 2  R   name="ether3" last-link-down-time=2022-07-19 12:46:06 last-link-up-time=2022-07-19 12:46:08 link-downs=11 
        rx-byte=944 043 040 tx-byte=32 392 350 rx-packet=617 271 tx-packet=17 tx-queue-drop=0 fp-rx-byte=6 860 921 
        fp-tx-byte=0 fp-rx-packet=46 671 fp-tx-packet=0 

 3  R   name="ether4" last-link-down-time=2022-07-19 12:46:06 last-link-up-time=2022-07-19 12:46:07 link-downs=10 
        rx-byte=7 038 417 tx-byte=32 398 973 rx-packet=9 tx-packet=4 tx-queue-drop=0 fp-rx-byte=6 852 283 
        fp-tx-byte=0 fp-rx-packet=46 586 fp-tx-packet=0 

 4  R   name="ether5" last-link-down-time=2022-07-19 12:46:06 last-link-up-time=2022-07-19 12:46:08 link-downs=10 
        rx-byte=7 036 903 tx-byte=32 502 437 rx-packet=5 tx-packet=9 tx-queue-drop=0 fp-rx-byte=6 850 637 
        fp-tx-byte=178 fp-rx-packet=46 568 fp-tx-packet=2 

 5      name="sfp1" link-downs=0 rx-byte=0 tx-byte=0 rx-packet=0 tx-packet=0 tx-queue-drop=0 fp-rx-byte=0 
        fp-tx-byte=0 fp-rx-packet=0 fp-tx-packet=0 
```

## 監控流量 {#monitor-traffic}

可透過 `monitor-traffic` 命令監控經過任意介面的流量。

此工具提供即時吞吐量統計資訊，包括接收和傳送資料的封包速率及位元率。它對於直接從命令列介面驗證介面活動並識別高頻寬佔用者至關重要。

例如，使用此命令觀察特定 WAN 介面上的每秒位元數，以排查疑似網路瓶頸。它還可用於確認流量是否正確透過新配置的 VLAN 或橋接成員。

```ros
[admin@MikroTik] > /interface/monitor-traffic [find]
                         name:     ether1 ether2 ether3 ether4 ether5 sfp1
        rx-packets-per-second:         19      0      0      0      0    0
           rx-bits-per-second:   27.8kbps   0bps   0bps   0bps   0bps 0bps
     fp-rx-packets-per-second:         29      0      0      0      0    0
        fp-rx-bits-per-second:   26.8kbps   0bps   0bps   0bps   0bps 0bps
        tx-packets-per-second:         21      0      0      0      0    0
           tx-bits-per-second:  149.4kbps   0bps   0bps   0bps   0bps 0bps
     fp-tx-packets-per-second:          0      0      0      0      0    0
        fp-tx-bits-per-second:       0bps   0bps   0bps   0bps   0bps 0bps
    tx-queue-drops-per-second:          0      0      0      0      0    0

```

:::info
更多[乙太網統計資訊](../wired-connections/ethernet.md#stats)可在 `/interface/ethernet` 選單中檢視。
:::
