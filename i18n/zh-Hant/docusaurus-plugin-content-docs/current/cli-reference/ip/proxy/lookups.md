---
sidebar_key: "cli-reference/ip/proxy/lookups"
sidebar_position: 8
title: "lookups"
sidebar_label: 'lookups'
source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy/lookups
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/lookups {#ipproxylookups}
**型別：** 設定目錄

代理在其快取中查詢的請求計數。有關快取的概述，請參閱 [Web 代理](../../../network-management/proxy/web-proxy.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="successes" typ="num">從快取中應答的請求數。</ArgTableRow>
<ArgTableRow arg="not-found" typ="num">針對不在快取中的物件的請求數。</ArgTableRow>
<ArgTableRow arg="non-cacheable" typ="num">由於其方法（例如 `POST` 和 `HEAD`）而不會被代理在快取中查詢的請求數。</ArgTableRow>
<ArgTableRow arg="denied" typ="num">匹配 [`/ip/proxy/cache`](./cache/index.md) 中 `action=deny` 規則的請求數。</ArgTableRow>
<ArgTableRow arg="expired" typ="num">在快取中找到物件、但代理又從伺服器重新獲取該物件的請求數。</ArgTableRow>
<ArgTableRow arg="no-expiration-info" typ="num"></ArgTableRow>
</ArgTable>
