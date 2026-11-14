---
sidebar_key: "cli-reference/system/package/update"
title: "update"
sidebar_label: 'update'
source: https://manual.mikrotik.com/docs/cli-reference/system/package/update
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/package/update {#systempackageupdate}
**型別：** 設定目錄

管理 `check-for-updates` 通道並執行 RouterOS 升級。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="channel" typ="enum (long-term | stable | testing | development)">檢查新版本時要使用的升級 [channel](#channel)。</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (https | http)">連線 MikroTik 下載伺服器所使用的協定。僅當您的網路遮蔽 HTTPS 時才使用 `http`。建議使用 HTTPS。</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (no | yes | yes-without-crl)">是否以及如何驗證伺服器 SSL 證書。為確保連線安全，應始終使用 `yes`。可使用 `yes-without-crl` 跳過 CRL 驗證。</ArgTableRow>
<ArgTableRow arg="ip-version" typ="enum (auto | ipv4 | ipv6)">連線 MikroTik 下載伺服器時首選的 IP 版本。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="installed-version" typ="string">當前已安裝的 RouterOS 版本。</ArgTableRow>
<ArgTableRow arg="latest-version" typ="string">所選[通道](#channel)中可用的最新 RouterOS 版本。</ArgTableRow>
<ArgTableRow arg="status" typ="string">更新過程的當前狀態（例如 `New version is available`）。</ArgTableRow>
</ArgTable>
