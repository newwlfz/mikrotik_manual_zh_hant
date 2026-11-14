---
sidebar_key: "cli-reference/ipv6/settings"
sidebar_position: 10
title: "settings"
sidebar_label: "settings"
description: "此選單允許您配置各種與 IPv6 相關的核心及系統級網路引數。這些設定控制作業系統如何處理 IP 流量和網路通訊。"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/ipv6/settings
captured_at: '2026-11-01T21:29:11+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ipv6/settings {#ipv6settings}
**型別：** 設定目錄

此選單允許你配置各種與 IPv6 相關的核心及系統級網路引數。這些設定控制作業系統如何處理 IP 流量和網路通訊。

:::note
更改 IPv6 設定不會動態移除現有的 SLAAC 配置，需要重啟路由器。

:::

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="disable-ipv6" typ="bool">在系統範圍內停用或啟用 IPv6。停用後，會阻止生成鏈路本地地址。</ArgTableRow>
<ArgTableRow arg="forward" typ="bool">啟用或停用介面之間的封包轉發。</ArgTableRow>
<ArgTableRow arg="multipath-hash-policy" typ="enum (l3 | l4 | l3-inner) { l3:0, l4:1, l3-inner:2 }">
為 [ECMP](../../user-guides/routing-and-networking-protocols/routing-decision.md#multipath-ecmp-routes) 路由指定 IPv6 雜湊策略：
- l3 - 對源 IP、目標 IP、流標籤和 IP 協定進行三層雜湊。
- l3-inner - 三層雜湊，或在可用時進行內層三層雜湊。
- l4 - 對源 IP、目標 IP、IP 協定、源埠和目標埠進行四層雜湊。

啟用 [L3 硬體解除安裝](../../bridging-and-switching/l3-hardware-offloading.md) 後，硬體轉發的 ECMP 使用交換晶片自身的雜湊掩碼，其中包含 TCP/UDP 的 L4 埠；配置的策略會被忽略。FastTrack 解除安裝的連線遵循核心 FIB 查詢，並可能選擇不同的下一跳。[FastPath](../../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path) 按 L3 快取路由。
</ArgTableRow>
<ArgTableRow arg="accept-redirects" typ="bool">接受或拒絕 ICMP 重定向訊息。在主機上啟用，在路由器上停用。</ArgTableRow>
<ArgTableRow arg="accept-router-advertisements" typ="enum (no | yes-if-forwarding-disabled | yes) { no:0, yes-if-forwarding-disabled:1, yes:2 }">控制是否接受路由器通告 (RA) 訊息。啟用後，路由器會使用 [無狀態地址配置](../../system-information-and-utilities/neighbor-discovery.md) 獲取地址。</ArgTableRow>
<ArgTableRow arg="accept-router-advertisements-on" typ="enum">指定在哪些介面上監聽傳入的路由器通告 (RA)。</ArgTableRow>
<ArgTableRow arg="disable-link-local-address" typ="bool">停用非 VPN 介面的自動鏈路本地地址生成。當你需要手動配置鏈路本地地址時使用此選項。</ArgTableRow>
<ArgTableRow arg="stale-neighbor-detect-interval" typ="num">設定系統檢查過期 IPv6 鄰居條目並探測這些條目以驗證可達性的間隔。</ArgTableRow>
<ArgTableRow arg="stale-neighbor-timeout" typ="num">超時持續時間，超過後過期 IPv6 鄰居條目將被清除。</ArgTableRow>
<ArgTableRow arg="min-neighbor-entries" typ="num">設定裝置必須為其分配記憶體的 IPv6 鄰居條目的最小數量。</ArgTableRow>
<ArgTableRow arg="soft-max-neighbor-entries" typ="num">設定系統應處理的 IPv6 鄰居條目的預期最大數量。</ArgTableRow>
<ArgTableRow arg="max-neighbor-entries" typ="num">
設定 IPv6 鄰居條目的最大數量。從 RouterOS 7.1 版本開始，預設值取決於已安裝的 RAM：
- 64 MiB 為 1024
- 128 MiB 為 2048
- 256 MiB 為 4096
- 512 MiB 為 8192
- 1024 MiB 或更高為 16384

將值設定為高於預設值會增加記憶體不足情況的風險。
</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">為 IPv6 流量啟用 [Fast Path](../../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path)。</ArgTableRow>
</ArgTable>
Fasttrack 和 fastpath 值自上次啟用該功能或自系統重啟以來累積計算。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="ipv6-fast-path-active" typ="bool">指示 IPv6 fast path 功能當前是否處於活動狀態。</ArgTableRow>
<ArgTableRow arg="ipv6-fast-path-packets" typ="num">透過 IPv6 fast path 處理的封包總數。</ArgTableRow>
<ArgTableRow arg="ipv6-fast-path-bytes" typ="num">透過 IPv6 fast path 處理的位元組總數。</ArgTableRow>
<ArgTableRow arg="ipv6-fasttrack-active" typ="bool">指示 IPv6 fasttrack 功能當前是否處於活動狀態。</ArgTableRow>
<ArgTableRow arg="ipv6-fasttrack-packets" typ="num">透過 IPv6 fasttrack 處理的封包總數。</ArgTableRow>
<ArgTableRow arg="ipv6-fasttrack-bytes" typ="num">透過 IPv6 fasttrack 處理的位元組總數。</ArgTableRow>
</ArgTable>
