---
sidebar_key: "getting-started/upgrading-to-v7"
sidebar_position: 9
title: "升級到 v7"
sidebar_label: "升級到 v7"
description: "本頁概述了將 MikroTik RouterOS 升級到版本 7 的步驟和注意事項，詳細說明了與 BGP、OSPF、MPLS 及 User Manager 設定等功能的相容性。它重點介紹了 BGP 連線的必選引數、合併後的 OSPF 選單，以及有關 MPLS 配置備份的注意事項。"
tags:
  - 'bgp'
  - 'ospf'
source: https://manual.mikrotik.com/docs/7.24/getting-started/upgrading-to-v7
captured_at: '2026-11-04T11:29:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

### 簡介 {#introduction}

本文介紹將 RouterOS 升級到 v7 主要版本的建議步驟以及升級時可能遇到的注意事項。

從 v6 升級到 v7 的方式與在 v6 版本內升級相同。更詳細的步驟請參閱[升級手冊](./installation-and-upgrade/upgrade.md)。如果您當前執行的是 RouterOS 版本 6 或更舊版本，我們首先建議升級到 v6 的最新穩定版或長期支援版。

:::info
在大多數使用上述 v6 版本執行正常的 RouterOS 設定中，不需要額外步驟。升級到 v7 會自動轉換配置，裝置將立即正常工作。

:::

:::note
**注意：** 我們不建議在記憶體不足 64 MB 的硬體上執行 v7。

:::

### 功能列表相容性 {#feature-list-compatibility}

如前所述，幾乎所有 RouterOS 系統都可以使用“檢查更新”功能，只需點選幾下即可升級到 v7，但有些功能可能需要額外步驟：

| 功能 | 狀態 |
| :-- | :-- |
| CAPsMAN | OK |
| Interfaces | OK |
| Wireless | OK |
| 橋接/交換 | OK |
| 隧道/PPP | OK |
| IPv6 | OK |
| BGP | OK，但需要注意  [\*](#ospf)  |
| OSPF | OK，但需要注意 [\*\*](#mpls) |
| MPLS | OK，但需要注意 [\*\*\*](#routing-filters) |
| 路由過濾器 | OK，但需要注意 [\*\*\*\*](#notes) |
| PIM-SM | 參見[注意事項](#notes) |
| IGMP 代理 | OK |
| Tools | OK |
| Queues | OK |
| Firewall | OK |
| HotSpot | OK |
| 靜態路由 | OK |
| User Manager | 參見[注意事項](#notes) |

### 備註 {#notes}

:::danger
路由協定配置升級只會觸發一次。這意味著，如果路由器被降級到 ROSv6、修改了配置，然後又被升級回 ROSv7，那麼最終配置將是降級前所存在的配置。要重新觸發 v6 配置轉換，請載入 ROSv6 備份，並使用選項 `force-v6-to-v7-configuration-upgrade=yes`。

:::

### **BGP** {#bgp}

所有已知配置都能從 6.x 成功升級到 7.x。但請注意，配置經過了徹底重新設計。v7 的 BGP 實現提供 **`connection`**、**`template`** 和 **`session`** 選單。

**`Template`** 包含所有與 BGP 協定相關的配置選項。它可用作動態對等體的模板，也可用於將類似配置應用到一組對等體。大多數引數與之前的實現類似，不同之處在於有些引數被分組到輸出和輸入部分，使配置更易讀，也更容易理解該選項是應用於輸入還是輸出。

BGP **`connection`** 的最小引數集是 `remote.address`、`template, connect`、`listen` 和 `local.role`  
Connect 和 listen 引數指定對等體是嘗試連線並監聽遠端地址，還是隻連線或只監聽。在某些設定中，如果對等體使用多跳連線，則還必須配置 `local.address`。對等體角色現在是必填引數。對於基本設定，直接使用 ibgp、ebgp 即可。

現在可以從 `/routing/bgp/session` 選單監控所有已連線和未連線對等體的狀態。  
所有路由程式的其他有用偵錯資訊可以從 `/routing/stats` 選單監控。

網路會被新增到防火牆 address-list，並在 BGP **`connection`** 配置中引用。

### OSPF {#ospf}

所有已知配置都能從 6.x 成功升級到 7.x。  
OSPFv2 和 OSPFv3 現在合併到一個選單 `/routing/ospf` 中。目前沒有預設例項和區域。要啟動 OSPF，您需要建立一個例項，然後向該例項新增一個區域。

RouterOSv7 使用模板將介面與模板匹配，並應用匹配模板中的配置。OSPF 選單 `interface` 和 `neighbor` 包含用於狀態監控的只讀條目。

### MPLS {#mpls}

升級 MPLS 設定時請謹慎，並確保在升級前備份配置。

### 路由過濾器 {#routing-filters}

所有受支援的選項都會順利升級；對於不受支援的選項，則會建立一個空條目。路由過濾器配置已改為類似指令碼的配置。

現在規則可以使用 "if .. then" 語法，根據 "if" 語句中的條件設定引數或應用動作。

多個不帶動作的規則會堆疊到單個規則中，並像防火牆一樣按順序執行；原因是 "set" 引數的順序很重要，每行寫一個 "set" 可以讓人從上到下更容易理解應用了哪些動作。

更多 RouterOSv7 路由過濾器示例見[此處](../user-guides/routing-and-networking-protocols/moving-from-rosv6-to-rosv7.md#routing-filters)。

### PIM-SM {#pim-sm}

將 RouterOS 升級到 v7 不會保留與 PIM 相關的配置。升級後，組播路由配置將在 `/routing/pimsm` 選單下提供，並且不再需要額外的 "multicast" 軟體包。更多資訊見[此處](../user-guides/routing-and-networking-protocols/multicast/pim-sm.md)。

### User Manager {#user-manager}

RouterOSv7 提供了全新且經過重新設計的 User Manager 實現，配置現已整合到 RouterOS WinBox 和控制檯（WEB 管理配置介面不可用），更多資訊見[此處](../authentication-authorization-accounting/user-manager.md)。無法從舊版 User Manager 直接遷移，但可以透過 `/user-manager/database/migrate-legacy-db` 遷移舊資料庫。不過，從零開始配置可能是個好主意。

### 新功能 {#new-features}

RouterOSv7 中實現了新核心，這會因路由快取而導致效能變化，並且某些任務可能因不同程式而需要更高的 CPU 和 RAM 使用量。

- 全新的 NTP 用戶端和伺服器實現。
- 合併了各個單獨的軟體包，只保留 bundle 和少數額外軟體包 *(不再支援 LCD 和 KVM 軟體包)*。
- 新的命令列介面（CLI）風格（仍支援 RouterOS v6 命令）。
- 支援 Let's Encrypt 證書生成。
- 支援 REST API。
- 支援 x86 上的 UEFI 啟動模式。
- CHR FastPath 支援 "vmxnet3" 和 "virtio-net" 驅動。
- 支援 "Cake" 和 "FQ\_Codel" 型別佇列。
- 支援 IPv6 NAT。
- 在配備 Marvell Prestera 交換器的 MikroTik 裝置上支援三層硬體加速、QoS 和 MLAG。
- 支援 MBIM 驅動，併為所有處於 MBIM 模式的調變解調器提供基本功能支援。
- 支援 VRRP 分組以及節點間的連線跟蹤資料同步。
- 支援虛擬可擴充套件區域網路（VXLAN）。
- 支援 L2TPv3。
- 支援 OpenVPN UDP 傳輸協定。
- 支援 WireGuard。
- 在 RTL8367 (RB4011, RB100AHx4) 和 MT7621 (hEX, hEX S, RBM33G) 交換器上支援硬體解除安裝的 VLAN 過濾。
- 在 ARM 和 ARM64 裝置上支援 ZeroTier。
- 支援 x86 裝置的 CPU 頻率調節。

### 不再支援 {#dropped-support}

在 RouterOS v7 中，已不再支援：

- LCD 軟體包
- KVM 軟體包
