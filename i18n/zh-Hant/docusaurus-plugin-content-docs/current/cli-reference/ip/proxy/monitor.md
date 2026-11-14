---
sidebar_key: "cli-reference/ip/proxy/monitor"
sidebar_position: 9
title: "monitor"
sidebar_label: 'monitor'
source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy/monitor
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/monitor {#ipproxymonitor}
**型別：** 命令

顯示 Web 代理的狀態和計數器。新增 `once` 以進行單次讀取，例如 `/ip/proxy/monitor once`。有關概述，請參閱 [Web 代理](../../../network-management/proxy/web-proxy.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="enum (stopped | running | invalid-address | building-cache | passthrough) { stopped:0, running:1, invalid-address:4, building-cache:5 }">
代理的狀態，例如：
- `running` - 代理已啟用並處理請求。
- `stopped` - 代理已停用。
</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">自代理啟動以來經過的時間。</ArgTableRow>
<ArgTableRow arg="client-connections" typ="num">來自用戶端的已開啟連線數。</ArgTableRow>
<ArgTableRow arg="server-connections" typ="num">到伺服器的已開啟連線數。</ArgTableRow>
<ArgTableRow arg="requests" typ="num">代理收到的請求數。</ArgTableRow>
<ArgTableRow arg="hits" typ="num">由快取應答的請求數。</ArgTableRow>
<ArgTableRow arg="cache-used" typ="num">快取中物件的大小，單位為 KiB。</ArgTableRow>
<ArgTableRow arg="total-ram-used" typ="num"></ArgTableRow>
<ArgTableRow arg="received-from-servers" typ="num">從伺服器接收的資料量，單位為 KiB。</ArgTableRow>
<ArgTableRow arg="sent-to-clients" typ="num">傳送到用戶端的資料量，單位為 KiB。</ArgTableRow>
<ArgTableRow arg="hits-sent-to-clients" typ="num">從快取傳送到用戶端的資料量，單位為 KiB。</ArgTableRow>
</ArgTable>
