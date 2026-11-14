---
sidebar_key: "cli-reference/ip/proxy/cache-contents"
sidebar_position: 3
title: "cache-contents"
sidebar_label: 'cache-contents'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/proxy/cache-contents
captured_at: '2026-11-01T21:24:20+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/cache-contents {#ipproxycache-contents}
**型別：** 目錄

Web 代理快取中的物件。刪除條目可使代理在下次請求時從伺服器獲取該物件。要清空整個快取，請使用 [`clear-cache`](./clear-cache.md)。有關快取的概述，請參閱 [Web 代理](../../../network-management/proxy/web-proxy.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="uri" typ="string">物件的 URL。</ArgTableRow>
<ArgTableRow arg="file-size" typ="num">物件的大小，單位為 KiB。</ArgTableRow>
<ArgTableRow arg="last-modified" typ="date">代理儲存物件的日期。它不是響應的 `Last-Modified` 標頭。</ArgTableRow>
<ArgTableRow arg="last-modified-time" typ="date">代理儲存物件的時間。</ArgTableRow>
<ArgTableRow arg="last-accessed" typ="date"></ArgTableRow>
<ArgTableRow arg="last-accessed-time" typ="date"></ArgTableRow>
</ArgTable>
