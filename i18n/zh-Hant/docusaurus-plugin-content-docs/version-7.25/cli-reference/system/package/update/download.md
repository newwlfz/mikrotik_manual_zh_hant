---
sidebar_key: "cli-reference/system/package/update/download"
sidebar_position: 3
title: "download"
sidebar_label: 'download'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/system/package/update/download
captured_at: '2026-11-01T21:25:38+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/package/update/download {#systempackageupdatedownload}
**型別：** 命令

下載最新的可用 RouterOS 軟體包，但不進行安裝。需要手動重啟才能應用更新。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="ignore-missing" typ="bool" unset="1">僅下載 RouterOS 主軟體包，省略缺失或未上傳的軟體包。</ArgTableRow>
</ArgTable>
