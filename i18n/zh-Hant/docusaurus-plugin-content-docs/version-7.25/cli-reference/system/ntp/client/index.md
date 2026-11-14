---
sidebar_key: "cli-reference/system/ntp/client/index"
sidebar_position: 1
title: "client"
sidebar_label: 'client'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/ntp/client
captured_at: '2026-11-01T21:25:32+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/ntp/client {#systemntpclient}
**型別：** 設定目錄

網路時間協定（NTP）用戶端設定。用戶端會將路由器時鐘與一個或多個 NTP 伺服器同步。靜態伺服器在 `servers` 中或 [servers](./servers.md) 列表中設定；當 DHCP 用戶端的 `use-peer-ntp` 啟用時，它會動態新增伺服器。請參閱 [NTP](../../../../system-information-and-utilities/ntp.md) 指南。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">啟用 NTP 用戶端。停用時，`status` 為 `stopped`。預設值：no。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (unicast | broadcast | multicast | manycast)">
用戶端從伺服器獲取時間的方式：
- `unicast`（預設）- 直接查詢每個已配置的伺服器。
- `broadcast` - 監聽本地網路中伺服器廣播的時間。
- `multicast` - 監聽本地網路中伺服器組播的時間。
- `manycast` - 透過向本地網路傳送 manycast 查詢來發現伺服器。
</ArgTableRow>
<ArgTableRow arg="servers" typ="multi { server-list: address (flags=46D)
 }">以空格分隔的 NTP 伺服器列表。接受 IPv4 和 IPv6 地址（在需要時可帶有 `@vrf` 或 `%interface` 字尾）以及域名，域名透過 `/ip/dns` 解析。此列表中的伺服器也會與動態條目一起顯示在 [servers](./servers.md) 列表中。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">用於與伺服器通訊的 VRF。預設值：main。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="freq-drift" typ="num">本地時鐘的估計頻率漂移，單位為 PPM。可透過 [`reset-freq-drift`](./reset-freq-drift.md) 重設。</ArgTableRow>
<ArgTableRow arg="status" typ="enum (stopped | waiting | synchronized | using-local-clock)">
當前用戶端狀態：
- `stopped` - 用戶端已停用。
- `waiting` - 尚無可用伺服器（無應答，或所有對等體均被拒絕）。
- `synchronized` - 時鐘已同步到 `synced-server`。
- `using-local-clock` - 使用本地時鐘作為參考（需要在 [`/system/ntp/server`](../server.md) 中設定 `use-local-clock=yes`）。
</ArgTableRow>
<ArgTableRow arg="synced-server" typ="address (flags=46D)">時鐘所同步到的伺服器地址。當本地時鐘作為參考時，為 `127.127.1.0`。</ArgTableRow>
<ArgTableRow arg="synced-stratum" typ="num">已同步來源的層級。主伺服器為 stratum 1；每經過一次同步層級加一。</ArgTableRow>
<ArgTableRow arg="system-offset" typ="num">本地時鐘與 NTP 來源之間的偏移量；使用 `print` 讀取時以毫秒顯示。</ArgTableRow>
</ArgTable>
