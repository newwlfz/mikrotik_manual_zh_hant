---
title: "balance-start"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/disk/btrfs/filesystem/balance-start
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## disk/btrfs/filesystem/balance-start 
**條件：** !smips
**系統能力：** storage
**類型：** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="data-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)"></ArgTableRow>
<ArgTableRow arg="metadata-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)"></ArgTableRow>
<ArgTableRow arg="system-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)"></ArgTableRow>
<ArgTableRow arg="data-usage" typ="range"></ArgTableRow>
<ArgTableRow arg="metadata-usage" typ="range"></ArgTableRow>
<ArgTableRow arg="system-usage" typ="range"></ArgTableRow>
</ArgTable>
