---
sidebar_key: "cli-reference/disk/btrfs/filesystem/remove-device"
sidebar_position: 4
title: "remove-device"
sidebar_label: 'remove-device'
source: https://manual.mikrotik.com/docs/cli-reference/disk/btrfs/filesystem/remove-device
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/btrfs/filesystem/remove-device {#diskbtrfsfilesystemremove-device}
**條件：** !smips
**系統能力：** storage
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum">要從檔案系統中移除的裝置的磁碟槽位，例如 `nvme9`。裝置上的資料會先遷移到其餘裝置；如果使用更少的裝置無法保持當前配置檔案，則移除失敗（例如當裝置數量降到兩個以下時，無法保持 `data,raid1`）。</ArgTableRow>
<ArgTableRow arg="device-id" typ="num">要移除的裝置的數字 ID（參見 [`filesystem`](./index.md) 中的 `dev-ids`）；當裝置缺失且不再有任何槽位時需要。</ArgTableRow>
</ArgTable>
