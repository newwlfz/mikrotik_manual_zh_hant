---
sidebar_key: "cli-reference/ip/dhcp-server/setup"
sidebar_position: 7
title: "setup"
sidebar_label: 'setup'
source: https://manual.mikrotik.com/docs/cli-reference/ip/dhcp-server/setup
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/dhcp-server/setup {#ipdhcp-serversetup}
**型別：** 命令

互動式設定，可一步建立 IP 池、DHCP 網路和 DHCP 伺服器。它會依次詢問每個值，並根據介面地址建議網路、閘道器和地址範圍，並根據伺服器預設值建議租約時間。有關示例，請參見 [DHCP 伺服器](../../../network-management/dhcp/server.md)。

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum">用於執行 DHCP 伺服器的介面。</ArgTableRow>
<ArgTableRow arg="network" typ="composite { address: ipAddr
, netmask: num [ .. 32]
 }">用於分配地址的網路，例如 `192.168.88.0/24`。根據介面地址建議。</ArgTableRow>
<ArgTableRow arg="gateway" typ="ipAddr">傳送給用戶端的預設閘道器。根據介面地址建議。</ArgTableRow>
<ArgTableRow arg="relay" typ="ipAddr">當用戶端不是直接連線時，DHCP 中繼的地址。</ArgTableRow>
<ArgTableRow arg="ippool" typ="multi { range: composite { min: ipAddr
, max: ipAddr
 }
 }">要分配的地址範圍，例如 `192.168.88.2-192.168.88.254`。該設定會使用此範圍建立 IP 池。</ArgTableRow>
<ArgTableRow arg="send-dns" typ="bool">DHCP 伺服器是否向用戶端傳送 DNS 伺服器。該設定要求輸入 `yes` 或 `no`。</ArgTableRow>
<ArgTableRow arg="dns-servers" typ="multi { address: ipAddr
 }">傳送給用戶端的 DNS 伺服器。留空則傳送路由器 DNS 設定（`/ip/dns`）中的 DNS 伺服器。</ArgTableRow>
<ArgTableRow arg="lease-time" typ="time">新伺服器的租約時間。建議值：1800s。</ArgTableRow>
</ArgTable>
