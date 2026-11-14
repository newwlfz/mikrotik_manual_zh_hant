---
sidebar_key: "cli-reference/disk/settings"
sidebar_position: 14
title: "settings"
sidebar_label: 'settings'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/disk/settings
captured_at: '2026-11-01T21:22:13+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## disk/settings {#disksettings}
**條件：** !smips
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="default-mount-point-template" typ="string">新磁碟和分割區在新增時用來代替其自身 `mount-point-template` 的掛載點模板。模板變數與磁碟項上的相同（`[slot]`、`[model]`、`[serial]`、`[fw-version]`、`[fs-label]`、`[fs-uuid]`、`[fs]`）。預設值：[slot]。</ArgTableRow>
<ArgTableRow arg="auto-smb-sharing" typ="bool">新磁碟或分割區是否會自動獲得 SMB 共享（參見 SMB 頁面）。之後格式化建立的新項也會獲得該共享，新的 `tmpfs` 資料夾同樣如此。某些路由器（例如 hAP ax²）的預設配置會將其設定為 `yes`，因此新磁碟和資料夾會在 LAN 上共享。預設值：no。</ArgTableRow>
<ArgTableRow arg="auto-smb-user" typ="enum">由 `auto-smb-sharing=yes` 建立的自動 SMB 共享的預設使用者。預設值：guest。</ArgTableRow>
<ArgTableRow arg="auto-media-sharing" typ="bool">新磁碟或分割區（包括新的 `tmpfs` 資料夾）是否會自動新增到 DLNA 媒體伺服器（`/ip/media`）。某些路由器（例如 hAP ax²）的預設配置會將其設定為 `yes`。預設值：no。</ArgTableRow>
<ArgTableRow arg="auto-media-interface" typ="iface_enum { none }">當 `auto-media-sharing=yes` 時，為新磁碟建立的動態 `/ip/media` 條目中使用的介面。某些路由器（例如 hAP ax²）的預設配置會將其設定為 `bridge`。預設值：none.</ArgTableRow>
</ArgTable>
