---
sidebar_key: "cli-reference/tool/ip-scan"
sidebar_position: 9
title: "ip-scan"
sidebar_label: 'ip-scan'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/tool/ip-scan
captured_at: '2026-11-01T21:25:56+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/ip-scan {#toolip-scan}
**條件：** !smips
**型別：** 命令

查詢網路中的主機，僅限 IPv4。使用 `address-range` 時，路由器會探測該範圍內的每個地址，並列出有應答的主機；僅使用 `interface` 時，它不傳送任何探測，而是列出它在該介面流量中看到的地址。掃描會一直執行，直到你停止它，或持續 `duration` 指定的時長。有關示例，請參閱 [IP 掃描](../../diagnostics-monitoring-and-troubleshooting/ip-scan.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="D" typ="dhcp">dhcp</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum">要監聽的介面。未指定 `address-range` 時，路由器不會向主機發送探測，而是列出它在該介面流量中看到的地址，包括來自其他子網的地址。</ArgTableRow>
<ArgTableRow arg="address-range" typ="ipRange">要掃描的地址：可以是 `192.168.88.0/24` 這樣的字首、`192.168.88.1-192.168.88.254` 這樣的範圍，或單個地址。在直連子網上，路由器透過 ARP 請求查詢主機；在其他網路上，則透過 ICMP 回顯請求查詢。同時指定 `interface` 時，路由器會掃描該範圍。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="address" typ="ipAddr">主機的地址。該範圍內路由器自身的地址也會列出。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">主機的 MAC 地址，來自其 ARP 應答。僅適用於直連子網上的主機。</ArgTableRow>
<ArgTableRow arg="time" typ="num">對 ICMP 回顯請求的響應時間。主機不響應 ping 時為空。</ArgTableRow>
<ArgTableRow arg="dns" typ="string">透過路由器的 DNS 解析器對該地址進行反向 DNS 查詢得到的名稱。</ArgTableRow>
<ArgTableRow arg="snmp" typ="string">主機的系統名稱（`sysName`），當其使用團體名 `public` 應答 SNMPv1 請求時顯示。</ArgTableRow>
<ArgTableRow arg="netbios" typ="string">主機的 NetBIOS 名稱，當其應答 UDP 埠 137 上的 NetBIOS 名稱查詢時顯示。</ArgTableRow>
</ArgTable>
