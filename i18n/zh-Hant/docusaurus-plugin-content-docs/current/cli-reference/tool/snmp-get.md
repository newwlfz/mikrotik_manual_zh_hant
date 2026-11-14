---
sidebar_key: "cli-reference/tool/snmp-get"
sidebar_position: 21
title: "snmp-get"
sidebar_label: 'snmp-get'
source: https://manual.mikrotik.com/docs/cli-reference/tool/snmp-get
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/snmp-get {#toolsnmp-get}
**型別：** 命令

從 SNMP 代理檢索一個 OID——例如測試路由器是否響應 SNMP 查詢，如 [SNMP 指南](../../diagnostics-monitoring-and-troubleshooting/snmp.md) 中所述。使用 `/tool/snmp-walk` 一次檢索整個子樹。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="oid" typ="object { oid: string
 }">要讀取的 OID，例如 `1.3.6.1.2.1.1.5.0`。</ArgTableRow>
<ArgTableRow arg="next" typ="bool">設定後，獲取 MIB 樹中緊隨給定 OID 之後的 OID（執行 GETNEXT 而非 GET）。</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">要查詢的 SNMP 代理地址。</ArgTableRow>
<ArgTableRow arg="port" typ="num">代理的 UDP 埠。預設值：`161`。</ArgTableRow>
<ArgTableRow arg="tries" typ="num">放棄前的嘗試次數。</ArgTableRow>
<ArgTableRow arg="try-timeout" typ="time">每次嘗試的超時時間。</ArgTableRow>
<ArgTableRow arg="version" typ="enum (1 | 2c | 3)">SNMP 協定版本：`1`、`2c` 或 `3`。</ArgTableRow>
<ArgTableRow arg="community" typ="string">團體名。對於 v1/v2c，該名稱就是密碼；對於 v3，它是攜帶匹配安全級別的團體名。</ArgTableRow>
<ArgTableRow arg="security" typ="enum (none | authorized | private) { none:0, authorized:1, private:2 }">安全級別，與團體名匹配：`none`、`authorized` 或 `private`。</ArgTableRow>
<ArgTableRow arg="authentication-password" typ="string">SNMPv3 認證密碼（至少 8 個字元）。</ArgTableRow>
<ArgTableRow arg="authentication-protocol" typ="enum (MD5 | SHA1 | SHA256 | SHA384 | SHA512)">SNMPv3 認證協定：`MD5`、`SHA1`、`SHA256`、`SHA384` 或 `SHA512`。</ArgTableRow>
<ArgTableRow arg="encryption-password" typ="string">SNMPv3 加密密碼（至少 8 個字元）。</ArgTableRow>
<ArgTableRow arg="encryption-protocol" typ="enum (DES | AES)">SNMPv3 加密協定：`DES` 或 `AES`。</ArgTableRow>
</ArgTable>

<ArgTable c1="只讀引數" c2="型別" c3="描述">
<ArgTableRow arg="oid" typ="string">代理返回值的 OID。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (null | integer | counter | gauge | timeticks | unsigned-integer | octet-string | opaque | object-id | ip-address | counter-64bit | no-such-object | no-such-instance | end-of-mib-view)">代理返回的值型別。</ArgTableRow>
<ArgTableRow arg="value" typ="string">代理返回的值。</ArgTableRow>
</ArgTable>
