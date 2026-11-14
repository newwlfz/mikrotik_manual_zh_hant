---
sidebar_key: "cli-reference/openflow"
title: "openflow"
sidebar_label: 'openflow'
source: https://manual.mikrotik.com/docs/cli-reference/openflow
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## openflow {#openflow}
**軟體包：** openflow
**型別：** 目錄

此選單列出 OpenFlow 用戶端的配置。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">條目的引用名稱</ArgTableRow>
<ArgTableRow arg="datapath-id" typ="super { number: num [0 .. 65535]
, [mac-address] /macAddr
 }">由兩部分（整數編號 [0..65535] 和 MAC 地址）組成、以斜槓分隔的 Datapath ID。</ArgTableRow>
<ArgTableRow arg="version" typ="enum (default | 1 | 1.3)">要使用的 OpenFlow 標準版本。</ArgTableRow>
<ArgTableRow arg="passive-port" typ="num">OpenFlow 代理用於監聽控制器連線的埠。</ArgTableRow>
<ArgTableRow arg="controllers" typ="object { contr: super { controler-protocol: enum (tcp | tls)
, [controller-address] /ip6Addr
, [controller-port] /num [1 .. 65535]
 }
 }">與控制器連線的配置。支援的協定為 **tcp** 和 **tls**。示例：`tcp/1.2.3.4/6654`。</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)" unset="1">[證書儲存中的證書](../../authentication-authorization-accounting/certificates.md)。與 `verify-peer` 引數一起使用。</ArgTableRow>
<ArgTableRow arg="verify-peer" typ="enum (required | none | if-cert-present)" unset="1">根據路由器的[證書儲存](../../authentication-authorization-accounting/certificates.md)驗證對端身份。</ArgTableRow>
<ArgTableRow arg="isolate-controllers" typ="bool" unset="1">是否將已配置的控制器彼此隔離。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="openflow-fast-path-packets" typ="num">傳送到快速路徑的封包數量。</ArgTableRow>
<ArgTableRow arg="openflow-fast-path-bytes" typ="num">傳送到快速路徑的位元組數。</ArgTableRow>
</ArgTable>
