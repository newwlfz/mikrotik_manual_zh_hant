---
sidebar_key: "cli-reference/disk/btrfs/filesystem/balance-start"
sidebar_position: 3
title: "balance-start"
sidebar_label: "balance-start"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/disk/btrfs/filesystem/balance-start
captured_at: '2026-11-01T21:26:41+08:00'
translated_at: "2026-11-11T16:55:57.729Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/btrfs/filesystem/balance-start {#diskbtrfsfilesystembalance-start}
**條件：** !smips
**系統能力：** storage
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="data-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)"></ArgTableRow>
<ArgTableRow arg="metadata-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)"></ArgTableRow>
<ArgTableRow arg="system-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)"></ArgTableRow>
<ArgTableRow arg="data-usage" typ="range"></ArgTableRow>
<ArgTableRow arg="metadata-usage" typ="range"></ArgTableRow>
<ArgTableRow arg="system-usage" typ="range"></ArgTableRow>
</ArgTable>
