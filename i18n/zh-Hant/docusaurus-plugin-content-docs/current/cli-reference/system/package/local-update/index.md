---
sidebar_key: "cli-reference/system/package/local-update"
title: "local-update"
sidebar_label: 'local-update'
source: https://manual.mikrotik.com/docs/cli-reference/system/package/local-update
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/package/local-update {#systempackagelocal-update}
**型別：** 目錄

除了直接連線到 MikroTik 伺服器之外，您還可以將軟體包檔案上傳到您的一臺本地 RouterOS 裝置，並將其用作本地軟體包伺服器。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="download" typ="bool">是否從本地軟體包伺服器下載可用的軟體包。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="source" typ="alt { ipv6: ip6Addr
, ip: ipAddr
 }">本地軟體包伺服器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="name" typ="string">軟體包的名稱。</ArgTableRow>
<ArgTableRow arg="version" typ="string">軟體包的版本。</ArgTableRow>
<ArgTableRow arg="status" typ="enum (installed | downloaded | downloading | scheduled | available) { installed:0, downloaded:1, downloading:2, scheduled:3, available:4 }">軟體包的當前狀態。</ArgTableRow>
<ArgTableRow arg="completed" typ="num">下載完成百分比。</ArgTableRow>
</ArgTable>
