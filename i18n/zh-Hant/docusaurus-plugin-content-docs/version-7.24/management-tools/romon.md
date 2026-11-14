---
sidebar_key: "management-tools/romon"
sidebar_position: 9
title: "RoMON"
sidebar_label: "RoMON"
description: "RoMON 是一種路由器管理覆蓋網路，它建立獨立的 MAC 層網路以實現安全的路由器管理，使用 EtherType 0x88bf 和 DST-MAC 01:80:c2:00:88:bf。它允許埠以可配置的 ID 和開銷參與，支援用於封包轉發的動態 ACL 規則，並使用 MD5 雜湊。"
tags:
  - 'romon'
  - 'mac-layer'
  - 'management'
source: https://manual.mikrotik.com/docs/7.24/management-tools/romon
captured_at: '2026-11-04T11:32:05+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

RoMON 代表“Router Management Overlay Network”。RoMON 透過建立一個獨立的 MAC 層對等發現和資料轉發網路來工作。RoMON 封包使用 EtherType 0x88bf 和 DST-MAC 01:80:c2:00:88:bf 進行封裝，其網路獨立於 L2 或 L3 轉發配置執行。啟用 RoMON 後，任何接收到的 RoMON 封包都不會由 sniffer 或 torch 工具顯示。

RoMON 網路上的每臺路由器都會被分配其 RoMON ID。RoMON ID 可以從埠 MAC 地址中選擇，也可以由使用者指定。

RoMON 協定不提供加密服務。加密在“應用”層提供，例如使用 ssh 或使用安全的 WinBox。

:::info
RoMON 封包可以透過網路交換器或網橋轉發，除非對組播流量有特定限制。使用帶硬體解除安裝的 MikroTik 網橋時，這些封包會被當作常規組播封包處理，並在整個網路中泛洪。

自 RouterOS v7.17 起，如果啟用了 RoMON 服務且交換晶片支援 ACL 規則，則會自動建立動態規則，將這些封包重定向到執行 RoMON 服務的 CPU。但是，如果交換器不支援 ACL 規則且配置不一致，例如 CPU 和 RoMON 未標記封包不在同一 VLAN 中，RoMON 服務可能無法按預期工作。

**RB5009**（switch‑chip 88E6393X）不支援此路徑。該晶片的 frame‑types=admit‑only‑vlan‑tagged 過濾器會在應用任何 ACL 規則之前丟棄 RoMON 幀，因此這些封包永遠不會到達 CPU。

:::

## 配置 {#configuration}

為了使裝置加入 RoMON 網路，必須啟用 RoMON 功能，並且必須指定加入 RoMON 網路的埠。

**子選單：** `/tool/romon`

| 屬性 | 描述 |
| :-- | :-- |
| **enabled** (*yes \| no*；預設：**no**) | 停用或啟用 RoMON 功能。 |
| **id** (*MAC 地址*；預設：**00:00:00:00:00:00**) | 用作此路由器 ID 的 MAC 地址。 |
| **secrets** (*string*；預設：) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於 RoMON 訊息雜湊的全域性金鑰列表。 |

當啟用 RoMON 而未指定 ID 時，會自動選擇 ID：

```routeros
[admin@MikroTik] /tool/romon> print 
     enabled: yes              
          id: 00:00:00:00:00:00
     secrets:                  
  current-id: DC:2C:6E:9E:11:27
```

加入 RoMON 網路的埠在 `/tool/romon/port` 選單中配置。埠列表是匹配特定介面或 interface-list 的條目列表。每個條目定義匹配的介面是允許還是禁止加入 RoMON 網路。如果允許加入，該條目還會指定埠開銷。

**子選單：** `/tool/romon/port`

| 屬性 | 描述 |
| :-- | :-- |
| **comment** (*string*；預設：) | 條目的簡短描述。 |
| **cost** (*integer: 0..4294967295*；預設：**100**) | 更改埠開銷。 |
| **disabled** (*yes \| no*；預設：**no**) | 更改條目是否被停用。 |
| **interface** (*name*；預設：) | 用於 RoMON 的介面名稱或 interface-list。 |
| **secrets** (*string*；預設：) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用於 RoMON 訊息雜湊的單個埠金鑰列表。 |
| **forbid** (*yes \| no*；預設：**no**) | 更改匹配的介面是允許還是禁止加入 RoMON 網路。|

:::info
預設預配置了一個 interface-list 為 "all" 的條目。這意味著啟用 RoMON 服務後，預設允許所有介面加入 RoMON 網路。此預設條目無法刪除或啟用/停用，但仍可以修改其 `cost`、將其設定為 `forbid` 參與，或配置 `secrets`。

:::

## 金鑰 {#secrets}

RoMON 協定金鑰透過使用 MD5 對訊息內容進行雜湊，用於訊息認證、完整性檢查和重放防護。

對於每個介面，如果介面特定的金鑰列表為空，則使用全域性金鑰列表。傳送時，如果列表不為空且第一項不是“空金鑰”（空字串 = ""），則使用列表中的第一個金鑰對訊息進行雜湊；否則，訊息將以未雜湊方式傳送。接收時，僅當金鑰列表為空或包含“空金鑰”時才接受未雜湊訊息；如果雜湊訊息使用列表中的任一金鑰進行雜湊，則接受該訊息。

此設計允許在網路中逐步引入和/或更改金鑰，而不會中斷 RoMON 服務，並且可以透過 RoMON 本身完成，例如：

- 最初，所有路由器都沒有金鑰。
- 逐臺將每臺路由器配置為 secrets="","mysecret" —— 這會使所有路由器仍然傳送未受保護的資料幀，但它們都將準備好接受使用金鑰 "mysecret" 保護的幀。
- 逐臺將每臺路由器配置為 secrets="mysecret","" —— 這會使所有路由器使用金鑰 "mysecret"，但仍會接受未受保護的幀（來自尚未更改的路由器）。
- 將每臺路由器配置為 secrets="mysecret" —— 這會使所有路由器使用金鑰 "mysecret"，並且只接受使用 "mysecret" 保護的幀。

在網路中更改金鑰應以類似方式進行，即在一段時間內網路中同時使用兩個金鑰。

## 對等發現 {#peer-discovery}

為了發現 RoMON 網路上的所有路由器，必須使用 RoMON discover 命令：

```ros
[admin@MikroTik] > /tool/romon/discover 
Flags: A - active
Columns: ADDRESS, COST, HOPS, PATH, L2MTU, IDENTITY, VERSION, BOARD
   ADDRESS            COS  H  PATH               L2MT  IDENTITY   VERSION    BOARD              
A  6C:3B:6B:48:0E:8B  200  1  6C:3B:6B:48:0E:8B  1500  hEX        6.47beta7  RB750Gr3           
A  6C:3B:6B:ED:83:69  200  1  6C:3B:6B:ED:83:69  1500  CCR1009    6.47beta7  CCR1009-7G-1C-1S+  
A  B8:69:F4:B3:1B:D2  200  1  B8:69:F4:B3:1B:D2  1500  4K11       6.47beta7  RB4011iGS+5HacQ2HnD
A  CC:2D:E0:26:22:4D  200  1  CC:2D:E0:26:22:4D  1500  CCR1036    6.47beta7  CCR1036-8G-2S+     
A  CC:2D:E0:8D:01:88  200  1  CC:2D:E0:8D:01:88  1500  CRS328     6.47beta7  CRS328-24P-4S+     
A  E4:8D:8C:1C:D3:0E  200  1  E4:8D:8C:1C:D3:0E  1500  MikroTik   6.47beta7  RB2011iLS          
A  E4:8D:8C:49:49:DB  200  1  E4:8D:8C:49:49:DB  1500  hAP        6.47beta7  RB962UiGS-5HacT2HnT

```

## 配置示例 {#configuration-examples}

為了使裝置加入 RoMON 網路，必須啟用 RoMON 功能，並且必須指定加入 RoMON 網路的埠。

```ros
/tool/romon/set enabled=yes secrets=testing
```

加入 RoMON 網路的埠在 **RoMON 埠** 選單中配置。埠列表是匹配特定埠或所有埠的條目列表，並指定匹配的埠是否被禁止加入 RoMON 網路；如果允許該埠加入 RoMON 網路，該條目還會指定埠開銷。請注意，所有特定埠條目的優先順序都高於 **interface=all** 的通配條目。

例如，以下列表指定所有埠以開銷 100 加入 RoMON 網路，ether7 介面以開銷 200 加入：

```ros
[admin@MikroTik] > /tool/romon/port/print
Flags: * - default
Columns: INTERFACE, FORBID, COST
#     INTERF  FO  COS
0  *  all     no  100
1     ether7  no  200
```

預設情況下，會建立一個通配條目，其 **forbid=no** 且 **cost=100**。

### 應用 {#applications}

可以在 RoMON 網路上執行多種應用。

為了測試 RoMON 網路上特定路由器的可達性，可以使用 RoMON ping 命令：

```ros
[admin@MikroTik] > /tool/romon/ping id=6C:3B:6B:48:0E:8B count=5
  SEQ HOST                                    TIME  STATUS                                                    
    0 6C:3B:6B:48:0E:8B                       1ms                                                             
    1 6C:3B:6B:48:0E:8B                       0ms                                                             
    2 6C:3B:6B:48:0E:8B                       1ms                                                             
    3 6C:3B:6B:48:0E:8B                       0ms                                                             
    4 6C:3B:6B:48:0E:8B                       1ms                                                             
    sent=5 received=5 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=1ms
```

為了與 RoMON 網路上的路由器建立安全終端連線，可以使用 RoMON SSH 命令：

```ros
[admin@MikroTik] > /tool/romon/ssh 6C:3B:6B:48:0E:8B
```

### 使用 CLI 在 WinBox 中執行 RoMON {#run-romon-in-winbox-by-using-cli}

為了在計算機上直接使用命令列建立 RoMON 會話，必須指定 RoMON 代理和目標路由器地址。RoMON 代理必須儲存在 WinBox 的 Managed routers 列表中，才能成功建立連線：

```ros
winbox.exe --romon 192.168.88.1 6C:3B:6B:48:0E:8B admin ""
```

### 透過 WinBox GUI 連線到 RoMON {#connect-to-romon-through-winbox-gui}

觀看影片[此處](https://www.youtube.com/watch?v=Peg6UcSJ_eA)。
