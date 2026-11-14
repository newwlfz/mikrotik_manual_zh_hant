---
sidebar_key: "cli-reference/ip/smb/index"
sidebar_position: 1
title: "smb"
sidebar_label: 'smb'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/smb
captured_at: '2026-11-01T21:24:26+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/smb {#ipsmb}
**條件：** !smips
**型別：** 設定目錄

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="enum (no | auto | yes)">
內建 SMB 伺服器是否執行：
- `no` - 伺服器已停用。
- `auto`（預設）- 當在 [`shares`](./shares.md) 中配置了第一個未停用的共享時，伺服器會自動啟動。
- `yes` - 伺服器已啟用。
</ArgTableRow>
<ArgTableRow arg="domain" typ="string">SMB 伺服器所屬的 Windows 工作組名稱。預設值：MSHOME。</ArgTableRow>
<ArgTableRow arg="comment" typ="string">SMB 伺服器的註釋。預設值：MikrotikSMB。</ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, interface: iface_enum { all:0 }
 }">SMB 服務監聽的介面。預設值：all。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="status" typ="string">SMB 伺服器的實際狀態，例如 `enabled`。</ArgTableRow>
</ArgTable>
