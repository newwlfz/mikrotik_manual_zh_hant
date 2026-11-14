---
sidebar_key: "cli-reference/ip/neighbor/lldp"
sidebar_position: 2
title: "lldp"
sidebar_label: 'lldp'
source: https://manual.mikrotik.com/docs/7.25/cli-reference/ip/neighbor/lldp
captured_at: '2026-11-01T21:24:18+08:00'
translated_at: "2026-11-11T16:56:12.375Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/neighbor/lldp {#ipneighborlldp}
**型別：** 目錄

此選單顯示從鄰居裝置接收到的詳細 LLDP 型別-長度-值（TLV）。

:::note
`lldpRemTable` SNMP 表僅報告透過 LLDP 發現的鄰居。僅由 CDP 或 MNDP 發現的條目會從 SNMP LLDP-MIB 中排除。
:::

示例輸出：

```ros
[admin@Switch] > /ip/neighbor/lldp/print
Columns: INTERFACE, ADDRESS4, ADDRESS6, MAC-ADDRESS, LLDP-CHASSIS-ID, LLDP-PORT-ID, LLDP-PORT-DESCRIPTION, LLDP-SYSTEM-NAME, LLDP-SYSTEM-DESCRIPTION
#  INTERFACE  ADDRESS4        ADDRESS6                   MAC-ADDRESS        LLDP-CHASSIS-ID    LLDP-PORT-ID  LLDP-PORT-DESCRIPTION  LLDP-SYSTEM-NAME  LLDP-SYSTEM-DESCRIPTION                                                     
0  ether2     192.168.88.128  fe80::f61e:57ff:fe13:d794  F4:1E:57:13:D7:94  F4:1E:57:13:D7:94  ether1        ether1                 Tested_CRS812     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS812-8DS-2DQ-2DDQ 
   bridge1                                                                                                                                                                                                                        
1  ether3     192.168.88.127  fe80::f61e:57ff:fe47:9255  F4:1E:57:47:92:55  F4:1E:57:47:92:55  ether1        ether1                 Tested_CRS520     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS520-4XS-16XQ     
   bridge1                                                                                                                                                                                                                        
2  ether4     192.168.88.9    fe80::1afd:74ff:fe81:9a    18:FD:74:81:00:9A  18:FD:74:81:00:86  ether1        ether1                 Tester6           MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CCR2216-1G-12XS-2XQ 
   bridge1                                                                                                                                                                                                                        
3  ether5     192.168.88.132  fe80::d601:c3ff:fe43:c035  D4:01:C3:43:C0:35  D4:01:C3:43:C0:35  ether1        ether1                 Tested_L009       MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 L009UiGS            
   bridge1                                                                                                                                                                                                                        
4  ether8     192.168.88.129  fe80::f61e:57ff:fec2:8a3d  F4:1E:57:C2:8A:3D  F4:1E:57:C2:8A:2B  ether17       ether17                Tested_CRS418     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS418-8P-8G-2S+    
   bridge1   
```

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="interface" typ="multi { interface: iface_enum
 }">發現該 LLDP 鄰居的介面。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { address4: ipAddr
, address6: ip6Addr
 }">LLDP 鄰居的 IPv4 或 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="address4" typ="ipAddr">LLDP 鄰居的 IPv4 地址。</ArgTableRow>
<ArgTableRow arg="address6" typ="ip6Addr">LLDP 鄰居的 IPv6 地址。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">LLDP 鄰居的 MAC 地址。</ArgTableRow>
<ArgTableRow arg="lldp-chassis-id-subtype" typ="enum (chassis-component | interface-alias | port-component | mac-address | network-address | interface-name | local) { chassis-component:1, interface-alias:2, port-component:3, mac-address:4, network-address:5, interface-name:6, local:7 }">LLDP 機箱 ID 的子型別。</ArgTableRow>
<ArgTableRow arg="lldp-chassis-id" typ="string">鄰居的 LLDP 機箱 ID。</ArgTableRow>
<ArgTableRow arg="lldp-port-id-subtype" typ="enum (interface-alias | port-component | mac-address | network-address | interface-name | agent-circuit-id | local) { interface-alias:1, port-component:2, mac-address:3, network-address:4, interface-name:5, agent-circuit-id:6, local:7 }">LLDP 埠 ID 的子型別。</ArgTableRow>
<ArgTableRow arg="lldp-port-id" typ="string">鄰居的 LLDP 埠 ID。</ArgTableRow>
<ArgTableRow arg="lldp-port-description" typ="string">鄰居的 LLDP 埠描述。</ArgTableRow>
<ArgTableRow arg="lldp-system-name" typ="string">鄰居的 LLDP 系統名稱（系統標識）。</ArgTableRow>
<ArgTableRow arg="lldp-system-description" typ="string">鄰居的 LLDP 系統描述。</ArgTableRow>
<ArgTableRow arg="lldp-ttl" typ="time">鄰居條目的 LLDP time-to-live 值。</ArgTableRow>
<ArgTableRow arg="lldp-system-caps" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)">鄰居的 LLDP 系統能力。</ArgTableRow>
<ArgTableRow arg="lldp-system-caps-enabled" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)">鄰居已啟用的 LLDP 系統能力。</ArgTableRow>
</ArgTable>
