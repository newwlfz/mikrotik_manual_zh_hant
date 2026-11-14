---
sidebar_key: "cli-reference/ip/ipsec/mode-config"
sidebar_position: 5
title: "mode-config"
sidebar_label: 'mode-config'
source: https://manual.mikrotik.com/docs/cli-reference/ip/ipsec/mode-config
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/ipsec/mode-config {#ipipsecmode-config}
**型別：** 目錄

此選單配置 ISAKMP 和 IKEv2 配置屬性。

:::note
並非所有 IKE 實現都支援由 `split-include` 選項提供的多個拆分網路。
:::

:::note
如果 RouterOS 用戶端是發起方，它始終傳送 CISCO UNITY 擴充套件，並且 RouterOS 僅支援此擴充套件中的 split-include。
:::

:::note
同時支援 Cisco Unity Split DNS（屬性型別 28675）和 RFC8598（屬性型別 25）這兩個屬性，但 ROS 僅以 responder 身份響應這些屬性。
:::

:::note
不能同時使用 `system-dns` 和 `static-dns`；ROS 只能使用一個 DNS。
:::

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">該項是否為預設項。</ArgTableRow>
<ArgTableRow arg="R" typ="responder">該項是否充當 responder。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">模式配置條目名稱。</ArgTableRow>
<ArgTableRow arg="responder" typ="bool">指定該配置將作為 initiator（用戶端）還是 responder（伺服器）工作。initiator 將從 responder 請求 mode-config 引數。</ArgTableRow>
<ArgTableRow arg="system-dns" typ="bool">啟用此選項後，將從 /ip/dns 獲取 DNS 地址。</ArgTableRow>
<ArgTableRow arg="static-dns" typ="object { address: alt { address4: ipAddr
 }
 }">手動指定要傳送給用戶端的 DNS 伺服器 IP 地址。</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">要分配給對等體的地址。</ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (none) { none:-1 }">從該地址池中為對等體分配一個地址。</ArgTableRow>
<ArgTableRow arg="address-prefix-length" typ="num">所分配地址的掩碼。</ArgTableRow>
<ArgTableRow arg="split-include" typ="object { subnet: alt { subnet4: ipPrefix
 }
 }">採用 CIDR 格式的子網列表，這些子網將被隧道傳輸。子網將使用 CISCO UNITY 擴充套件傳送給對等體。遠端對等體將建立特定的動態策略。</ArgTableRow>
<ArgTableRow arg="split-dns" typ="multi { array-id, dns: string
 }">將使用 system-dns=yes 或 static-dns= 設定解析的 DNS 名稱列表。</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="enum ()">指定地址列表將生成動態源 NAT 規則。此引數僅在 responder=no 時可用。帶 NAT 的 roadWarrior 用戶端</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="enum ()">要為 initiator 新增到 srcnat 鏈的 conection-mark</ArgTableRow>
<ArgTableRow arg="use-responder-dns" typ="enum (no | yes | exclusively)">傳送的 DNS 伺服器是否應由 initiator 使用</ArgTableRow>
</ArgTable>
