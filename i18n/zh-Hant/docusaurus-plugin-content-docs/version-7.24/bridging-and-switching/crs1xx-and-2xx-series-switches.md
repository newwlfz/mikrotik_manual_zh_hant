---
title: "CRS1xx 與 2xx 系列交換器"
description: "本頁面介紹 MikroTik RouterOS CRS1xx 與 2xx 系列交換器，說明其高效能特性，包括 Layer 2/3 交換、VLAN 支援、QoS 工具、鏡像功能與埠隔離選項。頁面詳細說明各型號差異、CPU 速度與 jumbo frame 大小等技術規格，並提供 VLAN 相關術語的縮寫。"
tags:
  - 'vlan'
  - 'qos'
  - 'switching'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching/crs1xx-and-2xx-series-switches
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

Cloud Router Switch 系列是高度整合的交換器，配備高效能 MIPS CPU 與功能豐富的封包處理器。CRS 交換器可設計用於各種 Ethernet 應用，包括非網管交換器、Layer 2 網管交換器、電信業者交換器，以及無線／有線統一封包處理。請參閱 [Cloud Router Switch](/docs/bridging-and-switching/user-guides/crs1xx-2xx-series-switches-examples) 設定範例。

:::danger
本文適用於 CRS1xx 與 CRS2xx 系列交換器，不適用於配備 Marvell Prestera 交換器的 MikroTik 設備（例如 CRS3xx）。對於配備 Marvell Prestera 交換器的 MikroTik 設備，請參閱 [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features) 手冊。
:::

| 功能 | 說明 |
| :-- | :-- |
| **轉送** | <ul class="bullets"><li>可設定用於交換或路由的埠</li><li>完整非阻塞線速交換</li><li>Unicast FDB 中最多 16k 個 MAC 項目，用於 Layer 2 unicast 轉送</li><li>Multicast FDB 中最多 1k 個 MAC 項目，用於 multicast 轉送</li><li>Reserved FDB 中最多 256 個 MAC 項目，用於控制與管理用途</li><li>所有 Forwarding Database 皆支援 IVL 與 SVL</li><li>可設定以埠為基礎的 MAC 學習限制</li><li>支援 Jumbo frame（CRS1xx/2xx：9204 Bytes；CRS125/CRS109：4064 Bytes）</li><li>支援 IGMP Snooping</li></ul> |
| **鏡像** | <ul class="bullets"><li>多種鏡像類型：<ul class="bullets"><li>以埠為基礎的鏡像</li><li>以 VLAN 為基礎的鏡像</li><li>以 MAC 為基礎的鏡像</li></ul></li><li>2 個獨立的鏡像分析器埠</li></ul> |
| **VLAN** | <ul class="bullets"><li>完全相容於 IEEE802.1Q 與 IEEE802.1ad VLAN</li><li>4k 個作用中 VLAN</li><li>彈性 VLAN 指派：<ul class="bullets"><li>以埠為基礎的 VLAN</li><li>以通訊協定為基礎的 VLAN</li><li>以 MAC 為基礎的 VLAN</li></ul></li><li>任意 VLAN 之間的轉換與交換</li><li>1:1 VLAN 交換：VLAN 對埠的對應</li><li>VLAN 過濾</li></ul> |
| **埠隔離與洩漏** | <ul class="bullets"><li>適用於 Private VLAN 實作</li><li>3 種埠設定檔類型：Promiscuous、Isolated 與 Community</li><li>最多 28 個 Community 設定檔</li><li>洩漏設定檔可略過 egress VLAN 過濾</li></ul> |
| **Trunking** | <ul class="bullets"><li>支援靜態鏈路彙總群組</li><li>最多 8 個 Port Trunk 群組</li><li>每個 Port Trunk 群組最多 8 個成員埠</li><li>硬體自動容錯移轉與負載平衡</li></ul> |
| **服務品質（QoS）** | <ul class="bullets"><li>彈性 QoS 分類與指派：<ul class="bullets"><li>以埠為基礎</li><li>以 MAC 為基礎</li><li>以 VLAN 為基礎</li><li>以通訊協定為基礎</li><li>以 PCP/DEI 為基礎</li><li>以 DSCP 為基礎</li><li>以 ACL 為基礎</li></ul></li><li>QoS 重新標記與重新對應，用於服務提供者與用戶端網路之間的 QoS 網域轉換</li><li>依據所設定的優先權覆寫各項 QoS 指派</li></ul> |
| **整形與排程** | <ul class="bullets"><li>每個實體埠有 8 個佇列</li><li>依埠、依佇列、依佇列群組進行整形</li></ul> |
| **存取控制清單** | <ul class="bullets"><li>Ingress 與 Egress ACL 表</li><li>最多 128 條 ACL 規則（受 RouterOS 限制）</li><li>依據埠、L2、L3、L4 通訊協定標頭欄位進行分類</li><li>ACL 動作包括過濾、轉送，以及修改通訊協定標頭欄位</li></ul> |

## Cloud Router Switch 型號 {#cloud-router-switch-models}

---

此表格說明 Cloud Router Switch 各型號之間的主要差異。

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **型號** | **交換器晶片** | **CPU** | **無線** | **SFP+ 埠** | **存取控制清單** | **Jumbo Frame（Bytes）** |
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

CVID - Customer VLAN id：IEEE 802.1ad 訊框的內部 VLAN tag id

SVID - Service VLAN id：IEEE 802.1ad 訊框的外層 VLAN 標籤 id

IVL - Independent VLAN learning：學習／查詢會同時依據 MAC 位址與 VLAN ID。

SVL - Shared VLAN learning：學習／查詢僅依據 MAC 位址，不依據 VLAN ID。

TPID - Tag Protocol Identifier（標籤協定識別碼）

PCP - Priority Code Point：指向 IEEE 802.1p 優先權的 3 位元欄位

DEI - 可捨棄指標

DSCP - 差異化服務代碼點

Drop precedence - 內部 CRS 交換器 QoS 屬性，用於封包佇列或丟棄。

## 埠切換 {#port-switching}

---

若要在 CRS1xx/2xx 系列交換器上設定埠切換，請參閱 [Bridge Hardware Offloading](/docs/bridging-and-switching/crs1xx-and-2xx-series-switches#bridge-hardware-offloading) 頁面。

:::warning
當建立硬體卸載 bridge 時加入已切換的埠群組，CRS 交換器會建立動態保留的 VLAN 項目（VLAN4091；VLAN4090；VLAN4089；等）。這些 VLAN 是內部運作所需，且優先順序低於使用者設定的 VLAN。
:::

### 多個交換器群組 {#multiple-switch-groups}

CRS1xx/2xx 系列交換器可讓你使用多個啟用硬體卸載的 bridge；這可讓你輕鬆隔離多個交換器群組。只要建立多個 bridge 並啟用硬體卸載即可完成。

:::warning
多個硬體卸載 bridge 的設定是為了提供快速且簡單的埠隔離方案，但會限制 CRS 交換器晶片支援的部分 VLAN 功能。進階設定請在 CRS 交換器晶片內對所有埠使用單一 bridge，設定 VLAN，並使用埠隔離 profile 設定來隔離埠群組。
:::

:::danger
CRS1xx/2xx 系列交換器可以在啟用 (R)STP 的情況下執行多個硬體卸載 bridge，但不建議這麼做，因為設備並非設計用於在硬體層級執行多個 (R)STP 執行個體。若要隔離多個交換器群組並啟用 (R)STP，你應該使用埠隔離 profile 設定來隔離埠群組。
:::

## 全域設定 {#global-settings}

---

CRS 交換器晶片可從 `/interface/ethernet/switch` 主控台選單設定。

**子選單：** `/interface/ethernet/switch`

| Property | Description |
| :-- | :-- |
| **name** (*string value*; Default: **switch1**) | 交換器名稱。 |
| **bridge-type** (*customer-vid-used-as-lookup-vid \| service-vid-used-as-lookup-vid*; Default: **customer-vid-used-as-lookup-vid**) | 橋接類型定義哪一個 VLAN 標籤用作 Lookup-VID。Lookup-VID 做為所有以 VLAN 為基礎查詢的 VLAN 索引鍵。 |
| **mac-level-isolation** (*yes \| no*; Default: **yes**) | 全域啟用或停用 MAC 層級隔離。啟用後，交換器會檢查來源與目的 MAC 位址項目，以及其在單播轉送表中的 `isolation-profile`。預設情況下，交換器會學習 MAC 位址，並將其放入 `promiscuous` 隔離設定檔。建立靜態單播項目時，可使用其他隔離設定檔。若來源或目的 MAC 位址位於 `promiscuous` 隔離設定檔，封包會被轉送。若來源與目的 MAC 位址都位於相同的 `community1` 或 `community2` 隔離設定檔，封包會被轉送。當來源與目的 MAC 位址的隔離設定檔為 `isolated`，或來源與目的 MAC 位址的隔離設定檔屬於不同群組時（例如來源 MAC 位址為 `community1`，目的 MAC 位址為 `community2`），封包會被丟棄。當 MAC 層級隔離在全域停用時，會略過隔離檢查。 |
| **use-svid-in-one2one-vlan-lookup** (*yes \| no*; Default: **no**) | 是否使用 service VLAN ID 進行 1:1 VLAN 交換查詢。 |
| **use-cvid-in-one2one-vlan-lookup** (*yes \| no*; Default: **yes**) | 是否使用 customer VLAN ID 進行 1:1 VLAN 交換查詢。 |
| <strong>multicast-lookup-mode</strong> (<em>dst-ip-and-vid-for-ipv4 &#124; dst-mac-and-vid-always</em>; <br/>Default:<strong>dst-ip-and-vid-for-ipv4</strong>) | IPv4 多播橋接的查詢模式。<ul class="bullets"><li>dst-mac-and-vid-always - 對所有封包類型，查詢索引鍵為目的 MAC 與 VLAN ID。</li><li>dst-ip-and-vid-for-ipv4 - 對 IPv4 封包，查詢索引鍵為目的 IP 與 VLAN ID。對其他封包類型，查詢索引鍵為目的 MAC 與 VLAN ID。</li></ul> |
| **unicast-fdb-timeout** (*time interval*; Default: **5m**) | Unicast FDB 項目的逾時時間。 |
| **override-existing-when-ufdb-full** (*yes \| no*; Default: **no**) | 啟用或停用當 UFDB 已滿時，覆寫具有最低老化值的現有項目。 |

| Property | Description |
| :-- | :-- |
| **drop-if-no-vlan-assignment-on-ports** (*ports*; Default: **none**) | 當未套用以 MAC 為基礎、以通訊協定為基礎的 VLAN 指派或 Ingress VLAN Translation 時，會丟棄訊框的埠。 |
| **drop-if-invalid-or-src-port- -not-member-of-vlan-on-ports** (*ports*; Default: **none**) | 會丟棄無效及其他埠 VLAN ID 訊框的埠。 |
| **unknown-vlan-lookup-mode** (*ivl \| svl*; Default: **svl**) | 對具有無效 VLAN 的封包所使用的查詢與學習模式。 |
| **forward-unknown-vlan** (*yes \| no*; Default: **yes**) | 是否允許轉送不屬於 VLAN 表的 VLAN。 |

| Property | Description |
| :-- | :-- |
| **bypass-vlan-ingress-filter-for** (*protocols*; Default: **none**) | 從 Ingress VLAN 篩選中排除的通訊協定。這些通訊協定若具有無效 VLAN，也不會被丟棄。（arp、dhcpv4、dhcpv6、eapol、igmp、mld、nd、pppoe-discovery、ripv1） |
| **bypass-ingress-port-policing-for** (*protocols*; Default: **none**) | 從 Ingress Port Policing 中排除的通訊協定。（arp、dhcpv4、dhcpv6、eapol、igmp、mld、nd、pppoe-discovery、ripv1） |
| **bypass-l2-security-check-filter-for** (*protocols*; Default: **none**) | 從 Policy rule security check 中排除的通訊協定。（arp、dhcpv4、dhcpv6、eapol、igmp、mld、nd、pppoe-discovery、ripv1） |

| Property | Description |
| :-- | :-- |
| **ingress-mirror0** (*port \| trunk,format*; Default: **none,modified**) | 第一個 ingress 鏡像分析器埠或 trunk，以及鏡像格式：<ul class="bullets"><li>analyzer-configured - 封包與送往目的地的封包相同。VLAN 格式會根據分析器埠的 VLAN 設定修改。</li><li>modified - 封包與送往目的地的封包相同。VLAN 格式會根據 egress 埠的 VLAN 設定修改。</li><li>original - 流量會被鏡像，且原始傳入封包格式不會有任何變更。但 service VLAN 標籤會在 edge 埠移除。</li></ul> |
| **ingress-mirror1** (*port \| trunk,format*; Default: **none,modified**) | 第二個 ingress 鏡像分析器埠或 trunk，以及鏡像格式：<ul class="bullets"><li>analyzer-configured - 封包與送往目的地的封包相同。VLAN 格式會根據分析器埠的 VLAN 設定修改。</li><li>modified - 封包與送往目的地的封包相同。VLAN 格式會根據 egress 埠的 VLAN 設定修改。</li><li>original - 流量會被鏡像，且原始傳入封包格式不會有任何變更。但 service VLAN 標籤會在 edge 埠移除。</li></ul> |
| **ingress-mirror-ratio** (*1/32768..1/1*; Default: **1/1**) | ingress 鏡像封包占所有封包的比例。 |
| **egress-mirror0** (*port \| trunk,format*; Default: **none,modified**) | 第一個 egress 鏡像分析器埠或 trunk，以及鏡像格式：<ul class="bullets"><li>analyzer-configured - 封包與送往目的地的封包相同。VLAN 格式會根據分析器埠的 VLAN 設定修改。</li><li>modified - 封包與送往目的地的封包相同。VLAN 格式會根據 egress 埠的 VLAN 設定修改。</li><li>original - 流量會被鏡像，且原始傳入封包格式不會有任何變更。但 service VLAN 標籤會在 edge 埠移除。</li></ul> |
| **egress-mirror1** (*port \| trunk,format*; Default: **none,modified**) | 第二個 egress 鏡像分析器埠或 trunk，以及鏡像格式：<ul class="bullets"><li>analyzer-configured - 封包與送往目的地的封包相同。VLAN 格式會根據分析器埠的 VLAN 設定修改。</li><li>modified - 封包與送往目的地的封包相同。VLAN 格式會根據 egress 埠的 VLAN 設定修改。</li><li>original - 流量會被鏡像，且原始傳入封包格式不會有任何變更。但 service VLAN 標籤會在 edge 埠移除。</li></ul> |
| **egress-mirror-ratio** (*1/32768..1/1*; Default: **1/1**) | egress 鏡像封包占所有封包的比例。 |
| **mirror-egress-if-ingress-mirrored** (*yes \| no*; Default: **no**) | 當封包同時套用 ingress 與 egress 鏡像時，若此設定停用，則只對封包執行 ingress 鏡像。若此設定啟用，則會套用兩種鏡像類型。 |
| **mirror-tx-on-mirror-port** (*yes \| no*; Default: **no**) |  |
| **mirrored-packet-qos-priority** (*0..7*; Default: **0**) | 鏡像封包中重新標記的優先順序。 |
| **mirrored-packet-drop-precedence** (*drop \| green \| red \| yellow*; Default: **green**) | 鏡像封包中重新標記的丟棄優先順序。此 QoS 屬性用於鏡像封包的佇列或丟棄。 |
| **fdb-uses** (*mirror0 \| mirror1*; Default: **mirror0**) | 用於以 FDB 為基礎鏡像的分析器埠。 |
| **vlan-uses** (*mirror0 \| mirror1*; Default: **mirror0**) | 用於以 VLAN 為基礎鏡像的分析器埠。 |

## 埠設定 {#port-settings}

---

**子選單：** `/interface/ethernet/switch/port`

| Property | Description |
| :-- | :-- |
| **vlan-type** (*edge-port \| network-port*; Default: **network-port**) | 埠 VLAN 類型指定 VLAN ID 是否用於 UFDB 學習。network port 會在 UFDB 中學習 VLAN ID，edge port 則不會（VLAN 0）。這只能在 IVL 學習模式中觀察到。 |
| <strong>isolation-leakage-profile-override</strong> (<em>yes &#124; no</em>; Default: <strong>!isolation-leakage-profile-override</strong>) <br/><strong>isolation-leakage-profile</strong> (<em>0..31</em>;) | 用於埠隔離／洩漏設定的自訂埠設定檔。<ul class="bullets"><li>埠層級隔離設定檔 0。Uplink 埠：允許該埠與設備中的所有埠通訊。</li><li>埠層級隔離設定檔 1。隔離埠：允許該埠僅與 uplink 埠通訊。</li><li>埠層級隔離設定檔 2 - 31。Community 埠：允許在相同 community 埠與 uplink 埠之間通訊。</li></ul> |
| **learn-override** (*yes \| no*; Default: **!learn-override**) **learn-limit** (*1..1023*; Default: **!learn-limit**) | 啟用或停用 MAC 位址學習，並設定埠上的 MAC 限制。當設定 !learn-override 與 !learn-limit 時，MAC 學習限制預設停用。自 RouterOS v6.42 起，learn-override 屬性已由 `/interface/bridge/port` 選單下的 learn 取代。 |
| **drop-when-ufdb-entry-src-drop** (*yes \| no*; Default: **yes**) | 當 UFDB 項目具有 src-drop 動作時，啟用或停用丟棄封包。 |
| **allow-unicast-loopback** (*yes \| no*; Default: **no**) | 埠上的單播回送。啟用時，對於已知單播封包，若來源埠與目的埠相同，則允許送回。 |
| **allow-multicast-loopback** (*yes \| no*; Default: **no**) | 埠上的多播回送。啟用時，對於已註冊多播或廣播封包，若來源埠與目的埠相同，則允許送回。 |
| **action-on-static-station-move** (*copy-to-cpu \| drop \| forward \| redirect-to-cpu*; Default: **forward**) | 當 UFDB 已包含具有相同 MAC 但位於不同埠的靜態項目時，對封包採取的動作。 |
| **drop-dynamic-mac-move** (*yes \| no*; Default: **no**) | 若 MAC 已在另一個埠上學習到，則在 UFDB 逾時前防止 MAC 重新學習。 |

| Property | Description |
| :-- | :-- |
| **allow-fdb-based-vlan-translate** (*yes \| no*; Default: **no**) | 啟用或停用埠上以 MAC 為基礎的 VLAN 轉換。 |
| <strong>allow-mac-based-service-vlan-assignment-for</strong> (<em>all-frames &#124; none &#124;</em><em>tagged-frame-only &#124; untagged-and-priority-tagged-frame-only</em>; Default: <br/><strong>none</strong>) | 適用以 MAC 為基礎的 service VLAN 轉換的訊框類型。 |
| <strong>allow-mac-based-customer-vlan-assignment-for</strong> (<em>all-frames &#124; none &#124;</em><em>tagged-frame-only &#124; untagged-and-priority-tagged-frame-only</em>; Default: <br/><strong>none</strong>) | 適用以 MAC 為基礎的 customer VLAN 轉換的訊框類型。 |
| **default-customer-pcp** (*0..7*; Default: **0**) | 埠的預設 customer PCP。 |
| **default-service-pcp** (*0..7*; Default: **0**) | 埠的預設 service PCP。 |
| **pcp-propagation-for-initial-pcp** (*yes \| no*; Default: **no**) | 啟用或停用 ingress 初始 PCP 指派的 PCP 傳播。<ul class="bullets"><li>若埠 vlan-type 為 Edge 埠，則 service PCP 會從 customer PCP 複製。</li><li>若埠 vlan-type 為 Network 埠，則 customer PCP 會從 service PCP 複製。</li></ul> |
| **filter-untagged-frame** (*yes \| no*; Default: **no**) | 是否篩選埠上的未標記訊框。 |
| **filter-priority-tagged-frame** (*yes \| no*; Default: **no**) | 是否篩選埠上具優先權的標記訊框。 |
| **filter-tagged-frame** (*yes \| no*; Default: **no**) | 是否篩選埠上的標記訊框。 |

| Property | Description |
| :-- | :-- |
| **egress-vlan-tag-table-lookup-key** (*according-to-bridge-type \| egress-vid*; Default: **egress-vid**) | Egress VLAN 表（VLAN 標記）查閱：<ul class="bullets"><li>egress-vid - 當設定為 Edge 埠時，查閱 VLAN ID 為 CVID；當設定為 Network 埠時，查閱 VLAN ID 為 SVID。</li><li>according-to-bridge-type - 當設定為 customer VLAN bridge 時，查閱 VLAN ID 為 CVID；當設定為 service VLAN bridge 時，查閱 VLAN ID 為 SVID。在 service VLAN bridge 中，Edge 埠的 Customer 標記不會被修改。</li></ul> |
| **egress-vlan-mode** (*tagged \| unmodified \| untagged*; Default: **unmodified**) | 埠上的 egress VLAN 標記動作。 |
| **egress-pcp-propagation** (*yes \| no*; Default: **no**) | 啟用或停用 egress PCP 傳播。<ul class="bullets"><li>若埠 vlan-type 為 Edge 埠，則 service PCP 會從 customer PCP 複製。</li><li>若埠 vlan-type 為 Network 埠，則 customer PCP 會從 service PCP 複製。</li></ul> |

| Property | Description |
| :-- | :-- |
| **ingress-mirror-to** (*mirror0 \| mirror1 \| none*; Default: **none**) | 用於以埠為基礎的 ingress 鏡像的 Analyzer 埠。 |
| **ingress-mirroring-according-to-vlan** (*yes \| no*; Default: **no**) |  |
| **egress-mirror-to** (*mirror0 \| mirror1 \| none*; Default: **none**) | 用於以埠為基礎的 egress 鏡像的 Analyzer 埠。 |

| Property | Description |
| :-- | :-- |
| **qos-scheme-precedence** (*da-based \| dscp-based \| ingress-acl-based \| pcp-based \| protocol-based \| sa-based \| vlan-based*; Default: **pcp-based, sa-based, da-based, dscp-based, protocol-based, vlan-based**) | 指定在埠 ingress 套用的 QoS 指派配置。<ul class="bullets"><li>da-based</li><li>dscp-based</li><li>ingress-acl-based</li><li>pcp-based</li><li>protocol-based</li><li>sa-based</li><li>vlan-based</li></ul> |
| **pcp-or-dscp-based-qos-change-dei** (*yes \| no*; Default: **no**) | 啟用或停用埠上以 PCP 或 DSCP 為基礎的 DEI 變更。 |
| **pcp-or-dscp-based-qos-change-pcp** (*yes \| no*; Default: **no**) | 啟用或停用埠上以 PCP 或 DSCP 為基礎的 PCP 變更。 |
| **pcp-or-dscp-based-qos-change-dscp** (*yes \| no*; Default: **no**) | 啟用或停用埠上以 PCP 或 DSCP 為基礎的 DSCP 變更。 |
| **dscp-based-qos-dscp-to-dscp-mapping** (*yes \| no*; Default: **yes**) | 啟用或停用埠上 DSCP 至內部 DSCP 的對應。 |
| **pcp-based-qos-drop-precedence-mapping** (*PCP/DEI-range:drop-precedence*; Default: **0-15:green**) | PCP/DEI 至 drop precedence（drop \| green \| red \| yellow）對應的新 drop precedence 值。允許多個對應，以逗號分隔，例如「0-7:yellow,8-15:red」。 |
| **pcp-based-qos-dscp-mapping** (*PCP/DEI-range:DEI*; Default: **0-15:0**) | PCP/DEI 至 DSCP（0..63）對應的新 DSCP 值。允許多個對應，以逗號分隔，例如「0-7:25,8-15:50」。 |
| **pcp-based-qos-dei-mapping** (*PCP/DEI-range:DEI*; Default: **0-15:0**) | PCP/DEI 至 DEI（0..1）對應的新 DEI 值。允許多個對應，以逗號分隔，例如「0-7:0,8-15:1」。 |
| **pcp-based-qos-pcp-mapping** (*PCP/DEI-range:DEI*; Default: **0-15:0**) | PCP/DEI 至 PCP（0..7）對應的新 PCP 值。允許多個對應，以逗號分隔，例如「0-7:3,8-15:4」。 |
| **pcp-based-qos-priority-mapping** (*PCP/DEI-range:DEI*; Default: **0-15:0**) | PCP/DEI 至 priority（0..15）對應的新內部優先權值。允許多個對應，以逗號分隔，例如「0-7:5,8-15:15」。 |

| Property | Description |
| :-- | :-- |
| **priority-to-queue** (*priority-range:queue*; Default: **0-15:0,1:1,2:2,3:3**) | 每埠的內部優先權（0..15）至佇列（0..7）對應。 |
| <strong>per-queue-scheduling</strong> (<em>Scheduling-type:Weight</em>; Default: <strong>wrr-group0:1,wrr-group0:2,wrr-group0:4,wrr-group0:8,wrr-group0:16,wrr-group0:32,</strong><br/><strong>wrr-group0:64,wrr-group0:128</strong>) | 設定埠針對每個佇列群組使用 strict 或 weighted round robin 流量整形策略；每個佇列以逗號分隔。 |

| Property | Description |
| :-- | :-- |
| <strong>ingress-customer-tpid-override</strong> (<em>yes &#124; no</em>; Default:<strong>!ingress-customer-tpid-override</strong>) <br/><strong>ingress-customer-tpid</strong> (<em>0..10000</em>; Default: <strong>0x8100</strong>) | Ingress customer TPID override 可接受具有自訂 customer tag TPID 的特定訊框。預設值適用於 802.1Q 訊框的標記。 |
| <strong>egress-customer-tpid-override</strong> (<em>yes &#124; no</em>; Default: <strong>!egress-customer-tpid-override</strong>) <strong>egress-customer-tpid</strong> (<em>0..10000</em>; Default: <br/><strong>0x8100</strong>) | Egress customer TPID override 可對具有 customer tag 的 egress 訊框進行自訂識別。預設值適用於 802.1Q 訊框的標記。 |
| <strong>ingress-service-tpid-override</strong> (<em>yes &#124; no</em>; Default: <strong>!ingress-service-tpid-override</strong>) <br/><strong>ingress-service-tpid</strong> (<em>0..10000</em>; Default: <strong>0x88A8</strong>) | Ingress service TPID override 可接受具有自訂 service tag TPID 的特定訊框。預設值適用於 802.1AD 訊框的 service tag。 |
| <strong>egress-service-tpid-override</strong> (<em>yes &#124; no</em>; Default: <strong>!egress-service-tpid-override</strong>) <strong>egress-service-tpid</strong> (<em>0..10000</em>; Default: <br/><strong>0x88A8</strong>) | Egress service TPID override 可對具有 service tag 的 egress 訊框進行自訂識別。預設值適用於 802.1AD 訊框的 service tag。 |

| Property | Description |
| :-- | :-- |
| **custom-drop-counter-includes** (*counters*; Default: **none**) | 自訂包含項目，用於交換器埠 custom-drop-packet 計數器統計丟棄的封包。<ul><li><strong>device-loopback</strong></li><li><strong>fdb-hash-violation</strong></li><li><strong>exceeded-port-learn-limitation</strong></li><li><strong>dynamic-station-move</strong></li><li><strong>static-station-move</strong></li><li><strong>ufdb-source-drop</strong></li><li><strong>host-source-drop</strong></li><li><strong>unknown-host</strong></li><li><strong>ingress-vlan-filtered</strong></li></ul> |
| **queue-custom-drop-counter0-includes** (*counters*; Default: **none**) | 自訂包含項目，用於交換器埠 tx-queue-custom0-drop-packet 計數器統計丟棄的封包，以及 tx-queue-custom0-drop-byte 計數器統計位元組。<br/><ul><li><strong>red</strong></li><li><strong>yellow</strong></li><li><strong>green</strong></li><li><strong>queue0</strong></li><li><strong>...</strong></li><li><strong>queue7</strong></li></ul> |
| **queue-custom-drop-counter1-includes** (*counters*; Default: **none**) | 自訂包含項目，用於交換器埠 tx-queue-custom1-drop-packet 計數器統計丟棄的封包，以及 tx-queue-custom1-drop-byte 計數器統計位元組。<br/><ul><li><strong>red</strong></li><li><strong>yellow</strong></li><li><strong>green</strong></li><li><strong>queue0</strong></li><li><strong>...</strong></li><li><strong>queue7</strong></li></ul> |
| **policy-drop-counter-includes** (*counters*; Default: **none**) | 自訂包含項目，用於交換器埠 policy-drop-packet 計數器統計丟棄的封包。<ul><li><strong>ingress-policing</strong></li><li><strong>ingress-acl</strong></li><li><strong>egress-policing</strong></li><li><strong>egress-acl</strong></li></ul> |

## 轉送資料庫 {#forwarding-databases}

---

### Unicast FDB

單播轉送資料庫最多支援 16K 個 MAC 項目。

**子選單：** `/interface/ethernet/switch/unicast-fdb`

| Property | Description |
| :-- | :-- |
| **action** (*action*; Default: **forward**) | UFDB 項目的動作：<ul class="bullets"><li>dst-drop - 當封包的目的 MAC 與項目相符時，捨棄封包。</li><li>dst-redirect-to-cpu - 當封包的目的 MAC 與項目相符時，將封包重新導向至 CPU。</li><li>forward - 轉送封包。</li><li>src-and-dst-drop - 當封包的來源 MAC 或目的 MAC 與項目相符時，捨棄封包。</li><li>src-and-dst-redirect-to-cpu - 當封包的來源 MAC 或目的 MAC 與項目相符時，將封包重新導向至 CPU。</li><li>src-drop - 當封包的來源 MAC 與項目相符時，捨棄封包。</li><li>src-redirect-to-cpu - 當封包的來源 MAC 與項目相符時，將封包重新導向至 CPU。</li></ul> |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用 Unicast FDB 項目。 |
| **isolation-profile** (*community1 \| community2 \| isolated \| promiscuous*; Default: **promiscuous**) | MAC 層級隔離設定檔。 |
| **mac-address** (*MAC address*) | 當目的 MAC 或來源 MAC 與項目相符時，動作命令會套用至封包。 |
| **mirror** (*yes \| no*; Default: **no**) | 依據來源 MAC 或目的 MAC 啟用或停用鏡像。 |
| **port** (*port*) | Unicast FDB 項目的相符埠。 |
| **qos-group** (*none*; Default: **none**) | 從 QoS group 選單定義的 QoS 群組。 |
| **svl** (*yes \| no*; Default: **no**) | Unicast FDB 學習模式：<ul class="bullets"><li>Shared VLAN Learning (svl) - 學習／查閱是依據 MAC 位址，而非 VLAN ID。</li><li>Independent VLAN Learning (ivl) - 學習／查閱同時依據 MAC 位址與 VLAN ID。</li></ul> |
| **vlan-id** (*0..4095*) | Unicast FDB 查閱／學習的 VLAN id。 |

### 多播 FDB {#multicast-fdb}

CRS125 交換器晶片在 MFDB 中最多支援 1024 個項目，用於多播轉送。對於每個多播封包，會在 MFDB 中執行目的 MAC 或目的 IP 查閱。MFDB 項目不會自動學習，只能透過設定建立。

**子選單：** `/interface/ethernet/switch/multicast-fdb`

| 屬性 | 說明 |
| :-- | :-- |
| **address** (*X.X.X.X \| XX:XX:XX:XX:XX:XX*) | 符合多播封包的 IP 位址或 MAC 位址。 |
| **bypass-vlan-filter** (*yes \| no*; 預設: **no**) | 允許符合的多播封包略過 VLAN 過濾。 |
| **disabled** (*yes \| no*; 預設: **no**) | 啟用或停用 Multicast FDB 項目。 |
| **ports** (*ports*) | 多播流量的成員埠。 |
| **qos-group** (*none*; 預設: **none**) | 從 QoS group 選單定義的 QoS 群組。 |
| **svl** (*yes \| no*; 預設: **no**) | Multicast FDB 學習模式：<ul class="bullets"><li>Shared VLAN Learning (svl) - 學習／查閱是根據 MAC 位址，而非 VLAN ID。</li><li>Independent VLAN Learning (ivl) - 學習／查閱是根據 MAC 位址與 VLAN ID。</li></ul> |
| **vlan-id** (*0..4095*; 預設: **0**) | Multicast FDB 查閱 VLAN ID。若 VLAN 學習模式為 IVL，VLAN id 即為查閱 ID，否則 VLAN id = 0。 |

### 保留的 FDB {#reserved-fdb}

Cloud Router Switch 支援 256 個 RFDB 項目。每個 RFDB 項目可使用特定指令儲存 Layer2 單播或多播 MAC 位址。

**子選單：** `/interface/ethernet/switch/reserved-fdb`

| 屬性 | 說明 |
| :-- | :-- |
| **action** (*copy-to-cpu \| drop \| forward \| redirect-to-cpu*; 預設: **forward**) | RFDB 項目的動作：<ul class="bullets"><li>copy-to-cpu - 當封包的目的地 MAC 符合該項目時，將封包複製到 CPU。</li><li>drop - 當封包的目的地 MAC 符合該項目時，丟棄封包。</li><li>forward - 當封包的目的地 MAC 符合該項目時，轉送封包。</li><li>redirect-to-cpu - 當封包的目的地 MAC 符合該項目時，將封包重新導向到 CPU。</li></ul> |
| **bypass-ingress-port-policing** (*yes \| no*; 預設: **no**) | 允許符合的封包略過 Ingress Port Policer。 |
| **bypass-ingress-vlan-filter** (*yes \| no*; 預設: **no**) | 允許符合的封包略過 VLAN 過濾。 |
| **disabled** (*yes \| no*; 預設: **no**) | 啟用或停用 Reserved FDB 項目。 |
| **mac-address** (*MAC address*; 預設: **00:00:00:00:00:00**) | Reserved FDB 項目的符合 MAC 位址。 |
| **qos-group** (*none*; 預設: **none**) | 從 QoS group 選單定義的 QoS 群組。 |

## VLAN

---

### VLAN 表 {#vlan-table}

VLAN 表支援 4096 個 VLAN 項目，用於儲存 VLAN 成員資訊，以及其他 VLAN 資訊，例如 QoS、隔離、強制 VLAN、學習與鏡像。

**子選單：** `/interface/ethernet/switch/vlan`

| 屬性 | 說明 |
| :-- | :-- |
| **disabled** (*yes \| no*；預設：**no**) | 指出 VLAN 項目是否已停用。只有啟用的項目會套用至查閱程序與轉送決策。 |
| **flood** (*yes \| no*；預設：**no**) | 啟用或停用每個 VLAN 的強制 VLAN 泛洪。若啟用此功能，系統會忽略 UFDB 或 MFDB 中的目的 MAC 查閱結果，<br/>並強制封包在 VLAN 中泛洪。 |
| **ingress-mirror** (*yes \| no*；預設：**no**) | 啟用每個 VLAN 的 ingress 鏡像，以支援以 VLAN 為基礎的鏡像功能。 |
| **learn** (*yes \| no*；預設：**yes**) | 啟用或停用 VLAN 的來源 MAC 學習。 |
| **ports** (*ports*) | VLAN 的成員埠。 |
| **qos-group** (*none*；預設：**none**) | 從 QoS group 選單定義的 QoS 群組。 |
| **svl** (*yes \| no*；預設：**no**) | 用於 UFDB 與 MFDB 查閱的 FDB 查閱模式。<ul class="bullets"><li>Shared VLAN Learning (svl) - 學習／查閱是根據 MAC 位址，而非 VLAN ID。</li><li>Independent VLAN Learning (ivl) - 學習／查閱是根據 MAC 位址與 VLAN ID。</li></ul> |
| **vlan-id** (*0..4095*) | VLAN 成員項目的 VLAN ID。 |

### Egress VLAN Tag

送出封包可以指派不同的 VLAN 標籤格式。當封包傳送至 egress 埠（目的埠）時，VLAN 標籤可以移除、新增或保持原樣。每個埠都有專屬的 egress VLAN 標籤格式控制。標籤格式包括：

- 未標記
- 已標記
- 未修改

Egress VLAN Tag 表格包含 4096 個項目，用於 VLAN 標記選擇。

**子選單：** `/interface/ethernet/switch/egress-vlan-tag`

| 屬性 | 說明 |
| :-- | :-- |
| **disabled** (*yes \| no*；預設：**no**) | 啟用或停用 Egress VLAN Tag 表格項目。 |
| **tagged-ports** (*ports*) | 在 egress 中加上標籤的埠。 |
| **vlan-id** (*0..4095*) | 在 egress 中加上標籤的 VLAN ID。 |

### Ingress/Egress VLAN 轉換 {#ingressegress-vlan-translation}

Ingress VLAN Translation 表格每個埠最多允許 15 個項目。可以從封包標頭選取一或多個欄位，用於在 Ingress VLAN Translation 表格中查閱。第一個符合項目中設定的 S-VLAN 或 C-VLAN，或兩者，會指派給該封包。

**子選單：** `/interface/ethernet/switch/ingress-vlan-translation, /interface/ethernet/switch/egress-vlan-translation`

| 屬性 | 說明 |
| :-- | :-- |
| **customer-dei** (*0..1*；預設：**none**) | 比對 customer tag 的 DEI。 |
| **customer-pcp** (*0..7*；預設：**none**) | 比對 customer tag 的 PCP。 |
| **customer-vid** (*0..4095*；預設：**none**) | 比對 customer tag 的 VLAN ID。 |
| **customer-vlan-format** (*any \| priority-tagged-or-tagged \| tagged \| untagged-or-tagged*；預設：**any**) | 具有 customer tag 且 VLAN translation 規則有效的訊框類型。 |
| **disabled** (*yes \| no*；預設：**no**) | 啟用或停用 VLAN translation 項目。 |
| **new-customer-vid** (*0..4095*；預設：**none**) | 新的 customer VLAN ID 會取代符合的 customer VLAN ID。若設為 4095 且使用 ingress VLAN translation，則流量會被丟棄。 |
| **new-service-vid** (*0..4095*；預設：**none**) | 新的 service VLAN ID 會取代符合的 service VLAN ID。 |
| **pcp-propagation** (*yes \| no*；預設：**no**) | 啟用或停用 PCP 傳播。<ul class="bullets"><li>若埠類型為 Edge，則 customer PCP 會從 service PCP 複製。</li><li>若埠類型為 Network，則 service PCP 會從 customer PCP 複製。</li></ul> |
| **ports** (*ports*) | VLAN translation 規則比對的交換器埠。 |
| **protocol** (*protocols*；預設：**none**) | 比對 Ethernet 協定。*(僅適用於 Ingress VLAN Translation)* |
| **sa-learning** (*yes \| no*；預設：**no**) | 啟用或停用 VLAN translation 後的來源 MAC 學習。*(僅適用於 Ingress VLAN Translation)* |
| **service-dei** (*0..1*；預設：**none**) | 比對 service tag 的 DEI。 |
| **service-pcp** (*0..7*；預設：**none**) | 比對 service tag 的 PCP。 |
| **service-vid** (*0..4095*；預設：**none**) | 比對 service tag 的 VLAN ID。 |
| **service-vlan-format** (*any \| priority-tagged-or-tagged \| tagged \| untagged-or-tagged*；預設：**any**) | 具有 service tag 且 VLAN translation 規則有效的訊框類型。 |

下表列出會觸發已設定特定 VLAN 格式之規則的流量；請注意，標記為 VLAN ID 0 的流量是特殊情況，也會納入考量。

| 屬性 | 說明 |
| :-- | :-- |
| **any** | 接受：<ul><li>未標記流量</li><li>已標記流量</li><li>已設定優先順序的已標記流量</li><li>VLAN 0 流量</li><li>已設定優先順序的 VLAN 0 流量</li></ul> |
| **priority-tagged-or-tagged** | 接受：<ul><li>已標記流量</li><li>已設定優先順序的已標記流量</li><li>VLAN 0 流量</li><li>已設定優先順序的 VLAN 0 流量</li></ul> |
| **tagged** | 接受：<ul><li>已標記流量</li><li>已設定優先順序的已標記流量</li></ul> |
| **untagged-or-tagged** | 接受：<ul><li>未標記流量</li><li>已標記流量</li><li>已設定優先順序的已標記流量</li></ul> |

:::danger
若 `VLAN-format` 設為 `any`，則設為 `0` 的 `customer-vid``/``service-vid` 會以 VLAN 0 流量觸發交換器規則。在此情況下，交換器規則會尋找未標記流量或具有 VLAN 0 tag 的流量，且只有 `untagged-or-tagged` 會篩選掉 VLAN 0 流量。
:::

### 以協定為基礎的 VLAN {#protocol-based-vlan}

Protocol Based VLAN 表格用於依每個埠將 VID 與 QoS 屬性指派給相關的協定封包。

**子選單：** `/interface/ethernet/switch/protocol-based-vlan`

| 屬性 | 說明 |
| :-- | :-- |
| **disabled** (*yes \| no*；預設：**no**) | 啟用或停用 Protocol Based VLAN 項目。 |
| **frame-type** (*ethernet \| llc \| rfc-1042*；預設：**ethernet**) | 符合條件的訊框封裝類型。 |
| **new-customer-vid** (*0..4095*；預設：**0**) | 新的 customer VLAN ID 會取代指定協定的原始 customer VLAN ID。若設為 4095，則捨棄流量。 |
| **new-service-vid** (*0..4095*；預設：**0**) | 新的 service VLAN ID 會取代指定協定的原始 service VLAN ID。 |
| **ports** (*ports*) | Protocol-based VLAN 規則符合的交換器埠。 |
| **protocol** (*protocol*；預設：**0**) | Protocol-based VLAN 規則符合的協定。 |
| **qos-group** (*none*；預設：**none**) | 從 QoS group 選單定義的 QoS 群組。 |
| **set-customer-vid-for** (*all \| none \| tagged \| untagged-or-priority-tagged*；預設：**all**) | 針對不同封包類型的 customer VLAN ID 指派指令。 |
| **set-qos-for** (*all \| none \| tagged \| untagged-or-priority-tagged*；預設：**none**) | QoS 指派指令適用的訊框類型。 |
| **set-service-vid-for** (*all \| none \| tagged \| untagged-or-priority-tagged*；預設：**all**) | 針對不同封包類型的 service VLAN ID 指派指令。 |

### 以 MAC 為基礎的 VLAN {#mac-based-vlan}

MAC Based VLAN 表用於根據來源 MAC 指派 VLAN。

**子選單：** `/interface/ethernet/switch/mac-based-vlan`

| 屬性 | 說明 |
| :-- | :-- |
| **disabled** (*yes \| no*；預設：**no**) | 啟用或停用 MAC Based VLAN 項目。 |
| **new-customer-vid** (*0..4095*；預設：**0**) | 新的 customer VLAN ID 會取代符合條件封包的原始 service VLAN ID。若設為 4095，則捨棄流量。 |
| **new-service-vid** (*0..4095*；預設：**0**) | 新的 service VLAN ID 會取代符合條件封包的原始 service VLAN ID。 |
| **src-mac-address** (*MAC address*) | MAC based VLAN 規則符合的來源 MAC 位址。 |

:::warning
所有 CRS1xx/2xx 系列交換器最多支援 1024 筆 MAC Based VLAN 表項目。
:::

### 1:1 VLAN 交換 {#11-vlan-switching}

1:1 VLAN switching 可用於取代符合封包的一般 L2 橋接。當封包命中 1:1 VLAN switching 表項目時，系統會將該項目中的目的埠資訊指派給封包。UFDB 與 MFDB 項目中符合的目的資訊不再適用於該封包。

**子選單：** `/interface/ethernet/switch/one2one-vlan-switching`

| Property | Description |
| :-- | :-- |
| **customer-vid** (*0..4095*; Default: **0**) | 用於 1:1 VLAN switching 的符合客戶 VLAN id。 |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用 1:1 VLAN switching 表項目。 |
| **dst-port** (*port*) | 符合 1:1 VLAN switching 封包的目的埠。 |
| **service-vid** (*0..4095*; Default: **0**) | 用於 1:1 VLAN switching 的符合客戶 VLAN id。 |

## 埠隔離／洩漏 {#port-isolationleakage}

---

CRS 交換器支援彈性的多層級隔離功能，可用於使用者存取控制、流量工程，以及進階安全與網路管理。隔離功能提供有序的架構結構，讓使用者可依埠、MAC 位址、VLAN、協定、流量與訊框類型輕鬆設定並控制存取。支援下列隔離與洩漏功能：

- 埠層級隔離
- MAC 層級隔離
- VLAN 層級隔離
- 協定層級隔離
- 流量層級隔離
- 上述功能的自由組合

埠層級隔離支援在來源埠與目的埠上使用不同的控制方案。每個項目都可針對來源埠或目的埠設定存取控制。

- 當項目設定為來源埠存取控制時，該項目為。

套用至入口封包。

- 當項目設定為目的地埠存取控制時，該項目

會套用至出口封包。

連接埠洩漏可略過連接埠上的出口 VLAN 過濾。洩漏連接埠可存取其他連接埠，用於安全性、網路控制及管理等各種應用。注意：當同一個連接埠同時套用隔離與洩漏時，該連接埠會被隔離。

**子選單：** `/interface/ethernet/switch/port-isolation`

**子選單：** `/interface/ethernet/switch/port-leakage`

| 屬性 | 說明 |
| :-- | :-- |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用連接埠隔離／洩漏項目。 |
| **flow-id** (*0..63*; Default: **none**) |  |
| **forwarding-type** (*bridged; routed*; Default: **bridged,routed**) | 比對 Cloud Router Switch 上的流量轉送類型。 |
| **mac-profile** (*community1 \| community2 \| isolated \| promiscuous*; Default: **none**) | 比對 MAC 隔離／洩漏設定檔。 |
| **port-profile** (*0..31*; Default: **none**) | 比對連接埠隔離／洩漏設定檔。 |
| **ports** (*ports*; Default: **none**) | 已隔離／洩漏的連接埠。 |
| **protocol-type** (*arp; nd; dhcpv4; dhcpv6; ripv1*; Default: **arp,nd,dhcpv4,dhcpv6,ripv1**) | 包含在隔離／洩漏中的協定。 |
| **registration-status** (*known; unknown*; Default: **known,unknown**) | 比對封包的註冊狀態。已知項目存在於 UFDB 與 MFDB 中，未知項目則不存在。 |
| **traffic-type** (*unicast; multicast; broadcast*; Default: **unicast,multicast,broadcast**) | 比對流量類型。 |
| **type** (*dst \| src*; Default: **src**) | 隔離／洩漏項目的查閱類型：<ul class="bullets"><li>src - 項目套用至連接埠的入口封包。</li><li>dst - 項目套用至連接埠的出口封包。</li></ul> |
| **vlan-profile** (*community1 \| community2 \| isolated \| promiscuous*; Default: **none**) | 比對 VLAN 隔離／洩漏設定檔。 |

## Trunking

---

Cloud Router Switch 中的 Trunking 提供靜態鏈路彙總群組，並具備硬體自動容錯移轉與負載平衡。不支援與 IEEE802.3ad 及 IEEE802.1ax 相容的 Link Aggregation Control Protocol。最多支援 8 個 Trunk 群組，每個 Trunk 群組最多支援 8 個 Trunk 成員連接埠。CRS Port Trunking 會根據下列所有參數計算 transmit-hash：L2 src-dst MAC + L3 src-dst IP + L4 src-dst Port。

**子選單：** `/interface/ethernet/switch/trunk`

| 屬性 | 說明 |
| :-- | :-- |
| **disabled** (*yes \| no*；預設：**no**) | 啟用或停用連接埠 trunk 項目。 |
| **member-ports** (*ports*) | Trunk 群組的成員埠。 |
| **name** (*string value*；預設：**trunkX**) | Trunk 群組的名稱。 |

## 服務品質 {#quality-of-service}

---

### Shaper

流量整形會限制從介面傳送出去的流量速率與突發大小。整形器以權杖桶實作。若封包超過最大速率或突發大小，表示沒有足夠的權杖可供封包使用，封包會存放在緩衝區中，直到有足夠的權杖可傳送為止。

**子選單：** `/interface/ethernet/switch/shaper`

| 屬性 | 說明 |
| :-- | :-- |
| **burst** (*integer*；預設：**100k**) | 允許突發時可傳送的最大資料速率。 |
| **disabled** (*yes \| no*；預設：**no**) | 啟用或停用流量整形器項目。 |
| **meter-unit** (*bit \| packet*；預設：**bit**) | 流量整形器速率的測量單位。 |
| **port** (*port*) | 流量整形器的實體埠。 |
| **rate** (*integer*；預設：**1M**) | 最大資料速率限制。 |
| **target** (*port \| queueX \| wrr-groupX*；預設：**port**) | 每個埠（包括 CPU 埠）支援三層整形器：<ul class="bullets"><li>埠層級 - 項目套用至交換器晶片的埠。</li><li>WRR 群組層級 - 項目套用至埠上 2 個加權循環佇列群組之一（wrr-group0、wrr-group1）。</li><li>佇列層級 - 項目套用至埠上 8 個佇列之一（queue0 - queue7）。</li></ul> |

### 入口埠管制器 {#ingress-port-policer}

**子選單：** `/interface/ethernet/switch/ingress-port-policer`

| 屬性 | 說明 |
| :-- | :-- |
| **burst** (*integer*; 預設: **100k**) | 允許突發時可傳輸的最大資料速率。 |
| **disabled** (*yes \| no*; 預設: **no**) | 啟用或停用 ingress 埠 policer 項目。 |
| **meter-len** (*layer-1 \| layer-2 \| layer-3*; 預設: **layer-1**) | 用於設定計量封包位元組長度的封包分類。<ul class="bullets"><li>layer-1 - 包含整個 layer-2 訊框 + FCS + 封包間隔 + 前導碼。</li><li>layer-2 - 包含 layer-2 訊框 + FCS。</li><li>layer-3 - 只包含 layer-3 + Ethernet 填充，不含 layer-2 標頭與 FCS。</li></ul> |
| **meter-unit** (*bit \| packet*; 預設: **bit**) | 流量 ingress 埠 policer 速率的計量單位。 |
| **new-dei-for-yellow** (*0..1 \| remap*; 預設: **none**) | 當 yellow-action 為 remark 時，超出流量重新標記的 DEI。 |
| **new-dscp-for-yellow** (*0..63 \| remap*; 預設: **none**) | 當 yellow-action 為 remark 時，超出流量重新標記的 DSCP。 |
| **new-pcp-for-yellow** (*0..7 \| remap*; 預設: **none**) | 當 yellow-action 為 remark 時，超出流量重新標記的 PCP。 |
| **packet-types** (*packet-types*; 預設: **all types from the description**) | ingress 埠 policer 項目有效的相符封包類型。 |
| **port** (*port*) | ingress 埠 policer 項目的實體埠或 trunk。 |
| **rate** (*integer*) | 最大資料速率限制。 |
| **yellow-action** (*drop \| forward \| remark*; 預設: **drop**) | 對超出流量執行的動作。 |

### QoS 群組 {#qos-group}

全域 QoS 群組表用於設定以 VLAN、Protocol 與 MAC 為基礎的 QoS 群組指派。

**子選單：** `/interface/ethernet/switch/qos-group`

| 屬性 | 說明 |
| :-- | :-- |
| **dei** (*0..1*; 預設: **none**) | QoS 群組的新 DEI 值。 |
| **disabled** (*yes \| no*; 預設: **no**) | 啟用或停用 protocol QoS 群組項目。 |
| **drop-precedence** (*drop \| green \| red \| yellow*; 預設: **green**) | Drop precedence 是用於封包排入佇列或丟棄的內部 QoS 屬性。 |
| **dscp** (*0..63*; 預設: **none**) | QoS 群組的新 DSCP 值。 |
| **name** (*string value*; 預設: **groupX**) | QoS 群組的名稱。 |
| **pcp** (*0..7*; 預設: **none**) | QoS 群組的新 PCP 值。 |
| **priority** (*0..15*; 預設: **0**) | 內部優先順序在本機具有意義，用於將流量分類到埠上的不同 egress 佇列。（1 為最高，15 為最低） |

### DSCP QoS 對應 {#dscp-qos-map}

全域 DSCP 至 QOS 對應表用於將封包的 DSCP 對應至表中設定的新 QoS 屬性。

**子選單：** `/interface/ethernet/switch/dscp-qos-map`

| 屬性 | 說明 |
| :-- | :-- |
| **dei** (*0..1*) | DSCP 至 QOS 對應項目的新 DEI 值。 |
| **drop-precedence** (*drop \| green \| red \| yellow*) | DSCP 至 QOS 對應項目的新 Drop precedence 值。 |
| **pcp** (*0..7*) | DSCP 至 QOS 對應項目的新 PCP 值。 |
| **priority** (*0..15*) | DSCP 至 QOS 對應項目的新內部優先順序值。 |

### DSCP 對應 DSCP 的對應表 {#dscp-to-dscp-map}

全域 DSCP 至 DSCP 對應表用於將封包的原始 DSCP 對應至表中設定的新 DSCP 值。

**子選單：** `/interface/ethernet/switch/dscp-to-dscp`

| 屬性 | 說明 |
| :-- | :-- |
| **new-dscp** (*0..63*) | DSCP 至 DSCP 對應項目的新 DSCP 值。 |

### Policer QoS 對應 {#policer-qos-map}

**子選單：** `/interface/ethernet/switch/policer-qos-map`

| 屬性 | 說明 |
| :-- | :-- |
| **dei-for-red** (*0..1*；預設：**0**) | 紅色封包的 Policer DEI 重新對應值。 |
| **dei-for-yellow** (*0..1*；預設：**0**) | 黃色封包的 Policer DEI 重新對應值。 |
| **dscp-for-red** (*0..63*；預設：**0**) | 紅色封包的 Policer DSCP 重新對應值。 |
| **dscp-for-yellow** (*0..63*；預設：**0**) | 黃色封包的 Policer DSCP 重新對應值。 |
| **pcp-for-red** (*0..7*；預設：**0**) | 紅色封包的 Policer PCP 重新對應值。 |
| **pcp-for-yellow** (*0..7*；預設：**0**) | 黃色封包的 Policer PCP 重新對應值。 |

## 存取控制清單 {#access-control-list}

---

存取控制清單由 ingress policy 與 egress policy 引擎組成，可設定最多 128 條 policy 規則（受 RouterOS 限制）。這是一項進階工具，可依據 Layer2、Layer3 與 Layer4 通訊協定標頭欄位條件，進行線速封包過濾、轉送、整形與修改。

:::info
請參閱 Summary 章節，以取得支援存取控制清單的 Cloud Router Switch 設備。
:::

:::danger
受限於硬體限制，無法比對特定埠上的 broadcast/multicast 流量。你應該使用連接埠隔離、在 ingress 埠上丟棄流量，或使用 VLAN 過濾，以避免特定 broadcast/multicast 流量被轉送。
:::

**子選單：** `/interface/ethernet/switch/acl`

### 封包 MAC 相關欄位的 ACL 條件部分 {#acl-condition-part-for-mac-related-fields-of-packets}

| 屬性 | 說明 |
| :-- | :-- |
| **disabled** (*yes \| no*; Default: **no**) | 啟用或停用 ACL 項目。 |
| **table** (*egress \| ingress*; Default: **ingress**) | 選取傳入或傳出封包的 policy 表。 |
| **invert-match** (*yes \| no*; Default: **no**) | 反轉整條 ACL 規則的比對結果。 |
| **src-ports** (*ports,trunks*) | 比對實體來源埠或 trunk。 |
| **dst-ports** (*ports,trunks*) | 比對實體目的埠或 trunk。受限於硬體限制，無法在 egress 埠上比對 broadcast/multicast 流量。 |
| **mac-src-address** (*MAC address/Mask*) | 來源 MAC 位址與遮罩。 |
| **mac-dst-address** (*MAC address/Mask*) | 目的 MAC 位址與遮罩。 |
| **dst-addr-registered** (*yes \| no*) | 定義是否比對處於 registered 狀態的封包，也就是目的 MAC 位址位於 UFDB/MFDB/RFDB 中的封包。僅在 egress 表中有效。 |
| **mac-protocol** (*802.2 \| arp \| homeplug-av \| ip \| ip-or-ipv6 \| ipv6 \| ipx \| lldp \| loop-protect \| mpls-multicast \| mpls-unicast \| mvrp \| non-ip \| packing-compr \| packing-simple \| pppoe \| pppoe-discovery \| rarp \| service-vlan \| vlan or integer: 0..65535 decimal format or 0x0000-0xffff hex format*) | Ethernet payload 類型（MAC 層通訊協定）<ul><li><strong>802.2</strong> - 802.2 Frames (0x0004)</li><li><strong>arp</strong> - Address Resolution Protocol (0x0806)</li><li><strong>capsman</strong> - CAPsMAN 與 CAP 之間的 MAC 層連線 (0x88BB)</li><li><strong>dot1x</strong> - EAPoL IEEE 802.1X (0x888E)</li><li><strong>homeplug-av</strong> - HomePlug AV MME (0x88E1)</li><li><strong>ip</strong> - Internet Protocol version 4 (0x0800)</li><li><strong>ip-or-ipv6</strong> - IPv4 或 IPv6 (0x0800 或 0x86DD)</li><li><strong>ipv6</strong> - Internet Protocol Version 6 (0x86DD)</li><li><strong>ipx</strong> - Internetwork Packet Exchange (0x8137)</li><li><strong>lacp</strong> - Link Aggregation Control Protocol (0x8809)</li><li><strong>lldp</strong> - Link Layer Discovery Protocol (0x88CC)</li><li><strong>loop-protect</strong> - Loop Protect Protocol (0x9003)</li><li><strong>macsec</strong> - MAC security IEEE 802.1AE (0x88E5)</li><li><strong>mpls-multicast</strong> - MPLS multicast (0x8848)</li><li><strong>mpls-unicast</strong> - MPLS unicast (0x8847)</li><li><strong>mvrp</strong> - Multiple VLAN Registration protocol (0x88F5)</li><li><strong>non-ip</strong> - 非 Internet Protocol version 4（非 0x0800）</li><li><strong>packing-compr</strong> - 使用壓縮 <a href="/docs/system-information-and-utilities/ip-packing">IP packing</a> 封裝的封包 (0x9001)</li><li><strong>packing-simple</strong> - 使用簡單 <a href="/docs/system-information-and-utilities/ip-packing">IP packing</a> 封裝的封包 (0x9000)</li><li><strong>pppoe</strong> - PPPoE Session Stage (0x8864)</li><li><strong>pppoe-discovery</strong> - PPPoE Discovery Stage (0x8863)</li><li><strong>rarp</strong> - Reverse Address Resolution Protocol (0x8035)</li><li><strong>romon</strong> - Router Management Overlay Network RoMON (0x88BF)</li><li><strong>service-vlan</strong> - Provider Bridging (IEEE 802.1ad) &amp; Shortest Path Bridging IEEE 802.1aq (0x88A8)</li><li><strong>vlan</strong> - VLAN-tagged frame (IEEE 802.1Q) 以及具 NNI 相容性的 Shortest Path Bridging IEEE 802.1aq (0x8100)</li></ul> |
| **drop-precedence** (*drop \| green \| red \| yellow*) | 比對內部 drop precedence。僅在 egress 表中有效。 |
| **custom-fields** |  |

### 封包 VLAN 相關欄位的 ACL 條件部分 {#acl-condition-part-for-vlan-related-fields-of-packets}

| Property | Description |
| :-- | :-- |
| **lookup-vid** (*0..4095*) | 用於查閱的 VLAN ID。可在抵達 egress 表之前變更。 |
| **service-vid** (*0-4095*) | 要比對的 service VLAN ID。 |
| **service-pcp** (*0..7*) | 要比對的 service PCP。 |
| **service-dei** (*0..1*) | 要比對的 service DEI。 |
| **service-tag** (*priority-tagged \| tagged \| tagged-or-priority-tagged \| untagged*) | service tag 的格式。 |
| **customer-vid** (*0-4095*) | 要比對的 customer VLAN ID。 |
| **customer-pcp** (*0..7*) | 要比對的 customer PCP。 |
| **customer-dei** (*0..1*) | 要比對的 customer DEI。 |
| **customer-tag** (*priority-tagged \| tagged \| tagged-or-priority-tagged \| untagged*) | customer tag 的格式。 |
| **priority** (*0..15*) | 要比對的內部優先順序。僅在 egress 表中有效。 |

### 封包 IPv4 與 IPv6 相關欄位的 ACL 條件部分 {#acl-condition-part-for-ipv4-and-ipv6-related-fields-of-packets}

| Property | Description |
| :-- | :-- |
| **ip-src** (*IPv4/0..32*) | 要比對的來源 IPv4 位址。 |
| **ip-dst** (*IPv4/0..32*) | 要比對的目的 IPv4 位址。 |
| **ip-protocol** (*tcp \| udp \| udp-lite \| other*) | IP 協定類型。 |
| **src-l3-port** (*0-65535*) | 要比對的 Layer3 來源埠。 |
| **dst-l3-port** (*0-65535*) | 要比對的 Layer3 目的埠。 |
| **ttl** (*0 \| 1 \| max \| other*) | 要比對封包的 TTL 欄位。 |
| **dscp** (*0..63*) | 要比對封包的 DSCP 欄位。 |
| **ecn** (*0..3*) | 要比對封包的 ECN 欄位。 |
| **fragmented** (*yes \| no*) | 是否比對已分片的封包。 |
| **first-fragment** (*yes \| no*) | YES 比對未分片封包與第一個分片，NO 比對其他分片。 |
| **ipv6-src** (*IPv6/0..128*) | 要比對的來源 IPv6 位址。 |
| **ipv6-dst** (*IPv6/0..128*) | 要比對的目的 IPv6 位址。 |
| **mac-isolation-profile** (*community1 \| community2 \| isolated \| promiscuous*) | 根據 UFDB 比對 isolation profile。僅在 egress policy 表中有效。 |
| **src-mac-addr-state** (*dynamic-station-move \| sa-found \| sa-not-found \| static-station-move*) | 定義是否比對具有已登錄狀態的封包，也就是目的 MAC 位址位於 UFDB/MFDB/RFDB 中的封包。僅在 egress policy 表中有效。 |
| **flow-id** (*0..63*) |  |

### ACL 規則動作部分 {#acl-rule-action-part}

| Property | Description |
| :-- | :-- |
| <strong>action</strong> (<em>copy-to-cpu &#124; drop &#124; forward &#124;</em><em>redirect-to-cpu &#124; send-to-new-dst-ports</em>; Default: <br/><strong>forward</strong>) | <ul class="bullets"><li>copy-to-cpu - 若封包符合 ACL 條件，則將封包複製到 CPU。</li><li>drop - 若封包符合 ACL 條件，則捨棄封包。</li><li>forward - 若封包符合 ACL 條件，則轉送封包。</li><li>redirect-to-cpu - 若封包符合 ACL 條件，則將封包重新導向到 CPU。</li><li>send-to-new-dst-ports - 若封包符合 ACL 條件，則將封包傳送到新的目的埠。</li></ul> |
| **new-dst-ports** (*ports,trunks*) | 若動作為「send-to-new-dst-ports」，此屬性會設定哪些 ports/trunks 做為新的目的端。 |
| **mirror-to** (*mirror0 \| mirror1*) | ACL 封包的鏡像目的端。 |
| **policer** (*policer*) | 套用至 ACL 封包的 ACL Policer。 |
| **src-mac-learn** (*yes \| no*) | 是否學習符合 ACL 封包的來源 MAC。僅在 ingress policy 表中有效。 |
| **new-service-vid** (*0..4095*) | ACL 封包的新 service VLAN ID。 |
| **new-service-pcp** (*0..7*) | ACL 封包的新 service PCP。 |
| **new-service-dei** (*0..1*) | ACL 封包的新 service DEI。 |
| **new-customer-vid** (*0..4095*) | ACL 封包的新 customer VLAN ID。若設為 4095，則流量會被捨棄。 |
| **new-customer-pcp** (*0..7*) | ACL 封包的新 customer PCP。 |
| **new-customer-dei** (*0..1*) | ACL 封包的新 customer DEI。 |
| **new-dscp** (*0..63*) | ACL 封包的新 DSCP。 |
| **new-priority** (*0..15*) | ACL 封包的新內部優先順序。 |
| **new-drop-precedence** (*drop \| green \| red \| yellow*) | ACL 封包的新內部捨棄優先順序。 |
| **new-registered-state** (*yes \| no*) | 是否修改封包狀態。YES 會將封包狀態設為 registered，NO 則設為 unregistered。僅在 ingress policy 表中有效。 |
| **new-flow-id** (*0..63*) |  |

### ACL 封包的篩選略過部分 {#filter-bypassing-part-for-acl-packets}

| Property | Description |
| :-- | :-- |
| **attack-filter-bypass** (*yes \| no*; Default: **no**) |  |
| **ingress-vlan-filter-bypass** (*yes \| no*; Default: **no**) | 允許對符合條件的封包略過 VLAN 表中的 ingress VLAN 篩選。這僅適用於 ingress policy 表。 |
| **egress-vlan-filter-bypass** (*yes \| no*; Default: **no**) | 允許對符合條件的封包略過 VLAN 表中的 egress VLAN 篩選。這僅適用於 ingress policy 表。 |
| **isolation-filter-bypass** (*yes \| no*; Default: **no**) | 允許對符合條件的封包略過 Isolation 表。這僅適用於 ingress policy 表。 |
| **egress-vlan-translate-bypass** (*yes \| no*; Default: **no**) | 允許對符合條件的封包略過 egress VLAN translation 表。 |

### ACL Policer

**子選單：** `/interface/ethernet/switch/acl/policer`

| Property | Description |
| :-- | :-- |
| **name** (*string*; Default: **policerX**) | ACL 中使用的 Policer 名稱。 |
| **yellow-rate** (*integer*) | 具有 yellow drop precedence 的封包之最大資料速率限制。 |
| **yellow-burst** (*integer*; Default: **0**) | 當具有 yellow drop precedence 的封包允許突發時，可傳輸的最大資料速率。 |
| **red-rate** (*integer*; Default: **0**) | 具有 red drop precedence 的封包之最大資料速率限制。 |
| **red-burst** (*integer*; Default: **0**) | 當具有 red drop precedence 的封包允許突發時，可傳輸的最大資料速率。 |
| **meter-unit** (*bit \| packet*; Default: **bit**) | ACL 流量速率的計量單位。 |
| **meter-len** (*layer-1 \| layer-2 \| layer-3*; Default: **layer-1**) | 設定用於計量之封包位元組長度的封包分類。<ul class="bullets"><li>layer-1 - 包含整個 layer-2 frame + FCS + inter-packet gap + preamble。</li><li>layer-2 - 包含 layer-2 frame + FCS。</li><li>layer-3 - 僅包含 layer-3 + ethernet padding，不含 layer-2 header 與 FCS。</li></ul> |
| **color-awareness** (*yes \| no*; Default: **no**) | YES 會讓 policer 考量預先標記的 drop precedence，NO 則忽略 drop precedence。 |
| **bucket-coupling** (*yes \| no*; Default: **no**) |  |
| **yellow-action** (*drop \| forward \| remark*; Default: **drop**) | 對具有 yellow drop precedence 的超出流量執行的動作。 |
| **new-dei-for-yellow** (*0..1 \| remap*) | 具有 yellow drop precedence 的封包之新 DEI。 |
| **new-pcp-for-yellow** (*0..7 \| remap*) | 具有 yellow drop precedence 的封包之新 PCP。 |
| **new-dscp-for-yellow** (*0..63 \| remap*) | 具有 yellow drop precedence 的封包之新 DSCP。 |
| **red-action** (*drop \| forward \| remark*; Default: **drop**) | 對具有 red drop precedence 的超出流量執行的動作。 |
| **new-dei-for-red** (*0..1 \| remap*) | 具有 red drop precedence 的封包之新 DEI。 |
| **new-pcp-for-red** (*0..7 \| remap*) | 具有 red drop precedence 的封包之新 PCP。 |
| **new-dscp-for-red** (*0..63 \| remap*) | 具有 red drop precedence 的封包之新 DSCP。 |

## 另請參閱 {#see-also}

---

- [CRS1xx/2xx series switches examples](/docs/bridging-and-switching/user-guides/crs1xx-2xx-series-switches-examples)
- [Basic VLAN switching](/docs/bridging-and-switching/user-guides/basic-vlan-switching)
- [Bridge Hardware Offloading](/docs/bridging-and-switching/crs1xx-and-2xx-series-switches#bridge-hardware-offloading)
- [Spanning Tree Protocol](/docs/bridging-and-switching/user-guides/spanning-tree-protocol)
- [IGMP Snooping](/docs/bridging-and-switching/user-guides/bridge-igmp-mld-snooping)
- [DHCP Snooping and Option 82](/docs/bridging-and-switching/crs1xx-and-2xx-series-switches#dhcp-snooping-and-dhcp-option-82)
- [MTU on RouterBOARD](/docs/hardware/mtu-in-routeros)
- [Layer2 misconfiguration](/docs/bridging-and-switching/user-guides/layer2-misconfiguration)
