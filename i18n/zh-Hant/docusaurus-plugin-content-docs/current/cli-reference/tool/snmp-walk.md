---
sidebar_key: "cli-reference/tool/snmp-walk"
sidebar_position: 22
title: "snmp-walk"
sidebar_label: 'snmp-walk'
source: https://manual.mikrotik.com/docs/cli-reference/tool/snmp-walk
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## tool/snmp-walk {#toolsnmp-walk}
**型別：** 命令

透過重複的 GETNEXT 請求從 SNMP 代理檢索整個 OID 子樹的值——例如一次性獲取所有介面計數器，或獲取 MikroTik OID `1.3.6.1.4.1.14988` 下的所有內容。使用 `/tool/snmp-get` 讀取單個 OID。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="oid" typ="string">遍歷開始的 OID；代理會列出該子樹，例如介面表使用 `1.3.6.1.2.1.2`。</ArgTableRow>
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
