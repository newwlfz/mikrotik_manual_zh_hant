---
sidebar_key: "bridging-and-switching/swos/gpen21"
sidebar_position: 4
title: "GPEN21 系列手冊"
sidebar_label: "GPEN21 系列手冊"
description: "適用於 MikroTik GPEN21 智慧 PoE 供電注入器和中繼器的 SwOS Lite 手冊：功能、埠設定、VLAN 和交換器管理。"
source: https://manual.mikrotik.com/docs/7.25/bridging-and-switching/swos/gpen21
captured_at: '2026-11-04T11:15:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

## 概述 {#summary}

GPEN21 是一款智慧供電注入器，可作為高階軟體控制的中繼器使用。它不僅可以透過 PoE 為上行裝置供電，還可以提供一系列有用的軟體功能。GPEN21 具有乙太網埠和 SFP 埠，用於光纖連線。客戶可以選擇使用 GPEN21 為光模組供電，以上行連線到提供商；也可以提供 PoE，為乙太網上行連線到提供商供電（使用我們的 GPeR 和/或 netPower 產品）。GPEN21 裝置可以安全地安裝到牆壁或通訊機櫃上。乙太網線纜可以直接穿過底部線纜開口，也可以布入牆內，按需選擇。

SwOS Lite 是專為管理 MikroTik GPEN21 產品而設計的作業系統。GPEN21 僅支援 SwOS Lite 作業系統。

---

## GPEN21 系列特性 {#gpen21-series-features}

| 功能 | 描述 |
| --- | --- |
| **Forwarding** | 全非阻塞線速交換；Host 表中最多 2k 個 MAC 條目 ¹；轉發資料庫僅基於 SVL 工作；支援巨型幀 - 10222 位元組 |
| **Monitoring** | SNMP；鏈路故障檢測；SFP 診斷；介面統計資訊 |
| **VLAN** | 完全相容 IEEE802.1Q；基於埠的 VLAN；最多 250 個 VLAN 條目（受 SwOS 限制）；VLAN 過濾 |
| **Security** | 埠鎖定；廣播風暴控制 |
| **Quality of Service (QoS)** | 入口流量限制；出口流量限制 |
| **Access Control List** | 入口 ACL 表；最多 32 條 ACL 規則（受 SwOS 限制）；基於埠、L2、L3、L4 協定頭欄位進行分類；ACL 動作包括過濾、轉發和修改協定頭欄位 |

¹ Host 表限制不影響轉發，因為即使達到 MAC 學習限制，封包仍會從上游埠傳送到下游埠，反之亦然。

---

## 連線到裝置 {#connecting-to-the-device}

開啟 Web 瀏覽器，輸入裝置的 IP 地址（預設 192.168.88.1），將出現登入介面。裝置也可以執行 DHCP 用戶端，請檢查 DHCP 伺服器是否已分配其他 IP 地址。

![Gpen21 login](/img/409dd330e4b344ae.webp)

SwOS 預設 IP 地址：**192.168.88.1**，使用者名稱：**admin**，並且沒有密碼。

[鄰居發現](../../system-information-and-utilities/neighbor-discovery.md) 可用於發現 Mikrotik 交換器的 IP 地址。不支援 LLDP。

---

## 介面概覽 {#interface-overview}

SwOS 介面選單由多個標籤頁組成，具體取決於裝置型號。以下是所有可能的 SwOS 選單：Link、SFP、Forwarding、Stats、Errors、Hist、VLAN、VLANs、Hosts、SNMP、ACL、System 和 Upgrade。

SwOS 配置工具中按鈕的說明：

- **Append** - 將新專案新增到列表末尾
- **Apply All** - 應用當前配置更改
- **Cut** - 從列表中移除專案
- **Clear** - 重設專案屬性
- **Discard Changes** - 移除未儲存的配置
- **Insert** - 將新專案新增到列表（放在當前專案之前）
- **Sort** - 按 VLAN ID 對 VLAN 表排序；按 MAC 地址對 Host 表排序
- **Change Password** - 更改裝置密碼
- **Logout** - 從當前設備註銷
- **Reboot** - 重啟裝置
- **Reset Configuration** - 將配置重設為出廠預設值
- **Choose File** - 瀏覽升級或備份檔案
- **Upgrade** - 使用選定的檔案升級裝置韌體
- **Download & Upgrade** - 自動嘗試下載並升級韌體；執行 Web 瀏覽器的 PC 應能夠訪問網際網路
- **Restore Backup** - 使用選定的備份檔案恢復裝置
- **Save Backup** - 生成並下載裝置的備份檔案

> **注意：** 每臺裝置都有自己的韌體，不能安裝在其他系列型號上！
>
> - GPEN21 支援 SwOS Lite v2.13 及更高版本。

---

## 系統 {#system}

System 標籤頁執行以下功能：

- 裝置的一般資訊
- 裝置管理
- 配置重設
- 備份和恢復配置

> **注意：** SwOS 使用簡單演算法來確保 TCP/IP 通訊——它只回複數據包來源的同一 IP 和 MAC 地址。這樣裝置本身就不需要預設閘道器。

![Gpen21 system](/img/d54c34af2163e92c.webp)

| 屬性 | 描述 |
| --- | --- |
| **Address Acquisition** | 指定要使用的地址獲取方法：`DHCP with fallback` - 設備嘗試從 DHCP 伺服器請求 IPv4 地址。如果請求不成功，則可以使用 **Static IP Address** 值訪問裝置`static` - 地址設定為 **Static IP Address** 值（僅 IPv4）`DHCP only` - 裝置使用 DHCPv4 用戶端獲取地址 |
| **Static IP Address** | 如果 **Address Acquisition** 設定為 `DHCP with fallback` 或 `static`，則為裝置的 IP 地址 |
| **Identity** | 裝置名稱（用於 Mikrotik Neighbor Discovery protocol） |
| **Allow From** | 可訪問裝置的 IP 地址。預設值為 `0.0.0.0/0` - 任意地址 |
| **Allow From Ports** | 裝置埠列表，可透過這些埠訪問裝置 |
| **Allow From VLAN** | 可訪問該服務的 VLAN ID。請確保先配置 VLAN 和 VLAN 頁面 |
| **Watchdog** | 啟用或停用系統 Watchdog。在發生故障情況時，它將重設裝置的 CPU |
| **Mikrotik Discovery Protocol** | 啟用或停用 Mikrotik Neighbor Discovery protocol |
| **Dark Mode** | 停用或啟用裝置上的所有 LED |
| **MAC Address** | 裝置的 MAC 地址（只讀） |
| **Serial Number** | 裝置的序列號（只讀） |
| **Board Name** | 裝置的 MikroTik 型號名稱（只讀） |
| **Uptime** | 當前裝置執行時間（只讀） |
| **PoE Out Mode** | 指定 PoE-Out 狀態：<br/><code>auto-on</code> - 板卡將嘗試檢測是否可以向埠供電。要發生上電，備用線對上應存在 3kΩ 至 26.5kΩ 範圍內的電阻<br/><code>forced-on</code> - 移除檢測範圍。因此，乙太網供電將始終開啟<br/><code>off</code> - 該埠的所有檢測和供電均關閉 |
| **PoE Out Status** | 顯示埠上當前的 PoE-Out 狀態（只讀） |

### 密碼和備份 {#password-and-backup}

![Swos system3 css326](/img/3ba4a76afdcc03bc.webp)

---

## 鏈路 {#link}

Link 標籤頁允許你配置每個介面的設定並監控鏈路狀態。

![Gpen21 link](/img/5ff6c176083c3282.webp)

| 屬性 | 說明 |
| --- | --- |
| **Enabled** | 啟用或停用埠 |
| **Name** | 可編輯的埠名稱 |
| **Link Status** | 當前鏈路狀態（只讀） |
| **Auto Negotiation** | 啟用或停用自動協商 |
| **Speed** | 顯示協商後的速度，或允許手動更改埠的速度設定（需要停用自動協商） |
| **Full Duplex** | 顯示協商後的雙工模式，或允許手動更改埠的雙工模式（需要停用自動協商） |
| **Hops** | 顯示鏈路中的 GPER 中繼器數量 |
| **Last Hop** | 如果鏈路終止，顯示最後一個 GPER 中繼器的編號 |
| **Length** | 如果鏈路終止，顯示線纜長度（米） |
| **Fault At** | 如果線纜損壞但鏈路仍活動，顯示到故障點的距離（米） |
| **Cable Pairs** | 顯示線纜線對的四個位置及其狀態：`O` - 開路；`S` - 短路；`P` - 反極性 |

裝置支援最大 10222 位元組的 Jumbo 幀。SwOS Lite 裝置不支援手動降低 MTU 設定。

---

## SFP {#sfp}

SFP 標籤頁允許你監控 SFP 模組的狀態。

![Gpen21 sfp](/img/be292d329c1e86cf.webp)

---

## 轉發 {#forwarding}

Forwarding 標籤頁提供裝置埠之間的高階轉發選項、埠鎖定、頻寬限制和廣播風暴控制功能。

![Gpen21 forwarding](/img/cd3fc931cb10de58.webp)

| 屬性 | 描述 |
| --- | --- |
| **Port Lock** | `Port Lock` - 啟用或停用此埠上的 MAC 地址學習。啟用該選項後，將限制 MAC 地址學習，並且應配置靜態 MAC 地址。任何源 MAC 地址未知的接收幀都將被丟棄。`Lock On First` - 允許從第一個接收幀中學習源 MAC 地址；此屬性應與 `Port Lock` 一起使用。每次介面狀態變化時，第一個 MAC 地址的學習都會重設。 |
| **Uplink Port** | `Set As Uplink Port` - 允許在 PoE-in（Port1）、PoE-out（Port2）或 SFP 介面之間更改上行埠。在下游埠接收的封包僅轉發到上行埠；只能使用單個介面作為上行鏈路。 |
| **Broadcast Storm Control** | `Storm Rate` - 限制介面傳送的廣播封包數量。速率以位元每秒（bps）為單位。`Limit Unknown Unicast` - 將 Host 表中無條目的單播封包納入 `Storm Rate` 限制。 |
| **Bandwidth Limit** | `Ingress Rate` - 限制進入此埠的流量（bps）`Egress Rate` - 限制離開此埠的流量（bps） |

> **注意：** 可以按埠限制入方向/出方向流量。入方向流量使用 policer，出方向流量使用 shaper。入方向 policer 透過丟包來控制接收的流量 —— 所有超過所定義限制的流量都會被丟棄。這可能影響終端主機上的 TCP 擁塞控制機制，實際達到的頻寬可能小於所定義的值。出方向 shaper 會嘗試將超過限制的封包排隊，而不是丟棄它們。最終，當輸出佇列滿時它也會丟棄封包；不過，它應能更好地利用所定義的吞吐量。

---

## Stats、Errors 與 Histogram {#stats-errors-and-histogram}

這些選單提供有關接收和傳送封包的詳細資訊。

![Gpen21 stats](/img/8c24a317a5b42b3a.webp)

![Gpen21 errors](/img/3d5a295488158c9c.webp)

![Gpen21 hist](/img/077b5e39de0381bb.webp)

---

## VLAN 與 VLANs {#vlan-and-vlans}

裝置埠的 VLAN 配置。

![Gpen21 vlan](/img/d06a967fc11b4004.webp)

| 屬性 | 描述 |
| --- | --- |
| **VLAN Mode** (*disabled \| optional \| strict*；預設：**optional**) | VLAN 過濾模式；這些選項與出埠相關（`strict` 模式除外）。`disabled` - 不使用 VLAN 表。裝置會在出埠丟棄帶有 VLAN 標籤的封包。如果封包帶有 VLAN 標籤，且 VLAN ID 與出埠上的 `Default VLAN ID` 匹配，則在 `VLAN Receive=any` 時，裝置會移除 VLAN 標籤並轉發該封包。`optional` - 停用 VLAN 過濾。對於 VLAN ID 不在 VLAN 表中的帶標籤封包，按與無 VLAN 標籤封包相同的方式處理。`strict` - 啟用 VLAN 過濾，並附加入口過濾，檢查入埠是否為 VLAN 表中接收到的 VLAN ID 的成員。入埠上接收到的 VLAN ID 與 VLAN 表不匹配的封包將被丟棄。必須為接入埠指定 Default VLAN ID，因為它將用於為某個埠的入口流量新增標籤，並移除出口流量的標籤。 |
| **VLAN Receive** (*any \| only tagged \| only untagged*；預設：**optional**) | 基於 VLAN 標籤存在情況對接收流量進行過濾。`any` - 允許某個埠上的帶標籤和無標籤封包`only tagged` - 僅允許帶有 VLAN 標籤的封包。"Default VLAN ID" 將不起作用，因為它僅適用於無標籤流量`only untagged` - 僅允許不帶 VLAN 標籤的封包 |
| **Default VLAN ID** (*整數：1..4095*；預設：**1**) | 裝置會將接收到的無標籤封包放入 "Default VLAN ID" VLAN。僅對無標籤流量有效，並且當 **VLAN Receive** 設定為 "any" 或 "only untagged" 時有效。它不適用於帶標籤流量。此引數通常用於為接入埠分配特定 VLAN。如果封包的 VLAN ID 與 Default VLAN ID 匹配，它也會用於移除出口流量的標籤。 |
| **Force VLAN ID** (*yes \| no*；預設：**no**) | 將所有入口流量（帶標籤和無標籤）分配為 `Default VLAN ID` 值。在所有 VLAN 模式下均有效。如果埠接收帶標籤流量，且 `Default VLAN ID` 設定為 1，則使用此引數後，出口流量將不帶標籤。 |

裝置埠的 VLAN 成員關係配置。

![Gpen21 vlans](/img/f6b4c2a55ea8de5f.webp)

| 屬性 | 說明 |
| --- | --- |
| **VLAN ID** (*整數：1..4094*；預設：**0**) | 要為其分配埠的 VLAN ID |
| **Members** (*埠*；預設：**none**) | 允許在定義的 VLAN 上轉發流量的埠組 |

### VLAN 配置示例 {#vlan-configuration-examples}

VLAN 配置示例取自 [CSS610 交換器使用者手冊](https://help.mikrotik.com/docs/display/SWOS/CSS610+series+Manual#CSS610seriesManual-VLANConfigurationExample)；不過，相同的原理也可應用於 GPEN21 裝置。

#### Trunk 和 Access 埠 {#trunk-and-access-ports}

![Access ports](/img/dcbdce357964f958.webp)

1. 在 VLANs 選單中新增 VLAN 條目並指定埠成員關係。

![Css610 vlans](/img/dd2937f9ae0a3398.webp)

1. 在 VLAN 選單中為計劃作為接入埠的埠（不帶標籤）配置 Default VLAN ID，選擇正確的 VLAN Receive 設定（Port2 為 only tagged，Port6-8 為 only untagged），並啟用 strict VLAN 過濾以確保只有被允許的 VLAN 能透過這些埠。

![Css610 vlan](/img/8fb78913b7a9e9ab.webp)

#### Trunk 和 Hybrid 埠 {#trunk-and-hybrid-ports}

![Hybrid ports](/img/90b987271e134d95.webp)

1. 在 VLANs 選單中新增 VLAN 條目並指定埠成員關係。

![Css610 vlans hybrid](/img/167fe7083c6b6f90.webp)

1. 在 VLAN 選單中為計劃作為混合埠的埠（用於不帶標籤的 VLAN）配置 Default VLAN ID，選擇正確的 VLAN Receive 設定（Port2 為 only tagged，Port6-8 為 any），並啟用 strict VLAN 過濾以確保只有被允許的 VLAN 能透過這些埠。

![Css610 vlan hybrid](/img/2d8b9483f5a9f2de.webp)

#### 管理訪問 {#management-access}

在此示例中，將建立 VLAN 200 上的裝置管理訪問。配置方案與“**Trunk and Access Ports**”相同，步驟 **1.、2.** 完全一樣。額外的第 **3** 步要求在 System 選單中指定管理 VLAN ID。應用配置後，裝置將僅在 Port2 上響應帶標籤的 VLAN 200 封包，並在 Port6 上響應無標籤封包。DHCP 用戶端也將在指定的 VLAN ID 中工作。

![Css610 system vlan](/img/2a14134bc28aaf54.webp)

> **警告：** 如果 VLAN 設定配置不正確，更改管理 VLAN 可能會完全停用對裝置管理的訪問。更改此設定前請儲存配置備份，並在管理訪問丟失時使用 [重設和重新安裝](#reset-and-reinstall)。

---

## 主機 {#hosts}

此表表示動態學習到的 MAC 地址到埠的對映條目。它可以包含兩種條目：動態和靜態。動態條目會自動新增——這也稱為學習過程：當裝置從某個埠接收到封包時，它會將該封包的源 MAC 地址以及接收該封包的埠新增到 Host 表，這樣當帶有特定目標 MAC 地址的封包進入時，它就知道應該將封包轉發到哪個埠。如果 Host 表中不存在目標 MAC 地址，則會將封包轉發到組中的所有埠。動態條目大約需要 5 分鐘超時。

如果已存在具有相同 MAC 地址的動態條目，靜態條目將取代動態條目。新增靜態條目還可獲得更多功能。

![Gpen21 hosts](/img/63754074b05b2fc7.webp)

**靜態主機屬性**

| 屬性 | 描述 |
| --- | --- |
| **埠** | 封包應轉發到的埠 |
| **MAC** | MAC 地址 |

**動態主機屬性（只讀）**

| 屬性 | 描述 |
| --- | --- |
| **埠** | 封包應轉發到的埠 |
| **MAC** | 學習到的 MAC 地址 |

---

## SNMP {#snmp}

SwOS 支援 SNMP v1 和 v2c（對 GetRequest、GetNextRequest 和 GetBulkRequest 的響應），並使用 IF-MIB、SNMPv2-MIB、BRIDGE-MIB 和 MIKROTIK-MIB（僅用於 health、PoE-out 和 SFP 診斷）。不支援 SNMP trap 和寫入 SwOS 配置。

可用的 SNMP 資料：

- 系統資訊
- 系統執行時間
- 埠狀態
- 介面統計
- 主機表資訊

![Swos snmp2 1](/img/f3b87569bbcad587.webp)

| 屬性 | 描述 |
| --- | --- |
| **Enabled** | 啟用或停用 SNMP 服務 |
| **Community** | SNMP 團體名稱 |
| **Contact Info** | NMS 的聯絡資訊 |
| **Location** | NMS 的位置資訊 |

---

## ACL {#acl}

訪問控制列表（ACL）規則表是一個非常強大的工具，可基於 L2、L3 和 L4 協定頭欄位條件實現線速的封包過濾、轉發和 VLAN 打標籤。每條規則包含條件部分和動作部分。

![Gpen21 acl](/img/c6424e2e468a15af.webp)

**條件部分引數**

| 屬性 | 描述 |
| --- | --- |
| **From** | 封包進入的埠 |
| **MAC Src** | 源 MAC 地址和掩碼 |
| **MAC Dst** | 目標 MAC 地址和掩碼 |
| **Ethertype** | 封裝在乙太網幀有效載荷中的協定 |
| **VLAN** | VLAN 頭是否存在：`any` / `present` / `not present` |
| **VLAN ID** | VLAN 標籤 ID |
| **Priority** | VLAN 標籤中的優先順序 |
| **IP Src**（IP/netmask:port） | 源 IPv4 地址、子網掩碼和 L4 埠號 |
| **IP Dst**（IP/netmask:port） | 目標 IPv4 地址、子網掩碼和 L4 埠號 |
| **Protocol** *（integer）* | IP 協定 |
| **DSCP** | IP DSCP 欄位 |

**動作部分引數**

| 屬性 | 說明 |
| --- | --- |
| **Drop** | 丟棄封包 |
| **Set VLAN ID** | 如果存在 VLAN 標籤，則更改 VLAN 標籤 ID |
| **Priority** | 如果存在 VLAN 標籤，則更改 VLAN 標籤優先順序位 |

---

## 重設與重新安裝 {#reset-and-reinstall}

GPEN21 內建備份 SwOS 韌體，可在標準韌體損壞或升級失敗時載入：

- 裝置啟動時按住 Reset 按鈕幾秒鐘將重設配置並載入備份韌體。Reset 按鈕位於前蓋後面。
- 載入備份韌體後，可以使用 Web 瀏覽器連線到 192.168.88.1（或 DHCP 伺服器租用的地址）並安裝新的 SwOS 韌體。
