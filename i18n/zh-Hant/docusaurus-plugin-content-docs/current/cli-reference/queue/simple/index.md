---
sidebar_key: "cli-reference/queue/simple"
title: "simple"
sidebar_label: 'simple'
source: https://manual.mikrotik.com/docs/cli-reference/queue/simple
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## queue/simple {#queuesimple}
**型別：** 目錄

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">停用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">無效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="target" typ="object { target: alt { target-interface: iface_enum
, target-address: alt { ip-address: ipPrefix
, ipv6-address: ip6Prefix
 }
 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dst" typ="alt { ip-address: ipPrefix
, ipv6-address: ip6Prefix
, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum (none) { none:0 }"></ArgTableRow>
<ArgTableRow arg="packet-marks" typ="multi { array-id, packet-mark: enum
 }"></ArgTableRow>
<ArgTableRow arg="priority" typ="composite { upload-priority: num [1 .. 8]
, download-priority: num [1 .. 8]
 }"></ArgTableRow>
<ArgTableRow arg="queue" typ="composite { upload-queue: enum
, download-queue: enum
 }"></ArgTableRow>
<ArgTableRow arg="limit-at" typ="composite { upload-limit-at: num
, download-limit-at: num
 }"></ArgTableRow>
<ArgTableRow arg="max-limit" typ="composite { upload-max-limit: num
, download-max-limit: num
 }"></ArgTableRow>
<ArgTableRow arg="burst-limit" typ="composite { upload-burst-limit: num
, download-burst-limit: num
 }"></ArgTableRow>
<ArgTableRow arg="burst-threshold" typ="composite { upload-threshold: num
, download-threshold: num
 }"></ArgTableRow>
<ArgTableRow arg="burst-time" typ="composite { upload-burst-time: time
, download-burst-time: time
 }"></ArgTableRow>
<ArgTableRow arg="bucket-size" typ="composite { upload-bucket-size: num [ .. 10000]
, download-bucket-size: num [ .. 10000]
 }"></ArgTableRow>
<ArgTableRow arg="total-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="total-queue" typ="enum"></ArgTableRow>
<ArgTableRow arg="total-limit-at" typ="num"></ArgTableRow>
<ArgTableRow arg="total-max-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-time" typ="time"></ArgTableRow>
<ArgTableRow arg="total-bucket-size" typ="num"></ArgTableRow>
<ArgTableRow arg="time" typ="super { !
, start: time
, [end] -time
, [day] ,ubit (sun, mon, tue, wed, thu, fri, sat)
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="bytes" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="dropped" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-dropped" typ="num"></ArgTableRow>
<ArgTableRow arg="rate" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-rate" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-packet-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-packets" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-queued-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-bytes" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-queued-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-queues" typ="composite { upload: num
, download: num
 }"></ArgTableRow>
<ArgTableRow arg="total-pcq-queues" typ="num"></ArgTableRow>
</ArgTable>
