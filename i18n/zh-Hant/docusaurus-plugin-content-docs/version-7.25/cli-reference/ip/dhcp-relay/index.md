---
sidebar_key: "cli-reference/ip/dhcp-relay/index"
sidebar_position: 1
title: "dhcp-relay"
sidebar_label: 'dhcp-relay'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/dhcp-relay
captured_at: '2026-11-01T21:23:50+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-relay {#ipdhcp-relay}
**型別：** 目錄

DHCP 中繼會把其介面上用戶端的 DHCP 請求轉發到其他網路中的 DHCP 伺服器，並將伺服器回覆傳回用戶端。新建中繼預設處於停用狀態；新增後請啟用。有關概述和示例，請參見 [DHCP 中繼](../../../network-management/dhcp/relay.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">中繼已停用。新建中繼預設處於停用狀態。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">中繼配置無效。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">中繼的名稱。</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">中繼在該介面上監聽來自用戶端的 DHCP 請求。</ArgTableRow>
<ArgTableRow arg="dhcp-server-vrf" typ="enum">用於訪問 DHCP 伺服器的 VRF。當它與 `interface` 的 VRF 不同時，伺服器傳送到 `local-address` 的回覆必須被引入此 VRF，例如透過 dst-nat 規則。預設值：main。</ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="multi { address: ipAddr
 }" mandatory="1">要將請求轉發到的 DHCP 伺服器。中繼會將每個請求轉發給所有這些伺服器。</ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { const: enum (none) { none:0 }
, time: time
 }">請求要被轉發時，seconds-elapsed 欄位（`secs`）必須達到的最小值，因此中繼只會轉發已經嘗試了該時長的用戶端。使用 `none` 時，所有請求都會被轉發。預設值：none。</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">中繼寫入轉發請求的閘道器地址欄位（`giaddr`）中的地址。DHCP 伺服器會將回復發送到此地址，並透過其 `relay` 屬性選擇伺服器。使用 `0.0.0.0` 時，會使用 `interface` 的一個地址。預設值：0.0.0.0。</ArgTableRow>
<ArgTableRow arg="add-relay-info" typ="bool">是否向轉發的請求新增中繼代理資訊（option 82）。circuit ID 為 `interface` 的 MAC 地址，remote ID 為用戶端的 MAC 地址；如果設定了 `relay-info-remote-id`，則為該值。預設值：no。</ArgTableRow>
<ArgTableRow arg="relay-info-remote-id" typ="string">作為 option 82 中的 remote ID 傳送的文字，用來代替用戶端的 MAC 地址。僅在 `add-relay-info=yes` 時使用。</ArgTableRow>
<ArgTableRow arg="local-address-as-src-ip" typ="bool">是否從 `local-address` 而不是從通向伺服器的介面地址傳送轉發的請求。預設值：no。</ArgTableRow>
</ArgTable>
