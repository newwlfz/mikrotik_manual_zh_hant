---
sidebar_key: "bridging-and-switching/crs1xx-and-2xx-series-switches"
sidebar_position: 8
title: "CRS1xx 和 2xx 系列交換器"
sidebar_label: "CRS1xx 和 2xx 系列交換器"
description: "本頁面介紹 MikroTik RouterOS CRS1xx 和 2xx 系列交換器，重點說明其高效能特性，包括二層/三層交換、VLAN 支援、QoS 工具、映象功能和埠隔離選項。頁面詳細說明了各型號之間的差異、CPU 速度和巨型幀大小等技術規格，並提供了 VLAN 相關術語的縮寫。"
tags:
  - 'vlan'
  - 'qos'
  - 'switching'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/crs1xx-and-2xx-series-switches
captured_at: '2026-11-07T17:11:03.548Z'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

Cloud Router Switch 系列是高度整合的交換器，配備高效能 MIPS CPU 和功能豐富的包處理器。CRS 交換器可設計用於各種乙太網應用，包括非管理型交換器、二層管理型交換器、運營商交換器以及無線/有線統一包處理。請參閱 [Cloud Router Switch](./user-guides/crs1xx-2xx-series-switches-examples.md) 配置示例。

:::danger
本文適用於 CRS1xx 和 CRS2xx 系列交換器，不適用於搭載 Marvell Prestera 交換晶片的 MikroTik 裝置（例如 CRS3xx）。有關搭載 Marvell Prestera 交換晶片的 MikroTik 裝置，請參閱 [Marvell Prestera 交換晶片特性](./marvell-prestera-switch-chip-features.md)手冊。
:::

| 功能 | 描述 |
| :-- | :-- |
| **轉發** | <ul class="bullets"><li>可配置用於交換或路由的埠</li><li>完全非阻塞線速交換</li><li>在單播 FDB 中最多 16k 條 MAC 條目，用於第 2 層單播轉發</li><li>在組播 FDB 中最多 1k 條 MAC 條目，用於組播轉發</li><li>在保留 FDB 中最多 256 條 MAC 條目，用於控制和管理目的</li><li>所有轉發資料庫均支援 IVL 和 SVL</li><li>可配置的基於埠的 MAC 學習限制</li><li>巨型幀支援（CRS1xx/2xx：9204 位元組；CRS125/CRS109：4064 位元組）</li><li>支援 IGMP Snooping</li></ul> |
| **映象** | <ul class="bullets"><li>各種型別的映象：<ul class="bullets"><li>基於埠的映象</li><li>基於 VLAN 的映象</li><li>基於 MAC 的映象</li></ul></li><li>2 個獨立的映象分析埠</li></ul> |
| **VLAN** | <ul class="bullets"><li>完全相容 IEEE802.1Q 和 IEEE802.1ad VLAN</li><li>4k 個活動 VLAN</li><li>靈活的 VLAN 分配：<ul class="bullets"><li>基於埠的 VLAN</li><li>基於協定的 VLAN</li><li>基於 MAC 的 VLAN</li></ul></li><li>從任意到任意的 VLAN 轉換與交換</li><li>1:1 VLAN 交換 - VLAN 到埠對映</li><li>VLAN 過濾</li></ul> |
| **埠隔離與洩漏** | <ul class="bullets"><li>適用於 Private VLAN 實現</li><li>3 種埠配置型別：Promiscuous、Isolated 和 Community</li><li>最多 28 個 Community 配置</li><li>Leakage 配置允許繞過出方向 VLAN 過濾</li></ul> |
| **鏈路聚合** | <ul class="bullets"><li>支援靜態鏈路聚合組</li><li>最多 8 個 Port Trunk 組</li><li>每個 Port Trunk 組最多 8 個成員埠</li><li>硬體自動故障轉移和負載均衡</li></ul> |
| **服務質量（QoS）** | <ul class="bullets"><li>靈活的 QoS 分類和分配：<ul class="bullets"><li>基於埠</li><li>基於 MAC</li><li>基於 VLAN</li><li>基於協定</li><li>基於 PCP/DEI</li><li>基於 DSCP</li><li>基於 ACL</li></ul></li><li>用於服務提供商與用戶端網路之間 QoS 域轉換的 QoS 重標記和重對映</li><li>根據配置的優先順序覆蓋每個 QoS 分配</li></ul> |
| **整形與排程** | <ul class="bullets"><li>每個物理埠 8 個佇列</li><li>按埠、按佇列、按佇列組整形</li></ul> |
| **訪問控制列表** | <ul class="bullets"><li>入方向與出方向 ACL 表</li><li>最多 128 條 ACL 規則（受 RouterOS 限制）</li><li>基於埠、L2、L3、L4 協定頭欄位的分類</li><li>ACL 操作包括過濾、轉發和修改協定頭欄位</li></ul> |

## Cloud Router Switch 型號 {#cloud-router-switch-models}

---

下表說明了 Cloud Router Switch 各型號之間的主要差異。

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **型號** | **交換晶片** | **CPU** | **無線** | **SFP+ 埠** | **訪問控制列表** | **巨型幀（位元組）** |
| **CRS105-5S-FB** | QCA-8511 | 400MHz | - | - | + | 9204 |
| **CRS106-1C-5S** | QCA-8511 | 400MHz | - | - | + | 9204 |
| **CRS112-8G-4S** | QCA-8511 | 400MHz | - | - | + | 9204 |
| **CRS210-8G-2S+** | QCA-8519 | 400MHz | - | + | + | 9204 |
| **CRS212-1G-10S-1S+** | QCA-8519 | 400MHz | - | + | + | 9204 |
| **CRS226-24G-2S+** | QCA-8519 | 400MHz | - | + | + | 9204 |
| **CRS125-24G-1S** | QCA-8513L | 600MHz | - | - | - | 4064 |
| **CRS125-24G-1S-2HnD** | QCA-8513L | 600MHz | + | - | - | 4064 |
| **CRS109-8G-1S-2HnD** | QCA-8513L | 600MHz | + | - | - | 4064 |

## 縮寫與說明 {#abbreviations-and-explanations}

---

CVID - 客戶 VLAN ID：IEEE 802.1ad 幀的內層 VLAN 標籤 ID

SVID - 服務 VLAN ID：IEEE 802.1ad 幀的外層 VLAN 標籤 ID

IVL - 獨立 VLAN 學習 - 學習和查詢基於 MAC 地址和 VLAN ID 兩者。

SVL - 共享 VLAN 學習 - 學習和查詢基於 MAC 地址 - 而不是 VLAN ID。

TPID - 標籤協定識別符號

PCP - 優先順序程式碼點：一個 3 位欄位，表示 IEEE 802.1p 優先順序

DEI - 丟棄資格指示符

DSCP - 差分服務程式碼點

丟棄優先順序 - 一種內部 CRS 交換器 QoS 屬性，用於封包入隊或丟棄。

## 埠交換 {#port-switching}

---

要在 CRS1xx/2xx 系列交換器上設定埠交換，請參閱 [網橋硬體解除安裝](./index.md#bridge-hardware-offloading) 頁面。

:::warning
在建立啟用硬體解除安裝的網橋並新增交換埠組時，CRS 交換器會建立動態保留 VLAN 條目（VLAN4091；VLAN4090；VLAN4089 等）。這些 VLAN 是內部執行所必需的，其優先順序低於使用者配置的 VLAN。
:::

### 多個交換器組 {#multiple-switch-groups}

CRS1xx/2xx 系列交換器允許使用多個帶硬體解除安裝的網橋；這樣可以輕鬆隔離多個交換器組。只需建立多個網橋並啟用硬體解除安裝即可完成。

:::warning
多硬體解除安裝橋接配置被設計為一種快速且簡單的埠隔離解決方案，但它限制了 CRS 交換晶片所支援的部分 VLAN 功能。對於高階配置，請在 CRS 交換晶片內為所有埠使用一個橋接，配置 VLAN，並透過埠隔離配置檔案配置來隔離埠組。
:::

:::danger
CRS1xx/2xx 系列交換器可以執行多個啟用 (R)STP 的硬體解除安裝網橋，但不建議這樣做，因為裝置並非設計為在硬體層面執行多個 (R)STP 例項。要在啟用 (R)STP 的同時隔離多個交換器組，應透過埠隔離配置檔案配置來隔離埠組。
:::

## 全域性設定 {#global-settings}

---

CRS 交換晶片可透過 `/interface/ethernet/switch` 控制檯選單配置。

**子選單：** `/interface/ethernet/switch`

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string value*; Default: **switch1**) | 交換器的名稱。 |
| **bridge-type** (*customer-vid-used-as-lookup-vid \| service-vid-used-as-lookup-vid*; Default: **customer-vid-used-as-lookup-vid**) | bridge 型別定義哪個 VLAN 標籤用作 Lookup-VID。Lookup-VID 用作所有基於 VLAN 的查詢的 VLAN 鍵。 |
| **mac-level-isolation** (*yes \| no*; Default: **yes**) | 全域性啟用或停用 MAC 級別隔離。啟用後，交換器將檢查源和目的 MAC 地址表項及其在單播轉發表中的 `isolation-profile`。預設情況下，交換器會學習 MAC 地址並將其放入 `promiscuous` 隔離配置檔案。建立靜態單播表項時可以使用其他隔離配置檔案。如果源或目的 MAC 地址位於 `promiscuous` 隔離配置檔案中，則轉發該封包。如果源和目的 MAC 地址都位於同一個 `community1` 或 `community2` 隔離配置檔案中，則轉發該封包。當源和目的 MAC 地址隔離配置檔案為 `isolated`，或源和目的 MAC 地址隔離配置檔案來自不同 community（例如源 MAC 地址為 `community1`，目的 MAC 地址為 `community2`）時，丟棄該封包。當 MAC 級別隔離全域性停用時，隔離被繞過。 |
| **use-svid-in-one2one-vlan-lookup** (*yes \| no*; Default: **no**) | 是否使用服務 VLAN ID 進行 1:1 VLAN 交換查詢。 |
| **use-cvid-in-one2one-vlan-lookup** (*yes \| no*; Default: **yes**) | 是否使用客戶 VLAN ID 進行 1:1 VLAN 交換查詢。 |
| <strong>multicast-lookup-mode</strong> (<em>dst-ip-and-vid-for-ipv4 &#124; dst-mac-and-vid-always</em>; <br/>Default:<strong>dst-ip-and-vid-for-ipv4</strong>) | IPv4 組播橋接的查詢模式。<ul class="bullets"><li>dst-mac-and-vid-always - 對於所有封包型別，查詢鍵是目的 MAC 和 VLAN ID。</li><li>dst-ip-and-vid-for-ipv4 - 對於 IPv4 封包，查詢鍵是目的 IP 和 VLAN ID。對於其他封包型別，查詢鍵是目的 MAC 和 VLAN ID。</li></ul> |
| **unicast-fdb-timeout** (*time interval*; Default: **5m**) | Unicast FDB 表項的超時時間。 |
| **override-existing-when-ufdb-full** (*yes \| no*; Default: **no**) | 啟用或停用當 UFDB 已滿時覆蓋具有最低老化值的現有表項。 |

| 屬性 | 描述 |
| :-- | :-- |
| **drop-if-no-vlan-assignment-on-ports**（*埠*；預設：**none**） | 如果未應用基於 MAC、基於協定的 VLAN 分配或入站 VLAN 轉換，則丟棄幀的埠。 |
| **drop-if-invalid-or-src-port- -not-member-of-vlan-on-ports**（*埠*；預設：**none**） | 丟棄無效幀和其他埠 VLAN ID 幀的埠。 |
| **unknown-vlan-lookup-mode**（*ivl \| svl*；預設：**svl**） | 具有無效 VLAN 的封包的查詢和學習模式。 |
| **forward-unknown-vlan**（*yes \| no*；預設：**yes**） | 是否允許轉發不屬於 VLAN 表成員的 VLAN。 |

| 屬性 | 描述 |
| :-- | :-- |
| **bypass-vlan-ingress-filter-for**（*協定*；預設：**none**） | 從入站 VLAN 過濾中排除的協定。如果這些協定具有無效 VLAN，則不會丟棄它們。（arp、dhcpv4、dhcpv6、eapol、igmp、mld、nd、pppoe-discovery、ripv1） |
| **bypass-ingress-port-policing-for**（*協定*；預設：**none**） | 從入站埠監管中排除的協定。（arp、dhcpv4、dhcpv6、eapol、igmp、mld、nd、pppoe-discovery、ripv1） |
| **bypass-l2-security-check-filter-for**（*協定*；預設：**none**） | 從 Policy 規則安全檢查中排除的協定。（arp、dhcpv4、dhcpv6、eapol、igmp、mld、nd、pppoe-discovery、ripv1） |

| 屬性 | 描述 |
| :-- | :-- |
| **ingress-mirror0** (*port \| trunk,format*; Default: **none,modified**) | 第一個入向映象分析埠或 trunk 以及映象格式：<ul class="bullets"><li>analyzer-configured - 封包與發往目的地的封包相同。VLAN 格式根據分析埠的 VLAN 配置進行修改。</li><li>modified - 封包與發往目的地的封包相同。VLAN 格式根據出口埠的 VLAN 配置進行修改。</li><li>original - 流量按原始入向封包格式原樣映象，不做任何更改。但邊緣埠中的服務 VLAN 標籤會被剝離。</li></ul> |
| **ingress-mirror1** (*port \| trunk,format*; Default: **none,modified**) | 第二個入向映象分析埠或 trunk 以及映象格式：<ul class="bullets"><li>analyzer-configured - 封包與發往目的地的封包相同。VLAN 格式根據分析埠的 VLAN 配置進行修改。</li><li>modified - 封包與發往目的地的封包相同。VLAN 格式根據出口埠的 VLAN 配置進行修改。</li><li>original - 流量按原始入向封包格式原樣映象，不做任何更改。但邊緣埠中的服務 VLAN 標籤會被剝離。</li></ul> |
| **ingress-mirror-ratio** (*1/32768..1/1*; Default: **1/1**) | 入向映象封包占所有封包的比例。 |
| **egress-mirror0** (*port \| trunk,format*; Default: **none,modified**) | 第一個出口映象分析埠或 trunk 以及映象格式：<ul class="bullets"><li>analyzer-configured - 封包與發往目的地的封包相同。VLAN 格式根據分析埠的 VLAN 配置進行修改。</li><li>modified - 封包與發往目的地的封包相同。VLAN 格式根據出口埠的 VLAN 配置進行修改。</li><li>original - 流量按原始入向封包格式原樣映象，不做任何更改。但邊緣埠中的服務 VLAN 標籤會被剝離。</li></ul> |
| **egress-mirror1** (*port \| trunk,format*; Default: **none,modified**) | 第二個出口映象分析埠或 trunk 以及映象格式：<ul class="bullets"><li>analyzer-configured - 封包與發往目的地的封包相同。VLAN 格式根據分析埠的 VLAN 配置進行修改。</li><li>modified - 封包與發往目的地的封包相同。VLAN 格式根據出口埠的 VLAN 配置進行修改。</li><li>original - 流量按原始入向封包格式原樣映象，不做任何更改。但邊緣埠中的服務 VLAN 標籤會被剝離。</li></ul> |
| **egress-mirror-ratio** (*1/32768..1/1*; Default: **1/1**) | 出口映象封包占所有封包的比例。 |
| **mirror-egress-if-ingress-mirrored** (*yes \| no*; Default: **no**) | 當封包同時應用入向和出口映象時，如果此設定停用，則僅對該封包執行入向映象。如果啟用此設定，則兩種映象型別都會應用。 |
| **mirror-tx-on-mirror-port** (*yes \| no*; 預設值： **no**) |  |
| **mirrored-packet-qos-priority** (*0..7*; Default: **0**) | 映象封包中重標記的優先順序。 |
| **mirrored-packet-drop-precedence** (*drop \| green \| red \| yellow*; Default: **green**) | 映象封包中重標記的丟棄優先順序。此 QoS 屬性用於映象封包入隊或丟棄。 |
| **fdb-uses** (*mirror0 \| mirror1*; Default: **mirror0**) | 用於基於 FDB 的映象的分析埠。 |
| **vlan-uses** (*mirror0 \| mirror1*; Default: **mirror0**) | 用於基於 VLAN 的映象的分析埠。 |

## 埠設定 {#port-settings}

---

**子選單：** `/interface/ethernet/switch/port`

| 屬性 | 描述 |
| :-- | :-- |
| **vlan-type** (*edge-port \| network-port*; Default: **network-port**) | 埠 VLAN 型別指定 VLAN ID 是否用於 UFDB 學習。network port 在 UFDB 中學習 VLAN ID，edge port 不學習 - VLAN 0。只能在 IVL 學習模式下觀察到。 |
| <strong>isolation-leakage-profile-override</strong> (<em>yes &#124; no</em>; Default: <strong>!isolation-leakage-profile-override</strong>) <br/><strong>isolation-leakage-profile</strong> (<em>0..31</em>;) | 用於埠隔離/洩漏配置的自定義埠配置檔案。<ul class="bullets"><li>埠級隔離配置檔案 0。Uplink 埠 - 允許該埠與裝置中的所有埠通訊。</li><li>埠級隔離配置檔案 1。Isolated 埠 - 僅允許該埠與 uplink 埠通訊。</li><li>埠級隔離配置檔案 2 - 31。Community 埠 - 允許在同一 community 埠和 uplink 埠之間通訊。</li></ul> |
| **learn-override** (*yes \| no*; Default: **!learn-override**) **learn-limit** (*1..1023*; Default: **!learn-limit**) | 啟用或停用 MAC 地址學習並設定埠上的 MAC 限制。當設定 !learn-override 和 !learn-limit 時，MAC 學習限制預設停用。自 RouterOS v6.42 起，屬性 learn-override 在 `/interface/bridge/port` 選單下由 learn 替代。 |
| **drop-when-ufdb-entry-src-drop** (*yes \| no*; Default: **yes**) | 啟用或停用當 UFDB 表項具有 action src-drop 時丟棄封包。 |
| **allow-unicast-loopback** (*yes \| no*; Default: **no**) | 埠上的單播環回。啟用後，對於已知單播封包，當源埠和目的埠相同時允許回送。 |
| **allow-multicast-loopback** (*yes \| no*; Default: **no**) | 埠上的組播環回。啟用後，對於已註冊組播或廣播封包，當源埠和目的埠相同時允許回送。 |
| **action-on-static-station-move** (*copy-to-cpu \| drop \| forward \| redirect-to-cpu*; Default: **forward**) | 當 UFDB 已包含具有相同 MAC 但埠不同的靜態表項時，對封包執行的動作。 |
| **drop-dynamic-mac-move** (*yes \| no*; Default: **no**) | 如果 MAC 已在另一個埠上學習到，則阻止 MAC 重新學習直到 UFDB 超時。 |

| 屬性 | 描述 |
| :-- | :-- |
| **allow-fdb-based-vlan-translate** (*yes \| no*; Default: **no**) | 啟用或停用埠上基於 MAC 的 VLAN 轉換。 |
| <strong>allow-mac-based-service-vlan-assignment-for</strong> (<em>all-frames &#124; none &#124;</em><em>tagged-frame-only &#124; untagged-and-priority-tagged-frame-only</em>; Default: <br/><strong>none</strong>) | 應用基於 MAC 的服務 VLAN 轉換的幀型別。 |
| <strong>allow-mac-based-customer-vlan-assignment-for</strong> (<em>all-frames &#124; none &#124;</em><em>tagged-frame-only &#124; untagged-and-priority-tagged-frame-only</em>; Default: <br/><strong>none</strong>) | 應用基於 MAC 的客戶 VLAN 轉換的幀型別。 |
| **default-customer-pcp** (*0..7*; Default: **0**) | 埠的預設客戶 PCP。 |
| **default-service-pcp** (*0..7*; Default: **0**) | 埠的預設服務 PCP。 |
| **pcp-propagation-for-initial-pcp** (*yes \| no*; Default: **no**) | 啟用或停用入向初始 PCP 分配時的 PCP 傳播。<ul class="bullets"><li>如果埠 vlan-type 為 Edge 埠，則服務 PCP 從客戶 PCP 複製。</li><li>如果埠 vlan-type 為 Network 埠，則客戶 PCP 從服務 PCP 複製。</li></ul> |
| **filter-untagged-frame** (*yes \| no*; Default: **no**) | 是否過濾埠上的未標記幀。 |
| **filter-priority-tagged-frame** (*yes \| no*; Default: **no**) | 是否過濾埠上的帶優先順序標記幀。 |
| **filter-tagged-frame** (*yes \| no*; Default: **no**) | 是否過濾埠上的標記幀。 |

| 屬性 | 描述 |
| :-- | :-- |
| **egress-vlan-tag-table-lookup-key** (*according-to-bridge-type \| egress-vid*; Default: **egress-vid**) | 出口 VLAN 表（VLAN Tagging）查詢：<ul class="bullets"><li>egress-vid - 當配置為 Edge 埠時，查詢 VLAN ID 為 CVID；當配置為 Network 埠時，為 SVID。</li><li>according-to-bridge-type - 當配置為客戶 VLAN bridge 時，查詢 VLAN ID 為 CVID；當配置為服務 VLAN bridge 時，為 SVID。在服務 VLAN bridge 中，Edge 埠的 Customer 標籤保持不變。</li></ul> |
| **egress-vlan-mode** (*tagged \| unmodified \| untagged*; Default: **unmodified**) | 埠上的出口 VLAN 標記動作。 |
| **egress-pcp-propagation** (*yes \| no*; Default: **no**) | 啟用或禁用出口 PCP 傳播。<ul class="bullets"><li>如果埠 vlan-type 為 Edge 埠，則服務 PCP 從客戶 PCP 複製。</li><li>如果埠 vlan-type 為 Network 埠，則客戶 PCP 從服務 PCP 複製。</li></ul> |

| 屬性 | 描述 |
| :-- | :-- |
| **ingress-mirror-to**（*mirror0 \| mirror1 \| none*；預設：**none**） | 用於基於埠的入站映象的分析埠。 |
| **ingress-mirroring-according-to-vlan**（*yes \| no*；預設：**no**） |  |
| **egress-mirror-to**（*mirror0 \| mirror1 \| none*；預設：**none**） | 用於基於埠的出站映象的分析埠。 |

| 屬性 | 描述 |
| :-- | :-- |
| **qos-scheme-precedence** (*da-based \| dscp-based \| ingress-acl-based \| pcp-based \| protocol-based \| sa-based \| vlan-based*; Default: **pcp-based, sa-based, da-based, dscp-based, protocol-based, vlan-based**) | 指定埠入嚮應用的 QoS 分配方案。<ul class="bullets"><li>da-based</li><li>dscp-based</li><li>ingress-acl-based</li><li>pcp-based</li><li>protocol-based</li><li>sa-based</li><li>vlan-based</li></ul> |
| **pcp-or-dscp-based-qos-change-dei** (*yes \| no*; Default: **no**) | 啟用或停用埠上基於 PCP 或 DSCP 的 DEI 更改。 |
| **pcp-or-dscp-based-qos-change-pcp** (*yes \| no*; Default: **no**) | 啟用或停用埠上基於 PCP 或 DSCP 的 PCP 更改。 |
| **pcp-or-dscp-based-qos-change-dscp** (*yes \| no*; Default: **no**) | 啟用或停用埠上基於 PCP 或 DSCP 的 DSCP 更改。 |
| **dscp-based-qos-dscp-to-dscp-mapping** (*yes \| no*; Default: **yes**) | 啟用或停用埠上的 DSCP 到內部 DSCP 對映。 |
| **pcp-based-qos-drop-precedence-mapping** (*PCP/DEI-range:drop-precedence*; Default: **0-15:green**) | 用於 PCP/DEI 到丟棄優先順序（drop、green、red、yellow）對映的新丟棄優先順序值。允許多個對映，用逗號分隔，例如 "0-7:yellow,8-15:red"。 |
| **pcp-based-qos-dscp-mapping** (*PCP/DEI-range:DEI*; Default: **0-15:0**) | 用於 PCP/DEI 到 DSCP（0..63）對映的新 DSCP 值。允許多個對映，用逗號分隔，例如 "0-7:25,8-15:50"。 |
| **pcp-based-qos-dei-mapping** (*PCP/DEI-range:DEI*; Default: **0-15:0**) | 用於 PCP/DEI 到 DEI（0..1）對映的新 DEI 值。允許多個對映，用逗號分隔，例如 "0-7:0,8-15:1"。 |
| **pcp-based-qos-pcp-mapping** (*PCP/DEI-range:DEI*; Default: **0-15:0**) | 用於 PCP/DEI 到 PCP（0..7）對映的新 PCP 值。允許多個對映，用逗號分隔，例如 "0-7:3,8-15:4"。 |
| **pcp-based-qos-priority-mapping** (*PCP/DEI-range:DEI*; Default: **0-15:0**) | 用於 PCP/DEI 到優先順序（0..15）對映的新內部優先順序值。允許多個對映，用逗號分隔，例如 "0-7:5,8-15:15"。 |

| 屬性 | 描述 |
| :-- | :-- |
| **priority-to-queue** (*priority-range:queue*; Default: **0-15:0,1:1,2:2,3:3**) | 每個埠的內部優先順序（0..15）到佇列（0..7）的對映。 |
| <strong>per-queue-scheduling</strong> (<em>Scheduling-type:Weight</em>; Default: <strong>wrr-group0:1,wrr-group0:2,wrr-group0:4,wrr-group0:8,wrr-group0:16,wrr-group0:32,</strong><br/><strong>wrr-group0:64,wrr-group0:128</strong>) | 設定埠對每個佇列組使用嚴格或加權輪詢策略進行流量整形；每個佇列用逗號分隔。 |

| 屬性 | 描述 |
| :-- | :-- |
| <strong>ingress-customer-tpid-override</strong> (<em>yes &#124; no</em>; Default:<strong>!ingress-customer-tpid-override</strong>) <br/><strong>ingress-customer-tpid</strong> (<em>0..10000</em>; Default: <strong>0x8100</strong>) | 入向客戶 TPID 覆蓋允許接受帶有自定義客戶標籤 TPID 的特定幀。預設值用於 802.1Q 幀的標籤。 |
| <strong>egress-customer-tpid-override</strong> (<em>yes &#124; no</em>; Default: <strong>!egress-customer-tpid-override</strong>) <strong>egress-customer-tpid</strong> (<em>0..10000</em>; Default: <br/><strong>0x8100</strong>) | 出口客戶 TPID 覆蓋允許對帶有客戶標籤的出口幀進行自定義標識。預設值用於 802.1Q 幀的標籤。 |
| <strong>ingress-service-tpid-override</strong> (<em>yes &#124; no</em>; Default: <strong>!ingress-service-tpid-override</strong>) <br/><strong>ingress-service-tpid</strong> (<em>0..10000</em>; Default: <strong>0x88A8</strong>) | 入向服務 TPID 覆蓋允許接受帶有自定義服務標籤 TPID 的特定幀。預設值用於 802.1AD 幀的服務標籤。 |
| <strong>egress-service-tpid-override</strong> (<em>yes &#124; no</em>; Default: <strong>!egress-service-tpid-override</strong>) <strong>egress-service-tpid</strong> (<em>0..10000</em>; Default: <br/><strong>0x88A8</strong>) | 出口服務 TPID 覆蓋允許對帶有服務標籤的出口幀進行自定義標識。預設值用於 802.1AD 幀的服務標籤。 |

| 屬性 | 描述 |
| :-- | :-- |
| **custom-drop-counter-includes** (*counters*; Default: **none**) | 自定義包含項，用於為交換器埠 custom-drop-packet 計數器統計丟棄的封包。<ul><li><strong>device-loopback</strong></li><li><strong>fdb-hash-violation</strong></li><li><strong>exceeded-port-learn-limitation</strong></li><li><strong>dynamic-station-move</strong></li><li><strong>static-station-move</strong></li><li><strong>ufdb-source-drop</strong></li><li><strong>host-source-drop</strong></li><li><strong>unknown-host</strong></li><li><strong>ingress-vlan-filtered</strong></li></ul> |
| **queue-custom-drop-counter0-includes** (*counters*; Default: **none**) | 自定義包含項，用於為交換器埠 tx-queue-custom0-drop-packet 和 tx-queue-custom0-drop-byte 計數器統計丟棄的封包和位元組。<br/><ul><li><strong>red</strong></li><li><strong>yellow</strong></li><li><strong>green</strong></li><li><strong>queue0</strong></li><li><strong>...</strong></li><li><strong>queue7</strong></li></ul> |
| **queue-custom-drop-counter1-includes** (*counters*; Default: **none**) | 自定義包含項，用於為交換器埠 tx-queue-custom1-drop-packet 和 tx-queue-custom1-drop-byte 計數器統計丟棄的封包和位元組。<br/><ul><li><strong>red</strong></li><li><strong>yellow</strong></li><li><strong>green</strong></li><li><strong>queue0</strong></li><li><strong>...</strong></li><li><strong>queue7</strong></li></ul> |
| **policy-drop-counter-includes** (*counters*; Default: **none**) | 自定義包含項，用於為交換器埠 policy-drop-packet 計數器統計丟棄的封包。<ul><li><strong>ingress-policing</strong></li><li><strong>ingress-acl</strong></li><li><strong>egress-policing</strong></li><li><strong>egress-acl</strong></li></ul> |

## 轉發表資料庫 {#forwarding-databases}

---

### 單播 FDB {#unicast-fdb}

單播轉發表資料庫最多支援 16K 個 MAC 條目。

**子選單：** `/interface/ethernet/switch/unicast-fdb`

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*action*; Default: **forward**) | UFDB 表項的動作：<ul class="bullets"><li>dst-drop - 當封包的目的 MAC 與表項匹配時丟棄封包。</li><li>dst-redirect-to-cpu - 當封包的目的 MAC 與表項匹配時將封包重定向到 CPU。</li><li>forward - 轉發封包。</li><li>src-and-dst-drop - 當封包的源 MAC 或目的 MAC 與表項匹配時丟棄封包。</li><li>src-and-dst-redirect-to-cpu - 當封包的源 MAC 或目的 MAC 與表項匹配時將封包重定向到 CPU。</li><li>src-drop - 當封包的源 MAC 與表項匹配時丟棄封包。</li><li>src-redirect-to-cpu - 當封包的源 MAC 與表項匹配時將封包重定向到 CPU。</li></ul> |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用 Unicast FDB 表項。 |
| **isolation-profile** (*community1 \| community2 \| isolated \| promiscuous*; Default: **promiscuous**) | MAC 級別隔離配置檔案。 |
| **mac-address** (*MAC address*) | 當目的 MAC 或源 MAC 與表項匹配時，action 命令應用於該封包。 |
| **mirror** (*yes \| no*; Default: **no**) | 啟用或停用基於源 MAC 或目的 MAC 的映象。 |
| **port** (*port*) | Unicast FDB 表項的匹配埠。 |
| **qos-group** (*none*; Default: **none**) | 從 QoS group 選單定義的 QoS 組。 |
| **svl** (*yes \| no*; Default: **no**) | Unicast FDB 學習模式：<ul class="bullets"><li>Shared VLAN Learning (svl) - 學習/查詢基於 MAC 地址 - 而不是 VLAN ID。</li><li>Independent VLAN Learning (ivl) - 學習/查詢同時基於 MAC 地址和 VLAN ID。</li></ul> |
| **vlan-id** (*0..4095*) | Unicast FDB 查詢/學習 VLAN ID。 |

### 組播 FDB {#multicast-fdb}

CRS125 交換晶片在 MFDB 中最多支援 1024 個條目用於組播轉發。對於每個組播封包，在 MFDB 中執行目標 MAC 或目標 IP 查詢。MFDB 條目不會自動學習，只能配置。

**子選單：** `/interface/ethernet/switch/multicast-fdb`

| 屬性 | 描述 |
| :-- | :-- |
| **address** (*X.X.X.X \| XX:XX:XX:XX:XX:XX*) | 組播封包的匹配 IP 地址或 MAC 地址。 |
| **bypass-vlan-filter** (*yes \| no*; Default: **no**) | 允許匹配的組播封包繞過 VLAN 過濾。 |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用 Multicast FDB 表項。 |
| **ports** (*ports*) | 組播流量的成員埠。 |
| **qos-group** (*none*; Default: **none**) | 從 QoS group 選單定義的 QoS 組。 |
| **svl** (*yes \| no*; Default: **no**) | Multicast FDB 學習模式：<ul class="bullets"><li>Shared VLAN Learning (svl) - 學習/查詢基於 MAC 地址 - 而不是 VLAN ID。</li><li>Independent VLAN Learning (ivl) - 學習/查詢同時基於 MAC 地址和 VLAN ID。</li></ul> |
| **vlan-id** (*0..4095*; Default: **0**) | Multicast FDB 查詢 VLAN ID。如果 VLAN 學習模式為 IVL，則 VLAN ID 為查詢 ID，否則 VLAN ID = 0。 |

### 保留 FDB {#reserved-fdb}

Cloud Router Switch 支援 256 個 RFDB 條目。每個 RFDB 條目可以儲存具有特定命令的二層單播或組播 MAC 地址。

**子選單：** `/interface/ethernet/switch/reserved-fdb`

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*copy-to-cpu \| drop \| forward \| redirect-to-cpu*; Default: **forward**) | RFDB 表項的動作：<ul class="bullets"><li>copy-to-cpu - 當封包的目的 MAC 與表項匹配時，將封包複製到 CPU。</li><li>drop - 當封包的目的 MAC 與表項匹配時丟棄封包。</li><li>forward - 當封包的目的 MAC 與表項匹配時轉發封包。</li><li>redirect-to-cpu - 當封包的目的 MAC 與表項匹配時將封包重定向到 CPU。</li></ul> |
| **bypass-ingress-port-policing** (*yes \| no*; Default: **no**) | 允許匹配的封包繞過入口埠 Policer。 |
| **bypass-ingress-vlan-filter** (*yes \| no*; Default: **no**) | 允許匹配的封包繞過 VLAN 過濾。 |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用 Reserved FDB 表項。 |
| **mac-address** (*MAC address*; Default: **00:00:00:00:00:00**) | Reserved FDB 表項的匹配 MAC 地址。 |
| **qos-group** (*none*; Default: **none**) | 從 QoS group 選單定義的 QoS 組。 |

## VLAN {#vlan}

---

### VLAN 表 {#vlan-table}

VLAN 表支援 4096 個 VLAN 條目，用於儲存 VLAN 成員資訊以及其他 VLAN 資訊，例如 QoS、隔離、強制 VLAN、學習和映象。

**子選單：** `/interface/ethernet/switch/vlan`

| 屬性 | 描述 |
| :-- | :-- |
| **disabled** (*yes \| no*; Default: **no**) | 指示 VLAN 表項是否停用。只有啟用的表項才會應用於查詢過程和轉發決策。 |
| **flood** (*yes \| no*; Default: **no**) | 啟用或停用按 VLAN 強制泛洪。如果啟用該功能，則忽略 UFDB 或 MFDB 中的目的 MAC 查詢結果，<br/>並且強制封包在 VLAN 中泛洪。 |
| **ingress-mirror** (*yes \| no*; Default: **no**) | 啟用按 VLAN 的入向映象，以支援基於 VLAN 的映象功能。 |
| **learn** (*yes \| no*; Default: **yes**) | 啟用或停用 VLAN 的源 MAC 學習。 |
| **ports** (*ports*) | VLAN 的成員埠。 |
| **qos-group** (*none*; Default: **none**) | 從 QoS group 選單定義的 QoS 組。 |
| **svl** (*yes \| no*; Default: **no**) | 用於在 UFDB 和 MFDB 中查詢的 FDB 查詢模式。<ul class="bullets"><li>Shared VLAN Learning (svl) - 學習/查詢基於 MAC 地址 - 而不是 VLAN ID。</li><li>Independent VLAN Learning (ivl) - 學習/查詢同時基於 MAC 地址和 VLAN ID。</li></ul> |
| **vlan-id** (*0..4095*) | VLAN 成員表項的 VLAN ID。 |

### 出站 VLAN 標籤 {#egress-vlan-tag}

出站封包可以被分配不同的 VLAN 標籤格式。當封包傳送到出站埠（目標埠）時，VLAN 標籤可以被移除、新增或保持原樣。每個埠對出站 VLAN 標籤格式有專用控制。標籤格式包括：

- 未標記
- 已標記
- 未修改

出站 VLAN 標籤表包含 4096 個條目，用於選擇 VLAN 標記。

**子選單：** `/interface/ethernet/switch/egress-vlan-tag`

| 屬性 | 描述 |
| :-- | :-- |
| **disabled**（*yes \| no*；預設：**no**） | 啟用或禁用出站 VLAN 標籤表條目。 |
| **tagged-ports**（*埠*） | 在出站中標記的埠。 |
| **vlan-id**（*0..4095*） | 在出站中標記的 VLAN ID。 |

### 入站/出站 VLAN 轉換 {#ingressegress-vlan-translation}

入站 VLAN 轉換表允許每個埠最多 15 個條目。可以從封包頭中選擇一個或多個欄位，以便在入站 VLAN 轉換表中查詢。第一個匹配條目中配置的 S-VLAN 或 C-VLAN 或兩者都會分配給該封包。

**子選單：** `/interface/ethernet/switch/ingress-vlan-translation, /interface/ethernet/switch/egress-vlan-translation`

| 屬性 | 描述 |
| :-- | :-- |
| **customer-dei** (*0..1*; Default: **none**) | 客戶標籤的匹配 DEI。 |
| **customer-pcp** (*0..7*; Default: **none**) | 客戶標籤的匹配 PCP。 |
| **customer-vid** (*0..4095*; Default: **none**) | 匹配客戶標籤的 VLAN ID。 |
| **customer-vlan-format** (*any \| priority-tagged-or-tagged \| tagged \| untagged-or-tagged*; Default:**any**) | VLAN 轉換規則有效的帶客戶標籤幀型別。 |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用 VLAN 轉換表項。 |
| **new-customer-vid** (*0..4095*; Default: **none**) | 新的客戶 VLAN ID 替換匹配的客戶 VLAN ID。如果設定為 4095 且使用入向 VLAN 轉換，則流量被丟棄。 |
| **new-service-vid** (*0..4095*; Default: **none**) | 新的服務 VLAN ID 替換匹配的服務 VLAN ID。 |
| **pcp-propagation** (*yes \| no*; Default: **no**) | 啟用或停用 PCP 傳播。<ul class="bullets"><li>如果埠型別為 Edge，則客戶 PCP 從服務 PCP 複製。</li><li>如果埠型別為 Network，則服務 PCP 從客戶 PCP 複製。</li></ul> |
| **ports** (*ports*) | VLAN 轉換規則的匹配交換器埠。 |
| **protocol** (*protocols*; Default: **none**) | 匹配乙太網協定。*(僅用於入向 VLAN 轉換)* |
| **sa-learning** (*yes \| no*; Default: **no**) | 啟用或停用 VLAN 轉換後的源 MAC 學習。*(僅用於入向 VLAN 轉換)* |
| **service-dei** (*0..1*; Default: **none**) | 服務標籤的匹配 DEI。 |
| **service-pcp** (*0..7*; Default: **none**) | 服務標籤的匹配 PCP。 |
| **service-vid** (*0..4095*; Default: **none**) | 匹配服務標籤的 VLAN ID。 |
| **service-vlan-format** (*any \| priority-tagged-or-tagged \| tagged \| untagged-or-tagged*; Default:**any**) | VLAN 轉換規則有效的帶服務標籤幀型別。 |

下表列出了會觸發具有特定 VLAN 格式設定的規則的流量；請注意，帶 VLAN ID 0 標記的流量是一種特殊情況，也會被考慮在內。

| 屬性 | 描述 |
| :-- | :-- |
| **any** | 接受：<ul><li>未標記流量</li><li>標記流量</li><li>設定了優先順序的標記流量</li><li>VLAN 0 流量</li><li>設定了優先順序的 VLAN 0 流量</li></ul> |
| **priority-tagged-or-tagged** | 接受：<ul><li>標記流量</li><li>設定了優先順序的標記流量</li><li>VLAN 0 流量</li><li>設定了優先順序的 VLAN 0 流量</li></ul> |
| **tagged** | 接受：<ul><li>標記流量</li><li>設定了優先順序的標記流量</li></ul> |
| **untagged-or-tagged** | 接受：<ul><li>未標記流量</li><li>標記流量</li><li>設定了優先順序的標記流量</li></ul> |

:::danger
如果 `VLAN-format` 設定為 `any`，那麼將 `customer-vid``/``service-vid` 設定為 `0` 會觸發針對 VLAN 0 流量的交換器規則。在這種情況下，交換器規則會查詢未標記流量或帶有 VLAN 0 標籤的流量，只有 `untagged-or-tagged` 會過濾掉 VLAN 0 流量。
:::

### 基於協定的 VLAN {#protocol-based-vlan}

基於協定的 VLAN 表用於按埠為相關協定封包分配 VID 和 QoS 屬性。

**子選單：** `/interface/ethernet/switch/protocol-based-vlan`

| 屬性 | 描述 |
| :-- | :-- |
| **disabled**（*yes \| no*；預設：**no**） | 啟用或停用基於協定的 VLAN 條目。 |
| **frame-type**（*ethernet \| llc \| rfc-1042*；預設：**ethernet**） | 匹配幀的封裝型別。 |
| **new-customer-vid**（*0..4095*；預設：**0**） | 新的客戶 VLAN ID 替換指定協定的原始客戶 VLAN ID。如果設定為 4095，則丟棄流量。 |
| **new-service-vid**（*0..4095*；預設：**0**） | 新的服務 VLAN ID 替換指定協定的原始服務 VLAN ID。 |
| **ports**（*埠*） | 基於協定的 VLAN 規則的匹配交換器埠。 |
| **protocol**（*協定*；預設：**0**） | 基於協定的 VLAN 規則的匹配協定。 |
| **qos-group**（*none*；預設：**none**） | 從 QoS 組選單定義的 QoS 組。 |
| **set-customer-vid-for**（*all \| none \| tagged \| untagged-or-priority-tagged*；預設：**all**） | 針對不同封包型別的客戶 VLAN ID 分配命令。 |
| **set-qos-for**（*all \| none \| tagged \| untagged-or-priority-tagged*；預設：**none**） | 應用 QoS 分配命令的幀型別。 |
| **set-service-vid-for**（*all \| none \| tagged \| untagged-or-priority-tagged*；預設：**all**） | 針對不同封包型別的服務 VLAN ID 分配命令。 |

### 基於 MAC 的 VLAN {#mac-based-vlan}

基於 MAC 的 VLAN 表用於根據源 MAC 分配 VLAN。

**子選單：** `/interface/ethernet/switch/mac-based-vlan`

| 屬性 | 描述 |
| :-- | :-- |
| **disabled**（*yes \| no*；預設：**no**） | 啟用或停用基於 MAC 的 VLAN 條目。 |
| **new-customer-vid**（*0..4095*；預設：**0**） | 新的客戶 VLAN ID 替換匹配封包的原始服務 VLAN ID。如果設定為 4095，則丟棄流量。 |
| **new-service-vid**（*0..4095*；預設：**0**） | 新的服務 VLAN ID 替換匹配封包的原始服務 VLAN ID。 |
| **src-mac-address**（*MAC 地址*） | 基於 MAC 的 VLAN 規則的匹配源 MAC 地址。 |

:::warning
所有 CRS1xx/2xx 系列交換器最多支援 1024 條基於 MAC 的 VLAN 表項。
:::

### 1:1 VLAN 交換 {#11-vlan-switching}

1:1 VLAN 交換可用於替換匹配封包的常規 L2 橋接。當封包命中 1:1 VLAN 交換表條目時，該條目中的目標埠資訊會分配給該封包。UFDB 和 MFDB 條目中匹配的目標資訊不再適用於該封包。

**子選單：** `/interface/ethernet/switch/one2one-vlan-switching`

| 屬性 | 描述 |
| :-- | :-- |
| **customer-vid**（*0..4095*；預設：**0**） | 用於 1:1 VLAN 交換的匹配客戶 VLAN ID。 |
| **disabled**（*yes \| no*；預設：**no**） | 啟用或停用 1:1 VLAN 交換表條目。 |
| **dst-port**（*埠*） | 匹配的 1:1 VLAN 交換封包的目標埠。 |
| **service-vid**（*0..4095*；預設：**0**） | 用於 1:1 VLAN 交換的匹配客戶 VLAN ID。 |

## 埠隔離/洩漏 {#port-isolationleakage}

---

CRS 交換器支援靈活的多級隔離功能，可用於使用者訪問控制、流量工程以及高階安全和網路管理。隔離功能提供有組織的結構，使使用者可以輕鬆地按埠、MAC 地址、VLAN、協定、流和幀型別程式設計和控制訪問。支援以下隔離和洩漏功能：

- 埠級隔離
- MAC 級隔離
- VLAN 級隔離
- 協定級隔離
- 流級隔離
- 上述功能的自由組合

埠級隔離在源埠和目標埠上支援不同的控制方案。每個條目可以為源埠或目標埠程式設計訪問控制。

- 當條目配置為源埠訪問控制時，該條目會。

應用於入站封包。

- 當條目配置為目的地埠訪問控制時，該條目

應用於出站封包。

埠洩漏允許繞過埠上的出站 VLAN 過濾。允許洩漏埠訪問其他埠，用於安全、網路控制和管理等各種應用。注意：當同一埠同時應用隔離和洩漏時，該埠被隔離。

**子選單：** `/interface/ethernet/switch/port-isolation`

**子選單：** `/interface/ethernet/switch/port-leakage`

| 屬性 | 描述 |
| :-- | :-- |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用埠隔離/洩漏表項。 |
| **flow-id** (*0..63*; 預設值： **none**) |  |
| **forwarding-type** (*bridged; routed*; Default: **bridged,routed**) | Cloud Router Switch 上的匹配流量轉發型別。 |
| **mac-profile** (*community1 \| community2 \| isolated \| promiscuous*; Default: **none**) | 匹配的 MAC 隔離/洩漏配置檔案。 |
| **port-profile** (*0..31*; Default: **none**) | 匹配的埠隔離/洩漏配置檔案。 |
| **ports** (*ports*; Default: **none**) | 隔離/洩漏埠。 |
| **protocol-type** (*arp; nd; dhcpv4; dhcpv6; ripv1*; Default: **arp,nd,dhcpv4,dhcpv6,ripv1**) | 隔離/洩漏包含的協定。 |
| **registration-status** (*known; unknown*; Default: **known,unknown**) | 匹配封包的註冊狀態。Known 表項存在於 UFDB 和 MFDB 中，unknown 表項不存在。 |
| **traffic-type** (*unicast; multicast; broadcast*; Default: **unicast,multicast,broadcast**) | 匹配流量型別。 |
| **type** (*dst \| src*; Default: **src**) | 隔離/洩漏表項的查詢型別：<ul class="bullets"><li>src - 表項應用於埠的入向封包。</li><li>dst - 表項應用於埠的出口封包。</li></ul> |
| **vlan-profile** (*community1 \| community2 \| isolated \| promiscuous*; Default: **none**) | 匹配的 VLAN 隔離/洩漏配置檔案。 |

## 幹道（Trunking） {#trunking}

---

Cloud Router Switch 中的 Trunking 提供具有硬體自動故障轉移和負載均衡的靜態鏈路聚合組。不支援 IEEE802.3ad 和 IEEE802.1ax 相容的鏈路聚合控制協定。最多支援 8 個 Trunk 組，每個 Trunk 組最多 8 個 Trunk 成員埠。CRS 埠 Trunking 根據以下所有引數計算 transmit-hash：L2 src-dst MAC + L3 src-dst IP + L4 src-dst Port。

**子選單：** `/interface/ethernet/switch/trunk`

| 屬性 | 描述 |
| :-- | :-- |
| **disabled**（*yes \| no*；預設：**no**） | 啟用或停用埠 trunking 條目。 |
| **member-ports**（*埠*） | Trunk 組的成員埠。 |
| **name**（*字串值*；預設：**trunkX**） | Trunk 組的名稱。 |

## 服務質量 {#quality-of-service}

---

### 整形器 {#shaper}

流量整形限制從介面傳輸的流的速率和突發大小。整形器透過令牌桶實現。如果封包超過最大速率或突發大小，這意味著沒有足夠的封包令牌，則該封包會儲存在緩衝區中，直到有足夠的令牌傳輸它。

**子選單：** `/interface/ethernet/switch/shaper`

| 屬性 | 描述 |
| :-- | :-- |
| **burst** (*integer*; Default: **100k**) | 允許突發期間可傳輸的最大資料速率。 |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用流量整形器表項。 |
| **meter-unit** (*bit \| packet*; Default: **bit**) | 流量整形器速率的測量單位。 |
| **port** (*port*) | 流量整形器的物理埠。 |
| **rate** (*integer*; Default: **1M**) | 最大資料速率限制。 |
| **target** (*port \| queueX \| wrr-groupX*; Default: **port**) | 每個埠（包括 CPU 埠）支援三級整形器：<ul class="bullets"><li>Port level - 表項應用於交換器晶片的埠。</li><li>WRR group level - 表項應用於埠上的 2 個加權輪詢佇列組之一（wrr-group0、wrr-group1）。</li><li>Queue level - 表項應用於埠上的 8 個佇列之一（queue0 - queue7）。</li></ul> |

### 入站埠監管器 {#ingress-port-policer}

**子選單：** `/interface/ethernet/switch/ingress-port-policer`

| 屬性 | 描述 |
| :-- | :-- |
| **burst** (*integer*; Default: **100k**) | 允許突發期間可傳輸的最大資料速率。 |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用入口埠 policer 表項。 |
| **meter-len** (*layer-1 \| layer-2 \| layer-3*; Default: **layer-1**) | 設定用於計量的封包位元組長度的封包分類。<ul class="bullets"><li>layer-1 - 包括整個二層幀 + FCS + 包間間隔 + 前導碼。</li><li>layer-2 - 包括二層幀 + FCS。</li><li>layer-3 - 僅包括三層 + 乙太網填充，不包括二層頭和 FCS。</li></ul> |
| **meter-unit** (*bit \| packet*; Default: **bit**) | 流量入口埠 policer 速率的測量單位。 |
| **new-dei-for-yellow** (*0..1 \| remap*; Default: **none**) | 如果 yellow-action 為 remark，則為超限流量重標記的 DEI。 |
| **new-dscp-for-yellow** (*0..63 \| remap*; Default: **none**) | 如果 yellow-action 為 remark，則為超限流量重標記的 DSCP。 |
| **new-pcp-for-yellow** (*0..7 \| remap*; Default: **none**) | 如果 yellow-action 為 remark，則為超限流量重標記的 PCP。 |
| **packet-types** (*packet-types*; Default: **all types from the description**) | 入口埠 policer 表項有效的匹配封包型別。 |
| **port** (*port*) | 入口埠 policer 表項的物理埠或 trunk。 |
| **rate** (*integer*) | 最大資料速率限制。 |
| **yellow-action** (*drop \| forward \| remark*; Default: **drop**) | 對超限流量執行的動作。 |

### QoS 組 {#qos-group}

全域性 QoS 組表用於基於 VLAN、基於協定和基於 MAC 的 QoS 組分配配置。

**子選單：** `/interface/ethernet/switch/qos-group`

| 屬性 | 描述 |
| :-- | :-- |
| **dei**（*0..1*；預設：**none**） | QoS 組的新 DEI 值。 |
| **disabled**（*yes \| no*；預設：**no**） | 啟用或停用協定 QoS 組條目。 |
| **drop-precedence**（*drop \| green \| red \| yellow*；預設：**green**） | 丟棄優先順序是一種內部 QoS 屬性，用於封包入隊或丟棄。 |
| **dscp**（*0..63*；預設：**none**） | QoS 組的新 DSCP 值。 |
| **name**（*字串值*；預設：**groupX**） | QoS 組的名稱。 |
| **pcp**（*0..7*；預設：**none**） | QoS 組的新 PCP 值。 |
| **priority**（*0..15*；預設：**0**） | 內部優先順序具有本地意義，用於將流量分類到埠上的不同出站佇列。（1 為最高，15 為最低） |

### DSCP QoS 對映 {#dscp-qos-map}

全域性 DSCP 到 QoS 對映表用於將封包的 DSCP 對映到表中配置的新 QoS 屬性。

**子選單：** `/interface/ethernet/switch/dscp-qos-map`

| 屬性 | 描述 |
| :-- | :-- |
| **dei**（*0..1*） | DSCP 到 QoS 對映條目的新 DEI 值。 |
| **drop-precedence**（*drop \| green \| red \| yellow*） | DSCP 到 QoS 對映條目的新丟棄優先順序值。 |
| **pcp**（*0..7*） | DSCP 到 QoS 對映條目的新 PCP 值。 |
| **priority**（*0..15*） | DSCP 到 QoS 對映條目的新內部優先順序值。 |

### DSCP 到 DSCP 對映 {#dscp-to-dscp-map}

全域性 DSCP 到 DSCP 對映表用於將封包的原始 DSCP 對映到表中配置的新 DSCP 值。

**子選單：** `/interface/ethernet/switch/dscp-to-dscp`

| 屬性 | 描述 |
| :-- | :-- |
| **new-dscp**（*0..63*） | DSCP 到 DSCP 對映條目的新 DSCP 值。 |

### 監管器 QoS 對映 {#policer-qos-map}

**子選單：** `/interface/ethernet/switch/policer-qos-map`

| 屬性 | 描述 |
| :-- | :-- |
| **dei-for-red**（*0..1*；預設：**0**） | 紅色封包的監管器 DEI 重對映值。 |
| **dei-for-yellow**（*0..1*；預設：**0**） | 黃色封包的監管器 DEI 重對映值。 |
| **dscp-for-red**（*0..63*；預設：**0**） | 紅色封包的監管器 DSCP 重對映值。 |
| **dscp-for-yellow**（*0..63*；預設：**0**） | 黃色封包的監管器 DSCP 重對映值。 |
| **pcp-for-red**（*0..7*；預設：**0**） | 紅色封包的監管器 PCP 重對映值。 |
| **pcp-for-yellow**（*0..7*；預設：**0**） | 黃色封包的監管器 PCP 重對映值。 |

## 訪問控制列表 {#access-control-list}

---

訪問控制列表由入站策略和出站策略引擎組成，最多允許配置 128 條策略規則（受 RouterOS 限制）。它是一種高階工具，可基於二層、三層和四層協定頭欄位條件進行線速封包過濾、轉發、整形和修改。

:::info
有關支援訪問控制列表的 Cloud Router Switch 裝置，請參閱摘要部分。
:::

:::danger
由於硬體限制，無法在特定埠上匹配廣播/組播流量。您應使用埠隔離、在入站埠上丟棄流量，或使用 VLAN 過濾來防止某些廣播/組播流量被轉發。
:::

**子選單：** `/interface/ethernet/switch/acl`

### 針對封包 MAC 相關欄位的 ACL 條件部分 {#acl-condition-part-for-mac-related-fields-of-packets}

| 屬性 | 描述 |
| :-- | :-- |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用 ACL 表項。 |
| **table** (*egress \| ingress*; Default: **ingress**) | 為入向或出向封包選擇策略表。 |
| **invert-match** (*yes \| no*; Default: **no**) | 反轉整個 ACL 規則匹配。 |
| **src-ports** (*ports,trunks*) | 匹配的物理源埠或 trunk。 |
| **dst-ports** (*ports,trunks*) | 匹配的物理目的埠或 trunk。由於硬體限制，無法在出口埠匹配廣播/組播流量。 |
| **mac-src-address** (*MAC address/Mask*) | 源 MAC 地址和掩碼。 |
| **mac-dst-address** (*MAC address/Mask*) | 目的 MAC 地址和掩碼。 |
| **dst-addr-registered** (*yes \| no*) | 定義是否匹配處於已註冊狀態的封包 - 其目的 MAC 地址位於 UFDB/MFDB/RFDB 中的封包。僅在出口表中有效。 |
| **mac-protocol** (*802.2 \| arp \| homeplug-av \| ip \| ip-or-ipv6 \| ipv6 \| ipx \| lldp \| loop-protect \| mpls-multicast \| mpls-unicast \| mvrp \| non-ip \| packing-compr \| packing-simple \| pppoe \| pppoe-discovery \| rarp \| service-vlan \| vlan or integer: 0..65535 decimal format or 0x0000-0xffff hex format*) | 乙太網負載型別（MAC 層協定）<ul><li><strong>802.2</strong> - 802.2 幀 (0x0004)</li><li><strong>arp</strong> - 地址解析協定 (0x0806)</li><li><strong>capsman</strong> - CAPsMAN 到 CAP 的 MAC 層連線 (0x88BB)</li><li><strong>dot1x</strong> - EAPoL IEEE 802.1X (0x888E)</li><li><strong>homeplug-av</strong> - HomePlug AV MME (0x88E1)</li><li><strong>ip</strong> - 網際網路協定版本 4 (0x0800)</li><li><strong>ip-or-ipv6</strong> - IPv4 或 IPv6 (0x0800 或 0x86DD)</li><li><strong>ipv6</strong> - 網際網路協定版本 6 (0x86DD)</li><li><strong>ipx</strong> - 網際網路分組交換 (0x8137)</li><li><strong>lacp</strong> - 鏈路聚合控制協定 (0x8809)</li><li><strong>lldp</strong> - 鏈路層發現協定 (0x88CC)</li><li><strong>loop-protect</strong> - Loop Protect 協定 (0x9003)</li><li><strong>macsec</strong> - MAC 安全 IEEE 802.1AE (0x88E5)</li><li><strong>mpls-multicast</strong> - MPLS 組播 (0x8848)</li><li><strong>mpls-unicast</strong> - MPLS 單播 (0x8847)</li><li><strong>mvrp</strong> - 多 VLAN 註冊協定 (0x88F5)</li><li><strong>non-ip</strong> - 非網際網路協定版本 4（不是 0x0800）</li><li><strong>packing-compr</strong> - 使用壓縮 [IP 打包](../system-information-and-utilities/ip-packing.md) 的封裝封包 (0x9001)</li><li><strong>packing-simple</strong> - 使用簡單 [IP 打包](../system-information-and-utilities/ip-packing.md) 的封裝封包 (0x9000)</li><li><strong>pppoe</strong> - PPPoE 會話階段 (0x8864)</li><li><strong>pppoe-discovery</strong> - PPPoE 發現階段 (0x8863)</li><li><strong>rarp</strong> - 反向地址解析協定 (0x8035)</li><li><strong>romon</strong> - Router Management Overlay Network RoMON (0x88BF)</li><li><strong>service-vlan</strong> - 提供商橋接 (IEEE 802.1ad) &amp; 最短路徑橋接 IEEE 802.1aq (0x88A8)</li><li><strong>vlan</strong> - VLAN 標記幀 (IEEE 802.1Q) 和具有 NNI 相容性的最短路徑橋接 IEEE 802.1aq (0x8100)</li></ul> |
| **drop-precedence** (*drop \| green \| red \| yellow*) | 匹配內部丟棄優先順序。僅在出口表中有效。 |
| **custom-fields** |  |

### 針對封包 VLAN 相關欄位的 ACL 條件部分 {#acl-condition-part-for-vlan-related-fields-of-packets}

| 屬性 | 描述 |
| :-- | :-- |
| **lookup-vid**（*0..4095*） | 查詢中使用的 VLAN ID。它可以在到達出站表之前更改。 |
| **service-vid**（*0-4095*） | 匹配服務 VLAN ID。 |
| **service-pcp**（*0..7*） | 匹配服務 PCP。 |
| **service-dei**（*0..1*） | 匹配服務 DEI。 |
| **service-tag**（*priority-tagged \| tagged \| tagged-or-priority-tagged \| untagged*） | 服務標籤的格式。 |
| **customer-vid**（*0-4095*） | 匹配客戶 VLAN ID。 |
| **customer-pcp**（*0..7*） | 匹配客戶 PCP。 |
| **customer-dei**（*0..1*） | 匹配客戶 DEI。 |
| **customer-tag**（*priority-tagged \| tagged \| tagged-or-priority-tagged \| untagged*） | 客戶標籤的格式。 |
| **priority**（*0..15*） | 匹配內部優先順序。僅在出站表中有效。 |

### 針對封包 IPv4 和 IPv6 相關欄位的 ACL 條件部分 {#acl-condition-part-for-ipv4-and-ipv6-related-fields-of-packets}

| 屬性 | 描述 |
| :-- | :-- |
| **ip-src**（*IPv4/0..32*） | 匹配源 IPv4 地址。 |
| **ip-dst**（*IPv4/0..32*） | 匹配目標 IPv4 地址。 |
| **ip-protocol**（*tcp \| udp \| udp-lite \| other*） | IP 協定型別。 |
| **src-l3-port**（*0-65535*） | 匹配三層源埠。 |
| **dst-l3-port**（*0-65535*） | 匹配三層目標埠。 |
| **ttl**（*0 \| 1 \| max \| other*） | 匹配封包的 TTL 欄位。 |
| **dscp**（*0..63*） | 匹配封包的 DSCP 欄位。 |
| **ecn**（*0..3*） | 匹配封包的 ECN 欄位。 |
| **fragmented**（*yes \| no*） | 是否匹配分片封包。 |
| **first-fragment**（*yes \| no*） | YES 匹配未分片和第一個分片，NO 匹配其他分片。 |
| **ipv6-src**（*IPv6/0..128*） | 匹配源 IPv6 地址。 |
| **ipv6-dst**（*IPv6/0..128*） | 匹配目標 IPv6 地址。 |
| **mac-isolation-profile**（*community1 \| community2 \| isolated \| promiscuous*） | 基於 UFDB 匹配隔離配置檔案。僅在出站策略表中有效。 |
| **src-mac-addr-state**（*dynamic-station-move \| sa-found \| sa-not-found \| static-station-move*） | 定義是否匹配具有註冊狀態的封包 - 其目標 MAC 地址在 UFDB/MFDB/RFDB 中的封包。僅在出站策略表中有效。 |
| **flow-id**（*0..63*） |  |

### ACL 規則操作部分 {#acl-rule-action-part}

| 屬性 | 描述 |
| :-- | :-- |
| <strong>action</strong> (<em>copy-to-cpu &#124; drop &#124; forward &#124;</em><em>redirect-to-cpu &#124; send-to-new-dst-ports</em>; Default: <br/><strong>forward</strong>) | <ul class="bullets"><li>copy-to-cpu - 如果封包匹配 ACL 條件，則複製到 CPU。</li><li>drop - 如果封包匹配 ACL 條件，則丟棄。</li><li>forward - 如果封包匹配 ACL 條件，則轉發。</li><li>redirect-to-cpu - 如果封包匹配 ACL 條件，則重定向到 CPU。</li><li>send-to-new-dst-ports - 如果封包匹配 ACL 條件，則傳送到新的目的埠。</li></ul> |
| **new-dst-ports** (*ports,trunks*) | 如果動作為 "send-to-new-dst-ports"，則此屬性設定哪些埠/trunk 是新的目的地。 |
| **mirror-to** (*mirror0 \| mirror1*) | ACL 封包的映象目的地。 |
| **policer** (*policer*) | 為 ACL 封包應用的 ACL Policer。 |
| **src-mac-learn** (*yes \| no*) | 是否學習匹配 ACL 封包的源 MAC。僅在入向策略表中有效。 |
| **new-service-vid** (*0..4095*) | ACL 封包的新服務 VLAN ID。 |
| **new-service-pcp** (*0..7*) | ACL 封包的新服務 PCP。 |
| **new-service-dei** (*0..1*) | ACL 封包的新服務 DEI。 |
| **new-customer-vid** (*0..4095*) | ACL 封包的新客戶 VLAN ID。如果設定為 4095，則流量被丟棄。 |
| **new-customer-pcp** (*0..7*) | ACL 封包的新客戶 PCP。 |
| **new-customer-dei** (*0..1*) | ACL 封包的新客戶 DEI。 |
| **new-dscp** (*0..63*) | ACL 封包的新 DSCP。 |
| **new-priority** (*0..15*) | ACL 封包的新內部優先順序。 |
| **new-drop-precedence** (*drop \| green \| red \| yellow*) | ACL 封包的新內部丟棄優先順序。 |
| **new-registered-state** (*yes \| no*) | 是否修改封包狀態。YES 將封包狀態設定為已註冊，NO - 未註冊。僅在入向策略表中有效。 |
| **new-flow-id** (*0..63*) |  |

### ACL 封包過濾繞過部分 {#filter-bypassing-part-for-acl-packets}

| 屬性 | 描述 |
| :-- | :-- |
| **attack-filter-bypass**（*yes \| no*；預設：**no**） |  |
| **ingress-vlan-filter-bypass**（*yes \| no*；預設：**no**） | 允許匹配的封包繞過 VLAN 表中的入站 VLAN 過濾。這僅適用於入站策略表。 |
| **egress-vlan-filter-bypass**（*yes \| no*；預設：**no**） | 允許匹配的封包繞過 VLAN 表中的出站 VLAN 過濾。這僅適用於入站策略表。 |
| **isolation-filter-bypass**（*yes \| no*；預設：**no**） | 允許匹配的封包繞過隔離表。這僅適用於入站策略表。 |
| **egress-vlan-translate-bypass**（*yes \| no*；預設：**no**） | 允許匹配的封包繞過出站 VLAN 轉換表。 |

### ACL 監管器 {#acl-policer}

**子選單：** `/interface/ethernet/switch/acl/policer`

| 屬性 | 描述 |
| :-- | :-- |
| **name** (*string*; Default: **policerX**) | ACL 中使用的 Policer 名稱。 |
| **yellow-rate** (*integer*) | 具有黃色丟棄優先順序的封包的最大資料速率限制。 |
| **yellow-burst** (*integer*; Default: **0**) | 具有黃色丟棄優先順序的封包在允許突發期間可傳輸的最大資料速率。 |
| **red-rate** (*integer*; Default: **0**) | 具有紅色丟棄優先順序的封包的最大資料速率限制。 |
| **red-burst** (*integer*; Default: **0**) | 具有紅色丟棄優先順序的封包在允許突發期間可傳輸的最大資料速率。 |
| **meter-unit** (*bit \| packet*; Default: **bit**) | ACL 流量速率的測量單位。 |
| **meter-len** (*layer-1 \| layer-2 \| layer-3*; Default: **layer-1**) | 設定用於計量的封包位元組長度的封包分類。<ul class="bullets"><li>layer-1 - 包括整個二層幀 + FCS + 包間間隔 + 前導碼。</li><li>layer-2 - 包括二層幀 + FCS。</li><li>layer-3 - 僅包括三層 + 乙太網填充，不包括二層頭和 FCS。</li></ul> |
| **color-awareness** (*yes \| no*; Default: **no**) | YES 使 policer 考慮預先著色的丟棄優先順序，NO - 忽略丟棄優先順序。 |
| **bucket-coupling** (*yes \| no*; 預設值： **no**) |  |
| **yellow-action** (*drop \| forward \| remark*; Default: **drop**) | 對具有黃色丟棄優先順序的超限流量執行的動作。 |
| **new-dei-for-yellow** (*0..1 \| remap*) | 黃色丟棄優先順序封包的新 DEI。 |
| **new-pcp-for-yellow** (*0..7 \| remap*) | 黃色丟棄優先順序封包的新 PCP。 |
| **new-dscp-for-yellow** (*0..63 \| remap*) | 黃色丟棄優先順序封包的新 DSCP。 |
| **red-action** (*drop \| forward \| remark*; Default: **drop**) | 對具有紅色丟棄優先順序的超限流量執行的動作。 |
| **new-dei-for-red** (*0..1 \| remap*) | 紅色丟棄優先順序封包的新 DEI。 |
| **new-pcp-for-red** (*0..7 \| remap*) | 紅色丟棄優先順序封包的新 PCP。 |
| **new-dscp-for-red** (*0..63 \| remap*) | 紅色丟棄優先順序封包的新 DSCP。 |

## 另請參閱 {#see-also}

---

- [CRS1xx/2xx 系列交換器示例](./user-guides/crs1xx-2xx-series-switches-examples.md)
- [基本 VLAN 交換](./user-guides/basic-vlan-switching.md)
- [網橋硬體解除安裝](index.md#bridge-hardware-offloading)
- [生成樹協定](./user-guides/spanning-tree-protocol.md)
- [IGMP Snooping](./user-guides/bridge-igmp-mld-snooping.md)
- [DHCP Snooping 和 Option 82](index.md#dhcp-snooping-and-dhcp-option-82)
- [RouterBOARD 上的 MTU](../hardware/mtu-in-routeros.md)
- [Layer2 配置錯誤](./user-guides/layer2-misconfiguration.md)
