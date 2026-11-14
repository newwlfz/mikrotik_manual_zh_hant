---
sidebar_key: "cli-reference/routing/rip/keys"
sidebar_position: 4
title: "keys"
sidebar_label: 'keys'
source: https://manual.mikrotik.com/docs/cli-reference/routing/rip/keys
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## routing/rip/keys {#routingripkeys}
**型別：** 目錄

MD5 認證金鑰鏈。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="chain" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key-id" typ="num" mandatory="1">金鑰識別符號。此編號會包含在 MD5 認證的 RIP 訊息中，並決定使用哪個金鑰來檢查特定訊息的認證。</ArgTableRow>
<ArgTableRow arg="key" typ="string" mandatory="1">認證金鑰。最大長度 16 個字元</ArgTableRow>
<ArgTableRow arg="valid-from" typ="date">金鑰從該日期和時間起有效。</ArgTableRow>
<ArgTableRow arg="valid-till" typ="date">金鑰有效期至該日期和時間。</ArgTableRow>
</ArgTable>
