---
sidebar_key: "cli-reference/routing/rpki/index"
sidebar_position: 1
title: "rpki"
sidebar_label: 'rpki'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/routing/rpki
captured_at: '2026-11-01T21:25:19+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/rpki {#routingrpki}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="group" typ="enum">分配給資料庫的組。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">RTR 伺服器地址。</ArgTableRow>
<ArgTableRow arg="port" typ="num">RTR 伺服器埠。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">用於繫結連線的 VRF 表。</ArgTableRow>
<ArgTableRow arg="preference" typ="num" unset="1">當存在多個 RTR 源時，數字越大表示優先順序越高。如果未配置 preference，RouterOS 會優先選擇組內最低的遠端 IP。如果遠端 IP 相同，RouterOS 會優先選擇最低的遠端埠。</ArgTableRow>
<ArgTableRow arg="refresh-interval" typ="num" unset="1">輪詢驗證器以獲取最新資料的間隔時間（秒）。</ArgTableRow>
<ArgTableRow arg="retry-interval" typ="num" unset="1">從驗證器輪詢資料失敗後重試的間隔時間（秒）。</ArgTableRow>
<ArgTableRow arg="expire-interval" typ="num" unset="1">當未從驗證器收到有效更新時，已輪詢資料保持有效的間隔時間（秒）。</ArgTableRow>
</ArgTable>
