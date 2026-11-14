---
sidebar_key: "cli-reference/snmp"
title: "snmp"
sidebar_label: 'snmp'
source: https://manual.mikrotik.com/docs/cli-reference/snmp
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## snmp {#snmp}
**型別：** 設定目錄

`/snmp` 選單用於啟用 SNMP agent 並設定其常規行為：用於向 SNMPv3 用戶端標識路由器的 engine ID、它響應的地址和 VRF，以及 trap 的傳送方式。該 agent 預設處於關閉狀態。實際可讀取或寫入的 community 在 `/snmp/community` 選單中定義。有關配置示例，請參閱 [SNMP 指南](../../diagnostics-monitoring-and-troubleshooting/snmp.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="enabled" typ="bool">SNMP 代理是否應答查詢併發送 trap。預設值：no。</ArgTableRow>
<ArgTableRow arg="contact" typ="string">管理聯絡人資訊，任何收集器都可讀取。預設值：empty。</ArgTableRow>
<ArgTableRow arg="location" typ="string">管理位置資訊，任何收集器都可讀取。預設值：empty。</ArgTableRow>
<ArgTableRow arg="engine-id-suffix" typ="string">代理 SNMP 引擎 ID 的尾部。路由器用字首 `80003a8c04` 和以 ASCII 十六進位制寫出的給定值組成完整引擎 ID；例如字尾 `1234` 生成的引擎 ID 為 `80003a8c0431323334`。將字尾留空則使用自動生成的引擎 ID，該 ID 每臺路由器各不相同，且重啟後保持不變。預設值：empty。</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ip: ipAddr
, ip6: ip6Addr
 }">SNMP 訊息的源地址。設定該值後，代理只應答發往該地址的請求，且 IPv4 值會使其停止應答 IPv6 請求。預設值：`::` - 回覆來自接收請求的介面的地址。</ArgTableRow>
<ArgTableRow arg="trap-target" typ="object { ip-addresses: alt { ipv6: ip6Addr
, ip: ipAddr
 }
 }">接收 SNMP trap 的收集器地址列表；trap 會發送到每個地址的 UDP 埠 162。預設值：empty。</ArgTableRow>
<ArgTableRow arg="trap-community" typ="enum">用於傳送 trap 的 community。它必須存在於 `/snmp/community` 選單中；其安全級別決定 trap 的保護方式。預設值：`public`。</ArgTableRow>
<ArgTableRow arg="trap-version" typ="enum (1 | 2 | 3) { 1:0, 2:1, 3:3 }">
trap 協定的版本。
- `1`（預設）- SNMPv1 trap。
- `2` - SNMPv2c trap。
- `3` - SNMPv3 trap，使用 `trap-community` 的認證和加密。
</ArgTableRow>
<ArgTableRow arg="trap-generators" typ="multi { array-id, generator: enum
 }">
生成 trap 的事件；多個值可以組合。
- `interfaces` - 當介面狀態變化時生成 `linkDown`/`linkUp` trap；可用 `trap-interfaces` 縮小範圍。
- `start-trap` - 當 SNMP 服務啟動時生成 trap。
- `temp-exception`（預設） - 當 CPU 溫度達到 `/system/health` 閾值時生成 trap。
</ArgTableRow>
<ArgTableRow arg="trap-interfaces" typ="object { interface: iface_enum
 }">狀態變化會生成 `interfaces` trap 的介面列表；其他介面保持靜默。為空表示任意介面。預設值：empty.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">SNMP 代理執行所在的 VRF。到達其他 VRF 的請求不會收到回覆。預設值：`main`.</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="engine-id" typ="string">代理的完整 SNMP engine ID：字首 `80003a8c04` 後跟以 ASCII 十六進位制表示的 `engine-id-suffix` 值；當字尾為空時，為自動生成的 ID。SNMPv3 用戶端透過此值定址代理，並在每個請求中都包含它。</ArgTableRow>
</ArgTable>
