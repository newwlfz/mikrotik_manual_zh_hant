---
sidebar_key: "cli-reference/disk/btrfs/filesystem/balance-start"
sidebar_position: 3
title: "balance-start"
sidebar_label: 'balance-start'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/disk/btrfs/filesystem/balance-start
captured_at: '2026-11-01T21:22:05+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/btrfs/filesystem/balance-start {#diskbtrfsfilesystembalance-start}
**條件：** !smips
**系統能力：** storage
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="data-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)">要將 `data` 塊轉換成的配置模式：`single` 將塊儲存一次（僅在單裝置時合理），`dup` 在同一裝置上儲存兩次，`raid*` 配置模式會將它們分佈到多個裝置上。在 [`add-device`](./add-device.md) 之後更改配置模式，可將單盤檔案系統變為 Btrfs RAID，例如 `data-profile=raid1`。</ArgTableRow>
<ArgTableRow arg="metadata-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)">要將 `meta`（元資料）塊轉換成的配置模式。與資料相比，元資料較小，因此 `dup`（單裝置時的預設值）或 `raid1` 是常見選擇。</ArgTableRow>
<ArgTableRow arg="system-profile" typ="enum (single | dup | raid0 | raid1 | raid1c3 | raid1c4 | raid10)">要將 `system` 塊轉換成的配置模式；請保持與 `metadata-profile` 相同。</ArgTableRow>
<ArgTableRow arg="data-usage" typ="range">僅遷移填充率至多為此百分比的資料塊，例如 `data-usage=50` 會跳過填充率超過一半的塊。值越低，平衡越快，但越不完整。</ArgTableRow>
<ArgTableRow arg="metadata-usage" typ="range">僅遷移填充率至多為此百分比的元資料塊。</ArgTableRow>
<ArgTableRow arg="system-usage" typ="range">僅遷移填充率至多為此百分比的系統塊。</ArgTableRow>
</ArgTable>
