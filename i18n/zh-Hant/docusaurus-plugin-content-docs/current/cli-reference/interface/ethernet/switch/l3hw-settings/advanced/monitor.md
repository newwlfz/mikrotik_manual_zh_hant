---
sidebar_key: "cli-reference/interface/ethernet/switch/l3hw-settings/advanced/monitor"
sidebar_position: 1
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/l3hw-settings/advanced/monitor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/l3hw-settings/advanced/monitor {#interfaceethernetswitchl3hw-settingsadvancedmonitor}
**系統能力：** rbswitch 和 crs_prestera
**型別：** 命令

這是 [Monitor](../monitor.md) 的增強版本，為高階使用者提供額外的遙測資料。Advanced Monitor 也包含基本 monitor 的所有資料。

```ros
/interface/ethernet/switch/l3hw-settings/advanced> monitor once
        ipv4-routes-total: 29968
           ipv4-routes-hw: 29957
          ipv4-routes-cpu: 11
  ipv4-shortest-hw-prefix: 0
               ipv4-hosts: 3
        ipv6-routes-total: 4
           ipv6-routes-hw: 0
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 0
         route-queue-size: 0
         route-queue-rate: 0
       route-process-rate: 0
     fasttrack-ipv4-conns: 0
     fasttrack-queue-size: 0
     fasttrack-queue-rate: 0
   fasttrack-process-rate: 0
   fasttrack-hw-min-speed: 0
   fasttrack-hw-offloaded: 0
    fasttrack-hw-unloaded: 0
                  lpm-cap: 54560
                lpm-usage: 31931
             lpm-bank-cap: 2728
           lpm-bank-usage: 46,0,0,0,2589,2591,1983,0,2728,2728,2728,2728,2728,2728,2728,2728,2728,170,0,0
                  pbr-cap: 8192
                pbr-usage: 0
             pbr-lpm-bank: 3
                nat-usage: 0
              nexthop-cap: 8192
            nexthop-usage: 85
```

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="error-code" typ="num">L3HW 驅動處於故障狀態時的錯誤程式碼。</ArgTableRow>
<ArgTableRow arg="state" typ="enum (ok | stopping | starting | fib-failure | net-failure | switch-failure | fasttrack-failure | out-of-memory) { ok:0, stopping:1, starting:2, fib-failure:3, net-failure:4, switch-failure:5, fasttrack-failure:6, out-of-memory:0xFFFFFFF4 }">L3HW 驅動的當前狀態。</ArgTableRow>
<ArgTableRow arg="ipv4-routes-total" typ="num">交換器驅動處理的 IPv4 路由總數。</ArgTableRow>
<ArgTableRow arg="ipv4-routes-hw" typ="num">硬體解除安裝的 IPv4 路由數量（即硬體路由）。</ArgTableRow>
<ArgTableRow arg="ipv4-routes-cpu" typ="num">重定向到 CPU 的 IPv4 路由數量（即軟體路由）。</ArgTableRow>
<ArgTableRow arg="ipv4-shortest-hw-prefix" typ="num">**最短硬體字首 (SHWP)**（針對 IPv4）。如果整個 IPv4 路由表無法放入硬體記憶體，則應用**部分解除安裝**，即最長字首被硬體解除安裝，而較短字首被重定向到 CPU。此欄位顯示被解除安裝到硬體記憶體的最短路由字首 (/x)。所有比該字首更短的字首都由 CPU 處理。`ipv4-shortest-hw-prefix=0` 表示整個 IPv4 路由表都被解除安裝到硬體記憶體。</ArgTableRow>
<ArgTableRow arg="ipv4-hosts" typ="num">硬體解除安裝的 IPv4 主機數量（/32 路由）。</ArgTableRow>
<ArgTableRow arg="ipv6-routes-total" typ="num">交換器驅動處理的 IPv6 路由總數。</ArgTableRow>
<ArgTableRow arg="ipv6-routes-hw" typ="num">硬體解除安裝的 IPv6 路由數量（即硬體路由）。僅在啟用 IPv6 硬體路由（`ipv6-hw=yes`）時顯示。</ArgTableRow>
<ArgTableRow arg="ipv6-routes-cpu" typ="num">重定向到 CPU 的 IPv6 路由數量（即軟體路由）。僅在啟用 IPv6 硬體路由（`ipv6-hw=yes`）時顯示。</ArgTableRow>
<ArgTableRow arg="ipv6-shortest-hw-prefix" typ="num">**最短硬體字首 (SHWP)**（針對 IPv6）。如果整個 IPv6 路由表無法放入硬體記憶體，則應用**部分解除安裝**，即最長字首被硬體解除安裝，而較短字首被重定向到 CPU。此欄位顯示被解除安裝到硬體記憶體的最短路由字首 (/x)。所有比該字首更短的字首都由 CPU 處理。`ipv6-shortest-hw-prefix=0` 表示整個 IPv6 路由表都被解除安裝到硬體記憶體。僅在啟用 IPv6 硬體路由（`ipv6-hw=yes`）時顯示。</ArgTableRow>
<ArgTableRow arg="ipv6-hosts" typ="num">硬體解除安裝的 IPv6 主機數量（/128 路由）。僅在啟用 IPv6 硬體路由（`ipv6-hw=yes`）時顯示。</ArgTableRow>
<ArgTableRow arg="route-queue-size" typ="num" syscap="!prestera-cpss">佇列中等待交換器晶片驅動處理的路由數量。在正常工作條件下，此欄位為 0，表示所有路由都已由驅動處理。</ArgTableRow>
<ArgTableRow arg="route-queue-rate" typ="num" syscap="!prestera-cpss">路由被加入佇列等待交換器驅動處理的速率（`route-queue-size` 路由每秒的增長速率）。</ArgTableRow>
<ArgTableRow arg="route-process-rate" typ="num" syscap="!prestera-cpss">交換器驅動處理先前排隊路由的速率（`route-queue-size` 路由每秒的減少速率）。</ArgTableRow>
<ArgTableRow arg="nexthop-cap" typ="num">下一跳容量。</ArgTableRow>
<ArgTableRow arg="nexthop-usage" typ="num">當前使用的下一跳數量。</ArgTableRow>
<ArgTableRow arg="vxlan-mtu-packet-drop" typ="num" syscap="prestera-bc2">因超出介面 MTU 設定而丟棄的 VXLAN 封包數量。</ArgTableRow>
<ArgTableRow arg="fasttrack-ipv4-conns" typ="num" syscap="prestera-bc2">硬體解除安裝的 FastTrack 連線數量。僅當啟用 FastTrack 連線的硬體解除安裝時才會顯示該引數。</ArgTableRow>
<ArgTableRow arg="fasttrack-queue-size" typ="num" syscap="prestera-bc2">佇列中等待交換器晶片驅動處理的 FastTrack 連線數量。</ArgTableRow>
<ArgTableRow arg="fasttrack-queue-rate" typ="num" syscap="prestera-bc2">FastTrack 連線被加入佇列等待交換器驅動處理的速率（`fasttrack-queue-size` 連線每秒的增長速率）。</ArgTableRow>
<ArgTableRow arg="fasttrack-process-rate" typ="num" syscap="prestera-bc2">交換器驅動處理先前排隊的 FastTrack 連線的速率（`fasttrack-queue-size` 連線每秒的減少速率）。</ArgTableRow>
<ArgTableRow arg="fasttrack-hw-min-speed" typ="num" syscap="prestera-bc2">當用於儲存 FastTrack 的硬體記憶體已滿時，此欄位顯示硬體解除安裝的 FastTrack 連線的最低速度（位元組/秒）。僅當啟用 FastTrack 連線的硬體解除安裝時才會顯示該引數。</ArgTableRow>
<ArgTableRow arg="fasttrack-hw-offloaded" typ="num" syscap="prestera-bc2">解除安裝到硬體的 FastTrack 連線數量。計數器每秒重設。</ArgTableRow>
<ArgTableRow arg="fasttrack-hw-unloaded" typ="num" syscap="prestera-bc2">從硬體解除安裝的 FastTrack 連線數量（重定向到軟體路由）。計數器每秒重設。</ArgTableRow>
<ArgTableRow arg="lpm-cap" typ="num" syscap="!prestera-ac3">LPM 硬體表的大小（LPM = 最長字首匹配）。LPM 儲存用於硬體路由的路由索引。並非所有交換器晶片型號都使用 LPM。其他型號使用 TCAM。</ArgTableRow>
<ArgTableRow arg="lpm-usage" typ="num" syscap="!prestera-ac3">已使用的 LPM 塊數量。</ArgTableRow>
<ArgTableRow arg="lpm-bank-cap" typ="num" syscap="!prestera-ac3">LPM 記憶體按 bank 組織。此值顯示單個 bank 的大小（以 LPM 塊為單位）。bank 大小取決於交換器晶片型號。lpm-cap / lpm-bank-cap = bank 數量。</ArgTableRow>
<ArgTableRow arg="lpm-bank-usage" typ="multi { array-id, lpm-bank: num
 }" syscap="!prestera-ac3">每個 bank 的 LPM 使用量（以 LPM 塊為單位）。</ArgTableRow>
<ArgTableRow arg="pbr-cap" typ="num" syscap="prestera-bc2">策略路由（PBR）硬體表的大小。PBR 用於 FastTrack 連線的 NAT 解除安裝。</ArgTableRow>
<ArgTableRow arg="pbr-usage" typ="num" syscap="prestera-bc2">已使用的 PBR 條目數量。</ArgTableRow>
<ArgTableRow arg="pbr-lpm-bank" typ="num" syscap="prestera-bc2">PBR 與路由表共享 LPM 記憶體 bank。此值顯示與 PBR 共享的 LPM bank 索引（0 = 第一個 bank）。</ArgTableRow>
<ArgTableRow arg="nat-usage" typ="num" syscap="prestera-bc2">已使用的 NAT 硬體條目數量（用於 FastTrack 連線）。</ArgTableRow>
</ArgTable>
