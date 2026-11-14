---
sidebar_key: "cli-reference/disk/btrfs/filesystem/replace-device"
sidebar_position: 6
title: "replace-device"
sidebar_label: 'replace-device'
source: https://manual.mikrotik.com/docs/cli-reference/disk/btrfs/filesystem/replace-device
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/btrfs/filesystem/replace-device {#diskbtrfsfilesystemreplace-device}
**條件：** !smips
**系統能力：** storage
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="device-to-remove" typ="enum">Btrfs 檔案系統中要替換的裝置的磁碟槽位。</ArgTableRow>
<ArgTableRow arg="device-to-remove-id" typ="num">要替換的裝置的數字 ID；當裝置從系統中缺失（`I - MISSING-DEVS` 標誌）時，請使用此項代替 `device-to-remove`，因為此時槽位已不再可用。</ArgTableRow>
<ArgTableRow arg="device-to-add" typ="enum">接管被移除裝置資料的新裝置的磁碟槽位。</ArgTableRow>
</ArgTable>
