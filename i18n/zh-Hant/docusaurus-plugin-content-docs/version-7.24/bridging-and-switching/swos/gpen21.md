---
title: "GPEN21 系列使用手冊"
description: "MikroTik GPEN21 智慧型 PoE 電源注入器與中繼器的 SwOS Lite 手冊：功能、埠設定、VLAN 與交換器管理。"
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/swos/gpen21
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

## 摘要 {#summary}

GPEN21 是一款智慧型電源注入器，可做為進階的軟體控制中繼器。它不僅可透過 PoE 為上行設備供電，也提供多種實用的軟體功能。GPEN21 具備 Ethernet 與 SFP 埠，可用於光纖連線。客戶可選擇使用 GPEN21 為光學模組供電，以向上游供應商進行上行連線；或提供 PoE，為 Ethernet 上行連線供電（使用我們的 GPeR 與／或 netPower 產品）。GPEN21 機體可穩固安裝於牆面或通訊機櫃。Ethernet 纜線可依需求直接由其底部纜線開孔引出，或穿入牆內配置。

SwOS Lite 是專為管理 MikroTik GPEN21 產品所設計的作業系統。GPEN21 僅支援 SwOS Lite 作業系統。

---

## GPEN21 系列功能 {#gpen21-series-features}

| 功能 | 說明 |
| --- | --- |
| **轉送** | 完整非阻塞線速交換<br/>Host 表中最多 2k 筆 MAC 項目 ¹<br/>Forwarding Database 僅依 SVL 運作<br/>支援 Jumbo frame：10222 bytes |
| **監控** | SNMP<br/>連結故障偵測<br/>SFP 診斷<br/>介面統計 |
| **VLAN** | 完全相容於 IEEE802.1Q<br/>以埠為基礎的 VLAN<br/>最多 250 筆 VLAN 項目（受 SwOS 限制）<br/>VLAN 過濾 |
| **安全性** | Port Lock<br/>Broadcast Storm Control |
| **服務品質（QoS）** | 限制流入流量<br/>限制流出流量 |
| **存取控制清單** | 流入 ACL 表<br/>最多 32 條 ACL 規則（受 SwOS 限制）<br/>依據埠、L2、L3、L4 協定標頭欄位進行分類<br/>ACL 動作包括過濾、轉送與修改協定標頭欄位 |

¹ Host 表限制不會影響轉送，因為即使已達到 MAC 學習上限，封包仍會從上游埠傳送至下游埠，反之亦然。

---

## 連線至設備 {#connecting-to-the-device}

開啟網頁瀏覽器並輸入設備的 IP 位址（預設為 192.168.88.1），隨後會出現登入畫面。設備也可執行 DHCP 用戶端，請確認 DHCP 伺服器是否指派了不同的 IP 位址。

![Gpen21 login](/img/409dd330e4b344ae.webp)

SwOS 預設 IP 位址：**192.168.88.1**，使用者名稱：**admin**，且沒有密碼。

[MikroTik Neighbor Discovery](/docs/system-information-and-utilities/neighbor-discovery) 可用於探索 Mikrotik 交換器的 IP 位址。不支援 LLDP。

---

## 介面概觀 {#interface-overview}

SwOS 介面選單由多個標籤頁組成，實際項目取決於設備型號。以下是所有可能的 SwOS 選單：Link、SFP、Forwarding、Stats、Errors、Hist、VLAN、VLANs、Hosts、SNMP、ACL、System 與 Upgrade。

SwOS 設定工具中的按鈕說明：

- **Append** - 在清單結尾新增項目
- **Apply All** - 套用目前的設定變更
- **Cut** - 從清單中移除項目
- **Clear** - 重設項目的屬性
- **Discard Changes** - 移除尚未儲存的設定
- **Insert** - 在清單中新增項目（放在目前項目之前）
- **Sort** - 依 VLAN-ID 排序 VLAN 表；依 MAC 位址排序主機表
- **Change Password** - 變更設備密碼
- **Logout** - 登出目前設備
- **Reboot** - 重新啟動設備
- **Reset Configuration** - 將設定重設為原廠預設值
- **Choose File** - 瀏覽升級或備份檔案
- **Upgrade** - 使用所選檔案升級設備韌體
- **Download & Upgrade** - 自動嘗試下載並升級韌體，執行網頁瀏覽器的電腦必須能存取網際網路
- **Restore Backup** - 使用所選備份檔案還原設備
- **Save Backup** - 從設備產生並下載備份檔案

> **注意：** 每台設備都有專屬韌體，無法安裝在其他系列型號上！
>
> - GPEN21 支援 SwOS Lite v2.13 及以上版本。

---

## 系統 {#system}

System Tab 執行下列功能：

- 設備的一般資訊
- 設備管理
- 重設設定
- 備份與還原設定

> **注意：** SwOS 使用簡單的演算法確保 TCP/IP 通訊，它只會回覆封包來源的相同 IP 與 MAC 位址。如此一來，設備本身不需要 Default Gateway。

![Gpen21 system](/img/d54c34af2163e92c.webp)

| 屬性 | 說明 |
| --- | --- |
| **Address Acquisition** | 指定要使用的位址取得方式：<br/><code>DHCP with fallback</code> - 設備會嘗試向 DHCP 伺服器要求 IPv4 位址。若要求失敗，可使用 <strong>Static IP Address</strong> 值存取設備<br/><code>static</code> - 位址設定為 <strong>Static IP Address</strong> 值（僅 IPv4）<br/><code>DHCP only</code> - 設備使用 DHCPv4 用戶端取得位址 |
| **Static IP Address** | 當 **Address Acquisition** 設為 `DHCP with fallback` 或 `static` 時，設備的 IP 位址 |
| **Identity** | 設備名稱（用於 Mikrotik Neighbor Discovery protocol） |
| **Allow From** | 可存取設備的 IP 位址。預設值為 `0.0.0.0/0`，表示任何位址 |
| **Allow From Ports** | 可存取設備的設備埠清單 |
| **Allow From VLAN** | 可存取服務的 VLAN ID。請務必先設定 VLAN 與 VLAN 頁面 |
| **Watchdog** | 啟用或停用系統 Watchdog。當發生故障時，它會重設設備的 CPU |
| **Mikrotik Discovery Protocol** | 啟用或停用 Mikrotik Neighbor Discovery protocol |
| **Dark Mode** | 停用或啟用設備上的所有 LED |
| **MAC Address** | 設備的 MAC 位址（唯讀） |
| **Serial Number** | 設備的序號（唯讀） |
| **Board Name** | 設備的 MikroTik 型號名稱（唯讀） |
| **Uptime** | 目前的設備運行時間（唯讀） |
| **PoE Out Mode** | 指定 PoE-Out 狀態：<br/><code>auto-on</code> - 板卡會嘗試偵測是否可對埠供電。若要供電，備用線對上的電阻必須介於 3kΩ 至 26.5kΩ<br/><code>forced-on</code> - 移除偵測範圍。因此，Ethernet 供電將永遠開啟<br/><code>off</code> - 關閉此埠的所有偵測與供電 |
| **PoE Out Status** | 顯示埠上目前的 PoE-Out 狀態（唯讀） |

### 密碼與備份 {#password-and-backup}

![Swos system3 css326](/img/3ba4a76afdcc03bc.webp)

---

## 連結 {#link}

Link Tab 可讓您設定每個介面設定並監控連線狀態。

![Gpen21 link](/img/5ff6c176083c3282.webp)

| 屬性 | 說明 |
| --- | --- |
| **Enabled** | 啟用或停用埠 |
| **Name** | 可編輯的埠名稱 |
| **Link Status** | 目前的連線狀態（唯讀） |
| **Auto Negotiation** | 啟用或停用自動協商 |
| **Speed** | 顯示協商後的速度，或允許手動變更埠的速度設定（需要停用自動協商） |
| **Full Duplex** | 顯示協商後的雙工模式，或允許手動變更埠的雙工模式（需要停用自動協商） |
| **Hops** | 顯示連線中 GPER 中繼器的數量 |
| **Last Hop** | 若連線已終止，顯示最後一個 GPER 中繼器的編號 |
| **Length** | 若連線已終止，以公尺顯示纜線長度 |
| **Fault At** | 若纜線損壞但連線仍有效，顯示到故障點的距離（以公尺為單位） |
| **Cable Pairs** | 顯示纜線線對的四個位置及其狀態：`O` - 開路；`S` - 短路；`P` - 極性反接 |

設備支援最高 10222 bytes 的 Jumbo frames。SwOS Lite 設備不支援手動降低 MTU 設定。

---

## SFP

SFP 標籤可讓你監控 SFP 模組的狀態。

![Gpen21 sfp](/img/be292d329c1e86cf.webp)

---

## Forwarding

Forwarding 標籤提供設備埠之間的進階轉送選項，以及埠鎖定、頻寬限制與廣播風暴控制功能。

![Gpen21 forwarding](/img/cd3fc931cb10de58.webp)

| Property | Description |
| --- | --- |
| **Port Lock** | <code>Port Lock</code> - 啟用或停用此埠的 MAC 位址學習。啟用此選項時，將限制 MAC 位址學習，並應設定靜態 MAC 位址。任何接收到且來源 MAC 位址未知的 frame 都會被丟棄。<br/><code>Lock On First</code> - 允許從接收到的第一個 frame 學習來源 MAC 位址；此屬性應與 <code>Port Lock</code> 一起使用。每次介面狀態變更時，第一個 MAC 位址的學習都會重設。 |
| **Uplink Port** | `Set As Uplink Port` - 允許在 PoE-in（Port1）、PoE-out（Port2）或 SFP 介面之間變更 uplink 埠。在下游埠接收到的封包只會轉送至 uplink 埠；只能使用單一介面作為 uplink。 |
| **Broadcast Storm Control** | <code>Storm Rate</code> - 限制介面傳送的廣播封包數量。速率以 bits per second（bps）為單位。<br/><code>Limit Unknown Unicast</code> - 將 host table 中沒有項目的 unicast 封包納入 <code>Storm Rate</code> 限制。 |
| **Bandwidth Limit** | <code>Ingress Rate</code> - 限制進入此埠的流量（bps）<br/><code>Egress Rate</code> - 限制離開此埠的流量（bps） |

> **Note:** 可以依每個埠限制 ingress/egress 流量。ingress 流量使用 policer，egress 流量使用 shaper。ingress policer 會透過丟棄封包來控制接收到的流量，所有超過定義限制的部分都會被丟棄。這可能會影響終端主機上的 TCP 壅塞控制機制，實際達到的頻寬可能低於定義值。egress shaper 會嘗試將超過限制的封包排入佇列，而不是直接丟棄。最終，當輸出佇列已滿時，它也會丟棄封包；不過，這應能更好地運用定義的輸送量。

---

## 統計、錯誤與直方圖 {#stats-errors-and-histogram}

這些選單提供接收到與傳送封包的詳細資訊。

![Gpen21 stats](/img/8c24a317a5b42b3a.webp)

![Gpen21 errors](/img/3d5a295488158c9c.webp)

![Gpen21 hist](/img/077b5e39de0381bb.webp)

---

## VLAN 與 VLAN {#vlan-and-vlans}

設備埠的 VLAN 設定。

![Gpen21 vlan](/img/d06a967fc11b4004.webp)

| Property | Description |
| --- | --- |
| **VLAN Mode** (*disabled \| optional \| strict*; Default: **optional**) | VLAN 篩選模式；這些選項與 egress 埠相關（strict 模式除外）。<br/><code>disabled</code> - 不使用 VLAN 表。設備會丟棄 egress 埠上帶有 VLAN 標籤的封包。如果封包帶有 VLAN 標籤，且 VLAN ID 與 egress 埠上的 <code>Default VLAN ID</code> 相符，則在 <code>VLAN Receive=any</code> 時，設備會移除 VLAN 標籤並轉送封包。<br/><code>optional</code> - 停用 VLAN 篩選。將帶有 VLAN 標籤 ID 但不存在於 VLAN 表中的封包，視為沒有 VLAN 標籤的封包處理。<br/><code>strict</code> - 啟用 VLAN 篩選並進行額外的 ingress 篩選，檢查 ingress 埠是否為 VLAN 表中所接收 VLAN ID 的成員。ingress 埠上接收到的 VLAN ID 與 VLAN 表不相符的封包將被丟棄。access 埠必須指定 Default VLAN ID，因為它會用於標記該埠的 ingress 流量，並移除該埠 egress 流量的標籤。 |
| **VLAN Receive** (*any \| only tagged \| only untagged*; Default: **optional**) | 根據 VLAN 標籤是否存在來篩選接收的流量。<br/><code>any</code> - 允許特定埠上有帶標籤與未帶標籤的封包<br/><code>only tagged</code> - 只允許帶有 VLAN 標籤的封包。"Default VLAN ID" 將無法運作，因為它僅適用於未帶標籤的流量<br/><code>only untagged</code> - 只允許沒有 VLAN 標籤的封包 |
| **Default VLAN ID** (*integer: 1..4095*; Default: **1**) | 設備會將接收到的未帶標籤封包放入 "Default VLAN ID" VLAN。僅對未帶標籤流量生效，且 **VLAN Receive** 設為 "any" 或 "only untagged" 時才會生效。不適用於帶標籤流量。此參數通常用於將特定 VLAN 指派給 access 埠。若封包的 VLAN ID 與 Default VLAN ID 相符，也會用於移除 egress 流量的標籤。 |
| **Force VLAN ID** (*yes \| no*; Default: **no**) | 將 `Default VLAN ID` 值指派給所有 ingress 流量（帶標籤與未帶標籤）。在所有 VLAN Mode 中都會生效。如果埠接收到帶標籤流量，且 `Default VLAN ID` 設為 1，則啟用此參數後，egress 流量將不帶標籤。 |

設備埠的 VLAN 成員設定。

![Gpen21 vlans](/img/f6b4c2a55ea8de5f.webp)

| Property | Description |
| --- | --- |
| **VLAN ID** (*integer: 1..4094*; Default: **0**) | 要指派埠的 VLAN ID |
| **Members** (*ports*; Default: **none**) | 允許在指定 VLAN 上轉送流量的埠群組 |

### VLAN 設定範例 {#vlan-configuration-examples}

VLAN 設定範例取自 [CSS610 switch user manual](https://help.mikrotik.com/docs/display/SWOS/CSS610+series+Manual#CSS610seriesManual-VLANConfigurationExample)；不過，相同的原則也可套用於 GPEN21 設備。

#### Trunk 與 Access 埠 {#trunk-and-access-ports}

![Access ports](/img/dcbdce357964f958.webp)

1. 在 VLANs 選單中新增 VLAN 項目，並指定埠成員。

![Css610 vlans](/img/dd2937f9ae0a3398.webp)

1. 在 VLAN 選單中，於預計作為 access 的埠上設定 Default VLAN ID（untagged），選擇正確的 VLAN Receive 設定（Port2 only tagged、Port6-8 only untagged），並啟用 strict VLAN filtering，以確保只有允許的 VLAN 能通過這些埠。

![Css610 vlan](/img/8fb78913b7a9e9ab.webp)

#### Trunk 與 Hybrid 埠 {#trunk-and-hybrid-ports}

![Hybrid ports](/img/90b987271e134d95.webp)

1. 在 VLANs 選單中新增 VLAN 項目，並指定埠成員資格。

![Css610 vlans hybrid](/img/167fe7083c6b6f90.webp)

1. 在 VLAN 選單中，於預計作為 hybrid 的埠上設定 Default VLAN ID（用於 untagged VLAN），選擇正確的 VLAN Receive 設定（Port2 only tagged、Port6-8 any），並啟用 strict VLAN filtering，以確保只有允許的 VLAN 能通過這些埠。

![Css610 vlan hybrid](/img/2d8b9483f5a9f2de.webp)

#### 管理存取 {#management-access}

在此範例中，將在 VLAN 200 上建立設備管理存取。設定架構與「**Trunk 與 Access 埠**」相同，且步驟 **1.、2.** 一致。額外的**第 3** 個步驟需要在 System 選單中指定管理 VLAN ID。套用設定後，設備只會回應 Port2 上 tagged VLAN 200 的封包，以及 Port6 上的 untagged 封包。DHCP client 也會在指定的 VLAN ID 中運作。

![Css610 system vlan](/img/2a14134bc28aaf54.webp)

> **警告：** 如果 VLAN 設定不正確，變更管理 VLAN 可能會完全停用對設備管理的存取。變更此設定前請儲存設定備份，若管理存取遺失，請使用 [Reset and Reinstall](#reset-and-reinstall)。

---

## Hosts

此表格代表動態學習到的 MAC 位址與埠對應項目。它可以包含兩種類型的項目：dynamic 與 static。Dynamic 項目會自動新增，這也稱為學習程序：當設備從某個埠收到封包時，它會將封包的來源 MAC 位址與收到封包的埠新增到 host table，因此當具有特定目的 MAC 位址的封包進入時，它會知道應將封包轉送至哪個埠。如果目的 MAC 位址不存在於 host table 中，則會將封包轉送至群組中的所有埠。Dynamic 項目約 5 分鐘後逾時。

如果已有相同 MAC 位址的動態項目，靜態項目將會取代動態項目。新增靜態項目也可使用更多功能。

![Gpen21 hosts](/img/63754074b05b2fc7.webp)

**靜態主機屬性**

| 屬性 | 說明 |
| --- | --- |
| **Ports** | 封包應轉送至的埠 |
| **MAC** | MAC 位址 |

**動態主機屬性（唯讀）**

| 屬性 | 說明 |
| --- | --- |
| **Port** | 封包應轉送至的埠 |
| **MAC** | 已學習到的 MAC 位址 |

---

## SNMP

SwOS 支援 SNMP v1 與 v2c（回應 GetRequest、GetNextRequest 與 GetBulkRequest），並使用 IF-MIB、SNMPv2-MIB、BRIDGE-MIB 與 MIKROTIK-MIB（僅用於健康狀態、PoE-out 與 SFP 診斷）。不支援 SNMP trap 與寫入 SwOS 設定。

可用的 SNMP 資料：

- 系統資訊
- 系統運行時間
- 埠狀態
- 介面統計
- 主機表資訊

![Swos snmp2 1](/img/f3b87569bbcad587.webp)

| 屬性 | 說明 |
| --- | --- |
| **Enabled** | 啟用或停用 SNMP 服務 |
| **Community** | SNMP community 名稱 |
| **Contact Info** | NMS 的聯絡資訊 |
| **Location** | NMS 的位置資訊 |

---

## ACL

存取控制清單（ACL）規則表是非常強大的工具，可根據 L2、L3 與 L4 通訊協定標頭欄位條件，進行線速封包過濾、轉送與 VLAN 標記。每條規則都包含條件部分與動作部分。

![Gpen21 acl](/img/c6424e2e468a15af.webp)

**條件部分參數**

| 屬性 | 說明 |
| --- | --- |
| **From** | 封包進入的埠 |
| **MAC Src** | 來源 MAC 位址與遮罩 |
| **MAC Dst** | 目的 MAC 位址與遮罩 |
| **Ethertype** | 封裝在 Ethernet Frame 酬載中的通訊協定 |
| **VLAN** | VLAN 標頭是否存在：`any` / `present` / `not present` |
| **VLAN ID** | VLAN 標籤 ID |
| **Priority** | VLAN 標籤中的優先順序 |
| **IP Src** (IP/netmask:port) | 來源 IPv4 位址、網路遮罩與 L4 連接埠號碼 |
| **IP Dst** (IP/netmask:port) | 目的 IPv4 位址、網路遮罩與 L4 連接埠號碼 |
| **Protocol** *(integer)* | IP 通訊協定 |
| **DSCP** | IP DSCP 欄位 |

**動作部分參數**

| 屬性 | 說明 |
| --- | --- |
| **Drop** | 丟棄封包 |
| **Set VLAN ID** | 若存在 VLAN 標籤，則變更 VLAN 標籤 ID |
| **Priority** | 若存在 VLAN 標籤，則變更 VLAN 標籤優先順序位元 |

---

## 重設與重新安裝 {#reset-and-reinstall}

GPEN21 內建備份 SwOS 韌體，可在標準韌體損毀或升級失敗時載入：

- 在設備開機時按住 Reset 按鈕幾秒，將會重設設定並載入備份韌體。Reset 按鈕位於前蓋後方。
- 載入備份韌體後，可以使用網頁瀏覽器連線至 192.168.88.1（或 DHCP 伺服器提供的租用位址），並安裝新的 SwOS 韌體。
