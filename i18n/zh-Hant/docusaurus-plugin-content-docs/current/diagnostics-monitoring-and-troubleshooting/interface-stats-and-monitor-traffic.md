---
sidebar_key: "diagnostics-monitoring-and-troubleshooting/interface-stats-and-monitor-traffic"
sidebar_position: 8
title: "介面統計與 monitor-traffic"
sidebar_label: "介面統計與 monitor-traffic"
description: "MikroTik RouterOS 上的介面統計與即時流量監控：使用 print 檢視介面計數器（stats、stats-detail），使用 monitor-traffic 觀察每秒速率，並透過 /tool/traffic-monitor 在速率越過閾值時執行指令碼觸發。"
tags:
  - 'stats'
  - 'monitor-traffic'
  - 'interface'
source: https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/interface-stats-and-monitor-traffic
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

每個 RouterOS 介面都包含各種計數器，例如接收和傳送的封包數量、[Fast Path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path) 位元組數、物理側鏈路斷開次數，以及被介面佇列丟棄的封包。這些統計資料可即時反映網路利用率和硬體效能；`monitor-traffic` 命令顯示每秒即時速率檢視，用於驗證吞吐量並排查瓶頸。

## 檢查計數器 {#inspect-the-counters}

使用 `stats`（或使用 `stats-detail` 獲取包含鏈路事件的逐介面列表）列印每個介面的累計計數器：

```ros
[admin@MikroTik] > /interface/print stats
Flags: X - DISABLED; R - RUNNING; S - SLAVE
Columns: NAME, RX-BYTE, TX-BYTE, RX-PACKET, TX-PACKET, RX-DROP, TX-DROP,
         TX-QUEUE-DROP, RX-ERROR, TX-ERROR
#     NAME            RX-BYTE    TX-BYTE  RX-PACKET  TX-PACKET  R  T  T  R  T
0   S ether1                0          0          0          0        0
1  RS ether2       28 805 078  8 117 511    221 798     17 287        0
2   S ether3                0          0          0          0        0
3   S ether4                0          0          0          0        0
4   S ether5                0          0          0          0        0
```

以 `fp` 開頭的值是 Fast Path 計數器；`tx-queue-drop` 統計被[介面佇列](../firewall-and-quality-of-service/queues/index.md#interface-queue)丟棄的封包數（一種擁塞訊號）。`stats-detail` 增加 link-up/down 時間戳和 `link-downs` 計數，它們用於發現線纜抖動（當該數字持續上升時，檢查線纜、SFP 或 PoE；介面特定的錯誤計數器位於[乙太網統計](../wired-connections/ethernet.md#stats)選單中）：

```ros
[admin@MikroTik] > /interface/print stats-detail
Flags: X - DISABLED; R - RUNNING; S - SLAVE
 0   S name="ether1" link-downs=0 rx-byte=0 tx-byte=0 rx-packet=0 tx-packet=0
       tx-queue-drop=0 fp-rx-byte=0 fp-tx-byte=0 fp-rx-packet=0 fp-tx-packet=0
       fp-rps-drop=0

 1  RS name="ether2" last-link-up-time=2026-10-09 12:41:25 link-downs=0
       rx-byte=28 805 078 tx-byte=8 117 511 rx-packet=221 798 tx-packet=17 287
       tx-queue-drop=0 fp-rx-byte=27 917 886 fp-tx-byte=0 fp-rx-packet=221 798
       fp-tx-packet=0 fp-rps-drop=0
```

## 檢視即時速率 {#watch-the-live-rate}

`/interface/monitor-traffic` 顯示所選介面的每秒速率：

```ros
[admin@MikroTik] > /interface/monitor-traffic ether2 duration=3
                       name:   ether2
      rx-packets-per-second:       26
         rx-bits-per-second: 26.4kbps
   fp-rx-packets-per-second:       26
      fp-rx-bits-per-second: 25.6kbps
      tx-packets-per-second:        2
         tx-bits-per-second: 12.7kbps
   fp-tx-packets-per-second:        0
      fp-tx-bits-per-second:     0bps
  tx-queue-drops-per-second:        0
```

該檢視會持續重新整理，直到你停止它；使用 `duration` 限制其持續時間。用它驗證新配置的 VLAN 或橋接成員是否透過流量，或驗證 WAN 埠是否沒有透過超出應有量的流量。傳入多個介面可並排比較，或使用 `aggregate` 觀察整個路由器。當單個介面持續繁忙時，使用 [Torch](./torch.md) 獲取按連線細分的資料。

## 在速率閾值上觸發指令碼 {#trigger-a-script-on-a-rate-threshold}

`/tool/traffic-monitor` 選單會在介面的傳送或接收速率高於（`above`）閾值、低於閾值，或每次輪詢（`always`）時執行指令碼：

```ros
/system/script/add name=rate-alert \
    source=":log info \"ether2 over threshold\""
/tool/traffic-monitor/add name=high-load interface=ether2 \
    traffic=received trigger=above threshold=100000000 \
    on-event=rate-alert
```

:::warning
`/tool/traffic-monitor` 選單使用 `ftp`、`reboot`、`read`、`write` 和 `test` 策略來執行指令碼。有關更多資訊，請參閱[指令碼許可權](../developer-guides/scripting/index.md#script-permissions)。
:::

## 技術細節 {#technical-details}

- 以 `fp` 開頭的值統計走 Fast Path（精簡的 CPU 轉發路徑）的流量。當常規計數器的增長速度遠快於 fp 計數器時，說明流量轉而走完整的 CPU 路徑（防火牆處理等）——這在繁忙的路由器上很有用。
- 介面丟棄/錯誤計數器（`rx-drop`、`tx-drop`、`rx-error`、`tx-error`）統計驅動程式發現的問題；`tx-queue-drop` 則屬於佇列系統。
- `link-downs` 只統計物理鏈路斷開；若 VLAN 成員上該數字不斷上升卻沒有任何 link-down 時間戳，通常說明該成員的父介面存在物理問題。

有關所有計數器和速率行，請參閱 [`/interface`](../cli-reference/interface/index.md) 和 [`/interface/monitor-traffic`](../cli-reference/interface/monitor-traffic.md) CLI 參考；[乙太網統計](../wired-connections/ethernet.md#stats) 選單還提供了硬體層級的計數器。
