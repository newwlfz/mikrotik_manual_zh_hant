---
sidebar_key: "cli-reference/disk/btrfs/filesystem/add-device"
sidebar_position: 1
title: "add-device"
sidebar_label: 'add-device'
source: https://manual.mikrotik.com/docs/cli-reference/disk/btrfs/filesystem/add-device
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/btrfs/filesystem/add-device {#diskbtrfsfilesystemadd-device}
**條件：** !smips
**系統能力：** storage
**型別：** 命令

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="device" typ="enum">要新增到 Btrfs 檔案系統的磁碟槽位，例如 `nvme9`。新增裝置後，使用所需的配置檔案執行 [`balance-start`](./balance-start.md)（例如 `data-profile=raid1`），才能真正將其用於儲存冗餘；否則該裝置只會列在 `devs` 下。</ArgTableRow>
</ArgTable>
