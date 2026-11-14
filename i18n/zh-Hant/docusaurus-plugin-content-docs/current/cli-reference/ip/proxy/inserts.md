---
sidebar_key: "cli-reference/ip/proxy/inserts"
sidebar_position: 7
title: "inserts"
sidebar_label: 'inserts'
source: https://manual.mikrotik.com/docs/cli-reference/ip/proxy/inserts
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/proxy/inserts {#ipproxyinserts}
**型別：** 設定目錄

代理寫入其快取的物件計數器。關於快取的概述，請參閱 [Web 代理](../../../network-management/proxy/web-proxy.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="successes" typ="num">已儲存在快取中的物件。</ArgTableRow>
<ArgTableRow arg="denied" typ="num">未儲存響應，因為 [`/ip/proxy/cache`](./cache/index.md) 中 `action=deny` 的規則匹配了該請求。</ArgTableRow>
<ArgTableRow arg="too-large" typ="num"></ArgTableRow>
<ArgTableRow arg="no-memory" typ="num"></ArgTableRow>
<ArgTableRow arg="errors" typ="num"></ArgTableRow>
</ArgTable>
