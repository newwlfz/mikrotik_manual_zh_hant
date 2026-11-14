---
sidebar_key: "cli-reference/system/package/update/index"
sidebar_position: 4
title: "update"
sidebar_label: "update"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/system/package/update
captured_at: '2026-11-01T21:29:59+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/package/update {#systempackageupdate}
**型別：** 設定目錄

管理 `check-for-updates` 通道並執行 RouterOS 升級。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="channel" typ="enum (long-term | stable | testing | development)">檢查新版本時使用的升級[通道](#channel)。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (https | http)">連線 MikroTik 下載伺服器所用的協定。僅當網路阻止 HTTPS 時才使用 `http`。建議使用 HTTPS。</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (no | yes | yes-without-crl)">是否以及如何驗證伺服器 SSL 證書。請始終使用 `yes` 以確保連線安全。</ArgTableRow>
<ArgTableRow arg="ip-version" typ="enum (auto | ipv4 | ipv6)">連線 MikroTik 下載伺服器時首選的 IP 版本。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="installed-version" typ="string">當前已安裝的 RouterOS 版本。</ArgTableRow>
<ArgTableRow arg="latest-version" typ="string">所選[通道](#channel)中可用的最新 RouterOS 版本。</ArgTableRow>
<ArgTableRow arg="status" typ="string">更新過程的當前狀態（例如 `New version is available`）。</ArgTableRow>
</ArgTable>
