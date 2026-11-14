---
sidebar_key: "cli-reference/tool/calea"
sidebar_position: 3
title: "calea"
sidebar_label: "calea"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/tool/calea
captured_at: '2026-11-01T21:30:14+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/calea {#toolcalea}
**包：** calea
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="case-id" typ="num"></ArgTableRow>
<ArgTableRow arg="case-name" typ="string"></ArgTableRow>
<ArgTableRow arg="intercept-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="intercept-port" typ="num"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (pcap | limited) { pcap:0, limited:1 }"></ArgTableRow>
<ArgTableRow arg="file-root" typ="string"></ArgTableRow>
<ArgTableRow arg="pcap-file-stop-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="pcap-file-stop-size" typ="num"></ArgTableRow>
<ArgTableRow arg="pcap-file-stop-count" typ="num"></ArgTableRow>
<ArgTableRow arg="pcap-file-hash-method" typ="enum (none | md5 | sha1 | sha256) { none:0, md5:1, sha1:2, sha256:3 }"></ArgTableRow>
<ArgTableRow arg="limited-file-stop-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="limited-file-hash-method" typ="enum (none | md5 | sha1 | sha256) { none:0, md5:1, sha1:2, sha256:3 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="access-session-id" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
</ArgTable>
