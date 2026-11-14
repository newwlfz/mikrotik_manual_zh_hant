---
sidebar_key: "cli-reference/snmp/send-trap"
sidebar_position: 2
title: "send-trap"
sidebar_label: 'send-trap'
source: https://manual.mikrotik.com/docs/cli-reference/snmp/send-trap
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## snmp/send-trap {#snmpsend-trap}
**型別：** 命令

`send-trap` 命令會立即向已配置的 trap 目標傳送一個 SNMP trap，這對於測試 trap 是否能到達採集器非常有用。該 trap 使用 SNMP 服務的 `trap-target`、`trap-community` 和 `trap-version` 設定（當 `trap-version=1` 時，它是經典的 v1 企業 trap；否則，它會在 MikroTik trap OID `1.3.6.1.4.1.14988.1.1.9.0.1` 下攜帶 OID 和值）。有關 trap 配置，請參閱 [SNMP 指南](../../diagnostics-monitoring-and-troubleshooting/snmp.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="oid" typ="string">trap 所報告物件的 OID。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (integer | string | nullobj | obj-id | ip-address | counter32 | timeticks | unsigned) { integer:0x02, string:0x04, nullobj:0x05, obj-id:0x06, ip-address:0x40, counter32:0x41, timeticks:0x43, unsigned:0x47 }">
值的 SNMP 型別。可接受的取值：
- `integer` - 有符號整數。
- `string` - 八位位元組串。
- `nullobj` - 一個 NULL 值。
- `obj-id` - 物件識別符號。
- `ip-address` - 一個 IP 地址。
- `counter32` - 一個 32 位計數器。
- `timeticks` - 以百分之一秒為單位的時間。
- `unsigned` - 無符號整數。
</ArgTableRow>
<ArgTableRow arg="value" typ="string">要傳送的值，採用所選 `type` 所要求的格式。</ArgTableRow>
</ArgTable>
