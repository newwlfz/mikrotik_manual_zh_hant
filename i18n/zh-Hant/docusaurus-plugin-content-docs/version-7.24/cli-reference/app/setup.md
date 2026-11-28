---
title: "setup"
source: https://manual.mikrotik.com/docs/7.24/cli-reference/app/setup
captured_at: '2026-11-28T10:19:39.818Z'
translated_at: "2026-11-28T11:05:16.851Z"
translation_provider: "opencode-go"
translation_model: "hy4-flash-free"
translation_source: "llm"
---

-----------

## app/setup 
**Syscap:** app
**套件:** container
**類型:** 指令

啟動設定精靈，自動化 App 系統的網路、儲存與登錄檔設定。

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="disk" typ="enum (none)">Selected storage disk for application installation</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none }">Selected LAN bridge interface for container networking</ArgTableRow>
<ArgTableRow arg="router-ip-alt" typ="alt { router-ip-enum: enum
, router-ip: ipAddr
 }">Manual IP address override for the RouterOS device</ArgTableRow>
</ArgTable>
