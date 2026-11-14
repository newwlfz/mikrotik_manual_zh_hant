---
sidebar_key: "cli-reference/cmr/client/pair"
sidebar_position: 2
title: "pair"
sidebar_label: 'pair'
source: https://manual.mikrotik.com/docs/cli-reference/cmr/client/pair
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## cmr/client/pair {#cmrclientpair}
**Conditions:** !smips
**型別：** Command

啟動與 CMR 伺服器的配對過程。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="username" typ="string" unset="1">CMR 伺服器使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string" unset="1">CMR 伺服器密碼。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="address (flags=46)">CMR 伺服器 IP 地址。</ArgTableRow>
<ArgTableRow arg="status" typ="string">配對狀態。</ArgTableRow>
</ArgTable>
