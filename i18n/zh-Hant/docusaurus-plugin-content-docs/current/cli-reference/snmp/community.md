---
sidebar_key: "cli-reference/snmp/community"
sidebar_position: 1
title: "community"
sidebar_label: 'community'
source: https://manual.mikrotik.com/docs/cli-reference/snmp/community
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## snmp/community {#snmpcommunity}
**型別：** 目錄

`/snmp/community` 選單用於定義 SNMP 團體：每個團體可以讀取或寫入什麼內容、可以從哪些地址訪問，以及在何種安全級別下訪問。團體名稱在 SNMPv1 和 v2c 中用作密碼，在 SNMPv3 中用作安全名稱。與任何團體都不匹配的請求（名稱錯誤或源地址錯誤）完全不會收到回覆。有關代理設定，請參閱 [`/snmp`](./index.md) 參考文件；有關示例，請參閱 [SNMP 指南](../../diagnostics-monitoring-and-troubleshooting/snmp.md)。

<ArgTable c1="標誌" c2="名稱" c3="描述">
<ArgTableRow arg="*" typ="default">預設 community。路由器在建立時自帶一個 community `public`，可從任意地址讀取，直到你更改或刪除它。</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已停用的 community。已停用的 community 不應答請求；新建的 community 為啟用狀態。</ArgTableRow>
</ArgTable>

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="name" typ="string">community 的名稱。對於 SNMPv1 和 v2c，它隨每個封包以明文傳輸，起到密碼的作用；對於 SNMPv3，它是安全名。預設值：`public`。</ArgTableRow>
<ArgTableRow arg="addresses" typ="object { address: alt { ipv6: ip6Prefix
, ip: ipPrefix
 }
 }">允許使用此 community 的源地址或字首。來自其他任何地址的請求都得不到應答。預設值：`::/0`（任意地址）。</ArgTableRow>
<ArgTableRow arg="security" typ="enum (none | authorized | private) { none:0, authorized:1, private:2 }">
此 community 要求的安全級別。
- `none`（預設）- 不進行身份驗證也不加密（noAuthNoPriv）；僅憑 community 名稱即可獲得訪問許可權。
- `authorized` - 要求 SNMPv3 身份驗證（authNoPriv）；v1 和 v2c 請求不會得到應答。
- `private` - 要求 SNMPv3 身份驗證和加密（authPriv）；v1 和 v2c 請求不會得到應答。
</ArgTableRow>
<ArgTableRow arg="read-access" typ="bool">請求是否可以讀取 MIB 值。預設值：yes。</ArgTableRow>
<ArgTableRow arg="write-access" typ="bool">請求是否可以更改路由器：設定系統標識、執行指令碼和重啟。具有寫許可權的 community 是很強的憑據，因此請讓其名稱難以猜測，並讓 `addresses` 保持較窄的範圍。預設值：no。</ArgTableRow>
<ArgTableRow arg="denied-oids" typ="multi { array-id, oid: string
 }">此 community 無法讀取的 OID 或子樹。對列入黑名單的 OID 直接執行 GET 會返回 no-such-object，walk 會跳過被阻止的子樹，因此監控工具的輪詢不會失敗。多個 OID 可以逗號分隔列表的形式給出。該設定按 community 分別生效。預設值：empty（agent 實現的所有內容均可讀）。</ArgTableRow>
<ArgTableRow arg="authentication-protocol" typ="enum (MD5 | SHA1 | SHA256 | SHA384 | SHA512) { MD5:0, SHA1:1, SHA256:2, SHA384:3, SHA512:4 }">
當 `security=authorized` 或 `private` 時，SNMPv3 使用的認證協定；community 的所有用戶端都必須使用該協定。
- `MD5`（預設值）
- `SHA1`
- `SHA256`
- `SHA384`
- `SHA512`
</ArgTableRow>
<ArgTableRow arg="encryption-protocol" typ="enum (DES | AES)">
當 `security=private` 時，SNMPv3 使用的加密協定。
- `DES`（預設值）
- `AES` - AES-128，定義於 RFC 3826。
</ArgTableRow>
<ArgTableRow arg="authentication-password" typ="string">SNMPv3 認證密碼，至少 8 個字元。屬於敏感資訊；請參閱[包含敏感引數的選單列表](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)。</ArgTableRow>
<ArgTableRow arg="encryption-password" typ="string">SNMPv3 加密密碼，至少 8 個字元。屬於敏感資訊；請參閱[包含敏感引數的選單列表](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)。</ArgTableRow>
</ArgTable>
