---
sidebar_key: "user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support"
sidebar_position: 3
title: "路由協定多核支援"
sidebar_label: "路由協定多核支援"
description: "RouterOS v7 透過將 FIB 更新、BGP 處理和協定處理等任務分配到獨立程式，從而支援多核路由。每個子任務使用私有記憶體或共享記憶體，BGP 輸入/輸出親和性可透過 CLI 自定義。可使用專用命令監控記憶體使用情況和任務狀態，從而提升多核裝置上的效能。"
tags:
  - 'routing'
source: https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/routing-protocol-multi-core-support
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

RouterOS v7 可以在多個程式之間拆分任務。

一個 "**main**" 任務會啟動和停止子任務，並在它們之間處理資料。每個子任務可以分配“私有”記憶體（僅該任務可訪問）和“共享”記憶體（所有路由任務均可訪問）。

啟用多程式路由時，以下任務會在獨立程式中執行：

- FIB 更新。
- 路由策略配置。
- 配置與報告 - 處理靜態路由配置、"route print" 命令、SNMP 監控等。
- BFD 協定處理
- OSPF 協定處理。
- RIP 協定處理。
- ISIS 協定處理。
- EVPN 處理。
- PIM-SM。
- LDP 協定處理。
- Fantasy - 負責生成用於測試的虛擬路由條目。
- BGP 連線與配置處理。
- BGP 接收（每個對等體一個任務，或按特定引數分組）。
- BGP 傳送（每個對等體一個任務，或按特定引數分組）。

## BGP 子任務 {#bgp-sub-tasks}

BGP 接收和傳送可以按特定引數拆分為子任務。例如，你可以按對等體執行輸入，或將所有對等體輸入分組後在 main 程式中執行。你透過 [`input.affinity`](../../cli-reference/routing/bgp/connection.md#input.affinity) 和 [`output.affinity`](../../cli-reference/routing/bgp/connection.md#output.affinity) 引數控制這種拆分，這些引數位於 [`/routing/bgp/template`](../../cli-reference/routing/bgp/template.md)。在核心數較少的裝置上，調整 affinity 值可以提升效能，因為在任務之間共享資料比在單個任務內處理相同資料略慢。例如，在單核或雙核裝置上，在 main 或 instance 程式中執行輸入和輸出可以提升效能。

:::warning
BGP 最多可生成 100 個唯一程式。
:::

你可以使用 [`/routing/stats/process/print`](../../cli-reference/routing/stats/process/index.md) 命令監控當前使用的所有任務及其分配的私有/共享記憶體。

示例輸出：

```text
[admin@BGP_MUM] /routing/stats/process> print interval=1
Columns: TASKS, PRIVATE-MEM-BLOCKS, SHARED-MEM-BLOCKS, PSS, RSS, VMS, RETIRED, ID, PID, RPID, PROCESS-TIME, KERNEL-TIME, CUR-BUSY, MAX-BUSY, CUR-CALC, MAX-CALC
   #  TASKS                         PRIVATE-M  SHARED-M  PSS        RSS      VMS      R  ID       PID  R  PROCESS-  KERNEL-TI  CUR-  MAX-BUSY  CUR-  MAX-CALC
   0  routing tables                11.8MiB    20.0MiB   19.8MiB    42.2MiB  51.4MiB  7  main     195  0  15s470ms  2s50ms     20ms  1s460ms   20ms  35s120ms
      rib                                                                                                                                                    
      connected networks                                                                                                                                     
   1  fib                           2816.0KiB  0         8.1MiB     27.4MiB  51.4MiB     fib      255  1  5s730ms   7m4s790ms        23s350ms        23s350ms
   2  ospf                          512.0KiB   0         3151.0KiB  14.6MiB  51.4MiB     ospf     260  1  20ms      100ms            20ms            20ms    
      connected networks                                                                                                                                     
   3  fantasy                       256.0KiB   0         1898.0KiB  5.8MiB   51.4MiB     fantasy  261  1  40ms      60ms             20ms            20ms    
   4  configuration and reporting   4096.0KiB  512.0KiB  9.2MiB     28.4MiB  51.4MiB     static   262  1  3s210ms   40ms             220ms           220ms   
   5  rip                           512.0KiB   0         3151.0KiB  14.6MiB  51.4MiB     rip      259  1  50ms      90ms             20ms            20ms    
      connected networks                                                                                                                                     
   6  routing policy configuration  768.0KiB   768.0KiB  2250.0KiB  6.2MiB   51.4MiB     policy   256  1  70ms      50ms             20ms            20ms    
   7  BGP service                   768.0KiB   0         3359.0KiB  14.9MiB  51.4MiB     bgp      257  1  4s260ms   8s50ms           30ms            30ms    
      connected networks                                                                                                                                     
   8  BFD service                   512.0KiB   0         3151.0KiB  14.6MiB  51.4MiB     12       258  1  80ms      40ms             20ms            20ms    
      connected networks                                                                                                                                     
   9  BGP Input 10.155.101.232      8.2MiB     6.8MiB    17.0MiB    39.1MiB  51.4MiB     20       270  1  24s880ms  3s60ms           18s550ms        18s550ms
      BGP Output 10.155.101.232                                                                                                                              
  10  Global memory                            256.0KiB                                  global     0  0    
```

## 路由表更新機制 {#routing-table-update-mechanism}

下圖以更友好的方式說明了路由表更新機制的工作方式。

![](/img/54a871194dff78f8.png)

路由協定會持續迴圈執行以下過程：

- "**main**" 程式等待來自其他子任務的更新（1）。
- 如果滿足以下條件，"**main**" 會開始計算新路由（2–4）：
  - 收到來自子任務的更新；
  - 協定尚未釋出所有路由；
  - 配置或鏈路狀態已發生變化。
- 在計算新路由期間（5），會發生以下事件：
  - 所有收到的更新都會應用到路由；
  - 確定閘道器可達性；
  - 解析遞迴路由；
- "**publish**" 事件執行，釋出 "**current**" 路由。在此階段，"**current**" 路由不會改變，但協定仍可接收和傳送更新（6）。
- 執行清理並釋放未使用的記憶體（7）。在此步驟中，新 "**current**" 表中不再使用的任何內容都會被移除（路由、屬性等）。

將 "**updated**" 和 "**current**" 視為路由表的兩個副本。當前使用的是 "**current**" 表（2），而 "**updated**"（1）是將在下一次釋出事件（3 和 4）中釋出的候選路由表。此方法可防止協定在 "**main**" 程式執行 "**publish**" 時用緩衝更新填滿記憶體。相反，協定會將最新更新直接傳送到 main 程式，然後該程式會將新更新複製到 "**updated**" 表中。OSPF 稍複雜一些：它在內部有類似的過程來選擇當前 OSPF 路由，然後將這些路由傳送到 "**main**" 進行進一步處理。
