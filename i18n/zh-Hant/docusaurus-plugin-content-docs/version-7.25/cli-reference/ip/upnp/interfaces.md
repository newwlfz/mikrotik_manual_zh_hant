---
sidebar_key: "cli-reference/ip/upnp/interfaces"
sidebar_position: 1
title: "interfaces"
sidebar_label: 'interfaces'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/upnp/interfaces
captured_at: '2026-11-01T21:24:31+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/upnp/interfaces {#ipupnpinterfaces}
**型別：** 目錄

UPnP 服務的介面分配：哪個介面連線到 Internet（`external`），以及本地 UPnP 用戶端連線的是哪些介面（`internal`）。每個外部介面都會獲得自己的 WANConnectionDevice 服務，因此可以同時啟用多個外部介面。請參閱 [UPnP 指南頁面](../../../firewall-and-quality-of-service/upnp.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">disabled。UPnP 不使用該介面。新條目建立時即為 enabled。</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">動態</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">介面名稱。在 `internal` 介面上，控制服務監聽其地址的 TCP 埠 2828，並從該介面發出 SSDP 通告。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (external | internal) { external:1, internal:2 }" mandatory="1">
UPnP 介面角色：
- `external` - 面向網際網路的介面。用戶端埠對映的動態 dst-nat 規則會使用該介面作為 `in-interface`，並使用其地址作為 `dst-address` 來建立。
- `internal` - UPnP 用戶端所連線的本地介面。
</ArgTableRow>
<ArgTableRow arg="forced-ip" typ="super { forced-ip: ipAddr
 }">將此地址用作該介面的外部 IP 地址：它會在 `GetExternalIPAddress` 響應中報告給用戶端，並在動態 dst-nat 規則中用作 `dst-address`。當外部介面具有多個地址時設定。未設定時，使用該介面的主地址。</ArgTableRow>
</ArgTable>
