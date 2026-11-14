---
sidebar_key: "cli-reference/interface/sstp-server/server"
sidebar_position: 2
title: "server"
sidebar_label: "server"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/interface/sstp-server/server
captured_at: '2026-11-01T21:27:39+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## interface/sstp-server/server {#interfacesstp-serverserver}
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="max-mru" typ="num"></ArgTableRow>
<ArgTableRow arg="mrru" typ="num"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled) { disabled:0 }"></ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="verify-client-certificate" typ="bool"></ArgTableRow>
<ArgTableRow arg="pfs" typ="enum (no | yes | required) { no:0, yes:1, required:2 }"></ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2) { any:0, only-1.2:2 }"></ArgTableRow>
<ArgTableRow arg="ciphers" typ="ubit (aes256-sha, aes256-gcm-sha384)"></ArgTableRow>
</ArgTable>
