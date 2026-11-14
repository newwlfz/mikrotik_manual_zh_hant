---
sidebar_key: "cli-reference/ip/nat-pmp/interfaces"
sidebar_position: 1
title: "interfaces"
sidebar_label: 'interfaces'
source: https://manual.mikrotik.com/docs/cli-reference/ip/nat-pmp/interfaces
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/nat-pmp/interfaces {#ipnat-pmpinterfaces}
**型別：** 目錄

NAT-PMP 服務的介面分配：連線到 Internet 的介面（`external`）以及 NAT-PMP 用戶端所連線的介面（`internal`）。該列表只接受一個外部介面（`only one external interface can be added to the list`）。請參閱 [NAT-PMP 指南頁面](../../../firewall-and-quality-of-service/nat-pmp.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">disabled。該介面不由 NAT-PMP 使用。新建條目時處於 enabled 狀態。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">介面名稱。在 `internal` 介面上，服務監聽用戶端請求，並向組播組 224.0.0.1、UDP 埠 5350 傳送外部地址通告。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (external | internal)" mandatory="1">
NAT-PMP 介面角色：
- `external` - 面向 Internet 的介面。只允許一個外部介面。
- `internal` - NAT-PMP 用戶端所連線的本地介面。
</ArgTableRow>
<ArgTableRow arg="forced-ip" typ="super { forced-ip: ipAddr
 }">向用戶端報告此地址作為路由器的外部地址，而不是介面地址，例如當外部介面有多個地址時。</ArgTableRow>
</ArgTable>
