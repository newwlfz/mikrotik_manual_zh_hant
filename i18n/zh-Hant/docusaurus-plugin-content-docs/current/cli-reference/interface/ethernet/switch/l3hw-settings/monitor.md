---
sidebar_key: "cli-reference/interface/ethernet/switch/l3hw-settings/monitor"
sidebar_position: 2
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/cli-reference/interface/ethernet/switch/l3hw-settings/monitor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/ethernet/switch/l3hw-settings/monitor {#interfaceethernetswitchl3hw-settingsmonitor}
**系統能力：** rbswitch and crs_prestera
**型別：** 命令

此命令用於監控交換晶片及 L3HW 相關驅動的統計資訊。

```ros
/interface/ethernet/switch/l3hw-settings/monitor
        ipv4-routes-total: 99363
           ipv4-routes-hw: 61250
          ipv4-routes-cpu: 38112
  ipv4-shortest-hw-prefix: 24
               ipv4-hosts: 87
        ipv6-routes-total: 15
           ipv6-routes-hw: 11
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 7
         route-queue-size: 118
     fasttrack-ipv4-conns: 2031
   fasttrack-hw-min-speed: 0
              nexthop-cap: 8192
            nexthop-usage: 93
    vxlan-mtu-packet-drop: 0
```

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="state" typ="enum (ok | stopping | starting | fib-failure | net-failure | switch-failure | fasttrack-failure | out-of-memory) { ok:0, stopping:1, starting:2, fib-failure:3, net-failure:4, switch-failure:5, fasttrack-failure:6, out-of-memory:0xFFFFFFF4 }">L3HW 驅動的當前狀態。</ArgTableRow>
<ArgTableRow arg="ipv4-routes-total" typ="num">交換晶片驅動處理的 IPv4 路由總數。</ArgTableRow>
<ArgTableRow arg="ipv4-routes-hw" typ="num">硬體解除安裝的 IPv4 路由數量。</ArgTableRow>
<ArgTableRow arg="ipv4-routes-cpu" typ="num">重定向到 CPU 的 IPv4 路由數量。</ArgTableRow>
<ArgTableRow arg="ipv4-shortest-hw-prefix" typ="num">IPv4 的**最短硬體字首 (SHWP)**。如果整個 IPv4 路由表無法裝入硬體記憶體，則會應用**部分解除安裝**，即最長字首被硬體解除安裝，而較短字首被重定向到 CPU。此欄位顯示解除安裝到硬體記憶體的最短路由字首 (/x)。所有比該字首更短的字首均由 CPU 處理。`ipv4-shortest-hw-prefix=0` 表示整個 IPv4 路由表都已解除安裝到硬體記憶體。</ArgTableRow>
<ArgTableRow arg="ipv4-hosts" typ="num">硬體解除安裝的 IPv4 主機（/32 路由）數量。</ArgTableRow>
<ArgTableRow arg="ipv6-routes-total" typ="num">交換晶片驅動處理的 IPv6 路由總數。</ArgTableRow>
<ArgTableRow arg="ipv6-routes-hw" typ="num">硬體解除安裝的 IPv6 路由（也稱為硬體路由）數量。僅當啟用 IPv6 硬體路由（`ipv6-hw=yes`）時顯示。</ArgTableRow>
<ArgTableRow arg="ipv6-routes-cpu" typ="num">重定向到 CPU 的 IPv6 路由（也稱為軟體路由）數量。僅當啟用 IPv6 硬體路由（`ipv6-hw=yes`）時顯示。</ArgTableRow>
<ArgTableRow arg="ipv6-shortest-hw-prefix" typ="num">IPv6 的**最短硬體字首 (SHWP)**。如果整個 IPv6 路由表無法裝入硬體記憶體，則會應用**部分解除安裝**，即最長字首被硬體解除安裝，而較短字首被重定向到 CPU。此欄位顯示解除安裝到硬體記憶體的最短路由字首 (/x)。所有比該字首更短的字首均由 CPU 處理。`ipv6-shortest-hw-prefix=0` 表示整個 IPv6 路由表都已解除安裝到硬體記憶體。僅當啟用 IPv6 硬體路由（`ipv6-hw=yes`）時顯示。</ArgTableRow>
<ArgTableRow arg="ipv6-hosts" typ="num">硬體解除安裝的 IPv6 主機（/128 路由）數量。</ArgTableRow>
<ArgTableRow arg="route-queue-size" typ="num" syscap="!prestera-cpss">等待交換晶片驅動處理的路由佇列中的路由數量。正常工作條件下，此欄位為 0，表示所有路由均已由驅動處理。</ArgTableRow>
<ArgTableRow arg="nexthop-cap" typ="num">下一跳容量。</ArgTableRow>
<ArgTableRow arg="nexthop-usage" typ="num">當前使用的下一跳數量。</ArgTableRow>
<ArgTableRow arg="vxlan-mtu-packet-drop" typ="num" syscap="prestera-bc2">由於超出介面 MTU 設定而丟棄的 VXLAN 封包數量。</ArgTableRow>
<ArgTableRow arg="fasttrack-ipv4-conns" typ="num" syscap="prestera-bc2">硬體解除安裝的 FastTrack 連線數量。僅當啟用 FastTrack 連線的硬體解除安裝時才會顯示此引數。</ArgTableRow>
<ArgTableRow arg="fasttrack-hw-min-speed" typ="num" syscap="prestera-bc2">當用於儲存 FastTrack 的硬體記憶體已滿時，此欄位顯示硬體解除安裝的 FastTrack 連線的最低速度（單位：位元組/秒）。僅當啟用 FastTrack 連線的硬體解除安裝時才會顯示此引數。</ArgTableRow>
</ArgTable>
