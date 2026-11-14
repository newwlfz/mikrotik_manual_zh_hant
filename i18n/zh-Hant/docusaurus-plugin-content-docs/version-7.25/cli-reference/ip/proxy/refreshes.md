---
sidebar_key: "cli-reference/ip/proxy/refreshes"
sidebar_position: 10
title: "refreshes"
sidebar_label: 'refreshes'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/proxy/refreshes
captured_at: '2026-11-01T21:24:25+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/refreshes {#ipproxyrefreshes}
**型別：** 設定目錄

代理在響應用戶端之前與伺服器重新驗證過的快取物件的計數器。為了重新驗證物件，代理會發送帶有 `If-Modified-Since` 或 `If-None-Match` 的條件請求。每個計數器統計一種原因。有關快取的概述，請參見 [Web 代理](../../../network-management/proxy/web-proxy.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="url-requests" typ="num">URL 包含查詢字串的物件。代理會在每次請求時重新驗證它們。</ArgTableRow>
<ArgTableRow arg="request-max-age" typ="num"></ArgTableRow>
<ArgTableRow arg="expired" typ="num"></ArgTableRow>
<ArgTableRow arg="response-max-age" typ="num"></ArgTableRow>
<ArgTableRow arg="config-max-fresh" typ="num"></ArgTableRow>
<ArgTableRow arg="heuristic" typ="num"></ArgTableRow>
<ArgTableRow arg="other" typ="num">其他原因，例如物件具有 `ETag` 標頭但沒有 `Last-Modified` 標頭。</ArgTableRow>
</ArgTable>
