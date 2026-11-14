---
sidebar_key: "cli-reference/ip/settings"
sidebar_position: 21
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/cli-reference/ip/settings
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/settings {#ipsettings}
**型別：** 設定目錄

此選單允許你配置與 IPv4 和 IPv6 相關的各類核心及系統級網路引數。這些設定控制作業系統如何處理 IP 流量和網路通訊。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ip-forward" typ="bool">啟用或停用介面之間的封包轉發。會按照 [RFC 1812](https://tools.ietf.org/html/rfc1812) 中對路由器的規定，把所有配置引數重設為預設值。</ArgTableRow>
<ArgTableRow arg="send-redirects" typ="bool">傳送 ICMP 重定向。在路由器上啟用此項。</ArgTableRow>
<ArgTableRow arg="accept-source-route" typ="bool">接受帶有 SRR 選項的封包。接受源路由（SSRR/LSRR）封包是一種眾所周知的安全風險，除非安裝環境要求，否則應保持停用。</ArgTableRow>
<ArgTableRow arg="accept-redirects" typ="bool">接受 ICMP 重定向訊息。在主機上啟用，在路由器上停用。</ArgTableRow>
<ArgTableRow arg="secure-redirects" typ="bool">僅接受來自預設閘道器列表中所列閘道器的 ICMP 重定向訊息。</ArgTableRow>
<ArgTableRow arg="rp-filter" typ="enum (no | strict | loose) { no:0, strict:1, loose:2 }">
啟用或停用源地址驗證。
- `no` - 不驗證源地址。
- `strict` - [RFC 3704](https://tools.ietf.org/html/rfc3704) 中定義的嚴格反向路徑模式。每個傳入封包都會與 FIB 進行比對，如果該介面不是最佳反向路徑，則封包檢查失敗。預設情況下，檢查失敗的封包會被丟棄。
- `loose` - [RFC 3704](https://tools.ietf.org/html/rfc3704) 中定義的鬆散反向路徑模式。每個傳入封包的源地址都會與 FIB 進行比對，如果該源地址無法透過任何介面到達，則封包檢查失敗。

[RFC 3704](https://tools.ietf.org/html/rfc3704) 建議啟用 `strict` 模式，以防止 DDoS 攻擊中的 IP 欺騙。

如果使用非對稱路由、複雜路由或 VRRP，則 `strict` 模式會引發問題，此時應改為啟用 `loose` 模式。
</ArgTableRow>
<ArgTableRow arg="ipv4-multipath-hash-policy" typ="enum (l3 | l4 | l3-inner) { l3:0, l4:1, l3-inner:2 }">
用於 [ECMP](../../user-guides/routing-and-networking-protocols/routing-decision.md#multipath-ecmp-routes) 路由的 IPv4 雜湊策略。

- l3 - 對源 IP 地址和目標 IP 地址進行三層雜湊。
- l3-inner - 進行三層雜湊，如果存在內層三層頭部則對內層進行雜湊。
- l4 - 對源 IP 地址、目標 IP 地址、IP 協定、源埠和目標埠進行四層雜湊。

啟用 [L3 硬體解除安裝](../../bridging-and-switching/l3-hardware-offloading.md) 後，硬體轉發的 ECMP 使用交換晶片自身的雜湊掩碼，其中包含 TCP/UDP 的 L4 埠；配置的策略會被忽略。FastTrack 解除安裝的連線遵循核心 FIB 查詢，並可能選擇不同的下一跳。[FastPath](../../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path) 按 L3 快取路由。
</ArgTableRow>
<ArgTableRow arg="tcp-syncookies" typ="bool">當套接字的 SYN 積壓佇列溢位時傳送 syncookies。這有助於防止 SYN flood 攻擊。不過，syncookies 違反 TCP 協定，並且會阻止使用 TCP 擴充套件，這可能會降低某些服務（例如 SMTP 中繼）的效能。這種效能下降可能會被你那些正在聯絡你的用戶端和中繼所察覺。</ArgTableRow>
<ArgTableRow arg="tcp-timestamps" typ="enum (disabled | random-offset | enabled) { disabled:0, random-offset:1, enabled:2 }">啟用或停用 TCP 時間戳，或為 TCP 時間戳新增隨機偏移量（預設行為）。停用時間戳有助於降低效能驟降的峰值。</ArgTableRow>
<ArgTableRow arg="max-neighbor-entries" typ="num">
設定 Linux 的 `gc_thresh3`。即 ARP 表中允許的鄰居條目的最大數量。預設值取決於已安裝的記憶體容量。可以設定高於預設值的數值，但這會增加記憶體耗盡的風險。
特定記憶體容量對應的預設值：

- 64 MiB 時為 2048，
- 128 MiB 時為 4096，
- 256 MiB 時為 8192，
- 512 MiB 或更高時為 16384。

ARP 快取用於儲存 ARP 條目，如果其中某些條目不完整，它們可能會無限期地留在快取中。這種情況只會發生在快取中的條目數量少於允許的最大值四分之一時。這樣做的原因是，在 ARP 表尚未接近滿時，避免不必要地執行垃圾回收器。
</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="time">在所有使用 ARP 的介面上設定 Linux 的 `base_reachable_time`（`base_reachable_time_ms`）。ARP 條目的初始有效期是在發現鄰居之後，從區間 [`timeout/2 - 3*timeout/2`]（預設 15 秒到 45 秒）中選取的。可以使用字尾 ms、s、m、h、d 表示毫秒、秒、分鐘、小時或天。如果未設定字尾，則使用秒（s）。該引數表示：在這段時間內，如果沒有任何裝置與該特定 MAC/IP 通訊，一條有效的 ARP 記錄還會被視為完整多久。該引數並不表示 ARP 條目從 ARP 快取中被刪除的時間（參見 `max-neighbor-entries` 設定）。</ArgTableRow>
<ArgTableRow arg="icmp-rate-limit" typ="num">限制向特定目標傳送型別匹配 icmp-rate-mask 的 ICMP 封包的最大速率。值為 `0` 表示停用任何限制，其他值表示響應之間的最小間隔（毫秒）。</ArgTableRow>
<ArgTableRow arg="icmp-rate-mask" typ="num">受速率限制的 ICMP 型別的掩碼。更多資訊請參見 [Linux 手冊頁](http://man7.org/linux/man-pages/man7/icmp.7.html)。</ArgTableRow>
<ArgTableRow arg="icmp-errors-use-inbound-interface-address" typ="bool">啟用後，傳送 ICMP 錯誤訊息回覆時，源地址使用導致該錯誤的接收介面的主地址。適用於複雜的網路偵錯。</ArgTableRow>
<ArgTableRow arg="ipv4-high-fragment-thresh" typ="num">
設定核心可為所有分片重組佇列合計消耗的記憶體上限（單位：位元組，包含每個介面和每條流）。當快取使用的總記憶體達到此限制時，核心會開始丟棄新到達的分片，從而導致封包被丟棄。提高該限制可減少在高分片負載下（例如帶有 VPN 的高吞吐鏈路，或受 MTU 限制的路徑）發生丟包的可能性，但同時也會提高可被佔用的最大 RAM 容量。

預設值取決於已安裝的記憶體容量：

- 64 MiB RAM 時為 512 KiB，
- 128 MiB RAM 時為 1024 KiB，
- 256 MiB RAM 時為 2048 KiB，
- 512MiB RAM 時為 4096 KiB，
- 1 GiB RAM 時為 16 MiB，
- 2 GiB 或更高 RAM 時為 32 MiB。
</ArgTableRow>
<ArgTableRow arg="ipv4-fragment-time" typ="num">IPv4 分片在記憶體中保留的時間（秒）。</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">允許使用 [Fast Path](../../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path)</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="ipv4-fast-path-active" typ="bool">指示 fast-path 是否處於活動狀態。</ArgTableRow>
<ArgTableRow arg="ipv4-fast-path-packets" typ="num">經過 fast-path 處理的封包數量。</ArgTableRow>
<ArgTableRow arg="ipv4-fast-path-bytes" typ="num">經過 fast-path 處理的位元組數。</ArgTableRow>
<ArgTableRow arg="ipv4-fasttrack-active" typ="bool">指示 fasttrack 是否處於活動狀態。</ArgTableRow>
<ArgTableRow arg="ipv4-fasttrack-packets" typ="num">經過 fasttrack 處理的封包數量。</ArgTableRow>
<ArgTableRow arg="ipv4-fasttrack-bytes" typ="num">經過 fasttrack 處理的位元組數。</ArgTableRow>
</ArgTable>
