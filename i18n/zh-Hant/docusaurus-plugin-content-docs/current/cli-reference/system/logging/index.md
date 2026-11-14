---
sidebar_key: "cli-reference/system/logging"
title: "logging"
sidebar_label: 'logging'
source: https://manual.mikrotik.com/docs/cli-reference/system/logging
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## system/logging {#systemlogging}
**型別：** 目錄

決定保留哪些日誌訊息以及將它們傳送到何處的規則。每條規則按主題選擇訊息，也可選地按正則表示式選擇訊息，並將它們傳遞給 [`/system/logging/action`](./action/index.md) 中的動作。預設規則將 `info`、`error` 和 `warning` 訊息傳遞給 `memory` 動作，將 `critical` 訊息傳遞給 `echo`；其他訊息（例如 `debug`）在規則要求之前不會被記錄。請參閱[日誌](../../../diagnostics-monitoring-and-troubleshooting/log/index.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="X" typ="disabled">規則已停用。</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">規則無效。</ArgTableRow>
<ArgTableRow arg="*" typ="default">四條預設規則之一：`info`、`error` 和 `warning` 傳送到 `memory`，`critical` 傳送到 `echo`。</ArgTableRow>
<ArgTableRow arg="Y" typ="managed"></ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="topics" typ="multi { array-id, array-id, topic: super { !
, topic: enum
 }
 }">
訊息為匹配而必須攜帶的主題。僅當訊息包含列出的每個主題時才會匹配：`topics=dhcp,debug` 匹配 DHCP 偵錯訊息，而不是所有 DHCP 訊息和所有偵錯訊息。要記錄多個主題，請為每個主題新增一條規則。沒有主題的規則會匹配所有訊息，包括偵錯訊息。

主題前的 `!` 會排除攜帶該主題的訊息，例如 `topics=ntp,debug,!packet` 會記錄 NTP 偵錯訊息但不包含封包轉儲。這些主題在[日誌](../../../diagnostics-monitoring-and-troubleshooting/log/index.md#topics)頁面中描述。路由器接受：`account`, `acme-client`, `amt`, `async`, `backup`, `bfd`, `bgp`, `bridge`, `calc`, `caps`, `certificate`, `clock`, `container`, `critical`, `ddns`, `debug`, `dhcp`, `discover`, `disk`, `dns`, `dot1x`, `dude`, `e-mail`, `error`, `event`, `evpn`, `fetch`, `firewall`, `gps`, `gsm`, `health`, `hotspot`, `igmp-proxy`, `info`, `interface`, `ipsec`, `iscsi`, `isdn`, `isis`, `kvm`, `l2tp`, `ldp`, `lora`, `lte`, `manager`, `mme`, `mpls`, `mqtt`, `mvrp`, `natpmp`, `netinstall`, `netwatch`, `ntp`, `ospf`, `ovpn`, `packet`, `pim`, `poe-in`, `poe-out`, `pon`, `ppp`, `pppoe`, `pptp`, `ptp`, `queue`, `radius`, `radvd`, `raw`, `read`, `rip`, `route`, `rpki`, `rproxy`, `rsvp`, `script`, `sertcp`, `simulator`, `smb`, `snmp`, `socksify`, `ssh`, `ssld`, `sstp`, `state`, `store`, `stp`, `system`, `telephony`, `tftp`, `timer`, `tr069`, `update`, `upnp`, `ups`, `vpls`, `vrrp`, `warning`, `watchdog`, `web-proxy`, `wiliot`, `wireguard`, `wireless`, `write`, `zerotier`。
</ArgTableRow>
<ArgTableRow arg="prefix" typ="string">新增在規則傳遞的每條訊息前面的文字，格式為 `<prefix>: <message>`。字首是儲存訊息和已傳送訊息的一部分。</ArgTableRow>
<ArgTableRow arg="regex" typ="string">與訊息文字以及其後的訊息額外欄位進行匹配的正則表示式。當它不匹配時，即使主題匹配，規則也不會傳遞該訊息。</ArgTableRow>
<ArgTableRow arg="action" typ="enum">從 [`/system/logging/action`](./action/index.md) 接收匹配訊息的動作。每條匹配的規則都會將訊息傳遞到自己的動作；當兩條規則將同一條訊息傳遞到同一個動作時，該動作只會接收一次。預設值：memory。</ArgTableRow>
</ArgTable>
