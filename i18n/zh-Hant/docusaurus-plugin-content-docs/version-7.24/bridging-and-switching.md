---
title: "Bridging and Switching"
tags:
  - 'bridging'
  - 'stp'
  - 'arp'
source: https://manual.mikrotik.com/docs/7.24/bridging-and-switching
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

---

![Bridge diagram](/img/341670d0f71b9c56.webp)

Ethernet-like 網路（Ethernet、Ethernet over IP、處於 ap-bridge 或 bridge 模式的 IEEE 802.11、WDS、VLAN）可以使用 MAC bridge 連接在一起。bridge 功能可讓連接到不同 LAN 的主機互相連線（使用 EoIP 時，只要地理上分散的網路之間存在任何形式的 IP 網路互連，也可以進行橋接），如同它們都連接到單一 LAN 一樣。由於 bridge 是透明的，因此不會出現在 traceroute 清單中，而且如果這些 LAN 已橋接，沒有任何工具可以區分在某個 LAN 中運作的主機與在另一個 LAN 中運作的主機。不過，視 LAN 的互連方式而定，主機之間的延遲與資料速率可能會有所不同。

網路迴圈可能（不論是否刻意）在複雜拓撲中出現。若未進行任何特殊處理，迴圈會導致封包呈雪崩式增生，使網路無法正常運作。每個 bridge 都會執行一種演算法，計算如何避免迴圈。(R/M)STP 讓 bridge 之間可以互相通訊，以協商出無迴圈的拓撲。所有其他原本會形成迴圈的替代連線都會進入待命狀態，因此當主要連線失敗時，另一條連線可以接替。此演算法會定期交換設定訊息（BPDUs - Bridge Protocol Data Unit），讓所有 bridge 都能取得網路拓撲變更的最新資訊。(R/M)STP 會選出 root bridge，負責網路重新設定，例如在其他 bridge 上阻斷與開啟埠。root bridge 是 bridge ID 最小的 bridge。

## Bridge 介面設定 {#bridge-interface-setup}

---

若要將多個網路合併為一個 bridge，應建立 bridge 介面。之後，應將所有所需介面設定為其埠。預設會依據 bridge 埠設定自動選擇 bridge MAC 位址。為避免非預期的 MAC 位址變更，建議停用 `auto-mac`，並使用 `admin-mac` 手動指定 MAC 位址。

**子選單：** `/interface/bridge`

| 屬性 | 說明 |
| :-- | :-- |
| **add-dhcp-option82** (*yes* \| *no*; Default: **no**) | <strong>重要：</strong>從 <strong>RouterOS 7.23 版</strong>開始，此設定已移除。現在可使用預先定義的變數（例如 BRIDGEMAC、HOSTNAME、INTERFACE、VID）設定自訂 Remote ID 與 Circuit ID 值。詳情請參閱下方的 <code>dhcp-agent-circuit-id</code> 與 <code>dhcp-agent-remote-id</code> 屬性。如果此設定在較早版本（7.22 或更早）中已啟用，升級時會自動將設定更新為新格式。 <br/> 是否將 DHCP Option 82 資訊（Agent Remote ID 與 Agent Circuit ID）加入 DHCP 封包。可與支援 Option 82 的 DHCP 伺服器搭配使用，以指派 IP 位址並實作原則。此屬性只有在 <code>dhcp-snooping</code> 設為 <span className="ros-icon-success"><code>yes</code></span> 時才會生效。 <br/> 在 RouterOS 7.22 或更早版本中，這些值是預先定義且無法修改： <br/><ul><li>對於 Agent Remote ID，RouterOS 會使用 bridge 介面的 MAC 位址，格式為「xx:xx:xx:xx:xx:xx」（小寫，以冒號分隔）。</li><li>對於 Agent Circuit ID，RouterOS 會使用 DHCP 用戶端所連接介面的名稱與 VLAN ID，並以冒號分隔（interface:vlan-id）。只有在 bridge 上啟用 <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> 時，才會包含 VLAN ID。</li></ul> 例如（<code>vlan-filtering=yes</code>）： <br/> Agent Remote ID - cc:2d:e0:01:6a:43 Agent Circuit ID - ether2:10 <br/> |
| **admin-mac** (*MAC address*; Default: **none**) | bridge 的靜態 MAC 位址。此屬性只有在 `auto-mac` 設為 `no` 時才會生效。 |
| **ageing-time** (*time*; Default: **00:05:00**) | 主機資訊會在 bridge 資料庫中保留多久。 |
| **arp** (*disabled* \| *enabled* \| *local-proxy-arp \| proxy-arp \| reply-only*; Default: **enabled**) | Address Resolution Protocol 設定<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 介面不會使用 ARP</li><li><span className="ros-icon-success"><code>enabled</code></span> - 介面會使用 ARP</li><li><span className="ros-icon-success"><code>local-proxy-arp</code></span> - 路由器會在介面上執行 proxy ARP，並將回覆傳送至同一介面</li><li><span className="ros-icon-success"><code>proxy-arp</code></span> - 路由器會在介面上執行 proxy ARP，並將回覆傳送至其他介面</li><li><span className="ros-icon-success"><code>reply-only</code></span> - 介面只會回應來自符合 IP 位址／MAC 位址組合的要求，而這些組合必須已作為靜態項目輸入 IP/ARP 表。IP/ARP 表中不會自動儲存動態項目。因此，若要成功通訊，必須已存在有效的靜態項目。</li></ul> |
| **arp-timeout** (*auto \| integer*; Default: **auto**) | 在沒有從某個 IP 位址收到封包後，ARP 記錄會在 ARP 表中保留多久。值 `auto` 等於 `/ip/settings` 中的 `arp-timeout` 值，預設為 30s。 |
| **auto-mac** (*yes \| no*; Default: **yes**) | 當設定 <code>auto-mac=yes</code> 時，bridge 會依下列優先順序自動為 bridge 介面選擇 MAC 位址： <br/><ol><li>從屬於 bridge 一部分的 Ethernet 介面取得；</li><li>從 bridge 中的非 Ethernet 介面取得（例如 WiFi 或 tunnel）；</li><li>若上述皆不可用，則使用隨機產生的位址。</li></ol> 如果設定變更，例如新增埠到 bridge，只有當出現較高優先順序的位址來源時，bridge 的 MAC 位址才會更新。例如，如果 bridge 最初使用隨機產生的 MAC，之後新增 Ethernet 介面，MAC 會依最高可用優先順序更新（在此例中為 Ethernet 介面）。如果目前 MAC 所關聯的埠被移到不同的 bridge，bridge 也會更新 MAC 位址。 <br/> 目前的 MAC 位址及其優先順序層級會被儲存，並在重新開機後繼續使用。 <br/> 當設定 <code>auto-mac=no</code> 時，可以使用 <code>admin-mac</code> 屬性手動設定靜態 MAC 位址。 |
| **comment** (*string*; Default: ) | 介面的簡短說明。 |
| **dhcp-agent-circuit-id** (*string*; Default: **!dhcp-agent-circuit-id**) | 指定通過 bridge 的 DHCP 訊息中，Option 82 的 <strong>Circuit ID</strong> 子選項值。字串長度限制為 255 個字元。 <br/> 此設定取代现已淘汰的 <code>add-dhcp-option82</code> 屬性。如果 <code>add-dhcp-option82</code> 在較早版本（7.22 或更早）中已啟用，升級時會自動將設定更新為新格式：$(INTERFACE):$(VID)。透過 GUI 設定此項目時，也會顯示此格式。 <br/> 支援下列變數： <br/><ul><li>$(BRIDGEMAC) - 目前的 bridge MAC 位址，格式為「xx:xx:xx:xx:xx:xx」（小寫，以冒號分隔）；</li><li>$(HOSTNAME) - 系統識別名稱；</li><li>$(INTERFACE) - DHCP 用戶端所連接的介面名稱；</li><li>$(VID) - DHCP 用戶端使用的 VLAN ID。如果 DHCP 用戶端未標記，VID 會對應至埠的 <span className="ros-background-accent-green-bolder"><code>pvid</code></span>。僅在 bridge 上啟用 <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> 時適用。</li></ul> 變數語法規則 <br/><ul><li>變數必須以括號包住，並在前面加上錢字號（$）。</li><li>從終端機設定時，錢字號必須以反斜線（\）逸出，否則會被解讀為 RouterOS 指令碼變數。</li></ul> 範例： <br/><code>/interface/bridge</code><br/><code>add add-dhcp-option82=yes dhcp-agent-circuit-id="interface: \$(INTERFACE), vlan: \$(VID)" dhcp-snooping=yes name=bridge1 vlan-filtering=yes</code> 此屬性只有在 <code>dhcp-snooping</code> 設為 yes 時才會生效。 <br/> |
| **dhcpv6-agent-circuit-id** (*string*; Default: **!dhcpv6-agent-circuit-id**) | 指定通過 bridge 的 DHCPv6 訊息中，Option 18 的 <strong>Interface ID</strong> 子選項值。<code>dhcpv6-agent-circuit-id</code> 屬性遵循與 <code>dhcp-agent-circuit-id</code> 相同的規則。 <br/> |
| **dhcp-agent-remote-id** (*string*; Default: **!dhcp-agent-remote-id**) | 指定通過 bridge 的 DHCP 訊息中，Option 82 的 <strong>Remote ID</strong> 子選項值。字串長度限制為 255 個字元。 <br/> 此設定取代现已淘汰的 <code>add-dhcp-option82</code> 屬性。如果 <code>add-dhcp-option82</code> 在較早版本（7.22 或更早）中已啟用，升級時會自動將設定更新為新格式：$(BRIDGEMAC)。透過 GUI 設定此項目時，也會顯示此格式。 <br/> 支援下列變數： <br/><ul><li>$(BRIDGEMAC) - 目前的 bridge MAC 位址，格式為「xx:xx:xx:xx:xx:xx」（小寫，以冒號分隔）；</li><li>$(HOSTNAME) - 系統識別名稱；</li><li>$(INTERFACE) - DHCP 用戶端所連接的介面名稱；</li><li>$(VID) - DHCP 用戶端使用的 VLAN ID。如果 DHCP 用戶端未標記，VID 會對應至埠的 <span className="ros-background-accent-green-bolder"><code>pvid</code></span>。僅在 bridge 上啟用 <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> 時適用。</li></ul> 變數語法規則 <br/><ul><li>變數必須以括號包住，並在前面加上錢字號（$）。</li><li>從終端機設定時，錢字號必須以反斜線（\）逸出，否則會被解讀為 RouterOS 指令碼變數。</li></ul> 範例： <br/><code>/interface/bridge</code><br/><code>add add-dhcp-option82=yes dhcp-agent-remote-id="ip: 192.168.88.1, identity: \$(HOSTNAME), mac: \$(BRIDGEMAC)" dhcp-snooping=yes name=bridge1 vlan-filtering=yes</code> 此屬性只有在 <code>dhcp-snooping</code> 設為 yes 時才會生效。 <br/> |
| **dhcpv6-agent-remote-id** (*string*; Default: **!dhcpv6-agent-remote-id**) | 指定通過 bridge 的 DHCPv6 訊息中，Option 37 的 <strong>Remote ID</strong> 子選項值。<code>dhcpv6-agent-remote-id</code> 屬性遵循與 <code>dhcp-agent-remote-id</code> 相同的規則。 <br/> |
| **dhcp-snooping** (*yes \| no*; Default: **no**) | 啟用或停用 bridge 上的 DHCP Snooping。 <br/><br/><strong>注意：</strong>啟用 DHCP snooping 功能會關閉 bridge <a href="/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fast-path">fast-path</a>，進而影響對通過該 bridge 的連線進行 <a href="/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fasttrack">fasttrack</a> 的能力。 <br/> |
| **dhcpv6-snooping**(*yes \| no*; Default: **no**) | 啟用或停用 bridge 上的 DHCPv6 Snooping。 <br/><br/><strong>注意：</strong>啟用 DHCP snooping 功能會關閉 bridge <a href="/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fast-path">fast-path</a>，進而影響對通過該 bridge 的連線進行 <a href="/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fasttrack">fasttrack</a> 的能力。 <br/> |
| **disabled** (*yes \| no*; Default: **no**) | 變更 bridge 是否停用。 |
| **ether-type** (*0x9100 \| 0x8100 \| 0x88a8*; Default: **0x8100**) | 變更 EtherType，用於判斷封包是否具有 VLAN tag。具有相符 EtherType 的封包會被視為已標記封包。此屬性只有在 `vlan-filtering` 設為 `yes` 時才會生效。 |
| **fast-forward** (*yes \| no*; Default: **yes**) | Fast Path 的一種特殊且更快速的案例，僅適用於具有 2 個介面的 bridge（新 bridge 預設啟用）。更多詳情請參閱 Fast Forward 一節。 |
| **forward-delay** (*time*; Default: **00:00:15**) | 在 bridge 開始正常運作前，bridge 介面初始化階段（也就是路由器啟動或啟用介面後）花費在 listening／learning 狀態的時間。 |
| **forward-reserved-addresses** (*yes \| no*: Default: **no**) | 是否轉送位於 <strong>01:80:C2:00:00:0x</strong> 範圍內的 IEEE 保留群播 MAC 位址。符合 R/M/STP 標準的 bridge 應避免轉送這些封包；此屬性只能在 <code>protocol-mode</code> 設為 <code>none</code> 時套用。 <br/> 啟用保留 MAC 位址轉送可能會影響依賴這些位址的特定協定。建議只有在絕對必要時才啟用轉送，例如透明橋接環境（例如延伸長距離鏈路、將 bridge 作為媒體轉換器，或進行網路分析）。 <br/> 以下是 RouterOS 使用的一些重要 MAC 位址與協定： <br/><ul><li>01:80:C2:00:00:00 - <a href="/docs/bridging-and-switching#spanning-tree-protocol" rel="nofollow">Spanning Tree Protocol (STP)</a>；</li><li>01:80:C2:00:00:01 - <a href="/docs/wired-connections/ethernet" rel="nofollow">Ethernet</a> Flow Control；</li><li>01:80:C2:00:00:02 - <a href="/docs/high-availability-solutions/bonding#8023ad" rel="nofollow">Link Aggregation Control Protocol (LACP)</a>；</li><li>01:80:C2:00:00:03 - <a href="/docs/authentication-authorization-accounting/dot1x" rel="nofollow">Dot1x</a> 用戶端與伺服器；</li><li>01:80:C2:00:00:08 - Spanning Tree Protocol（適用於 802.1ad bridge，使用 <span className="ros-background-accent-green-bolder"><code>ether-type=0x88a8</code></span>）；</li><li>01:80:C2:00:00:0D - <a href="/docs/bridging-and-switching#mvrp" rel="nofollow">Multiple VLAN Registration protocol</a>（適用於 802.1ad bridge，使用 <span className="ros-background-accent-green-bolder"><code>ether-type=0x88a8</code></span>）；</li><li>01:80:C2:00:00:0E - <a href="/docs/system-information-and-utilities/neighbor-discovery" rel="nofollow">Link Layer Discovery Protocol</a>、<a href="/docs/high-availability-solutions/multi-chassis-link-aggregation-group" rel="nofollow">Multi-chassis Link Aggregation Group</a> 與 <a href="/docs/system-information-and-utilities/precision-time-protocol">Precision Time Protocol</a>；</li></ul><br/><strong>重要：</strong>Flow Control MAC 位址 01:80:C2:00:00:01 是例外；bridge 不會轉送它。 <br/> |
| **frame-types** (*admit-all \| admit-only-untagged-and-priority-tagged \| admit-only-vlan-tagged*; Default: **admit-all**) | 指定 bridge 埠上允許的訊框類型。此屬性只有在 `vlan-filtering` 設為 `yes` 時才會生效。 |
| **igmp-snooping** (*yes \| no*; Default: **no**) | 啟用群播群組與埠學習，以避免群播流量泛洪到 bridge 中的所有介面。 |
| **igmp-version** (*2 \| 3*; Default: **2**) | 當 bridge 介面作為 IGMP querier 時，選擇產生 IGMP membership queries 的 IGMP 版本。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **ingress-filtering** (*yes \| no*; Default: **yes**) | 啟用或停用 VLAN ingress filtering，其會檢查 ingress 埠是否為 bridge VLAN 表中所收到 VLAN ID 的成員。依預設，bridge VLAN 表中不存在的 VLAN 會在傳出（egress）前被丟棄，但此屬性可讓你在收到封包時（ingress）就丟棄封包。應搭配 `frame-types` 使用，以指定 ingress 流量應為已標記或未標記。此屬性只有在 `vlan-filtering` 設為 `yes` 時才會生效。自 RouterOS v7 起，此設定預設啟用。 |
| **l2mtu** (*read-only*; Default: ) | L2MTU 表示此介面可傳送、不含 MAC 標頭的訊框大小上限。L2MTU 值會由 bridge 自動設定，並使用任何相關 bridge 埠中最低的 L2MTU 值。此值無法手動變更。 |
| **last-member-interval** (*time*; Default: **1s**) | 當 bridge 埠上的最後一位用戶端取消訂閱群播群組，且 bridge 作為主動 querier 時，bridge 會傳送群組特定的 IGMP/MLD query，以確認是否沒有其他用戶端仍在訂閱。此設定會變更這些 query 的回應時間。如果在特定時間期間（<code>last-member-interval</code> * <code>last-member-query-count</code>）內未收到 membership reports，該群播群組會從群播資料庫（MDB）中移除。 <br/> 如果 bridge 埠設定了 fast-leave，群播群組會立即移除，而不會傳送任何 query。 <br/> 此屬性只有在 <code>igmp-snooping</code> 與 <code>multicast-querier</code> 設為 <span className="ros-icon-success"><code>yes</code></span> 時才會生效。 |
| **last-member-query-count** (*integer: 0..4294967295*; Default: **2**) | 在 IGMP/MLD snooping bridge 停止轉送特定群播串流之前，`last-member-interval` 應經過多少次。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **max-hops** (*integer: 6..40*; Default: **20**) | 在啟用 MSTP 的網路中，同一區域內 BPDU 可通過的 bridge 數量，超過後 BPDU 會被忽略。此屬性只有在 `protocol-mode` 設為 `mstp` 時才會生效。 |
| **max-learned-entries** (*integer: 0..4294967295 \| auto \| unlimited*; Default: **auto**) | 設定 bridge 介面可學習的主機數量上限。預設值為 <span className="ros-icon-success"><code>auto</code></span>，取決於安裝的 RAM 容量。可以設定高於預設值的值，或選擇 <code>unlimited</code> 選項，但這會增加記憶體不足的風險。 <br/> 特定 RAM 大小的預設值： <br/><ul><li>64 MB 為 8192；</li><li>128 MB 為 16384；</li><li>256 MB 為 32768；</li><li>512 MB 為 65536；</li><li>1024 MB 或更高為 131072。</li></ul> 此限制專門套用於 bridge 介面，而非交換器 FDB 表的硬體限制。即使達到 bridge 限制，交換器仍可繼續學習主機直到其硬體上限，並做出正確的轉送決策。不過，這些額外主機不會顯示在 <code>/interface/bridge/host</code> 表中，也無法監控。此外，達到這個限制可能會影響 MLAG 主機同步。 <br/> 此設定自 RouterOS 7.16 版起提供。 |
| **max-message-age** (*time: 6s..40s*; Default: **00:00:20**) | 變更由 root bridge 傳送的 BPDU 封包中的 Max Age 值。root bridge 會傳送 Max Age 設為 `max-message-age` 值且 Message Age 為 0 的 BPDU。每個後續 bridge 都會在傳送其 BPDU 前遞增 Message Age。當 bridge 收到 Message Age 等於或大於 Max Age 的 BPDU 時，該 BPDU 會被忽略。此屬性只有在 `protocol-mode` 設為 `stp` 或 `rstp` 時才會生效。 |
| **membership-interval** (*time*; Default: **4m20s**) | 如果在 bridge 埠上未收到 IGMP/MLD membership reports，Multicast Database（MDB）中的項目會在多久後移除。此屬性只有在 `igmp-snooping` 設為 `yes` 時才會生效。 |
| **mld-version** (*1 \| 2*; Default: **1**) | 當 bridge 介面作為 MLD querier 時，選擇產生 MLD membership queries 的 MLD 版本。此屬性只有在 bridge 具有有效的 IPv6 位址，且 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **mtu** (*integer*; Default: **auto**) | 最大傳輸單位。依預設，bridge 會自動設定 MTU，並使用任何相關 bridge 埠中最低的 MTU 值。未新增任何 bridge 埠時，預設 bridge MTU 值為 1500。MTU 值可以手動設定，但不得超過 bridge L2MTU 或最低 bridge 埠 L2MTU。如果新增的 bridge 埠其 L2MTU 小於 bridge 的 <code>actual-mtu</code>（由 <code>mtu</code> 屬性設定），則手動設定的值會被忽略，bridge 會如同設定 <code>mtu=auto</code> 般運作。 <br/> 在 bridge 上新增 VLAN 介面，且 VLAN 使用高於預設 1500 的 MTU 時，建議手動設定 bridge 的 MTU。 |
| **multicast-querier** (*yes \| no*; Default: **no**) | Multicast querier 會產生定期的 IGMP/MLD general membership queries，所有支援 IGMP/MLD 的設備都會以 IGMP/MLD membership report 回應。通常，PIM（群播）路由器或 IGMP proxy 會產生這些 query。 <br/> 使用此屬性可讓啟用 IGMP/MLD snooping 的 bridge 產生 IGMP/MLD general membership queries。每當 Layer2 網路中沒有主動 querier（PIM 路由器或 IGMP proxy）時，就應使用此屬性。若 Layer2 網路中沒有 multicast querier，Multicast Database（MDB）就不會更新；學習到的項目會逾時，IGMP/MLD snooping 也無法正常運作。 <br/> 只會產生未標記的 IGMP/MLD general membership queries。IGMP query 會以 bridge 介面自身的 IPv4 位址作為來源位址傳送（請參閱 <code>querier-uses-bridge-address</code>），MLD query 則會以 bridge 介面的 IPv6 link-local 位址傳送。如果偵測到外部 IGMP/MLD querier，bridge 不會傳送 query（請參閱監控值 <code>igmp-querier</code> 與 <code>mld-querier</code>）。 <br/> 此屬性只有在 <code>igmp-snooping</code> 設為 <span className="ros-icon-success"><code>yes</code></span> 時才會生效。 |
| **multicast-router** (*disabled \| permanent \| temporary-query*; Default: **temporary-query**) | multicast router 埠是連接群播路由器或 querier 的埠。在此埠上，未註冊的群播串流與 IGMP/MLD membership reports 會被傳送。此設定會變更 bridge 介面本身的 multicast router 狀態。此屬性可用於將 IGMP/MLD membership reports 傳送至 bridge 介面，以進行後續的群播路由或 proxy。此屬性只有在 <code>igmp-snooping</code> 設為 <span className="ros-icon-success"><code>yes</code></span> 時才會生效。<ul><li><span className="ros-icon-success"><code>disabled</code></span> - 停用 bridge 介面上的 multicast router 狀態。不論 bridge 介面上設定為何，未註冊的群播與 IGMP/MLD membership reports 都不會傳送至 bridge 介面。</li><li><span className="ros-icon-success"><code>permanent</code></span> - 啟用 bridge 介面上的 multicast router 狀態。不論 bridge 介面上設定為何，未註冊的群播與 IGMP/MLD membership reports 都會傳送至 bridge 介面本身。</li><li><span className="ros-icon-success"><code>temporary-query</code></span> - 使用 IGMP/MLD query 自動偵測 bridge 介面上的 multicast router 狀態。</li></ul> |
| **name** (*text*; Default: **bridgeN**) | bridge 介面的名稱。 |
| **port-cost-mode** (*long \| short*; Default: **long**) | 變更橋接埠的 port path-cost 與 internal-path-cost 模式，使用依介面速度為基礎的自動值。此設定不會影響已手動設定 <code>path-cost</code> 或 <code>internal-path-cost</code> 屬性的橋接埠。以下範例說明特定資料速率所對應的 path-cost（中間速率按比例計算）： <br/><details><summary>Path-cost 表</summary><table><thead><tr><th>資料速率</th><th>Long</th><th>Short</th></tr></thead><tbody><tr><td>10 Mbps</td><td>2,000,000</td><td>100</td></tr><tr><td>100 Mbps</td><td>200,000</td><td>19</td></tr><tr><td>1 Gbps</td><td>20,000</td><td>4</td></tr><tr><td>10 Gbps</td><td>2,000</td><td>2</td></tr><tr><td>25 Gbps</td><td>800</td><td>1</td></tr><tr><td>40 Gbps</td><td>500</td><td>1</td></tr><tr><td>50 Gbps</td><td>400</td><td>1</td></tr><tr><td>100 Gbps</td><td>200</td><td>1</td></tr></tbody></table></details> 對於 HW offloaded bond 介面，會套用所有 bond 成員埠中最高的 path-cost；此值不受 bonding 總鏈路速度影響。 <br/> 對於虛擬介面（例如 VLAN、EoIP、VXLAN 與非 HW offloaded bond），以及 wifi、wireless 與 60GHz 介面，long 模式會指派 path-cost 20,000，short 模式則指派 10。 <br/> 對於動態橋接介面（例如 wifi、wireless、PPP、VPLS），long 模式的 path-cost 預設為 20,000，short 模式則為 10。不過，將介面動態新增至 bridge 的服務可以手動覆寫此值，例如使用 CAPsMAN <code>datapath.bridge-cost</code> 設定。 <br/> 使用 <a href="/docs/bridging-and-switching#bridge-port-monitoring">port monitor</a> 觀察套用的 path-cost。 <br/> 當 <code>protocol-mode</code> 設為 <code>stp</code>、<code>rstp</code> 或 <code>mstp</code> 時，此屬性會生效。 |
| **priority** (*integer: 0..65535 decimal format or 0x0000-0xffff hex format*; Default: **32768 / 0x8000**) | bridge priority，R/STP 會用它來判斷 root bridge，MSTP 會用它來判斷 CIST 與 IST 區域 root bridge。當 <code>protocol-mode</code> 設為 <code>none</code> 時，此屬性沒有作用。 <br/><strong>有效值：</strong>bridge priority 必須以 4096（0x1000）為步進設定。最低 12 位元會被忽略。有效值為：0x0000、0x1000、0x2000、0x3000、0x4000、0x5000、0x6000、0x7000、0x8000、0x9000、0xa000、0xb000、0xc000、0xd000、0xe000、0xf000（或其十進位對應值：0、4096、8192、12288、16384、20480、24576、28672、32768、36864、40960、45056、49152、53248、57344、61440）。 |
| **protocol-mode** (*none \| rstp \| stp \| mstp*; Default: **rstp**) | 選擇 Spanning tree protocol（STP）或 Rapid spanning tree protocol（RSTP），以確保任何橋接 LAN 都具有無迴圈拓撲。RSTP 在拓撲變更後可提供更快速的 spanning tree 收斂。選擇 MSTP 可確保跨多個 VLAN 的無迴圈拓撲。 <br/> 轉送位於 <strong>01:80:C2:00:00:0x</strong> 範圍內的保留 MAC 位址，已與 <code>protocol-mode=none</code> 分開，並自 RouterOS v7.16 起成為可控制的屬性 <code>forward-reserved-addresses</code>。 |
| **pvid** (*integer: 1..4094*; Default: **1**) | Port VLAN ID（pvid）指定未標記 ingress 流量要指派到哪個 VLAN。例如，這適用於從 bridge IP 傳送且目的地為 bridge 埠的訊框。此屬性只有在 `vlan-filtering` 設為 `yes` 時才會生效。 |
| **querier-interval** (*time*; Default: **4m15s**) | 變更已偵測到的 querier 與 multicast-router 埠的逾時期間。此屬性只有在 `igmp-snooping` 設為 `yes` 時才會生效。 |
| **querier-uses-bridge-address** (*yes \| no*; Default: **yes**) | 啟用時，bridge IGMP querier 會使用 bridge 介面自身的 IPv4 位址作為 IGMP query 封包的來源位址，而不是預設的 0.0.0.0。某些群播用戶端會將來自 0.0.0.0 的 query 視為無效而不回應，這可能導致 snooping 表項目逾時時群播串流中斷。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes`，且 bridge 介面已指派 IPv4 位址時才會生效。此設定僅適用於 IPv4（IGMP）。MLD query 一律使用 bridge 介面的 IPv6 link-local 位址。 |
| **query-interval** (*time*; Default: **2m5s**) | 當 bridge 介面作為 IGMP/MLD querier 時，變更傳送 IGMP/MLD general membership queries 的間隔。此間隔會在最後一次 startup query 傳送後開始。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **query-response-interval** (*time*; Default: **10s**) | 當 bridge 作為主動 IGMP/MLD querier 時，此設定會變更 general IGMP/MLD queries 的回應時間。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **region-name** (*text*; Default: ) | MSTP 區域名稱。此屬性只有在 `protocol-mode` 設為 `mstp` 時才會生效。 |
| **region-revision** (*integer: 0..65535*; Default: **0**) | MSTP 設定修訂編號。此屬性只有在 `protocol-mode` 設為 `mstp` 時才會生效。 |
| **ra-guard** (*yes \| no*; Default: **no**) | RA guard 是一項安全功能，會依據已授權、受信任埠的清單驗證傳入的 Router Advertisements。 |
| **startup-query-count** (*integer: 0..4294967295*; Default: **2**) | 指定當 bridge 介面啟用或主動 querier 逾時時，必須傳送多少次 general IGMP/MLD queries。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **startup-query-interval** (*time*; Default: **31s250ms**) | 指定 startup general IGMP/MLD queries 之間的間隔。此屬性只有在 `igmp-snooping` 與 `multicast-querier` 設為 `yes` 時才會生效。 |
| **transmit-hold-count** (*integer: 1..10*; Default: **6**) | Port Transmit 狀態機用來限制傳輸速率的 Transmit Hold Count。 |
| **vlan-filtering** (*yes \| no*; Default: **no**) | 全域啟用或停用 bridge 的 VLAN 功能。 |

:::danger
變更某些屬性可能導致 bridge 暫時停用所有埠。在正式環境中變更這類屬性時必須考量這一點，因為這可能導致所有封包暫時被丟棄。這類屬性包括 `vlan-filtering`、`protocol-mode`、`igmp-snooping`、`fast-forward` 等。
:::

### 範例 {#example}

下列範例示範如何建立並驗證基本 bridge 介面，以進行簡單的 Layer 2 交換。此設定會建立一個 bridge，將多個 Ethernet 埠合併為單一交換網路區段。

```ros
[admin@MikroTik] > /interface/bridge/add
[admin@MikroTik] > interface bridge print 
Flags: X - disabled, R - running 
0 R name="bridge1" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=5E:D2:42:95:56:7F protocol-mode=rstp fast-forward=yes 
igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6 vlan-filtering=no 
dhcp-snooping=no 
```

### 橋接監控 {#bridge-monitoring}

若要監控 bridge 介面的目前狀態，請使用 `monitor` 指令。

**子選單：** `/interface/bridge/monitor`

| Property | Description |
| :-- | :-- |
| **bridge-id** (*priority.MAC address*) | 本機 bridge 識別碼，格式為 bridge-priority.bridge-MAC-address。 |
| **current-mac-address** (*MAC address*) | bridge 目前的 MAC 位址。 |
| **designated-port-count** (*integer*) | 指定 bridge 埠的數量。 |
| **declared-vlan-ids** (*integer 1..4094*) | 透過 [MVRP protocol](/docs/bridging-and-switching#mvrp) 在 bridge 介面上宣告的 VLAN。 |
| **fast-forward** (*yes \| no*) | bridge fast-forward 是否啟用。 |
| **igmp-querier** (*none* \| *interface & IPv4 address*) | 顯示所偵測到 IGMP querier 的 bridge 埠與來源 IP 位址。只會顯示偵測到的外部 IGMP querier，不會顯示本機 bridge IGMP querier（包括 IGMP proxy 與 PIM）。只有在啟用 `igmp-snooping` 時才會出現監控值。 |
| **mld-querier** (*none* \| *interface & IPv6 address*) | 顯示所偵測到 MLD querier 的 bridge 埠與來源 IPv6 位址。只會顯示偵測到的外部 MLD querier，不會顯示本機 bridge MLD querier。只有在啟用 `igmp-snooping` 且 bridge 具有有效的 IPv6 位址時才會出現監控值。 |
| **mst-config-digest** (*integer*) | VLAN 對應至 MST Instance ID 的計算雜湊值。 |
| **multicast-router** (*yes \| no*) | 顯示是否在埠上偵測到 multicast 路由器。只有在啟用 `igmp-snooping` 時才會出現監控值。 |
| **port-count** (*integer*) | bridge 埠的數量。 |
| **regional-root-bridge-id** (*priority.MAC address*) | 區域 root bridge ID，格式為 bridge-priority.bridge-MAC-address。僅在啟用 MSTP 時適用。 |
| **registered-vlan-ids** (*integer 1..4094*) | 透過 [MVRP protocol](/docs/bridging-and-switching#mvrp) 在 bridge 介面上註冊的 VLAN。 |
| **root-bridge** (*yes \| no*) | 顯示 bridge 是否為 spanning tree 的 root bridge。 |
| **root-bridge-id** (*priority.MAC address*) | root bridge ID，格式為 bridge-priority.bridge-MAC-address。 |
| **root-path-cost** (*integer*) | 通往 root-bridge 的路徑總成本。 |
| **root-port** (*name*) | root bridge 所連接的埠。 |
| **state** (*enabled \| disabled*) | bridge 的狀態。 |

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

## 生成樹通訊協定 {#spanning-tree-protocol}

---

RouterOS bridge 介面能夠執行 Spanning Tree Protocol，以確保拓撲沒有迴圈並具備備援能力。對於只有 2 個 bridge 的小型網路，STP 不會帶來太多好處；但對於較大的網路，正確設定 STP 非常重要，若將 STP 相關數值保持在預設值，即使只有單一 bridge 故障，也可能導致整個網路無法連線。若要達成正確且無迴圈的備援拓撲，必須正確設定 bridge 優先權、埠路徑成本與埠優先權。

:::danger
在 RouterOS 中，可以將 bridge priority 設為 0 到 65535 之間的任何值，IEEE 802.1W 標準規定 bridge priority 必須以 4096 為間隔。這可能導致不支援此類數值的設備之間出現相容性問題。為避免相容性問題，建議只使用下列優先權：0、4096、8192、12288、16384、20480、24576、28672、32768、36864、40960、45056、49152、53248、57344、61440
:::

STP has multiple variants; currently, RouterOS supports STP, RSTP, and MSTP. Depending on needs, either one of them can be used; some devices are able to run some of these protocols using hardware offloading; detailed information about which devices support it can be found in the Hardware Offloading section. STP is considered to be outdated and slow; it has been almost entirely replaced in all network topologies by RSTP, which is backward compatible with STP. For network topologies that depend on VLANs, it is recommended to use MSTP since it is a VLAN-aware protocol and gives the ability to do load balancing per VLAN groups. There are a lot of considerations that should be made when designing an STP-enabled network, more detailed case studies can be found in the [Spanning Tree Protocol](/docs/bridging-and-switching/user-guides/spanning-tree-protocol) article. In RouterOS, the `protocol-mode` property controls the used STP variant.

:::info
RouterOS bridge does not work with PVST and its variants. The PVST BPDUs (with a MAC destination 01:00:0C:CC:CC:CD) are treated by RouterOS bridges as typical multicast packets. In simpler terms, they undergo RouterOS bridge/switch forwarding logic and may get tagged or untagged.
:::

:::info
By the IEEE 802.1ad standard, the BPDUs from bridges that comply with IEEE 802.1Q are not compatible with IEEE 802.1ad bridges. This means that the same bridge VLAN protocol should be used across all bridges in a single Layer2 domain; otherwise (R/M)STP will not function properly.
:::

### Per-port STP

There might be certain situations where you want to limit STP functionality on a single port or multiple ports. Below you can find examples for different use cases.

:::danger
Be careful when changing the default (R/M)STP functionality; make sure you understand the working principles of STP and BPDUs. Misconfigured (R/M)STP can cause unexpected behavior.
:::

#### Create Edge Ports

Edge ports are used for connections to end devices that have no other bridges attached, such as workstations or routers. Setting a bridge port as an edge port will restrict it from sending BPDUs (Bridge Protocol Data Units) and will cause it to ignore any received BPDUs. This allows the port to transition directly to the forwarding state, bypassing the standard STP learning and listening phases, which reduces network convergence time.

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 edge=yes
add bridge=bridge1 interface=ether2
```

## Drop Received BPDUs

The bridge firewall filter and NAT rules cannot drop BPDUs when the bridge has STP/RSTP/MSTP enabled because BPDUs receive special processing within the bridge. However, dropping received BPDUs on a specific port can be accomplished on some switch chips using ACL rules:

On MikroTik devices with a Marvell Prestera switch:

```ros
/interface/ethernet/switch/rule
add dst-mac-address=01:80:C2:00:00:00/FF:FF:FF:FF:FF:FF new-dst-ports="" port=ether1 switch=switch1
```

On CRS1xx/CRS2xx series devices with Access Control List (ACL) support:

```ros
/interface/ethernet/switch/acl
add action=drop mac-dst-address=01:80:C2:00:00:00 src-ports=ether1
```

This configuration drops all received BPDUs on **ether1**.

:::danger
If you intend to drop received BPDUs on a port, ensure that BPDUs are also prevented from being sent out through the interface that this port is connected to. A root bridge always transmits BPDUs and normally waits for a superior BPDU (from a bridge with a lower bridge ID). However, the bridge must temporarily disable the new root port when transitioning from a root bridge to a designated bridge. If you block BPDUs on only one side, the port will continuously flap between states.
:::

#### Enable BPDU guard

The BPDU Guard feature provides an additional layer of security for bridge ports. It is designed to prevent potential network issues by blocking a port if it receives a BPDU (Bridge Protocol Data Unit), which indicates an unauthorized bridge device has been connected. This is particularly useful for edge ports that should only connect to end devices. In this example, if **ether1** receives a BPDU, the port will be automatically blocked and will require manual intervention to re-enable it.

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 bpdu-guard=yes
add bridge=bridge1 interface=ether2
```

#### Enable Root Guard

Root Guard is a spanning tree security feature that prevents a port from becoming the root port, thereby protecting the active spanning tree topology from being influenced by external bridges. In this example, **ether1** is configured with `restricted-role=yes`. This setting prevents the port from becoming the root port for the CIST or any MSTI, regardless of its best spanning tree priority vector. Such a port will be selected as an Alternate Port (in discarding state) and will remain in that state as long as it continues to receive superior BPDUs. It will automatically transition to the forwarding state when it no longer detects a superior root path. Network administrators may enable this setting to safeguard against external bridges influencing the active spanning tree.

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

## Bridge Settings

---

Under the bridge settings menu, it is possible to control certain features for all bridge interfaces and monitor global bridge counters.

**Sub-menu:** `/interface/bridge/settings`

| Property | Description |
| :-- | :-- |
| **use-ip-firewall** (*yes \| no*; Default: **no**) | Direct bridged traffic to <a href="/docs/firewall-and-quality-of-service/firewall">IP/IPv6 firewall</a> (prerouting, forward, and postrouting sections of IP/IPv6 routing, see more details on <a href="/docs/firewall-and-quality-of-service/packet-flow-in-routeros#flow-of-bridged-packet">Packet Flow</a> article). Below are some use cases when this setting can be enabled to accomplish certain tasks: <br/><ul><li>In case you want to assign <a href="/docs/firewall-and-quality-of-service/queues#simple-queue" rel="nofollow">Simple Queues</a> or global <a href="/docs/firewall-and-quality-of-service/queues#queue-tree" rel="nofollow">Queue Tree</a> for traffic flowing through bridged ports.</li><li>In case you want to use IP/IPv6 firewall capabilities for traffic flowing through bridged ports, which would normally bypass IP/IPv6 firewall.</li></ul><br/><strong>Caution:</strong> Enabling the <code>use-ip-firewall</code> feature will turn off bridge <a href="/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fast-path">Fast Path</a>, which in turn affects the ability to <a href="/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fasttrack">fasttrack</a> connections going over that bridge. And because this setting introduces additional processing steps (prerouting, forward and postrouting chains), it will increase CPU usage even more when forwarding packets. <br/><strong>Routed traffic</strong>, including traffic from VLAN interfaces (e.g., <code>/interface/vlan</code> created on the bridge), <strong>is already processed by the IP firewall</strong>. In such cases, enabling this setting has no additional effect. <br/> |
| **use-ip-firewall-for-pppoe** (*yes \| no*; Default: **no**) | Direct bridged un-encrypted PPPoE encapsulated traffic to IP/IPv6 firewall. This property only has an effect when `use-ip-firewall` is set to `yes`. |
| **use-ip-firewall-for-vlan** (*yes \| no*; Default: **no**) | Direct bridged VLAN tagged traffic to IP/IPv6 firewall. This property only has an effect when <code>use-ip-firewall</code> is set to <span className="ros-icon-success"><code>yes</code></span>. <br/> If you need to use the IP/IPv6 firewall and bridge <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> is enabled (which involves VLAN tag handling), then you should also enable <code>use-ip-firewall-for-vlan=yes</code>. <br/> When this setting is enabled and packets are routed between VLAN interfaces (e.g., <code>/interface/vlan</code>), the <code>in-interface</code> in the IP firewall's <strong>prerouting</strong> chain will match the bridge interface instead of the individual VLAN interface. |
| **allow-fast-path** (*yes \| no*; Default: **yes**) | Whether to enable a bridge Fast Path globally. |
| **bridge-fast-path-active** (*yes \| no*; Default: *)* | Shows whether a bridge Fast Path is active globally. Fast Path status per bridge interface is not displayed. |
| **bridge-fast-path-packets** (*integer*; Default: *)* | Shows packet count forwarded by bridge Fast Path. |
| **bridge-fast-path-bytes** (*integer*; Default: *)* | Shows byte count forwarded by bridge Fast Path. |
| **bridge-fast-forward-packets** (*integer*; Default: *)* | Shows packet count forwarded by bridge Fast Forward. |
| **bridge-fast-forward-bytes** (*integer*; Default: *)* | Shows byte count forwarded by bridge Fast Forward. |

:::warning
In case you want to assign Simple Queues or global Queue Trees to traffic that is being forwarded by a bridge, then you need to enable the `use-ip-firewall` property. Without using this property the bridge traffic will never reach the postrouting chain. Simple Queues and global Queue Trees are working in the postrouting chain. To assign Simple Queues or global Queue Trees for VLAN or PPPoE traffic in a bridge you should enable the appropriate properties as well.
:::

## Port Settings

---

The Port submenu is used to add interfaces in a particular bridge.

**Sub-menu:** `/interface/bridge/port`

| Property | Description |
| :-- | :-- |
| **auto-isolate** (*yes \| no*; Default: **no**) | When enabled, it prevents a port from moving from discarding state into forwarding state if no BPDUs are received from the neighboring bridge. The port will change into a forwarding state only when a BPDU is received. This property only has an effect when `protocol-mode` is set to `rstp` or `mstp` and `edge` is set to `no`. |
| **bpdu-guard** (*yes \| no*; Default: **no**) | Enables or disables the BPDU Guard feature on a port. This feature puts the port in a disabled role if it receives a BPDU and requires the port to be manually disabled and enabled if a BPDU is received. It should be used to prevent a bridge from BPDU-related attacks. This property has no effect when `protocol-mode` is set to `none`. |
| **bridge** (*name*; Default: **none**) | The bridge interface where the respective interface is grouped. |
| **broadcast-flood** (*yes \| no*; Default: **yes**) | When enabled, the bridge floods broadcast traffic to all bridge egress ports. When disabled, the bridge drops broadcast traffic on egress ports. It can be used to filter all broadcast traffic on an egress port. Broadcast traffic is considered as traffic that uses **FF:FF:FF:FF:FF:FF** as the destination MAC address. Such traffic is crucial for many protocols such as DHCP, ARP, NDP, BOOTP (Netinstall), and others. This option does not limit traffic flood to the CPU. |
| **edge** (*auto \| no \| no-discover \| yes \| yes-discover*; Default: **auto**) | Set a port as an edge port or a non-edge port, or enable edge discovery. Edge ports are connected to a LAN that has no other bridges attached. An edge port will skip the learning and the listening states in STP and will transition directly to the forwarding state. This reduces the STP initialization time. If the port is configured to discover an edge port, then as soon as the bridge detects a BPDU coming to an edge port, the port becomes a non-edge port. This property has no effect when <code>protocol-mode</code> is set to <code>none</code>.<ul><li><span className="ros-icon-success"><code>no</code></span> - non-edge port with disabled discovery. It will participate in learning and listening states in STP. It will not transition to the forwarding state until it exchanges BPDUs and reaches agreement with the connected bridge. If no BPDU is received, the port may remain in a non-forwarding state indefinitely.</li><li><span className="ros-icon-success"><code>no-discover</code></span> - non-edge port with enabled discovery. It will participate in learning and listening states in STP. A port can become an edge port if no BPDU is received.</li><li><span className="ros-icon-success"><code>yes</code></span> - edge port without discovery. It will transition directly to forwarding state.</li><li><span className="ros-icon-success"><code>yes-discover</code></span> - edge port with enabled discovery. It will transition directly to forwarding state.</li><li><span className="ros-icon-success"><code>auto</code></span> - same as <span className="ros-icon-success"><code>no-discover</code></span>, but will additionally detect if a bridge port is a Wireless interface with disabled bridge-mode. Such an interface will be automatically set as an edge port without discovery.</li></ul> |
| **fast-leave** (*yes \| no*; Default: **no**) | Enables the IGMP/MLD fast leave feature on the bridge port. The bridge will stop forwarding multicast traffic to a bridge port when an IGMP/MLD leave message is received. This property only has an effect when `igmp-snooping` is set to `yes`. |
| **frame-types** (*admit-all \| admit-only-untagged-and-priority-tagged \| admit-only-vlan-tagged*; Default: **admit-all**) | Specifies allowed ingress frame types on a bridge port. This property only has an effect when `vlan-filtering` is set to `yes`. |
| **ingress-filtering** (*yes \| no*; Default: **yes**) | Enables or disables VLAN ingress filtering, which checks if the ingress port is a member of the received VLAN ID in the bridge VLAN table. Should be used with `frame-types` to specify if the ingress traffic should be tagged or untagged. This property only has an effect when `vlan-filtering` is set to `yes`. The setting is enabled by default since RouterOS v7. |
| **learn** (*auto \| no \| yes*; Default: **auto**) | Changes MAC learning behavior on a bridge port<ul><li><span className="ros-icon-success"><code>yes</code></span> - enables MAC learning</li><li><span className="ros-icon-success"><code>no</code></span> - disables MAC learning</li><li><span className="ros-icon-success"><code>auto</code></span> - detects if the bridge port is a Wireless interface and uses a Wireless registration table instead of MAC learning, will use the Wireless registration table if the Wireless interface is set to one of <span className="ros-icon-success"><code>ap-bridge</code></span>, <span className="ros-icon-success"><code>bridge</code></span>, <span className="ros-icon-success"><code>wds-slave</code></span> mode and bridge mode for the Wireless interface is disabled.</li></ul> |
| **multicast-router** (*disabled \| permanent \| temporary-query*; Default: **temporary-query**) | A multicast router port is a port where a multicast router or querier is connected. On this port, unregistered multicast streams and IGMP/MLD membership reports will be sent. This setting changes the state of the multicast router for bridge ports. This property can be used to send IGMP/MLD membership reports to certain bridge ports for further multicast routing or proxying. This property only has an effect when <code>igmp-snooping</code> is set to <span className="ros-icon-success"><code>yes</code></span>.<ul><li><span className="ros-icon-success"><code>disabled</code></span> - disabled multicast router state on the bridge port. Unregistered multicast and IGMP/MLD membership reports are not sent to the bridge port regardless of what is connected to it.</li><li><span className="ros-icon-success"><code>permanent</code></span> - enabled multicast router state on the bridge port. Unregistered multicast and IGMP/MLD membership reports are sent to the bridge port regardless of what is connected to it.</li><li><span className="ros-icon-success"><code>temporary-query</code></span> - automatically detect multicast router state on the bridge port using IGMP/MLD queries.</li></ul> |
| **horizon** (*integer 0..429496729*; Default: **none**) | Use split horizon bridging to prevent bridging loops. Set the same value for a group of ports, to prevent them from sending data to ports with the same horizon value. Split horizon is a software feature that disables hardware offloading. |
| **hw** (*yes \| no*; Default: **yes**) | Allows enabling or disabling [hardware offloading](/docs/bridging-and-switching#bridge-hardware-offloading) on interfaces capable of HW offloading. For software interfaces like [EoIP](/docs/virtual-private-networks/eoip) or [VLAN](/docs/vlan), this setting is ignored and has no effect. Certain bridge or port functions can automatically disable HW offloading, use the `print` command to see whether the "H" flag is active. |
| **internal-path-cost** (*integer: 1..200000000*; Default: ) | Path cost to the interface for MSTI0 inside a region. If not manually configured, the bridge automatically determines the internal-path-cost based on the interface speed and the <code>port-cost-mode</code> setting. To revert to the automatic determination and remove any manually applied value, simply use an exclamation mark before the <code>internal-path-cost</code> property. This property only has an effect when <code>protocol-mode</code> is set to <code>mstp</code>. <br/><code>/interface/bridge/port/set [find interface=sfp28-1] !internal-path-cost</code> Use <a href="/docs/bridging-and-switching#bridge-port-monitoring">port monitor</a> to observe the applied internal-path-cost. <br/> |
| **interface** (*name*; Default: **none**) | Name of the interface or interface list. |
| **path-cost** (*integer: 1..200000000*; Default: ) | Path cost to the interface, used by STP and RSTP to determine the best path, and used by MSTP to determine the best path between regions. If not manually configured, the bridge automatically determines the path-cost based on the interface speed and the <code>port-cost-mode</code> setting. To revert to the automatic determination and remove any manually applied value, simply use an exclamation mark before the <code>path-cost</code> property. This property has no effect when <code>protocol-mode</code> is set to <code>none</code>. <br/><code>/interface/bridge/port/set [find interface=sfp28-1] !path-cost</code> Use <a href="/docs/bridging-and-switching#bridge-port-monitoring">port monitor</a> to observe the applied path-cost. <br/> |
| **point-to-point** (*auto \| yes \| no*; Default: **auto**) | Specifies if a bridge port is connected to a bridge using a point-to-point link for faster convergence in case of failure. By setting this property to `yes`, you are forcing the link to be a point-to-point link, which will skip the checking mechanism, which detects and waits for BPDUs from other devices on this single link. By setting this property to `no`, you are expecting that a link can receive BPDUs from multiple devices. By setting the property to `yes`, you are significantly improving (R/M)STP convergence time. In general, you should only set this property to `no` if it is possible that another device can be connected to a link. This is mostly relevant to Wireless mediums and Ethernet hubs. If the Ethernet link is full-duplex, `auto` enables point-to-point functionality. This property has no effect when `protocol-mode` is set to `none`. |
| **priority** (*0x00 \| 0x10 \| 0x20 \| 0x30 \| 0x40 \| 0x50 \| 0x60 \| 0x70 \| 0x80 \| 0x90 \| 0xa0 \| 0xb0 \| 0xc0 \| 0xd0 \| 0xe0 \| 0xf0*; Default: **0x80**) | The priority of the interface, used by STP to determine the root port, used by MSTP to determine the root port between regions. Must be set in steps of 16 (0x10). |
| **pvid** (*integer 1..4094*; Default: **1**) | Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. This property only has an effect when `vlan-filtering` is set to `yes`. |
| **restricted-role** (*yes \| no*; Default: **no**) | Enables or disables the restricted role on a port. When enabled, it prevents the port from becoming the root port for the CIST or any MSTI, regardless of its best spanning tree priority vector. Such a port will be selected as an Alternate Port (discarding state) and remains so as long as it continues to receive superior BPDUs. It will automatically transition to the forwarding state when it no longer detects a superior root path. Network administrators may enable this setting to safeguard against external bridges influencing the active spanning tree, a feature also known as root-guard or root-protection. This property has an effect when `protocol-mode` is set to `stp`, `rstp`, or `mstp` (support for STP and RSTP is available since RouterOS v7.14). |
| **restricted-tcn** (*yes \| no*; Default: **no**) | Enables or disables topology change notification (TCN) handling on a port. When enabled, it causes the port not to propagate received topology change notifications to other ports, and any changes caused by the port itself do not result in topology change notification to other ports. This parameter is disabled by default. It can be set by a network administrator to prevent external bridges from causing MAC address flushing in the local network. This property has an effect when `protocol-mode` is set to `stp`, `rstp`, or `mstp` (support for STP and RSTP is available since RouterOS v7.14). |
| **tag-stacking** (*yes \| no*; Default: **no**) | Forces all packets to be treated as untagged packets. Packets on the ingress port will be tagged with another VLAN tag regardless of whether a VLAN tag already exists. Packets will be tagged with a VLAN ID that matches the `pvid`value and will use EtherType that is specified in `ether-type`. This property only has an effect when `vlan-filtering` is set to `yes`. |
| **trusted** (*yes \| no*; Default: **no**) | When enabled, it allows forwarding DHCP packets towards the DHCP server through this port. Mainly used to prevent unauthorized servers from providing malicious information for users. This property only has an effect when `dhcp-snooping` is set to `yes`. |
| **trusted-dhcpv6**(*yes \| no*; Default: **no**) | When enabled, it allows forwarding DHCPv6 packets towards the DHCP server through this port. Mainly used to prevent unauthorized servers from providing malicious information for users. This property only has an effect when `dhcpv6-snooping` is set to `yes`. |
| **trusted-ra** (*yes \| no*; Default: **no**) | Specifies whether the port is permitted to forward IPv6 Router Advertisement messages; set to **yes** for ports connected to legitimate routers and **no** to block unauthorized sources. This property only has an effect when `ra-guard` is set to `yes`. |
| **unknown-multicast-flood** (*yes \| no*; Default: **yes**) | Changes the multicast flood option on the bridge port and only controls the egress traffic. When enabled, the bridge allows flooding multicast packets to the specified bridge port, but when disabled, the bridge restricts multicast traffic from being flooded to the specified bridge port. The setting affects all multicast traffic. This includes non-IP, IPv4, IPv6 and the link-local multicast ranges (e.g. 224.0.0.0/24 and ff02::1). <br/> Note that when <code>igmp-snooping</code> is enabled and an IGMP/MLD querier is detected, the bridge will automatically restrict unknown IP multicast from being flooded, so the setting is not mandatory for IGMP/MLD snooping setups. <br/> When using this setting together with <code>igmp-snooping</code>, the only multicast traffic that is allowed on the bridge port is the known multicast from the MDB table. |
| **unknown-unicast-flood** (*yes \| no*; Default: **yes**) | Changes the unknown unicast flood option on the bridge port and only controls the egress traffic. When enabled, the bridge allows flooding unknown unicast packets to the specified bridge port, but when disabled, the bridge restricts unknown unicast traffic from being flooded to the specified bridge port. <br/> If a MAC address is not learned in the host table, then the traffic is considered unknown unicast traffic and will be flooded to all ports. MAC address is learned as soon as a packet on a bridge port is received and the source MAC address is added to the bridge host table. Since it is required for the bridge to receive at least one packet on the bridge port to learn the MAC address, it is recommended to use static bridge host entries to avoid packets being dropped until the MAC address has been learned. |

:::info
RouterOS can handle a maximum of 1024 bridged interfaces per bridge; this limit is fixed and cannot be modified. If you try to add more interfaces as bridge ports, it may lead to unpredictable behavior.
:::

### Example {#example-1}

This example demonstrates how to add Ethernet ports to an existing bridge interface to create a simple Layer 2 switching setup. By adding **ether1** and **ether2** to **bridge1**, these physical ports become part of a single switched network segment, allowing devices connected to either port to communicate with each other as if they were on the same LAN.

First, add each port to the bridge interface:

```ros
[admin@MikroTik] /interface/bridge/port/add bridge=bridge1 interface=ether1
[admin@MikroTik] /interface/bridge/port/add bridge=bridge1 interface=ether2
```

Verify the configuration by displaying the bridge port table:

```ros
[admin@MikroTik] /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE       BRIDGE       HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0     ether1          bridge1      yes  100     0x80         10                 10       none
 1     ether2          bridge1      yes  200     0x80         10                 10       none
```

The output confirms both ports are now bridged together. The **H** flag indicates that hardware offloading is active, meaning the switch chip is handling packet forwarding for optimal performance. Each port is assigned a default PVID (Port VLAN ID) of 100 and 200 respectively, and both use the standard STP priority of 0x80.

### Interface Lists

Starting with RouterOS v6.41, interface lists can be added as bridge ports and sorted. Interface lists simplify firewall rule configuration by grouping multiple interfaces together. The following example demonstrates how to add an interface list to a bridge:

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

When interface lists are added to a bridge, the individual ports from those lists appear as dynamic ports entries:

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

The order in which interface lists appear can be rearranged using the `move` command. The second parameter specifies the position before which the selected interface list should be placed. The following example demonstrates how to sort interface lists:

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
When using the `move` command, the second parameter represents the "before id" position, which determines where the selected interface list will be moved. If the first interface list is moved to the position of the second interface list, the command has no effect since the first list would already be positioned before the second list.
:::

### Interface Lists in VLAN Table

Starting from RouterOS version 7.17, you can use interface lists for the `tagged` and `untagged` properties in the bridge VLAN table. This enhancement allows for more flexible VLAN assignment to ports by simply modifying the interface list members, rather than updating each bridge VLAN entry individually.

If different interface lists are specified for the `tagged` and `untagged` settings, and there is overlap between the interface members, the `untagged` list takes priority. You can check the current interface configuration using the `current-tagged` and `current-untagged` properties with the `print` command.

The following example demonstrates how new interfaces can be added to existing interface lists, automatically updating the bridge port and VLAN table without directly modifying settings in those menus:

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

# make necessary changes to interface list members:
/interface/list/member/add list=vlan20_untagged interface=ether5
/interface/list/member/add list=vlan_tagged interface=sfp-sfpplus2 

# verify changes in bridge port and vlan menus:
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

### Bridge Port Monitoring

To monitor the current status of bridge ports, use the `monitor` command.

**Sub-menu:** `/interface/bridge/port/monitor`

| Property | Description |
| :-- | :-- |
| **actual-path-cost** (*integer: 1..200000000*) | Shows the actual port path-cost. Either manually applied or automatically determined based on the interface speed and the `port-cost-mode` setting. |
| **declared-vlan-ids** (*integer 1..4094*) | VLANs declared by the interface via [MVRP Protocol](/docs/bridging-and-switching#mvrp). |
| **designated-bridge-id** (*priority.MAC address*) | Shows the designated bridge identifier, as determined from the port's priority vector. |
| **designated-cost** (*integer*) | Shows the designated root-path-cost, as determined from the port's priority vector. |
| **designated-internal-cost** (*integer*) | Shows the designated internal-root-path-cost, as determined from the port's priority vector. |
| **designated-message-age**(*time)* | Shows the designated message age, as determined from the port's priority vector. |
| **designated-max-age** (*time)* | Shows the designated max age, as determined from the port's priority vector. The BPDU packet can pass as many bridges as specified in the `max-message-age` parameter. |
| **designated-port-id** (*priority*.*integer*) | Shows the designated port identifier, as determined from the port's priority vector. |
| **designated-remaining-hops** (*integer*) | Shows the designated remaining hops, as determined from the port's priority vector. Number of hops that a packet is allowed to traverse before reaching its destination. |
| **discard-transitions** (*integer*) | Counter, registering how often port transitions into discarding state. |
| **edge-port** (*yes \| no*) | Whether the port is an edge port or not. |
| **edge-port-discovery** (*yes \| no*) | Whether the port is set to automatically detect edge ports. |
| **external-fdb** (*yes \| no*) | Whether the registration table is used instead of a forwarding database. |
| **forwarding** (*yes \| no*) | Shows if the port is not blocked by (R/M)STP. |
| **forward-transitions** (*integer*) | Counter, registering how often port transitions into forwarding state |
| **hw-offload-group** (*switchX*) | Switch chip used by the port. |
| **interface** (*name*) | Interface name. |
| **last-topology-change** (*time)* | Last topology change timer, records time since the last change. |
| **learning** (*yes \| no*) | Shows whether the port is capable of learning MAC addresses. |
| **multicast-router** (*yes \| no*) | Shows if a multicast router is detected on the port. Monitoring value appears only when `igmp-snooping` is enabled. |
| **registered-vlan-ids** (*integer 1..4094*) | VLANs where the interface is registered via [MVRP Protocol](/docs/bridging-and-switching#mvrp). |
| **port-id** (*priority*.*integer*) | In Spanning Tree Protocol each port has a unique Port Identifier. Priority[hex] + port number. |
| **point-to-point-port** (*yes \| no*) | Whether the port is connected to a bridge port using full-duplex (yes) or half-duplex (no). |
| **role** (*designated \| root-port \| alternate \| backup \| disabled*) | (R/M)STP algorithm assigned port role: <br/><ul><li><span className="ros-icon-success"><code>disabled-port</code></span> - disabled or inactive port.</li><li><span className="ros-icon-success"><code>root-port</code></span> - port that is facing towards the root bridge and has the best (lowest cost) path to the root bridge. Only one root port is elected per bridge (except the root bridge itself).</li><li><span className="ros-icon-success"><code>alternative-port</code></span> - port that is facing towards the root bridge, but is not going to forward traffic. Port provides a backup path to the root bridge if the current root port fails.</li><li><span className="ros-icon-success"><code>designated-port</code></span> - port that is facing away from the root bridge and forwards traffic away from the root bridge to downstream devices.</li><li><span className="ros-icon-success"><code>backup-port</code></span> - port that is facing away from the root bridge, but is going to forward traffic. Port that serves as a backup for a designated port on the same segment.</li></ul> In RouterOS, the <strong>role</strong> monitoring property displays RSTP roles, such as <code>alternate-port</code> and <code>backup-port</code>, even when STP mode is enabled. While this is technically incorrect, it does not affect the operation of STP. This is because STP treats all blocked ports the same, without differentiating their purpose (e.g., as potential backup paths). The displayed roles are simply a reflection of RSTP functionality and have no practical impact when STP is in use. See more details on <a href="/docs/bridging-and-switching/user-guides/spanning-tree-protocol#stp-and-rstp">STP and RSTP page</a>. |
| **root-path-cost** (*integer*) | The total cost of the path to the root-bridge. |
| **sending-rstp** (*yes \| no*) | Whether the port is using RSTP or MSTP BPDU types. A port will transit to STP type when RSTP/MSTP enabled port receives an STP BPDU. This setting **does not** indicate whether the BPDUs are actually sent. |
| **status** (*in-bridge \| inactive*) | Port status:<ul><li><span className="ros-icon-success"><code>in-bridge</code></span> - port is enabled</li><li><span className="ros-icon-success"><code>inactive</code></span> - port is disabled.</li></ul> |
| **tx-rx-bpdu** (*integer*) | Sent/received bpdu messages counter. |
| **tx-rx-tc** (*integer*) | Topology change messages transmitted/received. |
| **topology-changes** (*integer*) | Topology change counter. |

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

## Hosts Table

---

The hosts table displays MAC addresses that have been learned on a bridge interface. This table also shows various flags that provide additional information about each host entry. Access the hosts table through the `/interface/bridge/host` submenu.

**Sub-menu:** `/interface/bridge/host`

| Property | Description |
| :-- | :-- |
| **bridge** (*read-only: name*) | The bridge to which the host entry belongs |
| **disabled** (*read-only: flag*) | Indicates whether the static host entry is disabled |
| **dynamic** (*read-only: flag*) | Indicates whether the host was dynamically learned |
| **external** (*read-only: flag*) | Indicates whether the host was learned from an external table, such as a switch chip or Wireless registration table. Static host entries added on hardware-offloaded bridge ports do not display this flag |
| **invalid** (*read-only: flag*) | Indicates whether the host entry is invalid. This flag may appear for statically configured hosts on an interface that has been removed |
| **local** (*read-only: flag*) | Indicates whether the host entry was created from the bridge itself, which displays all local interfaces |
| **mac-address** (*read-only: MAC address*) | The MAC address of the host |
| **on-interface** (*read-only: name*) | The bridge port to which the host is connected |

### Monitoring

To view the active hosts table, use the `print` command. The table displays all MAC addresses that have been learned on the bridge interface, along with flags indicators and connection details.

```ros
[admin@MikroTik] /interface/bridge/host/print
Flags: X - disabled, I - invalid, D - dynamic, L - local, E - external 
 #       MAC-ADDRESS        VID ON-INTERFACE            BRIDGE
0   D   B8:69:F4:C9:EE:D7      ether1                  bridge1
1   D   B8:69:F4:C9:EE:D8      ether2                  bridge1
2   DL  CC:2D:E0:E4:B3:38      bridge1                 bridge1
3   DL  CC:2D:E0:E4:B3:39      ether2                  bridge1
```

The output shows:

- **D** flag: Dynamically learned MAC addresses
- **DL** flag: Local interface MAC addresses (the bridge itself and its ports interfaces)
- **VID**: VLAN ID associated with the host entry
- **ON-INTERFACE**: The bridge port where the host was learned
- **BRIDGE**: The bridge interface the host belongs to

### Static Entries

The bridge host table supports static MAC address entries configuration. Static entries is useful in two primary scenarios: directing specific traffic through a designated port, and securing device resources by disabling dynamic MAC learning while relying solely on pre-configured static entries.

The following table lists all configurable parameters for static MAC address entries:

**Sub-menu:** `/interface/bridge/host`

| Property | Description |
| :-- | :-- |
| **bridge** (*name*; Default: **none**) | The bridge interface to which the MAC address is assigned. |
| **disabled** (*yes \| no*; Default: **no**) | Enables or disables the static MAC address entry. |
| **interface** (*name*; Default: **none**) | Name of the interface where the MAC address traffic is forwarded. |
| **mac-address** (*MAC address*; Default: ) | The MAC address to be added to the host table statically. |
| **vid** (*integer: 1..4094*; Default: ) | VLAN ID associated with the static MAC address entry. |

**Example:** To forward all traffic destined for MAC address **4C:5E:0C:4D:12:43** exclusively through **ether2**, use the following command:

```ros
/interface/bridge/host
add bridge=bridge1 interface=ether2 mac-address=4C:5E:0C:4D:12:43
```

## Multicast Table

---

The Multicast Table displays multicast group membership information learned through IGMP/MLD snooping. When IGMP/MLD snooping is enabled on a bridge, the device actively monitors IGMP/MLD network communications to build a Multicast Database (MDB) of active multicast groups and their subscribed ports members. The bridge then uses this information to intelligently forward multicast traffic only to ports where interested receivers devices are connected, rather than flooding all ports with multicast traffic.

Note that packets addressed to link-local multicast groups 224.0.0.0/24 and ff02::1 are exceptions to this behavior - these addresses are always flooded to all ports and VLANs without restriction, as they are used for network protocol operations.

To view the current multicast database entries table, use the `print` command in the multicast database submenu.

**Sub-menu:** `/interface/bridge/mdb`

| Property | Description |
| :-- | :-- |
| <strong>bridge</strong> (<em>read-only: name</em>) | Shows the bridge interface the entry belongs to. |
| <strong>group</strong> (*read-only:*ipv4 | ipv6 |
| <strong>on-interface</strong> (<em>read-only: name</em>) | Shows the bridge ports which are subscribed to the multicast group. |
| <strong>vid</strong> (<em>read-only: integer</em>) | Shows the VLAN ID for the multicast group, only applies when <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> is enabled. |

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

### Static entries

Since RouterOS version 7.7, it is possible to create static MDB entries for IPv4 and IPv6 multicast groups.

**Sub-menu:** `/interface/bridge/mdb`

| Property | Description |
| :-- | :-- |
| **bridge** (*name*; Default: ) | The bridge interface to which the MDB entry is going to be assigned. |
| **disabled** (*yes \| no*; Default: **no**) | Disables or enables the static MDB entry. |
| **group** (*ipv4 \| ipv6 \| MAC address*; Default: ) | The IPv4, IPv6 or MAC multicast address. Static entries for link-local multicast groups 224.0.0.0/24 and ff02::1 cannot be created, as these packets are always flooded on all ports and VLANs. |
| **interface** (*name*; Default: ) | The list of bridge ports to which the multicast group will be forwarded. |
| **vid** (*integer: 1..4094*; Default: ) | The VLAN ID on which the MDB entry will be created only applies when `vlan-filtering` is enabled. When VLAN ID is not specified, the entry will work in shared-VLAN mode and dynamically apply to all defined VLAN IDs for particular ports. |

For example, to create a static MDB entry for multicast group 229.10.10.10 on ports ether2 and ether3 on VLAN 10, use the command below:

```ros
/interface/bridge/mdb
add bridge=bridge1 group=229.10.10.10 interface=ether2,ether3 vid=10
```

Verify the results with the `print` command:

```ros
[admin@MikroTik] > /interface/bridge/mdb/print where group=229.10.10.10
Columns: GROUP, VID, ON-PORTS, BRIDGE
 # GROUP         VID  ON-PORTS  BRIDGE 
12 229.10.10.10   10  ether2    bridge1
                      ether3   
```

In case a certain IPv6 multicast group does not need to be snooped and it is desired for it to be flooded on all ports and VLANs, it is possible to create a static MDB entry on all VLANs and ports, including the bridge interface itself. Use the command below to create a static MDB entry for multicast group ff02::2 on all VLANs and ports (modify the `ports` setting for your particular setup):

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

## Bridge Hardware Offloading

---

It is possible to switch multiple ports together if a device has a built-in switch chip. While a bridge is a software feature that will consume CPU's resources, the bridge hardware offloading will allow you to use the built-in switch chip to forward packets at wire speed. This allows you to achieve higher throughput if configured correctly.

![HWoffloading_diagram](/img/8d426fcfc1794e99.webp)

A packet that is received by one of the ports always passes through the switch logic first. Switch logic decides which ports the packet should be going to - usually based on the destination MAC address. Hardware-forwarded packets will not be visible to RouterOS (only statistics will show that a packet has passed through). This is because the packet was already processed by the switch chip and never reached the CPU.

Packets can be forwarded to the CPU via the switch CPU port for management access, routing, firewall rules, or traffic control. This requires configuration specific to your device and use case. Check the manual page for your specific device:

- [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features)
- [CRS1xx/2xx series switches](/docs/bridging-and-switching/user-guides/crs1xx-2xx-series-switches-examples)
- [Non-CRS series switches](/docs/bridging-and-switching/switch-chip-features)

:::danger
Certain bridge and Ethernet port properties are directly related to switch chip settings. Changing such properties can trigger a **switch chip reset**, temporarily disabling all Ethernet ports. This must be taken into account whenever changing properties in production environments. Such properties include DHCP Snooping, IGMP Snooping, VLAN filtering, L2MTU, Flow Control, and others. The exact settings that can trigger a switch chip reset depend on the device's model.
:::

:::warning
[CRS1xx/2xx series switches](/docs/bridging-and-switching/crs1xx-and-2xx-series-switches#multiple-switch-groups) support multiple hardware offloaded bridges per switch chip. All other devices support only one. Use `hw=yes/no` under `/interface/bridge/port` to select which bridge uses hardware offloading.
:::

The following tables list which bridge features are supported with hardware offloading (✓) or disable hardware offloading (✗) for each switch chip type:

### MikroTik devices with Marvell Prestera Switch

For example: CRS3xx, CRS4xx, CRS5xx, CRS8xx, CCR2116, CCR2216, RDS2216. See [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features).

| Feature | HW Offload |
| :-- | :--: |
| STP/RSTP | ✓ |
| MSTP | ✓ |
| VLAN Filtering | ✓ |
| IGMP Snooping | ✓ |
| DHCP Snooping | ✓ |
| DHCPv6 Snooping | ✓ |
| RA Guard | ✓ |
| Bonding¹ | ✓ |
| MLAG | ✓ |
| Horizon | ✗ |

¹ Only `mode=802.3ad` (LACP), `mode=balance-xor` (static LAG) and `mode=active-backup` bonding interfaces are hardware offloaded. Other modes do not support HW offloading. The switch always uses Layer2+Layer3+Layer4 for transmit hash policy, changing transmit hash policy has no effect.

### 88E6393X, 88E6191X, 88E6190

For example: RB5009 series, L009 series, CCR2004-16G-2S+. See [Switch Chip Features](/docs/bridging-and-switching/switch-chip-features).

| Feature | HW Offload |
| :-- | :--: |
| STP/RSTP | ✓ |
| MSTP | ✓ |
| VLAN Filtering¹ | ✓ |
| IGMP Snooping² | ✓ |
| DHCP Snooping² | ✓ |
| Bonding³ | ✓ |
| DHCPv6 Snooping | ✗ |
| RA Guard | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

¹ Does not support `ether-type=0x88a8` or `ether-type=0x9100` (only default `ether-type=0x8100` is supported). No `tag-stacking=yes` support. Using these features disables HW offload.  
² No QinQ support, only the first VLAN tag is parsed. Double-tagged DHCP or IGMP packets may be processed incorrectly.  
³ Only `mode=802.3ad` (LACP), `mode=balance-xor` (static LAG) and `mode=active-backup` bonding interfaces are hardware offloaded. Other modes do not support HW offloading. Limited to Layer2 transmit hash, changing transmit hash policy has no effect.

### MT7621, MT7531, EN7523, RTL8367

For example: hEX S, hAP ax lite, hEX Refresh, RBM33G, RB4011, RB1100AHx4. See [Switch Chip Features](/docs/bridging-and-switching/switch-chip-features).

| Feature | HW Offload |
| :-- | :--: |
| STP/RSTP | ✓ |
| MSTP | ✓ |
| VLAN Filtering¹ | ✓ |
| IGMP Snooping | ✗ |
| DHCP Snooping | ✗ |
| DHCPv6 Snooping | ✗ |
| RA Guard | ✗ |
| Bonding | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

¹ Does not support `ether-type=0x88a8` or `ether-type=0x9100` (only default `ether-type=0x8100` is supported). No `tag-stacking=yes` support. Using these features disables HW offload.

### CRS1xx/CRS2xx series

For example: CRS105, CRS106, CRS109, CRS112, CRS125, CRS210, CRS212, CRS226. See [CRS1xx/2xx series switches](/docs/bridging-and-switching/crs1xx-and-2xx-series-switches).

| Feature | HW Offload |
| :-- | :--: |
| STP/RSTP | ✓ |
| IGMP Snooping¹ | ✓ |
| DHCP Snooping¹ | ✓ |
| MSTP | ✗ |
| VLAN Filtering | ✗ |
| DHCPv6 Snooping | ✗ |
| RA Guard | ✗ |
| Bonding | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

¹ Feature does not work properly in VLAN switching setups.

### QCA8337, Atheros8327, Atheros8316

For example: RB3011, RB1100AHx2, RB850Gx2, cAP ac, wAP ac, Audience, mANTBox, CCR1009. See [Switch Chip Features](/docs/bridging-and-switching/switch-chip-features).

| Feature | HW Offload |
| :-- | :--: |
| STP/RSTP | ✓ |
| DHCP Snooping¹ | ✓ |
| MSTP | ✗ |
| VLAN Filtering | ✗ |
| IGMP Snooping | ✗ |
| DHCPv6 Snooping | ✗ |
| RA Guard | ✗ |
| Bonding | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

¹ Feature does not work properly in VLAN switching setups.

### Atheros8227, Atheros7240

For example: hAP lite, hEX lite, PowerBox, wsAP ac lite, RBmAP2nD. See [Switch Chip Features](/docs/bridging-and-switching/switch-chip-features).

| Feature | HW Offload |
| :-- | :--: |
| STP/RSTP | ✓ |
| MSTP | ✗ |
| VLAN Filtering | ✗ |
| IGMP Snooping | ✗ |
| DHCP Snooping | ✗ |
| DHCPv6 Snooping | ✗ |
| RA Guard | ✗ |
| Bonding | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

### IPQ-PPE, QCA8386, PIPE 98PX1012

For example: hAP ax series, cAP ax, Chateau ax series, hAP be³ Media, CCR2004-1G-12S+2XS. See [Switch Chip Features](/docs/bridging-and-switching/switch-chip-features).

| Feature | HW Offload |
| :-- | :--: |
| STP/RSTP | ✗ |
| MSTP | ✗ |
| VLAN Filtering | ✗ |
| IGMP Snooping | ✗ |
| DHCP Snooping | ✗ |
| DHCPv6 Snooping | ✗ |
| RA Guard | ✗ |
| Bonding | ✗ |
| MLAG | ✗ |
| Horizon | ✗ |

:::danger
Using `protocol-mode=none` on **IPQ-PPE** enables HW offloaded bridge and can cause issues.  
It is recommended to use a non-HW offloaded bridge by keeping the default `protocol-mode=rstp` setting or by manually setting `hw=no` under `/interface/bridge/port`.
:::

### Example {#example-2}

The following example demonstrates how to configure port switching using a bridge with hardware offloading enabled. This configuration creates a bridge interface and adds multiple Ethernet interfaces as bridge ports. The `hw=yes` bridge port setting is used by default.

```ros
/interface bridge
add name=bridge1
/interface bridge port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
```

Verify that hardware offloading is active by checking the **H** flag in the bridge port table:

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

## Bridge VLAN Filtering

---

Bridge VLAN Filtering enables VLAN-aware Layer 2 forwarding and allows VLAN tag modification within the bridge. This feature makes the bridge operate more like a traditional Ethernet switch and helps resolve Spanning Tree compatibility issues that can occur when VLAN interfaces are bridged. Configuring Bridge VLAN Filtering is highly recommended to comply with STP (IEEE 802.1D) and RSTP (IEEE 802.1W) standards, and it is mandatory to enable MSTP (IEEE 802.1s) support in RouterOS.

The primary VLAN setting is `vlan-filtering`, which globally controls VLAN awareness and VLAN tag processing for the bridge. When `vlan-filtering` is set to `no`, the bridge ignores VLAN tags, operates in shared-VLAN-learning (SVL) mode, and cannot modify VLAN tags of packets. Enabling `vlan-filtering` activates all bridge VLAN-related functionality and switches to independent-VLAN-learning (IVL) mode. In addition to joining ports for Layer 2 forwarding, the bridge itself functions as an interface and therefore has a Port VLAN ID (pvid).

:::warning
Currently, MikroTik devices with Marvell Prestera switch and RTL8367, 88E6393X, 88E6191X, 88E6190, MT7621, MT7531, and EN7523 switch chips (since RouterOS v7) can use bridge VLAN filtering and hardware offloading simultaneously. Other devices cannot utilize the benefits of a built-in switch chip when bridge VLAN filtering is enabled. These devices should be configured according to the method described in the Basic VLAN switching guide. Using an improper configuration method can cause throughput issues in your network.
:::

### Bridge VLAN Table

The Bridge VLAN table defines per-VLAN port membership and specifies the VLAN tag action for egress traffic. Ports configured as `tagged` transmit frames with their corresponding VLAN ID, while ports configured as `untagged` remove the VLAN tag before transmitting frames. Bridge ports with `frame-types` set to `admit-all` or `admit-only-untagged-and-priority-tagged` are automatically added as untagged ports for their configured PVID.

**Sub-menu:** `/interface/bridge/vlan`

| Property | Description |
| :-- | :-- |
| <strong>bridge</strong> (<em>name</em>; Default: <strong>none</strong>) | The bridge interface to which this VLAN entry applies. |
| <strong>disabled</strong> (<em>yes</em> | <em>no</em>; Default: <strong>no</strong>) |
| <strong>tagged</strong> (<em>interface</em>; Default: <strong>none</strong>) | Interfaces or <a href="/docs/system-information-and-utilities/interface-lists">interface list</a> that transmit frames with a VLAN tag. This setting accepts comma-separated values, for example <code>tagged=ether1,ether2</code>. |
| <strong>untagged</strong> (<em>interface</em>; Default: <strong>none</strong>) | Interfaces or <a href="/docs/system-information-and-utilities/interface-lists">interface list</a> that transmit frames without a VLAN tag. This setting accepts comma-separated values, for example <code>untagged=ether3,ether4</code>. |
| <strong>vlan-ids</strong> (<em>integer 1..4094</em>; Default: <strong>1</strong>) | The VLAN ID or list of VLAN IDs for this port configuration. This setting accepts VLAN ID ranges as well as comma-separated values, for example <code>vlan-ids=100-115,120,122,128-130</code>. |

:::danger
The `vlan-ids` parameter can specify a set or range of VLANs, but this should only be used for tagged ports configurations. When multiple VLANs are specified for access ports configurations, tagged packets may be sent as untagged packets through the wrong access port, regardless of the PVID value.
:::

:::warning
Ensure all required interfaces are added to the bridge VLAN table when using bridge VLAN filtering.

For routing functions to work properly on the same device through ports using bridge VLAN filtering, you must allow access to the bridge interface (this includes the switch-cpu port when hardware-offloaded VLAN filtering is used). This can be done manually by adding the bridge interface itself to the VLAN table as a tagged port. Since RouterOS v7.16, this is done automatically when adding a VLAN interface to a bridge with VLAN filtering enabled (a dynamic entry with the comment "added by vlan on bridge" appears under the `/interface/bridge/vlan` menu). Additional examples can be found in the inter-VLAN routing and management access sections.

Since RouterOS 7.20, a dynamic tagged entry named "added by switch-cpu" is added when the same VLAN ID spans multiple switch chips or is used on both hardware and software ports.
:::

:::danger
When allowing access to the CPU, you are permitting access from a specific port to the router/switch itself. This is not always desirable. Ensure you implement proper firewall filter rules to secure your device when CPU access is allowed from a specific VLAN ID and port. Use firewall filter rules to allow access only to required services.
:::

:::warning
Improperly configured bridge VLAN filtering can cause security issues. Ensure you fully understand how the [Bridge VLAN table](/docs/bridging-and-switching/user-guides/bridge-vlan-table) operates before deploying your device in a production environment.
:::

### Bridge Port Settings

Each bridge port has multiple VLAN-related settings that control untagged VLAN membership, VLAN tagging and untagging behavior, and packet filtering based on VLAN tag presence.

**Sub-menu:** `/interface/bridge/port`

| Property | Description |
| :-- | :-- |
| <strong>frame-types</strong> (<em>admit-all</em> | <em>admit-only-untagged-and-priority-tagged</em> |
| <strong>ingress-filtering</strong> (<em>yes</em> | <em>no</em>; Default: <strong>yes</strong>) |
| <strong>pvid</strong> (<em>integer: 1..4094</em>; Default: <strong>1</strong>) | Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. This property only has an effect when <span className="ros-background-accent-green-bolder"><code>vlan-filtering</code></span> is set to <span className="ros-icon-success"><code>yes</code></span>. |
| <strong>tag-stacking</strong> (<em>yes</em> | <em>no</em>; Default: <strong>no</strong>) |

### Bridge host table

The Bridge host table displays MAC addresses that have been learned on a bridge interface. When vlan-filtering is enabled, the table also shows the VLAN ID associated with each learned MAC address, enabling independent VLAN learning (IVL) mode.

```ros
[admin@MikroTik] > /interface/bridge/host/print where !local 
Flags: X - disabled, I - invalid, D - dynamic, L - local, E - external 
 #       MAC-ADDRESS        VID ON-INTERFACE       BRIDGE
0   D   CC:2D:E0:E4:B3:AA  300 ether3             bridge1
1   D   CC:2D:E0:E4:B3:AB  400 ether4             bridge1
```

### VLAN Example: Trunk and Access Ports

This section demonstrates how to configure a basic VLAN setup with one trunk port and multiple access ports. The trunk port (ether2) carries tagged VLAN traffic between switches or to a router, while access ports (ether6, ether7, ether8) connect to end devices and use untagged VLAN traffic.

![access_ports](/img/dcbdce357964f958.webp)

#### Step 1: Create the Bridge Interface

Create a bridge interface with `vlan-filtering` disabled. This is important because enabling VLAN filtering immediately restricts traffic, which could lock you out of the device before the configuration is complete. For detailed information on managing access to the device during VLAN configuration, refer to the [Management access configuration](#management-access-configuration) section.

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
```

#### Step 2: Add Bridge Ports and Configure PVID

Add the physical interfaces to the bridge and configure the Port VLAN ID (pvid) for access ports. The pvid determines which VLAN untagged traffic is assigned to when entering the bridge. The `frame-types` setting controls what kind of traffic each port accepts: tagged only, untagged only, or both.

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether2 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether6 pvid=200 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether7 pvid=300 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether8 pvid=400 frame-types=admit-only-untagged-and-priority-tagged
```

#### Step 3: Create Bridge VLAN Table Entries

Create the bridge VLAN table entries. The trunk port (ether2) must be configured as a tagged member, meaning it will send and receive frames with VLAN tags. Access ports are automatically added as untagged members based on their pvid setting, so you only need to specify the tagged port in each VLAN entry.

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 vlan-ids=200
add bridge=bridge1 tagged=ether2 vlan-ids=300
add bridge=bridge1 tagged=ether2 vlan-ids=400
```

#### Step 4: Enable VLAN Filtering

Once all VLAN settings are configured, enable VLAN filtering on the bridge to activate the VLAN functionality.

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

#### Step 5: (Optional) Reject Untagged Traffic

As an optional security measure, you can set the bridge to reject untagged traffic by changing the frame-type. This prevents the default VLAN 1 (pvid=1) from being used and ensures only properly tagged traffic is accepted.

```ros
/interface/bridge/set bridge1 frame-types=admit-only-vlan-tagged
```

### VLAN Example - Trunk and Hybrid Ports

![hybrid_ports](/img/90b987271e134d95.webp)

Create a bridge with disabled `vlan-filtering` to avoid losing access to the router before VLANs are completely configured. If you need management access to the bridge, see the [Management access configuration](/docs/bridging-and-switching#management-access-configuration) section.

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
```

Add bridge ports and specify `pvid` on hybrid VLAN ports to assign untagged traffic to the intended VLAN.  Use the `frame-types` setting to accept only tagged packets on ether2.

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether2 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether6 pvid=200
add bridge=bridge1 interface=ether7 pvid=300
add bridge=bridge1 interface=ether8 pvid=400
```

Add Bridge VLAN entries and specify tagged ports in them. In this example, egress VLAN tagging is done on ether6, ether7, ether8 ports too, making them into hybrid ports. Bridge ports with `frame-types` set to `admit-all` will be automatically added as untagged ports for the `pvid` VLAN.

```ros
/interface/bridge/vlan 
add bridge=bridge1 tagged=ether2,ether7,ether8 vlan-ids=200
add bridge=bridge1 tagged=ether2,ether6,ether8 vlan-ids=300
add bridge=bridge1 tagged=ether2,ether6,ether7 vlan-ids=400
```

In the end, when VLAN configuration is complete, enable Bridge VLAN Filtering.

```ros
/interface/bridge/set bridge1 vlan-filtering=yes 
```

An Optional step is to set `frame-types=admit-only-vlan-tagged` on the bridge interface in order to disable the default untagged VLAN 1 (`pvid=1`).

```ros
/interface/bridge/set bridge1 frame-types=admit-only-vlan-tagged
```

:::danger
You don't have to add access ports as untagged ports, because they will be added dynamically as untagged ports with the VLAN ID that is specified in `pvid`, you can specify just the trunk port as a tagged port. All ports that have the same `pvid` set will be added as untagged ports in a single entry. You must take into account that the bridge itself is a port and it also has a `pvid` value, this means that the bridge port also will be added as an untagged port for the ports that have the same `pvid`. You can circumvent this behavior by either setting different `pvid` on all ports (even the trunk port and bridge itself), or using `frame-type` set to `accept-only-vlan-tagged`.
:::

### VLAN Example - InterVLAN Routing by Bridge

![vlan_routing](/img/f659d62947a98802.webp)

Create a bridge with disabled `vlan-filtering` to avoid losing access to the router before VLANs are completely configured.  If you need management access to the bridge, see the [Management access configuration](/docs/bridging-and-switching#management-access-configuration) section.

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
```

Add bridge ports and specify `pvid` for VLAN access ports to assign their untagged traffic to the intended VLAN. Use the `frame-types` setting to accept only untagged packets.

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether6 pvid=200 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether7 pvid=300 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether8 pvid=400 frame-types=admit-only-untagged-and-priority-tagged
```

Add Bridge VLAN entries and specify tagged ports in them. In this example **bridge1** interface is the VLAN trunk that will send traffic further to do InterVLAN routing. Bridge ports with `frame-types` set to `admit-only-untagged-and-priority-tagged` will be automatically added as untagged ports for the `pvid` VLAN.

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1 vlan-ids=200
add bridge=bridge1 tagged=bridge1 vlan-ids=300
add bridge=bridge1 tagged=bridge1 vlan-ids=400
```

Configure VLAN interfaces on the **bridge1** to allow handling of tagged VLAN traffic at the routing level and set IP addresses to ensure routing between VLANs as planned.

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

In the end, when VLAN configuration is complete, enable Bridge VLAN Filtering:

```ros
/interface/bridge/set bridge1 vlan-filtering=yes 
```

An optional step is to set `frame-types=admit-only-vlan-tagged` on the bridge interface in order to disable the default untagged VLAN 1 (`pvid=1`).

```ros
/interface/bridge/set bridge1 frame-types=admit-only-vlan-tagged
```

Since RouterOS v7, it is possible to route traffic using L3 HW offloading on certain devices. See more details on [L3 Hardware Offloading](/docs/bridging-and-switching/l3-hardware-offloading).

### Management access configuration

There are multiple ways to set up management access on a device that uses bridge VLAN filtering. Below are some of the most popular approaches to properly enable access to a router/switch. Start by creating a bridge without VLAN filtering enabled:

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
```

#### Untagged Access Without VLAN Filtering

In cases where VLAN filtering is not enabled on the bridge and management access via untagged traffic is required, the configuration is straightforward. The only necessary step is to assign an IP address directly to the bridge interface itself. Since the bridge operates at Layer 2 without VLAN tagging, any untagged traffic entering the bridge ports will be able to communicate with the IP address assigned to the bridge interface without additional configuration.

```ros
/ip/address
add address=192.168.99.1/24 interface=bridge1
```

This approach provides the simplest method for accessing the router or switch for management purposes when VLAN filtering is not part of the network design.

#### Tagged Access Without VLAN Filtering

This method is used when you want to manage the router/switch using tagged VLAN traffic, but without enabling bridge VLAN filtering. In this scenario, a separate VLAN interface is created on top of the bridge to handle the tagged management traffic. This approach is useful when you need to access the device through a specific VLAN ID while keeping the bridge configuration simple and straightforward.

To configure tagged management access, first create a VLAN interface on the bridge with the desired VLAN ID, then assign an IP address to that VLAN interface. This allows the router to be reachable through the tagged VLAN while maintaining the bridge in its default state (without VLAN filtering enabled). The VLAN interface acts as a logical sub-interface that inherits the MAC address from the parent bridge interface.

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

This configuration creates a management VLAN (VLAN 99) on the bridge, making the device accessible at IP address 192.168.99.1 through any port that carries VLAN 99 tagged traffic.

#### Tagged Access with VLAN Filtering

In scenarios where VLAN filtering is enabled on the bridge and management access through tagged traffic is required, additional configuration steps are necessary. This method allows you to reach the router/switch management interface using a specific VLAN ID (VLAN 99 in this example) through tagged traffic on designated ports.

First, create a VLAN interface on top of the bridge and assign an IP address to it. This VLAN interface will handle the tagged management traffic:

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

Next, you must add the appropriate entries to the bridge VLAN table to permit tagged traffic on the ports where management access will be initiated. For instance, if you need to access the device from ports **ether3**, **ether4**, and **sfp-sfpplus1** using VLAN 99 tagged traffic, include the **bridge1** interface itself in the tagged port list (the bridge interface must be tagged to allow the VLAN interface to communicate with the switch CPU):

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,ether3,ether4,sfp-sfpplus1 vlan-ids=99
```

Once the VLAN table is properly configured, you can enable VLAN filtering on the bridge:

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

This configuration enables management access through tagged VLAN 99 traffic while maintaining the security benefits of VLAN filtering. The bridge interface itself is included as a tagged member to ensure proper communication between the VLAN interface and the switch CPU for routing and management purposes.

### Untagged Access with VLAN Filtering

When bridge VLAN filtering is enabled and you need to access the device using untagged traffic, you must ensure that the management VLAN interface uses the same VLAN ID as the untagged port VLAN ID (configured via the `pvid` parameter). This ensures that untagged traffic from access ports can properly communicate with the router's management interface.

First, create a VLAN interface on the bridge and assign an IP address to it, just as you would in the previous example. This VLAN interface will handle the management traffic:

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

For example, if you want untagged ports **ether2** and **ether3** to be able to communicate with the VLAN 99 management interface, these ports must be configured with a `pvid` value that matches the management VLAN ID. Additionally, you need to add the bridge interface itself as a tagged port member in the VLAN table, which allows the router to process the tagged management traffic. You can also add additional tagged ports if needed for your specific network topology (see the previous examples for more details on tagged port configuration):

```ros
/interface/bridge/port
set [find interface=ether2] pvid=99
set [find interface=ether3] pvid=99
/interface/bridge/vlan 
add bridge=bridge1 tagged=bridge1 untagged=ether2,ether3 vlan-ids=99
```

Once you have completed the VLAN table configuration, you can enable VLAN filtering on the bridge. This will activate all VLAN-related functionality and begin filtering traffic based on your VLAN settings:

```ros
/interface/bridge/set bridge1 vlan-filtering=yes 
```

#### Changing untagged VLAN for the bridge interface

In case VLAN filtering is used, it is possible to change the untagged VLAN ID for the bridge interface using the `pvid` setting. Note that creating routable VLAN interfaces and allowing tagged traffic on the bridge is a more flexible and generally recommended option.

First, create an IP address on the bridge interface.

```ros
/ip/address
add address=192.168.99.1/24 interface=bridge1
```

For example, untagged **bridge1** traffic should be able to communicate with untagged **ether2** and **ether3** ports and tagged **sfp-sfpplus1** port in VLAN 99. In order to achieve this, **bridge1**, **ether2**, **ether3** should be configured with the same `pvid` and sfp-sfpplus1 should be added as a tagged member.

```ros
/interface/bridge
set [find name=bridge1] pvid=99
/interface/bridge/port
set [find interface=ether2] pvid=99
set [find interface=ether3] pvid=99
/interface/bridge/vlan
add bridge=bridge1 tagged=sfp-sfpplus1 untagged=bridge1,ether2,ether3 vlan-ids=99
```

After that you can enable VLAN filtering:

```ros
/interface/bridge/set bridge1 vlan-filtering=yes 
```

:::warning
If the connection to the router/switch through an IP address is not required, then steps for adding an IP address can be skipped since a connection to the router/switch through Layer2 protocols (e.g. MAC-telnet) will be working either way.
:::

### VLAN Tunneling (QinQ)

Since RouterOS v6.43 the RouterOS bridge is IEEE 802.1ad compliant and it is possible to filter VLAN IDs based on Service VLAN ID (0x88a8) rather than Customer VLAN ID (0x8100). The same principles can be applied as with IEEE 802.1Q VLAN filtering (the same setup examples can be used). Below is a topology for a common **Provider bridge**:

![Provider_bridge](/img/0285416b3135c6c9.webp)

In this example, **R1**, **R2**, **R3,** and **R4** might be sending any VLAN tagged traffic by 802.1Q (CVID), but **SW1** and **SW2** need to isolate traffic between routers in a way that **R1** is able to communicate only with **R3**, and **R2** is only able to communicate with **R4**. To do so, you can tag all ingress traffic with an SVID and only allow these VLANs on certain ports. Start by enabling the service tag 0x88a8, introduced by `802.1ad`, on the bridge. Use these commands on **SW1** and **SW2**:

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no ether-type=0x88a8
```

In this setup, **ether1** and **ether2** are going to be access ports (untagged), use the `pvid` parameter to tag all ingress traffic on each port, use these commands on **SW1** and **SW2**:

```ros
/interface/bridge/port
add interface=ether1 bridge=bridge1 pvid=200
add interface=ether2 bridge=bridge1 pvid=300
add interface=ether3 bridge=bridge1
```

Specify tagged and untagged ports in the bridge VLAN table. Use these commands on **SW1** and **SW2**:

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether3 untagged=ether1 vlan-ids=200
add bridge=bridge1 tagged=ether3 untagged=ether2 vlan-ids=300
```

When the bridge VLAN table is configured, you can enable bridge VLAN filtering. Use these commands on **SW1** and **SW2:**

```ros
/interface/bridge/set bridge1 vlan-filtering=yes 
```

:::danger
By enabling vlan-filtering you will be filtering out traffic destined to the CPU. Before enabling VLAN filtering you should make sure that you set up a Management port.

Note that if you are using the new EtherType/TPID 0x88a8 (service tag) and you also need a VLAN interface for your Service VLAN, you will also have to apply the `use-service-tag` parameter on the VLAN interface.
:::

:::danger
When `ether-type=0x8100` is configured, the bridge checks the outer VLAN tag to see if it is using EtherType `0x8100`. If the bridge receives a packet with an outer tag that has a different EtherType, it will mark the packet as `untagged`. Since RouterOS only checks the outer tag of a packet, it is not possible to filter 802.1Q packets when the 802.1ad protocol is used.
:::

:::warning
Currently, only MikroTik devices with Marvell Prestera switch are capable of hardware offloaded VLAN filtering using the Service tag, EtherType/TPID `0x88a8`.
:::

:::danger
Devices with switch chip Marvell-98DX3257 (e.g. CRS354 series) do not support VLAN filtering on 1Gbps Ethernet interfaces for other VLAN types (`0x88a8` and `0x9100`).
:::

### Tag stacking

Since RouterOS v6.43 it is possible to forcefully add a new VLAN tag over any existing VLAN tags. This feature can be used to achieve a CVID stacking setup, where a CVID (0x8100) tag is added before an existing CVID tag. This type of setup is very similar to the Provider bridge setup. To achieve the same setup but with multiple CVID tags (CVID stacking) we can use the same topology:

![Tag_stacking](/img/ed256f307c0776d1.webp)

In this example **R1**, **R2**, **R3,** and **R4** might be sending any VLAN tagged traffic, it can be 802.1ad, 802.1Q or any other type of traffic, but **SW1** and **SW2** need to isolate traffic between routers in a way that **R1** is able to communicate only with **R3**, and **R2** is only able to communicate with **R4**. To do so, you can tag all ingress traffic with a new CVID tag and only allow these VLANs on certain ports. Start by selecting the proper EtherType, use these commands on **SW1** and **SW2**:

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no ether-type=0x8100
```

In this setup, **ether1** and **ether2** will ignore any VLAN tags that are present and add a new VLAN tag. Use the `pvid` parameter to tag all ingress traffic on each port and allow `tag-stacking` on these ports. Use these commands on **SW1** and **SW2**:

```ros
/interface/bridge/port
add interface=ether1 bridge=bridge1 pvid=200 tag-stacking=yes
add interface=ether2 bridge=bridge1 pvid=300 tag-stacking=yes
add interface=ether3 bridge=bridge1
```

Specify tagged and untagged ports in the bridge VLAN table. You only need to specify the VLAN ID of the outer tag. Use these commands on **SW1** and **SW2**:

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether3 untagged=ether1 vlan-ids=200
add bridge=bridge1 tagged=ether3 untagged=ether2 vlan-ids=300
```

When the bridge VLAN table is configured, you can enable bridge VLAN filtering, which is required in order for the pvid parameter to have any effect. Use these commands on **SW1** and **SW2:**

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

:::danger
By enabling vlan-filtering you will be filtering out traffic destined to the CPU; before enabling VLAN filtering you should make sure that you set up a Management port.
:::

### MVRP

Multiple VLAN Registration Protocol (MVRP) is a protocol based on Multiple Registration Protocol (MRP) which allows registering attributes (VLAN IDs in the case of MVRP) with other members of a Bridged LAN.

An MRP application can make or withdraw declarations of attributes which result in registration or leaving of those attributes with other MRP participants.

Here's how it works.

MRP consists of two parts:

- **Applicant** - responsible for sending declarations (or leaves). Its behavior can be configured on a per-port basis using the setting called `mvrp-applicant-state`, and per-VLAN using the `mvrp-forbidden` setting.
- **Registrar** - responsible for registering incoming declarations. Its configuration can be set per-port using the `mvrp-registrar-state` setting, and per-VLAN using the `mvrp-forbidden` setting.

**Registration Propagation:** Incoming registration on a bridge port dynamically makes that specific port a tagged VLAN member. Additionally, the attributes associated with this registration are spread to all active (forwarding) bridge ports as a declaration.

**Declaration Operation:** In case of MVRP, the configured VLANs get declared on each port, but they will only get configured as members of those VLANs when a declaration is received from the LAN (Registrar will register the VLAN). From the perspective of an end-station, a single declaration will be registered on each upstream port across the entire LAN. When another end-station declares the same attribute, a path of registrations will be made between the two (or more) end stations, see the picture below.

MVRP helps to dynamically propagate VLAN information throughout the bridged network and configure VLANs only on the needed ports. This makes the network efficient by avoiding unnecessary traffic flooding.

As noted before, MVRP is only active on ports that are forwarding. In the case of MSTP, declarations and registrations are made only if the port is forwarding in the MSTI in which the VLAN is mapped.

The point-to-point ports speed up the process of registration (or leaving). Manually configuring `point-to-point=yes` can be advantageous for non-Ethernet interfaces.

![MVRP](/img/33d81c5bbb103a21.webp)

#### Property Reference

**Sub-menu:** `/interface/bridge`

| Property | Description |
| :-- | :-- |
| **mvrp** (*yes* \| *no*; Default: **no**) | Enables MVRP for bridge. It ensures that the MAC address 01:80:C2:00:00:21 is trapped and not forwarded. The `vlan-filtering` must be enabled. |

**Sub-menu:** `/interface/bridge/port`

The port menu enables control over the applicant and registrar settings on a per-port basis.

| Property | Description |
| :-- | :-- |
| **mvrp-applicant-state** (*non-participant \| normal-participant;* Default: **normal-participant**) | MVRP applicant options: <br/><ul><li><strong>non-participant</strong> - port does not send any MRP messages;</li><li><strong>normal-participant </strong>- port participates normally in MRP exchanges.</li></ul> |
| **mvrp-registrar-state** (*fixed \| normal*; Default: **normal**) | MVRP registrar options: <br/><ul><li><strong>fixed</strong> - port ignores all MRP messages, and remains Registered (IN) in all configured vlans.</li><li><strong>normal </strong>- port receives MRP messages and handles them according to the standard.</li></ul> |

To monitor the currently declared and registered VLAN IDs, use the `monitor` command.

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

**Sub-menu:** `/interface/bridge/vlan`

All ports that are members of static VLANs or dynamic untagged VLANs created by the port `pvid` setting are treated as "fixed." This means the registrar disregards all MRP messages and remains registered (IN) for those VLANs.

When a VLAN is neither manually configured nor created by the port `pvid` setting, incoming registrations on a bridge port can dynamically designate that specific port as a tagged VLAN member. The `mvrp-forbidden` feature allows creating a list of ports that are restricted from registering for a specific VLAN ID.

VLANs that are static or dynamic will be declared by the applicants unless this functionality is disabled by the port's `mvrp-applicant-state`, or by the VLAN's `mvrp-forbidden` setting.

| Property | Description |
| :-- | :-- |
| **mvrp-forbidden** (*interfaces*; Default: ) | Ports that ignore all MRP messages and remain Not Registered (MT), as well as disable applicant from declaring specific VLAN ID. |

**Sub-menu:** `/interface/bridge/vlan/mvrp`

The MVRP attributes menu can be used to see internal MVRP attribute states, as specified in the IEEE 802.1Q-2011.

| Property | Description |
| :-- | :-- |
| **applicant-state** | The Applicant state machine that declares attributes. Its state can be VO, VP, VN, AN, AA, QA, LA, AO, QO, AP, QP, or LO. Each state consists of two letters. <br/> The first letter indicates the state: <br/><ul><li>V—Very anxious;</li><li>A—Anxious;</li><li>Q—Quiet;</li><li>L—Leaving.</li></ul> The second letter indicates the membership state: <br/><ul><li>A - Active member;</li><li>P - Passive member;</li><li>O - Observer;</li><li>N - New.</li></ul> For example, VP indicates "Very anxious, Passive member." |
| **registrar-state** | The Registrar state machine that records the registration state of attributes declared by other participants. Its state can be IN, LV, or MT: <br/><ul><li>IN—Registered;</li><li>LV—Previously registered, but now being timed out;</li><li>MT—Not registered.</li></ul> |

```ros
[admin@Mikrotik] /interface/bridge/vlan/mvrp/print where vlan-id=10
Columns: BRIDGE, PORT, VLAN-ID, REGISTRAR-STATE, APPLICANT-STATE, LAST-EVENT
 #  BRIDGE    PORT           VLAN-ID  REGISTRAR-STATE  APPLICANT-STATE  LAST-EVENT
 1  bridge67  sfp-sfpplus1        10  IN               Quiet Active     JoinIn    
 9  bridge67  sfp-sfpplus5        10  MT               Quiet Active     JoinEmpty 
17  bridge67  sfp-sfpplus9        10  MT               Quiet Active     JoinEmpty 
25  bridge67  sfp-sfpplus13       10  IN               Quiet Active     JoinIn 
```

## Fast Forward

---

Fast Forward allows forwarding packets faster under special conditions. When Fast Forward is enabled, then the bridge can process packets even faster since it can skip multiple bridge-related checks, including MAC learning. Below you can find a list of conditions that **MUST** be met in order for Fast Forward to be active:

- Bridge has `fast-forward` set to `yes`.
- Bridge has only 2 running ports.
- Both bridge ports support [Fast Path](/docs/firewall-and-quality-of-service/packet-flow-in-routeros#fast-path), Fast Path is active on ports and globally on the bridge.
- Bridge Hardware Offloading is disabled.
- Bridge VLAN Filtering is disabled.
- Bridge DHCP snooping is disabled.
- `unknown-multicast-flood` is set to `yes`.
- `unknown-unicast-flood` is set to `yes`.
- `broadcast-flood` is set to `yes`.
- MAC address for the bridge matches a MAC address from one of the bridge slave ports.
- `horizon` for both ports is set to `none`.

:::warning
Fast Forward disables MAC learning; this is by design to achieve faster packet forwarding. MAC learning prevents traffic from flooding multiple interfaces, but MAC learning is not needed when a packet can only be sent out through just one interface.
:::

:::danger
Fast Forward is disabled when hardware offloading is enabled. Hardware offloading can achieve full wire-speed performance when it is active since it will use the built-in switch chip (if such exists on your device). Fast forward uses the CPU to forward packets. When comparing throughput results, you would get such results: Hardware offloading > Fast Forward > Fast Path > Slow Path.
:::

It is possible to check how many packets were processed by Fast Forward:

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
If packets are processed by Fast Path, then Fast Forward is not active. Packet count can be used as an indicator of whether Fast Forward is active or not.
:::

Since RouterOS 6.44 it is possible to monitor Fast Forward status, for example:

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
Disabling or enabling fast-forward will temporarily disable all bridge ports for settings to take effect. This must be taken into account whenever changing this property in production environments since it can cause all packets to be temporarily dropped.
:::

## IGMP/MLD Snooping

---

The bridge supports IGMP/MLD snooping. It controls multicast streams and prevents multicast flooding on unnecessary ports. Its settings are placed in the bridge menu and it works independently on every bridge interface. Software-driven implementation works on all devices with RouterOS, but MikroTik devices with Marvell Prestera switch, and 88E6393X, 88E6191X, 88E6190 switch chips also support IGMP/MLD snooping with hardware offloading. See more details on [IGMP/MLD snooping manual](/docs/bridging-and-switching/user-guides/bridge-igmp-mld-snooping).

## DHCP Snooping and DHCP Option 82

---

DHCP Snooping and DHCP Option 82 are supported by bridge. The DHCP Snooping is a Layer2 security feature that prevents unauthorized DHCP servers from providing malicious information to users. In RouterOS, you can specify which bridge ports are trusted (where a known DHCP server resides and DHCP messages should be forwarded) and which are untrusted (usually used for access ports, received DHCP server messages will be dropped). The DHCP Option 82 is additional information (Agent Circuit ID and Agent Remote ID) provided by DHCP Snooping enabled devices that allows identifying the device itself and DHCP clients.

![Dhcp_snooping](/img/1e3b5abc626baf0c.webp)

In this example, SW1 and SW2 are DHCP Snooping and Option 82-enabled devices. First, we need to create a bridge, assign interfaces and mark trusted ports. Use these commands on **SW1**:

```ros
/interface/bridge
add name=bridge
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2 trusted=yes
```

For SW2, the configuration will be similar, but we also need to mark ether1 as trusted, because this interface is going to receive DHCP messages with Option 82 already added. You need to mark all ports as trusted if they are going to receive DHCP messages with added Option 82, otherwise these messages will be dropped. Also, we add ether3 to the same bridge and leave this port untrusted, imagining there is an unauthorized (rogue) DHCP server. Use these commands on **SW2**:

```ros
/interface/bridge
add name=bridge
/interface/bridge/port
add bridge=bridge interface=ether1 trusted=yes
add bridge=bridge interface=ether2 trusted=yes
add bridge=bridge interface=ether3
```

Then we need to enable DHCP Snooping and configure Option 82. Starting from RouterOS version 7.23, it is possible to configure custom Remote ID and Circuit ID values using predefined variables (such as BRIDGEMAC, HOSTNAME, INTERFACE, VID). See the `dhcp-agent-circuit-id`, `dhcp-agent-remote-id` properties for more details. In case your DHCP server does not support DHCP Option 82 or you do not implement any Option 82-related policies, this step is not mandatory. In this configuration example, we are using these commands on **SW1** and **SW2**:

```ros
/interface/bridge
set [find where name="bridge"] dhcp-snooping=yes dhcp-agent-circuit-id="interface: \$(INTERFACE), vlan: \$(VID)" dhcp-agent-remote-id="ip: 192.168.88.1, identity: \$(HOSTNAME), mac: \$(BRIDGEMAC)"
```

Now both devices will analyze what DHCP messages are received on bridge ports. The **SW1** is responsible for adding and removing the DHCP Option 82. The **SW2** will limit rogue DHCP servers from receiving any discovery messages and drop malicious DHCP server messages from ether3.

:::warning
Currently, MikroTik devices with Marvell Prestera switch and 88E6393X, 88E6191X, 88E6190 switch chips fully support hardware offloaded DHCP Snooping and Option 82. For CRS1xx and CRS2xx series switches, it is possible to use DHCP Snooping along with VLAN switching, but then you need to make sure that DHCP packets are sent out with the correct VLAN tag using egress ACL rules. Other devices are capable of using DHCP Snooping and Option 82 features along with hardware offloading, but you must make sure that there is no VLAN-related configuration applied to the device, otherwise, DHCP Snooping and Option 82 might not work properly. See the Bridge Hardware Offloading section with supported features.
:::

:::info
Starting from RouterOS v7.17, DHCP snooping is supported with hardware offloading on bonding interfaces.
:::

### DHCP Snooping Binding Table

The DHCP snooping binding database is a runtime table generated by a bridge and intended to store DHCP leases provided by DHCP servers connected to trusted ports. Each entry records the client’s MAC address, assigned IP address, lease expiration time, VLAN ID, and the physical interface on which the client was seen. The bridge can utilize this database to enhance security. Namely, when a frame arrives on an untrusted port, the switch verifies that the source MAC/IP pair matches a stored binding before forwarding the packet, thereby blocking traffic from rogue DHCP servers or spoofed hosts, preventing address‑theft attacks, and enabling features such as IP‑Source‑Guard, ARP‑Inspection.

The present implementation of the DHCPv4 snooping binding table has been built on top of the existing `/interface/bridge/host` table. The relevant DHCP information is retrieved from DHCP messages traversing the bridge.

:::danger
The DHCP-related information collected by the bridge and summarized in the binding table is lost each time the bridge or just the DHCP snooping is disabled.
:::

The current status of the DHCP client is indicated by the `dhcpv4-status`. The possible status values are as follows: `searching`, `requesting`, `bound`, `renewing`, `rebinding`, `expired`, and `relay-agent`. The last one can appear only when a DHCP request message is received from a DHCP client hiding behind a relay agent.

The `dhcpv4-ip` shows the IP addresses granted by DHCP servers, while the `dhcpv4-server-id` column indicates the server ID. The `dhcpv4-expires-after` column shows the time left till the end of the current lease period provided by the DHCP server to a client.

When VLAN filtering is enabled on the bridge each host is identified not only by its MAC address, but by a pair MAC - VLAN ID.

The active DHCP binding table entries in Winbox:

![FDB with DHCP binding table in Winbox](/img/a51a51d564206202.png)

The active DHCP binding table entries in console:

![FDB with DHCP binding table in console](/img/509a91e9576f9771.png)

## DHCPv6 Snooping / DHCPv6 Shield

DHCPv6 Snooping is a Layer2 security feature that prevents unauthorized DHCPv6 servers from providing malicious information to users. In RouterOS, you can specify which bridge ports are trusted (where the known DHCPv6 server resides and DHCPv6 messages should be forwarded) and which are untrusted (usually used for access ports, received DHCPv6 server messages will be dropped, effectively implementing DHCPv6-Shield).

The DHCPv6 Option 18 (Interface-Id) and Option 37 (Remote-Id) are additional information provided by DHCPv6 Snooping enabled devices that allow identifying the device itself and DHCPv6 clients.

IPv6 allows a more granular approach as well as flexibility with the DHCPv6 Relay agent process. Functionally, these serve the exact same purpose as IPv4's Option 82: Option 18 acts as the Circuit ID (identifying the specific port/VLAN the client is attached to), and Option 37 acts as the Remote ID (identifying the relay agent or switch hardware itself).

- Option 18 - identifies the specific interface (port) on which the client's message was received. It ensures the server knows exactly where the request came through so it can apply the correct policy.
- Option 37 - identifies the relay agent (the switch or router) itself. It contains a unique caller ID (like the DUID—DHCP Unique Identifier). It tells the server which specific device in the network is talking to it.

## RA Guard

---

The RA guard feature is intended for discarding IPv6 packets containing router advertisement (RA) messages arriving on bridge ports specified by the user as untrusted ones, thereby allowing one to prevent potential rogue RA message-based attacks or accidental network misconfiguration. When enabled, it is possible to set each bridge port either as trusted or untrusted (by default all the bridge ports are set as RA untrusted).

Here are the network scheme and core principle behind IPv6 RA Guard (Router Advertisement Guard).

![RAguard](/img/0db2c93dce1fec4d.webp)

|  |
| :-- |
| <br/><code>#Layer 2 Access Switch - enabling RA guard on the main bridge</code><br/><code>/interface/bridge</code><br/><code>add name=bridge</code><br/><code>/interface/bridge</code><br/><code>set [find where name="bridge"] ra-guard=yes</code><br/><code>/interface/bridge/port</code><br/><code>add bridge=bridge interface=etherUplink Trusted RA=yes</code><br/><code>add bridge=bridge interface=etherX</code><br/><code>add bridge=bridge interface=etherY</code><br/><code>add bridge=bridge interface=etherZ</code><br/> |

### The Problem: Why is this needed?

In IPv6, devices use ICMPv6 to auto-configure themselves.

Router Advertisements (Type 134): Routers broadcast these messages to tell hosts: "I am the gateway, and here is your network prefix."

The Threat: If a user accidentally connects a consumer router (like a home Wi-Fi router) or a malicious actor launches a tool (like `Rogue RA`) on an access port, that device will start broadcasting RAs.

The Result: Other hosts on the network will auto-configure their IPv6 addresses based on the rogue device and set the rogue device as their default gateway. This causes a Man-in-the-Middle attack or a complete denial of service.

Here is the network scheme and the core principle behind IPv6 RA Guard (Router Advertisement Guard).

### The Core Principle: "Trust vs. Untrust"

The fundamental principle of IPv6 RA Guard is logically identical to DHCP Snooping in IPv4. It creates a security boundary within the Layer 2 switch infrastructure by categorizing switch ports into two roles:

- Trusted Ports: Ports connected to legitimate, authorized IPv6 routers. These ports are allowed to send Router Advertisement (RA) packets.
- Untrusted Ports: Ports connected to end-user hosts. These ports are blocked from sending RA packets.

### Packet parsing process

For ports not configured as RA Trusted, the RA Guard parser traverses the extension header chain until it encounters a non-extension header. The parsing process and subsequent actions are governed by the following rules:

**Transport Layer Termination**: If the parser encounters a valid transport layer header—such as TCP, UDP, ESP, RSVP, or an encapsulated IPv4/IPv6 header—parsing terminates and the packet is forwarded (subject to standard bridge checks).

- Drop Conditions - The packet is discarded if:

1. It fails to contain a transport layer header.
2. The final extension header in the chain does not specify NO\_NEXT\_HEADER (59) in its "Next Header" field.
3. If the ICMP message type is found to be 134, the packet is dropped.

- Fragmentation Handling: These parsing rules apply exclusively to the first fragment of fragmented IPv6 packets. Subsequent fragments are forwarded regardless of their content, as they do not contain the protocol headers necessary for RA identification.

## Bridge Firewall

---

The bridge firewall implements packet filtering and thereby provides security functions that are used to manage data flow to, from, and through the bridge.

[Packet flow diagram](/docs/firewall-and-quality-of-service/packet-flow-in-routeros) shows how packets are processed through the router. It is possible to force bridge traffic to go through `/ip/firewall/filter` rules (see the bridge settings).

There are two bridge firewall tables:

- **filter** - bridge firewall with three predefined chains:
  - **input** - filters packets, where the destination is the bridge (including those packets that will be routed, as they are destined to the bridge MAC address anyway).
  - **output** - filters packets, which come from the bridge (including those packets that have been routed normally).
  - **forward** - filters packets, which are to be bridged (note: this chain is not applied to the packets that should be routed through the router, just to those that are traversing between the ports of the same bridge).
- **nat** - bridge network address translation provides ways for changing source/destination MAC addresses of the packets traversing a bridge. Has two built-in chains:
  - **srcnat** - used for "hiding" a host or a network behind a different MAC address. This chain is applied to the packets leaving the router through a bridged interface.
  - **dstnat** - used for redirecting some packets to other destinations.

You can put packet marks in the bridge firewall (filter and NAT), which are the same as the packet marks in the IP firewall configured by `'/ip/firewall/mangle'`. In this way, packet marks put by the bridge firewall can be used in the 'IP firewall', and vice versa.

General bridge firewall properties are described in this section. Some parameters that differ between nat and filter rules are described in further sections.

**Sub-menu:** `/interface/bridge/filter, /interface/bridge/nat`

| Property | Description |
| :-- | :-- |
| **802.3-sap** (*integer*; Default: ) | DSAP (Destination Service Access Point) and SSAP (Source Service Access Point) are 2 one-byte fields, which identify the network protocol entities which use the link-layer service. These bytes are always equal. Two hexadecimal digits may be specified here to match an SAP byte. |
| **802.3-type** (*integer*; Default: ) | Ethernet protocol type, placed after the IEEE 802.2 frame header. Works only if 802.3-sap is 0xAA (SNAP - Sub-Network Attachment Point header). For example, AppleTalk can be indicated by the SAP code of 0xAA followed by a SNAP type code of 0x809B. |
| **action** (*accept \| drop \| jump \| log \| mark-packet \| passthrough \| return \| set-priority*; Default: ) | Action to take if the packet is matched by the rule:<ul><li>accept - accept the packet. The packet is not passed to the next firewall rule</li><li>drop - silently drop the packet</li><li>jump - jump to the user-defined chain specified by the value of <span className="ros-icon-success"><code>jump-target</code></span> parameter</li><li>log - add a message to the system log containing the following data: in-interface, out-interface, src-mac, protocol, src-ip:port-&gt;dst-ip:port and length of the packet. After the packet is matched it is passed to the next rule in the list, similar as <span className="ros-icon-success"><code>passthrough</code></span></li><li>mark-packet - place a mark specified by the new-packet-mark parameter on a packet that matches the rule</li><li>passthrough - if the packet is matched by the rule, increase counter and go to next rule (useful for statistics)</li><li>return - passes control back to the chain from where the jump took place</li><li>set-priority - set priority specified by the new-priority parameter on the packets sent out through a link that is capable of transporting priority (VLAN or WMM-enabled wireless interface). <a href="/docs/bridging-and-switching/user-guides/wmm-and-vlan-priority" rel="nofollow">Read more</a></li></ul> |
| **arp-dst-address** (*IP address*; Default: ) | ARP destination IP address. |
| **arp-dst-mac-address** (*MAC address*; Default: ) | ARP destination MAC address. |
| **arp-gratuitous** (*yes \| no*; Default: ) | Matches ARP gratuitous packets. |
| **arp-hardware-type** (*integer*; Default: **1**) | ARP hardware type. This is normally Ethernet (Type 1). |
| **arp-opcode** (*arp-nak \| drarp-error \| drarp-reply \| drarp-request \| inarp-reply \| inarp-request \| reply \| reply-reverse \| request \| request-reverse*; Default: ) | ARP opcode (packet type)<ul><li>arp-nak - negative ARP reply (rarely used, mostly in ATM networks)</li><li>drarp-error - Dynamic RARP error code, saying that an IP address for the given MAC address can not be allocated</li><li>drarp-reply - Dynamic RARP reply, with a temporary IP address assignment for a host</li><li>drarp-request - Dynamic RARP request to assign a temporary IP address for the given MAC address</li><li>inarp-reply - InverseARP Reply</li><li>inarp-request - InverseARP Request</li><li>reply - standard ARP reply with a MAC address</li><li>reply-reverse - reverse ARP (RARP) reply with an IP address assigned</li><li>request - standard ARP request to a known IP address to find out unknown MAC address</li><li>request-reverse - reverse ARP (RARP) request to a known MAC address to find out the unknown IP address (intended to be used by hosts to find out their own IP address, similarly to DHCP service)</li></ul> |
| **arp-packet-type** (*integer 0..65535 \| hex 0x0000-0xffff*; Default: ) | ARP Packet Type. |
| **arp-src-address** (*IP address*; Default: ) | ARP source IP address. |
| **arp-src-mac-address** (*MAC addres*; Default: ) | ARP source MAC address. |
| **chain** (*text*; Default: ) | Bridge firewall chain, which the filter is functioning in (either a built-in one, or a user-defined one). |
| **dst-address** (*IP address*; Default: ) | Destination IP address (only if MAC protocol is set to IP). |
| **dst-address6** (*IPv6 address*; Default: ) | Destination IPv6 address (only if MAC protocol is set to IPv6). |
| **dst-mac-address** (*MAC address*; Default: ) | Destination MAC address. |
| **dst-port** (*integer 0..65535*; Default: ) | Destination port number or range (only for TCP or UDP protocols). |
| **in-bridge** (*name*; Default: ) | Bridge interface through which the packet is coming in. |
| **in-bridge-list** (*name*; Default: ) | Set of bridge interfaces defined in interface list. Works the same as `in-bridge`. |
| **in-interface** (*name*; Default: ) | Physical interface (i.e., bridge port) through which the packet is coming in. |
| **in-interface-list** (*name*; Default: ) | Set of interfaces defined in interface list. Works the same as `in-interface`. |
| **ingress-priority** (*integer 0..63*; Default: ) | Matches the priority of an ingress packet. Priority may be derived from VLAN, WMM, DSCP or MPLS EXP bit. [read more](/docs/bridging-and-switching/user-guides/wmm-and-vlan-priority) |
| **ip-protocol** (*dccp \| ddp \| egp \| encap \| etherip \| ggp \| gre \| hmp \| icmp \| icmpv6 \| idpr-cmtp \| igmp \| ipencap \| ipip \| ipsec-ah \| ipsec-esp \| ipv6 \| ipv6-frag \| ipv6-nonxt \| ipv6-opts \| ipv6-route \| iso-tp4 \| l2tp \| ospf \| pim \| pup \| rdp \| rspf \| rsvp \| sctp \| st \| tcp \| udp \| udp-lite \| vmtp \| vrrp \| xns-idp \| xtp*; Default: ) | IP protocol (only if MAC protocol is set to IPv4)<ul><li>dccp - Datagram Congestion Control Protocol</li><li>ddp - Datagram Delivery Protocol</li><li>egp - Exterior Gateway Protocol</li><li>encap - Encapsulation Header</li><li>etherip - Ethernet-within-IP Encapsulation</li><li>ggp - Gateway-to-Gateway Protocol</li><li>gre - Generic Routing Encapsulation</li><li>hmp - Host Monitoring Protocol</li><li>icmp - IPv4 Internet Control Message Protocol</li><li>icmpv6 - IPv6 Internet Control Message Protocol</li><li>idpr-cmtp - Inter-Domain Policy Routing Control Message Transport Protocol</li><li>igmp - Internet Group Management Protocol</li><li>ipencap - IP in IP (encapsulation)</li><li>ipip - IP-within-IP Encapsulation Protocol</li><li>ipsec-ah - IPsec Authentication Header</li><li>ipsec-esp - IPsec Encapsulating Security Payload</li><li>ipv6 - Internet Protocol version 6</li><li>ipv6-frag - Fragment Header for IPv6</li><li>ipv6-nonxt - No Next Header for IPv6</li><li>ipv6-opts - Destination Options for IPv6</li><li>ipv6-route - Routing Header for IPv6</li><li>iso-tp4 - ISO Transport Protocol Class 4</li><li>l2tp - Layer Two Tunneling Protocol</li><li>ospf - Open Shortest Path First</li><li>pim - Protocol Independent Multicast</li><li>pup - PARC Universal Packet</li><li>rdp - Reliable Data Protocol</li><li>rspf - Radio Shortest Path First</li><li>rsvp - Reservation Protocol</li><li>sctp - Stream Control Transmission Protocol</li><li>st - Internet Stream Protocol</li><li>tcp - Transmission Control Protocol</li><li>udp - User Datagram Protocol</li><li>udp-lite - Lightweight User Datagram Protocol</li><li>vmtp - Versatile Message Transaction Protocol</li><li>vrrp - Virtual Router Redundancy Protocol</li><li>xns-idp - Xerox Network Systems Internet Datagram Protocol</li><li>xtp - Xpress Transport Protocol</li></ul> |
| **jump-target** (*name*; Default: ) | If `action=jump` specified, then specifies the user-defined firewall chain to process the packet. |
| **limit** (*integer/time,integer*; Default: ) | Matches packets up to a limited rate. A rule using this matcher will match until this limit is reached. <ul><li>count - maximum average packet rate, measured in packets per second (pps), unless followed by Time option</li><li>time - specifies the time interval over which the packet rate is measured</li><li>burst - number of packets to match in a burst</li></ul> |
| **log**(*yes \| no; Default:***no**) | Add a message to the system log containing the following data: in-interface, out-interface, src-mac, dst-mac, eth-protocol, ip-protocol, src-ip:port->dst-ip:port, and length of the packet. |
| **log-prefix** (*text*; Default: ) | Defines the prefix to be printed before the logging information. |
| **mac-protocol** (*802.2 \| arp \| capsman \| dot1x \| homeplug-av \| ip \| ipv6 \| ipx \| lacp \| length \| lldp \| loop-protect \| macsec \| mpls-multicast \| mpls-unicast \| mvrp \| packing-compr \| packing-simple \| pppoe \| pppoe-discovery \| rarp \| romon \| service-vlan \| vlan \| integer 0..65535 \| hex 0x0000-0xffff*; Default: ) | Ethernet payload type (MAC-level protocol). To match protocol type for VLAN encapsulated frames (0x8100 or 0x88a8), a vlan-encap property should be used.<ul><li>802.2 - 802.2 Frames (0x0004)</li><li>arp - Address Resolution Protocol (0x0806)</li><li>homeplug-av - HomePlug AV MME (0x88E1)</li><li>ip - Internet Protocol version 4 (0x0800)</li><li>ipv6 - Internet Protocol Version 6 (0x86DD)</li><li>ipx - Internetwork Packet Exchange (0x8137)</li><li>length - Packets with length field (0x0000-0x05DC)</li><li>lldp - Link Layer Discovery Protocol (0x88CC)</li><li>loop-protect - Loop Protect Protocol (0x9003)</li><li>mpls-multicast - MPLS multicast (0x8848)</li><li>mpls-unicast - MPLS unicast (0x8847)</li><li>mvrp - Multiple VLAN Registration protocol (0x88F5)</li><li>packing-compr - Encapsulated packets with compressed <a href="/docs/system-information-and-utilities/ip-packing">IP packing</a> (0x9001)</li><li>packing-simple - Encapsulated packets with simple <a href="/docs/system-information-and-utilities/ip-packing">IP packing</a> (0x9000)</li><li>pppoe - PPPoE Session Stage (0x8864)</li><li>pppoe-discovery - PPPoE Discovery Stage (0x8863)</li><li>rarp - Reverse Address Resolution Protocol (0x8035)</li><li>service-vlan - Provider Bridging (IEEE 802.1ad) &amp; Shortest Path Bridging IEEE 802.1aq (0x88A8)</li><li>vlan - VLAN-tagged frame (IEEE 802.1Q) and Shortest Path Bridging IEEE 802.1aq with NNI compatibility (0x8100)</li></ul> |
| **new-packet-mark** (*string*; Default: ) | Sets a new packet-mark value. |
| **new-priority** (*integer \| from-ingress*; Default: ) | Sets a new priority for a packet. This can be the VLAN, WMM or MPLS EXP priority [Read more](/docs/bridging-and-switching/user-guides/wmm-and-vlan-priority). This property can also be used to set an internal priori |
| **out-bridge** (*name*; Default: ) | Outgoing bridge interface. |
| **out-bridge-list** (*name*; Default: ) | Set of bridge interfaces defined in interface list. Works the same as `out-bridge`. |
| **out-interface** (*name*; Default: ) | Interface that the packet is leaving the bridge through. |
| **out-interface-list** (*name*; Default: ) | Set of interfaces defined in [interface list](/docs/getting-started/configuration-management/list-of-menus-with-sensitive-parameters). Works the same as `out-interface`. |
| **packet-mark** (*name*; Default: ) | Match packets with a certain packet mark. |
| **packet-type** (*broadcast \| host \| multicast \| other-host*; Default: ) | MAC frame type:<ul><li>broadcast - broadcast MAC packet</li><li>host - packet is destined to the bridge itself</li><li>multicast - multicast MAC packet</li><li>other-host - packet is destined to some other unicast address, not to the bridge itself</li></ul> |
| **src-address** (*IP address*; Default: ) | Source IP address (only if MAC protocol is set to IPv4). |
| **src-address6** (*IPv6 address*; Default: ) | Source IPv6 address (only if MAC protocol is set to IPv6). |
| **src-mac-address** (*MAC address*; Default: ) | Source MAC address. |
| **src-port** (*integer 0..65535*; Default: ) | Source port number or range (only for TCP or UDP protocols). |
| **stp-flags** (*topology-change \| topology-change-ack*; Default: ) | The BPDU (Bridge Protocol Data Unit) flags. Bridges exchange configuration messages named BPDU periodically for preventing loops<ul><li>topology-change - topology change flag is set when a bridge detects port state change, to force all other bridges to drop their host tables and recalculate network topology</li><li>topology-change-ack - topology change acknowledgment flag is sent in replies to the notification packets</li></ul> |
| **stp-forward-delay** (*integer 0..65535*; Default: ) | Forward delay timer. |
| **stp-hello-time** (*integer 0..65535*; Default: ) | STP hello packets time. |
| **stp-max-age** (*integer 0..65535*; Default: ) | Maximal STP message age. |
| **stp-msg-age** (*integer 0..65535*; Default: ) | STP message age. |
| **stp-port** (*integer 0..65535*; Default: ) | STP port identifier. |
| **stp-root-address** (*MAC address*; Default: ) | Root bridge MAC address. |
| **stp-root-cost** (*integer 0..65535*; Default: ) | Root bridge cost. |
| **stp-root-priority** (*integer 0..65535*; Default: ) | Root bridge priority. |
| **stp-sender-address** (*MAC address*; Default: ) | STP message sender MAC address. |
| **stp-sender-priority** (*integer 0..65535*; Default: ) | STP sender priority. |
| **stp-type** (*config \| tcn*; Default: ) | The BPDU type:<ul><li>config - configuration BPDU</li><li>tcn - topology change notification</li></ul> |
| **tls-host** (*string*; Default: ) | Allows matching https traffic based on TLS SNI hostname. Accepts [GLOB syntax](https://en.wikipedia.org/wiki/Glob_(programming)) for wildcard matching. Note that the matcher will not be able to match the hostname if the TLS handshake frame is fragmented into multiple TCP segments (packets). |
| **vlan-encap** (*802.2 \| arp \| ip \| ipv6 \| ipx \| length \| mpls-multicast \| mpls-unicast \| pppoe \| pppoe-discovery \| rarp \| vlan \| integer 0..65535 \| hex 0x0000-0xffff*; Default: ) | Matches the MAC protocol type encapsulated in the VLAN frame. |
| **vlan-id** (*integer 0..4095*; Default: ) | Matches the VLAN identifier field. |
| **vlan-priority** (*integer 0..7*; Default: ) | Matches the VLAN priority (priority code point) |

Footnotes:

- STP matchers are only valid if the destination MAC address is `01:80:C2:00:00:00/FF:FF:FF:FF:FF:FF` (Bridge Group address), also STP should be enabled.

- ARP matchers are only valid if mac-protocol is `arp` or `rarp`.

- VLAN matchers are only valid for `0x8100` or `0x88a8` ethernet protocols.

- IP or IPv6 related matchers are only valid if mac-protocol is either set to `ip` or `ipv6`.

- 802.3 matchers are only consulted if the actual frame is compliant with IEEE 802.2 and IEEE 802.3 standards. These matchers are ignored for other packets.

### Bridge Packet Filter

This section describes specific bridge filter options.

**Sub-menu:** `/interface/bridge/filter`

| Property | Description |
| :-- | :-- |
| **action** (*accept \| drop \| jump \| log \| mark-packet \| passthrough \| return \| set-priority*; Default: **accept**) | Action to take if the packet is matched by the rule:<ul><li>accept - accept the packet. No action, i.e., the packet is passed through without undertaking any action, and no more rules are processed in the relevant list/chain</li><li>drop - silently drop the packet (without sending the ICMP reject message)</li><li>jump - jump to the chain specified by the value of the jump-target argument</li><li>log - add a message to the system log containing the following data: in-interface, out-interface, src-mac, dst-mac, eth-proto, protocol, src-ip:port-&gt;dst-ip:port and length of the packet. After the packet is matched it is passed to the next rule in the list, similar to passthrough</li><li>mark - mark the packet to use the mark later</li><li>passthrough - ignore this rule and go on to the next one. Acts the same way as a disabled rule, except for the ability to count packets</li><li>return - return to the previous chain, from where the jump took place</li><li>set-priority - set priority specified by the new-priority parameter on the packets sent out through a link that is capable of transporting priority (VLAN or WMM-enabled wireless interface). <a href="/docs/bridging-and-switching/user-guides/wmm-and-vlan-priority" rel="nofollow">Read more</a></li></ul> |

### Bridge NAT

This section describes specific bridge NAT options.

**Sub-menu:** `/interface/bridge/nat`

| Property | Description |
| :-- | :-- |
| **action** (*accept \| drop \| jump \| mark-packet \| redirect \| set-priority \| arp-reply \| dst-nat \| log \| passthrough \| return \| src-nat*; Default: **accept**) | Action to take if the packet is matched by the rule:<ul><li>accept - accept the packet. No action, i.e., the packet is passed through without undertaking any action, and no more rules are processed in the relevant list/chain</li><li>arp-reply - send a reply to an ARP request (any other packets will be ignored by this rule) with the specified MAC address (only valid in dstnat chain)</li><li>drop - silently drop the packet (without sending the ICMP reject message)</li><li>dst-nat - change the destination MAC address of a packet (only valid in dstnat chain)</li><li>jump - jump to the chain specified by the value of the jump-target argument</li><li>log - log the packet</li><li>mark - mark the packet to use the mark later</li><li>passthrough - ignore this rule and go on to the next one. Acts the same way as a disabled rule, except for the ability to count packets</li><li>redirect - redirect the packet to the bridge itself (only valid in dstnat chain)</li><li>return - return to the previous chain, from where the jump took place</li><li>set-priority - set the priority specified by the new-priority parameter on the packets sent out through a link that is capable of transporting priority (VLAN or WMM-enabled wireless interface). <a href="/docs/bridging-and-switching/user-guides/wmm-and-vlan-priority" rel="nofollow">Read more</a></li><li>src-nat - change the source MAC address of a packet (only valid in srcnat chain)</li></ul> |
| **to-arp-reply-mac-address** (*MAC address*; Default: ) | Source MAC address to put in the Ethernet frame and the ARP payload, when `action=arp-reply` is selected |
| **to-dst-mac-address** (*MAC address*; Default: ) | Destination MAC address to put in Ethernet frames, when `action=dst-nat` is selected |
| **to-src-mac-address** (*MAC address*; Default: ) | Source MAC address to put in Ethernet frames, when `action=src-nat` is selected |

## See also

---

- [CRS1xx/2xx series switches](/docs/bridging-and-switching/crs1xx-and-2xx-series-switches)
- [Marvell Prestera switch chip features](/docs/bridging-and-switching/marvell-prestera-switch-chip-features)
- [Switch chip features](/docs/bridging-and-switching/switch-chip-features)
- [MTU on RouterBOARD](/docs/hardware/mtu-in-routeros)
- [Layer2 misconfiguration](/docs/bridging-and-switching/user-guides/layer2-misconfiguration)
- [Bridge VLAN Table](/docs/bridging-and-switching/user-guides/bridge-vlan-table)
