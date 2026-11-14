---
sidebar_key: "bridging-and-switching/index"
sidebar_position: 12
title: "橋接與交換"
sidebar_label: "橋接與交換"
tags:
  - 'bridging'
  - 'stp'
  - 'arp'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching
captured_at: '2026-11-04T11:27:55+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

---

![Bridge diagram](/img/341670d0f71b9c56.webp)

類似乙太網的網路（Ethernet、Ethernet over IP、ap-bridge 或 bridge 模式下的 IEEE 802.11、WDS、VLAN）可以使用 MAC 網橋連線在一起。網橋功能允許將連線到不同 LAN 的主機互連（使用 EoIP 時，只要它們之間存在任意型別的 IP 網路互連，地理上分散的網路也可以被橋接），就像它們連線到同一個 LAN 一樣。由於網橋是透明的，它們不會出現在 traceroute 列表中，而且如果這些 LAN 已橋接，任何工具都無法區分在一臺 LAN 中工作的主機和在另一臺 LAN 中工作的主機。但是，根據 LAN 的互連方式，主機之間的延遲和資料速率可能會有所不同。

在複雜拓撲中可能會出現網路環路（無論是有意還是無意）。如果不進行任何特殊處理，環路將阻止網路正常執行，因為它們會導致雪崩式的封包倍增。每個網橋都會執行一種演算法來計算如何防止環路。(R/M)STP 允許網橋相互通訊，因此它們可以協商出一個無環拓撲。所有其他原本會形成環路的替代連線都會處於待命狀態，以便在主連線發生故障時，另一條連線可以接替它。該演算法會定期交換配置訊息（BPDU - Bridge Protocol Data Unit），以便所有網橋都能獲得有關網路拓撲變化的最新資訊。(R/M)STP 會選擇根網橋，它負責網路重新配置，例如阻塞和開啟其他網橋上的埠。根網橋是具有最低網橋 ID 的網橋。

## 網橋介面設定 {#bridge-interface-setup}

---

要將多個網路組合到一個網橋中，應建立一個網橋介面。之後，應將所有所需的介面設定為其埠。預設情況下，網橋 MAC 地址將根據網橋埠配置自動選擇。為了避免不必要的 MAC 地址變更，建議停用 `auto-mac` 並使用 `admin-mac` 手動指定 MAC 地址。

**子選單：** `/interface/bridge`

| 屬性 | 描述 |
| :-- | :-- |
| **add-dhcp-option82** (*yes* \| *no*; 預設值：**no**) | <strong>重要：</strong> 從 <strong>RouterOS 版本 7.23</strong> 開始，此設定已被移除。現在可以使用預定義變數（例如 BRIDGEMAC、HOSTNAME、INTERFACE、VID）配置自定義 Remote ID 和 Circuit ID 值。詳情請參閱下面的 <code>dhcp-agent-circuit-id</code> 和 <code>dhcp-agent-remote-id</code> 屬性。如果此設定在早期版本（7.22 或更早）中已啟用，升級將自動把配置更新為新格式。 <br/> 是否將 DHCP Option 82 資訊（Agent Remote ID 和 Agent Circuit ID）新增到 DHCP 封包。可以與支援 Option 82 的 DHCP 伺服器一起使用來分配 IP 地址並實施策略。此屬性僅在 <code>dhcp-snooping</code> 設定為 <span className="ros-icon-success"><code>yes</code></span> 時生效。 <br/> 在 RouterOS 7.22 或更早版本中，這些值是預定義的且無法修改： <br/><ul><li>對於 Agent Remote ID，RouterOS 使用網橋介面 MAC 地址，格式為 "xx:xx:xx:xx:xx:xx"（小寫、冒號分隔）。</li><li>對於 Agent Circuit ID，RouterOS 使用 DHCP 用戶端所連線位置的介面名稱和 VLAN ID，以冒號分隔（interface:vlan-id）。僅當網橋上啟用了 <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> 時才包含 VLAN ID。</li></ul> 例如（<code>vlan-filtering=yes</code>）： <br/> Agent Remote ID - cc:2d:e0:01:6a:43 Agent Circuit ID - ether2:10 <br/> |
| **admin-mac** (*MAC address*; 預設值：**none**) | 網橋的靜態 MAC 地址。此屬性僅在 `auto-mac` 設定為 `no` 時生效。 |
| **ageing-time** (*time*; 預設值：**00:05:00**) | 主機資訊在網橋資料庫中保留多長時間。 |
| **arp** (*disabled* \| *enabled* \| *local-proxy-arp \| proxy-arp \| reply-only*; 預設值：**enabled**) | Address Resolution Protocol 設定<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 介面將不使用 ARP</li><li><span className="ros-icon-success"><code>enabled</code></span> - 介面將使用 ARP</li><li><span className="ros-icon-success"><code>local-proxy-arp</code></span> - 路由器在介面上執行代理 ARP，並向同一介面傳送回覆</li><li><span className="ros-icon-success"><code>proxy-arp</code></span> - 路由器在介面上執行代理 ARP，並向其他介面傳送回覆</li><li><span className="ros-icon-success"><code>reply-only</code></span> - 介面僅響應來自匹配 IP 地址/MAC 地址組合的請求，這些組合作為靜態條目輸入到 IP/ARP 表中。不會自動將動態條目儲存在 IP/ARP 表中。因此，為了使通訊成功，必須已經存在有效的靜態條目。</li></ul> |
| **arp-timeout** (*auto \| integer*; 預設值：**auto**) | 當一段時間內未從某個 IP 地址收到封包後，ARP 記錄在 ARP 表中保留多長時間。值 `auto` 等於 `/ip/settings` 中 `arp-timeout` 的值，預設值為 30s。 |
| **auto-mac** (*yes \| no*; 預設值：**yes**) | 當配置 <code>auto-mac=yes</code> 時，網橋將根據以下優先順序順序自動為網橋介面選擇 MAC 地址： <br/><ol><li>從屬於該網橋的 Ethernet 介面中選擇；</li><li>從網橋中的非 Ethernet 介面（例如 WiFi 或 tunnel）中選擇；</li><li>如果上述來源都不可用，則隨機生成一個地址。</li></ol> 如果配置發生變化，例如向網橋新增新埠，只有當出現更高優先順序的地址來源時，網橋的 MAC 地址才會更新。例如，如果網橋最初使用隨機生成的 MAC，隨後添加了 Ethernet 介面，則 MAC 將根據可用的最高優先順序（在本例中為 Ethernet 介面）進行更新。如果當前 MAC 與某個埠關聯，而該埠被移動到另一個網橋，網橋也會更新 MAC 地址。 <br/> 當前 MAC 地址及其優先順序會被儲存，並在重啟後重用。 <br/> 當配置 <code>auto-mac=no</code> 時，可以使用 <code>admin-mac</code> 屬性手動設定靜態 MAC 地址。 |
| **comment** (*string*; 預設值：) | 介面的簡短描述。 |
| **dhcp-agent-circuit-id** (*string*; 預設值：**!dhcp-agent-circuit-id**) | 指定透過網橋的 DHCP 訊息的 Option 82 的 <strong>Circuit ID</strong> 子選項值。字串長度限制為 255 個字元。 <br/> 此設定取代現已棄用的 <code>add-dhcp-option82</code> 屬性。如果在早期版本（7.22 或更早）中啟用了 <code>add-dhcp-option82</code>，升級將自動把配置更新為新格式：$(INTERFACE):$(VID)。透過 GUI 配置該設定時也會顯示此格式。 <br/> 支援以下變數： <br/><ul><li>$(BRIDGEMAC) - 當前網橋 MAC 地址，格式為 "xx:xx:xx:xx:xx:xx"（小寫、冒號分隔）；</li><li>$(HOSTNAME) - 系統標識；</li><li>$(INTERFACE) - DHCP 用戶端所連線的介面名稱；</li><li>$(VID) - DHCP 用戶端使用的 VLAN ID。如果 DHCP 用戶端未打標籤，VID 對應於埠的 <span className="ros-background-accent-green-bolder"><code>pvid</code></span>。僅當網橋上啟用了 <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> 時適用。</li></ul> 變數語法規則 <br/><ul><li>變數必須括在括號中，並以美元符號（$）為字首。</li><li>從終端進行配置時，美元符號必須使用反斜槓 () 轉義，否則它將被解釋為 RouterOS 指令碼變數。</li></ul> 示例： <br/><code>/interface/bridge</code><br/><code>add add-dhcp-option82=yes dhcp-agent-circuit-id="interface: \$(INTERFACE), vlan: \$(VID)" dhcp-snooping=yes name=bridge1 vlan-filtering=yes</code> 僅當 <code>dhcp-snooping</code> 設定為 yes 時，此屬性才生效。 <br/> |
| **dhcpv6-agent-circuit-id** (*string*; 預設值：**!dhcpv6-agent-circuit-id**) | 指定透過網橋的 DHCPv6 訊息的 Option 18 的 <strong>Interface ID</strong> 子選項值。<code>dhcpv6-agent-circuit-id</code> 屬性遵循與 <code>dhcp-agent-circuit-id</code> 相同的規則。 <br/> |
| **dhcp-agent-remote-id** (*string*; 預設值：**!dhcp-agent-remote-id**) | 指定透過網橋的 DHCP 訊息的 Option 82 的 <strong>Remote ID</strong> 子選項值。字串長度限制為 255 個字元。 <br/> 此設定取代現已棄用的 <code>add-dhcp-option82</code> 屬性。如果在早期版本（7.22 或更早）中啟用了 <code>add-dhcp-option82</code>，升級將自動把配置更新為新格式：$(BRIDGEMAC)。透過 GUI 配置該設定時也會顯示此格式。 <br/> 支援以下變數： <br/><ul><li>$(BRIDGEMAC) - 當前網橋 MAC 地址，格式為 "xx:xx:xx:xx:xx:xx"（小寫、冒號分隔）；</li><li>$(HOSTNAME) - 系統標識；</li><li>$(INTERFACE) - DHCP 用戶端所連線的介面名稱；</li><li>$(VID) - DHCP 用戶端使用的 VLAN ID。如果 DHCP 用戶端未打標籤，VID 對應於埠的 <span className="ros-background-accent-green-bolder"><code>pvid</code></span>。僅當網橋上啟用了 <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> 時適用。</li></ul> 變數語法規則 <br/><ul><li>變數必須括在括號中，並以美元符號（$）為字首。</li><li>從終端進行配置時，美元符號必須使用反斜槓 () 轉義，否則它將被解釋為 RouterOS 指令碼變數。</li></ul> 示例： <br/><code>/interface/bridge</code><br/><code>add add-dhcp-option82=yes dhcp-agent-remote-id="ip: 192.168.88.1, identity: \$(HOSTNAME), mac: \$(BRIDGEMAC)" dhcp-snooping=yes name=bridge1 vlan-filtering=yes</code> 僅當 <code>dhcp-snooping</code> 設定為 yes 時，此屬性才生效。 <br/> |
| **dhcpv6-agent-remote-id** (*string*; 預設值：**!dhcpv6-agent-remote-id**) | 指定透過網橋的 DHCPv6 訊息的 Option 37 的 <strong>Remote ID</strong> 子選項值。<code>dhcpv6-agent-remote-id</code> 屬性遵循與 <code>dhcp-agent-remote-id</code> 相同的規則。 <br/> |
| **dhcp-snooping** (*yes \| no*; 預設值：**no**) | 啟用或停用網橋上的 DHCP Snooping。 <br/><br/><strong>注意：</strong> 啟用 DHCP snooping 功能將關閉網橋 [fast-path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path)，進而影響透過該網橋的連線進行 [fasttrack](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fasttrack) 的能力。 <br/> |
| **dhcpv6-snooping**(*yes \| no*; 預設值：**no**) | 啟用或停用網橋上的 DHCPv6 Snooping。 <br/><br/><strong>注意：</strong> 啟用 DHCP snooping 功能將關閉網橋 [fast-path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path)，進而影響透過該網橋的連線進行 [fasttrack](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fasttrack) 的能力。 <br/> |
| **disabled** (*yes \| no*; 預設值：**no**) | 更改網橋是否被停用。 |
| **ether-type** (*0x9100 \| 0x8100 \| 0x88a8*; 預設值：**0x8100**) | 更改 EtherType，它用於確定封包是否帶有 VLAN 標籤。具有匹配 EtherType 的封包被視為已打標籤的封包。此屬性僅在 `vlan-filtering` 設定為 `yes` 時生效。 |
| **fast-forward** (*yes \| no*; 預設值：**yes**) | Fast Path 的一種特殊且更快的場景，僅在具有 2 個介面的網橋上有效（預設僅對新網橋啟用）。更多詳情可在 Fast Forward 部分找到。 |
| **forward-delay** (*time*; 預設值：**00:00:15**) | 網橋介面初始化階段（即路由器啟動或啟用介面後）在 listening/learning 狀態下花費的時間，之後網橋將開始正常執行。 |
| **forward-reserved-addresses** (*yes \| no*: 預設值：**no**) | 是否轉發位於 <strong>01:80:C2:00:00:0x</strong> 範圍內的 IEEE 保留組播 MAC 地址。符合 R/M/STP 標準的網橋應避免轉發這些封包；此屬性僅當 <code>protocol-mode</code> 設定為 <code>none</code> 時適用。 <br/> 啟用保留 MAC 地址的轉發可能會影響依賴這些地址的某些協定。建議僅在絕對必要時啟用轉發，例如在透明橋接設定中（例如擴充套件長鏈路、將網橋用作介質轉換器或進行網路分析）。 <br/> 以下是 RouterOS 使用的一些值得注意的 MAC 地址和協定： <br/><ul><li>01:80:C2:00:00:00 - [Spanning Tree Protocol (STP)](./index.md)；</li><li>01:80:C2:00:00:01 - [乙太網](../wired-connections/ethernet.md) Flow Control；</li><li>01:80:C2:00:00:02 - [Link Aggregation Control Protocol (LACP)](../high-availability-solutions/bonding.md)；</li><li>01:80:C2:00:00:03 - [Dot1x](../authentication-authorization-accounting/dot1x.md) 用戶端和伺服器；</li><li>01:80:C2:00:00:08 - Spanning Tree Protocol（對於 802.1ad 網橋，使用 <span className="ros-background-accent-green-bolder"><code>ether-type=0x88a8</code></span>）；</li><li>01:80:C2:00:00:0D - [多 VLAN 註冊協定](./index.md)（對於 802.1ad 網橋，使用 <span className="ros-background-accent-green-bolder"><code>ether-type=0x88a8</code></span>）；</li><li>01:80:C2:00:00:0E - [Link Layer Discovery Protocol](../system-information-and-utilities/neighbor-discovery.md)、[多機箱鏈路聚合組](../high-availability-solutions/multi-chassis-link-aggregation-group.md) 以及 [精確時間協定](../system-information-and-utilities/precision-time-protocol.md)；</li></ul><br/><strong>重要：</strong> Flow Control MAC 地址 01:80:C2:00:00:01 是例外；它不會被網橋轉發。 <br/> |
| **frame-types** (*admit-all \| admit-only-untagged-and-priority-tagged \| admit-only-vlan-tagged*; 預設值：**admit-all**) | 指定網橋埠上允許的幀型別。此屬性僅在 `vlan-filtering` 設定為 `yes` 時生效。 |
| **igmp-snooping** (*yes \| no*; 預設值：**no**) | 啟用組播組和埠學習，以防止組播流量泛洪到網橋中的所有介面。 |
| **igmp-version** (*2 \| 3*; 預設值：**2**) | 選擇當網橋介面充當 IGMP 查詢器時用於生成 IGMP 成員關係查詢的 IGMP 版本。此屬性僅在 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時生效。 |
| **ingress-filtering** (*yes \| no*; 預設值：**yes**) | 啟用或停用 VLAN 入口過濾，它會檢查入口埠是否為網橋 VLAN 表中接收到的 VLAN ID 的成員。預設情況下，網橋 VLAN 表中不存在的 VLAN 會在發出（egress）之前被丟棄，但此屬性允許在接收（ingress）時丟棄封包。應與 `frame-types` 一起使用，以指定入口流量應帶標籤還是不帶標籤。此屬性僅在 `vlan-filtering` 設定為 `yes` 時生效。自 RouterOS v7 起，該設定預設啟用。 |
| **l2mtu** (*read-only*; 預設值：) | L2MTU 表示此介面可以傳送的、不帶 MAC 頭的幀的最大大小。L2MTU 值將由網橋自動設定，並使用所有關聯網橋埠中最低的 L2MTU 值。此值無法手動更改。 |
| **last-member-interval** (*time*; 預設值：**1s**) | 當網橋埠上的最後一個用戶端取消訂閱某個組播組，且網橋充當活動查詢器時，網橋將傳送特定於該組的 IGMP/MLD 查詢，以確保沒有其他用戶端仍在訂閱。該設定會更改這些查詢的響應時間。如果在特定時間段（<code>last-member-interval</code> * <code>last-member-query-count</code>）內未收到成員關係報告，則會從組播資料庫（MDB）中移除該組播組。 <br/> 如果網橋埠配置了 fast-leave，則會立即移除組播組，而不傳送任何查詢。 <br/> 此屬性僅在 <code>igmp-snooping</code> 和 <code>multicast-querier</code> 設定為 <span className="ros-icon-success"><code>yes</code></span> 時生效。 |
| **last-member-query-count** (*integer: 0..4294967295*; 預設值：**2**) | `last-member-interval` 應經過多少次後，IGMP/MLD snooping 網橋才停止轉發某個組播流。此屬性僅在 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時生效。 |
| **max-hops** (*integer: 6..40*; 預設值：**20**) | 在啟用了 MSTP 的同一區域網路中，BPDU 在被忽略之前可以經過的網橋數量。此屬性僅在 `protocol-mode` 設定為 `mstp` 時生效。 |
| **max-learned-entries** (*integer: 0..4294967295 \| auto \| unlimited*; 預設值：**auto**) | 設定網橋介面可學習主機的最大數量。預設值為 <span className="ros-icon-success"><code>auto</code></span>，它取決於已安裝的 RAM 容量。可以設定高於預設值的值，或選擇 <code>unlimited</code> 選項，但這會增加記憶體耗盡的風險。 <br/> 特定 RAM 容量對應的預設值： <br/><ul><li>64 MB 為 8192；</li><li>128 MB 為 16384；</li><li>256 MB 為 32768；</li><li>512 MB 為 65536；</li><li>1024 MB 或更高為 131072。</li></ul> 此限制專門適用於網橋介面，而不是交換器 FDB 表上的硬體限制。即使達到了網橋限制，交換器仍可以繼續學習主機，直到達到其硬體限制，並做出正確的轉發決策。但是，這些額外的主機不會顯示在 <code>/interface/bridge/host</code> 表中，也無法被監控。此外，達到此限制可能會影響 MLAG 主機同步。 <br/> 此設定自 RouterOS 版本 7.16 起可用。 |
| **max-message-age** (*time: 6s..40s*; 預設值：**00:00:20**) | 更改根網橋傳輸的 BPDU 封包中的 Max Age 值。根網橋傳送 BPDU 時，將 Max Age 設定為 `max-message-age` 值，並將 Message Age 設定為 0。每個後續網橋在傳送其 BPDU 之前都會遞增 Message Age。一旦網橋收到 Message Age 等於或大於 Max Age 的 BPDU，該 BPDU 將被忽略。此屬性僅在 `protocol-mode` 設定為 `stp` 或 `rstp` 時生效。 |
| **membership-interval** (*time*; 預設值：**4m20s**) | 如果在網橋埠上未收到 IGMP/MLD 成員關係報告，組播資料庫（MDB）中的條目在多長時間後被移除。此屬性僅在 `igmp-snooping` 設定為 `yes` 時生效。 |
| **mld-version** (*1 \| 2*; 預設值：**1**) | 選擇當網橋介面充當 MLD 查詢器時用於生成 MLD 成員關係查詢的 MLD 版本。此屬性僅在網橋具有活動 IPv6 地址、`igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時生效。 |
| **mtu** (*integer*; 預設值：**auto**) | 最大傳輸單元。預設情況下，網橋將自動設定 MTU，並使用所有關聯網橋埠中最低的 MTU 值。未新增任何網橋埠時，預設網橋 MTU 值為 1500。可以手動設定 MTU 值，但它不能超過網橋 L2MTU 或最低的網橋埠 L2MTU。如果新增的新網橋埠 L2MTU 小於網橋的 <code>actual-mtu</code>（由 <code>mtu</code> 屬性設定），則手動設定的值將被忽略，網橋將表現得如同設定了 <code>mtu=auto</code>。 <br/> 在網橋上新增 VLAN 介面時，如果 VLAN 使用的 MTU 高於預設值 1500，建議手動設定網橋的 MTU。 |
| **multicast-querier** (*yes \| no*; 預設值：**no**) | 組播查詢器會生成周期性 IGMP/MLD 通用成員關係查詢，所有支援 IGMP/MLD 的裝置都會以 IGMP/MLD 成員關係報告進行響應。通常，PIM（組播）路由器或 IGMP 代理會生成這些查詢。 <br/> 透過使用此屬性，可以使啟用了 IGMP/MLD snooping 的網橋生成 IGMP/MLD 通用成員關係查詢。當 Layer2 網路中沒有活動查詢器（PIM 路由器或 IGMP 代理）時，應使用此屬性。如果 Layer2 網路中沒有組播查詢器，組播資料庫（MDB）將不會更新；已學習的條目將超時，IGMP/MLD snooping 將無法正常工作。 <br/> 僅生成不帶標籤的 IGMP/MLD 通用成員關係查詢。IGMP 查詢使用網橋介面自身的 IPv4 地址作為源地址傳送（參見 <code>querier-uses-bridge-address</code>），MLD 查詢使用網橋介面的 IPv6 鏈路本地地址傳送。如果檢測到外部 IGMP/MLD 查詢器，網橋將不會發送查詢（參見監控值 <code>igmp-querier</code> 和 <code>mld-querier</code>）。 <br/> 此屬性僅在 <code>igmp-snooping</code> 設定為 <span className="ros-icon-success"><code>yes</code></span> 時生效。 |
| **multicast-router** (*disabled \| permanent \| temporary-query*; 預設值：**temporary-query**) | 組播路由器埠是連線組播路由器或查詢器的埠。未註冊的組播流和 IGMP/MLD 成員關係報告將傳送到該埠。此設定會更改網橋介面自身的組播路由器狀態。此屬性可用於將 IGMP/MLD 成員關係報告發送到網橋介面，以便進一步進行組播路由或代理。此屬性僅在 <code>igmp-snooping</code> 設定為 <span className="ros-icon-success"><code>yes</code></span> 時生效。<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 網橋介面上停用組播路由器狀態。無論網橋介面上配置了什麼，未註冊的組播和 IGMP/MLD 成員關係報告都不會發送到網橋介面。</li><li><span className="ros-icon-success"><code>permanent</code></span> - 網橋介面上啟用組播路由器狀態。無論網橋介面上配置了什麼，未註冊的組播和 IGMP/MLD 成員關係報告都會發送到網橋介面自身。</li><li><span className="ros-icon-success"><code>temporary-query</code></span> - 使用 IGMP/MLD 查詢自動檢測網橋介面上的組播路由器狀態。</li></ul> |
| **name** (*text*; 預設值：**bridgeN**) | 網橋介面的名稱。 |
| **port-cost-mode** (*long \| short*; 預設值：**long**) | 更改橋接埠的埠路徑開銷和內部路徑開銷模式，利用基於介面速度的自動值。此設定不會影響手動配置了 <code>path-cost</code> 或 <code>internal-path-cost</code> 屬性的橋接埠。以下示例說明了與特定資料速率對應的路徑開銷（中間速率按比例計算）： <br/><details><summary>Path-cost 表</summary><table><thead><tr><th>資料速率</th><th>Long</th><th>Short</th></tr></thead><tbody><tr><td>10 Mbps</td><td>2,000,000</td><td>100</td></tr><tr><td>100 Mbps</td><td>200,000</td><td>19</td></tr><tr><td>1 Gbps</td><td>20,000</td><td>4</td></tr><tr><td>10 Gbps</td><td>2,000</td><td>2</td></tr><tr><td>25 Gbps</td><td>800</td><td>1</td></tr><tr><td>40 Gbps</td><td>500</td><td>1</td></tr><tr><td>50 Gbps</td><td>400</td><td>1</td></tr><tr><td>100 Gbps</td><td>200</td><td>1</td></tr></tbody></table></details> 對於 HW offloaded bond 介面，應用所有繫結成員埠中最高的路徑開銷；此值不受繫結總鏈路速度的影響。 <br/> 對於虛擬介面（例如 VLAN、EoIP、VXLAN 和非 HW offloaded bond），以及 wifi、wireless 和 60GHz 介面，long 模式分配路徑開銷 20,000，short 模式分配 10。 <br/> 對於動態橋接介面（例如 wifi、wireless、PPP、VPLS），路徑開銷在 long 模式下預設為 20,000，在 short 模式下預設為 10。但是，可以透過動態向網橋新增介面的服務手動覆蓋此值，例如使用 CAPsMAN 的 <code>datapath.bridge-cost</code> 設定。 <br/> 使用 [port monitor](./index.md#bridge-port-monitoring) 觀察應用的路徑開銷。 <br/> 當 <code>protocol-mode</code> 設定為 <code>stp</code>、<code>rstp</code> 或 <code>mstp</code> 時，此屬性生效。 |
| **priority** (*integer: 0..65535 decimal format or 0x0000-0xffff hex format*; 預設值：**32768 / 0x8000**) | 網橋優先順序，由 R/STP 用於確定根網橋，由 MSTP 用於確定 CIST 和 IST 區域根網橋。當 <code>protocol-mode</code> 設定為 <code>none</code> 時，此屬性無效。 <br/><strong>有效值：</strong> 網橋優先順序必須以 4096（0x1000）為步長設定。最低的 12 位會被忽略。有效值為：0x0000、0x1000、0x2000、0x3000、0x4000、0x5000、0x6000、0x7000、0x8000、0x9000、0xa000、0xb000、0xc000、0xd000、0xe000、0xf000（或其十進位制等價值：0、4096、8192、12288、16384、20480、24576、28672、32768、36864、40960、45056、49152、53248、57344、61440）。 |
| **protocol-mode** (*none \| rstp \| stp \| mstp*; 預設值：**rstp**) | 選擇 Spanning tree protocol (STP) 或 Rapid spanning tree protocol (RSTP)，以確保任何橋接 LAN 的無環拓撲。RSTP 在拓撲變化後提供更快的生成樹收斂。選擇 MSTP 以確保跨多個 VLAN 的無環拓撲。 <br/> 位於 <strong>01:80:C2:00:00:0x</strong> 範圍內的保留 MAC 地址的轉發已與 <code>protocol-mode=none</code> 分離，並且自 RouterOS v7.16 起可作為可控屬性 <code>forward-reserved-addresses</code> 使用。 |
| **pvid** (*integer: 1..4094*; 預設值：**1**) | 埠 VLAN ID（pvid）指定未打標籤的入口流量分配到哪個 VLAN。例如，它適用於從網橋 IP 傳送且目的地為網橋埠的幀。此屬性僅在 `vlan-filtering` 設定為 `yes` 時生效。 |
| **querier-interval** (*time*; 預設值：**4m15s**) | 更改檢測到的查詢器和組播路由器埠的超時時間。此屬性僅在 `igmp-snooping` 設定為 `yes` 時生效。 |
| **querier-uses-bridge-address** (*yes \| no*; 預設值：**yes**) | 啟用後，網橋 IGMP 查詢器使用網橋介面自身的 IPv4 地址作為 IGMP 查詢封包的源地址，而不是預設的 0.0.0.0。某些組播用戶端認為來自 0.0.0.0 的查詢無效並且不響應，這可能導致 snooping 表條目超時時組播流中斷。此屬性僅在 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 且網橋介面分配了 IPv4 地址時生效。此設定僅適用於 IPv4（IGMP）。MLD 查詢始終使用網橋介面的 IPv6 鏈路本地地址。 |
| **query-interval** (*time*; 預設值：**2m5s**) | 更改當網橋介面充當 IGMP/MLD 查詢器時傳送 IGMP/MLD 通用成員關係查詢的間隔。該間隔從傳送最後一個啟動查詢時開始計時。此屬性僅在 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時生效。 |
| **query-response-interval** (*time*; 預設值：**10s**) | 當網橋作為活動 IGMP/MLD 查詢器時，該設定更改通用 IGMP/MLD 查詢的響應時間。此屬性僅在 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時生效。 |
| **region-name** (*text*; 預設值：) | MSTP 區域名稱。此屬性僅在 `protocol-mode` 設定為 `mstp` 時生效。 |
| **region-revision** (*integer: 0..65535*; 預設值：**0**) | MSTP 配置修訂號。此屬性僅在 `protocol-mode` 設定為 `mstp` 時生效。 |
| **ra-guard** (*yes \| no*; 預設值：**no**) | RA guard - 一種安全功能，會根據授權可信埠列表驗證傳入的 Router Advertisement。 |
| **startup-query-count** (*integer: 0..4294967295*; 預設值：**2**) | 指定當網橋介面啟用或活動查詢器超時時，必須傳送通用 IGMP/MLD 查詢的次數。此屬性僅在 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時生效。 |
| **startup-query-interval** (*time*; 預設值：**31s250ms**) | 指定啟動通用 IGMP/MLD 查詢之間的間隔。此屬性僅在 `igmp-snooping` 和 `multicast-querier` 設定為 `yes` 時生效。 |
| **transmit-hold-count** (*integer: 1..10*; 預設值：**6**) | 埠傳輸狀態機用於限制傳輸速率的 Transmit Hold Count。 |
| **vlan-filtering** (*yes \| no*; 預設值：**no**) | 全域性啟用或停用網橋的 VLAN 功能。 |

:::danger
更改某些屬性可能導致橋接臨時停用所有埠。在生產環境中更改此類屬性時必須考慮到這一點，因為它可能導致所有封包被臨時丟棄。此類屬性包括 `vlan-filtering`、`protocol-mode`、`igmp-snooping`、`fast-forward` 等。
:::

### 示例 {#example}

以下示例演示如何為簡單的 Layer 2 交換建立並驗證一個基本網橋介面。此配置建立一個網橋，將多個 Ethernet 埠組合成單個交換網段。

```ros
[admin@MikroTik] > /interface/bridge/add
[admin@MikroTik] > interface bridge print 
Flags: X - disabled, R - running 
0 R name="bridge1" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=5E:D2:42:95:56:7F protocol-mode=rstp fast-forward=yes 
igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6 vlan-filtering=no 
dhcp-snooping=no 
```

### 網橋監控 {#bridge-monitoring}

要監控橋接介面的當前狀態，請使用 `monitor` 命令。

**子選單：** `/interface/bridge/monitor`

| 屬性 | 描述 |
| :-- | :-- |
| **bridge-id** (*priority.MAC address*) | 本地橋識別符號，格式為 bridge-priority.bridge-MAC-address。 |
| **current-mac-address** (*MAC address*) | 橋的當前 MAC 地址。 |
| **designated-port-count** (*integer*) | 指定橋埠的數量。 |
| **declared-vlan-ids** (*integer 1..4094*) | 透過 [MVRP 協定](./index.md#mvrp) 在橋接介面上宣告的 VLAN。 |
| **fast-forward** (*yes \| no*) | 橋快速轉發是否處於活動狀態。 |
| **igmp-querier** (*none* \| *interface & IPv4 address*) | 顯示檢測到的 IGMP 查詢器所在的橋埠和源 IP 地址。僅顯示檢測到的外部 IGMP 查詢器，本地橋 IGMP 查詢器（包括 IGMP proxy 和 PIM）將不會顯示。僅當啟用 `igmp-snooping` 時才會顯示該監控值。 |
| **mld-querier** (*none* \| *interface & IPv6 address*) | 顯示檢測到的 MLD 查詢器所在的橋埠和源 IPv6 地址。僅顯示檢測到的外部 MLD 查詢器，本地橋 MLD 查詢器將不會顯示。僅當啟用 `igmp-snooping` 且橋具有活動的 IPv6 地址時才會顯示該監控值。 |
| **mst-config-digest** (*integer*) | 計算得到的 VLAN 到 MST 例項 ID 對映的雜湊值。 |
| **multicast-router** (*yes \| no*) | 顯示是否在埠上檢測到組播路由器。僅當啟用 `igmp-snooping` 時才會顯示該監控值。 |
| **port-count** (*integer*) | 橋埠的數量。 |
| **regional-root-bridge-id** (*priority.MAC address*) | 區域根橋 ID，格式為 bridge-priority.bridge-MAC-address。僅當啟用 MSTP 時適用。 |
| **registered-vlan-ids** (*integer 1..4094*) | 透過 [MVRP 協定](./index.md#mvrp) 在橋接介面上註冊的 VLAN。 |
| **root-bridge** (*yes \| no*) | 顯示該橋是否為生成樹的根橋。 |
| **root-bridge-id** (*priority.MAC address*) | 根橋 ID，格式為 bridge-priority.bridge-MAC-address。 |
| **root-path-cost** (*integer*) | 到根橋路徑的總開銷。 |
| **root-port** (*name*) | 根橋所連線的埠。 |
| **state** (*enabled \| disabled*) | 橋的狀態。 |

```ros
[admin@MikroTik] /interface/bridge/monitor bridge1
                    state: enabled                         
      current-mac-address: 2C:C8:1B:FF:92:F4               
                bridge-id: 0x1000.2C:C8:1B:FF:92:F4        
              root-bridge: yes                             
           root-bridge-id: 0x1000.2C:C8:1B:FF:92:F4        
  regional-root-bridge-id: 0x1000.2C:C8:1B:FF:92:F4        
           root-path-cost: 0                               
                root-port: none                            
               port-count: 2                               
    designated-port-count: 2                               
        mst-config-digest: d2b171a8ad95f593c241fc33d419a88c
             fast-forward: no                              
         multicast-router: no                              
             igmp-querier: none                            
              mld-querier: none                            
        declared-vlan-ids: 1                               
      registered-vlan-ids: 1                               
```

## 生成樹協定 {#spanning-tree-protocol}

---

RouterOS 橋接介面能夠執行生成樹協定，以確保拓撲無環且具備冗餘性。對於僅有 2 臺橋的小型網路，STP 帶來的好處不多，但對於更大的網路，正確配置 STP 至關重要，即使僅有一臺橋發生故障，將 STP 相關值保留為預設值也可能導致網路完全不可達。要實現恰當的無環且冗餘的拓撲，必須正確設定橋優先順序、埠路徑開銷以及埠優先順序。

:::danger
在 RouterOS 中，可以將橋接優先順序設定為 0 到 65535 之間的任何值，而 IEEE 802.1W 標準規定橋接優先順序必須以 4096 為步長。這可能導致不支援此類值的裝置之間出現相容性問題。為避免相容性問題，建議僅使用以下優先順序：0、4096、8192、12288、16384、20480、24576、28672、32768、36864、40960、45056、49152、53248、57344、61440
:::

STP 有多種變體；目前 RouterOS 支援 STP、RSTP 和 MSTP。可根據需要選用其中任意一種；某些裝置能夠透過硬體解除安裝來執行其中部分協定，有關哪些裝置支援該功能的詳細資訊，請參見硬體解除安裝章節。STP 被認為是過時且緩慢的，在幾乎所有網路拓撲中它都已被 RSTP 取代，RSTP 與 STP 向後相容。對於依賴 VLAN 的網路拓撲，建議使用 MSTP，因為它是 VLAN 感知的協定，並能夠按 VLAN 組進行負載均衡。在設計啟用 STP 的網路時有許多需要考慮的事項，更詳細的案例研究可在 [生成樹協定](./user-guides/spanning-tree-protocol.md) 文章中查閱。在 RouterOS 中，`protocol-mode` 屬性控制所使用的 STP 變體。

:::info
RouterOS 橋接不支援 PVST 及其變體。PVST BPDU（目標 MAC 為 01:00:0C:CC:CC:CD）會被 RouterOS 橋接視為典型的組播封包。簡單來說，它們會經過 RouterOS 橋接/交換轉發邏輯，並可能被標記或取消標記。
:::

:::info
根據 IEEE 802.1ad 標準，符合 IEEE 802.1Q 的橋接發出的 BPDU 與 IEEE 802.1ad 橋接不相容。這意味著在單個二層域中的所有橋接上應使用相同的橋接 VLAN 協定；否則 (R/M)STP 將無法正常工作。
:::

### 每埠 STP {#per-port-stp}

在某些情況下，你可能希望限制單個或多個埠上的 STP 功能。下面你可以找到針對不同使用場景的示例。

:::danger
更改預設 (R/M)STP 功能時要小心；確保你理解 STP 和 BPDU 的工作原理。配置錯誤的 (R/M)STP 可能導致意外行為。
:::

#### 建立邊緣埠 {#create-edge-ports}

邊緣埠用於連線到未連線其他網橋的終端裝置，例如工作站或路由器。將網橋埠設定為邊緣埠會限制其傳送 BPDU（Bridge Protocol Data Units，橋協定資料單元），並使其忽略任何接收到的 BPDU。這允許埠直接轉換為轉發狀態，跳過標準 STP 的學習和偵聽階段，從而縮短網路收斂時間。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 edge=yes
add bridge=bridge1 interface=ether2
```

## 丟棄接收到的 BPDU {#drop-received-bpdus}

當網橋啟用了 STP/RSTP/MSTP 時，網橋防火牆的過濾規則和 NAT 規則無法丟棄 BPDU，因為 BPDU 在網橋內部會接受特殊處理。但是，在特定埠上丟棄接收到的 BPDU 可以在某些交換晶片上使用 ACL 規則實現：

在配備 Marvell Prestera 交換晶片的 MikroTik 裝置上：

```ros
/interface/ethernet/switch/rule
add dst-mac-address=01:80:C2:00:00:00/FF:FF:FF:FF:FF:FF new-dst-ports="" port=ether1 switch=switch1
```

在支援訪問控制列表（ACL）的 CRS1xx/CRS2xx 系列裝置上：

```ros
/interface/ethernet/switch/acl
add action=drop mac-dst-address=01:80:C2:00:00:00 src-ports=ether1
```

此配置會丟棄 **ether1** 上接收到的所有 BPDU。

:::danger
如果你打算在埠上丟棄接收到的 BPDU，請確保也阻止 BPDU 透過該埠所連線的介面傳送出去。根橋始終傳送 BPDU，並且通常等待更優的 BPDU（來自具有更低橋接 ID 的橋接）。但是，當從根橋過渡到指定橋接時，橋接必須臨時停用新的根埠。如果你僅在一側阻止 BPDU，埠將在狀態之間持續翻轉。
:::

#### 啟用 BPDU guard {#enable-bpdu-guard}

BPDU Guard 功能為橋接埠提供了額外的安全層。它旨在透過以下方式防止潛在的網路問題：如果埠收到 BPDU（橋協定資料單元），則將其阻塞；這表明有未經授權的橋接裝置接入。這對於僅應連線終端裝置的邊緣埠特別有用。在此示例中，如果 **ether1** 收到 BPDU，該埠將被自動阻塞，並且需要手動干預才能重新啟用。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 bpdu-guard=yes
add bridge=bridge1 interface=ether2
```

#### 啟用 Root Guard {#enable-root-guard}

Root Guard 是一種生成樹安全功能，可防止埠成為根埠，從而保護活動生成樹拓撲不受外部橋接裝置影響。在此示例中，**ether1** 配置了 `restricted-role=yes`。此設定會阻止該埠成為 CIST 或任何 MSTI 的根埠，無論其最佳生成樹優先順序向量如何。此類埠將被選為 Alternate Port（處於 discarding 狀態），並且只要它繼續收到更優的 BPDU，就會保持該狀態。當它不再檢測到更優的根路徑時，將自動轉換為轉發狀態。網路管理員可以啟用此設定，以防止外部橋接裝置影響活動生成樹。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 restricted-role=yes
add bridge=bridge1 interface=ether2
[admin@MikroTik] /interface/bridge/port/monitor [find]
                  interface: ether1                   ether2            
                     status: in-bridge                in-bridge          
                    port-id: 0x80.1                   0x80.2            
                       role: alternate-port           designated-port
                  edge-port: no                       yes           
        edge-port-discovery: yes                      yes            
        point-to-point-port: yes                      yes            
               external-fdb: no                       no             
               sending-rstp: yes                      yes            
                   learning: no                       yes            
                 forwarding: no                       yes            
           actual-path-cost: 2000                     2000           
    internal-root-path-cost: 2000                                    
       designated-bridge-id: 0x7000.64:D1:54:C7:3A:6E                
   designated-internal-cost: 0                        0              
         designated-port-id: 0x80.1                   0x80.2         
  designated-remaining-hops: 20                       20             
                 tx-rx-bpdu: 2/363                    4/1049         
        discard-transitions: 0                        0              
        forward-transitions: 0                        0              
                   tx-rx-tc: 0/2                      2/4            
           topology-changes: 0                        1              
       last-topology-change:                          34m53s         
           multicast-router: no                       yes            
           hw-offload-group: switch1                  switch1        
          declared-vlan-ids:                          
        registered-vlan-ids:                          
```

## 橋接設定 {#bridge-settings}

---

在橋接設定選單下，可以控制所有橋接介面的某些功能，並監控全域性橋接計數器。

**子選單：** `/interface/bridge/settings`

| 屬性 | 描述 |
| :-- | :-- |
| **use-ip-firewall** (*yes \| no*; 預設值: **no**) | 將橋接流量直接發往 [IP/IPv6 防火牆](../firewall-and-quality-of-service/firewall/index.md)（IP/IPv6 路由的 prerouting、forward 和 postrouting 部分，更多詳細資訊請參閱 [RouterOS 中的封包流程](../firewall-and-quality-of-service/packet-flow-in-routeros.md#flow-of-bridged-packet) 文章）。以下是啟用此設定可完成某些任務的一些用例： <br/><ul><li>如果您想為流經橋接埠的流量分配 [佇列](../firewall-and-quality-of-service/queues/index.md) 或全域性 [Queue Tree](../firewall-and-quality-of-service/queues/index.md)。</li><li>如果您想對原本會繞過 IP/IPv6 防火牆的、流經橋接埠的流量使用 IP/IPv6 防火牆功能。</li></ul><br/><strong>注意：</strong> 啟用 <code>use-ip-firewall</code> 功能將關閉橋接 [Fast Path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path)，這反過來會影響對經過該橋接的連線進行 [fasttrack](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fasttrack) 的能力。而且，由於此設定引入了額外的處理步驟（prerouting、forward 和 postrouting 鏈），在轉發封包時將進一步增加 CPU 使用率。 <br/><strong>路由流量</strong>（包括來自 VLAN 介面的流量，例如在橋接上建立的 <code>/interface/vlan</code>）<strong>已由 IP 防火牆處理</strong>。在這種情況下，啟用此設定沒有額外效果。 <br/> |
| **use-ip-firewall-for-pppoe** (*yes \| no*; 預設值: **no**) | 將橋接的未加密 PPPoE 封裝流量直接發往 IP/IPv6 防火牆。僅當 `use-ip-firewall` 設定為 `yes` 時，此屬性才生效。 |
| **use-ip-firewall-for-vlan** (*yes \| no*; 預設值: **no**) | 將橋接的 VLAN 標記流量直接發往 IP/IPv6 防火牆。僅當 <code>use-ip-firewall</code> 設定為 <span className="ros-icon-success"><code>yes</code></span> 時，此屬性才生效。 <br/> 如果您需要使用 IP/IPv6 防火牆，並且橋接 <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> 已啟用（這涉及 VLAN 標記處理），那麼還應啟用 <code>use-ip-firewall-for-vlan=yes</code>。 <br/> 啟用此設定後，當封包在 VLAN 介面之間路由時（例如 <code>/interface/vlan</code>），IP 防火牆 <strong>prerouting</strong> 鏈中的 <code>in-interface</code> 將匹配橋接介面，而不是單個 VLAN 介面。 |
| **allow-fast-path** (*yes \| no*; 預設值: **yes**) | 是否全域性啟用橋接 Fast Path。 |
| **bridge-fast-path-active** (*yes \| no*; 預設值: *)* | 顯示橋接 Fast Path 是否全域性處於活動狀態。不顯示每個橋接介面的 Fast Path 狀態。 |
| **bridge-fast-path-packets** (*integer*; 預設值: *)* | 顯示由橋接 Fast Path 轉發的封包計數。 |
| **bridge-fast-path-bytes** (*integer*; 預設值: *)* | 顯示由橋接 Fast Path 轉發的位元組計數。 |
| **bridge-fast-forward-packets** (*integer*; 預設值: *)* | 顯示由橋接 Fast Forward 轉發的封包計數。 |
| **bridge-fast-forward-bytes** (*integer*; 預設值: *)* | 顯示由橋接 Fast Forward 轉發的位元組計數。 |

:::warning
如果你希望將簡單佇列或全域性佇列樹分配給由橋接轉發的流量，則需要啟用 `use-ip-firewall` 屬性。如果不使用此屬性，橋接流量將永遠不會到達 postrouting 鏈。簡單佇列和全域性佇列樹在 postrouting 鏈中工作。要為橋接中的 VLAN 或 PPPoE 流量分配簡單佇列或全域性佇列樹，你還應啟用相應的屬性。
:::

## 埠設定 {#port-settings}

---

The Port 子選單用於將介面新增到特定網橋中。

**子選單：** `/interface/bridge/port`

| 屬性 | 描述 |
| :-- | :-- |
| **auto-isolate** (*yes \| no*; 預設：**no**) | 啟用後，如果未從相鄰網橋收到 BPDU，則阻止埠從丟棄狀態轉為轉發狀態。僅當收到 BPDU 時，埠才會轉為轉發狀態。僅當 `protocol-mode` 設定為 `rstp` 或 `mstp` 且 `edge` 設定為 `no` 時，此屬性才生效。 |
| **bpdu-guard** (*yes \| no*; 預設：**no**) | 啟用或停用埠上的 BPDU Guard 功能。如果收到 BPDU，此功能會將埠置於停用角色，並且如果收到 BPDU，則需要手動停用並啟用該埠。它應用於防止網橋受到與 BPDU 相關的攻擊。當 `protocol-mode` 設定為 `none` 時，此屬性無效。 |
| **bridge** (*name*; 預設：**none**) | 相應介面所屬的網橋介面。 |
| **broadcast-flood** (*yes \| no*; 預設：**yes**) | 啟用後，網橋會將廣播流量泛洪到所有網橋出口埠。停用後，網橋會在出口埠丟棄廣播流量。它可用於過濾出口埠上的所有廣播流量。廣播流量被視為使用 **FF:FF:FF:FF:FF:FF** 作為目標 MAC 地址的流量。此類流量對許多協定至關重要，例如 DHCP、ARP、NDP、BOOTP（Netinstall）等。此選項不會限制到 CPU 的流量泛洪。 |
| **edge** (*auto \| no \| no-discover \| yes \| yes-discover*; 預設：**auto**) | 將埠設定為邊緣埠或非邊緣埠，或啟用邊緣發現。邊緣埠連線到沒有連線其他網橋的 LAN。邊緣埠會跳過 STP 中的學習和監聽狀態，直接轉為轉發狀態。這會縮短 STP 初始化時間。如果埠配置為發現邊緣埠，則一旦網橋檢測到發往邊緣埠的 BPDU，該埠就會變為非邊緣埠。當 <code>protocol-mode</code> 設定為 <code>none</code> 時，此屬性無效。<ul><li><span className="ros-icon-success"><code>no</code></span> - 非邊緣埠，停用發現。它將參與 STP 中的學習和監聽狀態。在交換 BPDU 並與所連線的網橋達成一致之前，它不會轉為轉發狀態。如果未收到 BPDU，埠可能會無限期保持非轉發狀態。</li><li><span className="ros-icon-success"><code>no-discover</code></span> - 非邊緣埠，啟用發現。它將參與 STP 中的學習和監聽狀態。如果未收到 BPDU，埠可以成為邊緣埠。</li><li><span className="ros-icon-success"><code>yes</code></span> - 邊緣埠，不進行發現。它將直接轉為轉發狀態。</li><li><span className="ros-icon-success"><code>yes-discover</code></span> - 邊緣埠，啟用發現。它將直接轉為轉發狀態。</li><li><span className="ros-icon-success"><code>auto</code></span> - 與 <span className="ros-icon-success"><code>no-discover</code></span> 相同，但還會檢測網橋埠是否為停用了 bridge-mode 的 Wireless 介面。此類介面將自動設定為不進行發現的邊緣埠。</li></ul> |
| **fast-leave** (*yes \| no*; 預設：**no**) | 在網橋埠上啟用 IGMP/MLD 快速離開功能。當收到 IGMP/MLD 離開訊息時，網橋將停止向該網橋埠轉發組播流量。僅當 `igmp-snooping` 設定為 `yes` 時，此屬性才生效。 |
| **frame-types** (*admit-all \| admit-only-untagged-and-priority-tagged \| admit-only-vlan-tagged*; 預設：**admit-all**) | 指定網橋埠上允許的入口幀型別。僅當 `vlan-filtering` 設定為 `yes` 時，此屬性才生效。 |
| **ingress-filtering** (*yes \| no*; 預設：**yes**) | 啟用或停用 VLAN 入口過濾，該功能檢查入口埠是否為網橋 VLAN 表中收到的 VLAN ID 的成員。應與 `frame-types` 一起使用，以指定入口流量應帶標籤還是無標籤。僅當 `vlan-filtering` 設定為 `yes` 時，此屬性才生效。自 RouterOS v7 起，該設定預設啟用。 |
| **learn** (*auto \| no \| yes*; 預設：**auto**) | 更改網橋埠上的 MAC 學習行為<ul><li><span className="ros-icon-success"><code>yes</code></span> - 啟用 MAC 學習</li><li><span className="ros-icon-success"><code>no</code></span> - 停用 MAC 學習</li><li><span className="ros-icon-success"><code>auto</code></span> - 檢測網橋埠是否為 Wireless 介面，並使用 Wireless 登錄檔代替 MAC 學習；如果 Wireless 介面設定為 <span className="ros-icon-success"><code>ap-bridge</code></span>、<span className="ros-icon-success"><code>bridge</code></span>、<span className="ros-icon-success"><code>wds-slave</code></span> 模式之一，並且該 Wireless 介面的 bridge 模式已停用，則將使用 Wireless 登錄檔。</li></ul> |
| **multicast-router** (*disabled \| permanent \| temporary-query*; 預設：**temporary-query**) | 組播路由器埠是連線組播路由器或查詢器的埠。未註冊的組播流和 IGMP/MLD 成員報告將傳送到此埠。此設定會更改網橋埠的組播路由器狀態。此屬性可用於將 IGMP/MLD 成員報告發送到某些網橋埠，以便進行進一步的組播路由或代理。僅當 <code>igmp-snooping</code> 設定為 <span className="ros-icon-success"><code>yes</code></span> 時，此屬性才生效。<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 停用網橋埠上的組播路由器狀態。無論該網橋埠連線了什麼，未註冊的組播和 IGMP/MLD 成員報告都不會發送到該網橋埠。</li><li><span className="ros-icon-success"><code>permanent</code></span> - 啟用網橋埠上的組播路由器狀態。無論該網橋埠連線了什麼，未註冊的組播和 IGMP/MLD 成員報告都會發送到該網橋埠。</li><li><span className="ros-icon-success"><code>temporary-query</code></span> - 使用 IGMP/MLD 查詢自動檢測網橋埠上的組播路由器狀態。</li></ul> |
| **horizon** (*integer 0..429496729*; 預設：**none**) | 使用水平分割橋接以防止橋接環路。為一組埠設定相同的值，以防止它們向具有相同 horizon 值的埠傳送資料。水平分割是一種軟體功能，會停用硬體解除安裝。 |
| **hw** (*yes \| no*; 預設：**yes**) | 允許在支援硬體解除安裝的介面上啟用或停用[硬體解除安裝](./index.md#bridge-hardware-offloading)。對於 [EoIP](../virtual-private-networks/eoip.md) 或 [VLAN](./vlan.md) 等軟體介面，此設定會被忽略且無效。某些網橋或埠功能會自動停用硬體解除安裝，使用 `print` 命令檢視“H”標誌是否處於活動狀態。 |
| **internal-path-cost** (*integer: 1..200000000*; 預設： ) | 區域內 MSTI0 的介面路徑開銷。如果未手動配置，網橋會根據介面速度和 <code>port-cost-mode</code> 設定自動確定 internal-path-cost。要恢復自動確定並移除任何手動應用的值，只需在 <code>internal-path-cost</code> 屬性前使用感嘆號。僅當 <code>protocol-mode</code> 設定為 <code>mstp</code> 時，此屬性才生效。 <br/><code>/interface/bridge/port/set [find interface=sfp28-1] !internal-path-cost</code> 使用[埠監控](./index.md#bridge-port-monitoring)檢視所應用的 internal-path-cost。 <br/> |
| **interface** (*name*; 預設：**none**) | 介面或介面列表的名稱。 |
| **path-cost** (*integer: 1..200000000*; 預設： ) | 介面路徑開銷，由 STP 和 RSTP 用於確定最佳路徑，並由 MSTP 用於確定區域之間的最佳路徑。如果未手動配置，網橋會根據介面速度和 <code>port-cost-mode</code> 設定自動確定 path-cost。要恢復自動確定並移除任何手動應用的值，只需在 <code>path-cost</code> 屬性前使用感嘆號。當 <code>protocol-mode</code> 設定為 <code>none</code> 時，此屬性無效。 <br/><code>/interface/bridge/port/set [find interface=sfp28-1] !path-cost</code> 使用[埠監控](./index.md#bridge-port-monitoring)檢視所應用的 path-cost。 <br/> |
| **point-to-point** (*auto \| yes \| no*; 預設：**auto**) | 指定網橋埠是否透過點對點鏈路連線到網橋，以便在故障時更快收斂。將此屬性設定為 `yes` 會強制該鏈路為點對點鏈路，從而跳過檢查機制，該機制會檢測並等待此單條鏈路上其他裝置的 BPDU。將此屬性設定為 `no` 表示預期該鏈路可以接收來自多個裝置的 BPDU。將此屬性設定為 `yes` 可顯著改善（R/M）STP 收斂時間。通常，只有在可能將其他裝置連線到該鏈路時，才應將此屬性設定為 `no`。這主要與無線介質和乙太網集線器相關。如果乙太網鏈路為全雙工，`auto` 會啟用點對點功能。當 `protocol-mode` 設定為 `none` 時，此屬性無效。 |
| **priority** (*0x00 \| 0x10 \| 0x20 \| 0x30 \| 0x40 \| 0x50 \| 0x60 \| 0x70 \| 0x80 \| 0x90 \| 0xa0 \| 0xb0 \| 0xc0 \| 0xd0 \| 0xe0 \| 0xf0*; 預設：**0x80**) | 介面優先順序，由 STP 用於確定根埠，由 MSTP 用於確定區域之間的根埠。必須按 16（0x10）的步長設定。 |
| **pvid** (*integer 1..4094*; 預設：**1**) | 埠 VLAN ID（pvid）指定無標籤入口流量被分配到哪個 VLAN。僅當 `vlan-filtering` 設定為 `yes` 時，此屬性才生效。 |
| **restricted-role** (*yes \| no*; 預設：**no**) | 啟用或停用埠上的受限角色。啟用後，無論其最佳生成樹優先順序向量如何，都會阻止該埠成為 CIST 或任何 MSTI 的根埠。此類埠將被選為 Alternate Port（丟棄狀態），並且只要它繼續收到更優 BPDU，就會保持該狀態。當它不再檢測到更優根路徑時，會自動轉為轉發狀態。網路管理員可以啟用此設定，以防止外部網橋影響活動生成樹，此功能也稱為 root-guard 或 root-protection。當 `protocol-mode` 設定為 `stp`、`rstp` 或 `mstp` 時，此屬性生效（自 RouterOS v7.14 起支援 STP 和 RSTP）。 |
| **restricted-tcn** (*yes \| no*; 預設：**no**) | 啟用或停用埠上的拓撲變更通知（TCN）處理。啟用後，會使該埠不將收到的拓撲變更通知傳播到其他埠，並且由該埠本身引起的任何變更都不會導致向其他埠傳送拓撲變更通知。此引數預設停用。網路管理員可以設定此引數，以防止外部網橋在本地網路中引起 MAC 地址重新整理。當 `protocol-mode` 設定為 `stp`、`rstp` 或 `mstp` 時，此屬性生效（自 RouterOS v7.14 起支援 STP 和 RSTP）。 |
| **tag-stacking** (*yes \| no*; 預設：**no**) | 強制所有封包被視為無標籤封包。無論是否已存在 VLAN 標籤，入口埠上的封包都會被打上另一個 VLAN 標籤。封包將使用與 `pvid` 值匹配的 VLAN ID 打標籤，並使用 `ether-type` 中指定的 EtherType。僅當 `vlan-filtering` 設定為 `yes` 時，此屬性才生效。 |
| **trusted** (*yes \| no*; 預設：**no**) | 啟用後，允許透過此埠將 DHCP 封包轉發到 DHCP 伺服器。主要用於防止未經授權的伺服器向用戶提供惡意資訊。僅當 `dhcp-snooping` 設定為 `yes` 時，此屬性才生效。 |
| **trusted-dhcpv6**(*yes \| no*; 預設：**no**) | 啟用後，允許透過此埠將 DHCPv6 封包轉發到 DHCP 伺服器。主要用於防止未經授權的伺服器向用戶提供惡意資訊。僅當 `dhcpv6-snooping` 設定為 `yes` 時，此屬性才生效。 |
| **trusted-ra** (*yes \| no*; 預設：**no**) | 指定是否允許該埠轉發 IPv6 路由器通告訊息；對於連線到合法路由器的埠設定為 **yes**，對於阻止未經授權來源的埠設定為 **no**。僅當 `ra-guard` 設定為 `yes` 時，此屬性才生效。 |
| **unknown-multicast-flood** (*yes \| no*; 預設：**yes**) | 更改網橋埠上的組播泛洪選項，並且僅控制出口流量。啟用後，網橋允許將組播封包泛洪到指定的網橋埠；停用後，網橋會限制組播流量泛洪到指定的網橋埠。該設定影響所有組播流量。這包括非 IP、IPv4、IPv6 以及鏈路本地組播範圍（例如 224.0.0.0/24 和 ff02::1）。 <br/> 請注意，當啟用 <code>igmp-snooping</code> 並檢測到 IGMP/MLD 查詢器時，網橋會自動限制未知 IP 組播泛洪，因此對於 IGMP/MLD snooping 設定而言，該設定不是必需的。 <br/> 當將此設定與 <code>igmp-snooping</code> 一起使用時，網橋埠上唯一允許的組播流量是來自 MDB 表的已知組播。 |
| **unknown-unicast-flood** (*yes \| no*; 預設：**yes**) | 更改網橋埠上的未知單播泛洪選項，並且僅控制出口流量。啟用後，網橋允許將未知單播封包泛洪到指定的網橋埠；停用後，網橋會限制未知單播流量泛洪到指定的網橋埠。 <br/> 如果 MAC 地址未在主機表中學習到，則該流量被視為未知單播流量，並會泛洪到所有埠。一旦在網橋埠上收到封包並將源 MAC 地址新增到網橋主機表，就會學習到該 MAC 地址。由於網橋需要至少在網橋埠上接收一個數據包才能學習 MAC 地址，建議使用靜態網橋主機條目，以避免在 MAC 地址學習完成之前封包被丟棄。 |

:::info
RouterOS 每個橋接最多可以處理 1024 個橋接介面；此限制是固定的，無法修改。如果你嘗試新增更多介面作為橋接埠，可能會導致不可預測的行為。
:::

### 示例 {#example-1}

此示例演示如何將乙太網埠新增到現有網橋介面，以建立簡單的二層交換配置。透過將 **ether1** 和 **ether2** 新增到 **bridge1**，這些物理埠會成為單個交換網段的一部分，從而使連線到任一埠的裝置能夠像在同一 LAN 上一樣相互通訊。

首先，將每個埠新增到網橋介面：

```ros
[admin@MikroTik] /interface/bridge/port/add bridge=bridge1 interface=ether1
[admin@MikroTik] /interface/bridge/port/add bridge=bridge1 interface=ether2
```

透過顯示網橋埠表來驗證配置：

```ros
[admin@MikroTik] /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE       BRIDGE       HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0     ether1          bridge1      yes  100     0x80         10                 10       none
 1     ether2          bridge1      yes  200     0x80         10                 10       none
```

輸出確認兩個埠現已橋接在一起。**H** 標誌表示硬體解除安裝已啟用，這意味著交換晶片正在處理封包轉發以獲得最佳效能。每個埠分別分配了預設 PVID（埠 VLAN ID）100 和 200，且兩者都使用標準 STP 優先順序 0x80。

### 介面列表 {#interface-lists}

從 RouterOS v6.41 開始，介面列表可以作為橋接埠新增並進行排序。介面列表透過將多個介面分組在一起，簡化了防火牆規則配置。以下示例演示如何將介面列表新增到橋接中：

```ros
/interface/list
add name=LAN1
add name=LAN2
/interface/list/member
add interface=ether1 list=LAN1
add interface=ether2 list=LAN1
add interface=ether3 list=LAN2
add interface=ether4 list=LAN2
/interface/bridge/port
add bridge=bridge1 interface=LAN1
add bridge=bridge1 interface=LAN2
```

當介面列表被新增到橋接中時，這些列表中的各個埠會顯示為動態埠條目：

```ros
[admin@MikroTik] /interface/bridge/port> pr
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE       BRIDGE       HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0     LAN1            bridge1      yes    1     0x80         10                 10       none
 1  D  ether1          bridge1      yes    1     0x80         10                 10       none
 2  D  ether2          bridge1      yes    1     0x80         10                 10       none
 3     LAN2            bridge1      yes    1     0x80         10                 10       none
 4  D  ether3          bridge1      yes    1     0x80         10                 10       none
 5  D  ether4          bridge1      yes    1     0x80         10                 10       none
```

可以使用 `move` 命令重新排列介面列表出現的順序。第二個引數指定所選介面列表應放置在其之前的位置。以下示例演示如何對介面列表進行排序：

```ros
[admin@MikroTik] > /interface/bridge/port/move 3 0
[admin@MikroTik] > /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE       BRIDGE       HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0     LAN2            bridge1      yes    1     0x80         10                 10       none
 1  D  ether3          bridge1      yes    1     0x80         10                 10       none
 2  D  ether4          bridge1      yes    1     0x80         10                 10       none
 3     LAN1            bridge1      yes    1     0x80         10                 10       none
 4  D  ether1          bridge1      yes    1     0x80         10                 10       none
 5  D  ether2          bridge1      yes    1     0x80         10                 10       none
```

:::warning
使用 `move` 命令時，第二個引數表示 "before id" 位置，它確定所選介面列表將被移動到哪裡。如果將第一個介面列表移動到第二個介面列表的位置，該命令將無效，因為第一個列表已經位於第二個列表之前。
:::

### VLAN 表中的介面列表 {#interface-lists-in-vlan-table}

從 RouterOS 7.17 版本開始，可以在橋接 VLAN 表中為 `tagged` 和 `untagged` 屬性使用介面列表。此增強功能允許透過僅修改介面列表成員，而不是逐個更新每個橋接 VLAN 條目，來更靈活地將 VLAN 分配給埠。

如果為 `tagged` 和 `untagged` 設定指定了不同的介面列表，並且介面成員之間存在重疊，則 `untagged` 列表優先。可以使用 `current-tagged` 和 `current-untagged` 屬性以及 `print` 命令檢查當前介面配置。

以下示例演示如何將新介面新增到現有介面列表，自動更新橋接埠和 VLAN 表，而無需直接修改這些選單中的設定：

```ros
/interface/list
add name=vlan10_untagged
add name=vlan20_untagged
add name=vlan_tagged
/interface/list/member
add interface=ether2 list=vlan10_untagged
add interface=ether3 list=vlan10_untagged
add interface=ether4 list=vlan20_untagged
add interface=sfp-sfpplus1 list=vlan_tagged
/interface/bridge
add frame-types=admit-only-vlan-tagged name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 frame-types=admit-only-untagged-and-priority-tagged interface=vlan10_untagged pvid=10
add bridge=bridge1 frame-types=admit-only-untagged-and-priority-tagged interface=vlan20_untagged pvid=20
add bridge=bridge1 frame-types=admit-only-vlan-tagged interface=vlan_tagged
/interface/bridge/vlan
add bridge=bridge1 tagged=vlan_tagged vlan-ids=10
add bridge=bridge1 tagged=vlan_tagged vlan-ids=20

[admin@MikroTik] /interface/bridge/port/print 
Flags: D - DYNAMIC; H - HW-OFFLOAD
Columns: INTERFACE, BRIDGE, HW, PVID, PRIORITY, HORIZON
#    INTERFACE        BRIDGE   HW   PVID  PRIORITY  HORIZON
0    vlan10_untagged  bridge1  yes    10  0x80      none   
1 DH ether2           bridge1  yes    10  0x80      none   
2 DH ether3           bridge1  yes    10  0x80      none   
3    vlan20_untagged  bridge1  yes    20  0x80      none   
4 DH ether4           bridge1  yes    20  0x80      none   
5    vlan_tagged      bridge1  yes     1  0x80      none   
6 DH sfp-sfpplus1     bridge1  yes     1  0x80      none   

[admin@MikroTik] /interface/bridge/vlan/print
Flags: D - DYNAMIC
Columns: BRIDGE, VLAN-IDS, CURRENT-TAGGED, CURRENT-UNTAGGED
#   BRIDGE   VLAN-IDS  CURRENT-TAGGED  CURRENT-UNTAGGED
;;; added by pvid
0 D bridge1        10                  ether2          
                                       ether3          
;;; added by pvid
1 D bridge1        20                  ether4          
2   bridge1        10  sfp-sfpplus1                    
3   bridge1        20  sfp-sfpplus1                 

# 对接口列表成员进行必要的更改：
/interface/list/member/add list=vlan20_untagged interface=ether5
/interface/list/member/add list=vlan_tagged interface=sfp-sfpplus2 

# 在 bridge port 和 vlan 菜单中验证更改：
[admin@MikroTik] > /interface/bridge/port/print 
Flags: D - DYNAMIC; H - HW-OFFLOAD
Columns: INTERFACE, BRIDGE, HW, PVID, PRIORITY, HORIZON
#    INTERFACE        BRIDGE   HW   PVID  PRIORITY  HORIZON
0    vlan10_untagged  bridge1  yes    10  0x80      none   
1 DH ether2           bridge1  yes    10  0x80      none   
2 DH ether3           bridge1  yes    10  0x80      none   
3    vlan20_untagged  bridge1  yes    20  0x80      none   
4 DH ether4           bridge1  yes    20  0x80      none   
5 DH ether5           bridge1  yes    20  0x80      none   
6    vlan_tagged      bridge1  yes     1  0x80      none   
7 DH sfp-sfpplus1     bridge1  yes     1  0x80      none   
8 DH sfp-sfpplus2     bridge1  yes     1  0x80      none   

[admin@MikroTik] > /interface/bridge/vlan/print 
Flags: D - DYNAMIC
Columns: BRIDGE, VLAN-IDS, CURRENT-TAGGED, CURRENT-UNTAGGED
#   BRIDGE   VLAN-IDS  CURRENT-TAGGED  CURRENT-UNTAGGED
;;; added by pvid
0 D bridge1        10                  ether2          
                                       ether3          
;;; added by pvid
1 D bridge1        20                  ether4          
                                       ether5          
2   bridge1        10  sfp-sfpplus1                    
                       sfp-sfpplus2                    
3   bridge1        20  sfp-sfpplus1                    
                       sfp-sfpplus2                    
```

### 橋接埠監控 {#bridge-port-monitoring}

要監控橋接埠的當前狀態，請使用 `monitor` 命令。

**子選單：** `/interface/bridge/port/monitor`

| 屬性 | 描述 |
| :-- | :-- |
| **actual-path-cost** (*integer: 1..200000000*) | 顯示實際埠路徑開銷。該值可以是手動配置的，也可以是根據介面速率和 `port-cost-mode` 設定自動確定的。 |
| **declared-vlan-ids** (*integer 1..4094*) | 介面透過 [MVRP 協定](./index.md#mvrp) 宣告的 VLAN。 |
| **designated-bridge-id** (*priority.MAC address*) | 顯示指定網橋識別符號，該值根據埠的優先順序向量確定。 |
| **designated-cost** (*integer*) | 顯示指定根路徑開銷，該值根據埠的優先順序向量確定。 |
| **designated-internal-cost** (*integer*) | 顯示指定內部根路徑開銷，該值根據埠的優先順序向量確定。 |
| **designated-message-age**(*time)* | 顯示指定訊息老化時間，該值根據埠的優先順序向量確定。 |
| **designated-max-age** (*time)* | 顯示指定最大老化時間，該值根據埠的優先順序向量確定。BPDU 封包可以透過的網橋數量由 `max-message-age` 引數指定。 |
| **designated-port-id** (*priority*.*integer*) | 顯示指定埠識別符號，該值根據埠的優先順序向量確定。 |
| **designated-remaining-hops** (*integer*) | 顯示指定剩餘跳數，該值根據埠的優先順序向量確定。即封包在到達目的地之前允許經過的跳數。 |
| **discard-transitions** (*integer*) | 計數器，記錄埠進入丟棄狀態的次數。 |
| **edge-port** (*yes \| no*) | 該埠是否為邊緣埠。 |
| **edge-port-discovery** (*yes \| no*) | 該埠是否設定為自動檢測邊緣埠。 |
| **external-fdb** (*yes \| no*) | 是否使用登錄檔而非轉發資料庫。 |
| **forwarding** (*yes \| no*) | 顯示該埠是否未被 (R/M)STP 阻塞。 |
| **forward-transitions** (*integer*) | 計數器，記錄埠進入轉發狀態的次數 |
| **hw-offload-group** (*switchX*) | 該埠使用的交換晶片。 |
| **interface** (*name*) | 介面名稱。 |
| **last-topology-change** (*time)* | 上次拓撲變化計時器，記錄自上次變化以來的時間。 |
| **learning** (*yes \| no*) | 顯示該埠是否能夠學習 MAC 地址。 |
| **multicast-router** (*yes \| no*) | 顯示是否在該埠上檢測到組播路由器。僅當啟用 `igmp-snooping` 時才會顯示該監控值。 |
| **registered-vlan-ids** (*integer 1..4094*) | 介面透過 [MVRP 協定](./index.md#mvrp) 註冊的 VLAN。 |
| **port-id** (*priority*.*integer*) | 在生成樹協定中，每個埠都有唯一的埠識別符號。即優先順序[十六進位制] + 埠號。 |
| **point-to-point-port** (*yes \| no*) | 該埠是否以全雙工（yes）或半雙工（no）方式連線到網橋埠。 |
| **role** (*designated \| root-port \| alternate \| backup \| disabled*) | (R/M)STP 演算法分配的埠角色：<br/><ul><li><span className="ros-icon-success"><code>disabled-port</code></span> - 已停用或未啟用的埠。</li><li><span className="ros-icon-success"><code>root-port</code></span> - 面向根網橋且具有到根網橋的最佳（最低開銷）路徑的埠。每個網橋只選舉一個根埠（根網橋本身除外）。</li><li><span className="ros-icon-success"><code>alternative-port</code></span> - 面向根網橋但不會轉發流量的埠。噹噹前根埠故障時，該埠提供到根網橋的備份路徑。</li><li><span className="ros-icon-success"><code>designated-port</code></span> - 背向根網橋並將流量從根網橋轉發到下游裝置的埠。</li><li><span className="ros-icon-success"><code>backup-port</code></span> - 背向根網橋且會轉發流量的埠。該埠作為同一網段上指定埠的備份。</li></ul> 在 RouterOS 中，<strong>role</strong> 監控屬性即使在使用 STP 模式時也會顯示 RSTP 角色，例如 <code>alternate-port</code> 和 <code>backup-port</code>。這在技術上並不正確，但不會影響 STP 的執行。這是因為 STP 對所有被阻塞的埠一視同仁，不區分其用途（例如作為潛在的備份路徑）。所顯示的角色只是 RSTP 功能的反映，在 STP 使用時沒有實際影響。更多詳細資訊請參見 [STP 和 RSTP 頁面](./user-guides/spanning-tree-protocol.md#stp-and-rstp)。 |
| **root-path-cost** (*integer*) | 到根網橋的路徑總開銷。 |
| **sending-rstp** (*yes \| no*) | 該埠使用的是 RSTP 還是 MSTP 型別的 BPDU。當啟用了 RSTP/MSTP 的埠收到 STP BPDU 時，該埠會轉換為 STP 型別。此設定**並不**表示 BPDU 是否實際被髮送。 |
| **status** (*in-bridge \| inactive*) | 埠狀態：<ul><li><span className="ros-icon-success"><code>in-bridge</code></span> - 埠已啟用</li><li><span className="ros-icon-success"><code>inactive</code></span> - 埠已停用。</li></ul> |
| **tx-rx-bpdu** (*integer*) | 傳送/接收的 bpdu 訊息計數器。 |
| **tx-rx-tc** (*integer*) | 傳送/接收的拓撲變化訊息。 |
| **topology-changes** (*integer*) | 拓撲變化計數器。 |

```ros
[admin@MikroTik] /interface/bridge/port/monitor [find interface=ether1] 
                  interface: ether1                  
                     status: in-bridge               
                    port-id: 0x80.1                  
                       role: root-port               
                  edge-port: no                      
        edge-port-discovery: yes                     
        point-to-point-port: yes                     
               external-fdb: no                      
               sending-rstp: yes                     
                   learning: yes                     
                 forwarding: yes                     
           actual-path-cost: 20000                   
    internal-root-path-cost: 20000                   
       designated-bridge-id: 0x1000.2C:C8:1B:FF:92:F4
   designated-internal-cost: 0                       
         designated-port-id: 0x80.1                  
  designated-remaining-hops: 20                      
                 tx-rx-bpdu: 3/63                    
        discard-transitions: 0                       
        forward-transitions: 1                       
                   tx-rx-tc: 2/0                     
           topology-changes: 1                       
       last-topology-change: 2m5s                    
           multicast-router: no                      
           hw-offload-group: switch1                 
          declared-vlan-ids: 1                       
        registered-vlan-ids: 1                       
```

## 主機表 {#hosts-table}

---

主機表顯示已在網橋介面上學習到的 MAC 地址。該表還顯示各種標誌，提供有關每個主機條目的附加資訊。可透過 `/interface/bridge/host` 子選單訪問主機表。

**子選單：** `/interface/bridge/host`

| 屬性 | 描述 |
| :-- | :-- |
| **bridge** (*read-only: name*) | 主機條目所屬的網橋 |
| **disabled** (*read-only: flag*) | 表示該靜態主機條目是否已停用 |
| **dynamic** (*read-only: flag*) | 表示該主機是否為動態學習到的 |
| **external** (*read-only: flag*) | 表示該主機是否是從外部表（例如交換晶片或 Wireless 登錄檔）學習到的。在硬體解除安裝的網橋埠上新增的靜態主機條目不會顯示此標誌 |
| **invalid** (*read-only: flag*) | 表示該主機條目是否無效。對於配置在被移除的介面上的靜態主機，可能會出現此標誌 |
| **local** (*read-only: flag*) | 表示該主機條目是否由網橋自身建立，網橋自身會顯示所有本地介面 |
| **mac-address** (*read-only: MAC address*) | 主機的 MAC 地址 |
| **on-interface** (*read-only: name*) | 主機所連線的網橋埠 |

### 監控 {#monitoring}

要檢視活動主機表，請使用 `print` 命令。該表會顯示已在網橋介面上學習到的所有 MAC 地址，以及標誌指示和連線詳情。

```ros
[admin@MikroTik] /interface/bridge/host/print
Flags: X - disabled, I - invalid, D - dynamic, L - local, E - external 
 #       MAC-ADDRESS        VID ON-INTERFACE            BRIDGE
0   D   B8:69:F4:C9:EE:D7      ether1                  bridge1
1   D   B8:69:F4:C9:EE:D8      ether2                  bridge1
2   DL  CC:2D:E0:E4:B3:38      bridge1                 bridge1
3   DL  CC:2D:E0:E4:B3:39      ether2                  bridge1
```

輸出顯示：

- **D** 標誌：動態學習到的 MAC 地址
- **DL** 標誌：本地介面 MAC 地址（網橋自身及其埠介面）
- **VID**：與主機條目關聯的 VLAN ID
- **ON-INTERFACE**：學習到該主機的網橋埠
- **BRIDGE**：該主機所屬的網橋介面

### 靜態條目 {#static-entries}

網橋主機表支援配置靜態 MAC 地址條目。靜態條目在兩種主要場景下很有用：將特定流量引導透過指定埠，以及透過停用動態 MAC 學習、僅依賴預配置的靜態條目來保護裝置資源。

下表列出了靜態 MAC 地址條目的所有可配置引數：

**子選單：** `/interface/bridge/host`

| 屬性 | 描述 |
| :-- | :-- |
| **bridge** (*name*；預設值：**none**) | 為其分配 MAC 地址的網橋介面。 |
| **disabled** (*yes \| no*；預設值：**no**) | 啟用或停用該靜態 MAC 地址條目。 |
| **interface** (*name*；預設值：**none**) | 轉發該 MAC 地址流量的介面名稱。 |
| **mac-address** (*MAC address*；預設值： ) | 要靜態新增到主機表中的 MAC 地址。 |
| **vid** (*integer: 1..4094*；預設值： ) | 與該靜態 MAC 地址條目關聯的 VLAN ID。 |

**示例：** 要將發往 MAC 地址 **4C:5E:0C:4D:12:43** 的所有流量僅透過 **ether2** 轉發，請使用以下命令：

```ros
/interface/bridge/host
add bridge=bridge1 interface=ether2 mac-address=4C:5E:0C:4D:12:43
```

## 組播表 {#multicast-table}

---

組播表顯示透過 IGMP/MLD snooping 學習到的組播組成員關係資訊。當在橋上啟用 IGMP/MLD snooping 時，裝置會主動監控 IGMP/MLD 網路通訊，以構建活動組播組及其訂閱埠成員的組播資料庫（MDB）。然後，橋使用此資訊將組播流量智慧地僅轉發到連線了感興趣的接收者裝置的埠，而不是將組播流量泛洪到所有埠。

請注意，發往鏈路本地組播組 224.0.0.0/24 和 ff02::1 的封包是此行為的例外——這些地址始終無限制地泛洪到所有埠和 VLAN，因為它們用於網路協定操作。

要檢視當前組播資料庫條目的表，請在組播資料庫子選單中使用 `print` 命令。

**子選單：** `/interface/bridge/mdb`

| 屬性 | 描述 |
| :-- | :-- |
| <strong>bridge</strong> (<em>read-only: name</em>) | 顯示該條目所屬的橋接介面。 |
| <strong>group</strong> (*read-only:*ipv4 | ipv6 |
| <strong>on-interface</strong> (<em>read-only: name</em>) | 顯示已訂閱該組播組的橋接埠。 |
| <strong>vid</strong> (<em>read-only: integer</em>) | 顯示該組播組的 VLAN ID，僅在啟用 <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> 時適用。 |

```ros
[admin@MikroTik] /interface/bridge/mdb/print 
Flags: D - DYNAMIC
Columns: GROUP, VID, ON-PORTS, BRIDGE
 #   GROUP              VID  ON-PORTS  BRIDGE 
 0 D ff02::2              1  bridge1   bridge1
 1 D ff02::6a             1  bridge1   bridge1
 2 D ff02::1:ff00:0       1  bridge1   bridge1
 3 D ff02::1:ff01:6a43    1  bridge1   bridge1
 4 D 229.1.1.1           10  ether2    bridge1
 5 D 229.2.2.2           10  ether3    bridge1
                             ether2           
 6 D ff02::2             10  ether5    bridge1
                             ether3           
                             ether2           
                             ether4           
```

### 靜態條目 {#static-entries-1}

自 RouterOS 7.7 版本起，可以為 IPv4 和 IPv6 組播組建立靜態 MDB 條目。

**子選單：** `/interface/bridge/mdb`

| 屬性 | 描述 |
| :-- | :-- |
| **bridge** (*name*; 預設值：) | 將為其分配 MDB 條目的網橋介面。 |
| **disabled** (*yes \| no*; 預設值：**no**) | 停用或啟用靜態 MDB 條目。 |
| **group** (*ipv4 \| ipv6 \| MAC address*; 預設值：) | IPv4、IPv6 或 MAC 組播地址。無法為鏈路本地組播組 224.0.0.0/24 和 ff02::1 建立靜態條目，因為這些封包始終會在所有埠和 VLAN 上泛洪。 |
| **interface** (*name*; 預設值：) | 組播組將被轉發到的網橋埠列表。 |
| **vid** (*integer: 1..4094*; 預設值：) | 將在其上建立 MDB 條目的 VLAN ID 僅在啟用 `vlan-filtering` 時適用。未指定 VLAN ID 時，條目將工作在 shared-VLAN 模式下，並動態應用於特定埠的全部已定義 VLAN ID。 |

例如，要為 VLAN 10 上埠 ether2 和 ether3 的組播組 229.10.10.10 建立靜態 MDB 條目，請使用以下命令：

```ros
/interface/bridge/mdb
add bridge=bridge1 group=229.10.10.10 interface=ether2,ether3 vid=10
```

使用 `print` 命令驗證結果：

```ros
[admin@MikroTik] > /interface/bridge/mdb/print where group=229.10.10.10
Columns: GROUP, VID, ON-PORTS, BRIDGE
 # GROUP         VID  ON-PORTS  BRIDGE 
12 229.10.10.10   10  ether2    bridge1
                      ether3   
```

如果某個 IPv6 組播組不需要被偵聽，並且希望它在所有埠和 VLAN 上泛洪，則可以在所有 VLAN 和埠（包括網橋介面本身）上建立靜態 MDB 條目。使用以下命令為所有 VLAN 和埠上的組播組 ff02::2 建立靜態 MDB 條目（請根據你的具體設定修改 `ports` 設定）：

```ros
/interface/bridge/mdb
add bridge=bridge1 group=ff02::2 interface=bridge1,ether2,ether3,ether4,ether5

[admin@MikroTik] > /interface/bridge/mdb/print where group=ff02::2
Flags: D - DYNAMIC
Columns: GROUP, VID, ON-PORTS, BRIDGE
 #   GROUP    VID  ON-PORTS  BRIDGE 
 0   ff02::2                 bridge1
15 D ff02::2    1  bridge1   bridge1
16 D ff02::2   10  bridge1   bridge1
                   ether2           
                   ether3           
                   ether4           
                   ether5           
17 D ff02::2   20  bridge1   bridge1
                   ether2           
                   ether3           
18 D ff02::2   30  bridge1   bridge1
                   ether2           
                   ether3     
```

## 網橋硬體解除安裝 {#bridge-hardware-offloading}

---

如果裝置具有內建交換晶片，就可以將多個埠組合交換。雖然網橋是一種會消耗 CPU 資源的軟體功能，但網橋硬體解除安裝允許你使用內建交換晶片以線速轉發封包。如果配置正確，這可以讓你實現更高的吞吐量。

![HWoffloading_diagram](/img/8d426fcfc1794e99.webp)

其中一個埠接收到的封包總是首先經過交換邏輯。交換邏輯決定封包應發往哪些埠——通常基於目標 MAC 地址。硬體轉發的封包對 RouterOS 不可見（只有統計資訊會顯示封包已經過）。這是因為該封包已由交換晶片處理，從未到達 CPU。

封包可以透過交換器 CPU 埠轉發到 CPU，用於管理訪問、路由、防火牆規則或流量控制。這需要針對您的裝置和使用場景進行特定配置。請檢視適用於您特定裝置的手冊頁：

- [Marvell Prestera 交換器晶片功能](./marvell-prestera-switch-chip-features.md)
- [CRS1xx/2xx 系列交換器](./user-guides/crs1xx-2xx-series-switches-examples.md)
- [非 CRS 系列交換器](./switch-chip-features.md)

:::danger
某些橋接和乙太網埠屬性與交換器晶片設定直接相關。更改此類屬性可能會觸發**交換器晶片重設**，臨時停用所有乙太網埠。在生產環境中更改屬性時必須考慮到這一點。此類屬性包括 DHCP 監聽、IGMP 監聽、VLAN 過濾、L2MTU、流量控制等。可能觸發交換器晶片重設的確切設定取決於裝置型號。
:::

:::warning
[CRS1xx/2xx 系列交換器](./crs1xx-and-2xx-series-switches.md#multiple-switch-groups)支援每個交換器晶片多個硬體解除安裝橋接。所有其他裝置僅支援一個。在 `/interface/bridge/port` 下使用 `hw=yes/no` 選擇哪個橋接使用硬體解除安裝。
:::

以下表格列出了每種交換器晶片型別下，哪些網橋功能支援硬體解除安裝（✓）或會停用硬體解除安裝（✗）：

### 搭載 Marvell Prestera 交換器的 MikroTik 裝置 {#mikrotik-devices-with-marvell-prestera-switch}

例如：CRS3xx、CRS4xx、CRS5xx、CRS8xx、CCR2116、CCR2216、RDS2216。請參閱 [Marvell Prestera 交換器晶片功能](./marvell-prestera-switch-chip-features.md)。

| 功能 | 硬體解除安裝 |
| :-- | :--: |
| STP/RSTP | ✓ |
| MSTP | ✓ |
| VLAN 過濾 | ✓ |
| IGMP 偵聽 | ✓ |
| DHCP 偵聽 | ✓ |
| DHCPv6 偵聽 | ✓ |
| RA 防護 | ✓ |
| 繫結¹ | ✓ |
| MLAG | ✓ |
| Horizon | ✗ |

¹ 只有 `mode=802.3ad`（LACP）、`mode=balance-xor`（靜態 LAG）和 `mode=active-backup` 繫結介面支援硬體解除安裝。其他模式不支援硬體解除安裝。交換器始終使用 Layer2+Layer3+Layer4 作為傳送雜湊策略，更改傳送雜湊策略不會產生任何效果。

### 88E6393X、88E6191X、88E6190 {#88e6393x-88e6191x-88e6190}

例如：RB5009 系列、L009 系列、CCR2004-16G-2S+。請參閱 [交換器晶片功能](./switch-chip-features.md)。

| 功能 | 硬體解除安裝 |
| :-- | :--: |
| STP/RSTP | ✓ |
| MSTP | ✓ |
| VLAN 過濾¹ | ✓ |
| IGMP 偵聽² | ✓ |
| DHCP 偵聽² | ✓ |
| 繫結³ | ✓ |
| DHCPv6 偵聽 | ✗ |
| RA 防護 | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

¹ 不支援 `ether-type=0x88a8` 或 `ether-type=0x9100`（僅支援預設 `ether-type=0x8100`）。不支援 `tag-stacking=yes`。使用這些功能會停用硬體解除安裝。  
² 不支援 QinQ，僅解析第一個 VLAN 標籤。雙重標記的 DHCP 或 IGMP 封包可能會被錯誤處理。  
³ 僅 `mode=802.3ad`（LACP）、`mode=balance-xor`（靜態 LAG）和 `mode=active-backup` 繫結介面支援硬體解除安裝。其他模式不支援硬體解除安裝。僅限於 Layer2 傳輸雜湊，更改傳輸雜湊策略沒有任何效果。

### MT7621, MT7531, EN7523, RTL8367 {#mt7621-mt7531-en7523-rtl8367}

例如：hEX S、hAP ax lite、hEX Refresh、RBM33G、RB4011、RB1100AHx4。參見 [交換器晶片功能](./switch-chip-features.md)。

| 功能 | 硬體解除安裝 |
| :-- | :--: |
| STP/RSTP | ✓ |
| MSTP | ✓ |
| VLAN 過濾¹ | ✓ |
| IGMP 偵聽 | ✗ |
| DHCP 偵聽 | ✗ |
| DHCPv6 偵聽 | ✗ |
| RA 防護 | ✗ |
| 繫結 | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

¹ 不支援 `ether-type=0x88a8` 或 `ether-type=0x9100`（僅支援預設 `ether-type=0x8100`）。不支援 `tag-stacking=yes`。使用這些功能會停用硬體解除安裝。

### CRS1xx/CRS2xx 系列 {#crs1xxcrs2xx-series}

例如：CRS105、CRS106、CRS109、CRS112、CRS125、CRS210、CRS212、CRS226。參見 [CRS1xx/2xx 系列交換器](./crs1xx-and-2xx-series-switches.md)。

| 功能 | 硬體解除安裝 |
| :-- | :--: |
| STP/RSTP | ✓ |
| IGMP 偵聽¹ | ✓ |
| DHCP 偵聽¹ | ✓ |
| MSTP | ✗ |
| VLAN 過濾 | ✗ |
| DHCPv6 偵聽 | ✗ |
| RA 防護 | ✗ |
| 繫結 | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

¹ 該功能在 VLAN 交換配置中無法正常工作。

### QCA8337, Atheros8327, Atheros8316 {#qca8337-atheros8327-atheros8316}

例如：RB3011、RB1100AHx2、RB850Gx2、cAP ac、wAP ac、Audience、mANTBox、CCR1009。參見[交換器晶片功能](./switch-chip-features.md)。

| 功能 | 硬體解除安裝 |
| :-- | :--: |
| STP/RSTP | ✓ |
| DHCP 偵聽¹ | ✓ |
| MSTP | ✗ |
| VLAN 過濾 | ✗ |
| IGMP 偵聽 | ✗ |
| DHCPv6 偵聽 | ✗ |
| RA 防護 | ✗ |
| 繫結 | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

¹ 該功能在 VLAN 交換配置中無法正常工作。

### Atheros8227, Atheros7240 {#atheros8227-atheros7240}

例如：hAP lite、hEX lite、PowerBox、wsAP ac lite、RBmAP2nD。參見[交換器晶片功能](./switch-chip-features.md)。

| 功能 | 硬體解除安裝 |
| :-- | :--: |
| STP/RSTP | ✓ |
| MSTP | ✗ |
| VLAN 過濾 | ✗ |
| IGMP 偵聽 | ✗ |
| DHCP 偵聽 | ✗ |
| DHCPv6 偵聽 | ✗ |
| RA 防護 | ✗ |
| 繫結 | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

### IPQ-PPE, QCA8386, PIPE 98PX1012 {#ipq-ppe-qca8386-pipe-98px1012}

例如：hAP ax 系列、cAP ax、Chateau ax 系列、hAP be³ Media、CCR2004-1G-12S+2XS。參見[交換器晶片功能](./switch-chip-features.md)。

| 功能 | 硬體解除安裝 |
| :-- | :--: |
| STP/RSTP | ✗ |
| MSTP | ✗ |
| VLAN 過濾 | ✗ |
| IGMP 偵聽 | ✗ |
| DHCP 偵聽 | ✗ |
| DHCPv6 偵聽 | ✗ |
| RA 防護 | ✗ |
| 繫結 | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

:::danger
在 **IPQ-PPE** 上使用 `protocol-mode=none` 會啟用硬體解除安裝橋接，並可能導致問題。  
建議透過保留預設的 `protocol-mode=rstp` 設定或在 `/interface/bridge/port` 下手動設定 `hw=no` 來使用非硬體解除安裝的橋接。
:::

### 示例 {#example-2}

以下示例演示如何使用啟用了硬體解除安裝的網橋配置埠交換。此配置會建立一個網橋介面，並將多個乙太網介面新增為網橋埠。`hw=yes` 網橋埠設定預設使用。

```ros
/interface bridge
add name=bridge1
/interface bridge port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
```

透過檢查橋接埠表中的 **H** 標誌，驗證硬體解除安裝是否已啟用：

```ros
[admin@MikroTik] /interface/bridge/port/print 
Flags: H - HW-OFFLOAD
Columns: INTERFACE, BRIDGE, HW, HORIZON, TRUSTED, TRUSTED-RA, TRUSTED-DHCPV6, FAST-LEAVE, BPDU-GUARD, EDGE, POINT-TO-POINT, PVID, FRAME-TYPES
#   INTERFACE  BRIDGE   HW   HORIZON  TRUSTED  TRUSTED-RA  TRUSTED-DHCPV6  FAST-LEAVE  BPDU-GUARD  EDGE  POINT-TO-POINT  PVID  FRAME-TYPES
0 H ether2     bridge1  yes  none     no       no          no              no          no          auto  auto               1  admit-all  
1 H ether3     bridge1  yes  none     no       no          no              no          no          auto  auto               1  admit-all  
2 H ether4     bridge1  yes  none     no       no          no              no          no          auto  auto               1  admit-all  
3 H ether5     bridge1  yes  none     no       no          no              no          no          auto  auto               1  admit-all  
```

## 橋接 VLAN 過濾 {#bridge-vlan-filtering}

---

橋接 VLAN 過濾可啟用 VLAN 感知的二層轉發，並允許在橋接內修改 VLAN 標籤。此功能使橋接更類似於傳統乙太網交換器，並有助於解決橋接 VLAN 介面時可能出現的生成樹相容性問題。強烈建議配置橋接 VLAN 過濾，以符合 STP（IEEE 802.1D）和 RSTP（IEEE 802.1W）標準；而在 RouterOS 中啟用 MSTP（IEEE 802.1s）支援時，則必須進行此配置。

主要 VLAN 設定是 `vlan-filtering`，它全域性控制橋接的 VLAN 感知和 VLAN 標籤處理。當 `vlan-filtering` 設定為 `no` 時，橋接會忽略 VLAN 標籤，以 shared-VLAN-learning (SVL) 模式執行，並且無法修改封包的 VLAN 標籤。啟用 `vlan-filtering` 會啟用所有與橋接 VLAN 相關的功能，並切換到 independent-VLAN-learning (IVL) 模式。除了將埠加入二層轉發之外，橋接本身也作為一個介面執行，因此具有埠 VLAN ID（pvid）。

:::warning
目前，配備 Marvell Prestera 交換器以及 RTL8367、88E6393X、88E6191X、88E6190、MT7621、MT7531 和 EN7523 交換器晶片（自 RouterOS v7 起）的 MikroTik 裝置可以同時使用橋接 VLAN 過濾和硬體解除安裝。在啟用橋接 VLAN 過濾時，其他裝置無法利用內建交換器晶片的優勢。這些裝置應按照基本 VLAN 交換指南中描述的方法進行配置。使用不正確的配置方法可能會導致網路中的吞吐量問題。
:::

### 橋接 VLAN 表 {#bridge-vlan-table}

橋接 VLAN 表定義每個 VLAN 的埠成員關係，並指定出站流量的 VLAN 標籤操作。配置為 `tagged` 的埠會發送帶有其對應 VLAN ID 的幀，而配置為 `untagged` 的埠會在傳送幀之前移除 VLAN 標籤。`frame-types` 設定為 `admit-all` 或 `admit-only-untagged-and-priority-tagged` 的橋接埠會自動新增為其配置的 PVID 對應的 untagged 埠。

**子選單：** `/interface/bridge/vlan`

| 屬性 | 描述 |
| :-- | :-- |
| <strong>bridge</strong> (<em>name</em>; 預設值：<strong>none</strong>) | 此 VLAN 條目所應用的橋接介面。 |
| <strong>disabled</strong> (<em>yes</em> | <em>no</em>; 預設值：<strong>no</strong>) |
| <strong>tagged</strong> (<em>interface</em>; 預設值：<strong>none</strong>) | 以 VLAN 標籤傳送幀的介面或 [介面列表](../system-information-and-utilities/interface-lists.md)。此設定接受逗號分隔的值，例如 <code>tagged=ether1,ether2</code>。 |
| <strong>untagged</strong> (<em>interface</em>; 預設值：<strong>none</strong>) | 傳送不帶 VLAN 標籤的幀的介面或 [介面列表](../system-information-and-utilities/interface-lists.md)。此設定接受逗號分隔的值，例如 <code>untagged=ether3,ether4</code>。 |
| <strong>vlan-ids</strong> (<em>integer 1..4094</em>; 預設值：<strong>1</strong>) | 此埠配置的 VLAN ID 或 VLAN ID 列表。此設定接受 VLAN ID 範圍以及逗號分隔的值，例如 <code>vlan-ids=100-115,120,122,128-130</code>。 |

:::danger
`vlan-ids` 引數可以指定一組或一系列 VLAN，但僅應用於帶標籤埠配置。當為接入埠配置指定多個 VLAN 時，無論 PVID 值如何，帶標籤的封包都可能透過錯誤的接入埠作為未標記封包傳送。
:::

:::warning
使用橋接 VLAN 過濾時，確保將所有必需的介面新增到橋接 VLAN 表中。

為了使路由功能在同一裝置上透過使用橋接 VLAN 過濾的埠正常工作，必須允許訪問橋接介面（當使用硬體解除安裝的 VLAN 過濾時，這包括 switch-cpu 埠）。可以透過將橋接介面本身作為帶標籤埠新增到 VLAN 表來手動完成此操作。自 RouterOS v7.16 起，在啟用了 VLAN 過濾的橋接上新增 VLAN 介面時，會自動完成此操作（在 `/interface/bridge/vlan` 選單下會出現一條註釋為 "added by vlan on bridge" 的動態條目）。更多示例可以在 VLAN 間路由和管理訪問部分找到。

自 RouterOS 7.20 起，當同一 VLAN ID 跨越多個交換器晶片或在硬體埠和軟體埠上同時使用時，會新增一條名為 "added by switch-cpu" 的動態帶標籤條目。
:::

:::danger
允許訪問 CPU 時，你允許從特定埠訪問路由器/交換器本身。這並不總是可取的。當允許從特定 VLAN ID 和埠訪問 CPU 時，確保實施適當的防火牆過濾規則來保護你的裝置。使用防火牆過濾規則僅允許訪問所需的服務。
:::

:::warning
配置不當的橋接 VLAN 過濾可能導致安全問題。在生產環境中部署裝置之前，確保你完全理解 [橋接 VLAN 表](./user-guides/bridge-vlan-table.md) 的工作原理。
:::

### 橋接埠設定 {#bridge-port-settings}

每個橋接埠都有多個與 VLAN 相關的設定，用於控制未標記 VLAN 成員關係、VLAN 標記與取消標記行為，以及基於是否存在 VLAN 標籤的封包過濾。

**子選單：** `/interface/bridge/port`

| 屬性 | 描述 |
| :-- | :-- |
| <strong>frame-types</strong> (<em>admit-all</em> | <em>admit-only-untagged-and-priority-tagged</em> |
| <strong>ingress-filtering</strong> (<em>yes</em> | <em>no</em>; 預設值：<strong>yes</strong>) |
| <strong>pvid</strong> (<em>integer: 1..4094</em>; 預設值：<strong>1</strong>) | 埠 VLAN ID（pvid）指定未標記的入站流量分配到哪個 VLAN。僅當 <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> 設定為 <span className="ros-icon-success"><code>yes</code></span> 時，此屬性才生效。 |
| <strong>tag-stacking</strong> (<em>yes</em> | <em>no</em>; 預設值：<strong>no</strong>) |

### 橋接主機表 {#bridge-host-table}

橋接主機表顯示已在橋接介面上學習到的 MAC 地址。啟用 vlan-filtering 後，該表還會顯示與每個學習到的 MAC 地址關聯的 VLAN ID，從而啟用獨立 VLAN 學習（IVL）模式。

```ros
[admin@MikroTik] > /interface/bridge/host/print where !local 
Flags: X - disabled, I - invalid, D - dynamic, L - local, E - external 
 #       MAC-ADDRESS        VID ON-INTERFACE       BRIDGE
0   D   CC:2D:E0:E4:B3:AA  300 ether3             bridge1
1   D   CC:2D:E0:E4:B3:AB  400 ether4             bridge1
```

### VLAN 示例：Trunk 和 Access 埠 {#vlan-example-trunk-and-access-ports}

本節演示如何配置一個基本的 VLAN 設定，其中包含一個 Trunk 埠和多個 Access 埠。Trunk 埠（ether2）在交換器之間或到路由器之間承載帶標籤的 VLAN 流量，而 Access 埠（ether6、ether7、ether8）連線終端裝置並使用不帶標籤的 VLAN 流量。

![access_ports](/img/dcbdce357964f958.webp)

#### 步驟 1：建立網橋介面 {#step-1-create-the-bridge-interface}

建立一個停用 `vlan-filtering` 的網橋介面。這一點很重要，因為立即啟用 VLAN 過濾會限制流量，可能在配置完成前使你無法訪問裝置。有關在 VLAN 配置期間管理裝置訪問的詳細資訊，請參閱[管理訪問配置](#management-access-configuration)部分。

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
```

#### 步驟 2：新增網橋埠並配置 PVID {#step-2-add-bridge-ports-and-configure-pvid}

將物理介面新增到網橋，併為 Access 埠配置埠 VLAN ID（pvid）。pvid 決定進入網橋時，不帶標籤的流量被分配到哪個 VLAN。`frame-types` 設定控制每個埠接受哪種型別的流量：僅帶標籤、僅不帶標籤或兩者都接受。

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether2 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether6 pvid=200 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether7 pvid=300 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether8 pvid=400 frame-types=admit-only-untagged-and-priority-tagged
```

#### 步驟 3：建立網橋 VLAN 表條目 {#step-3-create-bridge-vlan-table-entries}

建立網橋 VLAN 表條目。Trunk 埠（ether2）必須配置為帶標籤成員，這意味著它將傳送和接收帶有 VLAN 標籤的幀。Access 埠會根據其 pvid 設定自動新增為不帶標籤成員，因此你只需在每個 VLAN 條目中指定帶標籤埠。

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 vlan-ids=200
add bridge=bridge1 tagged=ether2 vlan-ids=300
add bridge=bridge1 tagged=ether2 vlan-ids=400
```

#### 步驟 4：啟用 VLAN 過濾 {#step-4-enable-vlan-filtering}

配置完所有 VLAN 設定後，在網橋上啟用 VLAN 過濾以啟用 VLAN 功能。

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

#### 步驟 5：（可選）拒絕未標記流量 {#step-5-optional-reject-untagged-traffic}

作為可選的安全措施，你可以透過更改 frame-type 來將網橋設定為拒絕未標記流量。這會阻止使用預設 VLAN 1（pvid=1），並確保只接受正確標記的流量。

```ros
/interface/bridge/set bridge1 frame-types=admit-only-vlan-tagged
```

### VLAN 示例 - Trunk 和 Hybrid 埠 {#vlan-example---trunk-and-hybrid-ports}

![hybrid_ports](/img/90b987271e134d95.webp)

建立一個停用 `vlan-filtering` 的網橋，以避免在 VLAN 完全配置完成之前失去對路由器的訪問。如果你需要對網橋進行管理訪問，請參閱[管理訪問配置](./index.md#management-access-configuration)部分。

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
```

新增網橋埠，並在 Hybrid VLAN 埠上指定 `pvid`，以將未標記流量分配到預期的 VLAN。使用 `frame-types` 設定僅在 ether2 上接受帶標記的封包。

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether2 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether6 pvid=200
add bridge=bridge1 interface=ether7 pvid=300
add bridge=bridge1 interface=ether8 pvid=400
```

新增 Bridge VLAN 條目，並在其中指定帶標記埠。在此示例中，出方向 VLAN 標記也在 ether6、ether7、ether8 埠上執行，使它們成為 Hybrid 埠。`frame-types` 設定為 `admit-all` 的網橋埠將自動新增為 `pvid` VLAN 的未標記埠。

```ros
/interface/bridge/vlan 
add bridge=bridge1 tagged=ether2,ether7,ether8 vlan-ids=200
add bridge=bridge1 tagged=ether2,ether6,ether8 vlan-ids=300
add bridge=bridge1 tagged=ether2,ether6,ether7 vlan-ids=400
```

最後，當 VLAN 配置完成後，啟用 Bridge VLAN Filtering。

```ros
/interface/bridge/set bridge1 vlan-filtering=yes 
```

可選步驟是在網橋介面上設定 `frame-types=admit-only-vlan-tagged`，以停用預設的未標記 VLAN 1（`pvid=1`）。

```ros
/interface/bridge/set bridge1 frame-types=admit-only-vlan-tagged
```

:::danger
你不必手動將接入埠新增為未標記埠，因為它們將根據 `pvid` 中指定的 VLAN ID 動態新增為未標記埠，你只需將幹道埠指定為帶標籤埠。所有具有相同 `pvid` 設定的埠將作為未標記埠新增到一個條目中。你必須考慮到橋接本身也是一個埠，並且它也有 `pvid` 值，這意味著橋接埠也將為具有相同 `pvid` 的埠新增為未標記埠。你可以透過在所有埠（甚至幹道埠和橋接本身）上設定不同的 `pvid`，或使用 `frame-type` 設定為 `accept-only-vlan-tagged` 來規避此行為。
:::

### VLAN 示例 - 透過網橋進行 InterVLAN 路由 {#vlan-example---intervlan-routing-by-bridge}

![vlan_routing](/img/f659d62947a98802.webp)

建立一個停用 `vlan-filtering` 的網橋，以避免在 VLAN 完全配置完成之前失去對路由器的訪問。如果你需要對網橋進行管理訪問，請參閱[管理訪問配置](./index.md#management-access-configuration)部分。

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
```

新增網橋埠，併為 VLAN 接入埠指定 `pvid`，將其未標記流量分配到預期 VLAN。使用 `frame-types` 設定僅接受未標記封包。

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether6 pvid=200 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether7 pvid=300 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether8 pvid=400 frame-types=admit-only-untagged-and-priority-tagged
```

新增 Bridge VLAN 條目，並在其中指定帶標籤埠。在此示例中，**bridge1** 介面是 VLAN 中繼，將進一步轉發流量以執行 InterVLAN 路由。`frame-types` 設定為 `admit-only-untagged-and-priority-tagged` 的網橋埠將自動新增為 `pvid` VLAN 的未標記埠。

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1 vlan-ids=200
add bridge=bridge1 tagged=bridge1 vlan-ids=300
add bridge=bridge1 tagged=bridge1 vlan-ids=400
```

在 **bridge1** 上配置 VLAN 介面，以允許在路由層面處理帶標籤的 VLAN 流量，並設定 IP 地址以確保按計劃在 VLAN 之間進行路由。

```ros
/interface/vlan
add interface=bridge1 name=VLAN200 vlan-id=200
add interface=bridge1 name=VLAN300 vlan-id=300
add interface=bridge1 name=VLAN400 vlan-id=400

/ip/address
add address=20.0.0.1/24 interface=VLAN200
add address=30.0.0.1/24 interface=VLAN300
add address=40.0.0.1/24 interface=VLAN400
```

最後，當 VLAN 配置完成後，啟用 Bridge VLAN Filtering：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes 
```

可選步驟是在橋接介面上設定 `frame-types=admit-only-vlan-tagged`，以停用預設的未標記 VLAN 1（`pvid=1`）。

```ros
/interface/bridge/set bridge1 frame-types=admit-only-vlan-tagged
```

自 RouterOS v7 起，可以在某些裝置上使用 L3 硬體解除安裝來路由流量。更多詳情請參閱 [L3 硬體解除安裝](./l3-hardware-offloading.md)。

### 管理訪問配置 {#management-access-configuration}

在啟用了橋接 VLAN 過濾的裝置上，有多種方式可以設定管理訪問。以下是一些最常用的正確啟用路由器/交換器訪問的方法。首先建立一個未啟用 VLAN 過濾的橋接：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
```

#### 未啟用 VLAN 過濾的未標記訪問 {#untagged-access-without-vlan-filtering}

在橋接上未啟用 VLAN 過濾，且需要透過未標記流量進行管理訪問的情況下，配置很簡單。唯一必要的步驟是直接將 IP 地址分配給橋接介面本身。由於橋接在第 2 層執行且不帶 VLAN 標記，進入橋接埠的任何未標記流量都將能夠與分配給橋接介面的 IP 地址通訊，而無需額外配置。

```ros
/ip/address
add address=192.168.99.1/24 interface=bridge1
```

當 VLAN 過濾不屬於網路設計的一部分時，此方法提供了訪問路由器或交換器以進行管理的最簡單方式。

#### 未啟用 VLAN 過濾的標記訪問 {#tagged-access-without-vlan-filtering}

此方法用於需要透過帶標籤的 VLAN 流量管理路由器/交換器，但不啟用橋接 VLAN 過濾的場景。在這種情況下，會在橋接之上建立一個單獨的 VLAN 介面來處理帶標籤的管理流量。當您需要透過特定 VLAN ID 訪問裝置，同時保持橋接配置簡單直接時，這種方法很有用。

要配置帶標籤的管理訪問，首先在橋接上建立一個具有所需 VLAN ID 的 VLAN 介面，然後為該 VLAN 介面分配 IP 地址。這允許路由器透過帶標籤的 VLAN 可達，同時讓橋接保持預設狀態（未啟用 VLAN 過濾）。VLAN 介面充當邏輯子介面，並從父橋接介面繼承 MAC 地址。

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

此配置在橋接上建立一個管理 VLAN（VLAN 99），使裝置可透過任何承載 VLAN 99 帶標籤流量的埠在 IP 地址 192.168.99.1 訪問。

#### 帶 VLAN 過濾的帶標籤訪問 {#tagged-access-with-vlan-filtering}

在橋接上啟用了 VLAN 過濾且需要透過帶標籤流量進行管理訪問的場景中，需要額外的配置步驟。此方法允許您透過指定埠上的帶標籤流量，使用特定 VLAN ID（本例中為 VLAN 99）訪問路由器/交換器管理介面。

首先，在橋接之上建立一個 VLAN 介面併為其分配 IP 地址。此 VLAN 介面將處理帶標籤的管理流量：

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

接下來，必須向橋接 VLAN 表新增相應條目，以允許在將發起管理訪問的埠上傳輸帶標籤流量。例如，如果您需要透過 VLAN 99 帶標籤流量從埠 **ether3**、**ether4** 和 **sfp-sfpplus1** 訪問裝置，請將 **bridge1** 介面本身包含在標記埠列表中（橋接介面必須被標記，以允許 VLAN 介面與交換器 CPU 通訊）：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,ether3,ether4,sfp-sfpplus1 vlan-ids=99
```

在 VLAN 表正確配置後，您可以在橋接上啟用 VLAN 過濾：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

此配置允許透過帶標籤的 VLAN 99 流量進行管理訪問，同時保留 VLAN 過濾的安全優勢。網橋介面本身作為帶標籤成員包含在內，以確保 VLAN 介面與交換器 CPU 之間為路由和管理目的進行正確通訊。

### 使用 VLAN 過濾的未標記訪問 {#untagged-access-with-vlan-filtering}

啟用網橋 VLAN 過濾後，當您需要使用未標記流量訪問裝置時，必須確保管理 VLAN 介面使用與未標記埠 VLAN ID 相同的 VLAN ID（透過 `pvid` 引數配置）。這可確保來自接入埠的未標記流量能夠與路由器的管理介面正確通訊。

首先，在網橋上建立 VLAN 介面併為其分配 IP 地址，就像上一個示例中那樣。此 VLAN 介面將處理管理流量：

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

例如，如果您希望未標記埠 **ether2** 和 **ether3** 能夠與 VLAN 99 管理介面通訊，則這些埠必須配置為與管理 VLAN ID 匹配的 `pvid` 值。此外，您需要將網橋介面本身作為帶標籤埠成員新增到 VLAN 表中，這允許路由器處理帶標籤的管理流量。如有需要，您還可以為特定網路拓撲新增其他帶標籤埠（有關帶標籤埠配置的更多詳細資訊，請參見前面的示例）：

```ros
/interface/bridge/port
set [find interface=ether2] pvid=99
set [find interface=ether3] pvid=99
/interface/bridge/vlan 
add bridge=bridge1 tagged=bridge1 untagged=ether2,ether3 vlan-ids=99
```

完成 VLAN 表配置後，您可以在網橋上啟用 VLAN 過濾。這將啟用所有與 VLAN 相關的功能，並開始根據您的 VLAN 設定過濾流量：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes 
```

#### 更改網橋介面的未標記 VLAN {#changing-untagged-vlan-for-the-bridge-interface}

在使用 VLAN 過濾的情況下，可以使用 `pvid` 設定更改網橋介面的未標記 VLAN ID。請注意，建立可路由 VLAN 介面並允許網橋上的帶標籤流量是更靈活且通常推薦的做法。

首先，在網橋介面上建立一個 IP 地址。

```ros
/ip/address
add address=192.168.99.1/24 interface=bridge1
```

例如，未標記的 **bridge1** 流量應能與 VLAN 99 中未標記的 **ether2** 和 **ether3** 埠以及已標記的 **sfp-sfpplus1** 埠通訊。為實現這一點，**bridge1**、**ether2**、**ether3** 應配置相同的 `pvid`，並且應將 sfp-sfpplus1 新增為標記成員。

```ros
/interface/bridge
set [find name=bridge1] pvid=99
/interface/bridge/port
set [find interface=ether2] pvid=99
set [find interface=ether3] pvid=99
/interface/bridge/vlan
add bridge=bridge1 tagged=sfp-sfpplus1 untagged=bridge1,ether2,ether3 vlan-ids=99
```

之後，您可以啟用 VLAN 過濾：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes 
```

:::warning
如果不需要透過 IP 地址連線到路由器/交換器，則可以跳過新增 IP 地址的步驟，因為透過二層協定（例如 MAC-telnet）連線到路由器/交換器無論如何都可以工作。
:::

### VLAN 隧道 (QinQ) {#vlan-tunneling-qinq}

從 RouterOS v6.43 起，RouterOS 網橋符合 IEEE 802.1ad，並且可以基於服務 VLAN ID (0x88a8) 而不是客戶 VLAN ID (0x8100) 來過濾 VLAN ID。可以應用與 IEEE 802.1Q VLAN 過濾相同的原則（可以使用相同的設定示例）。下面是一個常見 **提供商網橋** 的拓撲：

![Provider_bridge](/img/0285416b3135c6c9.webp)

在此示例中，**R1**、**R2**、**R3,** 和 **R4** 可能透過 802.1Q (CVID) 傳送任何 VLAN 標記流量，但 **SW1** 和 **SW2** 需要以某種方式隔離路由器之間的流量，使 **R1** 只能與 **R3** 通訊，而 **R2** 只能與 **R4** 通訊。為此，您可以用 SVID 標記所有入口流量，並僅在某些埠上允許這些 VLAN。首先在網橋上啟用由 `802.1ad` 引入的服務標籤 0x88a8。在 **SW1** 和 **SW2** 上使用以下命令：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no ether-type=0x88a8
```

在此設定中，**ether1** 和 **ether2** 將成為接入埠（未標記），使用 `pvid` 引數為每個埠上的所有入口流量打標籤，在 **SW1** 和 **SW2** 上使用以下命令：

```ros
/interface/bridge/port
add interface=ether1 bridge=bridge1 pvid=200
add interface=ether2 bridge=bridge1 pvid=300
add interface=ether3 bridge=bridge1
```

在網橋 VLAN 表中指定標記和未標記埠。在 **SW1** 和 **SW2** 上使用以下命令：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether3 untagged=ether1 vlan-ids=200
add bridge=bridge1 tagged=ether3 untagged=ether2 vlan-ids=300
```

配置好網橋 VLAN 表後，即可啟用網橋 VLAN 過濾。請在 **SW1** 和 **SW2** 上使用以下命令：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes 
```

:::danger
透過啟用 vlan-filtering，你將過濾掉髮往 CPU 的流量。在啟用 VLAN 過濾之前，應確保設定了管理埠。

請注意，如果你使用新的 EtherType/TPID 0x88a8（服務標籤）並且還需要為服務 VLAN 使用 VLAN 介面，則還必須在 VLAN 介面上應用 `use-service-tag` 引數。
:::

:::danger
當配置 `ether-type=0x8100` 時，橋接檢查外部 VLAN 標籤以確定它是否使用 EtherType `0x8100`。如果橋接收到外部標籤具有不同 EtherType 的封包，它會將該封包標記為 `untagged`。由於 RouterOS 僅檢查封包的外部標籤，因此在使用 802.1ad 協定時無法過濾 802.1Q 封包。
:::

:::warning
目前，只有配備 Marvell Prestera 交換器的 MikroTik 裝置能夠使用服務標籤 EtherType/TPID `0x88a8` 進行硬體解除安裝的 VLAN 過濾。
:::

:::danger
配備 Marvell-98DX3257 交換器晶片的裝置（例如 CRS354 系列）不支援在 1Gbps 乙太網介面上對其他 VLAN 型別（`0x88a8` 和 `0x9100`）進行 VLAN 過濾。
:::

### 標籤堆疊 {#tag-stacking}

自 RouterOS v6.43 起，可以在任何現有 VLAN 標籤之上強制新增新的 VLAN 標籤。此功能可用於實現 CVID 堆疊方案，即在現有 CVID 標籤之前新增一個 CVID（0x8100）標籤。此類方案與 Provider bridge 方案非常相似。要實現相同的方案但使用多個 CVID 標籤（CVID 堆疊），我們可以使用相同的拓撲：

![Tag_stacking](/img/ed256f307c0776d1.webp)

在此示例中，**R1**、**R2**、**R3** 和 **R4** 可能傳送任何 VLAN 標記的流量，可以是 802.1ad、802.1Q 或任何其他型別的流量，但 **SW1** 和 **SW2** 需要以某種方式隔離路由器之間的流量，使 **R1** 只能與 **R3** 通訊，而 **R2** 只能與 **R4** 通訊。為此，您可以為所有入站流量打上新的 CVID 標籤，並僅在特定埠上允許這些 VLAN。首先選擇合適的 EtherType，請在 **SW1** 和 **SW2** 上使用以下命令：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no ether-type=0x8100
```

在此方案中，**ether1** 和 **ether2** 將忽略所有已存在的 VLAN 標籤，並新增一個新的 VLAN 標籤。使用 `pvid` 引數為每個埠上的所有入站流量打標籤，並在這些埠上允許 `tag-stacking`。請在 **SW1** 和 **SW2** 上使用以下命令：

```ros
/interface/bridge/port
add interface=ether1 bridge=bridge1 pvid=200 tag-stacking=yes
add interface=ether2 bridge=bridge1 pvid=300 tag-stacking=yes
add interface=ether3 bridge=bridge1
```

在網橋 VLAN 表中指定帶標籤和不帶標籤的埠。您只需指定外層標籤的 VLAN ID。請在 **SW1** 和 **SW2** 上使用以下命令：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether3 untagged=ether1 vlan-ids=200
add bridge=bridge1 tagged=ether3 untagged=ether2 vlan-ids=300
```

配置好網橋 VLAN 表後，即可啟用網橋 VLAN 過濾，這是使 pvid 引數生效所必需的。請在 **SW1** 和 **SW2** 上使用以下命令：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

:::danger
透過啟用 vlan-filtering，你將過濾掉髮往 CPU 的流量；在啟用 VLAN 過濾之前，應確保設定了管理埠。
:::

### MVRP {#mvrp}

多 VLAN 註冊協定（MVRP）是一種基於多註冊協定（MRP）的協定，它允許向橋接區域網路的其他成員註冊屬性（在 MVRP 的情況下為 VLAN ID）。

MRP 應用可以做出或撤回屬性宣告，從而導致這些屬性在其他 MRP 參與者處被註冊或離開。

其工作原理如下。

MRP 由兩部分組成：

- **Applicant** - 負責傳送宣告（或離開）。其行為可以基於每個埠透過名為 `mvrp-applicant-state` 的設定進行配置，並基於每個 VLAN 透過 `mvrp-forbidden` 設定進行配置。
- **Registrar** - 負責註冊傳入的宣告。其配置可以基於每個埠透過 `mvrp-registrar-state` 設定進行設定，並基於每個 VLAN 透過 `mvrp-forbidden` 設定進行設定。

**註冊傳播：** 橋接埠上傳入的註冊會動態地將該特定埠變為帶標籤的 VLAN 成員。此外，與此註冊相關聯的屬性會作為宣告傳播到所有活動（轉發）橋接埠。

**宣告操作：** 在 MVRP 的情況下，已配置的 VLAN 會在每個埠上被宣告，但只有當從 LAN 收到宣告時，它們才會被配置為這些 VLAN 的成員（Registrar 將註冊該 VLAN）。從終端站的角度來看，單個宣告將在整個 LAN 中的每個上游埠上被註冊。當另一個終端站宣告相同的屬性時，這兩個（或更多）終端站之間將建立一條註冊路徑，見下圖。

MVRP 有助於在整個橋接網路中動態傳播 VLAN 資訊，並且僅在需要的埠上配置 VLAN。這透過避免不必要的流量泛洪使網路更加高效。

如前所述，MVRP 僅在處於轉發狀態的埠上活動。對於 MSTP，只有在埠於 VLAN 所對映到的 MSTI 中處於轉發狀態時，才會進行宣告和註冊。

點對點埠會加快註冊（或離開）過程。對於非乙太網介面，手動配置 `point-to-point=yes` 可能是有益的。

![MVRP](/img/33d81c5bbb103a21.webp)

#### 屬性參考 {#property-reference}

**子選單：** `/interface/bridge`

| 屬性 | 描述 |
| :-- | :-- |
| **mvrp** (*yes* \| *no*; 預設：**no**) | 為網橋啟用 MVRP。它確保 MAC 地址 01:80:C2:00:00:21 被捕獲而不被轉發。必須啟用 `vlan-filtering`。 |

**子選單：** `/interface/bridge/port`

埠選單允許按埠控制 applicant 和 registrar 設定。

| 屬性 | 描述 |
| :-- | :-- |
| **mvrp-applicant-state** (*non-participant \| normal-participant;* 預設：**normal-participant**) | MVRP applicant 選項： <br/><ul><li><strong>non-participant</strong> - 埠不傳送任何 MRP 訊息；</li><li><strong>normal-participant </strong>- 埠正常參與 MRP 交換。</li></ul> |
| **mvrp-registrar-state** (*fixed \| normal*; 預設：**normal**) | MVRP registrar 選項： <br/><ul><li><strong>fixed</strong> - 埠忽略所有 MRP 訊息，並在所有已配置的 VLAN 中保持 Registered (IN)。</li><li><strong>normal </strong>- 埠接收 MRP 訊息，並根據標準處理它們。</li></ul> |

要監控當前已宣告和註冊的 VLAN ID，請使用 `monitor` 命令。

```ros
[admin@MikroTik] > /interface/bridge/port/monitor [find interface=sfp-sfpplus1]
            interface: sfp-sfpplus1
               status: in-bridge
          port-number: 1
                 role: designated-port
            edge-port: no
  edge-port-discovery: yes
  point-to-point-port: yes
         external-fdb: no
         sending-rstp: yes
             learning: yes
           forwarding: yes
     actual-path-cost: 2000
     hw-offload-group: switch1
    declared-vlan-ids: 1,10,20-21
  registered-vlan-ids: 1,10,20,30-33
```

**子選單：** `/interface/bridge/vlan`

所有屬於靜態 VLAN 成員或由埠 `pvid` 設定建立的動態未標記 VLAN 成員的埠都被視為“固定”。這意味著註冊器會忽略所有 MRP 訊息，併為這些 VLAN 保持已註冊（IN）狀態。

當某個 VLAN 既未手動配置，也不是由埠 `pvid` 設定建立時，橋接埠上的傳入註冊可以動態地將該特定埠指定為帶標記的 VLAN 成員。`mvrp-forbidden` 功能允許建立一組埠，這些埠被限制註冊特定的 VLAN ID。

靜態或動態 VLAN 將由申請者宣告，除非此功能被埠的 `mvrp-applicant-state` 或 VLAN 的 `mvrp-forbidden` 設定停用。

| 屬性 | 描述 |
| :-- | :-- |
| **mvrp-forbidden** (*interfaces*; 預設: ) | 忽略所有 MRP 訊息並保持未註冊（MT）狀態，同時禁止申請者宣告特定 VLAN ID 的埠。 |

**子選單：** `/interface/bridge/vlan/mvrp`

MVRP 屬性選單可用於檢視內部 MVRP 屬性狀態，如 IEEE 802.1Q-2011 所規定。

| 屬性 | 描述 |
| :-- | :-- |
| **applicant-state** | 宣告屬性的 Applicant 狀態機。其狀態可以是 VO、VP、VN、AN、AA、QA、LA、AO、QO、AP、QP 或 LO。每個狀態由兩個字母組成。 <br/> 第一個字母表示狀態： <br/><ul><li>V—非常急切；</li><li>A—急切；</li><li>Q—安靜；</li><li>L—離開。</li></ul> 第二個字母表示成員狀態： <br/><ul><li>A - 活動成員；</li><li>P - 被動成員；</li><li>O - 觀察者；</li><li>N - 新。</li></ul> 例如，VP 表示“非常急切，被動成員”。 |
| **registrar-state** | 記錄其他參與者所宣告屬性註冊狀態的 Registrar 狀態機。其狀態可以是 IN、LV 或 MT： <br/><ul><li>IN—已註冊；</li><li>LV—先前已註冊，但當前正在超時；</li><li>MT—未註冊。</li></ul> |

```ros
[admin@Mikrotik] /interface/bridge/vlan/mvrp/print where vlan-id=10
Columns: BRIDGE, PORT, VLAN-ID, REGISTRAR-STATE, APPLICANT-STATE, LAST-EVENT
 #  BRIDGE    PORT           VLAN-ID  REGISTRAR-STATE  APPLICANT-STATE  LAST-EVENT
 1  bridge67  sfp-sfpplus1        10  IN               Quiet Active     JoinIn    
 9  bridge67  sfp-sfpplus5        10  MT               Quiet Active     JoinEmpty 
17  bridge67  sfp-sfpplus9        10  MT               Quiet Active     JoinEmpty 
25  bridge67  sfp-sfpplus13       10  IN               Quiet Active     JoinIn 
```

## 快速轉發 {#fast-forward}

---

Fast Forward 允許在特殊條件下更快地轉發封包。啟用 Fast Forward 後，網橋可以更快地處理封包，因為它可以跳過多個與網橋相關的檢查，包括 MAC 學習。下面列出了為使 Fast Forward 處於活動狀態而**必須**滿足的條件：

- 網橋的 `fast-forward` 設定為 `yes`。
- 網橋只有 2 個執行中的埠。
- 兩個網橋埠都支援 [Fast Path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path)，Fast Path 在埠上以及網橋上全域性處於活動狀態。
- 網橋硬體解除安裝已停用。
- 網橋 VLAN 過濾已停用。
- 網橋 DHCP snooping 已停用。
- `unknown-multicast-flood` 設定為 `yes`。
- `unknown-unicast-flood` 設定為 `yes`。
- `broadcast-flood` 設定為 `yes`。
- 網橋的 MAC 地址與其中一個網橋從埠的 MAC 地址匹配。
- 兩個埠的 `horizon` 都設定為 `none`。

:::warning
快速轉發會停用 MAC 學習；這是為了更快地轉發封包而設計的。MAC 學習可防止流量泛洪到多個介面，但當封包只能透過一個介面傳送時，不需要 MAC 學習。
:::

:::danger
啟用硬體解除安裝時，快速轉發被停用。硬體解除安裝在活動時可以實現全線速效能，因為它將使用內建交換器晶片（如果你的裝置存在這樣的晶片）。快速轉發使用 CPU 轉發封包。比較吞吐量結果時，你會得到這樣的結果：硬體解除安裝 > 快速轉發 > Fast Path > 慢速路徑。
:::

可以檢查 Fast Forward 處理了多少個數據包：

```ros
[admin@MikroTik] /interface/bridge/settings> pr
              use-ip-firewall: no
     use-ip-firewall-for-vlan: no
    use-ip-firewall-for-pppoe: no
              allow-fast-path: yes
      bridge-fast-path-active: yes
     bridge-fast-path-packets: 0
       bridge-fast-path-bytes: 0
  bridge-fast-forward-packets: 16423
    bridge-fast-forward-bytes: 24864422
```

:::warning
如果封包由 Fast Path 處理，則快速轉發未活動。封包計數可用作快速轉發是否活動的指標。
:::

自 RouterOS 6.44 起，可以監控 Fast Forward 狀態，例如：

```ros
[admin@MikroTik] /interface/bridge/monitor bridge1 
                  state: enabled
    current-mac-address: B8:69:F4:C9:EE:D7
            root-bridge: yes
         root-bridge-id: 0x8000.B8:69:F4:C9:EE:D7
         root-path-cost: 0
              root-port: none
             port-count: 2
  designated-port-count: 2
           fast-forward: yes
```

:::danger
停用或啟用快速轉發將臨時停用所有橋接埠以使設定生效。在生產環境中更改此屬性時必須考慮到這一點，因為它可能導致所有封包被臨時丟棄。
:::

## IGMP/MLD 監聽 {#igmpmld-snooping}

---

網橋支援 IGMP/MLD snooping。它控制組播流並防止在不需要的埠上進行組播泛洪。其設定位於網橋選單中，並且在每個網橋介面上獨立工作。軟體驅動的實現可在所有執行 RouterOS 的裝置上工作，但配備 Marvell Prestera 交換晶片以及 88E6393X、88E6191X、88E6190 交換晶片的 MikroTik 裝置還支援帶硬體解除安裝的 IGMP/MLD snooping。更多詳細資訊請參閱 [IGMP/MLD snooping 手冊](./user-guides/bridge-igmp-mld-snooping.md)。

## DHCP Snooping 與 DHCP Option 82 {#dhcp-snooping-and-dhcp-option-82}

---

網橋支援 DHCP Snooping 和 DHCP Option 82。DHCP Snooping 是一種二層安全功能，用於阻止未經授權的 DHCP 伺服器向用戶提供惡意資訊。在 RouterOS 中，你可以指定哪些網橋埠是受信任的（已知 DHCP 伺服器所在的位置，DHCP 訊息應被轉發），哪些是不受信任的（通常用於接入埠，收到的 DHCP 伺服器訊息將被丟棄）。DHCP Option 82 是由啟用了 DHCP Snooping 的裝置提供的附加資訊（Agent Circuit ID 和 Agent Remote ID），用於標識裝置本身和 DHCP 用戶端。

![Dhcp_snooping](/img/1e3b5abc626baf0c.webp)

在本示例中，SW1 和 SW2 是啟用了 DHCP Snooping 和 Option 82 的裝置。首先，我們需要建立一個網橋、分配介面並標記受信任的埠。在 **SW1** 上使用以下命令：

```ros
/interface/bridge
add name=bridge
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2 trusted=yes
```

對於 SW2，配置將類似，但我們還需要將 ether1 標記為受信任，因為該介面將接收已新增 Option 82 的 DHCP 訊息。如果所有埠都將接收添加了 Option 82 的 DHCP 訊息，則需要將它們全部標記為受信任，否則這些訊息將被丟棄。此外，我們將 ether3 新增到同一個網橋，並將該埠保持為不受信任，設想存在一個未經授權的（惡意）DHCP 伺服器。在 **SW2** 上使用以下命令：

```ros
/interface/bridge
add name=bridge
/interface/bridge/port
add bridge=bridge interface=ether1 trusted=yes
add bridge=bridge interface=ether2 trusted=yes
add bridge=bridge interface=ether3
```

然後我們需要啟用 DHCP Snooping 並配置 Option 82。從 RouterOS 7.23 版本開始，可以使用預定義變數（如 BRIDGEMAC、HOSTNAME、INTERFACE、VID）配置自定義的 Remote ID 和 Circuit ID 值。更多詳細資訊請參閱 `dhcp-agent-circuit-id`、`dhcp-agent-remote-id` 屬性。如果你的 DHCP 伺服器不支援 DHCP Option 82，或者你不實施任何與 Option 82 相關的策略，則此步驟不是必需的。在此配置示例中，我們在 **SW1** 和 **SW2** 上使用以下命令：

```ros
/interface/bridge
set [find where name="bridge"] dhcp-snooping=yes dhcp-agent-circuit-id="interface: \$(INTERFACE), vlan: \$(VID)" dhcp-agent-remote-id="ip: 192.168.88.1, identity: \$(HOSTNAME), mac: \$(BRIDGEMAC)"
```

現在兩臺裝置都將分析在網橋埠上收到的 DHCP 訊息。**SW1** 負責新增和刪除 DHCP Option 82。**SW2** 將限制惡意 DHCP 伺服器接收任何發現訊息，並丟棄來自 ether3 的惡意 DHCP 伺服器訊息。

:::warning
目前，配備 Marvell Prestera 交換器以及 88E6393X、88E6191X、88E6190 交換器晶片的 MikroTik 裝置完全支援硬體解除安裝的 DHCP 監聽和 Option 82。對於 CRS1xx 和 CRS2xx 系列交換器，可以將 DHCP 監聽與 VLAN 交換一起使用，但你需要確保使用出口 ACL 規則以正確的 VLAN 標籤傳送 DHCP 封包。其他裝置能夠使用 DHCP 監聽和 Option 82 功能以及硬體解除安裝，但你必須確保裝置上沒有應用與 VLAN 相關的配置，否則 DHCP 監聽和 Option 82 可能無法正常工作。請參閱橋接硬體解除安裝部分及支援的功能。
:::

:::info
從 RouterOS v7.17 開始，在 bonding 介面上支援帶硬體解除安裝的 DHCP 監聽。
:::

### DHCP Snooping 繫結表 {#dhcp-snooping-binding-table}

DHCP snooping 繫結資料庫是由網橋生成的執行時表，用於儲存連線到受信任埠的 DHCP 伺服器所提供的 DHCP 租約。每個條目記錄用戶端的 MAC 地址、分配的 IP 地址、租約到期時間、VLAN ID 以及發現用戶端所在的物理介面。網橋可以利用該資料庫來增強安全性。即，當幀到達不受信任的埠時，交換器會在轉發封包之前驗證源 MAC/IP 對是否與儲存的繫結匹配，從而阻止來自惡意 DHCP 伺服器或偽造主機的流量，防止地址盜用攻擊，並啟用諸如 IP-Source-Guard、ARP-Inspection 等功能。

當前 DHCPv4 snooping 繫結表的實現建立在現有的 `/interface/bridge/host` 表之上。相關的 DHCP 資訊從經過網橋的 DHCP 訊息中獲取。

:::danger
橋接收集並在繫結表中彙總的 DHCP 相關資訊在每次停用橋接或僅停用 DHCP 監聽時都會丟失。
:::

DHCP 用戶端的當前狀態由 `dhcpv4-status` 指示。可能的狀態值如下：`searching`、`requesting`、`bound`、`renewing`、`rebinding`、`expired` 和 `relay-agent`。最後一個值僅當從隱藏在中繼代理後面的 DHCP 用戶端收到 DHCP 請求訊息時才會出現。

`dhcpv4-ip` 顯示 DHCP 伺服器授予的 IP 地址，而 `dhcpv4-server-id` 列指示伺服器 ID。`dhcpv4-expires-after` 列顯示 DHCP 伺服器提供給用戶端的當前租約期還剩多少時間。

當在網橋上啟用 VLAN 過濾時，每個主機不僅透過其 MAC 地址標識，還透過 MAC - VLAN ID 對標識。

WinBox 中的活動 DHCP 繫結表條目：

![FDB with DHCP binding table in Winbox](/img/a51a51d564206202.png)

控制檯中的活動 DHCP 繫結表條目：

![FDB with DHCP binding table in console](/img/509a91e9576f9771.png)

## DHCPv6 偵聽 / DHCPv6 防護 {#dhcpv6-snooping--dhcpv6-shield}

DHCPv6 Snooping 是一種二層安全功能，可防止未經授權的 DHCPv6 伺服器向用戶提供惡意資訊。在 RouterOS 中，您可以指定哪些網橋埠是受信任的（已知 DHCPv6 伺服器所在且應轉發 DHCPv6 訊息的位置），以及哪些是不受信任的（通常用於接入埠，收到的 DHCPv6 伺服器訊息將被丟棄，從而有效實現 DHCPv6-Shield）。

DHCPv6 Option 18 (Interface-Id) 和 Option 37 (Remote-Id) 是由啟用了 DHCPv6 Snooping 的裝置提供的附加資訊，可用於識別裝置本身和 DHCPv6 用戶端。

IPv6 為 DHCPv6 Relay agent 過程提供了更細粒度的方法以及靈活性。在功能上，它們與 IPv4 的 Option 82 用途完全相同：Option 18 充當 Circuit ID（標識用戶端連線的特定埠/VLAN），Option 37 充當 Remote ID（標識中繼代理或交換器硬體本身）。

- Option 18 - 標識接收用戶端訊息的特定介面（埠）。它確保伺服器確切知道請求來自何處，以便應用正確的策略。
- Option 37 - 標識中繼代理（交換器或路由器）本身。它包含唯一的 caller ID（例如 DUID——DHCP 唯一識別符號）。它告知伺服器網路中的哪個特定裝置正在與它通訊。

## RA 防護 {#ra-guard}

---

RA guard 功能旨在丟棄到達使用者指定為不受信任的橋接埠的、包含路由器通告（RA）訊息的 IPv6 封包，從而防止潛在的惡意 RA 訊息攻擊或意外的網路配置錯誤。啟用後，可以將每個橋接埠設定為受信任或不受信任（預設情況下，所有橋接埠都設定為 RA 不受信任）。

以下是 IPv6 RA Guard (Router Advertisement Guard) 背後的網路方案和核心原理。

![RAguard](/img/0db2c93dce1fec4d.webp)

|  |
| :-- |
| <br/><code>#Layer 2 Access Switch - enabling RA guard on the main bridge</code><br/><code>/interface/bridge</code><br/><code>add name=bridge</code><br/><code>/interface/bridge</code><br/><code>set [find where name="bridge"] ra-guard=yes</code><br/><code>/interface/bridge/port</code><br/><code>add bridge=bridge interface=etherUplink Trusted RA=yes</code><br/><code>add bridge=bridge interface=etherX</code><br/><code>add bridge=bridge interface=etherY</code><br/><code>add bridge=bridge interface=etherZ</code><br/> |

### 問題：為什麼需要這個？ {#the-problem-why-is-this-needed}

在 IPv6 中，裝置使用 ICMPv6 進行自動配置。

路由器通告（Type 134）：路由器廣播這些訊息來告知主機：“我是閘道器，這是你的網路字首。”

威脅：如果使用者意外將消費級路由器（例如家庭 Wi-Fi 路由器）連線到接入埠，或者惡意行為者在接入埠上啟動工具（例如 `Rogue RA`），該裝置就會開始廣播 RA。

結果：網路中的其他主機會根據該非授權裝置自動配置其 IPv6 地址，並將該非授權裝置設定為預設閘道器。這會導致中間人攻擊或完全拒絕服務。

以下是網路方案以及 IPv6 RA Guard（Router Advertisement Guard）背後的核心原理。

### 核心原則：“信任與非信任” {#the-core-principle-trust-vs-untrust}

IPv6 RA Guard 的基本原理在邏輯上與 IPv4 中的 DHCP Snooping 完全相同。它透過將交換器埠劃分為兩種角色，在第 2 層交換器基礎設施內建立安全邊界：

- 受信任埠：連線到合法、授權 IPv6 路由器的埠。允許這些埠傳送 Router Advertisement（RA）封包。
- 不受信任埠：連線到終端使用者主機的埠。禁止這些埠傳送 RA 封包。

### 封包解析過程 {#packet-parsing-process}

對於未配置為 RA Trusted 的埠，RA Guard 解析器會遍歷擴充套件頭鏈，直到遇到非擴充套件頭。解析過程及後續操作由以下規則控制：

**傳輸層終止**：如果解析器遇到有效的傳輸層頭——例如 TCP、UDP、ESP、RSVP 或封裝的 IPv4/IPv6 頭——則解析終止，並且封包被轉發（受標準網橋檢查約束）。

- 丟棄條件 - 如果出現以下情況，則丟棄封包：

1. 未能包含傳輸層頭。
2. 鏈中的最後一個擴充套件頭在其 "Next Header" 欄位中未指定 NO\_NEXT\_HEADER (59)。
3. 如果發現 ICMP 訊息型別為 134，則丟棄封包。

- 分片處理：這些解析規則僅適用於分片 IPv6 封包的第一個分片。後續分片無論其內容如何都會被轉發，因為它們不包含識別 RA 所需的協定頭。

## 網橋防火牆 {#bridge-firewall}

---

網橋防火牆實現封包過濾，從而提供用於管理到網橋、來自網橋以及穿過網橋的資料流的安全功能。

[封包流程圖](../firewall-and-quality-of-service/packet-flow-in-routeros.md)展示了封包如何經過路由器處理。可以強制網橋流量經過 `/ip/firewall/filter` 規則（請參閱網橋設定）。

有兩個網橋防火牆表：

- **filter** - 具有三個預定義鏈的網橋防火牆：
  - **input** - 過濾封包，其目的地為網橋（包括將被路由的封包，因為它們無論如何都發往網橋 MAC 地址）。
  - **output** - 過濾來自網橋的封包（包括已正常路由的封包）。
  - **forward** - 過濾將要被橋接的封包（注意：該鏈不適用於應透過路由器路由的封包，只適用於在同一網橋的埠之間穿行的封包）。
- **nat** - 網橋網路地址轉換提供了更改穿過網橋的封包的源/目標 MAC 地址的方法。有兩個內建鏈：
  - **srcnat** - 用於將主機或網路“隱藏”在不同的 MAC 地址之後。該鏈應用於透過橋接介面離開路由器的封包。
  - **dstnat** - 用於將某些封包重定向到其他目的地。

你可以在網橋防火牆（filter 和 NAT）中放置封包標記，這些標記與由 `'/ip/firewall/mangle'` 配置的 IP 防火牆中的封包標記相同。透過這種方式，網橋防火牆設定的封包標記可以在“IP 防火牆”中使用，反之亦然。

本節介紹網橋防火牆的通用屬性。nat 和 filter 規則之間不同的某些引數將在後續章節中介紹。

**子選單：** `/interface/bridge/filter, /interface/bridge/nat`

| 屬性 | 描述 |
| :-- | :-- |
| **802.3-sap** (*integer*; Default: ) | DSAP（Destination Service Access Point）和 SSAP（Source Service Access Point）是 2 個單位元組欄位，用於標識使用鏈路層服務的網路協定實體。這兩個位元組始終相等。此處可指定兩個十六進位制數字以匹配 SAP 位元組。 |
| **802.3-type** (*integer*; Default: ) | Ethernet 協定型別，位於 IEEE 802.2 幀頭之後。僅在 802.3-sap 為 0xAA（SNAP - Sub-Network Attachment Point 報頭）時有效。例如，AppleTalk 可由 SAP 程式碼 0xAA 後跟 SNAP 型別程式碼 0x809B 來表示。 |
| **action** (*accept \| drop \| jump \| log \| mark-packet \| passthrough \| return \| set-priority*; Default: ) | 封包與規則匹配時要執行的操作：<ul><li>accept - 接受封包。該封包不會傳遞給下一條防火牆規則</li><li>drop - 靜默丟棄封包</li><li>jump - 跳轉到由 <span className="ros-icon-success"><code>jump-target</code></span> 引數值指定的使用者定義鏈</li><li>log - 將包含以下資料的訊息新增到系統日誌：in-interface、out-interface、src-mac、protocol、src-ip:port-&gt;dst-ip:port 以及封包長度。封包匹配後，會像 <span className="ros-icon-success"><code>passthrough</code></span> 一樣傳遞給列表中的下一條規則</li><li>mark-packet - 在匹配規則的封包上放置由 new-packet-mark 引數指定的標記</li><li>passthrough - 如果封包匹配該規則，則增加計數器並轉到下一條規則（用於統計）</li><li>return - 將控制權返回到發生跳轉的鏈</li><li>set-priority - 在為能夠傳輸優先順序的鏈路（VLAN 或啟用 WMM 的無線介面）傳送的封包上，設定由 new-priority 引數指定的優先順序。[閱讀更多](./user-guides/wmm-and-vlan-priority.md)</li></ul> |
| **arp-dst-address** (*IP address*; Default: ) | ARP 目標 IP 地址。 |
| **arp-dst-mac-address** (*MAC address*; Default: ) | ARP 目標 MAC 地址。 |
| **arp-gratuitous** (*yes \| no*; Default: ) | 匹配 ARP 免費封包。 |
| **arp-hardware-type** (*integer*; Default: **1**) | ARP 硬體型別。通常為 Ethernet（型別 1）。 |
| **arp-opcode** (*arp-nak \| drarp-error \| drarp-reply \| drarp-request \| inarp-reply \| inarp-request \| reply \| reply-reverse \| request \| request-reverse*; Default: ) | ARP 操作碼（封包型別）<ul><li>arp-nak - 否定 ARP 應答（很少使用，主要用於 ATM 網路）</li><li>drarp-error - 動態 RARP 錯誤程式碼，表示無法為給定 MAC 地址分配 IP 地址</li><li>drarp-reply - 動態 RARP 應答，為主機分配臨時 IP 地址</li><li>drarp-request - 動態 RARP 請求，為給定 MAC 地址分配臨時 IP 地址</li><li>inarp-reply - InverseARP 應答</li><li>inarp-request - InverseARP 請求</li><li>reply - 帶有 MAC 地址的標準 ARP 應答</li><li>reply-reverse - 帶有已分配 IP 地址的反向 ARP（RARP）應答</li><li>request - 向已知 IP 地址發出的標準 ARP 請求，以找出未知 MAC 地址</li><li>request-reverse - 向已知 MAC 地址發出的反向 ARP（RARP）請求，以找出未知 IP 地址（旨在供主機用來發現自己的 IP 地址，類似於 DHCP 服務）</li></ul> |
| **arp-packet-type** (*integer 0..65535 \| hex 0x0000-0xffff*; Default: ) | ARP 封包型別。 |
| **arp-src-address** (*IP address*; Default: ) | ARP 源 IP 地址。 |
| **arp-src-mac-address** (*MAC addres*; Default: ) | ARP 源 MAC 地址。 |
| **chain** (*text*; Default: ) | 過濾器所生效的網橋防火牆鏈（內建鏈或使用者定義鏈）。 |
| **dst-address** (*IP address*; Default: ) | 目標 IP 地址（僅當 MAC 協定設定為 IP 時）。 |
| **dst-address6** (*IPv6 address*; Default: ) | 目標 IPv6 地址（僅當 MAC 協定設定為 IPv6 時）。 |
| **dst-mac-address** (*MAC address*; Default: ) | 目標 MAC 地址。 |
| **dst-port** (*integer 0..65535*; Default: ) | 目標埠號或範圍（僅適用於 TCP 或 UDP 協定）。 |
| **in-bridge** (*name*; Default: ) | 封包進入所經過的網橋介面。 |
| **in-bridge-list** (*name*; Default: ) | 在介面列表中定義的網橋介面集合。工作方式與 `in-bridge` 相同。 |
| **in-interface** (*name*; Default: ) | 封包進入所經過的物理介面（即網橋埠）。 |
| **in-interface-list** (*name*; Default: ) | 在介面列表中定義的介面集合。工作方式與 `in-interface` 相同。 |
| **ingress-priority** (*integer 0..63*; Default: ) | 匹配入站封包的優先順序。優先順序可來自 VLAN、WMM、DSCP 或 MPLS EXP 位。[閱讀更多](./user-guides/wmm-and-vlan-priority.md) |
| **ip-protocol** (*dccp \| ddp \| egp \| encap \| etherip \| ggp \| gre \| hmp \| icmp \| icmpv6 \| idpr-cmtp \| igmp \| ipencap \| ipip \| ipsec-ah \| ipsec-esp \| ipv6 \| ipv6-frag \| ipv6-nonxt \| ipv6-opts \| ipv6-route \| iso-tp4 \| l2tp \| ospf \| pim \| pup \| rdp \| rspf \| rsvp \| sctp \| st \| tcp \| udp \| udp-lite \| vmtp \| vrrp \| xns-idp \| xtp*; Default: ) | IP 協定（僅當 MAC 協定設定為 IPv4 時）<ul><li>dccp - Datagram Congestion Control Protocol</li><li>ddp - Datagram Delivery Protocol</li><li>egp - Exterior Gateway Protocol</li><li>encap - Encapsulation Header</li><li>etherip - Ethernet-within-IP Encapsulation</li><li>ggp - Gateway-to-Gateway Protocol</li><li>gre - Generic Routing Encapsulation</li><li>hmp - Host Monitoring Protocol</li><li>icmp - IPv4 Internet Control Message Protocol</li><li>icmpv6 - IPv6 Internet Control Message Protocol</li><li>idpr-cmtp - Inter-Domain Policy Routing Control Message Transport Protocol</li><li>igmp - Internet Group Management Protocol</li><li>ipencap - IP in IP (encapsulation)</li><li>ipip - IP-within-IP Encapsulation Protocol</li><li>ipsec-ah - IPsec Authentication Header</li><li>ipsec-esp - IPsec Encapsulating Security Payload</li><li>ipv6 - Internet Protocol version 6</li><li>ipv6-frag - Fragment Header for IPv6</li><li>ipv6-nonxt - No Next Header for IPv6</li><li>ipv6-opts - Destination Options for IPv6</li><li>ipv6-route - Routing Header for IPv6</li><li>iso-tp4 - ISO Transport Protocol Class 4</li><li>l2tp - Layer Two Tunneling Protocol</li><li>ospf - Open Shortest Path First</li><li>pim - Protocol Independent Multicast</li><li>pup - PARC Universal Packet</li><li>rdp - Reliable Data Protocol</li><li>rspf - Radio Shortest Path First</li><li>rsvp - Reservation Protocol</li><li>sctp - Stream Control Transmission Protocol</li><li>st - Internet Stream Protocol</li><li>tcp - Transmission Control Protocol</li><li>udp - User Datagram Protocol</li><li>udp-lite - Lightweight User Datagram Protocol</li><li>vmtp - Versatile Message Transaction Protocol</li><li>vrrp - Virtual Router Redundancy Protocol</li><li>xns-idp - Xerox Network Systems Internet Datagram Protocol</li><li>xtp - Xpress Transport Protocol</li></ul> |
| **jump-target** (*name*; Default: ) | 如果指定了 `action=jump`，則指定用於處理封包的使用者定義防火牆鏈。 |
| **limit** (*integer/time,integer*; Default: ) | 匹配封包直到達到限制速率。使用此匹配器的規則將一直匹配，直到達到該限制。<ul><li>count - 最大平均封包速率，以每秒封包數（pps）為單位，除非後面跟有 Time 選項</li><li>time - 指定測量封包速率的時間間隔</li><li>burst - 突發中要匹配的封包數量</li></ul> |
| **log**(*yes \| no; Default:***no**) | 將包含以下資料的訊息新增到系統日誌：in-interface、out-interface、src-mac、dst-mac、eth-protocol、ip-protocol、src-ip:port->dst-ip:port 以及封包長度。 |
| **log-prefix** (*text*; Default: ) | 定義在日誌資訊之前列印的字首。 |
| **mac-protocol** (*802.2 \| arp \| capsman \| dot1x \| homeplug-av \| ip \| ipv6 \| ipx \| lacp \| length \| lldp \| loop-protect \| macsec \| mpls-multicast \| mpls-unicast \| mvrp \| packing-compr \| packing-simple \| pppoe \| pppoe-discovery \| rarp \| romon \| service-vlan \| vlan \| integer 0..65535 \| hex 0x0000-0xffff*; Default: ) | Ethernet 負載型別（MAC 層協定）。要匹配 VLAN 封裝幀（0x8100 或 0x88a8）的協定型別，應使用 vlan-encap 屬性。<ul><li>802.2 - 802.2 幀（0x0004）</li><li>arp - Address Resolution Protocol（0x0806）</li><li>homeplug-av - HomePlug AV MME（0x88E1）</li><li>ip - Internet Protocol version 4（0x0800）</li><li>ipv6 - Internet Protocol Version 6（0x86DD）</li><li>ipx - Internetwork Packet Exchange（0x8137）</li><li>length - 帶有長度欄位的封包（0x0000-0x05DC）</li><li>lldp - Link Layer Discovery Protocol（0x88CC）</li><li>loop-protect - Loop Protect Protocol（0x9003）</li><li>mpls-multicast - MPLS 組播（0x8848）</li><li>mpls-unicast - MPLS 單播（0x8847）</li><li>mvrp - Multiple VLAN Registration protocol（0x88F5）</li><li>packing-compr - 使用壓縮 [IP 打包](../system-information-and-utilities/ip-packing.md) 封裝的報文（0x9001）</li><li>packing-simple - 使用簡單 [IP 打包](../system-information-and-utilities/ip-packing.md) 封裝的報文（0x9000）</li><li>pppoe - PPPoE Session Stage（0x8864）</li><li>pppoe-discovery - PPPoE Discovery Stage（0x8863）</li><li>rarp - Reverse Address Resolution Protocol（0x8035）</li><li>service-vlan - Provider Bridging（IEEE 802.1ad）&amp; Shortest Path Bridging IEEE 802.1aq（0x88A8）</li><li>vlan - 帶 VLAN 標籤的幀（IEEE 802.1Q）以及具有 NNI 相容性的 Shortest Path Bridging IEEE 802.1aq（0x8100）</li></ul> |
| **new-packet-mark** (*string*; Default: ) | 設定新的封包標記值。 |
| **new-priority** (*integer \| from-ingress*; Default: ) | 設定封包的新優先順序。這可以是 VLAN、WMM 或 MPLS EXP 優先順序 [閱讀更多](./user-guides/wmm-and-vlan-priority.md)。此屬性也可用於設定內部優先順序 |
| **out-bridge** (*name*; Default: ) | 出站網橋介面。 |
| **out-bridge-list** (*name*; Default: ) | 在介面列表中定義的網橋介面集合。工作方式與 `out-bridge` 相同。 |
| **out-interface** (*name*; Default: ) | 封包離開網橋時所經過的介面。 |
| **out-interface-list** (*name*; Default: ) | 在[介面列表](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)中定義的介面集合。工作方式與 `out-interface` 相同。 |
| **packet-mark** (*name*; Default: ) | 匹配具有特定封包標記的封包。 |
| **packet-type** (*broadcast \| host \| multicast \| other-host*; Default: ) | MAC 幀型別：<ul><li>broadcast - 廣播 MAC 封包</li><li>host - 封包目的地為網橋本身</li><li>multicast - 組播 MAC 封包</li><li>other-host - 封包目的地為其他單播地址，而不是網橋本身</li></ul> |
| **src-address** (*IP address*; Default: ) | 源 IP 地址（僅當 MAC 協定設定為 IPv4 時）。 |
| **src-address6** (*IPv6 address*; Default: ) | 源 IPv6 地址（僅當 MAC 協定設定為 IPv6 時）。 |
| **src-mac-address** (*MAC address*; Default: ) | 源 MAC 地址。 |
| **src-port** (*integer 0..65535*; Default: ) | 源埠號或範圍（僅適用於 TCP 或 UDP 協定）。 |
| **stp-flags** (*topology-change \| topology-change-ack*; Default: ) | BPDU（Bridge Protocol Data Unit）標誌。網橋定期交換名為 BPDU 的配置訊息以防止環路<ul><li>topology-change - 當網橋檢測到埠狀態變化時設定拓撲變化標誌，以強制所有其他網橋丟棄其主機表並重新計算網路拓撲</li><li>topology-change-ack - 在對通知封包的應答中傳送拓撲變化確認標誌</li></ul> |
| **stp-forward-delay** (*integer 0..65535*; Default: ) | 轉發延遲計時器。 |
| **stp-hello-time** (*integer 0..65535*; Default: ) | STP hello 封包時間。 |
| **stp-max-age** (*integer 0..65535*; Default: ) | STP 訊息最大年齡。 |
| **stp-msg-age** (*integer 0..65535*; Default: ) | STP 訊息年齡。 |
| **stp-port** (*integer 0..65535*; Default: ) | STP 埠識別符號。 |
| **stp-root-address** (*MAC address*; Default: ) | 根網橋 MAC 地址。 |
| **stp-root-cost** (*integer 0..65535*; Default: ) | 根網橋開銷。 |
| **stp-root-priority** (*integer 0..65535*; Default: ) | 根網橋優先順序。 |
| **stp-sender-address** (*MAC address*; Default: ) | STP 訊息傳送方 MAC 地址。 |
| **stp-sender-priority** (*integer 0..65535*; Default: ) | STP 傳送方優先順序。 |
| **stp-type** (*config \| tcn*; Default: ) | BPDU 型別：<ul><li>config - 配置 BPDU</li><li>tcn - 拓撲變化通知</li></ul> |
| **tls-host** (*string*; Default: ) | 允許基於 TLS SNI 主機名匹配 https 流量。接受 [GLOB 語法](https://en.wikipedia.org/wiki/Glob_(programming)) 進行萬用字元匹配。請注意，如果 TLS 握手幀被分片為多個 TCP 段（封包），匹配器將無法匹配該主機名。 |
| **vlan-encap** (*802.2 \| arp \| ip \| ipv6 \| ipx \| length \| mpls-multicast \| mpls-unicast \| pppoe \| pppoe-discovery \| rarp \| vlan \| integer 0..65535 \| hex 0x0000-0xffff*; Default: ) | 匹配封裝在 VLAN 幀中的 MAC 協定型別。 |
| **vlan-id** (*integer 0..4095*; Default: ) | 匹配 VLAN 識別符號欄位。 |
| **vlan-priority** (*integer 0..7*; Default: ) | 匹配 VLAN 優先順序（優先順序程式碼點）。 |

腳註：

- STP 匹配器僅在目標 MAC 地址為 `01:80:C2:00:00:00/FF:FF:FF:FF:FF:FF`（Bridge Group 地址）時有效，並且應啟用 STP。

- 僅當 mac-protocol 為 `arp` 或 `rarp` 時，ARP 匹配器才有效。

- 僅當乙太網協定為 `0x8100` 或 `0x88a8` 時，VLAN 匹配器才有效。

- 僅當 mac-protocol 設定為 `ip` 或 `ipv6` 時，IP 或 IPv6 相關匹配器才有效。

- 僅當實際幀符合 IEEE 802.2 和 IEEE 802.3 標準時，才會檢查 802.3 匹配器。對於其他封包，這些匹配器會被忽略。

### 網橋封包過濾器 {#bridge-packet-filter}

本節介紹特定的網橋過濾器選項。

**子選單：** `/interface/bridge/filter`

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*accept \| drop \| jump \| log \| mark-packet \| passthrough \| return \| set-priority*；預設值：**accept**) | 如果封包與規則匹配，則要執行的操作：<ul><li>accept - 接受封包。不執行任何操作，即封包會直接透過而不執行任何操作，並且相關列表/鏈中不會處理更多規則</li><li>drop - 靜默丟棄封包（不傳送 ICMP 拒絕訊息）</li><li>jump - 跳轉到由 jump-target 引數值指定的鏈</li><li>log - 向系統日誌新增一條訊息，其中包含以下資料：in-interface、out-interface、src-mac、dst-mac、eth-proto、protocol、src-ip:port-&gt;dst-ip:port 以及封包長度。封包匹配後，會被傳遞給列表中的下一條規則，類似於 passthrough</li><li>mark - 標記封包，以便稍後使用該標記</li><li>passthrough - 忽略此規則並繼續處理下一條規則。其作用與已停用規則相同，區別在於能夠統計封包</li><li>return - 返回到發生跳轉的上一個鏈</li><li>set-priority - 對透過能夠傳輸優先順序的鏈路（VLAN 或支援 WMM 的無線介面）發出的封包，設定由 new-priority 引數指定的優先順序。[閱讀更多](./user-guides/wmm-and-vlan-priority.md)</li></ul> |

### 橋接 NAT {#bridge-nat}

本節介紹特定的橋接 NAT 選項。

**子選單：** `/interface/bridge/nat`

| 屬性 | 描述 |
| :-- | :-- |
| **action** (*accept \| drop \| jump \| mark-packet \| redirect \| set-priority \| arp-reply \| dst-nat \| log \| passthrough \| return \| src-nat*；預設值：**accept**) | 當封包與該規則匹配時要執行的操作：<ul><li>accept - 接受封包。不執行任何操作，即封包被直接放行而不執行任何動作，並且不再處理相關列表/鏈中的更多規則</li><li>arp-reply - 使用指定的 MAC 地址傳送對 ARP 請求的應答（此規則將忽略任何其他封包）（僅在 dstnat 鏈中有效）</li><li>drop - 靜默丟棄封包（不傳送 ICMP reject 訊息）</li><li>dst-nat - 更改封包的目標 MAC 地址（僅在 dstnat 鏈中有效）</li><li>jump - 跳轉到由 jump-target 引數值指定的鏈</li><li>log - 記錄封包日誌</li><li>mark - 標記封包，以便稍後使用該標記</li><li>passthrough - 忽略此規則並繼續處理下一條規則。其行為與停用規則相同，區別在於能夠統計封包</li><li>redirect - 將封包重定向到網橋本身（僅在 dstnat 鏈中有效）</li><li>return - 返回到執行跳轉的上一級鏈</li><li>set-priority - 對透過支援傳輸優先順序的鏈路（VLAN 或啟用 WMM 的無線介面）傳送的封包，設定由 new-priority 引數指定的優先順序。[閱讀更多](./user-guides/wmm-and-vlan-priority.md)</li><li>src-nat - 更改封包的源 MAC 地址（僅在 srcnat 鏈中有效）</li></ul> |
| **to-arp-reply-mac-address** (*MAC 地址*；預設值：) | 當選擇 `action=arp-reply` 時，放入乙太網幀和 ARP 負載中的源 MAC 地址 |
| **to-dst-mac-address** (*MAC 地址*；預設值：) | 當選擇 `action=dst-nat` 時，放入乙太網幀中的目標 MAC 地址 |
| **to-src-mac-address** (*MAC 地址*；預設值：) | 當選擇 `action=src-nat` 時，放入乙太網幀中的源 MAC 地址 |

## 另請參閱 {#see-also}

---

- [CRS1xx/2xx 系列交換器](./crs1xx-and-2xx-series-switches.md)
- [Marvell Prestera 交換器晶片功能](./marvell-prestera-switch-chip-features.md)
- [交換器晶片功能](./switch-chip-features.md)
- [RouterBOARD 上的 MTU](../hardware/mtu-in-routeros.md)
- [二層錯誤配置](./user-guides/layer2-misconfiguration.md)
- [橋接 VLAN 表](./user-guides/bridge-vlan-table.md)
