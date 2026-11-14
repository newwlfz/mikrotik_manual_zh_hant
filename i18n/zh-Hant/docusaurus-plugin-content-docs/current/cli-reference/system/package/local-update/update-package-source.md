---
sidebar_key: "cli-reference/system/package/local-update/update-package-source"
sidebar_position: 5
title: "update-package-source"
sidebar_label: 'update-package-source'
source: https://manual.mikrotik.com/docs/cli-reference/system/package/local-update/update-package-source
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/package/local-update/update-package-source {#systempackagelocal-updateupdate-package-source}
**型別：**目錄

在此列表中定義要從中獲取軟體包的伺服器。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }" mandatory="1">本地軟體包伺服器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">用於訪問本地軟體包伺服器的使用者名稱。</ArgTableRow>
<ArgTableRow arg="password" typ="string" mandatory="1">用於訪問本地軟體包伺服器的密碼。</ArgTableRow>
</ArgTable>
