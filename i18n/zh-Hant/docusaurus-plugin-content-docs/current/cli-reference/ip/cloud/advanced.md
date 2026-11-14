---
sidebar_key: "cli-reference/ip/cloud/advanced"
sidebar_position: 1
title: "advanced"
sidebar_label: 'advanced'
source: https://manual.mikrotik.com/docs/cli-reference/ip/cloud/advanced
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/cloud/advanced {#ipcloudadvanced}
**型別：** 設定目錄

高階 DDNS 設定。有關概述，請參閱 [DDNS](../../../network-management/cloud/index.md#ddns)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="use-local-address" typ="bool">DNS 名稱指向的是路由器的本地地址而非其公網地址。使用 `yes` 時，`dns-name` 會解析為路由器傳送請求時所用的地址，例如位於 NAT 後的私有地址，而 `public-address` 仍會顯示公網地址。預設：no。</ArgTableRow>
</ArgTable>
